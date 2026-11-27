import hou
from types import TracebackType
from typing import Protocol, TypedDict, Unpack

class _UndoRedoListener(Protocol):
    def onUndoOrRedo(self) -> None: ...

class _SelectionUndoListener(Protocol):
    def handleSelectionUndoOrRedo(self, new_sel: hou.Selection) -> None: ...

class _UndosGroupKwargs(TypedDict, total=False):
    editor: hou.NetworkEditor | None

class UndoPreviewUpdater:
    """
    Added at the start of each undo block.
    When an undo is triggered, this ends up being ran
    last, and so is perfectly set up to update any guide geos
    and drawables after updating the parameters fully on undo.
    """
    main_state: _UndoRedoListener
    def __init__(self, main_state: _UndoRedoListener) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class RedoPreviewUpdater(UndoPreviewUpdater):
    """
    Added at the end of each undo block.
    When a redo is triggered, this ends up being ran last,
    and so is perfectly set up to update any guide geos and
    drawables after updating the paramteres fully on redo.
    """
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class SelectionUndo:
    """
    Use to manage setting up undos when we change the selection
    in the viewer state.
    """
    main_state: _SelectionUndoListener
    pre_selection: hou.Selection
    post_selection: hou.Selection
    def __init__(self, main_state: _SelectionUndoListener, pre_selection: hou.Selection, post_selection: hou.Selection) -> None: ...
    def undo(self) -> None:
        """ Called on undo to change the selection. """
    def redo(self) -> None:
        """ Called on redo to change the selection. """

class NothingBlock:
    """
    The nothing block is used as a placeholder for cases where we need
    to keep the with block structure but don't want to use an
    UndoBlock for whatever reason.
    """
    def __init__(self, *args: object, **kwargs: object) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

class UndoBlockWrapper:
    """
    Wrap an undo block to add an UndoPreviewUpdater at the start
    of the block and a RedoPreviewUpdater at the end of the block.
    """
    source_block: hou.UndosGroup
    main_state: _UndoRedoListener
    def __init__(self, source_block: hou.UndosGroup, main_state: _UndoRedoListener) -> None: ...
    def __enter__(self) -> None:
        """ Called when a with block is entered. """
    def __exit__(self, *args: Unpack[tuple[type[BaseException] | None, BaseException | None, TracebackType | None]]) -> None:
        """ Called when a with block is exited. """

def getUndoBlock(make_undo_block: bool, main_state: _UndoRedoListener, *args: Unpack[tuple[str]], **kwargs: Unpack[_UndosGroupKwargs]) -> NothingBlock | UndoBlockWrapper:
    """
    Get the undo block object to use.

    :make_undo_block: Whether to create an undo block, or return a placeholder.
    :main_state: The CurveState on which we can call onUndoOrRedo().
    :args: Additional args to supply to hou.undos.group(*args, **kwargs)
    :kwargs: Additional kwargs to supply to hou.undos.group(*args, **kwargs)
    """
