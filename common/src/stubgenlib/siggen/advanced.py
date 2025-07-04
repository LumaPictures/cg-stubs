from __future__ import absolute_import, annotations, division, print_function

import fnmatch
import re
from dataclasses import dataclass, field
from typing import Literal, NamedTuple, TypeVar, cast

from mypy.stubdoc import infer_sig_from_docstring
from mypy.stubgenc import (
    ArgSig,
    FunctionContext,
    FunctionSig,
    SignatureGenerator,
)
from mypy.stubgenc import (
    DocstringSignatureGenerator as CDocstringSignatureGenerator,
)

T = TypeVar("T")


class Optionality(NamedTuple):
    accepts_none: bool
    has_default: bool = True


@dataclass
class AdvancedSigMatcher(object):
    """
    Defines rules for matching objects within inspected modules and correcting
    or overriding their inspected signature.
    """

    # Full signature replacements.
    #   name_pattern: sig_str
    #   e.g. "*.VolatileBool.set": "(self, a: object) -> None"
    signature_overrides: dict[str, str | list[str]] = field(default_factory=dict)

    # Override argument types
    #   (name_pattern, arg, type): arg_type
    #   e.g. ("*", "flags", "int"): "typing.SupportsInt"
    arg_type_overrides: dict[tuple[str, str, str | re.Pattern[str] | None], str] = (
        field(default_factory=dict)
    )

    # Override result types
    #   (name_pattern, type): result_type
    #   e.g. ("*", "int"): "typing.SupportsInt"
    result_type_overrides: dict[tuple[str, str | re.Pattern[str] | None], str] = field(
        default_factory=dict
    )

    # Override property types
    #   (name_pattern, type): type
    #   e.g. ("*", "int"): "typing.SupportsInt"
    property_type_overrides: dict[tuple[str, str | re.Pattern[str] | None], str] = (
        field(default_factory=dict)
    )

    # Types that have implicit alternatives.
    #   type_str: list of types that can be used instead
    #   e.g. "PySide2.QtGui.QKeySequence": ["str"],
    implicit_arg_types: dict[str, list[str]] = field(default_factory=dict)

    # Args which should be made Optional[].
    #   (name_pattern, arg, type): Optionality
    optional_args: dict[tuple[str, str, str | re.Pattern[str] | None], Optionality] = (
        field(default_factory=dict)
    )

    # Results which should be made Optional[].
    optional_result: list[str] = field(default_factory=list)

    # Add new overloads to existing functions.
    #   name_pattern: list of sig_str
    #   e.g. "*.VolatileBool.set": ["(self, a: object) -> None"]
    new_overloads: dict[str, list[str]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        # insert OptionalKeys
        self.arg_type_overrides.update(
            {
                # method, arg name, type
                (
                    "*",
                    "*",
                    orig,
                ): "typing.Union[{},{}]".format(orig, ",".join(alt))
                for orig, alt in self.implicit_arg_types.items()
            }
        )
        self.arg_type_overrides.update(
            {
                # method, arg name, type
                (
                    "*",
                    "*",
                    "typing.Union[{},NoneType]".format(orig),
                ): "typing.Union[{},{},NoneType]".format(orig, ",".join(alt))
                for orig, alt in self.implicit_arg_types.items()
            }
        )
        # restructure this so that it can be used with find_result_match
        self._optional_result: dict[tuple[str, str | re.Pattern[str] | None], bool] = {
            (name, "*"): True for name in self.optional_result
        }
        # self.arg_name_replacements = {
        #     tuple(OptionalKey(k) for k in key): value
        #     for key, value in self._arg_name_replacements.items()
        # }

    def find_func_match(self, fullname: str, items: dict[str, T]) -> T | None:
        """Look for a match in the given dictionary of function/method overrides"""
        for pattern, value in items.items():
            if fnmatch.fnmatchcase(fullname, pattern):
                return value
        return None

    def _type_match(
        self,
        type_match: str | re.Pattern[str] | None,
        new_value: T,
        orig_type: str | None,
    ) -> T | None:
        """Return the matched type or None if there was no match.

        if type_match is a regular expression, the new_value may be altered by subsitutions,
        otherwise the value returned will be new_value.
        """
        if orig_type is None:
            return new_value if (type_match is None or type_match == "*") else None
        elif isinstance(type_match, re.Pattern):
            if not isinstance(new_value, str):
                raise ValueError(
                    f"{type_match} is a regex, but {repr(new_value)} is not a string"
                )
            return cast("T | None", type_match.sub(new_value, orig_type))
        elif type_match:
            return new_value if fnmatch.fnmatchcase(orig_type, type_match) else None
        else:
            return None

    def find_arg_match(
        self,
        fullname: str,
        arg_name: str,
        arg_type: str | None,
        items: dict[tuple[str, str, str | re.Pattern[str] | None], T],
    ) -> T | None:
        """Look for a match in the given dictionary of argument overrides

        arg_type : if None means only replace if the type is unset (None).
        items : key is (name_pattern, arg, type). value is whatever we're trying to find.
        """
        for (method_match, arg_name_match, arg_type_match), value in items.items():
            if fnmatch.fnmatchcase(fullname, method_match) and fnmatch.fnmatchcase(
                arg_name, arg_name_match
            ):
                new_value = self._type_match(arg_type_match, value, arg_type)
                if new_value is not None:
                    return new_value
        return None

    def find_result_match(
        self,
        fullname: str,
        ret_type: str | None,
        items: dict[tuple[str, str | re.Pattern[str] | None], T],
    ) -> T | None:
        """Look for a match in the given dictionary of argument overrides"""
        for (method_match, ret_type_match), value in items.items():
            if fnmatch.fnmatchcase(fullname, method_match):
                new_value = self._type_match(ret_type_match, value, ret_type)
                if new_value is not None:
                    return new_value
        return None


class AdvancedSignatureGenerator(SignatureGenerator):
    """
    A signature generator that uses an AdvancedSigMatcher to override all or
    part of a function signature.
    """

    WHITESPACE_FIX = re.compile(",(?=\w)")

    sig_matcher: AdvancedSigMatcher

    def __init__(
        self,
        fallback_sig_gen=CDocstringSignatureGenerator(),
        merge_overrides_with_fallback: bool = False,
        select_overload_to_merge: Literal["first", "by_index"] = "first",
    ) -> None:
        """
        fallback_sig_gen: used to find a signature when signature_overrides has no match.
        """
        self.fallback_sig_gen = fallback_sig_gen
        self.merge_overrides_with_fallback = merge_overrides_with_fallback
        self.select_overload_to_merge = select_overload_to_merge

    def get_signature_str(self, ctx: FunctionContext) -> str | list[str] | None:
        """Look for a docstring signature in signature_overrides"""
        return self.sig_matcher.find_func_match(
            ctx.fullname, self.sig_matcher.signature_overrides
        )

    def process_arg(self, ctx: FunctionContext, arg: ArgSig) -> None:
        """Update ArgSig in place"""
        # if key in self.arg_name_replacements:
        #     arg.name = self.arg_name_replacements[key]

        optionality = self.sig_matcher.find_arg_match(
            ctx.fullname, arg.name, arg.type, self.sig_matcher.optional_args
        )
        if optionality is not None:
            if optionality.has_default:
                arg.default = True
            if optionality.accepts_none:
                arg.type = "typing.Union[{},NoneType]".format(arg.type)

        # FIXME: I think we want an else here, since arg.type is set, above
        arg_type_override = self.sig_matcher.find_arg_match(
            ctx.fullname, arg.name, arg.type, self.sig_matcher.arg_type_overrides
        )
        if arg_type_override is not None:
            arg.type = arg_type_override

        if arg.type:
            # fixes the removal of whitepsace caused by infer_sig_from_docstring
            arg.type = self.WHITESPACE_FIX.sub(", ", arg.type)

    def process_sig(self, ctx: FunctionContext, sig: FunctionSig) -> FunctionSig:
        """
        Check if the AdvancedSigMatcher matches `sig` and if it does, apply
        fixes.
        """
        for arg in sig.args:
            self.process_arg(ctx, arg)
        if self.sig_matcher.find_result_match(
            ctx.fullname, sig.ret_type, self.sig_matcher._optional_result
        ):
            # make result optional
            sig = sig._replace(ret_type=f"typing.Optional[{sig.ret_type}]")
        else:
            # override result type
            ret_override = self.sig_matcher.find_result_match(
                ctx.fullname, sig.ret_type, self.sig_matcher.result_type_overrides
            )
            if ret_override:
                sig = sig._replace(ret_type=ret_override)
        if sig.ret_type:
            # fixes the removal of whitepsace caused by infer_sig_from_docstring
            fixed_type = self.WHITESPACE_FIX.sub(", ", sig.ret_type)
            if sig.ret_type != fixed_type:
                sig = sig._replace(ret_type=fixed_type)
        return sig

    def process_sigs(
        self, ctx: FunctionContext, results: list[FunctionSig]
    ) -> list[FunctionSig]:
        """
        Process all of the signatures
        """
        for i, inferred in enumerate(results):
            results[i] = self.process_sig(ctx, inferred)

        new_overloads = self.sig_matcher.find_func_match(
            ctx.fullname, self.sig_matcher.new_overloads
        )
        if new_overloads:
            docstr = "\n".join(ctx.name + overload for overload in new_overloads)
            new_sigs = infer_sig_from_docstring(docstr, ctx.name)
            if new_sigs:
                results.extend(new_sigs)
        return results

    def get_overridden_signatures(
        self, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        """
        Return a full replacement for the docstring signature, if it has
        been provded by the AdvancedSigMatcher.
        """
        docstr_override = self.get_signature_str(ctx)
        if docstr_override:
            name = ctx.name
            docstr = docstr_override

            def prep_doc(d: str) -> str:
                if not d.startswith(name):
                    d = name + d
                return d

            # process our override
            if isinstance(docstr, list):
                docstr = "\n".join(prep_doc(d) for d in docstr)
            else:
                docstr = prep_doc(docstr)
            return infer_sig_from_docstring(docstr, name)
        else:
            return None

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        """Main override to apply the signature overrides"""
        from stubgenlib.utils import merge_signature_kwargs

        results = self.get_overridden_signatures(ctx)
        if results and self.merge_overrides_with_fallback:
            fallback = self.fallback_sig_gen.get_function_sig(default_sig, ctx)
            if fallback:
                if self.select_overload_to_merge == "first":
                    for i, result in enumerate(results):
                        results[i] = merge_signature_kwargs(result, fallback[0])
                elif self.select_overload_to_merge == "by_index":
                    assert len(results) == len(fallback)
                    for i, (result, fb) in enumerate(zip(results, fallback)):
                        results[i] = merge_signature_kwargs(result, fb)
                else:
                    raise ValueError(self.select_overload_to_merge)

        if not results:
            # call the standard docstring-based generator.
            results = self.fallback_sig_gen.get_function_sig(default_sig, ctx)
            if results is None:
                results = [default_sig]

        if results:
            return self.process_sigs(ctx, results)

        return results

    def get_property_type(
        self, default_type: str | None, ctx: FunctionContext
    ) -> str | None:
        """Return the type of the given property"""
        ret_type = self.fallback_sig_gen.get_property_type(default_type, ctx)
        type_override = self.sig_matcher.find_result_match(
            ctx.fullname, ret_type, self.sig_matcher.property_type_overrides
        )
        if type_override is not None:
            return type_override
        else:
            return ret_type
