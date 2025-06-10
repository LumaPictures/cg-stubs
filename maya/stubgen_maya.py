from __future__ import absolute_import, annotations, division, print_function

import argparse
import inspect
from typing import Any

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

stubgenlib.moduleinspect.patch()


def flag_has_mode(flag_info, mode):
    return mode in flag_info.get("modes", [])


class MayaCmdSignatureGenerator(SignatureGenerator):
    def __init__(self):
        import pymel.internal.cmdcache

        pymel.internal.cmdcache.CmdCache.version = "2023"
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

    # def get_property_type(self, default_type: str | None, ctx: FunctionContext) -> str | None:
    #     """Infer property type from docstring or docstring signature."""
    #     pass


class CmdsStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [MayaCmdSignatureGenerator()]

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
        for typ in ["Callable"]:
            self.add_name(f"typing.{typ}", require=False)


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
            return self.module_name
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


delegate = GeneratorDelegate[mypy.stubgen.InspectionStubGenerator](
    rules={
        "maya.api.*": APIStubGenerator,
        "maya.cmds": CmdsStubGenerator,
    },
    fallback=mypy.stubgen.InspectionStubGenerator,
)

mypy.stubgen.InspectionStubGenerator = delegate  # type: ignore[attr-defined,misc]
mypy.stubgenc.InspectionStubGenerator = delegate  # type: ignore[misc]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python stub generator for Nuke")
    parser.add_argument("outdir", help="The path to the output directory")
    args = parser.parse_args()

    print("initializing maya")
    import maya.standalone

    maya.standalone.initialize()
    print("done")

    mypy.stubgen.main(["-p=maya.app", "--parse-only", f"-o={args.outdir}"])

    mypy.stubgen.main(
        [
            "-m=maya.cmds",
            "-p=maya.api",
            "-p=ufe",
            "--inspect-mode",
            f"-o={args.outdir}",
        ]
    )
