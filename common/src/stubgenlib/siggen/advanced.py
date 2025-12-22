from __future__ import absolute_import, annotations, division, print_function

import fnmatch
import re
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Generic, Literal, NamedTuple, TypeVar, cast

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

KeyT = TypeVar("KeyT")
T = TypeVar("T")
MatcherT = TypeVar("MatcherT")


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
    signature_overrides: dict[str, str | list[str] | list[FunctionSig]] = field(
        default_factory=dict
    )

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


class Matcher(Generic[KeyT, T]):
    def __init__(self, label: str, search_items: dict[KeyT, T]):
        self.label = label
        self._search_items = search_items
        self._matches: defaultdict[KeyT, list[str]] = defaultdict(list)

    def print_info(self, matches: bool = False) -> None:
        unmatched = set(self._search_items).difference(self._matches)
        print(f"{self.label} match info")
        if matches:
            print("  Matched:")
            for key in sorted(self._matches):
                print(f"    {key}")
                for match in self._matches[key]:
                    print(f"      {match}")
        print("  Unmatched:")
        for key in sorted(unmatched):
            print(f"    {key}")

    @classmethod
    def _type_match(
        cls,
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


class FuncMatcher(Matcher[str, T]):
    def find_func_match(self, fullname: str) -> T | None:
        """Look for a match in the given dictionary of function/method overrides"""
        for pattern, value in self._search_items.items():
            if fnmatch.fnmatchcase(fullname, pattern):
                self._matches[pattern].append(fullname)
                return value
        return None


class ArgMatcher(Matcher[tuple[str, str, str | re.Pattern[str] | None], T]):
    def find_arg_match(
        self,
        fullname: str,
        arg_name: str,
        arg_type: str | None,
    ) -> T | None:
        """Look for a match in the given dictionary of argument overrides

        arg_type : if None means only replace if the type is unset (None).
        items : key is (name_pattern, arg, type). value is whatever we're trying to find.
        """
        for (
            method_match,
            arg_name_match,
            arg_type_match,
        ), value in self._search_items.items():
            if fnmatch.fnmatchcase(fullname, method_match) and fnmatch.fnmatchcase(
                arg_name, arg_name_match
            ):
                new_value = self._type_match(arg_type_match, value, arg_type)
                if new_value is not None:
                    self._matches[
                        (method_match, arg_name_match, arg_type_match)
                    ].append(fullname)
                    return new_value
        return None


class ResultMatcher(Matcher[tuple[str, str | re.Pattern[str] | None], T]):
    def find_result_match(
        self,
        fullname: str,
        ret_type: str | None,
    ) -> T | None:
        """Look for a match in the given dictionary of argument overrides"""
        for (method_match, ret_type_match), value in self._search_items.items():
            if fnmatch.fnmatchcase(fullname, method_match):
                new_value = self._type_match(ret_type_match, value, ret_type)
                if new_value is not None:
                    self._matches[(method_match, ret_type_match)].append(fullname)
                    return new_value
        return None


class Overridden(list[FunctionSig]):
    """
    Indicates that the signatures were generated by an explicit override rather than
    from untrusted docstrings. This information can be used to prevent resorting, for example."""


# FIXME: generate a report of rules that were not used atexit.
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
        strict: bool = False,
    ) -> None:
        """
        fallback_sig_gen: used to find a signature when signature_overrides has no match.
        strict: whether to error if provided signature strings cannot be parsed
        """
        self.fallback_sig_gen = fallback_sig_gen
        self.merge_overrides_with_fallback = merge_overrides_with_fallback
        self.select_overload_to_merge = select_overload_to_merge
        self.strict = strict
        self._matchers: list[Matcher] = []

        self._signature_overrides_matcher = self._add_matcher(
            FuncMatcher("signature_overrides", self.sig_matcher.signature_overrides)
        )
        self._arg_type_overrides_matcher = self._add_matcher(
            ArgMatcher("arg_type_overrides", self.sig_matcher.arg_type_overrides)
        )
        self._optional_result_matcher = self._add_matcher(
            ResultMatcher("optional_result", self.sig_matcher._optional_result)
        )
        self._optional_args_matcher = self._add_matcher(
            ArgMatcher("optional_args", self.sig_matcher.optional_args)
        )
        self._result_type_overrides_matcher = self._add_matcher(
            ResultMatcher(
                "result_type_overrides", self.sig_matcher.result_type_overrides
            )
        )
        self._new_overloads_matcher = self._add_matcher(
            FuncMatcher("new_overloads", self.sig_matcher.new_overloads)
        )
        self._property_type_overrides_matcher = self._add_matcher(
            ResultMatcher(
                "property_type_overrides", self.sig_matcher.property_type_overrides
            )
        )

    def _add_matcher(self, matcher: MatcherT) -> MatcherT:
        self._matchers.append(matcher)
        return matcher

    def print_info(self, matches: bool = False) -> None:
        for matcher in self._matchers:
            matcher.print_info(matches=matches)

    def get_signature_str(
        self, ctx: FunctionContext
    ) -> str | list[str] | list[FunctionSig] | None:
        """Look for a docstring signature in signature_overrides"""
        return self._signature_overrides_matcher.find_func_match(ctx.fullname)

    def process_arg(self, ctx: FunctionContext, arg: ArgSig) -> None:
        """Update ArgSig in place"""
        # if key in self.arg_name_replacements:
        #     arg.name = self.arg_name_replacements[key]

        optionality = self._optional_args_matcher.find_arg_match(
            ctx.fullname,
            arg.name,
            arg.type,
        )
        if optionality is not None:
            if optionality.has_default:
                arg.default = True
            if optionality.accepts_none:
                arg.type = "typing.Union[{},NoneType]".format(arg.type)

        # FIXME: I think we want an else here, since arg.type is set, above
        arg_type_override = self._arg_type_overrides_matcher.find_arg_match(
            ctx.fullname,
            arg.name,
            arg.type,
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
        if self._optional_result_matcher.find_result_match(ctx.fullname, sig.ret_type):
            # make result optional
            sig = sig._replace(ret_type=f"typing.Optional[{sig.ret_type}]")
        else:
            # override result type
            ret_override = self._result_type_overrides_matcher.find_result_match(
                ctx.fullname,
                sig.ret_type,
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

        new_overloads = self._new_overloads_matcher.find_func_match(ctx.fullname)
        if new_overloads:
            docstr = "\n".join(ctx.name + overload for overload in new_overloads)
            new_sigs = infer_sig_from_docstring(docstr, ctx.name)
            if new_sigs:
                results.extend(new_sigs)
        return results

    def get_overridden_signatures(self, ctx: FunctionContext) -> Overridden | None:
        """
        Return a full replacement for the docstring signature, if it has
        been provded by the AdvancedSigMatcher.
        """
        docstr_override = self.get_signature_str(ctx)
        if docstr_override:
            if (
                isinstance(docstr_override, list)
                and len(docstr_override)
                and isinstance(docstr_override[0], FunctionSig)
            ):
                docstr_override = cast(list[FunctionSig], docstr_override)
                return Overridden(docstr_override)

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
            sigs = infer_sig_from_docstring(docstr, name)
            if sigs:
                return Overridden(sigs)
            if self.strict and not sigs:
                raise ValueError(f"Could not convert override to signatures\n{docstr}")
        return None

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        """Main override to apply the signature overrides"""
        from stubgenlib.utils import merge_signature_kwargs

        results: list[FunctionSig] | None = self.get_overridden_signatures(ctx)
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
        type_override = self._property_type_overrides_matcher.find_result_match(
            ctx.fullname, ret_type
        )
        if type_override is not None:
            return type_override
        else:
            return ret_type
