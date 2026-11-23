import hou
from hutil.Qt import QtCore, QtWidgets
from typing import ClassVar

class FileChooserButton(QtWidgets.QToolButton):
    '''
hou.qt.FileChooserButton

A button with the Houdini look and feel that opens the Houdini file
chooser dialog when clicked.

This class inherits from Qt\'s QtWidgets.QToolButton class.

SIGNALS


    fileSelected(str)
        This signal is emitted when a selection is made in the file
        chooser dialog.

EXAMPLES

    This example demonstrates creating a file chooser button and hooking
    it to a callback function that is invoked when a file is selected
    from the chooser dialog:

  > 
  > def onFileSelected(file_path):
  >     print("Selected file:", file_path)
  > 
  > file_chooser_btn = hou.qt.FileChooserButton()
  > file_chooser_btn.setFileChooserTitle("Please select a file")
  > file_chooser_btn.setFileChooserMode(hou.fileChooserMode.Read)
  > file_chooser_btn.fileSelected.connect(onFileSelected)

'''
    start_directory: str | None
    title: str | None
    collapse_sequences: bool
    file_filter: hou.EnumValue[hou.fileType]
    file_pattern: str | None
    default_value: str | None
    multiple_select: bool
    is_image_chooser: bool
    chooser_mode: hou.EnumValue[hou.fileChooserMode]
    __module__: str
    fileSelected: ClassVar[QtCore.Signal]
    def __init__(self) -> None:
        """
__init__(self)

    Create and return a new FileChooserButton object.

"""
    def setFileChooserStartDirectory(self, start_dir: str | None) -> None:
        """
setFileChooserStartDirectory(self, start_dir)

    Set the initial directory that the file chooser dialog will open in.

"""
    def setFileChooserTitle(self, title: str | None) -> None:
        """
setFileChooserTitle(self, title)

    Set the window title of the file chooser dialog.

"""
    def setFileChooserFilter(self, file_filter: hou.EnumValue[hou.fileType]) -> None:
        """
setFileChooserFilter(self, file_filter)

    Set the file filter in the chooser dialog.

    file_filter must be a hou.fileType value.

"""
    def setFileChooserPattern(self, file_pattern: str | None) -> None:
        """
setFileChooserPattern(self, file_pattern)

    Set the pattern used by the file chooser dialog. The dialog only
    lists files that match the pattern.

"""
    def setFileChooserDefaultValue(self, default_value: str | None) -> None:
        """
setFileChooserDefaultValue(self, default_value)

    Set the default value in the file chooser dialog. The default value
    is used to populate the file name field in the dialog.

"""
    def setFileChooserMultipleSelect(self, multiple_select: bool) -> None:
        """
setFileChooserMultipleSelect(self, multiple_select)

    Set whether the file chooser dialog accepts multiple selection.

"""
    def setFileChooserIsImageChooser(self, is_image_chooser: bool) -> None:
        """
setFileChooserIsImageChooser(self, is_image_chooser)

    Set whether the file chooser dialog will be used to select image
    files. Image thumbnails are shown in the dialog. The default is for
    the dialog to not be used solely for selecting image files.

"""
    def setFileChooserMode(self, chooser_mode: hou.EnumValue[hou.fileChooserMode]) -> None:
        """
setFileChooserMode(self, chooser_mode)

    Set the mode of the file chooser dialog.

    chooser_mode must be a hou.fileChooserMode value.

"""
