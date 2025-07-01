from __future__ import absolute_import, annotations, division, print_function

import argparse
import inspect
import os
import re
import types
from typing import Any, Iterable

import mypy.stubgen
import mypy.stubgenc
from mypy.stubdoc import ArgSig, FunctionSig
from mypy.stubgenc import DocstringSignatureGenerator, SignatureGenerator
from mypy.stubutil import FunctionContext

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


def flag_has_mode(flag_info, mode):
    return mode in flag_info.get("modes", [])


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
                args = [ArgSig("*args"), ArgSig("query", type="Literal[True]"), ArgSig(flag_name, type="Literal[True]")]
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
        return inspect.isbuiltin(obj) or inspect.isfunction(obj)

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
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
    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [DocstringSignatureGenerator()]

    def strip_or_import(self, type_name: str) -> str:
        try:
            return super().strip_or_import(type_name)
        except SyntaxError:
            return "Incomplete"

    def get_obj_module(self, obj: object) -> str | None:
        """Return module name of the object."""
        module = super().get_obj_module(obj)
        if module and module.startswith("Open"):
            # convert "OpenMaya" to "maya.api.OpenMaya"
            return f"maya.api.{module}"
        return module

    def is_function(self, obj: object) -> bool:
        if self.module_name == "maya.cmds" or self.module_name.startswith("maya.api."):
            return inspect.isbuiltin(obj) or inspect.isfunction(obj)
        else:
            return super().is_function(obj)

    def is_method(self, class_info: ClassInfo, name: str, obj: object) -> bool:
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
        "maya.mel":  MelStubGenerator,
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
    # maya/__init__
    outdir.joinpath("maya", "__init__.pyi").touch()

    # ufe/__init__
    init = outdir.joinpath("ufe", "__init__.pyi")
    init.unlink()
    init.with_name("PyUfe.pyi").rename(init)

    marker = outdir.joinpath("maya", "py.typed")
    marker.write_text("partial\n")

    print("Done")
