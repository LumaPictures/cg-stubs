from collections.abc import Iterable, Sequence
from typing import TypeAlias

import hou
import hutil.cppinline

_StructDescription: TypeAlias = tuple[str, str | Sequence[tuple[str, str]]]
_ExtendableClass: TypeAlias = (
    type[hou.Node]
    | type[hou.ParmTuple]
    | type[hou.NodeType]
    | type[hou.NodeTypeCategory]
    | type[hou.Track]
    | type[hou.DopData]
    | type[hou.Vector2]
    | type[hou.Vector3]
    | type[hou.Vector4]
    | type[hou.Matrix3]
    | type[hou.Matrix4]
    | type[hou.BoundingBox]
    | type[hou.Color]
    | type[hou.Quaternion]
    | type[hou.Ramp]
    | type[hou.Geometry]
)

_hou_classes_to_cpp_class_names: dict[_ExtendableClass, str]

class HcustomCompilerHook(hutil.cppinline.CompilerHook):
    def default_shared_library_directory(self) -> str: ...
    def find_shared_library(self, shared_library_file_name: str) -> str | None: ...
    def get_compile_command(
        self,
        cpp_file_path: str,
        output_shared_library_path: str,
        debug: bool,
        include_dirs: Iterable[str],
        link_dirs: Iterable[str],
        link_libs: Iterable[str],
    ) -> str: ...
    def clean_up_after_compiling(
        self,
        cpp_file_path: str,
        output_shared_library_path: str,
        debug: bool,
        include_dirs: Iterable[str],
        link_dirs: Iterable[str],
        link_libs: Iterable[str],
    ) -> None: ...

class ConstGU_DetailHandle(hutil.cppinline.ConverterHandle):
    gu_detail_handle: hou._GUDetailHandle
    def __init__(self, geometry: hou.Geometry) -> None: ...
    def as_pointer(self) -> int: ...
    def destroy(self) -> None: ...

class GU_DetailHandle(ConstGU_DetailHandle):
    def __init__(self, geometry: hou.Geometry) -> None: ...

def createLibrary(
    name: str,
    includes: str = ...,
    function_sources: Sequence[str] = ...,
    debug: bool = ...,
    catch_crashes: bool | None = ...,
    acquire_hom_lock: bool = ...,
    structs: Sequence[_StructDescription] = ...,
    include_dirs: Sequence[str] = ...,
    link_dirs: Sequence[str] = ...,
    link_libs: Sequence[str] = ...,
    config: hutil.cppinline.Config | None = ...,
) -> hutil.cppinline._Library: ...
def extendClass(
    cls: _ExtendableClass,
    library_name: str,
    includes: str = ...,
    function_sources: Sequence[str] = ...,
    debug: bool = ...,
    catch_crashes: bool | None = ...,
    structs: Sequence[_StructDescription] = ...,
    auto_add_include: bool = ...,
    include_dirs: Sequence[str] = ...,
    link_dirs: Sequence[str] = ...,
    link_libs: Sequence[str] = ...,
    config: hutil.cppinline.Config | None = ...,
) -> None: ...
