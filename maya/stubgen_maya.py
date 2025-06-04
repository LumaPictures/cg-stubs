from __future__ import absolute_import, annotations, division, print_function

import argparse
import inspect
import sys
from typing import Any

import mypy.stubgen
import mypy.stubgenc
from mypy.stubdoc import ArgSig, FunctionSig
from mypy.stubgenc import SignatureGenerator
from mypy.stubutil import FunctionContext

import stubgenlib.moduleinspect
from stubgenlib.siggen import (
    AdvancedSigMatcher,
    AdvancedSignatureGenerator,
)

stubgenlib.moduleinspect.patch()

import pymel.internal.cmdcache

pymel.internal.cmdcache.CmdCache.version = "2023"
cmdcache = pymel.internal.cmdcache.CmdCache()
data = cmdcache.load()
datamap = dict(zip(cmdcache.cacheNames(), data))
CMDLIST = datamap["cmdlist"]  # type: pymel.internal.cmdcache.CommandInfo


def flag_has_mode(flag_info, mode):
    return mode in flag_info.get("modes", [])


class MayaSignatureGenerator(SignatureGenerator):
    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        if ctx.module_name == "maya.cmds":
            try:
                cmd_info = CMDLIST[ctx.name]
            except KeyError:
                print(f"No command info found for {ctx.name}")
                return None

            try:
                cmd_flags = cmd_info["flags"]
            except KeyError:
                print(f"No flag info found for {ctx.name}")
                return None

            args = [ArgSig("*args")] + self._get_args(cmd_flags)
            return [FunctionSig(ctx.name, args=args, ret_type="Any")]

    def _mel_type_to_python_type(self, typ, as_result=False) -> str:
        """Convert a mel type to a python type"""
        if isinstance(typ, str):
            if typ == "timerange":
                # FIXME: tuple support may be pymel-specific
                return "str | tuple[float, float] | tuple[float]"
            elif typ == "floatrange":
                return "str | int | float"
            elif typ == "time":
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

    def _get_flag_type(
        self, flag_info: "pymel.internal.cmdcache.flag_info", as_result=False
    ) -> str:
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

    def _get_args(self, cmd_flags, skip=None) -> list[ArgSig]:
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
            short_name = flag_info["shortname"]
            if skip and (flag_name in skip or short_name in skip):
                continue

            typ = self._get_flag_type(flag_info, as_result=False)
            if flag_has_mode(flag_info, "query") and typ != "bool | int":
                typ = "bool | int | %s" % typ

            add_arg(flag_name, typ)
            add_arg(short_name, typ)

        return new_args

    # def get_property_type(self, default_type: str | None, ctx: FunctionContext) -> str | None:
    #     """Infer property type from docstring or docstring signature."""
    #     pass


# FIXME: this class gets instantiated for each module.  break this into two separate classes.
class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [MayaSignatureGenerator()]

    def get_obj_module(self, obj: object) -> str | None:
        """Return module name of the object."""
        module = super().get_obj_module(obj)
        if (
            module
            and self.module_name.startswith("maya.api.Open")
            and module.startswith("Open")
        ):
            return self.module_name
        elif module and self.module_name == "maya.cmds" and inspect.isfunction(obj):
            return self.module_name
        return module

    def is_function(self, obj: object) -> bool:
        if self.module_name == "maya.cmds" or self.module_name.startswith("maya.api."):
            return inspect.isbuiltin(obj) or inspect.isfunction(obj)
        else:
            return super().is_function(obj)

    def is_method(self, class_info: ClassInfo, name: str, obj: object) -> bool:
        if self.module_name.startswith("maya.api."):
            return inspect.ismethoddescriptor(obj) or type(obj) in (
                type(str.index),
                type(str.__add__),
                type(str.__new__),
            )
        else:
            # this is valid because it is only called on members of a class
            return inspect.isfunction(obj)

    def is_classmethod(self, class_info: ClassInfo, name: str, obj: object) -> bool:
        if self.module_name.startswith("maya.api."):
            return inspect.isbuiltin(obj) or type(obj).__name__ in (
                "classmethod",
                "classmethod_descriptor",
            )
        else:
            return inspect.ismethod(obj)

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        members = super().get_members(obj)
        return sorted(members, key=lambda x: x[0])

    # def set_defined_names(self, defined_names: set[str]) -> None:
    #     super().set_defined_names(defined_names)
    #     for typ in ["Any", "Self", "Iterable", "Mapping"]:
    #         self.add_name(f"typing.{typ}", require=False)


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[attr-defined,misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python stub generator for Nuke")
    parser.add_argument("outdir", help="The path to the output directory")
    args = parser.parse_args()

    print("initializing maya")
    import maya.standalone

    maya.standalone.initialize()
    print("done")

    sys.argv[1:] = ["-p=maya.app", "--parse-only", f"-o={args.outdir}"]
    mypy.stubgen.main()

    sys.argv[1:] = [
        "-m=maya.cmds",
        "-p=maya.api",
        "--inspect-mode",
        f"-o={args.outdir}",
    ]
    mypy.stubgen.main()
