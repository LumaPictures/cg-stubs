from __future__ import absolute_import, annotations, division, print_function

import re
import ast

import mypy.stubgen
import mypy.stubgenc
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator

from stubgenlib import (
    AdvancedSignatureGenerator,
    AdvancedSigMatcher,
    SignatureFixer,
    CppTypeConverter,
)


tupleTypeRegex = re.compile("^_([a-zA-Z0-9]+)Tuple$")
tupleGenTypeRegex = re.compile("^_([a-zA-Z0-9]+)TupleGenerator$")


def is_std(node: ast.AST, attr: str) -> bool:
    if (
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "std"
        and node.attr == attr
    ):
        return True
    return False


class AnnotationFixer(ast.NodeTransformer):
    """
    This class is used for advance transformations to type annotations.

    For example those that require unwrapping a generic, or altering lists.
    """

    def transform(self, type_str: str) -> str:
        """Entry point to transform a type string"""
        node = ast.parse(type_str)
        # print(ast.dump(node, indent=4))
        new_node = self.visit(node)
        return ast.unparse(new_node)

    def visit_Tuple(self, node: ast.Tuple) -> ast.AST:
        elts = []
        for child in node.elts:
            if isinstance(child, ast.Subscript) and (
                is_std(child.value, "allocator") or is_std(child.value, "less")
            ):
                continue
            else:
                elts.append(child)
        if len(elts) != node.elts:
            if len(elts) == 1:
                return self.visit(elts[0])
            else:
                node = ast.Tuple(elts, ast.Load())
        return self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> ast.AST:
        if isinstance(node.value, ast.Name) and node.value.id in (
            "ElemPtr",
            "UT_SharedPtr",
        ):
            # convert:  ElemPtr[Foo]  -->  Foo
            return node.slice

        new_node = self.generic_visit(node)
        if isinstance(new_node, ast.Subscript) and is_std(new_node.value, "vector"):
            # NOTE: we use Tuple instead of Tuple because of Parm.Tuple()
            # convert:  std.vector[Foo]  -->  Tuple[Foo, ...]
            return ast.Subscript(
                value=ast.Name(id="Tuple", ctx=ast.Load()),
                slice=ast.Tuple(
                    elts=[new_node.slice, ast.Constant(value=Ellipsis)], ctx=ast.Load()
                ),
                ctx=ast.Load(),
            )
        return new_node


class DefaultSigGenerator(SignatureGenerator):
    """Sig Gen that uses the signature extracted from the source code"""

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        return [default_sig]


class HoudiniCppTypeConverter(CppTypeConverter):
    TUPLE_TYPES = {
        "_StringTuple": "str",
        "_StringTupleTuple": "Sequence[str]",
        "_IntTuple": "int",
        "_IntTupleTuple": "Sequence[int]",
        "_Int64Tuple": "int",
        "_BoolTuple": "bool",
        "_FloatTuple": "float",
        "_FloatTupleTuple": "Sequence[float]",
        "_DoubleTuple": "float",
        "_DoubleTupleTuple": "Sequence[float]",
        "_PointTupleTuple": "Sequence[Point]",
        "_IKTargetTuple": "_ik_Target",
        "_EnumTuple": "EnumValue",
    }

    TYPE_MAP = [
        (r"\bHOM_PtrOrNull\b", "Optional"),
        (r"\bHOM_OptionalDouble\b", "Optional[float]"),
        (r"\bHOM_OptionalInt\b", "Optional[int]"),
        (r"\bHOM_BinaryString\b", "bytes"),
        # HOM classes that have underscores
        (r"\bHOM_logging_LogEntry\b", "_logging_LogEntry"),
        (r"\bHOM_logging_MemorySink\b", "_logging_MemorySink"),
        (r"\bHOM_ik_Joint\b", "_ik_Joint"),
        (r"\bHOM_ik_Skeleton\b", "_ik_Skeleton"),
        (r"\bHOM_ik_Target\b", "_ik_Target"),
        (r"\bHOM_clone_Connection\b", "_clone_Connection"),
        # other
        (r"\bHOM_IterableList\b", "Iterator"),
        (r"\bHOM_NodeBundle\b", "Bundle"),
        (r"\bInterpreterObject\b", "Any"),
        (r"\bhboost::any\b", "Any"),
        (r"\bPyObject\b", "Any"),
        (r"\bUT_Tuple\b", "Tuple"),
        (r"\bswig::SwigPyIterator\b", "Self"),
        (r"\bUT_InfoTree\b", "NodeInfoTree"),
    ] + CppTypeConverter.TYPE_MAP

    # Don't replace vector with list.  Instead, we'll replace std.vector with
    # Tuple in AnnotationFixer
    RESULT_TYPE_MAP = []

    def to_python_id(self, cpp_type):
        py_type = cpp_type.replace("HOM_", "")
        sub_type = self.TUPLE_TYPES.get(py_type)
        if sub_type is not None:
            py_type = f"Sequence[{sub_type}]"
        else:
            match = tupleTypeRegex.match(py_type)
            if match:
                sub_type = match.groups()[0]
                py_type = f"Sequence[{sub_type}]"
        return py_type

    def process_ptr(self, converted_type: str, is_result: bool) -> str:
        if is_result:
            return f"Optional[{converted_type}]"
        else:
            return converted_type


class HoudiniTypeFixer(SignatureFixer):
    converter = HoudiniCppTypeConverter()
    transfomer = AnnotationFixer()

    def maybe_add_optional(self, type_name: str, default_value: str | None):
        if default_value == "None" and not (
            type_name.startswith("Optional[")
            or type_name.startswith("typing.Optional[")
        ):
            return f"Optional[{type_name}]"
        else:
            return type_name

    def cleanup_type(
        self,
        type_name: str,
        ctx: FunctionContext,
        is_result: bool,
        default_value: str | None = None,
    ) -> str:
        if type_name.startswith("'") and type_name.endswith("'"):
            type_name = type_name[1:-1]
        new_type = self.converter.cpp_arg_to_py_type(type_name, is_result)
        new_type = self.transfomer.transform(new_type)
        new_type = self.maybe_add_optional(new_type, default_value)
        return new_type


class HoudiniSignatureGenerator(AdvancedSignatureGenerator):
    sig_matcher = AdvancedSigMatcher(
        signature_overrides={
            # signatures for these special methods include many inaccurate overloads
            "*.__ne__": "(self, other: object) -> bool",
            "*.__eq__": "(self, other: object) -> bool",
            "*.__lt__": "(self, other: object) -> bool",
            "*.__le__": "(self, other: object) -> bool",
            "*.__gt__": "(self, other: object) -> bool",
            "*.__ge__": "(self, other: object) -> bool",
            "*.applicationVersion": "(include_patch: bool = False) -> Tuple[int, int, int]",
            "*.expandString": "(text: str) -> str",
            # "*.expandStringAtFrame": "(text: str, frame_number: float) -> str",
            "*.runVex": "(vex_file: str, inputs: dict[str, Any], precision: Literal['32', '64'] = '32') -> dict[str, Any]",
            "*.startHoudiniEngineDebugger": "(portOrPipeName: Union[int, str]) -> None",
            "*.NetworkMovableItem.shiftPosition": "(self, vector2: Union[Sequence[float], Vector2]) -> None",
            "*.Node.simulation": "(self) -> DopSimulation",
            "*.Node.setInput": "(self, input_index: int, item_to_become_input: Optional[NetworkMovableItem], output_index: int = 0) -> None",
            "*.Node.setFirstInput": "(self, item_to_become_input: Optional[NetworkMovableItem], output_index: int = 0) -> None",
            "*.Node.setParms": "(self, parm_dict: dict[str, Any]) -> None",
            "*.Node.setParmExpressions": "(self, parm_dict: dict[str, Any], language: Optional[EnumValue] = None, replace_expressions: bool = True) -> None",
            "*.Node.parmTemplateGroup": "(self) -> ParmTemplateGroup",
            "*.Node.addSpareParmTuple": "(self, parm_template: ParmTemplate, in_folder: Tuple[str, ...] = ..., create_missing_folders: bool = False) -> ParmTuple",
            "*.Node.layoutChildren": "(self, items: Sequence[NetworkMovableItem] = ..., horizontal_spacing: float = 1.0, vertical_spacing: float = 1.0) -> None",
            "*.Node.createOutputNode": "(self, node_type_name: str, node_name: Optional[str] = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> T",
            "*.Node.createInputNode": "(self, input_index: int, node_type_name: str, node_name: Optional[str] = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> T",
            "*.Node.creationTime": "(self) -> datetime.datetime",
            "*.Node.modificationTime": "(self) -> datetime.datetime",
            "*.Node.inputs": "(self) -> Tuple[T, ...]",
            # "*.Node.input": "(self, inputidx: int) -> T",
            "*.Node.outputs": "(self) -> Tuple[T, ...]",
            "*.LopNode.displayNode": "(self) -> LopNode",
            "*.LopNode.setLastModifiedPrims": "(self, primPaths: Sequence[str]) -> None",
            "*.Geometry.addAttrib": "(self, type: EnumValue, name: str, default_value: Any, transform_as_normal: bool = True, create_local_variable: bool = True) -> Attrib",
            "*.Geometry.setGlobalAttribValue": "(self, name_or_attrib: Union[str, Attrib], attrib_value: Any) -> None",
            "*.StickyNote.setSize": "(self, size: Union[Sequence[float], Vector2]) -> None",
            "*.Parm.set": "(self, value: Union[int, float, str, Parm, Ramp], language: Optional[EnumValue] = None, follow_parm_reference: bool = True) -> None",
            "*.ParmTuple.__iter__": "(self) -> Iterator[Parm]",
            "*.ParmTuple.set": "(self, value: Union[Iterable[int], Iterable[float], Iterable[str], Iterable[Parm], ParmTuple], language: Optional[EnumValue] = None, follow_parm_reference: bool = True) -> None",
            "*.ParmTemplate.conditionals": "(self) -> dict[EnumValue, str]",
            "*.ParmTemplate.setTags": "(self, tags: dict[str, str]) -> None",
            "*.DataParmTemplate.__init__": "(self, name: , label: , num_components: int, look: EnumValue = parmLook.Regular, naming_scheme: EnumValue = parmNamingScheme.XYZW, unknown_str: Optional[str] = None, disable_when: Optional[str] = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: dict[str, str] = {}, unknown_dict: dict[EnumValue, str] = {}, default_expression: Sequence[str] = (), default_expression_language: Sequence[EnumValue] = ()) -> DataParmTemplate",
            "*.FolderSetParmTemplate.folderNames": "(self) -> list[str]",
            "*.FolderSetParmTemplate.setFolderNames": "(self, folder_names: Sequence[str]) -> None",
            "*.MenuParmTemplate.setDefaultExpressionLanguage": "(self, default_expression_language: EnumValue) -> None",
            "*.Vector2.__iter__": "(self) -> Iterator[float]",
            "*.Vector3.__iter__": "(self) -> Iterator[float]",
            "*.Vector4.__iter__": "(self) -> Iterator[float]",
            "*.Matrix2.__init__": "(self, values: Union[int, float, Iterable[Union[int, float]], Iterable[Iterable[Union[int, float]]]] = 0) -> Matrix2",
            "*.Matrix3.__init__": "(self, values: Union[int, float, Iterable[Union[int, float]], Iterable[Iterable[Union[int, float]]]] = 0) -> Matrix3",
            "*.Matrix4.__init__": "(self, values: Union[int, float, Sequence[Union[int, float]], Sequence[Sequence[Union[int, float]]]] = 0) -> Matrix4",
            "*.Take.name": "(self) -> str",
            "*.Prim.setIntrinsicValue": "(self, intrinsic_name: str, value: Union[int, float, str, Iterable[int], Iterable[float], Iterable[str]]) -> None",
            "*.Prim.voxelRange": "(self, range: BoundingBox) -> Union[Tuple[bool, ...], Tuple[int, ...], Tuple[float, ...], Tuple[Vector3, ...]]",
            "*.Prim.voxelRangeAsBool": "(self, range: BoundingBox) -> Tuple[bool, ...]",
            "*.Prim.voxelRangeAsInt": "(self, range: BoundingBox) -> Tuple[int, ...]",
            "*.Prim.voxelRangeAsFloat": "(self, range: BoundingBox) -> Tuple[float, ...]",
            "*.Prim.voxelRangeAsVector3": "(self, range: BoundingBox) -> Tuple[Vector3, ...]",
            "*.Keyframe.__init__": "(self, value: Optional[float] = None, time: Optional[float] = None) -> None",
            "*.Keyframe.__init__": "(self, expression: Optional[str] = None, time: Optional[float] = None, language: Optional[EnumValue] = exprLanguage.Python) -> None",
            "*.SceneViewer.groupListMask": "(self) -> str",
            "*.SceneViewer.isGroupPicking": "(self) -> bool",
            "*.SceneViewer.selectGeometry": "(self, prompt: str = 'Select geometry', sel_index: int = 0, allow_drag: bool = False, quick_select: bool = False, use_existing_selection: bool = True, initial_selection: Optional[str] = None, initial_selection_type: Optional[EnumValue] = None, ordered: bool = False, geometry_types: Sequence[EnumValue] = ..., primitive_types: Sequence[EnumValue] = ..., allow_obj_sel: bool = True, icon: Optional[str] = None, label: Optional[str] = None, prior_selection_paths: list = ..., prior_selection_ids: list = ..., prior_selections: list = ..., allow_other_sops: bool = True, consume_selections: bool = True) -> GeometrySelection",
            "*.ViewportVizualizer.setParm": "(self, parm_name: str, value: Union[int, float, str]) -> None",
            "*.NetworkEditor.flashMessage": "(self, image: Optional[str], message: Optional[str], duration: float) -> None",
            "*.NetworkEditor.registerPref": "(self, pref: str, value: str, _global: bool) -> None",
            "*.Selection.numSelected": "(self) -> int",
            "*.NodeInfoTree.__init__": "(self, tree_root: Any, tree: Any) -> None",
            "*.PerfMonProfile.stats": "(self) -> dict[str, Any]",
            "*.SwigPyIterator.__sub__": "(self, n: int) -> Any",
            "*.OperationFailed.__init__": "(self, message: Optional[str] = ...) -> None",
            "*.AgentMetadata.data": "(self) -> dict[str, Any]",
            "*.AgentMetadata.setData": "(self, data: dict[str, Any]) -> None",
            "*.AgentMetadata.setMetadata": "(self, item_id: str, metadata: dict[str, Any]) -> None",
            "*.ChannelGraph.selectedKeyframes": "(self) -> dict[Parm, Tuple[BaseKeyframe, ...]]",
            "*.GeometryViewport.changeType": "(self, type: EnumValue) -> None",
            "*._StringMapDoubleTuple.__iter__": "(self) -> Iterator[str]",
            # "*.VopNode.deleteIndependentInputNodes": "(self, input_index: int, make_parm_node: bool, reference_input_defaults: Any) -> bool",
            "*.hda.reloadHDAModule": "(self, hda_module: HDAModule) -> None",
            "*.hmath.buildTransform": "(self, values_dict: dict[str, Union[Vector3, Sequence[float]]], transform_order: str = 'srt', rotate_order: str = 'xyz') -> Matrix4",
            "*.playbar.setChannelList": "(arg: ChannelList) -> None",
            "*.hotkeys.assignments": "(self, hotkey_symbol: str) -> list[str]",
            "*.qt.mainWindow": "(self) -> QtWidgets.QMainWindow",
            "*.qt.Icon": "(self, icon_name: str, width: Optional[int] = None, height: Optional[int] = None) -> QtGui.QIcon",
            "*.ui.displayConfirmation": "(self, text: str, severity: EnumValue = severityType.Message, help: Optional[str] = None, title: Optional[str] = None, details: Optional[str] = None, destails_label: Optional[str] = None, destails_expanded: bool = False) -> bool",
            "*.ui.hasDragSourceData": "(label: str, index: int) -> bool",
            "*.ui.selectFile": "(self, start_directory: Optional[str] = None, title: Optional[str] = None, collapse_sequences: bool = False, file_type: EnumValue = fileType.Any, pattern: Optional[str] = None, default_value: Optional[str] = None, multiple_select: bool = False, image_chooser: bool = False, chooser_mode: EnumValue = fileChooserMode.ReadAndWrite, width: int = 0, height: int = 0) -> str",
            "*.webServer.registerOpdefPath": "(self, prefix: str) -> None",
        }
    )


class ASTStubGenerator(mypy.stubgen.ASTStubGenerator):
    def visit_class_def(self, o) -> None:
        # filter _*Tuple classes, they are not used (See to_python_id).
        if (
            o.name in ("SwigPyIterator", "_AgentDefnMap")
            or tupleTypeRegex.match(o.name)
            or tupleGenTypeRegex.match(o.name)
        ):
            return

        return super().visit_class_def(o)

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [
            HoudiniSignatureGenerator(
                fallback_sig_gen=HoudiniTypeFixer(
                    DefaultSigGenerator(), default_sig_handling="ignore"
                )
            )
        ]

    def get_signatures(
        self,
        default_signature: FunctionSig,
        sig_generators: list[SignatureGenerator],
        func_ctx: FunctionContext,
    ) -> list[FunctionSig]:
        if (
            func_ctx.class_info
            and func_ctx.class_info.name[0].islower()
            and not func_ctx.name.startswith("__")
        ):
            self._decorators.append("@staticmethod")
            if default_signature.args[0].name == "self":
                default_signature.args.pop(0)
        return super().get_signatures(default_signature, sig_generators, func_ctx)

    def get_imports(self) -> str:
        imports = super().get_imports()
        imports += "\nimport typing\nfrom typing import Any, Iterator, Optional, Sequence, Self, Tuple\n"
        return imports


mypy.stubgen.ASTStubGenerator = ASTStubGenerator  # type: ignore[attr-defined,misc]
# mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]


def enableHouModule():
    """Set up the environment so that "import hou" works."""
    import sys, os

    # Importing hou will load Houdini's libraries and initialize Houdini.
    # This will cause Houdini to load any HDK extensions written in C++.
    # These extensions need to link against Houdini's libraries,
    # so the symbols from Houdini's libraries must be visible to other
    # libraries that Houdini loads.  To make the symbols visible, we add the
    # RTLD_GLOBAL dlopen flag.
    if hasattr(sys, "setdlopenflags"):
        old_dlopen_flags = sys.getdlopenflags()
        sys.setdlopenflags(old_dlopen_flags | os.RTLD_GLOBAL)

    # For Windows only.
    # Add %HFS%/bin to the DLL search path so that Python can locate
    # the hou module's Houdini library dependencies.  Note that
    # os.add_dll_directory() does not exist in older Python versions.
    # Python 3.7 users are expected to add %HFS%/bin to the PATH environment
    # variable instead prior to launching Python.
    if sys.platform == "win32" and hasattr(os, "add_dll_directory"):
        os.add_dll_directory("{}/bin".format(os.environ["HFS"]))

    try:
        import hou
    finally:
        # Reset dlopen flags back to their original value.
        if hasattr(sys, "setdlopenflags"):
            sys.setdlopenflags(old_dlopen_flags)


enableHouModule()


def main(outdir: str):
    mypy.stubgen.main(
        ["-m=hou", "--verbose", "--parse-only", "--include-docstrings", "-o", outdir]
    )

    # print(AnnotationFixer().transform('Tuple[str, ...]'))
    # print(AnnotationFixer().transform('std.vector[str]'))
