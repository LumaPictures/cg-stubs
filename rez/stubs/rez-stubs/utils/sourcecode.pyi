import rez.packages
from _typeshed import Incomplete
from rez.packages import PackageBaseResourceWrapper as PackageBaseResourceWrapper
from rez.util import load_module_from_file as load_module_from_file
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.formatting import indent as indent
from rez.utils.logging_ import print_debug as print_debug
from types import CodeType, ModuleType
from typing import Any, Callable, Generic, TypeVar

T = TypeVar('T')
CallabeT = TypeVar('CallabeT', bound=Callable)

def early() -> Callable[[CallabeT], CallabeT]:
    """Used by functions in package.py to harden to the return value at build time.

    The term 'early' refers to the fact these package attribute are evaluated
    early, ie at build time and before a package is installed.
    """
def late() -> Callable[[CallabeT], CallabeT]:
    """Used by functions in package.py that are evaluated lazily.

    The term 'late' refers to the fact these package attributes are evaluated
    late, ie when the attribute is queried for the first time.

    If you want to implement a package.py attribute as a function, you MUST use
    this decorator - otherwise it is understood that you want your attribute to
    be a function, not the return value of that function.
    """
def include(module_name: str, *module_names: str) -> Callable[[CallabeT], CallabeT]:
    """Used by functions in package.py to have access to named modules.

    See the 'package_definition_python_path' config setting for more info.
    """
def _add_decorator(fn, name, **kwargs) -> None: ...

class SourceCodeError(Exception):
    short_msg: str
    def __init__(self, msg: str, short_msg: str) -> None: ...

class SourceCodeCompileError(SourceCodeError): ...
class SourceCodeExecError(SourceCodeError): ...

class SourceCode(Generic[T]):
    """Wrapper for python source code.

    This object is aware of the decorators defined in this sourcefile (such as
    'include') and deals with them appropriately.
    """
    source: str
    func: Callable[[], T] | None
    filepath: str | None
    eval_as_function: bool
    package: rez.packages.PackageBaseResourceWrapper | None
    funcname: str | None
    decorators: list[dict[Any, Any]]
    def __init__(self, source: str | None = None, func: Callable[[], T] | None = None, filepath: str | None = None, eval_as_function: bool = True) -> None: ...
    def copy(self) -> SourceCode[T]: ...
    def _init_from_func(self) -> None: ...
    @cached_property
    def includes(self) -> set | None: ...
    @cached_property
    def late_binding(self) -> bool: ...
    @cached_property
    def evaluated_code(self) -> str: ...
    @property
    def sourcename(self) -> str: ...
    @cached_property
    def compiled(self) -> CodeType: ...
    def set_package(self, package: PackageBaseResourceWrapper) -> None: ...
    def exec_(self, globals_={}) -> T: ...
    def to_text(self, funcname: str) -> str: ...
    def _get_decorator_info(self, name: str) -> dict | None: ...
    def __getstate__(self): ...
    def __setstate__(self, state) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class IncludeModuleManager:
    """Manages a cache of modules imported via '@include' decorator.
    """
    include_modules_subpath: str
    modules: dict[Any, Any]
    def __init__(self) -> None: ...
    def load_module(self, name: str, package: PackageBaseResourceWrapper) -> ModuleType | None: ...

include_module_manager: Incomplete
