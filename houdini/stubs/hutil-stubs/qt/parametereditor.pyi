# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtGui
import dataclasses
import hou
import re
import weakref
from hrecipes import rtypes as rtypes
from hutil.PySide import QAction as QAction, QtCore as QtCore
from hutil.PySide.QtCore import Qt as Qt
from hutil.qt.common import config as config, core as core, models as models, qmlviews as qmlviews
from hutil.qt.pluto import colors as colors
from hutil.qt.util import linearColorToView as linearColorToView
from typing import Callable as Callable, ClassVar, Self, Sequence, TypeAlias, TypedDict, Unpack

from typing import TypeAlias
_ParmValue: TypeAlias = int | float | str | dict[str, str]
_MenuTemplate: TypeAlias = hou.MenuParmTemplate | hou.StringParmTemplate | hou.IntParmTemplate
TempTypeSpec: TypeAlias = type[hou.ParmTemplate] | tuple[type[hou.ParmTemplate], ...]
class _ContextFields(TypedDict, total=False):
    node: hou.Node
    state: ParmEditorState
    find: Callable[[str], hou.ParmTuple | None]
    level: int

NODE_EVENTS: tuple[hou.EnumValue[hou.nodeEventType], ...]
digits_expr: re.Pattern[str]
embedded_icon_expr: re.Pattern[str]
null_parent: PySide6.QtCore.QModelIndex
anim_fns: tuple[str, ...]

def extract_embedded_icon_name(label: str) -> tuple[str, str]: ...
def extract_embedded_icon_names(labels: Sequence[str]) -> tuple[list[str], list[str]]: ...
def modifierArgs(modifiers: int) -> dict[str, bool]: ...

@dataclasses.dataclass(frozen=True)
class Context:
    node: hou.Node
    state: ParmEditorState
    find: Callable[[str], hou.ParmTuple | None]
    level: int = ...
    def replace(self, **kwargs: Unpack[_ContextFields]) -> Self: ...

class ParmProxy(core.Info):
    name: str
    index: int
    type: str
    dataType: str
    alias: str
    isScoped: bool
    isPending: bool
    isLocked: bool
    rawValue: str
    intValue: int
    numValue: float
    stringValue: str
    hasKeys: bool
    expression: str
    expressionLanguage: str
    isShowingExpression: bool
    checked: bool
    isAtDefault: bool
    isOnKey: bool
    isTimeDependent: bool
    dynamicStateChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forParm(cls, p: hou.Parm) -> Self: ...
    def __init__(self, **kwargs: object) -> None: ...
    def updateFromParm(self, parm: hou.Parm, frame: float | None = None) -> None: ...
    def updateChannelProperties(self, parm: hou.Parm, frame: float) -> None: ...
    def updateValueFromParm(self, parm: hou.Parm) -> None: ...

class TupleProxy(core.Info):
    name: str
    label: str
    level: int
    labelIsInternal: bool
    isSpare: bool
    isTimeDependent: bool
    invisible: bool
    isDisabled: bool
    isHidden: bool
    joinsWithNext: bool
    type: str
    dataType: str
    numComponents: int
    namingScheme: str
    look: str
    isLabelHidden: bool
    tags: dict[str, str]
    tokens: list[str]
    parms: list[ParmProxy]
    isAtDefault: bool
    isTab: bool
    underlayParmMenu: bool
    isHeaderTuple: bool
    menuType: str
    menuItems: Sequence[str]
    menuLabels: Sequence[str]
    menuIcons: Sequence[str]
    objects: models.MenuModel
    @classmethod
    def forTemplate(cls, ctx: Context, template: hou.ParmTemplate, override_type: str | None = None) -> Self: ...
    @classmethod
    def forTuple(cls, ctx: Context, pt: hou.ParmTuple, template: hou.ParmTemplate | None = None, override_type: str | None = None) -> Self: ...
    def __init__(self, context: Context, **kwargs: object) -> None: ...
    def __del__(self) -> None: ...
    def node(self) -> hou.Node: ...
    def parmTuple(self) -> hou.ParmTuple | None: ...
    def setComponent(self, component: int, value: _ParmValue) -> None: ...
    def set(self, value: _ParmValue) -> None: ...
    def revertToDefaults(self, bounce: bool) -> None: ...
    def setFromData(self, data: rtypes.ParmUnionData, bounce: bool) -> None: ...
    def pressActionButton(self, modifiers: int) -> None: ...
    def isJoinGroup(self) -> bool: ...
    def updateFromTuple(self, pt: hou.ParmTuple) -> None: ...
    def updateValues(self, pt: hou.ParmTuple) -> None: ...
    def updateTimeDependentProperties(self, pt: hou.ParmTuple, frame: float) -> None: ...
    def updateParmLocks(self, pt: hou.ParmTuple) -> None: ...
    def setupMenu(self, template: _MenuTemplate) -> None: ...
    def updateMenu(self) -> None: ...

class NumberTupleProxy(TupleProxy):
    defaultValues: Sequence[float]
    units: str
    minValue: float
    minIsStrict: bool
    maxValue: float
    maxIsStrict: bool
    @classmethod
    def forTuple(cls, ctx: Context, pt: hou.ParmTuple, template: hou.ParmTemplate | None = None, override_type: str | None = None) -> Self: ...

class RampProxy(TupleProxy):
    isColor: bool
    colorType: str
    points: models.RampModel
    shapeChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, ctx: Context, **kwargs: object) -> None: ...
    def lookupFloat(self, x: float) -> float: ...
    def lookupColor(self, x: float) -> PySide6.QtGui.QColor: ...
    def startEditing(self) -> None: ...
    def insertPoint(self, pos: float, value: float) -> int: ...
    def setPoint(self, index: int, pos: float, value: float) -> None: ...
    def movePoints(self, indices: Sequence[int], dx: float, dy: float) -> None: ...
    def finishEditing(self) -> None: ...
    def cancelEditing(self) -> None: ...
    def updateValues(self, pt: hou.ParmTuple) -> None: ...

class LabelProxy(TupleProxy):
    columnLabels: Sequence[str]
    labelParmType: str
    @classmethod
    def forTuple(cls, ctx: Context, pt: hou.ParmTuple, template: hou.ParmTemplate | None = None, override_type: str | None = None) -> Self: ...

class MenuProxy(TupleProxy):
    defaultValue: int | tuple[int, ...] | tuple[str, ...]
    isButton: bool
    isButtonStrip: bool
    isIconStrip: bool
    isIconMenu: bool
    def __init__(self, ctx: Context, **kwargs: object) -> None: ...
    @classmethod
    def forTemplate(cls, ctx: Context, template: hou.ParmTemplate, override_type: str | None = None) -> Self: ...
    def chooseButtonMenu(self, index: int) -> None: ...
    def updateFromTuple(self, pt: hou.ParmTuple) -> None: ...

class StringTupleProxy(TupleProxy):
    defaultValues: Sequence[str]
    stringType: str
    menuType: str
    menuItems: Sequence[str]
    menuLabels: Sequence[str]
    menuIcons: Sequence[str]
    tokens: list[str]
    @classmethod
    def forTemplate(cls, ctx: Context, template: hou.ParmTemplate, override_type: str | None = None) -> Self: ...
    def toggleStringToken(self, component: int, token: str) -> None: ...
    def updateValues(self, pt: hou.ParmTuple) -> None: ...

class ToggleProxy(TupleProxy):
    labelIsInternal: bool

class ButtonProxy(TupleProxy):
    labelIsInternal: bool
    def press(self, modifiers: int) -> None: ...

class DataProxy(TupleProxy):
    dataParmType: str
    isDict: bool
    rows: models.KeyValueModel
    @classmethod
    def forTemplate(cls, ctx: Context, template: hou.ParmTemplate, override_type: str | None = None) -> Self: ...
    def __del__(self) -> None: ...
    def updateValues(self, pt: hou.ParmTuple) -> None: ...

class FolderProxy(TupleProxy):
    defaultValue: int
    folderType: str
    endsTabGroup: bool
    tuples: list[TupleProxy]
    depth: int
    switcher: str
    toggle: ToggleProxy
    @classmethod
    def forTemplate(cls, ctx: Context, template: hou.ParmTemplate, override_type: str | None = None) -> Self: ...
    @classmethod
    def forTuple(cls, ctx: Context, pt: hou.ParmTuple, template: hou.ParmTemplate | None = None, override_type: str | None = None) -> Self: ...

class MultiparmTableModel(QtCore.QAbstractTableModel):
    TupleRole: int
    ParmRole: int
    ComponentIndexRole: int
    SourceRowRole: int
    NameRole: int
    TypeRole: int
    DataTypeRole: int
    ValueRole: int
    ScopedRole: int
    PendingRole: int
    LockedRole: int
    RawRole: int
    HasKeysRole: int
    ExpressionRole: int
    ExpressionLangRole: int
    CheckedRole: int
    AtDefaultRole: int
    OnKeyRole: int
    TimeDependentRole: int
    LookRole: int
    def __init__(self, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    def roleNames(self) -> dict[int, bytes]: ...
    def setParmTuple(self, pt: hou.ParmTuple, blocks: list[MultiparmBlock]) -> None: ...
    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = 0) -> str | None: ...
    def flags(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> PySide6.QtCore.Qt.ItemFlag: ...
    def setBlocks(self, blocks: list[MultiparmBlock]) -> None: ...
    def rowCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = None) -> int: ...
    def columnCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = None) -> int: ...
    def data(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, role: int = 0) -> TupleProxy | ParmProxy | str | int | float | bool | None: ...

class MultiparmProxy(FolderProxy):
    blocks: list[MultiparmBlock]
    sourceModelChanged: ClassVar[PySide6.QtCore.Signal]
    tableModelChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forTuple(cls, ctx: Context, pt: hou.ParmTuple, template: hou.ParmTemplate | None = None, override_type: str | None = None) -> Self: ...
    def __init__(self, context: Context, **kwargs: object) -> None: ...
    def sourceModel(self) -> MultiparmTableModel: ...
    def tableModel(self) -> PySide6.QtCore.QSortFilterProxyModel: ...
    def sortBy(self, column: int, reversed: bool) -> None: ...
    def moveMultiParmInstance(self, from_index: int, to_index: int) -> None: ...
    def updateValues(self, pt: hou.ParmTuple, force: bool = False) -> None: ...

class MultiparmBlock(core.Info):
    id: str
    expanded: bool
    tuples: list[TupleProxy]
    children: list[MultiparmBlock]

def multiparmBlocks(ctx: Context, pt: hou.ParmTuple) -> list[MultiparmBlock]: ...

class TabGroup(TupleProxy):
    level: int
    name: str
    tabs: list[FolderProxy]
    activeTab: float
    depth: int
    def __init__(self, context: Context, tab: FolderProxy, **kwargs: object) -> None: ...
    def open(self) -> bool: ...
    def append(self, tab: FolderProxy) -> None: ...
    def updateValues(self, pt: hou.ParmTuple) -> None: ...

class JoinGroup(TupleProxy):
    tuples: list[TupleProxy]
    def __init__(self, context: Context, proxy: TupleProxy, **kwargs: object) -> None: ...
    def isOpen(self) -> bool: ...
    def isJoinGroup(self) -> bool: ...

def proxyList(ctx: Context, templates: Sequence[hou.ParmTemplate]) -> list[TupleProxy]: ...

tuple_classes: tuple[tuple[TempTypeSpec, type[TupleProxy]], ...]

def proxyForTuple(ctx: Context, pt: hou.ParmTuple, template: hou.ParmTemplate | None = None) -> TupleProxy: ...

class ParmEditorConfig(config.BaseConfig):
    rowHeight: float
    rowSpacing: float
    showSliderTicks: bool
    fieldTintAlpha: float
    keyedColorName: str
    onKeyColorName: str
    pendingColorName: str

class ParmEditorState(qmlviews.SharedState[ParmEditorConfig]):
    labelWidth: float
    labelSpacing: float
    path: str
    name: str
    iconName: str
    typeName: str
    selectedNames: list[str]
    selectedPaths: list[str]
    typeOrder: list[str]
    parmTuples: list[TupleProxy]
    bounceRequested: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, **kwargs: object) -> None: ...
    def __del__(self) -> None: ...
    def findProxy(self, pt: hou.ParmTuple, event_type: hou.EnumValue[hou.nodeEventType] | None = None) -> tuple[hou.ParmTuple, TupleProxy]: ...
    def houdiniNamedColor(self, name: str) -> PySide6.QtGui.QColor: ...
    @property
    def lookup(self) -> weakref.WeakValueDictionary[str, TupleProxy]: ...
    @property
    def invisibles(self) -> set[str]: ...
    def viewColor(self, r: float, g: float, b: float, a: float) -> PySide6.QtGui.QColor: ...
    def tmiColor(self, t: float, m: float, i: float, a: float) -> PySide6.QtGui.QColor: ...
    def rgbToTmi(self, r: float, g: float, b: float) -> tuple[float, float, float]: ...
    def node(self) -> hou.Node | None: ...
    def setNetworkEditor(self, editor: hou.NetworkEditor) -> None: ...
    def updateSelection(self) -> None: ...
    def setSelectedNodes(self, selection: Sequence[hou.Node]) -> None: ...
    def reload(self) -> None: ...

class ParmEditorViewWindow(qmlviews.BaseQmlView[ParmEditorState]):
    SOURCE_URL: str
    def __init__(self, *, parent_window: PySide6.QtGui.QWindow | None = None) -> None: ...
    def setEditor(self, editor: hou.NetworkEditor) -> None: ...
