import ctypes
from collections.abc import Callable, Mapping, Sequence
from typing import Any, Never, Protocol, SupportsInt, TypeAlias, TypeVar

from _ctypes import CFuncPtr, _CDataType

import hutil.parsecppsig

_T = TypeVar("_T")

_StructDescription: TypeAlias = tuple[str, str | Sequence[tuple[str, str]]]

class _ParamConverter(Protocol):
    def from_param(self, obj: object) -> ctypes.c_void_p: ...

# Calls the function that calls into C++, returning its result, or None if it traps an error
# (hou.runCallbackAndCatchCrashes).
class _ErrorTrapper(Protocol):
    def __call__(self, callback: Callable[[], _T], /) -> _T | None: ...

class _Handle(Protocol):
    def as_pointer(self) -> SupportsInt: ...
    def destroy(self) -> object: ...

class Config:
    compiler_hook: "CompilerHook"
    cpp_source_boilerplate_prefix: str
    cpp_source_filtering_function: Callable[[str], str] | None
    error_trapping_function: _ErrorTrapper | None
    known_typedefs_dict: dict[str, str]
    version_info_string: str
    cpp_types_to_ctypes_converter: dict[str, _ParamConverter]
    cpp_types_to_converter_handles: dict[str, Callable[[Any], _Handle]]
    def __init__(self) -> None: ...
    def register_type_conversion(
        self, py_class: type[_T], cpp_type_name: str, conversion_function: Callable[[_T], SupportsInt]
    ) -> None: ...
    def register_handle_type(
        self, cpp_type_name: str, handle_class: Callable[[Never], _Handle]
    ) -> None: ...

class ConverterHandle:
    def __init__(self, py_object: object, py_class: type[object]) -> None: ...

class CompilerHook:
    def default_shared_library_directory(self) -> str: ...
    def find_shared_library(self, shared_library_file_name: str) -> str | None: ...
    def get_compile_command(
        self,
        cpp_file_path: str,
        output_shared_library_path: str,
        debug: bool,
        include_dirs: Sequence[str],
        link_dirs: Sequence[str],
        link_libs: Sequence[str],
    ) -> str | None: ...
    def get_link_command(
        self,
        cpp_file_path: str,
        output_shared_library_path: str,
        debug: bool,
        include_dirs: Sequence[str],
        link_dirs: Sequence[str],
        link_libs: Sequence[str],
    ) -> str | None: ...
    def clean_up_after_compiling(
        self,
        cpp_file_path: str,
        output_shared_library_path: str,
        debug: bool,
        include_dirs: Sequence[str],
        link_dirs: Sequence[str],
        link_libs: Sequence[str],
    ) -> None: ...

class GPlusPlusCompilerHook(CompilerHook):
    def get_compile_command(
        self,
        cpp_file_path: str,
        output_shared_library_path: str,
        debug: bool,
        include_dirs: Sequence[str],
        link_dirs: Sequence[str],
        link_libs: Sequence[str],
    ) -> str: ...
    def get_link_command(
        self,
        cpp_file_path: str,
        output_shared_library_path: str,
        debug: bool,
        include_dirs: Sequence[str],
        link_dirs: Sequence[str],
        link_libs: Sequence[str],
    ) -> str: ...

class CompilerError(Exception): ...

class _Library:
    def __init__(
        self,
        name: str,
        config: Config,
        includes: str,
        struct_descriptions: Sequence[_StructDescription],
        function_sources: Sequence[str],
        debug: bool,
        catch_crashes: bool,
        include_dirs: Sequence[str],
        link_dirs: Sequence[str],
        link_libs: Sequence[str],
    ) -> None: ...
    def __repr__(self) -> str: ...

class UnconvertedCharP(ctypes.c_char_p): ...

win_msvcrt_lib_name: str

class _CPPFunction:
    config: Config
    catch_crashes: bool
    source: str
    __doc__: str
    __get__: None
    __name__: str
    c_function: CFuncPtr | None
    cpp_signature: hutil.parsecppsig.CPPSignature
    name: str
    parm_name_indices: dict[str, int]
    parm_indices_to_handle_classes: list[tuple[int, Callable[[Any], _Handle]]]
    def __init__(
        self,
        config: Config,
        source: str,
        catch_crashes: bool,
        cpp_type_structs_dict: Mapping[str, hutil.parsecppsig.CPPType],
    ) -> None: ...
    @property
    def return_cpp_type(
        self,
    ) -> hutil.parsecppsig.CPPNativeType | hutil.parsecppsig.CPPUserType | hutil.parsecppsig.CPPPointerType | None: ...
    @property
    def return_type_name(self) -> str: ...
    @property
    def orig_return_type_name(self) -> str: ...
    @property
    def return_ctype(self) -> type[_CDataType] | None: ...
    def __repr__(self) -> str: ...
    def signature(self) -> str: ...
    def symbol_name(self) -> str: ...
    def set_c_function(self, c_function: CFuncPtr) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

loaded_libraries: dict[str, _Library]

def create_library(
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
    config: Config | None = ...,
) -> _Library: ...
