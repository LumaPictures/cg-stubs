from __future__ import absolute_import, annotations, division, print_function

import os
import pathlib
import re
from typing import Any

import mypy.stubgen
import mypy.stubgenc
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator

import Callbacks.Callbacks  # type: ignore[import]
from Callbacks.Callbacks import _TypeEnum  # type: ignore[import]

from stubgenlib import (
    get_mypy_ignore_directive,
    AdvancedSignatureGenerator,
    FixableCDocstringSigGen,
    FixableDocstringSigGen,
    CFunctionStub,
    Notifier,
    DocstringTypeFixer,
    Optionality,
)

notifier = Notifier()


class KatanaDocstringTypeFixer(DocstringTypeFixer):
    SPECIAL_REPLACEMENTS = [
        ("FnGeolib", "PyFnGeolib"),
        ("FnAttribute", "PyFnAttribute"),
        ("FnGeolibServices", "PyFnGeolibServices"),
        ("FnGeolibProducers", "PyFnGeolibProducers"),
        (
            r"PyFnGeolib.GeolibRuntime\.Transaction",
            "PyFnGeolib.GeolibRuntimeTransaction",
        ),
        (r"PyFnGeolib.GeolibRuntime\.Op", "PyFnGeolib.GeolibRuntimeOp"),
        (r"NodegraphAPI\.LiveGroupMixin", "NodegraphAPI.LiveGroup.LiveGroupMixin"),
    ]

    def get_replacements(self, is_return: bool) -> list[tuple[str, str]]:
        return super().get_replacements(is_return) + self.SPECIAL_REPLACEMENTS

    def get_full_name(self, type_name: str) -> str:
        # FIXME: would be nice to have something that can do a search through known objects
        absolute_names = (
            (
                "TerminalOpDelegate",
                "Nodes3DAPI.TerminalOpDelegates.TerminalOpDelegate.TerminalOpDelegate",
            ),
            ("Nodes?", "NodegraphAPI.Node"),
            ("GroupNode", "NodegraphAPI.GroupNode"),
            ("Port", "NodegraphAPI.Port"),
            ("GraphState", "NodegraphAPI.GraphState"),
            ("Op", "PyFnGeolib.GeolibRuntimeOp"),
            ("WorkingSet", "PyUtilModule.WorkingSet.WorkingSet"),
            ("PortOpClient", "Nodes3DAPI.PortOpClient.PortOpClient"),
            ("GroupAttribute", "PyFnAttribute.GroupAttribute"),
            ("Package", "PackageSuperToolAPI.Packages.Package"),
            # stuubgen will add imported modules that it discovers to generated
            # output, but types in docstrings may refer to modules that are not
            # imported into the module namespace.  e.g. QtCore. Forcing to the
            # full path will ensure that an import is added. An alternative may
            # be to register `import PyQt5.QtCore as QtCore' in every module:
            # it's likely that the imports will only be added if the imported
            # object is actually used.
            ("(Qt.*)", r"PyQt5.\1"),
        )
        for short_name, full_name in absolute_names:
            type_name = re.sub(
                r"(?<![A-Za-z0-9._]){}\b".format(short_name), full_name, type_name
            )
        return type_name


class KatanaDocstringSignatureGenerator(
    KatanaDocstringTypeFixer, FixableDocstringSigGen
):
    # FIXME: implement?
    def get_property_type(
        self, default_type: str | None, ctx: FunctionContext
    ) -> str | None:
        return default_type


class KatanaCSignatureGenerator(KatanaDocstringTypeFixer, FixableCDocstringSigGen):
    pass


class KatanaSignatureGenerator(AdvancedSignatureGenerator):
    signature_overrides: dict[str, str | list[str]] = {
        # these docstring sigs are malformed
        "NodegraphAPI_cmodule.GraphState.edit": "(self) -> GraphStateBuilder",
        "NodegraphAPI_cmodule.GraphState.getDynamicEntry": "(self, path: str)",
        "NodegraphAPI_cmodule.GraphState.getOpSystemArgs": "(self) -> GroupAttribute",
        "NodegraphAPI_cmodule.GraphState.getStaticEntry": "(self, path: str)",
        "NodegraphAPI_cmodule.Node.getInputPort": "(self, name: str) -> Port | None",
        "NodegraphAPI_cmodule.Node.getOutputPort": "(self, name: str) -> Port | None",
        "NodegraphAPI_cmodule.Node.getParameterValue": "(self, name: str, time: float)",
    }
    # FIXME: enabling these creates an explosion of errors to resolve.
    # optional_result = [
    #     "NodegraphAPI_cmodule.Node.getInputPortByIndex",
    #     "NodegraphAPI_cmodule.Node.getOutputPortByIndex",
    #     "NodegraphAPI_cmodule.Node.getParameter",
    #     "NodegraphAPI_cmodule.GroupNode.getChild",
    #     "NodegraphAPI_cmodule.Parameter.getChild",
    #     "NodegraphAPI_cmodule.Parameter.getChildByIndex",
    #     "NodegraphAPI_cmodule.Port.getPort",
    #     "PyFnAttribute.GroupAttribute.getChildByIndex",
    #     "PyFnAttribute.GroupAttribute.getChildByName",
    #     "PyFnGeolibProducers.GeometryProducer.getAttribute",
    #     "PyFnGeolibProducers.GeometryProducer.getChildByName",
    #     "PyFnGeolibProducers.GeometryProducer.getDelimitedGlobalAttribute",
    #     "PyFnGeolibProducers.GeometryProducer.getDelimitedLocalAttribute",
    #     "PyFnGeolibProducers.GeometryProducer.getFirstChild",
    #     "PyFnGeolibProducers.GeometryProducer.getFnAttribute",
    #     "PyFnGeolibProducers.GeometryProducer.getGlobalAttribute",
    #     "PyFnGeolibProducers.GeometryProducer.getNextSibling",
    #     "PyFnGeolibProducers.GeometryProducer.getProducerByPath",
    # ]
    arg_type_overrides = {
        # FIXME: I'm using typing.Optional here because " | None" is getting stripped
        (
            "*",
            "graphState",
            "Incomplete | None",
        ): "typing.Optional[NodegraphAPI.GraphState]",
        ("*", "graphState", None): "NodegraphAPI.GraphState",
        ("*", "port", "Incomplete | None"): "typing.Optional[NodegraphAPI.Port]",
        ("*", "port", None): "NodegraphAPI.Port",
        ("*", "node", "Incomplete | None"): "typing.Optional[NodegraphAPI.Node]",
        ("*", "node", None): "NodegraphAPI.Node",
        (
            "*",
            "producer",
            "Incomplete | None",
        ): "typing.Optional[PyFnGeolibProducers.GeometryProducer]",
        ("*", "producer", None): "PyFnGeolibProducers.GeometryProducer",
        ("*", "*Callback", "Incomplete | None"): "typing.Optional[typing.Callable]",
        ("*", "*Callback", None): "typing.Callable",
        ("Nodes3DAPI.RenderNodeUtil.SyncOutputPorts", "node", "*"): "NodegraphAPI.Node",
        (
            "Nodes3DAPI.RenderNodeUtil.GetRenderNodeInfo",
            "node",
            "*",
        ): "NodegraphAPI.Node",
    }
    result_type_overrides = {
        # None means the type is unset/unknown
        ("NodegraphAPI_cmodule.*.getNode", "Any"): "Node",
        ("*.getNode", None): "NodegraphAPI.Node",
        (
            "NodegraphAPI_cmodule.Parameter.getValue",
            "*",
        ): "Any",
        ("NodegraphAPI_cmodule.GroupNode.getChild", "*"): "Node",
        ("NodegraphAPI_cmodule.GroupNode.getChildren", "*"): "list[Node]",
        ("NodegraphAPI_cmodule.Parameter.getChildren", "*"): "list[Parameter]",
        ("NodegraphAPI_cmodule.Port.getConnectedPorts", "*"): "list[Port]",
        ("PyFnAttribute.GroupAttribute.childList", "*"): "list[tuple[str, Attribute]]",
        (
            "PyFnGeolibProducers.GeometryProducer_childIter.__next__",
            "*",
        ): "GeometryProducer",
        (
            "PyFnGeolibProducers.GeometryProducer.getFlattenedGlobalXform",
            "*",
        ): "tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float]",
        (
            "drawing_cmodule.nodeWorld_getBounds",
            "*",
        ): "tuple[float, float, float, float]",
        (
            "drawing_cmodule.nodeWorld_getBoundsOfListOfNodes",
            "*",
        ): "tuple[float, float, float, float]",
    }
    optional_args = {
        (
            "UI4.FormMaster.KatanaFactory.KatanaWidgetFactoryClass.buildWidget",
            "policy",
            "*",
        ): Optionality(accepts_none=True, has_default=False),
    }

    def get_property_type(
        self, default_type: str | None, ctx: FunctionContext
    ) -> str | None:
        return self.fallback_sig_gen.get_property_type(default_type, ctx)


class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    DATA_ATTRS = {
        "DataAttribute": "T",
        "DoubleAttribute": "float",
        "FloatAttribute": "float",
        "IntAttribute": "int",
        "StringAttribute": "str",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.known_modules.extend(["PyQt5.QtCore", "PyQt5.QtWidgets", "PyQt5.QtGui"])
        # preserve original sorting to redude the diff, for now
        self.resort_members = True

    def get_sig_generators(self) -> list[SignatureGenerator]:
        if self.is_c_module:
            return [
                KatanaSignatureGenerator(fallback_sig_gen=KatanaCSignatureGenerator())
            ]
        else:
            return [
                KatanaSignatureGenerator(
                    fallback_sig_gen=KatanaDocstringSignatureGenerator()
                )
            ]

    def should_reexport(self, name: str, full_module: str, name_is_alias: bool) -> bool:
        # the usual logic breaks down because Katana has so many damned packages
        return full_module in self.known_modules

    def is_defined_in_module(self, obj: object) -> bool:
        # _TypeEnum is a type, but it's created dynamically.  This change ensures
        # that we don't assume things of type _TypeEnum are external to their
        # current module and should thus be imported.
        return super().is_defined_in_module(obj) or type(obj).__name__ == "_TypeEnum"

    def set_defined_names(self, defined_names: set[str]) -> None:
        super().set_defined_names(defined_names)
        for typ in ["Tuple", "Set"]:
            self.add_name(f"typing.{typ}", require=True)

    def strip_or_import(self, type_name: str) -> str:
        if not self.is_c_module and re.match("^[A-Za-z0-9_.]+$", type_name):
            parts = type_name.split(".")
            # It's impossible to get access to members of certain modules without
            # changing the import style, because the modules are replaced with
            # objects of the same name
            if (len(parts) >= 2 and parts[-2] == parts[-1]) or (
                len(parts) >= 3 and parts[-3] == parts[-2]
            ):
                self.import_tracker.add_import_from(
                    ".".join(parts[:-1]), [(parts[-1], None)]
                )
                self.import_tracker.require_name(parts[-1])
                return parts[-1]
        return super().strip_or_import(type_name)

    def get_imports(self) -> str:
        if self.module_name == "PyFnAttribute":
            self.add_name("typing.TypeVar")
            type_vars = 'T = TypeVar("T")\n'
        else:
            type_vars = ""
        imports = super().get_imports()
        return (
            get_mypy_ignore_directive(
                ["misc", "override", "attr-defined", "no-redef", "assignment"]
            )
            + imports
            + type_vars
        )

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        # Note that there is a mix of fixes here for C and non-C modules, but
        # I'm not separating them because it's easy to get mixed up
        members = dict(super().get_members(obj))

        if self.is_c_module:

            def add(x):
                members[x.__name__] = x

            if isinstance(obj, type) and obj.__name__ in self.DATA_ATTRS:
                sub_type = self.DATA_ATTRS[obj.__name__]
                is_abstract = obj.__name__ == "DataAttribute"
                # Add abstract methods that are shared by all sub-classes
                add(
                    CFunctionStub(
                        "getValue",
                        f"getValue(self, defaultValue: {sub_type} = ..., throwOnError: bool = ...) -> {sub_type}",
                        is_abstract=is_abstract,
                    )
                )
                add(
                    CFunctionStub(
                        "getData",
                        f"getData(self) -> ConstVector[{sub_type}]",
                        is_abstract=is_abstract,
                    )
                )
                add(
                    CFunctionStub(
                        "getNearestSample",
                        f"getNearestSample(self, sampleTime: float) -> ConstVector[{sub_type}]",
                        is_abstract=is_abstract,
                    )
                )
                add(
                    CFunctionStub(
                        "getSamples",
                        f"getSamples(self) -> dict[float, ConstVector[{sub_type}]]",
                        is_abstract=is_abstract,
                    )
                )
            elif isinstance(obj, type) and obj.__name__ == "ConstVector":
                add(CFunctionStub("__iter__", "__iter__(self) -> typing.Iterator[T]"))
                add(
                    CFunctionStub(
                        "__getitem__",
                        "__getitem__(self, arg0: int) -> T\n"
                        "__getitem__(self, arg0: slice) -> ConstVector[T]",
                    )
                )

            return list(members.items())
        else:
            if isinstance(obj, type) and obj.__name__ == "CallbacksManager":
                enums = {
                    x: _TypeEnum(x)
                    for x in dir(Callbacks.Callbacks.Type)
                    if not x.startswith("_")
                }
                enumType = type("_TypeEnumList", (), enums)
                enumType.__module__ = "Callbacks.Callbacks"
                members["Type"] = enumType

            return list(members.items())

    def get_base_types(self, obj: type) -> list[str]:
        bases = super().get_base_types(obj)
        if obj.__name__ in self.DATA_ATTRS or obj.__name__ == "ConstVector":
            sub_type = self.DATA_ATTRS.get(obj.__name__, "T")
            if obj.__name__ in ["DataAttribute", "ConstVector"]:
                self.add_name("typing.Generic")
                return bases + [f"Generic[{sub_type}]"]
            else:
                base = bases[0]
                return [f"{base}[{sub_type}]"]
        else:
            return bases


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]


def main(outdir: str, katana_site_dir: str) -> None:
    modules = [
        "_FnKatanaCoreUI",
        "drawing_cmodule",
        "AssetAPI_cmodule",
        "ConfigurationAPI_cmodule",
        "NodegraphAPI_cmodule",
        "Nodes2DAPI_cmodule",
        "Nodes3DAPI_cmodule",
        "PyFCurve",
        "PyFnAttribute",
        "PyFnGeolib",
        "PyFnGeolibProducers",
        "PyFnGeolibServices",
        "PyResolutionTableFn",
        "PyXmlIO",
        "RenderingAPI_cmodule",
        "PyOpenColorIO",
    ]

    args = ["-v", "--inspect-mode", "--include-private", "-o", outdir]
    for module in modules:
        args.append(f"-p={module}")

    for path in pathlib.Path(katana_site_dir).iterdir():
        if path.is_dir() and path.name[0].isupper():
            module = path.name
            if module == "PyQt5":
                continue
            args.append(f"-p={module}")

    mypy.stubgen.main(args)

    # the cg-stubs repo provides stubs for PyOpenColorIO 2.x, but Katana uses
    # OCIO 1.x until Katana 6. So we generate stubs for Katana's OCIO lib.
    # However, we make it private and only refer to it via Katana.OCIO so that
    # the Katana stubs for this lib are not used by other apps which may be using
    # differnet OCIO versions.
    out = pathlib.Path(outdir)
    out.joinpath("PyOpenColorIO.pyi").rename(out.joinpath("_PyOpenColorIO.pyi"))
