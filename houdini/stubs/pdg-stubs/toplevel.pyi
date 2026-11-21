# Houdini stubs generated from Houdini 22.0.466

import _pdg
import typing
from typing import Any

def curPlatform() -> _pdg.platform:
    """
    Returns the pdg.platform enum value for the current system
    """
def workItem() -> _pdg.WorkItem | None:
    """
    Returns the thread local active work item, and adds a channel dependency on
    the active work item if called during a cook
    """
def isEvaluating() -> bool:
    """
    Returns True if the thread is evaluating a PDG work item
    """
def attrib(name: str, index: int | None = None, default_value: object = None) -> Any:
    """
    Returns value of an attribute on the active work item. If an index is not
    specified, this method returns the full value array for the attribute if
    applicable
    """
@typing.overload
def input(index: None = ..., tag: str | None = ..., localize: bool = ...) -> list[str]: ...
@typing.overload
def input(index: int | str, tag: str | None = ..., localize: bool = ...) -> str | list[str]: ...
@typing.overload
def kwargs(arg: None = ...) -> dict[str, Any]: ...
@typing.overload
def kwargs(arg: str) -> Any: ...
