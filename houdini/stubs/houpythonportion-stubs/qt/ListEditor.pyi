import hou
import layout
import PySide6.QtCore
import PySide6.QtWidgets
from collections.abc import Iterable
from hutil.PySide import QtWidgets
from typing import ClassVar, TypedDict, Unpack

class _ListEditorOptions(TypedDict, total=False):
    strings: Iterable[str]
    top_message: str | None
    bottom_message: str | None
    allow_editing: bool
    allow_add_remove: bool
    allow_reorder: bool
    allow_empty_string: bool
    show_checkboxes: bool
    keep_sorted: bool
    initial_string: str
    initial_check: bool
    exclusive_check: bool
    allow_empty_list: bool

class ListEditorDialog(QtWidgets.QDialog):
    __module__: str
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None, **kwargs: Unpack[_ListEditorOptions]) -> None: ...
    def editor(self) -> ListEditor: ...

class ListEditor(QtWidgets.QFrame):
    '''
hou.qt.ListEditor

A convenient user interface (as a dialog or a reusable widget) for
displaying/editing a list of strings.

OVERVIEW

    Often when designing a user interface, you need provide the user
    with a way to view/edit a list of strings. For example, configuring
    a list of directories to search for plugin files, or a list of tags
    to apply to an object, or a list of object paths that a light should
    illuminate.

    This object provides a compact, simple, yet powerful editor for
    these types of jobs. You provide a list of strings to present to the
    user. The widget allows the user to add, delete, reorder, and/or
    edit items in the list (depending on the options).

    In addition to editing the text of the strings, you can display
    checkboxes next to each item, and use the checked state as
    additional information. For example, you might have an interface
    where the user specifies a list of asset libraries to pull props
    from. You can provide checkboxes on the items to let the user
    temporarily enable/disable individual libraries without having to
    delete and re-add them.

USING THE HOU.QT.LISTEDITORDIALOG CONVENIENCE CLASS

    To get a ListEditor in a dialog window, you can use the pre-made
    class hou.qt.ListEditorDialog. It takes the same keyword arguments
    as ListEditor and simply wraps the widget in a dialog window.

    Use the ListEditorDialog.editor() to get a reference to the
    `ListEditor

    This class inherits from Qt\'s QtWidgets.QDialog class. Refer to the
    Qt documentation for information on the large number of useful
    methods provided by this object.

    MODAL DIALOG

        Calling the widget this way requires the user to accept or
        cancel the dialog before they can use other Houdini windows.

         1. Instantiate and configure the widget with the options you
            want.

         2. Call the widget\'s .exec_() method to open the dialog and
            wait for the user to finish interacting with it.

         3. Use the return value of the .exec_() method call to tell
            whether the user accepted or canceled the dialog.

      > dialog = hou.qt.ListEditorDialog(allow_editing=True, allow_add_remove=True,
      >                                  allow_reorder=True, allow_empty_string=False)
      > dialog.setWindowTitle("Edit Files")
      > dialog.resize(400, 360)
      > 
      > editor = dialog.editor()
      > editor.setTopMessage("Add, remove, or edit which files to read")
      > # Get the current list of file paths from a variable
      > editor.setStrings(list_of_file_paths)
      > 
      > accepted = editor.exec_()
      > if accepted:
      >     # Replace the variable with the new edited list of file paths
      >     list_of_file_paths = editor.strings()

    NON-MODAL DIALOG

         1. Instantiate and configure the widget with the options you
            want.

         2. Connect to the widget\'s accepted, rejected, or finished
            signals.

         3. Call .show() on the dialog object to open it as a window.

      > def show_tag_editor_for(node):
      >     # Create and configure the editor widget
      >     dialog = hou.qt.ListEditorDialog(allow_editing=False, allow_add_remove=True,
      >                                      allow_reorder=False, keep_sorted=True,
      >                                      show_checkboxes=True, initial_check=False)
      >     dialog.setWindowTitle("Edit Tags")
      > 
      >     editor = dialog.editor()
      >     editor.setTopMessage("Check the tags you want to apply. You can add new tags.")
      > 
      >     # Set the contents of the editor to the list of all known tags. Check the tags
      >     # that currently apply to the given node.
      >     for tag in list_of_all_tags:
      >         editor.addListItem(tag, node.hasTag(tag))
      > 
      >     # Connect the editor\'s "accepted" signal to a function that updates the tags
      >     dialog.accepted.connect(lambda: update_node_tags(node, editor.stringsAndChecks()))
      > 
      >     # Stash a reference to this widget in `hou.session`, so it doesn\'t go away as soon
      >     # as this function ends. This is a bit simplified, since storing it in a variable
      >     # like this means there can only be one tag editor at a a time.
      >     hou.sesssion.tag_editor = editor
      > 
      >     # Show the widget as a window so the user can interact with it
      >     dialog.show()
      > 
      > 
      > def update_node_tags(node, tags_and_checks):
      >     for tag, checked in tags_and_checks:
      >         if checked:
      >             node.addTag(tag)

        NOTE
            Remember that you must have at least one persistent
            reference to the widget, otherwise the window will be
            garbage collected and immediately close.

EMBEDDING LISTEDITOR AS A WIDGET IN A QT LAYOUT

    You can use ListEditor as a plain widget in a larger user interface.

     1. Instantiate and configure the widget with the options you want.

     2. Add the widget to a Qt interface as you would with any QWidget.

     3. Use the widget\'s strings() or stringsAndChecks() methods when
        you need to get the current editor contents.

  > # Set setting up your Qt user interface
  > class MyUI(QtWidgets.QFrame):
  >     def __init__(self, parent):
  >         super(MyUI, self).__init__(parent)
  >         layout = QtWidgets.QVBoxLayout()
  >         self.setLayout(layout)
  > 
  >         # Create and configure the ListEditor object
  >         self._editor = hou.qt.ListEditor(allow_editing=True,
  >                                          allow_add_remove=True,
  >                                          allow_reorder=True,
  >                                          allow_empty_string=False)
  >         self._editor.setTopMessage("Add, remove, or edit which files to read")
  >         # Get the current list of file paths from a variable
  >         self._editor.setStrings(list_of_file_paths)
  > 
  >         # Add the widget to your user interface
  >         layout.addWidget(self._editor)
  > 
  >     def read_files(self):
  >         for filepath in self._editor.strings():
  >             ...

TIPS AND NOTES

  * When allow_add_remove=True but allow_editing=False, the user can
    type out the initial string value of a newly created item, but
    cannot then edit that string after pressing [Enter].

  * If you have allow_reorder=True and also keep_sorted=True, the user
    will be allowed to drag items but dropping them will not change the
    order. To prevent confusion, you should turn off allow_reorder if
    you turn on keep_sorted.

SIGNALS


    itemEdited(int, str)
        Triggered when the text of an item is changed. Called with the
        row number (starting at 0) and new text of the item.

    checkChanged(int, str, bool)
        Triggered when the check state of an item is changed. Called
        with the row number (starting at 0), the text of the item, and
        the new checked state (True or False).

    listChanged()
        Triggered anytime the list of strings changes (the user adds,
        moves, or removes items). You can then call the strings() or
        stringsAndChecks() method to get the new list contents.

'''
    __module__: str
    listChanged: ClassVar[PySide6.QtCore.Signal]
    checkChanged: ClassVar[PySide6.QtCore.Signal]
    itemEdited: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, strings: Iterable[str] = ..., top_message: str | None = None, bottom_message: str | None = None, allow_editing: bool = True, allow_add_remove: bool = True, allow_reorder: bool = True, allow_empty_string: bool = True, show_checkboxes: bool = False, keep_sorted: bool = False, initial_string: str = '', initial_check: bool = True, exclusive_check: bool = False, allow_empty_list: bool = True, parent: PySide6.QtWidgets.QWidget | None = None) -> None:
        '''
__init__(self, strings=(), top_message=None, bottom_message=None,
allow_editing=True, allow_add_remove=True, allow_reorder=True,
allow_empty_string=True, show_checkboxes=False, keep_sorted=False,
initial_string="", initial_check=True, allow_empty_list=True)


    strings
        A list of strings to populate the list.

    top_message
        A string to display above the list. Use this label to describe
        the list contents or give instructions to the user.

    bottom_message
        A string to display below the list, to the right of the
        add/remove buttons. You can use this label to provide secondary
        information to the user.

    allow_editing
        If this is True, the user can edit the string contents of items
        in the list.

    allow_add_remove
        If this is True, the user can add new items, and/or remove
        existing items.

    allow_reorder
        If this is True, the user can change the order of the list by
        dragging and dropping items.

    allow_empty_string
        When allow_editing is on, this controls what happens when the
        user tries to enter an empty string. If this is True, an item
        can contain an empty string. If this is False, setting an item
        to an empty string deletes it.

    show_checkboxes
        Show checkboxes next to items to allow you to turn items on or
        off.

    keep_sorted
        Displays the list sorted, and maintains the sort as the user
        adds/edits items. If you turn this on, you should make sure
        allow_reorder is off.

    initial_string
        When the user adds a new item, the widget creates a new row and
        automatically makes it editable. This specifies the initial
        contents of the text edit field for a new row. The default is
        empty.

    initial_check
        When show_checkboxes is on, this controls the initial check
        state of newly created items (and items added by calling
        hou.qt.InfoWindow.setStrings).

    exclusive_check
        Only allow one checkbox to be on at a time. You can get the
        index of the checked item with the checkedRow() method, or the
        text of the selected item with checkedString().

    allow_empty_list
        Allow the editor to have no items. If you set this to False, the
        editor will not allow the user to delete the last item if there
        is only one. This does not prevent you from initializing the
        editor with an empty list, or setting the list to be empty.

'''
    def itemCount(self) -> int:
        """
itemCount() -> int

    Returns the number of rows in the editor.

"""
    def strings(self) -> list[str]:
        """
strings() -> list of str

    Returns a list of the string contents of each item.

"""
    def stringsAndChecks(self) -> list[tuple[str, bool]]:
        '''
stringsAndChecks() -> list of (str, bool) tuples

    Returns a list of tuples, where the first item of each tuple is the
    string content of an item and the second is a boolean indicating
    whether the item was checked.

  > # Show a list of nodes in /obj, with checkboxes indicating whether the node needs to cook
  > objnode = hou.node("/obj")
  > editor = ListEditor()
  > for node in hou.node("/obj").children():
  >     editor.addListItem(node.name(), node.needsToCook())
  > # Show the dialog and wait for the user to finish with it
  > ok = w.exec_()
  > # If the user accepted the dialog, recook all the nodes that were checked
  > if ok:
  >     for name, checked in w.stringsAndChecks():
  >         node = objnode.node(name)
  >         if checked:
  >             node.cook()
'''
    def rowIsChecked(self, row_num: int) -> bool:
        """
rowIsChecked(row_num) -> bool

    Returns True if the item in the given row number (starting at 0) is
    checked.

"""
    def setRowChecked(self, row_num: int, checked: bool) -> None:
        """
setRowChecked(row_num, checked)

    Sets the checked state of the item on the given row (starting at 0).
    The item is checked if the second argument is true, otherwise it is
    unchecked.

"""
    def rowString(self, row_num: int) -> str:
        """
rowString(row_num) -> str

    Returns the string in the given row number (starting at 0).

"""
    def checkedRows(self) -> list[int]:
        """
checkedRows() -> list of int

    Returns a list of row numbers corresponding to the checked items.

"""
    def checkedStrings(self) -> list[str]:
        """
checkedStrings() -> list of str

    Returns a list of strings corresponding to the checked items.

"""
    def checkedRow(self) -> int | None:
        """
checkedRow() -> int or None

    Returns the row number of the first checked item, or None if there
    are no checked items. This is a convenience for when exclusive_check
    is True.

"""
    def checkedString(self) -> str | None:
        """
checkedString() -> str or None

    Returns the text of the first checked item, or None if there are no
    checked items. This is a convenience for when exclusive_check is
    True.

"""
    def setStrings(self, strings: Iterable[str]) -> None:
        """
setStrings(strings)

    Sets the list of strings to display in the dialog.

"""
    def setStringsAndChecks(self, strings_and_checks: Iterable[tuple[str, bool]]) -> None:
        '''
setStringsAndChecks(strings_and_checks)

    Takes a sequence of (str, bool) tuples, where the first item in each
    tuple is the string content of an item and the second is a boolean
    indicating whether the item is checked.

  > # Show a list of nodes in /obj, with checkboxes indicating whether the node needs to cook
  > editor = ListEditor()
  > for node in hou.node("/obj").children():
  >     editor.addListItem(node.name(), node.needsToCook())
'''
    def clear(self) -> None:
        """
clear()

    Clears the list, leaving the dialog empty.

"""
    def addListItem(self, text: str, checked: bool | None = None, insert_at: int = -1) -> None:
        """
addListItem(text, checked=None, insert_at=-1)

    Adds a single item to the current list.


    text
        The string content of the item.

    checked
        If this is True or False, sets the checked state of the item. If
        this is None, it uses the widget's initial_check setting as the
        checked state for the item.

    insert_at
        If this is -1 (the default), the new item appears at the end of
        the list. If you specify a row number (starting at 0), the new
        item is inserted at that point in the list.

        Even if you insert the item at a specific point, if keep_sorted
        is on the item may immediately move to its sorted position.

"""
    def removeRow(self, row_num: int) -> None:
        """
removeRow(row_num)

    Removes the row at the given position (starting at 0).

"""
    def topMessage(self) -> str:
        """
topMessage() -> str

    Returns the current text in the label above the list.

"""
    def setTopMessage(self, text: str) -> None:
        """
setTopMessage(text)

    Sets the text above the list widget.

"""
    def bottomMessage(self) -> str:
        """
bottomMessage() -> str

    Returns the current text in the label below the list.

"""
    def setBottomMessage(self, text: str) -> None:
        """
setBottomMessage(text)

    Sets the text below the list.

"""
    def isEditingAllowed(self) -> bool:
        """
isEditingAllowed() -> bool

    Whether the user is allowed to edit (rewrite) the string contents of
    items.

"""
    def setAllowEditing(self, allow: bool) -> None:
        """
setAllowEditing(allow)

    Sets whether editing (rewriting) the string content of items is
    allowed.

"""
    def isEmptyListAllowed(self) -> bool:
        """
isEmptyListAllowed() -> bool

    Whether the user is allowed to delete the last item to leave the
    list empty.

"""
    def setAllowEmptyList(self, allow: bool) -> None:
        """
setAllowEmptyList()

    Sets whether the user is allowed to delete the last item to leave
    the list empty.

"""
    def isAddRemoveAllowed(self) -> bool:
        """
isAddRemoveAllowed() -> bool

    Whether the user can add or remove items.

"""
    def setAllowAddRemove(self, allow: bool) -> None:
        """
setAllowAddRemove(allow)

    Sets whether the user can add or remove items.

"""
    def isReorderAllowed(self) -> bool:
        """
isReorderAllowed() -> bool

    Whether the user is allowed to drag items in the list to reorder
    them.

"""
    def setAllowReorder(self, allow: bool) -> None:
        """
setAllowReorder(allow)

    Sets whether the user is allowed to drag items in the list to
    reorder them.

"""
    def isEmptyStringAllowed(self) -> bool:
        """
isEmptyStringAllowed() -> bool

    Whether the user can enter an empty string as the contents for an
    item.

"""
    def setAllowEmptyString(self, allow: bool) -> None:
        """
setAllowEmptyString(allow)

    Sets whether the user can enter an empty string as the contents for
    an item.

"""
    def showCheckboxes(self) -> bool:
        """
showCheckboxes(show)

    Whether the widget shows checkboxes next to items in the list.

"""
    def setShowCheckboxes(self, show: bool) -> None:
        """
setShowCheckboxes(show)

    Sets whether to show checkboxes next to items in the list.

"""
    def keepSorted(self) -> bool:
        """
keepSorted(show)

    Whether the widget maintains the list in sorted order.

"""
    def setKeepSorted(self, keep_sorted: bool) -> None:
        """
setKeepSorted(keep_sorted)

    Sets whether the widget should maintain the list in sorted order.

"""
    def initialString(self) -> str:
        """
initialString() -> str

    The initial text in the text edit field when the user creates a new
    item with the Add button.

"""
    def setInitialString(self, text: str) -> None:
        """
setInitialString(text)

    Sets the initial text of a newly added item.

"""
    def initialCheck(self) -> bool:
        """
initialCheck() -> bool

    Whether newly created items are checked by default.

"""
    def setInitialCheck(self, checked: bool) -> None:
        """
setInitialCheck(checked)

    Sets whether newly created items will be checked by default.

"""
