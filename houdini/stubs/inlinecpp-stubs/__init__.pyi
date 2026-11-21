import hou
import hutil.cppinline
from collections.abc import Iterable, Sequence

from typing import TypeAlias
from typing import TypeAlias
_StructDescription: TypeAlias = tuple[str, str | Sequence[tuple[str, str]]]
_ExtendableClass: TypeAlias = type[hou.Node] | type[hou.ParmTuple] | type[hou.NodeType] | type[hou.NodeTypeCategory] | type[hou.Track] | type[hou.DopData] | type[hou.Vector2] | type[hou.Vector3] | type[hou.Vector4] | type[hou.Matrix3] | type[hou.Matrix4] | type[hou.BoundingBox] | type[hou.Color] | type[hou.Quaternion] | type[hou.Ramp] | type[hou.Geometry]
class HcustomCompilerHook(hutil.cppinline.CompilerHook):
    def default_shared_library_directory(self) -> str: ...
    def find_shared_library(self, shared_library_file_name: str) -> str | None: ...
    def get_compile_command(self, cpp_file_path: str, output_shared_library_path: str, debug: bool, include_dirs: Iterable[str], link_dirs: Iterable[str], link_libs: Iterable[str]) -> str: ...
    def clean_up_after_compiling(self, cpp_file_path: str, output_shared_library_path: str, debug: bool, include_dirs: Iterable[str], link_dirs: Iterable[str], link_libs: Iterable[str]) -> None: ...

class ConstGU_DetailHandle(hutil.cppinline.ConverterHandle):
    gu_detail_handle: hou._GUDetailHandle
    def __init__(self, geometry: hou.Geometry) -> None: ...
    def as_pointer(self) -> int: ...
    def destroy(self) -> None: ...

class GU_DetailHandle(ConstGU_DetailHandle):
    def __init__(self, geometry: hou.Geometry) -> None: ...

_hou_classes_to_cpp_class_names: dict[type[object], str]

def createLibrary(name: str, includes: str = '', function_sources: Sequence[str] = ..., debug: bool = False, catch_crashes: bool | None = None, acquire_hom_lock: bool = False, structs: Sequence[_StructDescription] = ..., include_dirs: Sequence[str] = ..., link_dirs: Sequence[str] = ..., link_libs: Sequence[str] = ..., config: hutil.cppinline.Config | None = None) -> hutil.cppinline._Library: ...
def extendClass(cls: _ExtendableClass, library_name: str, includes: str = '', function_sources: Sequence[str] = ..., debug: bool = False, catch_crashes: bool | None = None, structs: Sequence[_StructDescription] = ..., auto_add_include: bool = True, include_dirs: Sequence[str] = ..., link_dirs: Sequence[str] = ..., link_libs: Sequence[str] = ..., config: hutil.cppinline.Config | None = None) -> None:
    """Extend a hou class by adding methods implemented in C++.

    cls is the hou module class you're extending.  The rest of the arguments
    are the same as for createLibrary, except acquire_hom_lock is always True.
    Note that this function automatically adds a `#include` line for the
    underlying C++ class unless auto_add_include is False.

    The first parameter to your C++ functions must be a pointer to a C++ object
    corresponding to the hou object.  See the module documentation for the
    mapping from hou classes to C++ HDK classes.

    Note that if you are passing hou.Geometry objects, you must provide a
    const GU_Detail * if it can be called on a read-only hou.Geometry object
    and a GU_Detail * only if it can only be called on a hou.Geometry object
    from within a Python SOP.
    """
