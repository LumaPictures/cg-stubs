# Houdini stubs generated from Houdini 22.0.466

from hutil.Qt import QtWidgets

class HelpButton(QtWidgets.QToolButton):
    """
hou.qt.HelpButton

A button with the Houdini look and feel that opens a help page when
clicked.

This class inherits from Qt's QtWidgets.QToolButton class.

"""
    __module__: str
    def __init__(self, help_path: str, tooltip: str = 'Show help for this window') -> None:
        '''
__init__(self, help_path, tooltip="Show help for this window")

    Create and return a new help button that opens the given help when
    clicked.

    help_path must be a recognized help path. For example, set help_path
    to /nodes/sop/torus to open the Torus SOP help when the button is
    clicked.

    You can optionally set tooltip to add hover tooltip text to the
    button.

'''
