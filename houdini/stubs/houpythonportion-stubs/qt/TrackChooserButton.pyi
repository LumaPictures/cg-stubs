import PySide6.QtCore
import hou
from hutil.Qt import QtWidgets
from typing import ClassVar

class TrackChooserButton(QtWidgets.QToolButton):
    '''
hou.qt.TrackChooserButton

A button with the Houdini look and feel that opens the Houdini track
chooser dialog when clicked.

This class inherits from Qt\'s QtWidgets.QToolButton class.

SIGNALS


    trackSelected(str)
        This signal is emitted when a selection is made in the track
        chooser dialog.

EXAMPLES

    This example demonstrates creating a chooser button for SOP nodes
    and hooking it to a callback function that is invoked when a node is
    selected from the chooser dialog:

  > 
  > def onTrackSelected(track_path):
  >     print("Selected track:", track_path)
  > 
  > track_chooser_btn = hou.qt.NodeChooserButton()
  > track_chooser_btn.setNodeChooserFilter(hou.nodeTypeFilter.Chop)
  > track_chooser_btn.trackSelected.connect(onTrackSelected)

'''
    relative_to_node: None
    initial_selection: dict[str, list[tuple[hou.ChopNode | None, str]]]
    node_filter: hou.EnumValue[hou.nodeTypeFilter]
    select_multiple: bool
    __module__: str
    trackSelected: ClassVar[PySide6.QtCore.Signal]
    def __init__(self) -> None:
        """
__init__(self)

    Create and return a new TrackChooserButton object.

"""
    def setInitialSelection(self, initial_track: hou.Track) -> None:
        """
setInitialSelection(self, initial_track)

    Set the initially selected track when the track chooser dialog
    is opened.

"""
    def setNodeChooserFilter(self, node_filter: hou.EnumValue[hou.nodeTypeFilter]) -> None:
        """
setNodeChooserFilter(self, node_filter)

    Set the node type filter used by the track chooser dialog.

    node_filter must be a hou.nodeTypeFilter enumerated value.

"""
    def setSelectMultiple(self, value: bool) -> None:
        """
setSelectMultiple(self, value)

    Set if multiple tracks should be selectable with the chooser dialog.

"""
