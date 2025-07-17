from __future__ import absolute_import, annotations, division, print_function

from collections import abc
import argparse
import copy
import fnmatch
import importlib
import inspect
import logging
import os
import re
import types
from typing import Any, Iterable

import mypy.stubgen
import mypy.stubgenc
from mypy.stubdoc import ArgSig, FunctionSig
from mypy.stubgenc import DocstringSignatureGenerator, SignatureGenerator
from mypy.stubutil import ClassInfo, FunctionContext

import stubgenlib.moduleinspect
from stubgenlib.siggen import (
    AdvancedSigMatcher,
    AdvancedSignatureGenerator,
)
from stubgenlib.stubgen.delegate import GeneratorDelegate
from stubgenlib.utils import add_positional_only_args

stubgenlib.moduleinspect.patch()


_MAYA_VERSION = os.getenv("MAYA_VERSION", "2025")
_FlagsType = Iterable[tuple[str, "pymel.internal.cmdcache.flag_info"]]

_API_DOCTSTRING_BLOCK_EXPRESSION = re.compile(
    r"""
    (?:
        \s* \* .+                   # Find the start of a `" * foo (bar)"` line.
        (?:
            \n(?:\ {4,}|\t)\ .*     # Check for indented continuation lines
        )*                          # Allow 0+ continuation lines, if any
        (?:\n|$)                    # Stop checking for blocks at these terminator(s)
    )+
    """,
    re.VERBOSE | re.MULTILINE,
)

_API_DOCSTRING_TYPE_EXPRESSION = re.compile(
    # This expression grabs the `"* foo (bar)"` portions of a Maya-API docstring
    #
    # Example: `help(OpenMaya.MDataBlock.inputValue)`
    #
    # ```
    # ...
    #
    # * plug (MPlug) - the plug whose data you wish to access
    # * attribute (MObject) - the attribute of the node that you want to access
    # ```
    #
    r"""
    ^\s*\*\s+                      # A typical line beginning

    (?P<name>\w+)

    .*                            # Sometimes there's little notes, omit them.
                                  # e.g. `" * foo [OUT] (MPoint)"`.
                                  # See `help(maya.api.OpenMaya.MPxSurfaceShape.pointAtParm)`
                                  # for an example

    \((?P<type>[^)]+)\)
    """,
    re.VERBOSE | re.MULTILINE,
)

_NAMESPACE_SEPARATOR = "."
_UNKNOWN_TYPE = "Incomplete"

_LOGGER = logging.getLogger(__name__)


def _is_protected_module(name: str) -> bool:
    """Check if module `name` is protected or private.

    Args:
        name: Some module namespace. e.g. `"maya.api._OpenMaya_py2"`.

    Returns:
        If any section of the import is private / protected, return `True`.

    """
    return any(part for part in name.split(_NAMESPACE_SEPARATOR) if part.startswith("_"))


def _get_fixed_type_name(name: str) -> str:
    """Replace Autodesk's raw, weird `name` with a real Python type.

    Sometimes the Maya documentation will write `"float*"` instead of
    `"list[float]"` or `"seq of ints"` instead of `"list[int]"` or `"string"`
    instead of `"str"`. This function catches those cases.

    Args:
        name: Some raw Autodesk-docstring-provided type name.

    Returns:
        A known Python type, if any.

    """
    if name.lower().endswith(" constant"):
        # NOTE: This is the only case that we can see currently. Maybe we would
        # want to just make an exception for this one case instead?
        #
        # Example: `help(maya.api.OpenMaya.MItMeshEdge.center)`
        #
        # ...
        # * space (MSpace constant) - The  transformation space
        #
        name = name[:-1 * len(" constant")]

    return name


def _fix_type_if_needed(type_: str) -> str:
    """Try to split and enrich `type_`, if needed.

    Example:
        >>> _fix_type_if_needed("str or int")   # "int | str"
        >>> _fix_type_if_needed("0 or 1")   # "Literal[0] | Literal[1]"

    Args:
        type_: Some type or multiple types to split out.

    Returns:
        A mypy-compatible type-hint to represent `type_`.

    """
    cleaned: list[str] = []

    for part in re.split(r"\s+or\s+", type_):
        if stripped := part.strip():
            if stripped.isdigit():
                stripped = f"Literal[{stripped}]"

            cleaned.append(stripped)

    return " | ".join(cleaned)


def _strip_arguments(omit: set[str], sigs: Iterable[FunctionSig]) -> list[FunctionSig]:
    """Remove any argument that matches `omit` from `sigs`.

    Args:
        sigs: All of the callable function signatures to return as a new copy.
        omit: The function signature argument(s) to omit.

    Returns:
        All-new copies of `sigs` but with `omit` excluded.
    """
    output: list[FunctionSig] = []

    for signature in sigs:
        args = [arg for arg in signature.args if arg.name not in omit]
        output.append(
            FunctionSig(
                name=signature.name,
                args=args,
                ret_type=signature.ret_type,
                type_args=signature.type_args,
            )
        )

    return output


def flag_has_mode(flag_info, mode):
    return mode in flag_info.get("modes", [])


class MayaCmdAdvSignatureGenerator(AdvancedSignatureGenerator):
    sig_matcher = AdvancedSigMatcher(
        # Override entire function signature:
        # This is particularly useful for creating multiple overloads where the return
        # type varies based on the args.
        signature_overrides={
            "maya.cmds.connectionInfo": [
                # NOTE: These are all known possible signatures for `connectionInfo`
                "(attribute: str, destinationFromSource: Literal[True]) -> list[str]",
                "(attribute: str, getExactDestination: Literal[True]) -> str",
                "(attribute: str, getLockedAncestor: Literal[True]) -> str",
                "(attribute: str, getSource: Literal[True]) -> str",
                "(attribute: str, isDestination: Literal[True]) -> bool",
                "(attribute: str, isExactDestination: Literal[True]) -> bool",
                "(attribute: str, isExactSource: Literal[True]) -> bool",
                "(attribute: str, isLocked: Literal[True]) -> bool",
                "(attribute: str, isSource: Literal[True]) -> bool",
                "(attribute: str, sourceFromDestination: Literal[True]) -> str",
            ],
            "maya.cmds.referenceQuery": [
                # Using **kwargs here because I'm too lazy to map out all of the valid combinations
                #  of secondary flags.
                # str results
                "(*args, filename: Literal[True], **kwargs) -> str",
                "(*args, referenceNode: Literal[True], **kwargs) -> str",
                "(*args, parentNamespace: Literal[True], **kwargs) -> str",
                "(*args, namespace: Literal[True], **kwargs) -> str",
                # list[str] results
                "(*args, nodes: Literal[True], **kwargs) -> list[str]",
                "(*args, editAttrs: Literal[True], **kwargs) -> list[str]",
                "(*args, editNodes: Literal[True], **kwargs) -> list[str]",
                "(*args, editStrings: Literal[True], **kwargs) -> list[str]",
                # bool results. (actually ints)
                "(*args, isNodeReferenced: Literal[True], **kwargs) -> bool",
                "(*args, isExportEdits: Literal[True], **kwargs) -> bool",
                "(*args, isLoaded: Literal[True], **kwargs) -> bool",
                "(*args, isPreviewOnly: Literal[True], **kwargs) -> bool",
            ]
            # "maya.cmds.ls": [
            #     # "(*args, lights: Literal[True] = True, **kwargs) -> str",
            #     # "(*args, whatever: Literal[True] = True, **kwargs) -> str",
            # ],
        },
        # Override argument types
        #   dict of (name_pattern, arg, type) to arg_type
        #   type can be str | re.Pattern
        arg_type_overrides={},
        # Override result types
        #   dict of (name_pattern, type) to result_type
        #   e.g. ("*", "Buffer"): "numpy.ndarray"
        result_type_overrides={
            ("maya.cmds.connectAttr", "*"): "None",
            ("maya.cmds.createNode", "*"): "str",
            ("maya.cmds.disconnectAttr", "*"): "None",
            ("maya.cmds.listAnimatable", "*"): "list[str]",
            ("maya.cmds.listAttr", "*"): "list[str] | None",
            ("maya.cmds.listConnections", "*"): "list[str] | None",
            ("maya.cmds.listHistory", "*"): "list[str]",
            ("maya.cmds.listRelatives", "*"): "list[str] | None",
            ("maya.cmds.listSets", "*"): "list[str] | None",
            ("maya.cmds.list*", "*"): "list[str] | None",
            ("maya.cmds.loadPlugin", "*"): "None",
            ("maya.cmds.ls", "*"): "list[str]",
            ("maya.cmds.objExists", "*"): "bool",
            ("maya.cmds.rename", "*"): "None",
            ("maya.cmds.setAttr", "*"): "None",
            ("maya.cmds.setKeyframe", "*"): "None",
            ("maya.cmds.undo", "*"): "None",
            ("maya.cmds.unloadPlugin", "*"): "None",

            # NOTE: `maya.cmds.nodeType` has some flags that look like they
            # might return bool, such as `isTypeName`. They do not. They always
            # return a string.
            #
            ("maya.cmds.nodeType", "*"): "str",
        },
        # Override property types
        #   dict of (name_pattern, type) to result_type
        #   e.g. ("*", "Buffer"): "numpy.ndarray"
        property_type_overrides={},
        # Types that have implicit alternatives.
        #   dict of type_str to list of types that can be used instead
        #   e.g. "PySide2.QtGui.QKeySequence": ["str"],
        # converts any matching argument to a union of the supported types
        implicit_arg_types={},
    )


class _ApiDocstringGenerator(DocstringSignatureGenerator):
    """Parse Maya docstrings for function signature details.

    The Maya Python 2.0 API may have a docstring like this:

    `help(maya.api.OpenMaya.MDataBlock.inputValue)`

    ```
    Help on method_descriptor:

    inputValue(...)
        inputValue(plug) -> MDataHandle
        inputValue(attribute) -> MDataHandle

        Gets a handle to this data block ...

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute of the node that you want to access
    ```

    The top portion are the overloads and the bottom portions are the argument
    + types. The base class, `DocstringSignatureGenerator` already does a good
    job finding the signatures. But the bottom portion is where all the types
    are and is also what this subclass focuses on parsing.

    Important:
        This class will usually not work as expected for Maya OpenMaya 1.0 API
        because their docstrings lack the details (we can't parse what we don't have).

    """

    sig_matcher = AdvancedSigMatcher(
        # Override entire function signature:
        signature_overrides={},
        # Override argument types
        #   dict of (name_pattern, arg, type) to arg_type
        #   type can be str | re.Pattern
        arg_type_overrides={
            ("*", "*", "Bool"): "bool",
            ("*", "*", "MString"): "str",  # NOTE: This may be too aggressive but is probably okay.
            ("*", "*", "string"): "str",
            ("*", "*", "string"): "str",
            ("*", "*", "unicodestring"): "str",
            ("*", "*", "unsigned char*"): "list[bytes]",
            ("*", "*", "unsigned int"): "int",
            ("*", "*", r"float\*"): "MFloatArray | list[float]",
            ("*", "colorSet", "*"): "str",
            ("*", "int", "*"): "int",
            ("*", "string", "*"): "str",
            ("*", "unicodestring", "*"): "str",
            ("*", "uvSet", "*"): "str",
            ("maya.api.OpenMaya.*", "space", "*"): "MSpace",
            ("maya.api.OpenMaya.MFnMesh.*", "modifier", "*"): "MDGModifier",
        },
        # Override result types
        #   dict of (name_pattern, type) to result_type
        #   e.g. ("*", "Buffer"): "numpy.ndarray"
        result_type_overrides={
            ("*", "Bool"): "bool",
            ("*", "Integer"): "int",
            ("*", "MString"): "str",  # NOTE: This may be too aggressive but is probably okay.
            ("*", "double"): "float",
            ("*", "integer"): "int",
            ("*", "long"): "float",
            ("*", "self"): "Self",
            ("*", "string"): "str",
            ("*", "unicodestring"): "str",
            ("*", "unsigned int"): "int",
            ("*", "unsignedint"): "int",
        },
        # Override property types
        #   dict of (name_pattern, type) to result_type
        #   e.g. ("*", "Buffer"): "numpy.ndarray"
        property_type_overrides={},
        # Types that have implicit alternatives.
        #   dict of type_str to list of types that can be used instead
        #   e.g. "PySide2.QtGui.QKeySequence": ["str"],
        # converts any matching argument to a union of the supported types
        implicit_arg_types={},
    )

    def _get_fixed_arg_type_name(
        self,
        arg: ArgSig,
        context: str,
        options: abc.MutableMapping[str, str],
    ) -> str | None:
        """Suggest a new data type for `arg`, if needed.

        Args:
            arg:
                Some argument from some function to check.
            context:
                The fully-qualified function / method name.
                e.g. `"maya.api.OpenMaya.FooClass.barMethod"`.
            options:
                Extra fallback argument types to choose from.

        Returns:
            The found type name.

        """
        type_ = arg.type or options.get(arg.name)

        if type_:
            type_ = _get_fixed_type_name(type_)

        match = self.sig_matcher.find_arg_match(
            context, arg.name, type_, self.sig_matcher.arg_type_overrides
        )

        return match or type_

    def _get_fixed_return_type_name(self, type_name: str | None, context: str) -> str:
        """Suggest a new data type based on `type_name`, if needed.

        Args:
            type_name:
                An expected return type. `None` means "we don't know or have a guess".
            context:
                The fully-qualified function / method name.
                e.g. `"maya.api.OpenMaya.FooClass.barMethod"`.

        Returns:
            The found type name, if any.

        """
        if not type_name:
            return None

        type_name = _get_fixed_type_name(type_name)

        return self.sig_matcher.find_result_match(
            context, type_name, self.sig_matcher.result_type_overrides
        ) or type_name

    def _get_fixed_signature(self, sig: FunctionSig, context: str) -> FunctionSig:
        """Fix any obvious return type or argument type issues on `sig`.

        Example:
            Some functions will claim to return `"string"`, this function will
            force `"string"` -> `"str"`.

            - `help(maya.api.OpenMaya.MArgList.asString)`
            - `help(maya.api.OpenMaya.MFileObject.expandedFullName)`

        Args:
            sig:
                Some function signature that we can modify safely.
            context:
                The fully-qualified function / method name.
                e.g. `"maya.api.OpenMaya.FooClass.barMethod"`.

        Returns:
            The new signature.

        """
        return_type = None

        if sig.ret_type:
            return_type = _get_fixed_type_name(sig.ret_type)

        args: list[ArgSig] = []

        for arg in sig.args:
            arg = copy.deepcopy(arg)
            arg.type = self._get_fixed_arg_type_name(arg, context, {})
            args.append(arg)

        return FunctionSig(
            name=sig.name,
            args=args,
            ret_type=self._get_fixed_return_type_name(return_type, context),
            type_args=sig.type_args,
        )

    def _get_matching_function_sigs(
        self,
        signatures: Iterable[FunctionSig],
        args_per_signature: Sequence[abc.MutableMapping[str, str]],
        context: str,
    ) -> list[FunctionSig]:
        """Generate a function signature for all of `signatures`.

        Args:
            signatures:
                Some function signature that we can modify safely.
            args_per_signature:
                The expected argument name and type for each of `signatures`.
            context:
                The fully-qualified function / method name.
                e.g. `"maya.api.OpenMaya.FooClass.barMethod"`.

        Returns:
            All computed signatures.

        """
        output: list[FunctionSig] = []
        index = -1

        for sig in signatures:
            if not sig.args:
                # NOTE: When a function takes no arguments, it doesn't get
                # written about in the docstring.
                #
                # Example: `help(maya.api.OpenMaya.MItSurfaceCV.reset)`.
                #
                # It has 3 signatures but only 2 docstring blocks. So we skip here
                #
                continue

            index += 1

            try:
                arg_types = args_per_signature[index]
            except IndexError:
                _LOGGER.error(
                    'Signature "%s" has out-of-range "%s" for "%s" data.',
                    context,
                    index,
                    args_per_signature,
                )

                continue

            args: list[ArgSig] = []

            for arg in sig.args:
                args.append(
                    ArgSig(
                        name=arg.name,
                        type=self._get_fixed_arg_type_name(arg, context, arg_types),
                        default=arg.default,
                        default_value=arg.default_value,
                    )
                )

            output.append(
                FunctionSig(
                    name=sig.name,
                    args=args,
                    ret_type=self._get_fixed_return_type_name(sig.ret_type, context),
                    type_args=sig.type_args,
                )
            )

        return output

    def _get_mismatched_function_sigs(
        self,
        signatures: Iterable[FunctionSig],
        context: str,
        options: abc.MutableMapping[str, str],
    ) -> list[FunctionSig]:
        """Generate `signatures`, given some uneven number of argument `options`.

        Note:
            Some docstrings don't match their overrides.

            `help(maya.api.OpenMayaAnim.MFnWeightGeometryFilter.setWeight)`

            - Has 4 signatures but only 1 docstring block.
            - That block is meant to apply to all signatures.

            This method handles situations like that.

        Args:
            signatures:
                Some function signature that we can modify safely.
            context:
                The fully-qualified function / method name.
                e.g. `"maya.api.OpenMaya.FooClass.barMethod"`.
            options:
                Some unique argument types to choose from, while type-hinting.

        Returns:
            All computed signatures.

        """
        output: list[FunctionSig] = []

        for sig in signatures:
            args: list[str] = []

            for arg in sig.args:
                args.append(
                    ArgSig(
                        name=arg.name,
                        type=self._get_fixed_arg_type_name(arg, context, options),
                        default=arg.default,
                        default_value=arg.default_value,
                    )
                )

            output.append(
                FunctionSig(
                    name=sig.name,
                    args=args,
                    ret_type=self._get_fixed_return_type_name(sig.ret_type, context),
                    type_args=sig.type_args,
                )
            )

        return output

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        """Find all function signatures for some Function `ctx`.

        Args:
            default_sig: The signature to fallback to.
            ctx: Data to parse into function signatures.

        Returns:
            The found signatures, if any.

        """
        signatures = [
            self._get_fixed_signature(sig, ctx.fullname)
            for sig in super().get_function_sig(default_sig, ctx) or []
        ]

        if not signatures:
            return signatures

        if not ctx.docstring:
            return signatures

        docstring_blocks = _API_DOCTSTRING_BLOCK_EXPRESSION.findall(ctx.docstring)

        if not docstring_blocks:
            return signatures

        all_arg_types_by_signature: list[dict[str, str]] = []
        all_arg_types: dict[str, str] = {}
        has_overloads = False

        for block in docstring_blocks:
            arg_types: dict[str, str] = {}

            for name, type_ in _API_DOCSTRING_TYPE_EXPRESSION.findall(block):
                type_ = _fix_type_if_needed(type_)

                if name not in all_arg_types:
                    all_arg_types[name] = type_
                else:
                    # SEE: :meth:`_ApiDocstringGenerator._get_mismatched_function_sigs`
                    # for details on why we need this.
                    #
                    has_overloads = True

                arg_types[name] = type_

            if arg_types:
                all_arg_types_by_signature.append(arg_types)

        if not has_overloads:
            return self._get_mismatched_function_sigs(signatures, ctx.fullname, all_arg_types)

        return self._get_matching_function_sigs(signatures, all_arg_types_by_signature, ctx.fullname)


class MayaCmdSignatureGenerator(SignatureGenerator):
    """A special way of auto-generating type-hint signatures for `maya.cmds`.

    It works by iterating over the flags in a function with `query=True` and
    recording its return value. In short, if a function supports `query=True`
    this might be able to auto-type-hint it! But for other functions, this
    class is not useful. For those situations,
    see :attr:`MayaCmdAdvSignatureGenerator.sig_matcher` instead.
    """

    add_exists_overloads = [
        "control",
        "menu",
        "shelfLayout",
        "window",
    ]

    add_query_overloads = [
        "playbackOptions",
    ]

    def __init__(self):
        import pymel.internal.cmdcache

        pymel.internal.cmdcache.CmdCache.version = _MAYA_VERSION
        cmdcache = pymel.internal.cmdcache.CmdCache()
        data = cmdcache.load()
        datamap = dict(zip(cmdcache.cacheNames(), data))
        self.CMDLIST = datamap["cmdlist"]  # type: pymel.internal.cmdcache.CommandInfo

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        if ctx.module_name == "maya.cmds":
            try:
                cmd_info = self.CMDLIST[ctx.name]
            except KeyError:
                print(f"No command info found for {ctx.name}")
                return None

            try:
                cmd_flags = cmd_info["flags"]
            except KeyError:
                # print(f"No flag info found for {ctx.name}")
                return None

            args = [ArgSig("*args")] + self._get_args(cmd_flags)
            sigs = [FunctionSig(ctx.name, args=args, ret_type="Any")]
            flag_pairs = list(cmd_flags.items())

            if ctx.name in self.add_query_overloads:
                sigs = self._get_query_overloads(ctx.name, flag_pairs) + sigs

            has_edit_sigs = False

            edit_sigs = self._get_edit_overloads(ctx.name, flag_pairs)

            if edit_sigs:
                has_edit_sigs = True
                sigs = _strip_arguments({"edit"}, sigs)
                sigs = edit_sigs + sigs

            if ctx.name in self.add_exists_overloads:
                exists_sigs = self._get_exists_overloads(ctx.name, cmd_flags)

                if exists_sigs:
                    if has_edit_sigs:
                        exists_sigs = _strip_arguments({"edit"}, exists_sigs)

                    sigs = _strip_arguments({"exists"}, sigs)
                    sigs = exists_sigs + sigs

            return sigs

    def _mel_type_to_python_type(self, typ, as_result=False) -> str:
        """Convert a mel type to a python type"""
        if isinstance(typ, str):
            if typ == "timerange":
                # FIXME: tuple support may be pymel-specific
                return "str | tuple[float, float] | tuple[float]"
            elif typ == "floatrange":
                if as_result:
                    return "float"
                else:
                    return "str | int | float"
            elif typ == "time":
                if as_result:
                    return "float"
                else:
                    return "int | float"
            elif typ == "PyNode":
                return "str"
            elif typ == "script":
                return "str | Callable"
            elif " " in typ:
                # I've seen one case of bad type name in our cmdlist cache
                return "Any"
        elif typ is bool and not as_result:
            # it's a common pattern coming from MEL to use 1/0 for True/False
            return "bool | int"
        else:
            return typ.__name__

    def _get_arg_type(
        self, flag_info: "pymel.internal.cmdcache.flag_info", as_result=False
    ) -> str:
        """Get the python type for the command argument."""
        if flag_info["numArgs"] < 2:
            typ = self._mel_type_to_python_type(flag_info["args"], as_result=as_result)
        else:
            # FIXME: this may be affected by resultNeedsUnpacking
            typ = "tuple[%s]" % ", ".join(
                [
                    self._mel_type_to_python_type(arg_type, as_result=as_result)
                    for arg_type in flag_info["args"]
                ]
            )
        if not as_result and flag_has_mode(flag_info, "multiuse"):
            typ = "%s | list[%s]" % (typ, typ)
        return typ

    def _get_args(self, cmd_flags) -> list[ArgSig]:
        """
        Get list of argument definitions (including type) that should replace
        **kwargs
        """
        new_args = []
        used_flags = set()

        def add_arg(name: str, typ: str) -> None:
            if name not in used_flags:
                new_args.append(ArgSig(name, typ, default=True))
                used_flags.add(name)

        for flag_name, flag_info in cmd_flags.items():
            typ = self._get_arg_type(flag_info, as_result=False)
            if flag_has_mode(flag_info, "query") and typ not in [
                "bool | int",
                "bool",
                "int",
            ]:
                typ = "bool | int | %s" % typ

            add_arg(flag_name, typ)
            # FIXME: add an option to include/exclude short names
            # add_arg(short_name, typ)

        return new_args

    def _get_edit_overloads(self, name: str, flags: _FlagsType) -> list[FunctionSig]:
        """Add function signature(s) for `edit=True`-style function calls.

        Example:
            >>> cmds.polySphere("pSphere1", edit=True, radius=10)

        Args:
            name: The cmds function name. e.g. `"keyTangent"` (from `cmds.keyTangent`).
            flags: All parameter flag data that we know about, for this function.

        Returns:
            If `edit=True` is found, return any signature(s) needed.
            Otherwise return nothing.

        """
        sigs: list[FunctionSig] = []
        edit_flags = [
            (flag_name, flag_info)
            for flag_name, flag_info in flags
            if flag_has_mode(flag_info, "edit")
        ]

        if not edit_flags:
            return []

        args = [
            ArgSig("*args"),
            ArgSig("edit", type="Literal[True]"),
            *[
                ArgSig(
                    flag_name,
                    type=self._get_arg_type(flag_info, as_result=False),
                    default=True,
                )
                for flag_name, flag_info in edit_flags
            ],
        ]
        sigs.append(FunctionSig(name, args=args, ret_type="None"))

        return sigs

    def _get_exists_overloads(self, name: str, flags) -> list[FunctionSig]:
        """If the function `name` has `exists=True`, create a function signature for it.

        Args:
            name: Some cmds function name. e.g. `"joint"` (from `cmds.joint`).
            flags: All parameter flag data that we know about, for this function.

        Returns:
            If `exists=True` is found, return any signature(s) needed.
            Otherwise return nothing.

        """
        exists_flag = flags.get("exists")

        if not exists_flag:
            return []

        if not flag_has_mode(exists_flag, "query"):
            args = [ArgSig("*args"), ArgSig("exists", type="Literal[True]")]

            return [FunctionSig(name, args=args, ret_type="bool")]

        sigs: list[FunctionSig] = []

        for flag_name, flag_info in flags.items():
            # NOTE: Some maya commands can only call `exists=True` when
            # `query=True` is also included.
            #
            # Example: `cmds.file(file_path, query=True, exists=True)`
            #
            args = [
                ArgSig("*args"),
                ArgSig("query", type="Literal[True]"),
                ArgSig("exists", type="Literal[True]"),
                ArgSig(flag_name, type=self._get_arg_type(flag_info, as_result=False))
            ]
            sigs.append(FunctionSig(name, args=args, ret_type="bool"))

        return sigs

    def _get_query_overloads(self, name: str, flags: _FlagsType) -> list[FunctionSig]:
        """Make a function signature for every queriable flag.

        e.g. if `flags` has 10 queriable values then this function returns 10
        signatures, one each.

        Args:
            name: The cmds function name. e.g. `"keyTangent"` (from `cmds.keyTangent`).
            flags: All parameter flag data that we know about, for this function.

        Returns:
            If `edit=True` is found, return any signature(s) needed.
            Otherwise return nothing.

        """
        # FIXME: this does not support supplemental flags that modify the query
        sigs: list[FunctionSig] = []
        for flag_name, flag_info in flags:
            if flag_has_mode(flag_info, "query"):
                args = [
                    ArgSig("*args"),
                    ArgSig("query", type="Literal[True]"),
                    ArgSig(flag_name, type="Literal[True]"),
                ]
                ret_type = self._get_arg_type(flag_info, as_result=True)
                sigs.append(FunctionSig(name, args=args, ret_type=ret_type))
        return sigs

    # def get_property_type(self, default_type: str | None, ctx: FunctionContext) -> str | None:
    #     """Infer property type from docstring or docstring signature."""
    #     pass


class CmdsStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [
            MayaCmdAdvSignatureGenerator(
                merge_overrides_with_fallback=True,
                fallback_sig_gen=MayaCmdSignatureGenerator(),
            )
        ]

    def get_obj_module(self, obj: object) -> str | None:
        """Return module name of the object."""
        module = super().get_obj_module(obj)
        if module and inspect.isfunction(obj):
            return self.module_name
        return module

    def is_function(self, obj: object) -> bool:
        # many of the commands are detected as builtin because they are compiled
        return inspect.isbuiltin(obj) or inspect.isfunction(obj)

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        # sort members because there's so damn many of them
        members = super().get_members(obj)
        return sorted(members, key=lambda x: x[0])

    def set_defined_names(self, defined_names: set[str]) -> None:
        super().set_defined_names(defined_names)
        for typ in ["Callable", "Literal"]:
            self.add_name(f"typing.{typ}", require=False)


class MelStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def get_obj_module(self, obj: object) -> str | None:
        """Return module name of the object."""
        module = super().get_obj_module(obj)
        if module and inspect.isfunction(obj):
            return self.module_name
        return module

    def is_function(self, obj: object) -> bool:
        return inspect.isbuiltin(obj) or inspect.isfunction(obj)


class APIStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def __init__(
        self,
        module_name: str,
        known_modules: list[str],
        doc_dir: str = "",
        _all_: list[str] | None = None,
        include_private: bool = False,
        export_less: bool = False,
        include_docstrings: bool = False,
        module: ModuleType | None = None,
    ):
        """Force `from typing import ..., Self, ...` to be included in the .pyi file."""
        super().__init__(
            module_name=module_name,
            known_modules=known_modules,
            doc_dir=doc_dir,
            _all_=_all_,
            include_private=include_private,
            export_less=export_less,
            include_docstrings=include_docstrings,
            module=module,
        )

        # NOTE: A number of Maya signatures use typing.Self so we make it available
        self.import_tracker.add_import_from("typing", [("Literal", None), ("Self", None)])

        self._initialize_maya_imports()

    def _initialize_maya_imports(self) -> None:
        """Make the module aware of any Maya-related imports.

        These imports will only be added to a generated .pyi file if some type
        annotation is found that matches it.

        """
        if fnmatch.fnmatch(self.module_name, "maya.api.*"):
            external_modules = [
                module
                for module in self.known_modules
                if module.startswith("maya.api.")
            ]
        else:
            external_modules = [
                module for module in self.known_modules
                if module.startswith("maya.") and not module.startswith("maya.api.")
            ]

        for module, members in sorted(
            self._get_external_module_members(external_modules).items()
        ):
            self.import_tracker.add_import_from(
                module,
                # NOTE: Maya types start with an "M" - e.g. MDagPath, MObject, etc.
                [(member, None) for member in members if member.startswith("M")],
            )

    def _get_external_module_members(self, modules: Iterable[str]) -> dict[str, list[str]]:
        """Find all members (classes, functions, attributes) from `modules`.

        Args:
            modules:
                All external modules that we assume are valid to import in the
                current module.

        Returns:
            The found module-member associations.

        """
        result: dict[str, list[str]] = {}

        for module_name in modules:
            if module_name == self.module_name:
                # NOTE: Prevent this instance from treating itself as an
                # external dependency by accident.
                #
                continue

            if _is_protected_module(module_name):
                # NOTE: Ignore private modules, we don't want to import their types.
                continue

            try:
                module = importlib.import_module(module_name)
            except ImportError:
                _LOGGER.exception('Module "%s" could not be imported.', module_name)

                continue
            else:
                result[module_name] = [member[0] for member in inspect.getmembers(module)]

        return result

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [_ApiDocstringGenerator()]

    def process_inferred_sigs(self, inferred: list[FunctionSig]) -> None:
        """Add `"Incomplete"` to any signatures in `inferred` which don't have types.

        Args:
            inferred: Function signatures that may be partially-defined.

        """
        for index, sig in enumerate(inferred):
            arguments = sig.args

            if sig.is_special_method():
                # NOTE: We ignore the `self` / `cls` bound argument
                arguments = arguments[1:]

            for arg in arguments:
                if not arg.type:
                    arg.type = _UNKNOWN_TYPE

            if not sig.ret_type:
                # NOTE: `sig.ret_type` is immutable so we have to get creative
                # here. Don't worry though, the mypy source code runs this
                # exact same code so it should be safe to do.
                #
                inferred[index] = sig._replace(ret_type=_UNKNOWN_TYPE)

        super().process_inferred_sigs(inferred)

    def strip_or_import(self, type_name: str) -> str:
        # some type annotations are invalid: stop them from aborting the whole process
        try:
            return super().strip_or_import(type_name)
        except SyntaxError:
            return _UNKNOWN_TYPE

    def get_obj_module(self, obj: object) -> str | None:
        """Return module name of the object."""
        module = super().get_obj_module(obj)
        # the maya.api.Open* modules think their module name is maya.Open*
        if module and module.startswith("Open"):
            # convert "OpenMaya" to "maya.api.OpenMaya"
            return f"maya.api.{module}"
        return module

    def is_function(self, obj: object) -> bool:
        # many of the functions are detected as builtin because they are compiled
        return inspect.isbuiltin(obj) or inspect.isfunction(obj)

    def is_method(self, class_info: ClassInfo, name: str, obj: object) -> bool:
        # Note: this and other overrides on this class are the default behavior for modules
        # detected as c-modules, however maya.Open* and maya.api.Open* modules are .py files
        # which *contain* many C-extension objects, thus they confuse the stub generator.

        # Look into setting self.is_c_module and self.resort_members to simplify this.
        return inspect.ismethoddescriptor(obj) or type(obj) in (
            type(str.index),
            type(str.__add__),
            type(str.__new__),
        )

    def is_classmethod(self, class_info: ClassInfo, name: str, obj: object) -> bool:
        return inspect.isbuiltin(obj) or type(obj).__name__ in (
            "classmethod",
            "classmethod_descriptor",
        )


class UFESignatureGenerator(AdvancedSignatureGenerator):
    sig_matcher = AdvancedSigMatcher(
        # Override entire function signature:
        signature_overrides={},
        # Override argument types
        #   dict of (name_pattern, arg, type) to arg_type
        #   type can be str | re.Pattern
        arg_type_overrides={},
        # Override result types
        #   dict of (name_pattern, type) to result_type
        #   e.g. ("*", "Buffer"): "numpy.ndarray"
        result_type_overrides={},
        # Override property types
        #   dict of (name_pattern, type) to result_type
        #   e.g. ("*", "Buffer"): "numpy.ndarray"
        property_type_overrides={},
        # Types that have implicit alternatives.
        #   dict of type_str to list of types that can be used instead
        #   e.g. "PySide2.QtGui.QKeySequence": ["str"],
        # converts any matching argument to a union of the supported types
        implicit_arg_types={},
    )

    def process_sig(
        self, ctx: mypy.stubgen.FunctionContext, sig: mypy.stubgen.FunctionSig
    ) -> mypy.stubgen.FunctionSig:
        # Analyze the signature and add a '/' argument if necessary to mark
        # arguments which cannot be access by name.
        return add_positional_only_args(ctx, super().process_sig(ctx, sig))


class UFEStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [
            UFESignatureGenerator(
                fallback_sig_gen=DocstringSignatureGenerator(),
            )
        ]

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        members = super().get_members(obj)
        # these two objects generate invalid class names, but they don't appear elsewhere
        # in the stubs.  safe to filter for now.
        if isinstance(obj, types.ModuleType):
            reg = re.compile("KeysView|ItemsView|ValuesView")
            return [m for m in members if not reg.match(m[0])]
        return members

    def set_defined_names(self, defined_names: set[str]) -> None:
        super().set_defined_names(defined_names)
        for typ in ["Set"]:
            self.add_name(f"typing.{typ}", require=False)


delegate = GeneratorDelegate[mypy.stubgen.InspectionStubGenerator](
    rules={
        "maya.api.*": APIStubGenerator,
        "maya.Open*": APIStubGenerator,
        "maya.cmds": CmdsStubGenerator,
        "maya.mel": MelStubGenerator,
        "ufe.PyUfe": UFEStubGenerator,
    },
    fallback=mypy.stubgen.InspectionStubGenerator,
)

mypy.stubgen.InspectionStubGenerator = delegate  # type: ignore[attr-defined,misc]
mypy.stubgenc.InspectionStubGenerator = delegate  # type: ignore[misc]


if __name__ == "__main__":
    import pathlib

    parser = argparse.ArgumentParser(description="Python stub generator for Nuke")
    parser.add_argument("outdir", help="The path to the output directory")
    parser.add_argument(
        "--maya-version",
        default="2025",
        help="The major version to generate stubs for. e.g. 2023, 2024, 2025, etc.",
    )
    args = parser.parse_args()

    _MAYA_VERSION = args.maya_version

    print("Initializing maya")
    import maya.standalone

    maya.standalone.initialize()
    print("Initialization complete")

    # mypy.stubgen.main(["-p=maya.app", "--parse-only", f"-o={args.outdir}"])

    mypy.stubgen.main(
        [
            "-m=maya.cmds",
            "-m=maya.mel",
            "-m=maya.standalone",
            "-p=maya.api",
            "-m=maya.OpenMaya",
            "-m=maya.OpenMayaAnim",
            "-m=maya.OpenMayaRender",
            "-m=maya.OpenMayaUI",
            "-m=maya.OpenMayaMPx",
            "-p=ufe",
            "--inspect-mode",
            f"-o={args.outdir}",
        ]
    )

    print("Patching up generated stubs")
    outdir = pathlib.Path(args.outdir)
    # make an empty maya/__init__.pyi
    outdir.joinpath("maya", "__init__.pyi").touch()

    # replace the useless ufe/__init__.pyi with ufe/PyUfe.pyi
    init = outdir.joinpath("ufe", "__init__.pyi")
    init.unlink()
    init.with_name("PyUfe.pyi").rename(init)

    # indicate to type checkers that the stub package does not have full coverage
    # (it's missing maya.app, for example)
    marker = outdir.joinpath("maya", "py.typed")
    marker.write_text("partial\n")

    print("Done")
