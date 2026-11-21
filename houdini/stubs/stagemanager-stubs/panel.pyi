# Houdini stubs generated from Houdini 22.0.466

import hou
from . import common as common, model as model, view as view, widgets as widgets
from .common import Column as Column
from collections.abc import Mapping, Sequence
from edit.lop.panel import LopEditPanel
from hutil.PySide import QtCore, QtGui, QtWidgets
from pxr import Ar as Ar, Tf as Tf

FILE_BROWSER_DEFAULT_PATH: str

class StageManagerPanel(QtWidgets.QFrame):
    source_node: hou.OpNode | None
    scene_viewer: hou.SceneViewer
    stacked_layout: QtWidgets.QStackedLayout
    inspector_variant_sets_layout: QtWidgets.QVBoxLayout
    main_toolbar: widgets.MainToolbar
    scenegraph_model: model.StageManagerSortAndFilterModel
    scenegraph_treeview: view.SceneGraphTreeView
    scenegraph_filter: QtWidgets.QLineEdit
    tools_widget: QtWidgets.QTabWidget
    inspector_paths_model: QtGui.QStandardItemModel
    inspector_resolved_paths_model: QtGui.QStandardItemModel
    prim_path: QtWidgets.QLineEdit
    kind_attr: QtWidgets.QComboBox
    instanceable_toggle: QtWidgets.QCheckBox
    instanceable: QtWidgets.QComboBox
    variant_sets_group: QtWidgets.QGroupBox
    variant_sets_layout: QtWidgets.QVBoxLayout
    file_browser_tab: QtWidgets.QWidget
    file_browser_toolbar: widgets.FileBrowserToolbar
    file_browser_treeview: view.FileBrowserTreeView
    reference_paths_group: widgets.ReferencePathsGroup
    asset_catalog_tab: QtWidgets.QWidget
    transforms_panel: LopEditPanel
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def updateViews(self, parent: QtCore.QModelIndex, first: int, last: int) -> None: ...
    def handleInstanceableToggled(self, state: bool) -> None: ...
    def handlePrimPickerAccept(self, selected: Sequence[str]) -> None: ...
    def handleEditRefPrimPath(self) -> None: ...
    def handleSetData(self, column: int, value: str | bool | Mapping[str, str] | None) -> None: ...
    def handleSetAttr(self, attr: str, value: bool | None) -> None: ...
    def handleUpdateInspector(self) -> None: ...
    def updateVariantSets(self, selection_changed: bool = False) -> None: ...
    def handleFilterChanged(self) -> None: ...
    def handleFileViewRootChanged(self, file_path: str) -> None: ...
    def handleReloadFiles(self, **kwargs: object) -> None: ...
    def handleToggleControlPane(self) -> None: ...
    def clearAllEdits(self) -> None: ...
    def toggleFlattenLayers(self) -> None: ...
