"""Configuration hou stub generation clean up.

The constants in this module act as overrides for the automatic type annotations we get from
the C++ type analysis.
"""

_TYPE_ALIAS_COMPONENTS = {
    "ATTRIB": ["int", "float", "str"],
    "PARM": ["bool", "int", "float", "str", "dict[str, str]", "'Ramp'", "'Geometry'"],
    "PARM_ARG_ONLY": ["'Parm'"],
    "PARM_RETURN_ONLY": ["'OpNode'"],
    "OPTION": [
        "bool",
        "int",
        "float",
        "str",
        "Vector2",
        "Vector3",
        "Vector4",
        "Quaternion",
        "Matrix3",
        "Matrix4",
    ],
    "OPTION_MULTI_ARG": [
        "bool",
        "int",
        "float",
        "str",
        "Vector2",
        "Vector3",
        "Vector4",
        "Quaternion",
        "Matrix3",
        "Matrix4",
        "Sequence[int]",
        "Sequence[float]",
    ],
    "OPTION_MULTI_RETURN": [
        "bool",
        "int",
        "float",
        "str",
        "Vector2",
        "Vector3",
        "Vector4",
        "Quaternion",
        "Matrix3",
        "Matrix4",
        "Tuple[int, ...]",
        "Tuple[float, ...]",
    ],
}


def get_type_aliases() -> dict[str, str]:
    attrib_arg_types = _TYPE_ALIAS_COMPONENTS["ATTRIB"] + [
        f"Sequence[{typ}]" for typ in _TYPE_ALIAS_COMPONENTS["ATTRIB"]
    ]
    attrib_return_types = _TYPE_ALIAS_COMPONENTS["ATTRIB"] + [
        f"Tuple[{typ}, ...]" for typ in _TYPE_ALIAS_COMPONENTS["ATTRIB"]
    ]

    parm_arg_types = (
        _TYPE_ALIAS_COMPONENTS["PARM"] + _TYPE_ALIAS_COMPONENTS["PARM_ARG_ONLY"]
    )
    parm_return_types = (
        _TYPE_ALIAS_COMPONENTS["PARM"] + _TYPE_ALIAS_COMPONENTS["PARM_RETURN_ONLY"]
    )

    result = {
        "AttribBasicType": " | ".join(_TYPE_ALIAS_COMPONENTS["ATTRIB"]),
        "AttribArgType": " | ".join(attrib_arg_types),
        "AttribDictArgType": " | ".join(
            f"dict[str, {typ}]" for typ in attrib_arg_types
        ),
        "AttribReturnType": " | ".join(attrib_return_types),
        "AttribDictReturnType": " | ".join(
            f"dict[str, {typ}]" for typ in attrib_return_types
        ),
        "ParmArgType": " | ".join(parm_arg_types),
        "ParmReturnType": " | ".join(parm_return_types),
        "ParmTupleArgType": " | ".join(f"Sequence[{typ}]" for typ in parm_arg_types),
        "ParmTupleReturnType": " | ".join(
            f"Tuple[{typ}, ...]" for typ in parm_return_types
        ),
        "OptionType": " | ".join(_TYPE_ALIAS_COMPONENTS["OPTION"]),
        "OptionSequenceType": " | ".join(
            f"Sequence[{typ}]" for typ in _TYPE_ALIAS_COMPONENTS["OPTION"]
        ),
        "OptionMultiArgType": " | ".join(_TYPE_ALIAS_COMPONENTS["OPTION_MULTI_ARG"]),
        "OptionMultiReturnType": " | ".join(
            _TYPE_ALIAS_COMPONENTS["OPTION_MULTI_RETURN"]
        ),
    }

    return result


TYPE_ALIASES = get_type_aliases()


ADDITIONAL_ENUM_NAMES = {
    "fbxMaterialMode": {
        "FBXShaderNodes",
        "PrincipledShaders",
        "VopNetworks",
    },
    "fbxCompatibilityMode": {
        "FBXStandard",
        "Maya",
    },
    "_ik_targetType": {
        "All",
        "Orientation",
        "Position",
    },
    "parmTemplateType": {
        "Folder",
        "Data",
    },
    "optionalBool": {
        "Yes",
        "No",
        "NoOpinion",
    },
}


# These will be added at the end of the stubs.
MISSING_CLASSES = {
    # hou.data comes from the houpythonportion.data module, but is accessible via hou
    None: {
        "_PointTupleGenerator": [
            "def __getitem__(self, key: int) -> Point",
            "def __len__(self) -> int",
            "def __repr__(self) -> str",
        ],
        "_PrimTupleGenerator": [
            "def __getitem__(self, key: int) -> Prim",
            "def __len__(self) -> int",
            "def __repr__(self) -> str",
        ],
        "_EdgeTupleGenerator": [
            "def __getitem__(self, key: int) -> Edge",
            "def __len__(self) -> int",
            "def __repr__(self) -> str",
        ],
        "_VertexTupleGenerator": [
            "def __getitem__(self, key: int) -> Vertex",
            "def __len__(self) -> int",
            "def __repr__(self) -> str",
        ],
        "data": [
            "@staticmethod\ndef clusterItemsAsData(items: Sequence[NetworkMovableItem], target_node: OpNode, frame_nodes: Sequence[NetworkMovableItem]=..., selected_nodes: Sequence[NetworkMovableItem]=..., current_node: NetworkMovableItem =..., flags: bool=True, nodes_only: bool=False, target_children: bool=False, children: bool=True, target_editables: bool=False, editables: bool=True, target_parms: Union[bool, Sequence[ParmTuple], Sequence[str]]=True, parms: bool=True, default_parmvalues: bool=False, evaluate_parmvalues: bool=False, parms_as_brief: bool=True, parmtemplates: str=..., metadata: bool=False, verbose: bool=False) -> dict[str, Any]",
            "@staticmethod\ndef createClusterItemsFromData(parent: OpNode, data: dict[str, Any], target_node: OpNode=..., clear_content=False, force_item_creation: bool=True, external_connections: bool=True, parms: bool=True, parmtemplates: bool=True, children: bool=True, editables: bool=True, offset_position: Vector2=..., skip_notes: bool=False) -> dict[str, NetworkMovableItem]",
            "@staticmethod\ndef createItemsFromData(parent: OpNode, data: dict[str, Any], clear_content: bool=False, force_item_creation: bool=True, offset_position: Vector2=..., external_connections: bool=True, parms: bool=True, parmtemplates: bool=True, children: bool=True, editables: bool=True, skip_notes: bool=False) -> dict[str, NetworkMovableItem]",
            "@staticmethod\ndef dataFromParms(parms: Sequence[ParmTuple], values: bool=True, evaluate_values: bool=False, locked: bool=True, brief: bool=True, multiparm_instances: bool=True, metadata: bool=False, verbose: bool=False) -> dict[str,Any]",
            "@staticmethod\ndef itemsAsData(items: Sequence[NetworkMovableItem], nodes_only: bool=False, children: bool=True, editables:bool=True, inputs: bool=True, position: bool=True, anchor_position: Vector2=..., flags: bool=True, parms: bool=True, parms_as_brief: bool=True, default_parmvalues: bool=False, evaluate_parmvalues: bool=False, parmtemplates: str=..., metadata: bool=False, verbose: bool=False) -> dict[str, Any]",
            "@staticmethod\ndef selectedItemsAsData(nodes_only: bool=False, children: bool=True, editables: bool=True, inputs: bool=True, position: bool=True, anchor_position: Vector2=..., flags: bool=True, parms: bool=True, parms_as_brief: bool=True, default_parmvalues: bool=False, evaluate_parmvalues: bool=False, parmtemplates: str=..., metadata: bool=False, verbose: bool=False) -> dict[str, Any]",
        ],
    },
    "qt": {
        "ColorField(QtWidgets.QWidget)": [
            "def __init__(self, label: str ='', include_alpha: bool = False) -> None",
            "def color(self) -> QtGui.QColor",
            "def setColor(self, color: QtGui.QColor) -> None",
        ],
        "ColorPalette(QtWidgets.QFrame)": [
            "paletteChanged: QtCore.Signal  # QtCore.Signal()",
            "colorEdited: QtCore.Signal  # QtCore.Signal(int, QtGui.QColor, QtGui.QColor)",
            "colorSelected: QtCore.Signal  # QtCore.Signal(int, QtGui.QColor)",
            "colorAccepted: QtCore.Signal  # QtCore.Signal(int, QtGui.QColor)",
            "colorCancelled: QtCore.Signal  # QtCore.Signal()",
            "def __init__(self, colors: Sequence[QtGui.QColor] | None =None, size: int = 32, by_column: bool = False, show_at_pointer: bool = True, columns: int | None =None, rows: int | None =None, allow_editing:bool=True, selected_index: int=-1, bg_color: QtGui.QColor | QtGui.QBrush | None=None, empty_color: QtGui.QColor | QtGui.QBrush | None = None, parent: QtWidgets.QWidget | None =None) -> None",
            "def color(self, index: int) -> None",
            "def colorCount(self) -> int",
            "def colorList(self) -> list[QtGui.QColor]",
            "def isEditingAllowed(self) -> bool",
            "def selectedColor(self) -> QtGui.QColor",
            "def selectedIndex(self) -> int",
            "def setColor(self, index: int, color: QtGui.QColor) -> None",
            "def setColorList(self, colors: Sequence[QtGui.QColor]) -> None",
            "def setEditingAllowed(self, allowed: bool) -> None",
            "def setSelectedIndex(self, index: int) -> None",
            "def setSwatchSize(self, size: int) -> None",
            "def swatchSize(self) -> int",
        ],
        "ColorSwatchButton(QtWidgets.QPushButton)": [
            "PositionOff: int",
            "PositionTop: int",
            "PositionBottom: int",
            "PositionLeft: int",
            "PositionRight: int",
            "PositionAll: int",
            "colorChanged: QtCore.Signal  # QtCore.Signal(QtGui.QColor)",
            "def __init__(self, include_alpha: bool=False) -> None",
            "def color(self) -> QtGui.QColor",
            "def hasAlpha(self) -> bool",
            "def secondaryColor(self) -> QtGui.QColor",
            "def secondaryColorPosition(self) -> int",
            "def setColor(self, color: QtGui.QColor) -> None",
            "def setSecondaryColor(self, color: QtGui.QColor) -> None",
            "def setSecondaryColorPosition(self, position: int) -> None",
        ],
        "ComboBox(QtWidgets.QComboBox)": [
            "def __init__(self) -> None",
        ],
        "Dialog(QtWidgets.QDialog)": [
            "def __init__(self) -> None",
        ],
        "FieldLabel(QtWidgets.QLabel)": [
            "def __init__(self, label: str) -> None",
        ],
        "FileChooserButton(QtWidgets.QToolButton)": [
            "fileSelected: QtCore.Signal  # QtCore.Signal(str)",
            "def __init__(self) -> None",
            "def setFileChooserDefaultValue(self, default_value: str) -> None",
            "def setFileChooserFilter(self, file_filter: EnumValue) -> None",
            "def setFileChooserIsImageChooser(self, is_image_chooser: bool) -> None",
            "def setFileChooserMode(self, chooser_mode: EnumValue) -> None",
            "def setFileChooserMultipleSelect(self, multiple_select: bool) -> None",
            "def setFileChooserPattern(self, file_pattern: str) -> None",
            "def setFileChooserStartDirectory(self, start_dir: str) -> None",
            "def setFileChooserTitle(self, title: str) -> None",
        ],
        "FileLineEdit(QtWidgets.QLineEdit)": [
            "def __init__(self, icon: QtGui.QIcon | str | None = None, parent: QtWidgets.QWidget | None = None) -> None",
        ],
        "GridLayout(QtWidgets.QGridLayout)": [
            "def __init__(self) -> None",
        ],
        "HelpButton(QtWidgets.QToolButton)": [
            "def __init__(self, help_path: str, tooltip: str = ...) -> None",
        ],
        "Icon(QtGui.QIcon)": [
            "def __init__(self, icon_name: str, width: int | None = None, height: int | None = None) -> None",
        ],
        "InputField(QtWidgets.QWidget)": [
            "IntegerType: int",
            "FloatType: int",
            "StringType: int",
            "valueChanged: QtCore.Signal  # QtCore.Signal()",
            "hotkeyInvoked: QtCore.Signal  # QtCore.Signal(str)",
            "editingFinished: QtCore.Signal  # QtCore.Signal(list)",
            "ladderChanged: QtCore.Signal  # QtCore.Signal()",
            "def __init__(self, data_type: int, num_components: int, label: str | None=..., mouse_hotkeys: Any | None = None, size_policy: QtWidgets.QSizePolicy | None=None, notify_pending_changes: bool=True, parent: QtWidgets.QWidget | None=None) -> None",
            "def menu(self) -> QtWidgets.QMenu",
            "def onContextMenuEvent(self, event: QtGui.QContextMenuEvent, context_menu: QtWidgets.QMenu) -> None",
            "def onMousePressEvent(self, event: QtGui.QMouseEvent) -> None",
            "def onMouseWheelEvent(self, event: QtGui.QWheelEvent) -> None",
            "def setAlignment(self, a: QtCore.Qt.Alignment | QtCore.Qt.AlignmentFlag) -> None",
            "def setMenu(self, menu: QtWidgets.QMenu) -> None",
            "def setState(self, state_name: str, state_value: bool, index: int = 0) -> None",
            "def setValidator(self, validator: QtGui.QValidator) -> None",
            "def setValue(self, value: int | float | str | None, index: int = 0) -> None",
            "def setValues(self, values: Sequence[int] | Sequence[float] | Sequence[str]) -> None",
            "def setWidth(self, width: float) -> None",
            "def state(self, state_name: str, index: int = 0) -> bool",
            "def value(self, index: int = 0) -> int | float | str",
            "def values(self) -> list[int] | list[float] | list[str]",
        ],
        "ListEditor(QtWidgets.QFrame)": [
            "listChanged: QtCore.Signal  # QtCore.Signal()",
            "checkChanged: QtCore.Signal  # QtCore.Signal(int, str, bool)",
            "itemEdited: QtCore.Signal  # QtCore.Signal(int, str)",
            "def __init__(self, strings: Sequence[str]=..., top_message: str | None=None, bottom_message: str | None=None, allow_editing: bool=True, allow_add_remove: bool=True, allow_reorder: bool=True, allow_empty_string: bool =True, show_checkboxes: bool=False, keep_sorted: bool = False, initial_string: str = '', initial_check: bool = True, exclusive_check: bool = False, allow_empty_list: bool = True, parent: QtWidgets.QWidget | None = None) -> None",
            "def addListItem(self, text: str, checked: bool | None=None, insert_at: int=-1) -> None",
            "def bottomMessage(self) -> str",
            "def checkedRow(self) -> int | None",
            "def checkedRows(self) -> list[int]",
            "def checkedString(self) -> str | None",
            "def checkedStrings(self) -> list[str]",
            "def clear(self) -> None",
            "def initialCheck(self) -> bool",
            "def initialString(self) -> str",
            "def isAddRemoveAllowed(self) -> bool",
            "def isEditingAllowed(self) -> bool",
            "def isEmptyListAllowed(self) -> bool",
            "def isEmptyStringAllowed(self) -> bool",
            "def isReorderAllowed(self) -> bool",
            "def itemCount(self) -> int",
            "def keepSorted(self) -> bool",
            "def removeRow(self, row_num: int) -> None",
            "def rowIsChecked(self, row_num: int) -> bool",
            "def rowString(self, row_num: int) -> str",
            "def setAllowAddRemove(self, allow: bool) -> None",
            "def setAllowEditing(self, allow: bool) -> None",
            "def setAllowEmptyList(self, allow: bool) -> None",
            "def setAllowEmptyString(self, allow: bool) -> None",
            "def setAllowReorder(self, allow: bool) -> None",
            "def setBottomMessage(self, text: str) -> None",
            "def setInitialCheck(self, checked: bool) -> None",
            "def setInitialString(self, text: str) -> None",
            "def setKeepSorted(self, keep_sorted: bool) -> None",
            "def setRowChecked(self, row_num: int, checked: bool) -> None",
            "def setShowCheckboxes(self, show: bool) -> None",
            "def setStrings(self, strings: Sequence[str]) -> None",
            "def setStringsAndChecks(self, strings_and_checks: Sequence[tuple[str, bool]]) -> None",
            "def setTopMessage(self, text: str) -> None",
            "def showCheckboxes(self) -> bool",
            "def strings(self) -> list[str]",
            "def stringsAndChecks(self) -> list[tuple[str, bool]]",
            "def topMessage(self) -> str",
        ],
        "ListEditorDialog(QtWidgets.QDialog)": [
            "def __init__(self, parent: QtWidgets.QWidget | None = None, window_type: QtCore.Qt.WindowType = ..., strings: Sequence[str]=..., top_message: str | None=None, bottom_message: str | None=None, allow_editing: bool=True, allow_add_remove: bool=True, allow_reorder: bool=True, allow_empty_string: bool =True, show_checkboxes: bool=False, keep_sorted: bool = False, initial_string: str = '', initial_check: bool = True, exclusive_check: bool = False, allow_empty_list: bool = True) -> None",
            "def editor(self) -> qt.ListEditor",
        ],
        "Menu(QtWidgets.QMenu)": [
            "def __init__(self) -> None",
        ],
        "MenuBar(QtWidgets.QMenuBar)": [
            "def __init__(self, parent: QtWidgets.QWidget | None=None) -> None",
        ],
        "MenuButton(QtWidgets.QPushButton)": [
            "def __init__(self, menu: QtWidgets.QMenu) -> None",
        ],
        "MixerFilterProxyModel(QtCore.QSortFilterProxyModel)": [],
        "NodeChooserButton(QtWidgets.QToolButton)": [
            "nodeSelected: QtCore.Signal  # QtCore.Signal(object)",
            "nodePathsSelected: QtCore.Signal  # QtCore.Signal(str)",
            "chooserStarted: QtCore.Signal  # QtCore.Signal()",
            "def __init__(self) -> None",
            "def setNodeChooserFilter(self, node_filter: EnumValue) -> None",
            "def setNodeChooserInitialNode(self, initial_node: OpNode) -> None",
            "def setNodeChooserRelativeToNode(self, relative_to_node: OpNode) -> None",
            "def setSelectMultiple(self, value: bool) -> None",
        ],
        "ParmChooserButton(QtWidgets.QToolButton)": [
            "parmSelected: QtCore.Signal  # QtCore.Signal(object)",
            "def __init__(self) -> None",
            "def setCategoryFilter(self, category_filter: EnumValue) -> None",
            "def setInitialSelection(self, initial_selection: OpNode) -> None",
            "def setRelativeToNode(self, relative_to_node: OpNode) -> None",
            "def setSelectMultiple(self, value: bool) -> None",
        ],
        "ParmDialog(QtWidgets.QWidget)": [
            "def __init__(self, node: OpNode | None, showTitleBar: bool = False, compact: bool = False, labelsize: float = -1.0) -> None",
            "def multiParmTab(self, parm: str) -> None",
            "def node(self) -> OpNode",
            "def scrollPosition(self) -> Vector2",
            "def setMultiParmTab(self, parm: str, index) -> None",
            "def setNode(self, node: OpNode | None) -> None",
            "def setScrollPosition(self, pos: Vector2) -> None",
            "def visibleParms(self) -> tuple[ParmTuple, ...]",
        ],
        "ParmTupleChooserButton(QtWidgets.QToolButton)": [
            "parmTupleSelected: QtCore.Signal  # QtCore.Signal(object)",
            "def __init__(self) -> None",
            "def setCategoryFilter(self, category_filter: EnumValue) -> None",
            "def setInitialSelection(self, initial_selection: OpNode) -> None",
            "def setRelativeToNode(self, relative_to_node: OpNode) -> None",
            "def setSelectMultiple(self, value: bool) -> None",
        ],
        "SearchLineEdit(QtWidgets.QLineEdit)": [
            "searchBackward: QtCore.Signal  # QtCore.Signal()",
            "def __init__(self, icon: QtGui.QIcon | str | None = None, parent: QtWidgets.QWidget | None = None) -> None",
            "def allowSearchBackward(self) -> bool",
            "def setAllowSearchBackward(self, on: bool) -> None",
        ],
        "Separator(QtWidgets.QFrame)": [
            "def __init__(self) -> None",
        ],
        "ToolTip(QtWidgets.QWidget)": [
            "def __init__(self) -> None",
            "def setHelpUrl(self, help_url: str) -> None",
            "def setHotkey(self, hotkey: str) -> None",
            "def setTargetWidget(self, widget: QtWidgets.QWidget) -> None",
            "def setText(self, text: str) -> None",
            "def setTitle(self, title: str) -> None",
        ],
        "TrackChooserButton(QtWidgets.QToolButton)": [
            "trackSelected: QtCore.Signal  # QtCore.Signal(object)",
            "def __init__(self) -> None",
            "def setInitialSelection(self, initial_track: Track) -> None",
            "def setNodeChooserFilter(self, node_filter: EnumValue) -> None",
            "def setSelectMultiple(self, value: bool) -> None",
        ],
        "WindowOverlay(QtWidgets.QWidget)": [
            "def __init__(self, parent: qt.Window, win_floating_panel: QtWidgets.QWidget | None) -> None",
            "def onContainerWindowEvent(self, event: QtCore.QEvent) -> None",
            "def onInitWindow(self) -> None",
            "def onParentWindowEvent(self, event: QtCore.QEvent) -> None",
            "def windowContainer(self) -> QtWidgets.QWidget",
        ],
        "Window(QtWidgets.QWidget)": [
            "def __init__(self) -> None",
        ],
        "ViewerOverlay(WindowOverlay)": [
            "def __init__(self, scene_viewer: SceneViewer) -> None",
            "def moveBy(self, delta: QtCore.QPoint) -> None",
            "def moveTo(self, pos: QtCore.QPoint) -> None",
            "def onBeginResize(self) -> None",
            "def onColorSchemeChanged(self) -> None",
            "def onEndResize(self) -> None",
            "def onInitWindow(self) -> None",
            "def onLayoutChanged(self) -> None",
            "def onMoveContainerWindow(self, new_pos: QtCore.QPoint, old_pos: QtCore.QPoint) -> None",
            "def onResizing(self) -> None",
            "def onSizeChanged(self) -> None",
            "def onViewerActivated(self) -> None",
            "def onViewerDeactivated(self) -> None",
            "def onWindowPlacement(self) -> None",
            "def sceneViewer(self) -> SceneViewer",
        ],
        "XMLMenuParser(object)": [
            "def __init__(self, context: str ='', kwargs: dict[str, Any] | None=None, kwargsfunc=Callable, xmlfilename: Path | str | None=None, xmlstring: str | None=None) -> None",
            "def generateMenu(self, kwargs: dict[str, Any], menu:qt.Menu | None=None, actionitem_callback: Callable[[str], None] | None=None) -> None",
            "def handleKeyPress(self, keystring: str, kwargs: dict[str, Any], actionitem_callback: Callable | None=None, hotkey_context: str | None=None) -> None",
            "def hotkeyContext(self) -> str",
            "def parseFile(self, xmlfile: Path | str) -> None",
            "def parseFiles(self, xmlfilename: str) -> None",
            "def parseString(self, xmlstring: str) -> None",
            "def setHotkeyContext(self, hotkey_context) -> None",
        ],
    },
}


# Define functions that are missing entirely from hou.py
# This may come from the houpythonportion package, which patches these methods
# in via a setattr decorator.
# WARNING: Try not to redefine functions that are deprecated and have been removed from hou.py
MISSING_DEFINITIONS = {
    # Missing module level imports are sorted into the `None` class.
    None: [
        # NOTE: These are left as an example of deprecated functions that should not be added.
        # "def expandString(text: str) -> str",
        # "def expandStringAtFrame(text: str, frame_number: float) -> str",
    ],
    "Agent": [
        "def clipCatalog(self) -> AgentClip",
        "def layers(self) -> AgentLayer",
        "def rig(self) -> AgentRig",
        "def shapeLibrary(self) -> AgentShapeLibrary",
    ],
    "NetworkItem": [
        "def __lt__(self, other: object) -> bool",
        "def __le__(self, other: object) -> bool",
        "def __gt__(self, other: object) -> bool",
        "def __ge__(self, other: object) -> bool",
        "def __eq__(self, other: object) -> bool",
        "def __ne__(self, other: object) -> bool",
    ],
    "Node": [
        "def createOutputNode(self, node_type_name: str, node_name: str | None = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> Self",
        "def createInputNode(self, input_index: int, node_type_name: str, node_name: str | None = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> Self",
        "def creationTime(self) -> datetime.datetime",
        "def modificationTime(self) -> datetime.datetime",
        "def outputsWithIndices(self, ignore_network_dots: bool = False, use_names: bool = False) -> list[tuple[NetworkMovableItem, int | str, int | str]]",
    ],
    "OpNode": [
        "def appendParmTemplatesFromData(self, data: dict[str, Any], rename_conflicts: bool = True) -> dict[str, ParmTuple]",
        "def appendParmTemplatesToFolderFromData(self, data: dict[str, Any], parm_name: str, rename_conflicts: bool = True) -> dict[str, ParmTuple]",
        "def asData(self, nodes_only: bool = False, children: bool = False, editables: bool = False, inputs: bool = False, position: bool = False, flags: bool = False, parms: Union[bool, Sequence[ParmTuple], Sequence[str]]=True, default_parmvalues: bool = False, evaluate_parmvalues: bool = False, parms_as_brief: bool = True, parmtemplates: str=..., metadata: bool = False, verbose: bool = False) -> dict[str, Any]",
        "def children(self) -> Tuple[OpNode, ...]",
        "def childrenAsData(self, nodes_only: bool = False, children: bool = True, editables: bool = True, inputs: bool = True, position: bool = True, flags: bool = True, parms: bool = True, default_parmvalues: bool = False, evaluate_parmvalues: bool = False, parms_as_brief: bool = True, parmtemplates: str=..., metadata: bool = False, verbose: bool = False) -> dict[str, Any]",
        "def createDecorationItemsFromData(self, items: Sequence[NetworkMovableItem], frame_nodes: Sequence[NetworkMovableItem] | None=None, selected_nodes: Sequence[NetworkMovableItem] | None=None, current_node: NetworkMovableItem | None=None, flags: bool = True, nodes_only: bool = False, target_children: bool = False, children: bool = True, target_editables: bool = False, editables: bool = True, target_parms: Union[bool, Sequence[ParmTuple], Sequence[str]]=True, parms: bool = True, default_parmvalues: bool = False, evaluate_parmvalues: bool = False, parms_as_brief: bool = True, parmtemplates: str=..., metadata: bool = False, verbose: bool = False) -> dict[str, Any]",
        "def createNode(self, node_type_name: str, node_name: str | None = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False, force_valid_node_name: bool = False) -> OpNode",
        "def editablesAsData(self, nodes_only: bool = False, children: bool = True, editables: bool = True, inputs: bool = True, position: bool = True, flags: bool = True, parms: bool = True, default_parmvalues: bool = False, evaluate_parmvalues: bool = False, parms_as_brief: bool = True, parmtemplates: str=..., metadata: bool = False, verbose: bool = False) -> dict[str, Any]",
        "def inputConnections(self) -> Tuple[OpNodeConnection, ...]",
        "def inputsAsData(self, ignore_network_dots: bool = False, ignore_subnet_indirect_inputs: bool = False, use_names: bool = False) -> Sequence[dict[str, Any]]",
        "def insertParmTemplatesAfterFromData(self, data: dict[str, Any], parm_name: str, rename_conflicts: bool = True) -> dict[str, ParmTuple]",
        "def insertParmTemplatesBeforeFromData(self, data: dict[str, Any], parm_name: str, rename_conflicts: bool = True) -> dict[str, ParmTuple]",
        "def node(self, node_path: str) -> OpNode | None",
        "def outputConnections(self) -> Tuple[OpNodeConnection, ...]",
        "def outputsAsData(self, ignore_network_dots: bool = False, ignore_subnet_indirect_inputs: bool = False, use_names: bool = False) -> Sequence[dict[str, Any]]",
        "def parmTemplateChildrenAsData(self, name: str= '', parmtemplate_order: bool = False) -> dict[str, Any]",
        "def parmTemplatesAsData(self, name: str= '', children: bool = True, parmtemplate_order: bool = False) -> dict[str, Any]",
        "def parmsAsData(self, values: bool = True, parms: bool = True, default_values: bool = False, evaluate_values: bool = False, locked: bool = True, brief: bool = True, multiparm_instances: bool = True, metadata: bool = False, verbose: bool = False) -> dict[str, Any]",
        "def prependParmTemplatesToFolderFromData(self, data: dict[str, Any], parm_name: str, rename_conflicts: bool = True) -> dict[str, ParmTuple]",
        "def replaceParmTemplatesFromData(self, data: dict[str, Any]) -> dict[str, ParmTuple]",
        "def setChildrenFromData(self, clear_content: bool = True, force_item_creation: bool = True, offset_position: Vector2=..., external_connections: bool = True, parms: bool = True, parmtemplates: bool = True, children: bool = True, editables: bool = True, skip_notes: bool = False) -> None",
        "def setEditablesFromData(self, clear_content: bool = True, force_item_creation: bool = True, offset_position: Vector2=..., external_connections: bool = True, parms: bool = True, parmtemplates: bool = True, children: bool = True, editables: bool = True, skip_notes: bool = False) -> None",
        "def setFromData(self, data: dict[str, Any], clear_content: bool = False, force_item_creation: bool = True, parms: bool = True, parmtemplates: bool = True, children: bool = True, editables: bool = True, skip_notes: bool = False) -> None",
        "def setInputsFromData(self, data: dict[str, Any]) -> None",
        "def setOutputsFromData(self, data: dict[str, Any]) -> None",
        "def setParmExpressions(self, parm_dict: Mapping[str, str | Sequence[str]], language: EnumValue | None = None, replace_expressions: bool = True) -> None",
        "def setParms(self, parm_dict: Mapping[str, ParmArgType | ParmTupleArgType]) -> None",
        "def setParmsFromData(self, data: dict[str, Any]) -> None",
        "def type(self) -> OpNodeType",
    ],
    "OpNodeType": [
        "def category(self) -> OpNodeTypeCategory",
    ],
    "OpNodeTypeCategory": [
        "def nodeTypes(self) -> dict[str, OpNodeType]",
        "def nodeType(self, type_name: str) -> Optional[OpNodeType]",
    ],
    "Parm": [
        "def appendMultiParmInstancesFromData(self, data: Sequence[dict[str, Any]]) -> None",
        "def asData(self, value: bool=True, evaluate_value=False, locked: bool=True, brief: bool=True, multiparm_instances: bool=True, metadata: bool=False, verbose: bool=False, default_values: bool=...) -> dict[str, Any]",
        "def clipData(self, start:float|None=None, end:float|None=None, binary:bool=True, use_blosc_compression: bool=True, sample_rate:float=0) -> bytes",
        "def insertMultiParmInstancesFromData(self, data: Sequence[dict[str, Any]], index: int=0) -> None",
        "def insertTemplatesFromData(self, data: dict[str, Any], operation: str=..., rename_conflicts:bool=True) -> None",
        "def multiParmInstancesAsData(self, start_index: int=0, end_index: int=-1, value: bool = True, evaluate_value: bool = False, links: bool = True, locked: bool = True, brief: bool = True, metadata: bool = False, verbose: bool = False) -> Sequence[dict[str, Any]]",
        "def rampPointsAsData(self, evaluate: bool = True, metadata: bool = False, verbose: bool = False) -> Sequence[dict[str, Any]]",
        "def saveClip(self, file_name:str, start:float|None=None, end:float|None=None, sample_rate: float=0) -> None",
        "def set(self, value: int | float | str | dict[str, str] | Parm | Ramp | Geometry, language: EnumValue | None = None, follow_parm_reference: bool = True) -> None",
        "def setFromData(self, data: dict[str, Any]) -> None",
        "def setMultiParmInstancesFromData(self, data: Sequence[dict[str, Any]]) -> None",
        "def setRampPointsFromData(self, data: Sequence[dict[str, Any]]) -> None",
        "def setValueFromData(self, data: int | str | float | dict[str, Any] | Sequence[int] | Sequence[float] | Sequence[str]) -> None",
        "def templateAsData(self, children: bool = True) -> dict[str, Any]",
        "def templateChildrenAsData(self, parmtemplate_order: bool = False) -> dict[str, Any]",
        "def valueAsData(self, evaluate: bool = True, verbose: bool = True) -> int | str | float | dict[str, Any] | list[int] | list[float] | list[str]",
    ],
    "ParmTuple": [
        "def __iter__(self) -> Iterator[Parm]",
        "def asData(self, value: bool=True, evaluate_value=False, locked: bool=True, brief: bool=True, multiparm_instances: bool=True, metadata: bool=False, verbose: bool=False, default_values: bool=...) -> dict[str, Any]",
        "def clipData(self, start:float|None=None, end:float|None=None, binary:bool=True, use_blosc_compression: bool=True, sample_rate:float=0) -> bytes",
        "def insertMultiParmInstancesFromData(self, data: Sequence[dict[str, Any]], index: int=0) -> None",
        "def insertTemplatesFromData(self, data: dict[str, Any], operation: str = ..., rename_conflicts: bool = True) -> None",
        "def multiParmInstancesAsData(self, start_index: int=0, end_index: int=-1, value: bool = True, evaluate_value: bool = False, links: bool = True, locked: bool = True, brief: bool = True, metadata: bool = False, verbose: bool = False) -> Sequence[dict[str, Any]]",
        "def rampPointsAsData(self, evaluate: bool = True, metadata: bool = False, verbose: bool = False) -> Sequence[dict[str, Any]]",
        "def saveClip(self, file_name:str, start:float|None=None, end:float|None=None, sample_rate: float=0) -> None",
        "def set(self, value: Sequence[int] | Sequence[float] | Sequence[str] | Sequence[Parm] | ParmTuple, language: EnumValue | None = None, follow_parm_reference: bool = True) -> None",
        "def setFromData(self, data: dict[str, Any]) -> None",
        "def setMultiParmInstancesFromData(self, data: Sequence[dict[str, Any]]) -> None",
        "def setRampPointsFromData(self, data: Sequence[dict[str, Any]]) -> None",
        "def setValueFromData(self, data: int | str | float | dict[str, Any] | Sequence[int] | Sequence[float] | Sequence[str]) -> None",
        "def templateAsData(self, children: bool = True, parmtemplate_order: bool = False) -> dict[str, Any]",
        "def templateChildrenAsData(self, parmtemplate_order: bool = False) -> dict[str, Any]",
        "def valueAsData(self, evaluate: bool = True, verbose: bool = True) -> int | str | float | dict[str, Any] | list[int] | list[float] | list[str]",
    ],
    "Prim": [
        "def voxelRangeAsBool(self, range: BoundingBox) -> Tuple[bool, ...]",
        "def voxelRangeAsInt(self, range: BoundingBox) -> Tuple[int, ...]",
        "def voxelRangeAsFloat(self, range: BoundingBox) -> Tuple[float, ...]",
        "def voxelRangeAsVector3(self, range: BoundingBox) -> Sequence[Vector3]",
    ],
    "Geometry": [
        "def pointAttribs(self, scope: EnumValue = ...) -> Tuple[Attrib, ...]",
        "def primAttribs(self, scope: EnumValue = ...) -> Tuple[Attrib, ...]",
        "def vertexAttribs(self, scope: EnumValue = ...) -> Tuple[Attrib, ...]",
        "def globalAttribs(self, scope: EnumValue = ...) -> Tuple[Attrib, ...]",
    ],
    "Vector2": [
        "def __contains__(self, other: float) -> bool",
        "def __iter__(self) -> Iterator[float]",
        "def __reversed__(self) -> Iterator[float]",
    ],
    "Vector3": [
        "def __contains__(self, other: float) -> bool",
        "def __iter__(self) -> Iterator[float]",
        "def __reversed__(self) -> Iterator[float]",
    ],
    "Vector4": [
        "def __contains__(self, other: float) -> bool",
        "def __iter__(self) -> Iterator[float]",
        "def __reversed__(self) -> Iterator[float]",
    ],
    "hda": [
        "@staticmethod\ndef reloadHDAModule(hda_module: HDAModule) -> None",
    ],
    "hipFile": {
        "@staticmethod\ndef addEventCallback(callback: Callable[[EnumValue], None]) -> None",
        "@staticmethod\ndef removeEventCallback(callback: Callable[[EnumValue], None]) -> None",
        "@staticmethod\ndef eventCallbacks() -> Tuple[Callable[[EnumValue], None], ...]",
    },
    "qt": [
        "@staticmethod\ndef mainWindow() -> QtWidgets.QMainWindow",
    ],
    "ui": [
        "@staticmethod\ndef selectFile(start_directory: str | None = None, title: str | None = None, collapse_sequences: bool = False, file_type: EnumValue = fileType.Any, pattern: str | None = None, default_value: str | None = None, multiple_select: bool = False, image_chooser: bool = False, chooser_mode: EnumValue = fileChooserMode.ReadAndWrite, width: int = 0, height: int = 0) -> str",
        "@staticmethod\ndef selectNode(relative_to_node: Node | None = None, initial_node: Node | None = None, node_type_filter: EnumValue | None = None, title: str | None = None, width: int = 0, height: int = 0, multiple_select: bool = False, custom_node_filter_callback: Callable[[Node], bool] | None = None) -> str | Tuple[str, ...] | None",
        "@staticmethod\ndef openTypePropertiesDialog(node_or_node_type: OpNode | OpNodeType, promote_spare_parms: bool=False, immediately_save: bool=False) -> None",
    ],
}


# Functions that return these types are never optional.
NON_OPTIONAL_RETURN_TYPES = {
    "EnumValue",
    "Iterator",
    "Matrix2",
    "Matrix3",
    "Matrix4",
    "Quaternion",
    "Tuple",
    "Vector2",
    "Vector3",
    "Vector4",
    "std.vector",
    "tuple",
}


# Functions that are not Optional returns, even though they are pointers.
NON_OPTIONAL_RETURN_FUNCTIONS = {
    None: {
        "root",
        "pwd",
        "phm",
        "currentDopNet",
        "createApexRootNode",
        "nodeTypeCategories",
        "addNodeBundle",
    },
    "_clone_Connection": {
        "duplicate",
        "lopNode",
    },
    "_ik_Target": {
        "joint",
    },
    "Face": {
        "addVertex",
        "vertex",
    },
    "Agent": {
        "collisionLayer",
        "currentLayer",
        "definition",
    },
    "AgentClip": {
        "freeze",
    },
    "AgentDefinition": {
        "freeze",
        "metadata",
        "rig",
        "shapeLibrary",
    },
    "AgentMetadata": {
        "freeze",
    },
    "AgentRig": {
        "freeze",
    },
    "AgentShape": {
        "freeze",
        "geometry",
    },
    "AgentShapeBinding": {
        "deformer",
        "shape",
    },
    "AgentShapeLibrary": {
        "addShape",
        "data",
        "freeze",
    },
    "Attrib": {
        "dataId",
        "geometry",
    },
    "ChannelGraphSelection": {
        "animBar",
        "channelList",
        "graph",
        "parm",
    },
    "ChannelPrim": {
        "addVertex",
        "vertex",
    },
    "ChopNode": {
        "addVertex",
        "clip",
    },
    "Color": {
        "ocio_transform",
        "ocio_viewTransform",
    },
    "ConstructionPlane": {
        "sceneViewer",
        "transform",
    },
    "DataParmTemplate": {
        "defaultExpressionLanguage",
    },
    "Desktop": {
        "createFloatingPane",
        "createFloatingPaneTab",
        "shelfDock",
    },
    "DopData": {
        "createSubData",
        "freeze",
        "options",
        "simulation",
    },
    "DopNode": {
        "pythonSolverData",
        "simulation",
    },
    "DopSimulation": {
        "dopNetNode",
    },
    "Edge": {
        "geometry",
    },
    "EdgeGroup": {
        "dataId",
        "geometry",
    },
    "FlipbookSettings": {
        "stash",
    },
    "Gallery": {
        "createEntry",
    },
    "GalleryEntry": {
        "createChildNode",
    },
    "Geometry": {
        "addArrayAttrib",
        "createBezierCurve",
        "createBezierSurface",
        "createChannelPrim",
        "createEdgeGroup",
        "createHexahedron",
        "createHexahedronInPlace",
        "createMeshSurface",
        "createNURBSCurve",
        "createNURBSCurve",
        "createNURBSSurface",
        "createPacked",
        "createPoint",
        "createPointGroup",
        "createPolygon",
        "createPrimGroup",
        "createTetrahedron",
        "createTetrahedronInPlace",
        "createVertexGroup",
        "createVolume",
        "freeze",
        "primitiveIntrinsicsDataId",
        "selection",
        "topologyDataId",
        "unpackFromFolder",
    },
    "GeometryDrawable": {
        "geometry",
    },
    "GeometryDrawableGroup": {
        "drawable",
        "geometry",
    },
    "GeometrySelection": {
        "drawable",
        "geometry",
    },
    "GeometryViewport": {
        "camera",
        "defaultCamera",
        "settings",
    },
    "GeometryViewportCamera": {
        "stash",
    },
    "GeometryViewportSettings": {
        "backgroundImage",
        "displaySet",
    },
    "HDADefinition": {
        "addSection",
        "nodeType",
        "options",
        "parmTemplateGroup",
    },
    "HDASection": {
        "definition",
    },
    "IndexPairPropertyTable": {
        "attrib",
        "propertyDataType",
    },
    "InterruptableOperation": {
        "__enter__",
    },
    "LopNetwork": {
        "viewportOverrides",
        "viewportLoadMasks",
        "loadNamedViewportLoadMasks",
        "editablePostLayer",
    },
    "LopNode": {
        "loadMasks",
        "selectionRule",
        "viewerNode",
    },
    "LopPostLayer": {
        "__enter__",
    },
    "LopViewportOverrides": {
        "__enter__",
    },
    "NodeConnection": {
        "outputItem",
    },
    "Node": {
        "childTypeCategory",
        "collapseIntoSubnet",
        "copyNetworkBox",
        "copyStickyNote",
        "createInputNode",
        "createNetworkBox",
        "createNetworkDot",
        "createNode",
        "createOutputNode",
        "createStickyNote",
        "creator",
        "moveToGoodPosition",
        "type",
    },
    "NodeGroup": {
        "parent",
    },
    "NodeType": {
        "parmTemplateGroup",
    },
    "OpNode": {
        "addNodeGroup",
        "hdaModule",
        "hm",
        "parmTemplateGroup",
        "expressionLanguage",
        "simulation",
    },
    "OpNodeTypeCategory": {
        "createDigitalAsset",
    },
    "PackedGeometry": {"getEmbeddedGeometry"},
    "PackedPrim": {
        "vertex",
    },
    "Pane": {
        "createTab",
        "currentTab",
        "splitHorizontally",
        "splitVertically",
    },
    "PaneTab": {
        "clone",
        "setType",
    },
    "Parm": {
        "evalAsRamp",
        "evalAsRampAtFrame",
        "expressionLanguage",
        "getReferencedParm",
        "parmTemplate",
        "tuple",
        "uiBackgroundColor",
    },
    "ParmTemplate": {
        "clone",
    },
    "ParmTemplateGroup": {
        "entryAtIndices",
    },
    "ParmTuple": {
        "__getitem__",
        "parmTemplate",
    },
    "PathBasedPaneTab": {
        "currentNode",
        "pwd",
    },
    "PerfMonEvent": {
        "__enter__",
    },
    "Point": {
        "geometry",
    },
    "PointGroup": {
        "dataId",
    },
    "Prim": {
        "geometry",
    },
    "PrimGroup": {
        "dataId",
    },
    "Quadric": {
        "vertex",
    },
    "RadialMenu": {
        "categories",
        "createScriptItem",
        "createSubmenu",
        "item",
        "items",
        "label",
        "root",
        "shortcut",
        "sourceFile",
    },
    "RadialScriptItem": {
        "check",
        "icon",
        "label",
        "script",
        "shortcut",
    },
    "RadialSubmenu": {
        "createScriptItem",
        "createSubmenu",
        "items",
        "label",
        "shortcut",
    },
    "RedrawBlock": {
        "__enter__",
    },
    "ReferencePlane": {
        "sceneViewer",
    },
    "SceneViewer": {
        "constructionPlane",
        "curViewport",
        "flipbookSettings",
        "referencePlane",
        "selectGeometry",
        "selectedViewport",
    },
    "ScriptEvalContext": {
        "__enter__",
    },
    "Selection": {
        "freeze",
    },
    "Selector": {
        "nodeType",
    },
    "SimpleDrawable": {"geometry"},
    "SopNode": {
        "curPoint",
        "curPrim",
        "curVertex",
    },
    "SopNodeType": {
        "addSelector",
    },
    "StyleSheet": {
        "clone",
        "cloneWithAddedStyleSheet",
        "cloneWithObject",
        "cloneWithPrim",
        "cloneWithShape",
    },
    "Surface": {
        "vertex",
    },
    "Take": {
        "addChildTake",
        "insertTakeAbove",
    },
    "Track": {
        "clip",
    },
    "UndosDisabler": {
        "__enter__",
    },
    "UndosGroup": {
        "__enter__",
    },
    "VDB": {
        "vertex",
    },
    "Vertex": {
        "geometry",
        "point",
        "prim",
    },
    "VertexGroup": {
        "dataId",
        "geometry",
    },
    "VexContext": {
        "nodeTypeCategory",
    },
    "ViewerDragger": {
        "curViewport",
        "viewport",
    },
    "ViewerState": {
        "nodeType",
    },
    "ViewportVisualizer": {
        "evalParmAsRamp",
        "type",
    },
    "Volume": {
        "vertex",
    },
    "VopNetNode": {
        "definedType",
        "vexContext",
    },
    "VopNode": {
        "insertParmGenerator",
    },
    "anim": {
        "newBookmark",
    },
    "clone": {
        "createClone",
    },
    "galleries": {
        "createGalleryEntry",
    },
    "lop": {
        "createConnectionParmsForProperty",
        "createParmsForParameter",
        "createParmsForProperty",
        "outputProcessorParms",
        "shaderNodeType",
    },
    "perfMon": {
        "loadProfile",
        "startCookEvent",
        "startEvent",
        "startPaneEvent",
        "startProfile",
        "startTimedCookEvent",
        "startTimedEvent",
    },
    "playbar": {
        "animBar",
        "channelList",
        "channelListFromNodes",
        "channelListFromParmTuples",
        "channelListFromParms",
        "channelListFromSelection",
        "frameRange",
        "playbackRange",
        "selectionRanges",
        "timeRange",
        "timelineRange",
    },
    "properties": {
        "parmTemplate",
    },
    "shelves": {
        "newShelf",
        "newShelfSet",
        "newTool",
    },
    "takes": {
        "currentTake",
        "rootTake",
    },
    "ui": {
        "createDialog",
        "createRadialItem",
        "createRadialMenu",
        "curDesktop",
        "device",
        "sharedAssetGalleryDataSource",
        "showFloatingParameterEditor",
    },
    "undos": {
        "disabler",
        "group",
    },
    "viewportVisualizer": {
        "copyVisualizer",
    },
}

# Functions for which we want to declare a specific return type.
EXPLICIT_RETURN_TYPES = {
    None: {
        "shopNodeTypeCategory": "OpNodeTypeCategory",
        "ropNodeTypeCategory": "OpNodeTypeCategory",
        "dataNodeTypeCategory": "OpNodeTypeCategory",
        "apexNodeTypeCategory": "ApexNodeTypeCategory",
        "chopNetNodeTypeCategory": "OpNodeTypeCategory",
        "chopNodeTypeCategory": "OpNodeTypeCategory",
        "dopNodeTypeCategory": "OpNodeTypeCategory",
        "cop2NetNodeTypeCategory": "OpNodeTypeCategory",
        "cop2NodeTypeCategory": "OpNodeTypeCategory",
        "copNodeTypeCategory": "OpNodeTypeCategory",
        "objNodeTypeCategory": "OpNodeTypeCategory",
        "rootNodeTypeCategory": "OpNodeTypeCategory",
        "lopNodeTypeCategory": "OpNodeTypeCategory",
        "managerNodeTypeCategory": "OpNodeTypeCategory",
        "sopNodeTypeCategory": "OpNodeTypeCategory",
        "topNodeTypeCategory": "OpNodeTypeCategory",
        "vopNetNodeTypeCategory": "OpNodeTypeCategory",
        "vopNodeTypeCategory": "OpNodeTypeCategory",
    },
    "Bundle": {
        "pattern": "str | None",
    },
    "Color": {
        "hsl": "Tuple[float, float, float]",
        "hsv": "Tuple[float, float, float]",
        "lab": "Tuple[float, float, float]",
        "rgb": "Tuple[float, float, float]",
        "tmi": "Tuple[float, float, float]",
        "xyz": "Tuple[float, float, float]",
    },
    "DopData": {
        "creator": "OpNode",
        "dopNetNode": "OpNode",
    },
    "DopNode": {
        "createdObjects": "Tuple[DopObject, ...]",
        "displayNode": "OpNode | None",
        "dopNetNode": "OpNode",
        "objectsToProcess": "Tuple[DopObject, ...]",
        "processedObjects": "Tuple[DopObject, ...]",
        "renderNode": "OpNode | None",
    },
    "GeometrySelection": {
        "mergedNode": "SopNode",
    },
    "HDADefinition": {
        "nodeType": "OpNodeType",
        "nodeTypeCategory": "OpNodeTypeCategory",
    },
    "LopNode": {
        "activeLayer": "pxr.Sdf.Layer | None",
        "editableLayer": "pxr.Sdf.Layer | None",
        "editableStage": "pxr.Usd.Stage | None",
        "inputPrims": "Tuple[pxr.Sdf.Path, ...]",
        "lastModifiedPrims": "Tuple[pxr.Sdf.Path, ...]",
        "network": "OpNode",
        "sourceLayer": "pxr.Sdf.Layer | None",
        "stage": "pxr.Usd.Stage | None",
        "uneditableStage": "pxr.Usd.Stage | None",
    },
    "LopSelectionRule": {
        "sourceNode": "LopNode | None",
    },
    "OpNode": {
        "changeNodeType": "ChopNode",
        "createDigitalAsset": "OpNode",
        "findOrCreateMotionEffectsNetwork": "OpNode",
    },
    "OpNodeType": {
        "instances": "Tuple[OpNode, ...]",
    },
    "Parm": {
        "createClip": "ChopNode",
        "node": "OpNode",
        "evalAsNode": "OpNode | None",
        "evalAsNodeAtFrame": "OpNode | None",
    },
    "ParmTuple": {
        "createClip": "ChopNode",
        "node": "OpNode",
    },
    "PythonPanel": {"activeInterfaceRootWidget": "QtWidgets.QWidget"},
    "ScriptEvalContext": {
        "node": "OpNode | None",
    },
    "VDB": {
        "voxelRange": "Tuple[bool, ...] | Tuple[int, ...] | Tuple[float, ...] | Tuple[Vector3, ...]"
    },
    "ViewerState": {
        "categoryNode": "OpNode | None",
    },
    "ViewportVisualizer": {
        "evalParm": "int | float | str",
    },
    "dop": {"scriptSolverNetwork": "OpNode | None"},
}

# Completely redefine function definitions that are wrong or did not come with C++ type hints.
# WARNING: mypy.stubdoc._TYPE_RE must be updated the pattern below to accept
#  Tuple subscripts, literals, and modern | characters.
#  Note that even in mypy 1.15, this pattern does not support | characters.
#   _TYPE_RE: Final = re.compile(r"^[a-zA-Z_][\w\[\], .\"\'|]*(\.[a-zA-Z_][\w\[\], ]*)*$")
# FIXME: The Callables provided to the callback system for most classes take
#  different argument types and numbers of arguments according to the event type associated
#  with the callback.  To avoid an overload nightmare and to avoid fully articulating code
#  that is likely to be out of date at some stage, I'm going to leave them as `Callable`
#  with no subscript annotation.
EXPLICIT_DEFINITIONS = {
    None: {
        # signatures for these special methods include many inaccurate overloads
        "__ne__": "(self, other: object) -> bool",
        "__eq__": "(self, other: object) -> bool",
        "__lt__": "(self, other: object) -> bool",
        "__le__": "(self, other: object) -> bool",
        "__gt__": "(self, other: object) -> bool",
        "__ge__": "(self, other: object) -> bool",
    },
    "__hou__": {
        "addAnimationLayer": "(layermixer: ChopNode, layername: str = '') -> ChopNode",
        "applicationVersion": "(include_patch: bool = False) -> Tuple[int, int, int]",
        "addContextOptionChangeCallback": "(callback: Callable[[str], None]) -> None",
        "removeContextOptionChangeCallback": "(callback: Callable[[str], None]) -> None",
        "contextOptionChangeCallbacks": "() -> Tuple[Callable[[str], None], ...]",
        "ch": "(path: str) -> ParmArgType",
        "contextOption": "(opt: str) -> float | str",
        "createAnimationClip": "(path: str = ..., set_export: bool = False) -> ChopNode",
        "createAnimationLayers": "(path: str = ...) -> ChopNode",
        "evalParm": "(path: str) -> ParmReturnType",
        "evalParmTuple": "(path: str) -> ParmTupleReturnType",
        "fileReferences": "(project_dir_variable: str = 'HIP', include_all_refs: bool = true) -> Sequence[Tuple[Parm, str]]",
        "hscriptExpression": "(expression: str) -> float | str | Tuple[float, ...] | Tuple[str, ...]",
        "loadCPIODataFromString": "(data: bytes) -> Tuple[Tuple[str, bytes], ...]",
        "loadIndexDataFromString": "(data: bytes) -> dict[str, bytes]",
        "loadImageDataFromFile": "(file_name: str, arg: EnumValue = ...) -> bytes",
        "lvar": "(name: str) -> float | str",
        "nodeType": "(category_or_name: NodeTypeCategory | str, internal_name: str | None = None) -> NodeType | None",
        "registerOpdefPath": "(path: str, server_name: str, port: str = '') -> None",
        "removeAnimationLayer": "(layermixer: ChopNode, layername: str, merge_down: bool = False) -> bool",
        "runCallbackAndCatchCrashes": "(callback: Callable) -> Optional[Any]",
        "runVex": "(vex_file: str, inputs: Mapping[str, OptionType | OptionSequenceType], precision: Literal['32', '64'] = '32') -> dict[str, Any]",
        "saveImageDataToFile": "(color_and_alpha_data: Sequence[float] | bytes, width: int, height: int, file_name: str) -> None",
        "setContextOption": "(option: str, value: str | float | None) -> None",
        "startHoudiniEngineDebugger": "(portOrPipeName: int | str) -> None",
    },
    "_clone_Connection": {
        "contextOptionExpression": "(self, opt: str) -> str",
    },
    "_StringMapDoubleTuple": {
        "__iter__": "(self) -> Iterator[str]",
    },
    "_ik_Skeleton": {
        "addJoint": "(self, world_transform: Matrix4 = ..., parent: _ik_Joint | None = None, rotation_weights: Vector3 = ..., translation_weights: Vector3 = ..., mass: float = 1.0, local_com: Vector3 = ...) -> _ik_Joint",
    },
    "_ik_Target": {
        "__init__": "(self, joint: _ik_Joint | None = None, goal_transform: Matrix4 = ..., joint_offset: Matrix4 = ..., target_type: EnumValue = _ik_targetType.Position, weight: float = 1.0, priority: int = 0, depth: int = -1) -> None",
    },
    "_logging_Sink": {
        "setFilterCallback": "(self, callback: Callable[[_logging_LogEntry], None]) -> None",
    },
    "AdvancedDrawable": {
        "draw": "(self, handle: Handle, params: Mapping[str, Any] | None = None) -> None",
        "setParams": "(self, params: Mapping[str, Any] | None = None) -> None",
    },
    "AgentClip": {
        "__init__": "(self, name: str, stage: pxr.Usd.Stage, prim_path: str, rig: AgentRig) -> None",
    },
    "AgentLayer": {
        "__init__": "(self, name: str, rig: AgentRig, shapelib: AgentShapeLibrary, shape_bindings: Sequence[AgentShapeBinding], source_layer: AgentLayer | None = None) -> None",
        "bindings": "(self, transform: int | None = None) -> Tuple[AgentShapeBinding, ...]",
    },
    "AgentMetadata": {
        "__init__": "(self, data: Mapping[str, Any]) -> None",
        "data": "(self) -> dict[str, Any]",
        "setData": "(self, data: Mapping[str, Any]) -> None",
        "setMetadata": "(self, item_id: str, metadata: Mapping[str, Any]) -> None",
    },
    "AgentRig": {
        "__init__": "(self, name: str, transform_names: Sequence[str], hierarchy: Sequence[int]) -> None",
    },
    "AgentShapeBinding": {
        "__init__": "(self, shape: AgentShape, deformer: AgentShapeDeformer, bounds_scale: float = 1.0) -> None",
    },
    "AgentShapeDeformer": {
        "__init__": "(self, name: str | EnumValue) -> None",
    },
    "AgentShapeLibrary": {
        "__init__": "(self, filename: str, keep_external_ref: bool = True) -> None",
    },
    "AgentTransformGroup": {
        "__init__": "(self, name: str, transforms: Sequence[int], rig: AgentRig, weights: Sequence[float], channels: Sequence[int]) -> None",
    },
    "AssetGalleryDataSource": {
        "addItem": "(self, label: str, file_path: str | None = None, thumbnail: bytes = b'', type_name: str = 'asset', blind_data: bytes = b'', creation_date: int = 0) -> str",
    },
    "Attrib": {
        "defaultValue": "(self) -> AttribReturnType",
        "dicts": "Tuple[dict[str, AttribBasicType], ...]",
        "option": "(self, option_name: str) -> OptionMultiReturnType",
        "options": "(self) -> dict[str, OptionMultiReturnType]",
        "setOption": "(self, name: str, value: OptionMultiArgType, type_hint: EnumValue = ...) -> None",
    },
    "Bookmark": {
        "metadata": "(self, key: str, default_value: Any = None) -> Any",
        "setEndFrame": "(self, end: float) -> None",
        "setMetadata": "(self, key: str, value: Any, type_hint: EnumValue = ...) -> None",
        "setStartFrame": "(self, start: float) -> None",
    },
    "BoundingBox": {
        "__init__": "(self, bbox_or_xmin: float | BoundingBox = 0.0, ymin: float = 0.0, zmin: float = 0.0, xmax: float = 0.0, ymax: float = 0.0, zmax: float = 0.0) -> None",
        "enlargeToContain": "(self, point_or_bbox: Sequence[float] | Vector3, BoundingBox) -> None",
    },
    "BoundingRect": {
        "__init__": "(self, brect_or_p1_or_xmin: BoundingRect | Vector2 | float, p2_or_ymin: Vector2 | float, xmax: float = 0.0, ymax: float = 0.0) -> None",
        "enlargeToContain": "(self, point_or_rect: Sequence[float] | Vector2 | BoundingRect) -> None",
        "intersects": "(self, rect: BoundingRect) -> bool",
        "contains": "(self, rect: BoundingRect) -> bool",
    },
    "ButtonParmTemplate": {
        "__init__": "(self, name: str, label: str, disable_when: str | None = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: str=..., script_callback: str | None = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Mapping[str, str] = ...) -> None",
    },
    "ChannelGraph": {
        "selectedKeyframes": "(self) -> dict[Parm, Tuple[BaseKeyframe, ...]]",
    },
    "ChannelGraphSelection": {
        "__init__": "(self, path: str | None = None, flags: Sequence[int] = ...) -> None",
    },
    "ChannelList": {
        "addGeometryChannels": "(self, geometry: Geometry, collection_name: str | None = None, pattern: str | None = None, selected: bool = True, pinned: bool = False, valueselected: bool = False) -> str",
        "addNodeGeometryChannels": "(self, node: SopNode, pattern: str | None = None, selected: bool = True, pinned: bool = False, valueselected: bool = False) -> str",
        "asCode": "(self, var_name: str = 'chanlist') -> str",
        "containsGeometryChannel": "(self, collection_name: str, channel: str | None = None) -> bool",
        "deselect": "(self, parm: Parm | Sequence[Parm]) -> None",
        "deselectGeometryChannel": "(self, collection_name: str, channel: str | None = None) -> str",
        "deselectGeometryChannelValue": "(self, collection_name: str, channel: str | None = None) -> str",
        "deselectValue": "(self, parm: Parm | Sequence[Parm]) -> None",
        "pin": "(self, parm: Parm | Sequence[Parm]) -> None",
        "pinGeometryChannel": "(self, collection_name: str, channel: str | None = None) -> str",
        "remove": "(self, parm: Parm | Sequence[Parm]) -> None",
        "select": "(self, parm: Parm | Sequence[Parm]) -> None",
        "selectGeometryChannel": "(self, collection_name: str, channel: str | None = None) -> str",
        "selectGeometryChannelValue": "(self, collection_name: str, channel: str | None = None) -> str",
        "selectValue": "(self, parm: Parm | Sequence[Parm]) -> None",
        "unpin": "(self, parm: Parm | Sequence[Parm]) -> None",
        "unpinGeometryChannel": "(self, collection_name: str, channel: str | None = None) -> str",
    },
    "ChopNode": {
        "clipData": "(self, binary: Any) -> bytes",
        "saveClip": "(self, file_name: str) -> bool",
    },
    "Color": {
        "__init__": "(self, rgb_tuple: Sequence[float] | float = ..., g: float = ..., b: float = ...) -> None",
    },
    "CompositorViewer": {
        "bindViewerHandle": "(self, handle_type: str, name: str, settings: str | None = None, cache_previous_parms: bool = ..., handle_parms: Sequence[str] | None = None) -> None",
        "bindViewerHandleStatic": "(self, handle_type: str, name: str, bindings: Sequence[tuple[str, str]], settings: str | None = None) -> None",
    },
    "Cop2Node": {
        "allPixels": "(self, plane: str = 'C', component: str | None = None, interleaved: bool = True, time: float = -1.0) -> Tuple[float, ...]",
        "allPixelsAsString": "(self, plane: str = 'C', component: str | None = None, interleaved: bool = True, time: float = -1.0) -> bytes",
        "imageBounds": "(self, plane: str = 'C') -> Tuple[int, int, int]",
        "saveImage": "saveImage(self, file_name: str, frame_range: Sequence[float] = ...) -> None",
        "setPixelsOfCookingPlaneFromString": "(self, values: bytes, component: str | None = None, interleaved: bool = True, depth: EnumValue | None = None, flip_vertically: bool = False) -> None",
    },
    "DataParmTemplate": {
        "__init__": "(self, name: str, label: str, num_components: int, look: EnumValue = ..., naming_scheme: EnumValue = ..., unknown_str: str | None = None, disable_when: str | None = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: str | None = None, script_callback: str | None = None, script_callback_language: EnumValue = ..., tags: dict[str, str] = ..., unknown_dict: dict[EnumValue, str] = ..., default_expression: Sequence[str] = ..., default_expression_language: Sequence[EnumValue] = ...) -> None",
    },
    "Desktop": {
        "createFloatingPane": "(self, pane_tab_type: EnumValue, position: Sequence[float] = ..., size: Sequence[float] = ..., python_panel_interface: PythonPanelInterface | None = ..., immediate: bool = False) -> PaneTab",
        "createFloatingPaneTab": "(self, pane_tab_type: EnumValue, position: Sequence[float] = ..., size: Sequence[float] = ..., python_panel_interface: PythonPanelInterface | None = ..., immediate: bool = False) -> PaneTab",
        "createFloatingPanel": "(self, pane_tab_type: EnumValue, position: Sequence[float] = ..., size: Sequence[float] = ..., python_panel_interface: PythonPanelInterface | None = ..., immediate: bool = False) -> FloatingPanel",
    },
    "Dialog": {
        "addCallback": "(self, name: str, callback: Callable[[], None]) -> None",
        "callbacks": "(self, name: str) -> Tuple[Callable[[], None], ...]",
        "removeCallback": "(self, name: str, callback: Callable[[], None]) -> None",
        "setValue": "(self, name: str, value: OptionType) -> None",
        "value": "(self, name: str) -> OptionType",
        "waitForValueToChangeTo": "(self, name: str, new_value: OptionType) -> None",
    },
    "DopData": {
        "createSubData": "(self, data_name: str, data_type: str = ..., avoid_name_collisions: bool = False) -> DopData",
    },
    "DopRecord": {
        "setField": "(self, field_name: str, value: OptionType) -> None",
        "field": "(self, field_name: str) -> OptionType",
    },
    "Drawable": {
        "draw": "(self, handle: Handle, params: dict[str, Any] | None = None) -> None",
    },
    "Drawable2D": {
        "__init__": "(self, scene_viewer: SceneViewer | CompositorViewer, type: EnumValue, name: str, label: str | None = None, pickable: bool = False, params: dict[str, Any] | None = None) -> None",
        "draw": "(self, handle: Handle, params: dict[str, Any] | None = None) -> None",
        "params": "(self) -> dict[str, Any]",
        "setParams": "(self, params: dict[str, Any]) -> None",
    },
    "EdgeGroup": {
        "add": "(self, edge_or_list_or_edge_group: Edge | Sequence[Edge] | EdgeGroup) -> None",
        "iterEdges": "(self) -> _EdgeTupleGenerator",
        "remove": "(self, edge_or_list_or_edge_group: Edge | Sequence[Edge] | EdgeGroup) -> None",
    },
    "Face": {
        "attribValueAt": "(self, attrib_or_name: Attrib | str, u: float, du: float = 0) -> int | float | str | Tuple[int, ...] | Tuple[float, ...]"
    },
    "FlipbookSettings": {
        # FIXME: Most of these methods are both setters and getters, where it will set the value if
        #  one is provided and return None, or will return the current value if none is provided.
        #  We would have better results if we overloaded each of these.
        "LUT": "(self, value: str | None = None) -> str | None",
        "antialias": "(self, value: EnumValue | None = None) -> EnumValue | None",
        "aperture": "(self, value: float | None = None) -> float | None",
        "appendFramesToCurrent": "(self, value: bool | None = None) -> bool | None",
        "audioFilename": "(self, audio_file: str | None = None) -> str | None",
        "audioFrameStart": "(self, audio_file: float | None = None) -> float | None",
        "audioTimeOffset": "(self, value: float | None = None) -> float | None",
        "backgroundImage": "(self, value: str | None = None) -> str | None",
        "beautyPassOnly": "(self, value: bool | None = None) -> bool | None",
        "blockEditing": "(self, value: bool | None = None) -> bool | None",
        "cropOutMaskOverlay": "(self, value: bool | None = None) -> bool | None",
        "depthOfFieldFromCamera": "(self, value: bool | None = None) -> bool | None",
        "depthOfFieldQuality": "(self, value: float | None = None) -> float | None",
        "fStop": "(self, value: float | None = None) -> float | None",
        "focusDistance": "(self, value: float | None = None) -> float | None",
        "frameIncrement": "(self, value: float | None = None) -> float | None",
        "frameRange": "(self, value: Sequence[float] | None = None) -> Tuple[float, float] | None",
        "fromAudioPanel": "(self, value: bool | None = None) -> bool | None",
        "gamma": "(self, value: float | None = None) -> float | None",
        "initializeSimulations": "(self, value: bool | None = None) -> bool | None",
        "leaveFrameAtEnd": "(self, value: bool | None = None) -> bool | None",
        "motionBlurFrameRange": "(self, value: EnumValue | None = None) -> EnumValue | None",
        "motionBlurSegments": "(self, value: int | None = None) -> int | None",
        "output": "(self, value: str | None = None) -> str | None",
        "outputToMPlay": "(self, value: bool | None = None) -> bool | None",
        "outputZoom": "(self, value: int | None = None) -> int | None",
        "overrideGamma": "(self, value: bool | None = None) -> bool | None",
        "overrideLUT": "(self, value: bool | None = None) -> bool | None",
        "renderAllViewports": "(self, value: bool | None = None) -> bool | None",
        "resolution": "(self, value: Tuple[int, int] | None = None) -> Tuple[int, int] | None",
        "scopeChannelKeyframesOnly": "(self, value: bool | None = None) -> bool | None",
        "sessionLabel": "(self, value: str | None = None) -> str | None",
        "sheetSize": "(self, value: Sequence[int] | None = None) -> Tuple[int, int] | None",
        "shutter": "(self, value: float | None = None) -> float | None",
        "shutterFromCamera": "(self, value: bool | None = None) -> bool | None",
        "useDepthOfField": "(self, value: bool | None = None) -> bool | None",
        "useMotionBlur": "(self, value: bool | None = None) -> bool | None",
        "useResolution": "(self, value: bool | None = None) -> bool | None",
        "useSheetSize": "(self, value: bool | None = None) -> bool | None",
        "visibleObjects": "(self, value: str | None = None) -> str | None",
        "visibleTypes": "(self, value: EnumValue | None = None) -> EnumValue | None",
    },
    "FloatParmTemplate": {
        "__init__": "(self, name: str, label: str, num_components: int, default_value: Sequence[float] = ..., min: float = 0.0, max: float = 10.0, min_is_strict: bool = False, max_is_strict: bool = False, look: EnumValue = parmLook.Regular, naming_scheme: EnumValue = parmNamingScheme.XYZW, disable_when: str | None = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: str | None = None, script_callback: str | None = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Mapping[str, str] = ..., default_expression: Sequence[str] = ..., default_expression_language: Sequence[EnumValue] = ...) -> None",
    },
    "FolderParmTemplate": {
        "__init__": "(self, name: str, label: str, parm_templates: Sequence[ParmTemplate] = ..., folder_type: EnumValue = folderType.Tabs, is_hidden: bool = False, ends_tab_group: bool = False, tags: Mapping[str, str] = ..., conditionals: Mapping[EnumValue, str] = ..., tab_conditionals: Mapping[EnumValue, str] = ...) -> None",
    },
    "FolderSetParmTemplate": {
        "__init__": "(self, name: str, folder_names: Sequence[str], folder_type: EnumValue, tags: Mapping[str, str] = ...) -> None",
        "folderNames": "(self) -> list[str]",
        "setFolderNames": "(self, folder_names: Sequence[str]) -> None",
    },
    "Geometry": {
        "addAttrib": "(self, type: EnumValue, name: str, default_value: AttribArgType | AttribDictArgType, transform_as_normal: bool = True, create_local_variable: bool = True) -> Attrib",
        "attribValue": "(self, name_or_attrib: str | Attrib) -> AttribReturnType | AttribDictReturnType",
        "containsPrimType": "(self, type_or_name: EnumValue | str) -> bool",
        "countPrimType": "(self, type_or_name: EnumValue | str) -> int",
        "createPoints": "(self, point_positions: Sequence[Sequence[float]]) -> Tuple[Point, ...]",
        "createPolygons": "(self, point_positions: Sequence[Point | Sequence[int]], is_closed: bool = True) -> Tuple[Polygon, ...]",
        "deletePoints": "(self, points: Iterable[Point] | PointGroup) -> None",
        "deletePrims": "(self, prims: Sequence[Prim] | PrimGroup, keep_points: bool = False) -> None",
        "dictAttribValue": "(self, attrib: Attrib | str) -> AttribDictReturnType",
        "dictListAttribValue": "(self, name_or_attrib: Attrib | str) -> Sequence[AttribDictReturnType]",
        "edgeGroups": "(self, scope: EnumValue = groupScope.Public) -> Tuple[EdgeGroup, ...]",
        "edgeLoop": "(self, edges: Sequence[Edge], loop_type: EnumValue, full_loop_per_edge: bool, force_ring: bool, allow_ring: bool) -> Tuple[Edge, ...]",
        "findEdgeGroup": "(self, name: str, scope: EnumValue = groupScope.Public) -> EdgeGroup | None",
        "findGlobalAttrib": "(self, name: str, scope: EnumValue = attribScope.Public) -> Attrib | None",
        "findPointAttrib": "(self, name: str, scope: EnumValue = attribScope.Public) -> Attrib | None",
        "findPointGroup": "(self, name: str, scope: EnumValue = groupScope.Public) -> PointGroup | None",
        "findPrimAttrib": "(self, name: str, scope: EnumValue = attribScope.Public) -> Attrib | None",
        "findPrimGroup": "(self, name: str, scope: EnumValue = groupScope.Public) -> PrimGroup | None",
        "findVertexAttrib": "(self, name: str, scope: EnumValue = attribScope.Public) -> Attrib | None",
        "findVertexGroup": "(self, name: str, scope: EnumValue = groupScope.Public) -> VertexGroup | None",
        "floatAttribValue": "(self, name_or_attrib: str | Attrib) -> float",
        "floatListAttribValue": "(self, name_or_attrib: str | Attrib) -> Tuple[float, ...]",
        "generateAttribMenu": "(self, attrib_type: EnumValue | None = None, data_type: EnumValue | None = None, min_size: int = 1, max_size: int = -1, array_type: bool = True, scalar_type: bool = True, case_sensitive: bool = True, pattern: str = '*', decode_tokens: bool = False) -> Tuple[str, ...]",
        "importLop": "(self, lopnode: LopNode, selectionrule: LopSelectionRule, purpose: str | None = None, traversal: str | None = None, path_attrib_name: str | None = None, name_attrib_name: str | None = None, strip_layers: bool = False, frame: float | None = None) -> LopLockedStage",
        "importUsdStage": "(self, stage: pxr.Usd.Stage, selectionrule: LopSelectionRule, purpose: str | None = None, traversal: str | None = None, path_attrib_name: str | None = None, name_attrib_name: str | None = None, frame: float | None = None) -> None",
        "intAttribValue": "(self, attrib: Attrib | str) -> int",
        "intListAttribValue": "(self, name_or_attrib: Attrib | str) -> Tuple[int, ...]",
        "intrinsicValue": "(self, intrinsic_name: str) -> AttribReturnType",
        "iterPoints": "(self) -> _PointTupleGenerator",
        "iterPrims": "(self) -> _PrimTupleGenerator",
        "packedFolderProperties": "(self, path: str) -> dict[str, bool]",
        "pointFloatAttribValuesAsString": "(self, name: str, float_type: EnumValue = numericData.Float32) -> bytes",
        "pointGroups": "(self, scope: EnumValue = groupScope.Public) -> Tuple[PointGroup, ...]",
        "pointIntAttribValuesAsString": "(self, name: str, int_type: EnumValue = numericData.Int32) -> bytes",
        "pointLoop": "(self, points: Sequence[Point], loop_type: EnumValue) -> Tuple[Point, ...]",
        "pointNormals": "(self, points: Sequence[Point] | PointGroup) -> Sequence[Vector3]",
        "primFloatAttribValuesAsString": "(self, name: str, float_type: EnumValue = numericData.Float32) -> bytes",
        "primGroups": "(self, scope: EnumValue = groupScope.Public) -> Tuple[PrimGroup, ...]",
        "primIntAttribValuesAsString": "(self, name: str, int_type: EnumValue = numericData.Int32) -> bytes",
        "primLoop": "(self, prims: Sequence[Prim], loop_type: EnumValue) -> Tuple[Prim, ...]",
        "setGlobalAttribValue": "(self, name_or_attrib: str | Attrib, attrib_value: AttribArgType | AttribDictArgType) -> None",
        "setIntrinsicValue": "(self, intrinsic_name: str, value: AttribArgType) -> None",
        "setPointFloatAttribValuesFromString": "(self, name: str, values: bytes, float_type: EnumValue = numericData.Float32) -> None",
        "setPointIntAttribValuesFromString": "(self, name: str, values: bytes, int_type: EnumValue = numericData.Float32) -> None",
        "setPrimFloatAttribValuesFromString": "(self, name: str, values: bytes, float_type: EnumValue = numericData.Float32) -> None",
        "setPrimIntAttribValuesFromString": "(self, name: str, values: bytes, int_type: EnumValue = numericData.Float32) -> None",
        "setVertexFloatAttribValuesFromString": "(self, name: str, values: bytes, float_type: EnumValue = numericData.Float32) -> None",
        "setVertexIntAttribValuesFromString": "(self, name: str, values: bytes, int_type: EnumValue = numericData.Float32) -> None",
        "stringAttribValue": "(self, attrib: Attrib | str) -> str",
        "stringListAttribValue": "(self, name_or_attrib: Attrib | str) -> Tuple[str, ...]",
        "transformPrims": "(self, prims: Sequence[Prim] | PrimGroup, matrix: Matrix4) -> None",
        "vertexFloatAttribValuesAsString": "(self, name: str, float_type: EnumValue = numericData.Float32) -> bytes",
        "vertexGroups": "(self, scope: EnumValue = groupScope.Public) -> Tuple[VertexGroup, ...]",
        "vertexIntAttribValuesAsString": "(self, name: str, int_type: EnumValue = numericData.Int32) -> bytes",
    },
    "GeometryDelta": {
        "setPointPositionsFromString": "(self, positions: bytes, float_type: EnumValue = numericData.Float32) -> None",
    },
    "GeometryDrawable": {
        "__init__": "(self, scene_viewer: SceneViewer, geo_type: EnumValue, name: str, label: str | None = None, geometry: Geometry | None = None, params: Mapping[str, Any] | None = None) -> None",
    },
    "GeometryDrawableGroup": {
        "__init__": "(self, name: str, label: str | None = None) -> None",
    },
    "GeometrySelection": {
        "__init__": "(self) -> None",
    },
    "GeometryViewport": {
        "addEventCallback": "(self, callback: Callable[[dict[str, Any]], None]) -> None",
        "changeType": "(self, type: EnumValue) -> None",
        "eventCallbacks": "(self) -> Tuple[Callable[[dict[str, Any]], None], ...]",
        "queryWorldPositionAndNormal": "(self, x: int, y: int, selectionRestriction: bool = False) -> Tuple[Vector3, Vector3, bool]",
        "removeEventCallback": "(self, callback: Callable[[dict[str, Any]], None]) -> None",
        "setCamera": "(self, camera_node: ObjNode) -> None",
    },
    "GeometryViewportSettings": {
        "allowParticleSprites": "(self) -> bool",
        "autoGenerateVertexNormals": "(self) -> bool",
        "closureSelection": "(self, arg: EnumValue) -> EnumValue",
        "geometryInfo": "(self, arg: EnumValue) -> EnumValue",
        "guideFontSize": "(self) -> EnumValue",
        "handleHighlight": "(self, arg: EnumValue) -> EnumValue",
        "instanceStandInGeometry": "(self) -> EnumValue",
        "interiorWireAlpha": "(self) -> float",
        "levelOfDetail": "(self) -> float",
        "orientDiscToNormal": "(self) -> bool",
        "particleDiscSize": "(self) -> float",
        "particleDisplayType": "(self) -> EnumValue",
        "particlePointSize": "(self) -> float",
        "pointInstancing": "(self) -> bool",
        "pointInstancingLimit": "(self) -> int",
        "pointInstancingPercent": "(self) -> float",
        "polygonConvexQuality": "(self) -> bool",
        "selectWireframeAsSolid": "(self) -> bool",
        "setCamera": "(self, camera_node: ObjNode) -> None",
        "shadeOpenCurves": "(self) -> bool",
        "spriteTextureLimit": "(self) -> Tuple[int, ...]",
        "subdivsionLimit": "(self) -> int",
        "vertexNormalCuspAngle": "(self) -> float",
        "vertexNormalLimit": "(self) -> int",
        "volumeAmbientShadows": "(self) -> float",
        "volumeBSplines": "(self) -> EnumValue",
        "volumeQuality": "(self) -> EnumValue",
        "volumeWireAsPoints": "(self) -> bool",
        "wireBlend": "(self) -> float",
        "wireWidth": "(self) -> float",
    },
    "Handle": {
        "disableParms": "(self, parm_names: Sequence[str]) -> None",
        "enableParms": "(self, parm_names: Sequence[str]) -> None",
    },
    "HDADefinition": {
        "addSection": "(self, name: str, contents: str = '', compression_type: EnumValue = compressionType.NoCompression) -> HDASection",
        "extraFileOptions": "(self) -> dict[str, OptionType]",
        "setExtraFileOption": "(self, name, value: OptionType, type_hint: EnumValue = fieldType.NoSuchField) -> None",
    },
    "HDASection": {
        "binaryContents": "(self, compressionType: EnumValue = compressionType.NoCompression) -> bytes",
        "contents": "(self, compressionType: EnumValue = compressionType.NoCompression) -> str",
        "setContents": "(self, contents: str, compressionType: EnumValue = compressionType.NoCompression) -> None",
    },
    "InterruptableOperation": {
        "__exit__": "(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None",
    },
    "IntParmTemplate": {
        "__init__": "(self, name: str, label: str, num_components: int, default_value: Sequence[int] = ..., min: int = 0, max: int = 10, min_is_strict=False, max_is_strict: bool = False, look: EnumValue = parmLook.Regular, naming_scheme: EnumValue = parmNamingScheme.XYZW, menu_items: Sequence[str] = ..., menu_labels: Sequence[str] = ..., icon_names: Sequence[str] = ..., item_generator_script: str | None = None, item_generator_script_language: EnumValue | None = None, menu_type: EnumValue = menuType.Normal, disable_when: str | None = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: str | None = None, script_callback: str | None = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Mapping[str, str] = ..., default_expression: Sequence[str] = ..., default_expression_language: Sequence[str] = ...) -> None",
    },
    "IPRViewer": {
        "saveFrame": "(self, file_path: str, snapshot: int = 0, xres: int = -1, yres: int = -1, color: str = 'C', alpha: str = 'C', scope: str = '*', lut: str = '', gamma: float = 1.0, convert: bool = True) -> bool",
    },
    "Keyframe": {
        "__init__": "(self, value: float | None = None, time: float | None = None) -> None",
    },
    "LabelParmTemplate": {
        "__init__": "(self, name: str, label: str, column_labels: Sequence[str] = ..., is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: str | None = None, tags: Mapping[str, str] = ...) -> None",
    },
    "LopNetwork": {
        "activeLayer": "(self, output_index: int = ..., ignore_errors: bool = ..., use_last_cook_context_options: bool = ..., frame: float|None = ..., context_options: Mapping[str, str | float] = ...) -> pxr.Sdf.Layer",
        "postLayer": "(self, name: str) -> pxr.Sdf.Layer | None",
        "sourceLayer": "(self, layer_index: int = ..., output_index: int = ..., use_last_cook_context_options: bool = ..., frame: float|None = ..., context_options: Mapping[str, str | float] = ...) -> pxr.Sdf.Layer",
        "stage": "(self, output_index: int = ..., apply_viewport_overrides: bool = ..., ignore_errors: bool = ..., use_last_cook_context_options: bool = ..., apply_post_layers: bool = ..., frame: float|None = ..., context_options: Mapping[str, str | float] = ...) -> pxr.Usd.Stage",
        "viewportOverridesLayer": "(self, layer_id: EnumValue) -> pxr.Sdf.Layer",
    },
    "LopNode": {
        "activeLayer": "(self, output_index: int = 0, ignore_errors: bool = False, use_last_cook_context_options: bool = True, frame: float | None = None, context_options: Mapping[str, Any] = ...) -> pxr.Sdf.Layer",
        "addLockedGeometry": "(self, identifier: str, geo: Geometry, args: Mapping[str, str] | None = None) -> str",
        "displayNode": "(self) -> LopNode",
        "layersAboveLayerBreak": "(self, output_index: int = 0, use_last_cook_context_options: bool = True, frame: float | None = None, context_options: Mapping[str, str | float] | None = None) -> Tuple[str, ...]",
        "loadMasks": "(self, output_index: int = 0, force_cook: bool = False, use_last_cook_context_options: bool = True, frame: float | None = None, context_options: Mapping[str, str | float] | None = None) -> LopViewportLoadMasks",
        "setLastModifiedPrims": "(self, primPaths: Sequence[str]) -> None",
        "sourceLayer": "(self, layer_index: int = 0, output_index: int = 0, use_last_cook_context_options: bool = True, frame: float | None = None, context_options: Mapping[str, Any] = ...) -> pxr.Sdf.Layer",
        "sourceLayerCount": "(self, output_index: int = 0, use_last_cook_context_options: bool = True, frame: float | None = None, context_options: Mapping[str, str | float] | None = None) -> LopViewportLoadMasks",
        "stage": "(self, output_index: int = 0, apply_viewport_overrides: bool = False, ignore_errors: bool = False, use_last_cook_context_options: bool = True, apply_post_layers: bool = True, frame: float | None = None, context_options: Mapping[str, Any] = ...) -> pxr.Usd.Stage",
        "stagePrimStats": "(self, primpath: str | None = None, output_index: int = 0, apply_viewport_overrides: bool = False, ignore_errors: bool = False, do_geometry_counts: bool = False, do_separate_purposes: bool = False, use_last_cook_context_options: bool = True, apply_post_layers: bool = True, frame: float | None = None, context_options: Mapping[str, str | float] | None = None) -> dict[str, int]",
    },
    "LopPostLayer": {
        "__exit__": "(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None",
        "layer": "(self) -> pxr.Sdf.Layer",
        "stage": "(self) -> pxr.Usd.Stage",
    },
    "LopSelectionRule": {
        "collectionAwarePaths": "(self, lopnode: LopNode | None = None, fallback_to_new_paths: bool = False, stage: pxr.Usd.Stage | None = None, use_last_cook_context_options: bool = True) -> Tuple[pxr.Sdf.Path, ...]",
        "expandedPaths": "(self, lopnode: LopNode | None = None, return_ancestors: bool = False, fallback_to_new_paths: bool = False, stage: pxr.Usd.Stage | None = None, use_last_cook_context_options: bool = True) -> Tuple[pxr.Sdf.Path, ...]",
        "firstPath": "(self, lopnode: LopNode | None = None, return_ancestors: bool = False, fallback_to_new_paths: bool = False, stage: pxr.Usd.Stage | None = None, use_last_cook_context_options: bool = True) -> pxr.Sdf.Path",
        "newPaths": "(self, lopnode: LopNode | None = None, stage: pxr.Usd.Stage | None = None, use_last_cook_context_options: bool = True) -> Tuple[pxr.Sdf.Path, ...]",
    },
    "LopViewportOverrides": {
        "__exit__": "(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None",
        "layer": "(self) -> pxr.Sdf.Layer",
        "soloGeometry": "(self) -> pxr.Sdf.Path",
        "soloLights": "(self) -> pxr.Sdf.Path",
        "stage": "(self) -> pxr.Usd.Stage",
    },
    "Matrix2": {
        "__init__": "(self, values: int | float | Sequence[int] | Sequence[float] | Sequence[Sequence[int] | Sequence[float]] | 'Matrix2' = 0) -> None",
        "__mul__": "(self, matrix2_or_scalar: Matrix2 | float) -> Matrix2",
        "setTo": "(self, value: Sequence[float]) -> None",
    },
    "Matrix3": {
        "__init__": "(self, values: int | float | Sequence[int] | Sequence[float] | Sequence[Sequence[int] | Sequence[float]] | 'Matrix3' = 0) -> None",
        "__mul__": "(self, matrix3_or_scalar: Matrix3 | float) -> Matrix4",
        "setTo": "(self, value: Sequence[float]) -> None",
        "removeScalesAndShears": "(self, transform_order: Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs'] = 'srt') -> Tuple[Vector3, Vector3]",
        "extractRotates": "(self, rotate_order: Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'] = 'xyz') -> Vector3",
    },
    "Matrix4": {
        "__init__": "(self, values: int | float | Sequence[int] | Sequence[float] | Sequence[Sequence[int] | Sequence[float]] | 'Matrix4' = 0) -> None",
        "__mul__": "(self, matrix4_or_scalar: Matrix4 | float) -> Matrix4",
        "explode": "(self, transform_order: Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs'] = 'srt', rotate_order: Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'] = 'xyz', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> dict[str, Vector3]",
        "extractRotates": "(self, transform_order: Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs'] = 'srt', rotate_order: Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'] = 'xyz', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> Vector3",
        "extractScales": "(self, transform_order: Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs'] = 'srt', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> Vector3",
        "extractShears": "(self, transform_order: Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs'] = 'srt', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> Vector3",
        "extractTranslates": "(self, transform_order: Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs'] = 'srt', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> Vector3",
        "setTo": "(self, value: Sequence[float]) -> None",
    },
    "MenuParmTemplate": {
        "__init__": "(self, name: str, label: str, menu_items: Sequence[str], menu_labels: Sequence[str] = ..., default_value: int = 0, icon_names: Sequence[str] = ..., item_generator_script: str = '', item_generator_script_language: EnumValue | None = None, disable_when: str | None = None, menu_type: EnumValue = menuType.Normal, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: str | None = None, script_callback: str | None = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Mapping[str, str] = ..., default_expression: str = '', default_expression_language: EnumValue = scriptLanguage.Hscript, store_default_value_as_string: bool = False, menu_use_token: bool = False, is_button_strip: bool = False, strip_uses_icons: bool = False) -> None",
        "setDefaultExpressionLanguage": "(self, default_expression_language: EnumValue) -> None",
    },
    "NetworkAnimValue": {
        # FIXME: The value_start and value_end types must be the same, so some overloads are
        #  in order to make this type annotation correct.
        "__init__": "(self, duration: float | Vector2 | Vector3 | Vector4 | NetworkAnimValue, value_start: float | Vector2 | Vector3 | Vector4 = ..., value_end: float | Vector2 | Vector3 | Vector4 = ...) -> None",
    },
    "NetworkEditor": {
        "flashMessage": "(self, image: str | None, message: str | None, duration: float) -> None",
        "openNodeMenu": "(self, node: Node | None = None, items: Sequence[NetworkMovableItem] | None = None) -> None",
        "openTabMenu": "(self, key: str | None = None, auto_place: bool = False, branch: bool = False, src_item: NetworkMovableItem | None = None, src_connector_index: int = -1, dest_item: NetworkMovableItem | None = None, dest_connector_index: int = -1, node_position: Vector2 | None = None, src_items: Sequence[NetworkMovableItem] | None = None, src_indexes: Sequence[int] | None = None, dest_items: Sequence[NetworkMovableItem] | None = None, dest_indexes: Sequence[int] | None = None) -> None",
        "registerPref": "(self, pref: str, value: str, _global: bool) -> None",
        "setParmFilterCriteria": "(self, mode: EnumValue) -> None",
        "setParmFilterMode": "(self, mode: EnumValue) -> None",
    },
    "NetworkFootprint": {
        "__init__": "(self, condition: EnumValue | str, color: Color, ring: int, use_minimum_size: bool) -> None",
    },
    "NetworkImage": {
        "__init__": "(self, path: str, rect: BoundingRect) -> None",
    },
    "NetworkMovableItem": {
        "move": "(self, amount: Sequence[float] | Vector2) -> None",
        "setPosition": "(self, position: Sequence[float] | Vector2) -> None",
        "shiftPosition": "(self, amount: Sequence[float] | Vector2) -> None",
    },
    "NetworkDot": {
        "setInput": "(self, input_index: int, item_to_become_input: NetworkMovableItem | None, output_index: int = 0) -> None",
    },
    "NetworkShapeConnection": {
        "__init__": "(self, input_pos: Vector2, input_dir: Vector2, output_pos: Vector2, output_dir: Vector2, color: Color = ..., alpha: float = 1.0, fade_factor: float = 0.0, smooth: bool = True, dashed: bool = False) -> None",
    },
    "NetworkShapeLine": {
        "__init__": "(self, start: Vector2, end: Vector2, color: Color = ..., alpha: float = 1.0, width: float = 1.0, screen_space: bool = True, smooth: bool = True, dashed: bool = False) -> None",
    },
    "NetworkShapeBox": {
        "__init__": "(self, rect: BoundingRect, color: Color = ..., alpha: float = 1.0, fill: bool = True, screen_space: bool = True, smooth: bool = True) -> None",
    },
    "NetworkShapeNodeShape": {
        "__init__": "(self, rect: BoundingRect, shape: str, color: Color = ..., alpha: float = 1.0, fill: bool = True, screen_space: bool = True, smooth: bool = True) -> None",
    },
    "Node": {
        "copyItemsToClipboard": "(self, items: Iterable[NetworkMovableItem]) -> None",
        "deleteItems": "(self, items: Iterable[NetworkMovableItem], disable_safety_checks: bool = False) -> None",
        "input": "(self, input_index: int) -> Self | None",
        "inputFollowingOutputs": "(self, input_index: int) -> Self | None",
        "inputs": "(self) -> Tuple[Self | None, ...]",
        "layoutChildren": "(self, items: Sequence[NetworkMovableItem] = ..., horizontal_spacing: float = 1.0, vertical_spacing: float = 1.0) -> None",
        "outputs": "(self) -> Tuple[Self, ...]",
        "recursiveGlob": "(self, pattern: str, filter: EnumValue = nodeTypeFilter.NoFilter, include_subnets: bool = True) -> Tuple[Node, ...]",
        "setFirstInput": "(self, item_to_become_input: NetworkMovableItem | None, output_index: int = 0) -> None",
        "setInput": "(self, input_index: int, item_to_become_input: NetworkMovableItem | None, output_index: int = 0) -> None",
        "setNamedInput": "(self, input_name: str, item_to_become_input: NetworkMovableItem, output_name_or_index: str | int) -> None",
        "userData": "(self, name: str) -> str | None",
    },
    "NodeInfoTree": {
        "__init__": "(self, tree_root: Any, tree: Any) -> None",
    },
    "ObjNode": {
        "material": "(self, operation: Literal['override', 'select', 'remove', 'rmdefault', 'sync', 'revert', 'addlist'], parameter: Sequence[str] | None = None) -> None",
    },
    "OpNode": {
        "addError": "(self, message: str, severity: EnumValue = ...) -> None",
        "addEventCallback": "(self, event_types: Sequence[EnumValue], callback: Callable) -> None",
        "addParmCallback": "(self, callback: Callable[[OpNode, ParmTuple], None], names: Sequence[str]) -> None",
        "cook": "(self, force: bool = False, frame_range: Sequence[float] = ...) -> None",
        "cookCodeGeneratorNode": "(self, check_parent: bool = False) -> Node",
        "evalParm": "(self, parm_path: str) -> ParmArgType",
        "evalParmTuple": "(self, parm_path: str) -> ParmTupleReturnType",
        "eventCallbacks": "(self) -> Tuple[Tuple[Tuple[EnumValue, ...], Callable], ...]",
        "fileReferences": "(self, recurse: bool = True, project_dir_variable: str = 'HIP', include_all_refs: bool = True) -> Sequence[Tuple[Parm, str]]",
        "lastCookContextOptions": "(self, only_used_options: bool = False) -> dict[str, str | float]",
        "needsToCook": "(self, time: float = ...) -> bool",
        "removeEventCallback": "(self, event_types: Sequence[EnumValue], callback: Callable) -> None",
        "setDeleteScript": "(self, script_text: str, language: EnumValue = ...) -> None",
        "setInput": "(self, input_index: int, item_to_become_input: NetworkMovableItem | None, output_index: int = 0) -> None",
        "stampValue": "(self, parm_name: str, default_value: float | str) -> str",
    },
    "OpNodeType": {
        "deprecationInfo": "(self) -> dict[str, str | Self]",
    },
    "OperationFailed": {
        "__init__": "(self, message: str | None = ...) -> None",
    },
    "OrientedBoundingBox": {
        "__init__": "(self, oriented_bbox: OrientedBoundingBox = ...) -> None",
    },
    "PaneTab": {
        "displayRadialMenu": "(self, menu: str | RadialScriptItem) -> None",
    },
    "ParameterEditor": {
        "setFilterCriteria": "(self, criteria: EnumValue) -> None",
        "setFilterMode": "(self, mode: EnumValue) -> None",
    },
    "Parm": {
        "eval": "(self) -> int | float | str",
        "evalAtFrame": "(self, frame: float) -> int | float | str",
        "evalAtTime": "(self, frame: float) -> int | float | str",
        "keyframesRefit": "(self, refit: bool, refit_tol: float, refit_preserve_extrema: bool, refit_bezier: bool, resample: bool, resample_rate: float, resample_tol: float, range_: bool, range_start: float, range_end: bool, bake_chop: EnumValue, refit_smooth: bool) -> None",
        "pressButton": "(self, arguments: Mapping[str, int | bool | float | str] = ...) -> None",
        "set": "(self, value: int | float | str | Parm | Ramp, language: EnumValue | None = None, follow_parm_reference: bool = True) -> None",
    },
    "ParmTemplate": {
        "conditionals": "(self) -> dict[EnumValue, str]",
        "setTags": "(self, tags: Mapping[str, str]) -> None",
    },
    "ParmTemplateGroup": {
        "__init__": "(self, parm_templates: Sequence[ParmTemplate] = ...) -> None",
        "appendToFolder": "(self, label_or_labels_or_parm_template_or_indices: str | Sequence[str] | ParmTemplate | Sequence[int], parm_template: ParmTemplate) -> None",
        "asDialogScript": "(self, rename_conflicting_parms: bool = False, full_info: bool = False, script_name: str | None = None, script_label: str | None = None, script_tags: Mapping[str, str] = ...) -> str",
        "containingFolder": "(self, name_or_parm_template: str | ParmTemplate) -> FolderParmTemplate",
        "containingFolderIndices": "(self, name_or_parm_template_or_indices: str | ParmTemplate | Sequence[int]) -> Tuple[int, ...]",
        "findFolder": "(self, label_or_labels: str | Sequence[str]) -> ParmTemplate | None",
        "findIndices": "(self, name_or_parm_template: ParmTemplate | str) -> Tuple[int, ...]",
        "findIndicesForFolder": "(self, name_or_parm_template: ParmTemplate | str) -> Tuple[int, ...]",
        "hide": "(self, name_or_parm_template_or_indices: str | ParmTemplate | Sequence[int], on: bool) -> None",
        "hideFolder": "(self, label_or_labels: str | Sequence[str], on: bool) -> None",
        "insertAfter": "(self, name_or_parm_template_or_indices: str | ParmTemplate | Sequence[int], parm_template: ParmTemplate) -> None",
        "insertBefore": "(self, name_or_parm_template_or_indices: str | ParmTemplate | Sequence[int], parm_template: ParmTemplate) -> None",
        "isFolderHidden": "(self, label_or_labels: str | Sequence[str]) -> bool",
        "isHidden": "(self, name_or_parm_template_or_indices: str | ParmTemplate | Sequence[int]) -> bool",
        "remove": "(self, name_or_parm_template_or_indices: str | ParmTemplate | Sequence[int]) -> None",
        "replace": "(self, name_or_parm_template_or_indices: str | ParmTemplate | Sequence[int], parm_template: ParmTemplate) -> None",
    },
    "ParmTuple": {
        "eval": "(self) -> Tuple[int, ...] | Tuple[float, ...] | Tuple[str, ...] | Ramp",
        "evalAtFrame": "(self, frame: float) -> Tuple[int, ...] | Tuple[float, ...] | Tuple[str, ...] | Ramp",
        "evalAtTime": "(self, frame: float) -> Tuple[int, ...] | Tuple[float, ...] | Tuple[str, ...] | Ramp",
        "lock": "(self, bool_values: bool | Sequence[bool]) -> None",
        "node": "(self) -> OpNode",
        "setPending": "(self, values: Sequence[float | str]) -> None",
    },
    "PerfMonEvent": {
        "__exit__": "(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None",
    },
    "PerfMonProfile": {
        "stats": "(self) -> dict[str, Any]",
    },
    "PluginHotkeyDefinitions": {
        "addDefaultBinding": "(self, context: str, command: str, assignments: Sequence[str], apply_platform_modifier_mappings: bool = True) -> None",
    },
    "Point": {
        "attribValue": "(self, attrib: Attrib | str) -> AttribReturnType | AttribDictReturnType",
        "dictAttribValue": "(self, name_or_attrib: str | Attrib) -> AttribDictReturnType",
        "dictListAttribValue": "(self, name_or_attrib: str | Attrib) -> Sequence[AttribDictReturnType]",
        "floatAttribValue": "(self, name_or_attrib: str | Attrib) -> float",
        "floatListAttribValue": "(self, name_or_attrib: str | Attrib) -> Tuple[float, ...]",
        "intAttribValue": "(self, name_or_attrib: str | Attrib) -> int",
        "intListAttribValue": "(self, name_or_attrib: str | Attrib) -> Tuple[int, ...]",
        "setAttribValue": "(self, name_or_attrib: str | Attrib, attrib_value: AttribArgType | AttribDictArgType) -> None",
        "stringAttribValue": "(self, name_or_attrib: str | Attrib) -> str",
        "stringListAttribValue": "(self, name_or_attrib: str | Attrib) -> Tuple[str, ...]",
    },
    "PointGroup": {
        "add": "(self, point_or_list_or_point_group: Point | Sequence[Point] | PointGroup) -> None",
        "iterPoints": "(self) -> _PointTupleGenerator",
        "option": "(self, option_name: str) -> OptionMultiReturnType",
        "options": "(self) -> dict[str, OptionMultiReturnType]",
        "remove": "(self, point_or_list_or_point_group: Point | Sequence[Point] | PointGroup) -> None",
        "setOption": "(self, name: str, value: OptionMultiArgType, type_hint: EnumValue = fieldType.NoSuchField) -> None",
    },
    "Prim": {
        "attribValue": "(self, attrib: Attrib | str) -> AttribReturnType | AttribDictReturnType",
        "attribValueAtInterior": "(self, attrib: Attrib | str, u: float, v: float, w: float = 0.0) -> AttribReturnType",
        "dictAttribValue": "(self, attrib: Attrib | str) -> AttribDictReturnType",
        "dictListAttribValue": "(self, name_or_attrib: Attrib | str) -> Sequence[AttribDictReturnType]",
        "floatAttribValue": "(self, attrib: Attrib | str) -> float",
        "floatListAttribValue": "(self, name_or_attrib: str | Attrib) -> Tuple[float, ...]",
        "intAttribValue": "(self, attrib: Attrib | str) -> int",
        "intListAttribValue": "(self, name_or_attrib: Attrib | str) -> Tuple[int, ...]",
        "intrinsicValue": "(self, intrinsic_name: str) -> AttribReturnType",
        "primuConvert": "(self, u: float, mode: int, tol: float | None = ...) -> float",
        "primuvConvert": "(self, uv: Sequence[float] | Vector2, mode: int, tol: float | None = ...) -> Vector2",
        "setAttribValue": "(self, name_or_attrib: Attrib | str, attrib_value: AttribArgType | AttribDictArgType) -> None",
        "setIntrinsicValue": "(self, intrinsic_name: str, value: AttribArgType) -> None",
        "stringAttribValue": "(self, attrib: Attrib | str) -> str",
        "stringListAttribValue": "(self, name_or_attrib: Attrib | str) -> Tuple[str, ...]",
        "voxelRange": "(self, range: BoundingBox) -> Tuple[bool, ...] | Tuple[int, ...] | Tuple[float, ...] | Tuple[Vector3, ...]",
    },
    "PrimGroup": {
        "add": "(self, prim_or_list_or_prim_group: Prim | Sequence[Prim] | PrimGroup) -> None",
        "iterPrims": "(self) -> _PrimTupleGenerator",
        "option": "(self, option_name: str) -> OptionMultiReturnType",
        "options": "(self) -> dict[str, OptionMultiReturnType]",
        "remove": "(self, prim_or_list_or_prim_group: Prim | Sequence[Prim] | PrimGroup) -> None",
        "setOption": "(self, name: str, value: OptionMultiArgType, type_hint: EnumValue = fieldType.NoSuchField) -> None",
    },
    "Quaternion": {
        "__init__": "(self, x: Sequence[float] | float | 'Quaternion' | Matrix3 | Matrix4, y: Sequence[float] | float, z: float = ..., w: float = ...) -> None",
        "__mul__": "(self, quaternion_or_scalar: Quaternion | float) -> Quaternion",
        "extractEulerRotates": "(self, rotate_order: Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'] = 'xyz') -> Vector3",
        "setToEulerRotates": "(self, angles_in_deg: float, rotate_order: Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'] = 'xyz') -> None",
        "setToRotationMatrix": "(self, matrix3_or_matrix4: Matrix3 | Matrix4) -> None",
    },
    "RadialScriptItem": {
        "setActionCallback": "(self, callback: Callable) -> None",
        "setCheckCallback": "(self, callback: Callable) -> None",
    },
    "Ramp": {
        "__init__": "(self, basis: Sequence[EnumValue], keys: Sequence[float], values: Sequence[float] | Sequence[Tuple[float, float, float]]) -> None",
        "lookup": "(self, pos: float) -> float | Tuple[float, float, float]",
        "values": "(self) -> Tuple[float | Tuple[float, float, float], ...]",
    },
    "RampParmTemplate": {
        "__init__": "(self, name: str, label: str, ramp_parm_type: EnumValue, default_value: int = 2, default_basis: EnumValue | None = None, show_controls: bool = True, color_type: EnumValue | None = None, disable_when: str | None = None, is_hidden: bool = False, help: str | None = None, script_callback: str | None = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Mapping[str, str] = ..., default_expression_language: EnumValue = scriptLanguage.Hscript) -> None",
    },
    "RedrawBlock": {
        "__exit__": "(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None",
    },
    "RopNode": {
        "addRenderEventCallback": "(self, callback: Callable[[RopNode, EnumValue, float], None], run_before_script: bool = False) -> None",
        "removeRenderEventCallback": "(self, callback: Callable[[RopNode, EnumValue, float], None]) -> None",
        "render": "(self, frame_range: Sequence[float] | None = None, res: Sequence[int] | None = None, output_file: str | None = None, output_format: str=..., to_flipbook: bool = False, quality: int = 2, ignore_inputs: bool = False, method=RopByRop, ignore_bypass_flags: bool = False, ignore_lock_flags: bool = False, verbose: bool = False, output_progress: bool = False) -> None",
    },
    "SceneGraphTree": {
        "collapsePrimitives": "(self, prims: Sequence[str | pxr.Sdf.Path]) -> None",
        "expandPrimitives": "(self, prims: Sequence[str | pxr.Sdf.Path], collapse_others: bool = False, expand_leaf_primitives: bool = False) -> None",
        "expandedPrimitives": "(self, include_leaf_primitives: bool = False) -> Tuple[pxr.Sdf.Path, ...]",
    },
    "SceneViewer": {
        "addEventCallback": "(self, callback: Callable) -> None",
        "bindViewerHandle": "(self, handle_type: str, name: str, settings: str | None = None, cache_previous_parms: bool = False, handle_parms: Sequence[str] | None = None) -> None",
        "bindViewerHandleStatic": "(self, handle_type: str, name: str, bindings: Sequence[str], settings: str | None = None) -> None",
        "eventCallbacks": "(self) -> Tuple[Callable, ...]",
        "groupListMask": "(self) -> str",
        "isGroupPicking": "(self) -> bool",
        "locateSceneGraphPrim": "(self, x: int, y: int) -> Tuple[float, str]",
        "qtWindow": "(self) -> QtWidgets.QWidget",
        "removeEventCallback": "(self, callback: Callable) -> None",
        "runStateCommand": "(self, name: str, args: Mapping[str, Any] | None = None) -> None",
        "selectDrawableGeometry": "(self, drawable_selection: Mapping[str, Incomplete], selection_modifier: EnumValue = pickModifier.Replace) -> None",
        "selectDynamics": "(self, prompt: str = 'Select objects', sel_index: int = 0, allow_objects: bool = True, allow_modifiers: bool = False, quick_select: bool = False, use_existing_selection: bool = True, allow_multisel: bool = True, icon: str | None = None, label: str | None = None, prior_selection_paths: Sequence[str] | None = ..., prior_selection_ids: int | None = ..., prior_selections: Sequence[str] = ..., toolbox_templategroup: str | None = None, toolbox1_templategroup: str | None = None, select_parm: str = '') -> Tuple[DopData, ...]",
        "selectDynamicsPoints": "(self, prompt: str = 'Select objects', sel_index: int = 0, quick_select: bool = False, use_existing_selection: bool = True, allow_multisel: bool = True, only_select_points: bool = True, object_based_point_selection: bool = False, use_last_selected_object: bool = False, icon: str | None = None, label: str | None = None, prior_selection_paths: Sequence[str] | None = ..., prior_selection_ids: int | None = ..., prior_selections: Sequence[str] = ..., toolbox_templategroup: str | None = None, toolbox1_templategroup: str | None = None, select_parm: str = '') -> Sequence[Tuple[DopData, GeometrySelection]]",
        "selectDynamicsPolygons": "(self, prompt: str = 'Select objects', sel_index: int = 0, quick_select: bool = False, use_existing_selection: bool = True, object_based_point_selection: bool = False, use_last_selected_object: bool = False, icon: str | None = None, label: str | None = None, prior_selection_paths: Sequence[str] | None = ..., prior_selection_ids: int | None = ..., prior_selections: Sequence[str] = ..., toolbox_templategroup: str | None = None, toolbox1_templategroup: str | None = None, select_parm: str = '') -> Sequence[Tuple[DopData, GeometrySelection]]",
        "selectGeometry": "(self, prompt: str = 'Select geometry', sel_index: int = 0, allow_drag: bool = False, quick_select: bool = False, use_existing_selection: bool = True, initial_selection: str | None = None, initial_selection_type: EnumValue | None = None, ordered: bool = False, geometry_types: Sequence[EnumValue] = ..., primitive_types: Sequence[EnumValue] = ..., allow_obj_sel: bool = True, icon: str | None = None, label: str | None = None, prior_selection_paths: list = ..., prior_selection_ids: list = ..., prior_selections: list = ..., allow_other_sops: bool = True, consume_selections: bool = True) -> GeometrySelection",
        "selectObjects": "(self, prompt: str = 'Select objects', sel_index: int = 0, allow_drag: bool = False, quick_select: bool = False, use_existing_selection: bool = True, allow_multisel: bool = True, allowed_types: Sequence[str] = ..., icon: str | None = None, label: str | None = None, prior_selection_paths: Sequence[str] | None = ..., prior_selection_ids: int | None = ..., prior_selections: Sequence[str] = ..., toolbox_templategroup: str | None = None, toolbox1_templategroup: str | None = None, select_parm: str = '') -> Tuple[Node, ...]",
        "selectOrientedPositions": "(self, prompt: str = 'Click to specify a position', number_of_positions: int = 1, min_number_of_positions: int = -1, connect_positions: bool = True, show_coordinates: bool = True, bbox: BoundingBox = ..., icon: str | None = None, label: str | None = None, toolbox_templategroup: str | None = None, toolbox1_templategroup: str | None = None, select_parm: str = '') -> Sequence[Tuple[Vector3, Matrix3]]",
        "selectPositions": "(self, prompt: str = 'Click to specify a position', number_of_positions: int = 1, min_number_of_positions: int = -1, connect_positions: bool = True, show_coordinates: bool = True, bbox: BoundingBox = ..., position_type: EnumValue = positionType.WorldSpace, icon: str | None = None, label: str | None =None, toolbox_templategroup: str | None = None, toolbox1_templategroup: str | None = None, select_parm: str ='') -> Sequence[Vector3]",
        "selectSceneGraph": "(self, prompt: str ='Select primitives', preselection: Sequence[str] = ..., prim_mask: EnumValue = scenePrimMask.ViewerSetting, quick_select: bool = False, use_existing_selection: bool = True, confirm_existing: bool = False, allow_multisel: bool = True, allow_drag: bool = True, propagate_selection: bool = True, path_prefix_mask: str = '', prim_kind: str = '', validate_selection_for_node: Incomplete = ..., select_parm: str = '', allow_kind_mismatch: EnumValue = optionalBool.NoOpinion, allow_instance_proxies: EnumValue = optionalBool.NoOpinion, fix_preselection_paths=True) -> Tuple[str, ...]",
        "selectSceneGraphInstances": "(self, prompt: str = 'Select point instances', preselection: Sequence[str] = ..., quick_select: bool = False, use_existing_selection: bool = True, confirm_existing: bool = False, allow_multisel: bool = True, allow_drag: bool = True, path_prefix_mask: str = '', instance_level: int = 0, instance_indices_only: bool = False, validate_selection_for_node: Incomplete = ..., select_parm: str = '') -> Tuple[str, ...]",
        "setCurrentState": "(self, state: EnumValue, wait_for_exit: bool = False, generate: EnumValue = stateGenerateMode.Insert, request_new_on_generate: bool = True, ex_situ_generate: bool = False) -> None",
        "setPromptMessage": "(self, msg: str, msg_type: EnumValue = promptMessageType.Prompt) -> None",
        "stage": "(self) -> pxr.Usd.Stage",
        "triggerStateSelector": "(self, action: EnumValue, name: str | None = None) -> None",
    },
    "ScriptEvalContext": {
        "__exit__": "(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None",
        "__init__": "(self, node_or_parm: OpNode | Parm) -> None",
    },
    "Selection": {
        "__init__": "(self, selection: EnumValue | Geometry | Sequence[Prim] | Sequence[Point] | Sequence[Vertex] | Sequence[Edge], geometry_type: EnumValue | Sequence[EnumValue] = ..., selection_string: str = ...) -> None",
        "numSelected": "(self) -> int",
    },
    "SeparatorParmTemplate": {
        "__init__": "(self, name: str, is_hidden: bool = False, tags: Mapping[str, str] = ...) -> None",
    },
    "Shelf": {
        "setTools": "(self, tools: Sequence[Tool]) -> None",
    },
    "ShelfElement": {
        "setFilePath": "(self, file_path: str | None) -> None",
    },
    "ShopNode": {
        "shaderCode": "(self, shader_type: EnumValue | None = None) -> str",
        "shaderString": "(self, render_type: str | None = None) -> str",
    },
    "ShellIO": {
        "CloseCallbacks": "(self) -> Tuple[Callable[[], None], ...]",
        "addCloseCallback": "(self, callback: Callable[[], None]) -> None",
        "addExitCallback": "(self, callback: Callable[[], None]) -> None",
        "closeCallbacks": "(self) -> Tuple[Callable[[], None], ...]",
        "exitCallbacks": "(self) -> Tuple[Callable[[], None], ...]",
        "readline": "(self, size: int = -1) -> str",
        "removeCloseCallback": "(self, callback: Callable[[], None]) -> None",
        "removeExitCallback": "(self, callback: Callable[[], None]) -> None",
    },
    "SimpleDrawable": {
        "__init__": "(self, scene_viewer: SceneViewer, geometry: Geometry | EnumValue, name: str) -> None",
        "setOutlineColor": "(self, color: Color | Vector4) -> None",
    },
    "SopNodeType": {
        "addSelector": "(self, name: str, selector_type: str, prompt: str = 'Select components', primitive_types: Sequence[EnumValue] = ..., group_parm_name: str | None = None, group_type_parm_name: str | None = None, input_index: int = 0, input_required: bool = True, allow_dragging: bool = False, empty_string_selects_all: bool = True) -> Selector",
        "selectors": "(self, selector_indices: Sequence[int] = ...) -> Tuple[Selector, ...]",
    },
    "OpVerb": {
        "parms": "(self) -> dict[str, OptionType]",
        "setParms": "(self, p: Mapping[str, OptionMultiArgType | Sequence[Mapping[str, OptionMultiArgType]]]) -> None",
    },
    "StickyNote": {
        "setSize": "(self, size: Sequence[float] | Vector2) -> None",
    },
    "StringKeyframe": {
        "__init__": "(self, expression: str | None = None, time: float | None = None, language: EnumValue | None = exprLanguage.Python) -> None",
    },
    "StringParmTemplate": {
        "__init__": "(self, name: str, label: str, num_components: int, default_value: Sequence[str] = ..., naming_scheme: EnumValue = parmNamingScheme.Base1, string_type: EnumValue = stringParmType.Regular, file_type: EnumValue = fileType.Any, menu_items: Sequence[str] = ..., menu_labels: Sequence[str] = ..., icon_names: Sequence[str] = ..., item_generator_script: str | None = None, item_generator_script_language: EnumValue | None = None, menu_type: EnumValue = menuType.Normal, disable_when: str | None = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: str | None = None, script_callback: str | None = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Mapping[str, str] = ..., default_expression: Sequence[str] = ..., default_expression_language: Sequence[EnumValue] = ...) -> None",
    },
    "StyleSheet": {
        "__init__": "(self, json_text: str = ...) -> None",
        "cloneWithAddedStyleSheet": "(self, stylesheet: StyleSheet, target: str | None = ...) -> StyleSheet",
    },
    "Surface": {
        "attribValueAt": "(self, attrib_or_name: Attrib | str, u: float, v: float, du: float = 0, dv: float = 0) -> int | float | str | Tuple[int, ...] | Tuple[float, ...]"
    },
    "SwigPyIterator": {
        "__sub__": "(self, n: int) -> Any",
    },
    "Take": {
        "loadChildTakeFromFile": "(self, filename: str) -> Tuple[Take, ...]",
        "name": "(self) -> str",
    },
    "TextDrawable": {
        "__init__": "(self, scene_viewer: SceneViewer, name: str, label: str | None = None, params: Mapping[str, Any] | None = None) -> None",
    },
    "ToggleParmTemplate": {
        "__init__": "(self, name: str, label: str, default_value: bool = False, disable_when: str | None =None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: str | None = None, script_callback: str | None = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Mapping[str, str] = ..., default_expression: str = '', default_expression_language: EnumValue = scriptLanguage.Hscript) -> None",
    },
    "Tool": {
        "setData": "(self, script: str = '', language: EnumValue = scriptLanguage.Python, icon: str = '', help: str = '', help_url: str = '', network_categories: Sequence[NodeTypeCategory] = ..., viewer_categories: Sequence[NodeTypeCategory] = ..., cop_viewer_categories: Sequence[NodeTypeCategory] = ..., network_op_type: str = '', viewer_op_type: str = '', locations: Sequence[str] = ...) -> None",
    },
    "TopNode": {
        "cookWorkItems": "(self, block: bool = False, generate_only: bool = False, tops_only: bool = False, save_prompt: bool = False, nodes: Sequence[TopNode] = ...) -> None",
        "generateStaticWorkItems": "(self, block: bool = False, nodes: Sequence[TopNode] = ...) -> None",
    },
    "UndosDisabler": {
        "__exit__": "(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None",
    },
    "UndosGroup": {
        "__exit__": "(self, type: type[BaseException], value: BaseException, traceback: TracebackType) -> None",
    },
    "Vector2": {
        "__init__": "(self, x: Sequence[float] | 'Vector2' | float = ..., y: float = ...) -> None",
        "__mul__": "(self, scalar_or_matrix2: float | Matrix2) -> Vector2",
    },
    "Vector3": {
        "__init__": "(self, x: Sequence[float] | 'Vector3' | float = ..., y: float = ..., z: float = ...) -> None",
        "__mul__": "(self, scalar_or_matrix3_or_matrix4: float | Matrix3 | Matrix4) -> Vector3",
        "smoothRotation": "(self, reference: Vector3, rotate_order: Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'] = 'xyz') -> Vector3",
    },
    "Vector4": {
        "__init__": "(self, x: Sequence[float] | 'Vector4' | float = ..., y: float = ..., z: float = ..., w: float = ...) -> None",
        "__mul__": "(self, scalar_or_matrix4: float | Matrix4) -> Vector4",
    },
    "Vertex": {
        "attribValue": "(self, attrib: Attrib | str) -> AttribReturnType | AttribDictReturnType",
        "dictAttribValue": "(self, name_or_attrib: str | Attrib) -> AttribDictReturnType",
        "dictListAttribValue": "(self, name_or_attrib: str | Attrib) -> Sequence[AttribDictReturnType]",
        "floatAttribValue": "(self, name_or_attrib: str | Attrib) -> float",
        "floatListAttribValue": "(self, name_or_attrib: str | Attrib) -> Tuple[float, ...]",
        "intAttribValue": "(self, name_or_attrib: str | Attrib) -> int",
        "intListAttribValue": "(self, name_or_attrib: str | Attrib) -> Tuple[int, ...]",
        "setAttribValue": "(self, name_or_attrib: str | Attrib, attrib_value: AttribArgType | AttribDictArgType) -> None",
        "stringAttribValue": "(self, name_or_attrib: str | Attrib) -> str",
        "stringListAttribValue": "(self, name_or_attrib: str | Attrib) -> Tuple[str, ...]",
    },
    "VertexGroup": {
        "add": "(self, vertex_or_list_or_vertex_group: Vertex | Sequence[Vertex] | VertexGroup) -> None",
        "iterVertices": "(self) -> _VertexTupleGenerator",
        "option": "(self, option_name: str) -> OptionMultiReturnType",
        "options": "(self) -> dict[str, OptionMultiReturnType]",
        "remove": "(self, vertex_or_list_or_vertex_group: Vertex | Sequence[Vertex] | VertexGroup) -> None",
        "setOption": "(self, name: str, value: OptionMultiArgType, type_hint: EnumValue = fieldType.NoSuchField) -> None",
    },
    "ViewerDragger": {
        "drag": "(self, event: ViewerEvent) -> dict[str, Any]",
    },
    "ViewerHandleContext": {
        "draw": "(self, handle: Handle) -> None",
        "scaleFactor": "(self, ref_position: Sequence[float] | Vector3 = ...) -> float",
    },
    "ViewerHandleTemplate": {
        "__init__": "(self, name: str, label: str, categories: Sequence[EnumValue]) -> None",
        "bindFactory": "(self, callback: Callable[[SceneViewer, str], Handle])",
        "bindGadget": "(self, drawable_type: EnumValue, gadget_name: str , gadget_label: str | None = None, parms: Sequence[str] | None = None) -> None",
        "bindParameter": "(self, param_type: EnumValue, name: str , label: str | None = None, default_value: int | float | str | None = None, num_components: int = 1, min_limit: int = 0, max_limit: int = 1, visible: bool = True) -> None",
        "bindSetting": "(self, param_type: EnumValue, name: str , label: str | None = None, menu_as_button_strip: bool = False, menu_items: Sequence[Tuple[str, str] | Tuple[str, str, str]] | None = None, num_components: int = 1, default_value: int | float | str | None = None, min_limit: int = 0, max_limit: int = 1, align: bool = False) -> None",
    },
    "ViewerState": {
        "parmTemplates": "(self) -> ParmTemplateGroup",
    },
    "ViewerStateDragger": {
        "__init__": "(self, name: str, xform: Matrix4 = ..., inv_xform: Matrix4 = ...) -> None",
    },
    "ViewerStateMenu": {
        "addActionItem": "(self, id,: str label: str, hotkey: str = '') -> None",
        "addRadioStripItem": "(self, strip_id: str, id: str label: str, hotkey: str = '') -> None",
        "addToggleItem": "(self, id,: str label: str, default: bool, hotkey: str = '') -> None",
    },
    "ViewerStateTemplate": {
        "__init__": "(self, state_name: str, state_label: str, node_type_category: NodeTypeCategory, contexts: Sequence[NodeTypeCategory] | None = None) -> None",
        "bindDrawableSelector": "(self, prompt: str, auto_start: bool = True, toolbox: bool = True, drawable_mask=[], hotkey: str = '', name: str = '') -> None",
        "bindDynamicsPointSelector": "(self, prompt: str, allow_objects: bool = True, allow_modifiers: bool = False, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, allow_multisel: bool = True, only_select_points: bool = True, object_based_point_selection: bool = False, use_last_selected_object: bool = False, hotkey: str = '', name: str = '') -> None",
        "bindDynamicsPolygonSelector": "(self, prompt: str, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, object_based_point_selection: bool = False, secure_selection: EnumValue = secureSelectionOption.Obey, use_last_selected_object: bool = False, hotkey: str = '', name: str = '') -> None",
        "bindDynamicsSelector": "(self, prompt: str, allow_objects: bool = True, allow_modifiers: bool = False, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, allow_multisel: bool = True, hotkey: str = '', name: str = '') -> None",
        "bindFactory": "(self, callback: Callable[[str, SceneViewer], Any])",
        "bindGadget": "(self, drawable_type: EnumValue, gadget_name: str, gadget_label: str | None = None) -> None",
        "bindGeometrySelector": "(self, prompt: str, allow_drag: bool = False, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, consume_selection: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, initial_selection: str = '', initial_selection_type: EnumValue = geometryType.Primitives, ordered: bool = False, geometry_types: Sequence[EnumValue] = ..., primitive_types: Sequence[EnumValue] = ..., allow_other_sops: bool = False, hotkey: str = '', name: str = '') -> None",
        "bindHandle": "(self, handle_type: str, name: str, settings: str | None = None) -> None",
        "bindHandleStatic": "(self, handle_type: str, name: str, bindings: Sequence[str] , settings: str | None = None) -> None",
        "bindObjectSelector": "(self, prompt: str, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, allow_multisel: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, allowed_types: Sequence[str] = ..., hotkey: str = '', name: str = '') -> None",
        "bindParameter": "(self, param_type: EnumValue, name: str | None = None, label: str | None = None, menu_as_button_strip: bool = False, menu_items: Sequence[Tuple[str, str] | Tuple[str, str, str]] | None = None, num_components: int = 1, default_value: ParmArgType | None=None, min_limit: int = 0, max_limit: int = 1, align: bool = False, toolbox: bool = True) -> None",
        "bindSceneGraphSelector": "(self, prompt: str, allow_drag: bool = True, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, consume_selection: bool = False, allow_multisel: bool = True, prior_selection_paths: Sequence[str] | None=..., prim_mask: str | None=..., path_prefix_mask: str | None=..., prim_kind: str | None=..., hotkey: str = '', name: str = '') -> None",
        "bindSelector": "(self, name, selector_type, prompt: str, primitive_types: Sequence[EnumValue]=..., group_parm_name: str = ..., input_index=0, input_required: bool = True, allow_dragging: bool = True) -> None",
    },
    "ViewportVisualizer": {
        "setParm": "(self, parm_name: str, value: int | float | str) -> None",
    },
    "Volume": {
        "setAllVoxelsFromString": "(self, values: bytes) -> None",
        "setVoxelSliceFromString": "(self, values: bytes, plane: str, index: int) -> None",
    },
    "VopNode": {
        "shaderCode": "(self, shader_type: EnumValue | None = None) -> str",
        "shaderString": "(self, render_type: str | None = None, shader_type: EnumValue = shaderType.Surface, as_encapsulated: bool = False) -> str",
    },
    "anim": {
        "addBookmarksChangedCallback": "(callback: Callable) -> None",
        "addGeometryChannelsChangedCallback": "(collection_name: str, callback: Callable, on_mouse_up: bool = True) -> bool",
        "getGeometryChannels": "(collection_name: str, geometry: Geometry, channel_names: Sequence[str] | None = None) -> None",
        "isGeometryChannelPinned": "(collection_name: str, channel_names: str | None = None) -> bool",
        "mergeGeometryChannels": "(collection_name: str, geometry: Geometry, channel_names: Sequence[str] | None = None) -> None",
        "newBookmark": "(name: str, start: float, end: float) -> Bookmark",
        "removeBookmarksChangedCallback": "(callback: Callable) -> None",
        "removeGeometryChannelsChangedCallback": "(collection_name: str, callback: Callable, on_mouse_up: bool = True) -> bool",
        "saveBookmarks": "(filename: str, bookmarks: Sequence[Bookmark] | None = None, include_temporary: bool = False) -> bool",
        "saveBookmarksToString": "(bookmarks: Sequence[Bookmark] | None = None, include_temporary: bool = False, binary: bool = True) -> bytes",
        "setGeometryChannelsFromPattern": "(collection_name: str, geometry: Geometry, pattern: str) -> None",
    },
    "clone": {
        "addConnectionChangeCallback": "(callback: Callable[[str], None]) -> None",
        "addImageChangeCallback": "(callback: Callable[[str], None]) -> None",
        "connectionChangeCallbacks": "() -> Tuple[Callable[[str], None], ...]",
        "imageChangeCallbacks": "() -> Tuple[Callable[[str], None], ...]",
        "removeConnectionChangeCallback": "(callback: Callable[[str], None]) -> None",
        "removeImageChangeCallback": "(callback: Callable[[str], None]) -> None",
    },
    "crowds": {
        "findAgentDefinitions": "(geometry: Geometry, group: str = '', group_type: EnumValue = geometryType.Primitives) -> Tuple[AgentDefinition, ...]",
        "replaceAgentDefinitions": "(geometry: Geometry, new_definition_map: Mapping[AgentDefinition, AgentDefinition], group: str = '', group_type: EnumValue = geometryType.Primitives) -> None",
        "setBlendshapeDeformerParms": "(base_shape_geo: Geometry, attribs: str = 'P N', point_id_attrib: str = 'id', prim_id_attrib: str = 'id') -> None",
        "applyUsdProcedural": "(stage: pxr.Usd.Stage, selection_rule: LopSelectionRule, camera_path: str, resolution: Tuple[int, int], lod_threshold: float, offscreen_quality: float, optimize_identical_poses: bool, bake_all_agents: bool, frame: float, prototype_material: str, instance_material: str, default_material: str) -> None",
    },
    "hda": {
        "addEventCallback": "(event_types: Sequence[EnumValue], callback: Callable) -> None",
        "eventCallbacks": "() -> Tuple[Tuple[Tuple[EnumValue, ...], Callable], ...]) -> None",
        "removeEventCallback": "(event_types: Sequence[EnumValue], callback: Callable) -> None",
    },
    "hipFile": {
        "collisionNodesIfMerged": "(file_name: str, node_pattern: str = '*') -> Tuple[OpNode, ...]",
        "importFBX": "(file_name: str, suppress_save_prompt: bool = False, merge_into_scene: bool = True, import_cameras: bool = True, import_joints_and_skin: bool = True, import_geometry: bool = True, import_lights: bool = True, import_animation: bool = True, import_materials: bool = True, resample_animation: bool = False, resample_interval: float = 1.0, override_framerate: bool = False, framerate: int = -1, hide_joints_attached_to_skin: bool = True, convert_joints_to_zyx_rotation_order: bool = False, material_mode: EnumValue = fbxMaterialMode.FBXShaderNodes, compatibility_mode: EnumValue = fbxCompatibilityMode.Maya, single_precision_vertex_caches: bool = False, triangulate_nurbs: bool = False, triangulate_patches: bool = False, import_global_ambient_light: bool = False, import_blend_deformers_as_blend_sops: bool = False, segment_scale_already_baked_in: bool = True, convert_file_paths_to_relative: bool = True, unlock_geometry: bool = False, unlock_deformations: bool = False, import_nulls_as_subnets: bool = False, import_into_object_subnet: bool = True, convert_into_y_up_coordinate_system: bool = False, create_sibling_bones: bool = True, override_scene_frame_range: bool = False, convert_units: bool = False) -> Tuple[ObjNode, ...]",
        "merge": "(file_name: str, node_pattern: str = '*', overwrite_on_conflict: bool = False, ignore_load_warnings: bool = False) -> None",
    },
    "hmath": {
        "buildRotate": "(rx: float | Vector3, ry: float = ..., rz: float = ..., order: str = 'xyz') -> Matrix4",
        "buildScale": "(sx: float | Vector3, sy: float = ..., sz: float = ...) -> Matrix4",
        "buildShear": "(shearx: float | Vector3, sheary: float = ..., shearz: float = ...) -> Matrix4",
        "buildTransform": "(values_dict: Mapping[str, Vector3 | Sequence[float]], transform_order: Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs'] = 'srt', rotate_order: Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'] = 'xyz') -> Matrix4",
        "buildTranslate": "(tx: float | Vector3, ty: float = ..., tz: float = ...) -> Matrix4",
        "combineLocalTransform": "(local: Matrix4, world: Matrix4, parent_local: Matrix4 | None = None, mode: EnumValue = scaleInheritanceMode.Default) -> Matrix4",
        "extractLocalTransform": "(local: Matrix4, world: Matrix4, parent_local: Matrix4, mode: EnumValue = scaleInheritanceMode.Default, effective_local: Matrix4 | None = None) -> Matrix4",
    },
    "hotkeys": {
        "addAssignment": "(context: str, hotkey_symbol: str, key: str = ...) -> bool",
        "addCommand": "(hotkey_symbol: str, label: str, description: str, assignments: Sequence[str]) -> bool",
        "assignments": "(hotkey_symbol: str) -> Tuple[str, ...]",
        "availableKeycodes": "(context: str, hotkey_symbol: str, layout_keys: Sequence[str] | None = None, modifiers: int = 0) -> Tuple[int, ...]",
        "clearAssignments": "(context: str, hotkey_symbol: str = ...) -> bool",
        "findConflicts": "(context: str, hotkey_symbol: str, key: str | None = None) -> Tuple[str, ...]",
        "removeAssignment": "(context: str, hotkey_symbol: str, key: str = ...) -> bool",
        "revertToDefaults": "(context: str, hotkey_symbol: str, one_level_only: bool) -> None",
    },
    "ik": {
        "solveFBIK": "(skeleton: Sequence[_ik_Skeleton], targets: Sequence[_ik_Target], iters: int = 30, tolerance: float = 1e-5, pin_root: bool = False) -> None",
        "solvePhysFBIK": "(skeleton: Sequence[_ik_Skeleton], targets: Sequence[_ik_Target], com_target: _ik_Target | None = None, iters: int = 30, damping: float = 0.5, tolerance: float = 1e-5) -> None",
    },
    "lop": {
        "addLockedGeometry": "(identifier: str, geo: Geometry, args: Mapping[str, str] | None = None) -> str",
        "addPreferenceChangeCallback": "(callback: Callable) -> None",
        "availableRendererInfo": "() -> list[dict[str, Any]]",
        "createConnectionParmsForProperty": "(source: LopNode | str, primpath: str, propertyname: str, parametername: str | None = None, prepend_control_parm: bool = ...) -> ParmTemplateGroup",
        "createParmsForProperty": "(source: LopNode | str, primpath: str, propertyname: str, parametername: str | None = None, prepend_control_parm: bool = ..., prefix_xform_parms: bool = ...) -> ParmTemplateGroup",
        "removePreferenceChangeCallback": "(callback: Callable) -> None",
        "setParmTupleFromProperty": "(parmtuple: ParmTuple, source: LopNode | str, primpath: str, propertyname: str) -> None",
        "translateShader": "(node: Node, node_output_name: str, material_prim_path: str, container_prim_path: str, shader_prim_name: str | None = None, frame: float | None = None) -> str",
    },
    "playbar": {
        "addEventCallback": "(callback: Callable[[EnumValue, float], None]) -> None",
        "eventCallbacks": "() -> Tuple[Callable[[EnumValue, float], None], ...]",
        "removeEventCallback": "(callback: Callable[[EnumValue, float], None]) -> None",
        "setChannelList": "(arg: ChannelList) -> None",
    },
    "properties": {
        "classes": "(tags: Sequence[str] | None = None) -> Tuple[str, ...]",
    },
    "shelves": {
        "newTool": "(file_path: str | None = None, name: str | None = None, label: str | None = None, script: str | None = None, language: EnumValue = scriptLanguage.Python, icon: str | None = None, help: str | None = None, help_url: str | None = None, network_categories: Sequence[NodeTypeCategory] = ..., viewer_categories: Sequence[NodeTypeCategory] = ..., cop_viewer_categories: Sequence[NodeTypeCategory] = ..., network_op_type: str | None = None, viewer_op_type: str | None = None, locations: Sequence[str] = ..., hda_definition: HDADefinition | None = None) -> Tool",
    },
    "text": {
        "collapseCommonVars": "(path: str, vars: Sequence[str] = ...) -> str",
    },
    "ui": {
        "addEventLoopCallback": "(callback: Callable[[], None]) -> None",
        "addResourceEventCallback": "(callback: Callable[[EnumValue, Any, str], None]) -> None",
        "addSelectionCallback": "(callback: Callable[[Sequence[NetworkMovableItem]], None]) -> None",
        "addTriggerUpdateCallback": "(callback: Callable) -> None",
        "displayConfirmation": "(text: str, severity: EnumValue = ..., help: str | None = None, title: str | None = None, details: str | None = None, details_label: str | None = None, details_expanded: bool = False, suppress: EnumValue = ...) -> bool",
        "displayCustomConfirmation": "(text: str, buttons: Sequence[str] = ..., severity: EnumValue = ..., default_choice: int = 0, close_choice: int = -1, help: str | None = None, title: str | None = None, details: str | None = None, details_label: str | None = None, details_expanded: bool = False, suppress: EnumValue = ...) -> int",
        "displayFileDependencyDialog": "(rop_node: RopNode | None = None, uploaded_files: Sequence[str] = ..., forced_unselected_patterns: Sequence[str] = ..., project_dir_variable: str = 'HIP', is_standalone: bool = true) -> Tuple[bool, Tuple[Tuple[Parm, str], ...]]",
        "displayMessage": "(text: str, buttons: Sequence[str] = ..., severity: EnumValue = ..., default_choice: int = 0, close_choice: int = -1, help: str | None = None, title: str | None = None, details: str | None = None, details_label: str | None = None, details_expanded: bool = False, suppress: EnumValue = ...) -> int",
        "eventLoopCallbacks": "() -> Tuple[Callable[[], None], ...]",
        "fireResourceCustomEvent": "(resource_type: EnumValue, user_data: Mapping[str, bool | AttribBasicType], queue: bool = True) -> None",
        "getDragSourceData": "(label: str, index: int = 0) -> Any",
        "hasDragSourceData": "(label: str, index: int) -> bool",
        "loadPackageArchive": "(file_path: str, extract_path: str | None = None) -> Tuple[str, ...]",
        "openColorEditor": "(color_changed_callback: Callable[[Color, float], None], include_alpha: bool = False, initial_color: Color | None = None, initial_alpha: float = 1.0) -> None",
        "openFileEditor": "(title: str, file_path: str, action_callback: Callable[[Mapping[str, int | float | bool | str]], None] | None = None, params: Mapping[str, int | float | bool | str] | None = None) -> None",
        "openValueLadder": "(initial_value: float, value_changed_callback: Callable[[float], None], type: EnumValue = valueLadderType.Generic, data_type: EnumValue = valueLadderDataType.Float) -> None",
        "openViewerHandleCodeGenDialog": "(category: NodeTypeCategory, action_callback: Callable[[Mapping[str, str | bool]], None]) -> None",
        "openViewerStateCodeGenDialog": "(category: NodeTypeCategory, action_callback: Callable[[Mapping[str, int | float | bool | str]], None], operator_name: str | None = None) -> None",
        "packageInfo": "(file_paths: Sequence[str]) -> str",
        "postEventCallback": "(callback: Callable[[], None]) -> None",
        "printResourceMessage": "(resource_type: EnumValue, message: str, message_type: EnumValue = ...) -> None",
        "readInput": "(text: str, buttons: Sequence[str] = ..., severity_type: EnumValue = ..., default_choice: int = 0, close_choice: int = -1, help: str | None = None, title: str | None = None, initial_contents: str | None = None) -> Tuple[int, str]",
        "readMultiInput": "(text: str, input_labels: Sequence[str], password_input_indices: Sequence[int] = ..., buttons: Sequence[str] = ..., severity_type: EnumValue = ..., default_choice: int = 0, close_choice: int = -1, help: str | None = None, title: str | None = None, initial_contents: Sequence[str] = ...) -> Tuple[int, Tuple[str, ...]]",
        "reloadViewerStates": "(state_names: Sequence[str] | None = None) -> None",
        "removeEventLoopCallback": "(callback: Callable[[], None]) -> None",
        "removePostedEventCallback": "(callback: Callable[[], None]) -> None",
        "removeResourceEventCallback": "(callback: Callable[[EnumValue, Any, str], None]) -> None",
        "removeSelectionCallback": "(callback: Callable[[Sequence[NetworkMovableItem]], None]) -> None",
        "removeTriggerUpdateCallback": "(callback: Callable) -> None",
        "selectFromList": "(choices: Sequence[str], default_choices: Sequence[int] = ..., exclusive: bool = False, message: str | None = None, title: str | None = None, column_header: str = 'Choices', num_visible_rows: int = 10, clear_on_cancel: bool = False, width: int = 0, height: int = 0, sort: bool = False, condense_paths: bool = False) -> Tuple[int, ...]",
        "selectFromTree": "(choices: Sequence[str], picked: Sequence[int] = ..., exclusive: bool = False, message: str | None = None, title: str | None = None, clear_on_cancel: bool = False, width: int = 0, height: int = 0) -> Tuple[str, ...]",
        "selectMultipleNodes": "(relative_to_node: Node | None = None, initial_node: Node | None = None, node_type_filter: EnumValue | None = None, title: str | None = None, width: int = 0, height: int = 0, custom_node_filter_callback: Callable[[Node], bool] | None = None) -> Tuple[str, ...]",
        "selectColor": "(initial_color: Color | None = NOne, options: dict[str, Any] | None = None) -> Optional[Color]",
        "selectParm": "(category: NodeTypeCategory = ..., bound_parms_only: bool = False, relative_to_node: OpNode | None = None, message: str | None = None, title: str | None = None, initial_parms: Sequence[Parm] = ..., multiple_select: bool = True, width: int = 0, height: int = 0) -> Tuple[str, ...]",
        "selectParmTuple": "(category: NodeTypeCategory = ..., bound_parms_only: bool = False, relative_to_node: OpNode | None = None, message: str | None = None, title: str | None = None, initial_parm_tuples: Sequence[ParmTuple] = ..., multiple_select: bool = True, width: int = 0, height: int = 0) -> Tuple[str, ...]",
        "selectionCallbacks": "() -> Tuple[Callable[[Sequence[NetworkMovableItem]], None], ...]",
        "setStatusMessage": "(message: str, severity: EnumValue = ...) -> None",
        "viewerHandleInfo": "(handle_names: Sequence[str] = ...) -> str",
        "viewerStateInfo": "(state_names: Sequence[str] = ...) -> str",
        "waitUntil": "(callback: Callable[[], bool]) -> None",
    },
    "viewportVisualizers": {
        "addEventCallback": "(self, event_types: EnumValue, callback: Callable, category: EnumValue = ..., node: Node | None = None) -> None",
        "createVisualizer": "(type: EnumValue, category: EnumValue = viewportVisualizerCategory.Common, node: Node | None = None) -> ViewportVisualizer",
        "eventCallbacks": "(category: EnumValue=..., node: Node | None=None) -> Sequence[Tuple[Sequence[EnumValue], Callable]]",
        "removeAllEventCallbacks": "(self, category: EnumValue = ..., node: Node | None = None) -> None",
        "removeEventCallback": "(self, event_types: Sequence[EnumValue], callback: Callable, category: EnumValue = ..., node: Node | None = None) -> None",
        "visualizers": "(category: EnumValue = ..., node: Node | None = None) -> Tuple[ViewportVisualizer, ...]",
    },
}
