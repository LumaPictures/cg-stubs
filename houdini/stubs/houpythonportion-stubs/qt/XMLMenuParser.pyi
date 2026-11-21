# Houdini stubs generated from Houdini 22.0.466

import hou
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import typing
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping, MutableMapping
from hutil.Qt import QtWidgets
from typing import Any, TypedDict

from typing import TypeVar
from typing import TypeVar
_MenuT = TypeVar('_MenuT', bound=PySide6.QtWidgets.QMenu)
class _MenuActionKwargs(TypedDict, extra_items=Any):  # type: ignore[call-arg]
    label: str
    id: str

ICON_SIZE: int

class _MenuTitleLabel(QtWidgets.QLabel):
    def __init__(self, text: Incomplete | None = None, parent: Incomplete | None = None) -> None: ...

class MenuTitleItem(QtWidgets.QWidgetAction):
    """ A custom widget action to be used as a menu title.  This is not
        intended as a separator item, it doesn't draw a section break line.
        Also, an icon set here will be ignored.
    """
    def __init__(self, text: str | None = None, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    def text(self) -> str: ...
    def setText(self, text: str) -> None: ...

class XMLMenuParser:
    '''
hou.qt.XMLMenuParser

Object for dealing with XML menus.

This object will build QMenus based on an XML menu definition and will
also simplify keyboard shortcut handling for activating items in the
menu that have shortcuts assigned to them.

Script items like expressions and script code are passed kwargs that
will contain (if defined) the id and label of the corresponding menu
item.

EXAMPLES

    This example shows how you would use this object to preparse the XML
    file. Then on-demand generate a which can be invoked within an event
    handler.

  >     self._mymenuparser = XmlMenuParser(context = "h.pane.parms", xmlfile = "c:/temp/menu.xml")
  > ...
  >     def contextMenuEvent(self, event):
  >         # custom kwargs passed to any expression or code in menu.xml when evaluating
  >         menukwargs["parm"] = menucontextparm
  >         menukwargs["parmname"] = menucontextparm.name()
  >         menu = self._mymenuparser.generateMenu(kwargs = menukwargs, actionitem_callback = self._processHotKeyAction)
  >         if not menu.isEmpty():
  >             menu.popup(event.globalPos())

    XML file:

  > <?xml version="1.0" encoding="UTF-8"?>
  > <menuDocument>
  > <menu>
  >     <actionItem id="set_keyframe">
  >         <label>Set a Keyframe</label>
  >     </actionItem>
  >     <actionItem id="rem_keyframe">
  >         <labelExpression>return kwargs["label"] + " - " + kwargs["parmname"]</labelExpression>
  >     </actionItem>
  >     <actionItem id="revert_defs">
  >     </actionItem>
  > 
  >     <toggleItem>
  >         <label>Parm Locked</label>
  >         <enableExpression><![CDATA[
  > return kwargs[\'parm\'] is not None
  > ]]></enableExpression>
  >         <valueExpression><![CDATA[
  > return kwargs[\'parm\'].isLocked()
  > ]]></valueExpression>
  >         <scriptCode><![CDATA[
  > kwargs[\'parm\'].lock(not kwargs[\'parm\'].isLocked())
  > ]]></scriptCode>
  >     </toggleItem>
  > 
  >     <actionItem id="lock_parm">
  >         <context><expression><![CDATA[
  > if kwargs[\'parm\'] is not None and kwargs[\'parm\'].isLocked():
  > return False
  > return True
  > ]]></expression></context>
  >     </actionItem>
  >     <actionItem id="unlock_parm">
  >         <context><expression><![CDATA[
  > if kwargs[\'parm\'] is not None and kwargs[\'parm\'].isLocked():
  > return True
  > return False
  > ]]></expression></context>
  >     </actionItem>
  >     <separatorItem/>
  >     <subMenu>
  >         <label>Expressions</label>
  >         <actionItem id="toggle_expr"/>
  >         <actionItem id="edit_expression"/>
  >         <actionItem id="expand_values"/>
  >         <actionItem id="use_python"/>
  >         <actionItem id="use_old_language"/>
  >     </subMenu>
  > </menu>
  > </menuDocument>

'''
    def __init__(self, context: str = '', kwargs: Mapping[str, object] | None = None, kwargsfunc: Callable[[], Mapping[str, object]] | None = None, xmlfilename: str | None = None, xmlstring: str | bytes | None = None) -> None:
        """
__init__(self, context, kwargs, xmlfile, xmlstring)

    When creating the object, one of xmlstring or xmlfile must be
    provided. If both are provided then only xmlstring will be used.


    context
        Hotkey context for this menu. This value is prepended to id
        values that do not contain '.'

    kwargs
        Additional kwargs items to be sent to all script code.

    xmlstring
        Optional XML Menu string to parse.

    xmlfilename
        Optional XML menu filename to find and parse.

"""
    def setHotkeyContext(self, hotkey_context: str) -> None: ...
    def hotkeyContext(self) -> str: ...
    def parseString(self, xmlstring: str | bytes) -> None:
        """
parseString(self, xmlstring)

    Parse an XML menu string and aggregate its contents into this menu.


    xmlstring
        A string containing valid XML.

"""
    def parseFile(self, xmlfile: str) -> None:
        """
parseFile(self, xmlfile)

    Parse an XML menu file and aggregate its contents into this menu.
    This should be a full path to the file as no search is performed to
    find the file.


    xmlfile
        A file name and path for a valid XML file.

"""
    def parseFiles(self, xmlfilename: str) -> None:
        """
parseFiles(self, xmlfilename)

    Search HOUDINI_PATH for and parse XML menu files that match given
    filename and aggregate their contents into this menu.


    xmlfilename
        A filename for a valid XML file.

"""
    @typing.overload
    def generateMenu(self, kwargs: MutableMapping[str, Any], menu: None = ..., actionitem_callback: Callable[[_MenuActionKwargs], object] | None = ...) -> PySide6.QtWidgets.QMenu: ...
    @typing.overload
    def generateMenu(self, kwargs: MutableMapping[str, Any], menu: _MenuT, actionitem_callback: Callable[[_MenuActionKwargs], object] | None = ...) -> _MenuT: ...
    def handleKeyPress(self, keystring: str, kwargs: MutableMapping[str, Any], actionitem_callback: Callable[[_MenuActionKwargs], object] | None = None, hotkey_context: str | None = None) -> bool:
        """
handleKeyPress(self, keystring, kwargs, actionitem_callback) -> bool

    Look up and trigger menu actions based on their shortcut key
    assigned in the hotkey manager. Returns True if the keystring was
    handled, otherwise False.


    keystring
        A string representation of the key press equivalent to what is
        provided by hou.qt.qtKeyToString()

    kwargs
        Is appended to the kwargs passed to all functions and scripts in
        the XML file. This is the way to pass context related data to
        those functions, like the currently selected items.

    actionitem_callback
        A function to be invoked when 'ActionItem' entries are
        activated. If this is None then any 'ActionItem' will be ignored
        as they cannot be activated.

"""
    class _MenuItem:
        def __init__(self, hotkey_context: str, attributes: Mapping[str, str] | None = None) -> None: ...
        def addKwargs(self, kwargs: Mapping[str, object]) -> None: ...
        def items(self) -> list['XMLMenuParser._MenuItem']: ...
        def handleKeyPress(self, keystring: str, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None, hotkey_context: str | None = None) -> bool: ...
        def isVisible(self, kwargs: Mapping[str, object]) -> bool: ...
        def isEnabled(self, kwargs: Mapping[str, object]) -> bool: ...
        def label(self, kwargs: Mapping[str, object]) -> str: ...
        def icon(self, kwargs: Mapping[str, object]) -> PySide6.QtGui.QIcon | None: ...
        def action(self, kwargs: Mapping[str, object], label: str | None = None) -> None: ...
        def symbol(self) -> str | None: ...
    class _ActionMenuItem(_MenuItem):
        def addQMenuItem(self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None) -> None: ...
        def handleKeyPress(self, keystring: str, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None, hotkey_context: str | None) -> bool: ...  # type: ignore[override]  # SideFX drops the base class's default
    class _ScriptMenuItem(_MenuItem):
        def addQMenuItem(self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None) -> None: ...
    class _ToggleMenuItem(_MenuItem):
        def __init__(self, hotkey_context: str, attributes: Mapping[str, str]) -> None: ...
        def addQMenuItem(self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None) -> None: ...
    class _SeparatorMenuItem(_MenuItem):
        def addQMenuItem(self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None) -> None: ...
    class _TitleMenuItem(_MenuItem):
        def addQMenuItem(self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None) -> None: ...
    class _SubMenuItem(_MenuItem):
        def addQMenuItem(self, menu: PySide6.QtWidgets.QMenu | None, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None) -> PySide6.QtWidgets.QMenu: ...
    class _ScriptMenuStripDynamicMenuItem(_MenuItem):
        def addQMenuItem(self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None) -> None: ...
    class _RootMenuItem(_SubMenuItem):
        def addQMenuItem(self, menu: PySide6.QtWidgets.QMenu | None, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None) -> PySide6.QtWidgets.QMenu: ...
