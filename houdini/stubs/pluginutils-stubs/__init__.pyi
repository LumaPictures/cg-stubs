import re
import types
from collections.abc import Callable as Callable, Generator, Iterable, Mapping, Sequence
from typing import Any

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
MODULE_CACHE: dict[str, tuple[types.ModuleType, float]]
LIST_CACHE: dict[tuple[tuple[str, ...], str, str], Sequence[str]]
CHECK_MOD_TIMES: bool
split_exp: re.Pattern[str]

def invalidateCache() -> None: ...
def loadModule(filepath: str, silent: bool = False, context: Mapping[str, object] | None = None) -> types.ModuleType | None:
    """
    Loads the contents of a file and evaluates it as a Python module object.
    This does not import the module, so the file does not need to be in the
    Python path, and the module is not added to the list of imported modules.

    :param filepath:
    :param silent:
    :return:
    """
def findModules(dirname: str, path_dirs: Sequence[str] | None = None, file_pattern: str = '*.py', include_shadowed: bool = False, reverse: bool = False, pathvar: str | None = None, order_key: str | None = None) -> list[str]:
    '''
    Looks for Python files in a list of path directories (by default, the
    Houdini path) and yields a series of loaded Module objects, according to the
    various arguments.

    Note that the "dirname" can actually be a path fragment; it is joined to
    each path directory, then the contents of the resulting path is searched.

    You will usually segregate a particular type of plugin by directory name,
    or possibly a file pattern, to avoid loading unrelated modules when you are
    looking for that type of plugin.

    For example, you would specify that "snapshot metadata" plugins must be on
    the path in a directory named "scripts/snapshot_metadata".

    :param dirname: Look for a directory with this name within each path
        directory. Pass "" or None to look directly in the path directories.
    :param path_dirs: A sequence of path directories. If this is None, the
        function uses the Houdini path. Earlier directories override later
        directories, using the Houdini convention.
    :param file_pattern: Look for Python files matching this glob pattern.
    :param include_shadowed: By default, a module earlier in the path will
        "shadow" (override) a module with the same name later in the path. This
        allows a user to override job or studio defaults, for example. If you
        specify `load_shadowed=True`, the function yields _all_ found modules,
        even modules that are shadowed by earlier modules with the same name.
    :param reverse: Reverse the order of the directory processing, so higher-priority
        (e.g. user) modules come after lower-priority (e.g. $HFS) modules.
    :param pathvar: The environment variable name that contains the list of
        paths that should be searched for dirname.
    :param order_key: An optional key to check for inside the module that
        specifies the order in which the module should appear in the final
        list, relative to the other modules in the same directory (i.e.,
        ordering does not take place between directories). For example, if the
        module files contain `processing_order = N`, you could specify
        `order_key=\'processing_order\'` in your call to this function. If left
        at `None`, then all the modules\' order hints are assumed to be 1.
    :return: A list of Module objects.
    '''
def findFunctions(dirname: str, fn_name: str, path_dirs: Sequence[str] | None = None, file_pattern: str = '*.py', include_shadowed: bool = False, reverse: bool = False, pathvar: str | None = None, order_key: str | None = None) -> Generator[Callable[..., Any], None, None]:
    '''

    :param dirname: Look for a directory with this name within each path
        directory. Pass "" or None to look directly in the path directories.
    :param fn_name: The name of the function in the found modules to look for.
    :param path_dirs: See the help for findModules().
    :param file_pattern: Look for Python files matching this glob pattern.
    :param include_shadowed: See the help for findModules().
    :param reverse: Reverse the order of the found functions, so higher-priority
        (e.g. user) functions come after lower-priority (e.g. $HFS) functions.
    :param pathvar: The environment variable name that contains the list of
        paths that should be searched for dirname.
    :param order_key: An optional key to check for inside the module that
        specifies the order in which the module should appear in the final
        list, relative to the other modules in the same directory (i.e.,
        ordering does not take place between directories). For example, if the
        module files contain `processing_order = N`, you could specify
        `order_key=\'processing_order\'` in your call to this function. If left
        at `None`, then all the modules\' order hints are assumed to be 1.
    :return:
    '''
def runFunctions(dirname: str, fn_name: str, args: Iterable[Any] = ..., kwargs: Mapping[str, object] | None = None, path_dirs: Sequence[str] | None = None, file_pattern: str = '*.py', include_shadowed: bool = False, reverse: bool = False, pathvar: str | None = None, order_key: str | None = None) -> list[Any]:
    '''

    :param dirname: Look for a directory with this name within each path
        directory. Pass "" or None to look directly in the path directories.
    :param fn_name: The name of the function in the found modules to run.
    :param args: A list or tuple of positional arguments to pass to each
        found function.
    :param kwargs: A dict of keyword arguments to pass to each found function.
    :param path_dirs: See the help for findModules().
    :param file_pattern: Look for Python files matching this glob pattern.
    :param include_shadowed: See the help for findModules().
    :param reverse: Reverse the order of the found functions, so higher-priority
        (e.g. user) functions come after lower-priority (e.g. $HFS) functions.
    :param pathvar: The environment variable name that contains the list of
        paths that should be searched for dirname.
    :param order_key: An optional key to check for inside the module that
        specifies the order in which the module should appear in the final
        list, relative to the other modules in the same directory (i.e.,
        ordering does not take place between directories). For example, if the
        module files contain `processing_order = N`, you could specify
        `order_key=\'processing_order\'` in your call to this function. If left
        at `None`, then all the modules\' order hints are assumed to be 1.
    :return: A list of the return value from each found function.
    '''
def pipelineFunctions(dirname: str, fn_name: str, main_arg: _T, args: Iterable[Any] = ..., kwargs: Mapping[str, object] | None = None, path_dirs: Sequence[str] | None = None, file_pattern: str = '*.py', include_shadowed: bool = False, reverse: bool = False, pathvar: str | None = None, order_key: str | None = None) -> _T:
    '''

    :param dirname: Look for a directory with this name within each path
        directory. Pass "" or None to look directly in the path directories.
    :param fn_name: The name of the function in the found modules to run.
    :param main_arg: This will be passed to the first found function.
    :param args: A list or tuple of positional arguments to pass to each
        found function.
    :param kwargs: A dict of keyword arguments to pass to each found function.
    :param path_dirs: See the help for findModules().
    :param file_pattern: Look for Python files matching this glob pattern.
    :param include_shadowed: See the help for findModules().
    :param reverse: If True, run higher-priority (e.g. user) functions last and
        lower-priority (e.g. $HFS) plugins first.
    :param pathvar: The environment variable name that contains the list of
        paths that should be searched for dirname.
    :param order_key: An optional key to check for inside the module that
        specifies the order in which the module should appear in the final
        list, relative to the other modules in the same directory (i.e.,
        ordering does not take place between directories). For example, if the
        module files contain `processing_order = N`, you could specify
        `order_key=\'processing_order\'` in your call to this function. If left
        at `None`, then all the modules\' order hints are assumed to be 1.
    :return: The value returned by the last found function.
    '''
def typedPipeline(dirname: str, fn_name: str, main_arg: dict[str, Any], args: Iterable[Any] = ..., kwargs: Mapping[str, object] | None = None, path_dirs: Sequence[str] | None = None, file_pattern: str = '*.py', include_shadowed: bool = False, reverse: bool = False, set_fields: Iterable[str] = ..., datetime_fields: Iterable[str] = ..., pathvar: str | None = None, order_key: str | None = None) -> dict[str, Any]:
    '''

    :param dirname: Look for a directory with this name within each path
        directory. Pass "" or None to look directly in the path directories.
    :param fn_name: The name of the function in the found modules to run.
    :param main_arg: This will be passed to the first found function.
    :param args: A list or tuple of positional arguments to pass to each
        found function.
    :param path_dirs: See the help for findModules().
    :param file_pattern: Look for Python files matching this glob pattern.
    :param include_shadowed: See the help for findModules().
    :param reverse: Reverse the order of the found functions, so higher-priority
        (e.g. user) functions come after lower-priority (e.g. $HFS) functions.
    :param set_fields: A list of field names to treat as sets in the main_arg
        dict.
    :param datetime_fields: A list of field names to treat as datetimes in the
        main_arg dict.
    :param pathvar: The environment variable name that contains the list of
        paths that should be searched for dirname.
    :param order_key: An optional key to check for inside the module that
        specifies the order in which the module should appear in the final
        list, relative to the other modules in the same directory (i.e.,
        ordering does not take place between directories). For example, if the
        module files contain `processing_order = N`, you could specify
        `order_key=\'processing_order\'` in your call to this function. If left
        at `None`, then all the modules\' order hints are assumed to be 1.
    :return: The value returned by the last found function.
    '''
def runSnapshotMetadataPlugins(meta_dict: dict[str, Any], args: Iterable[Any] = ..., kwargs: Mapping[str, object] | None = None, dirname: str = 'scripts/snapshot_metadata', fn_name: str = 'editSnapshotMetadata', set_fields: Iterable[str] = ('tags',), datetime_fields: Iterable[str] = ('taken',), pathvar: str | None = None) -> dict[str, Any]: ...
