from PySide6 import QtCore
from _typeshed import Incomplete
from maya.app.evaluationToolkit.EvaluationToolkitSectionGPUOutliner import OutlinerWidget as OutlinerWidget
from maya.app.evaluationToolkit.evaluation_toolkit_utilities import BUTTON_WIDTH as BUTTON_WIDTH, COLUMN_SPACING as COLUMN_SPACING, EvaluationToolkitSection as EvaluationToolkitSection, section_layout as section_layout
from maya.common.ui import LayoutManager as LayoutManager, callback_tool as callback_tool
from maya.debug.em_debug_utilities import dbg_deformations_to_dot as dbg_deformations_to_dot, get_default_directory as get_default_directory, open_file as open_file, print_deformer_clusters as print_deformer_clusters, require_evaluation_graph as require_evaluation_graph
from maya.internal.common.window.custom_control import QtCustomWindowControl as QtCustomWindowControl

kWidgetHeight: int
kPrintLabel: Incomplete
kShowLabel: Incomplete
kOutputFormat: Incomplete
kOutputLocation: Incomplete
kIncludePlugsLabel: Incomplete
kIncludePlugsAnnotation: Incomplete
kSelectedOnlyLabel: Incomplete
kSelectedOnlyAnnotation: Incomplete
kOmitPassthroughsLabel: Incomplete
kOmitPassthroughsAnnotation: Incomplete
kReuseModes: Incomplete
kNoSelectionError: Incomplete

class QEvaluationToolkitBridge(QtCore.QObject):
    tool: Incomplete
    def __init__(self, tool) -> None: ...
    def visualizeGraphSlot(self, nodes) -> None: ...

class EvaluationToolkitSectionGPUOverride(EvaluationToolkitSection):
    get_graphviz_manager: Incomplete
    widgets: Incomplete
    three_column_layout: Incomplete
    layout_widget: Incomplete
    reuseDef: Incomplete
    reuseSnk: Incomplete
    minVerts: Incomplete
    downloads: Incomplete
    downloadRejections: Incomplete
    bridge: Incomplete
    outlinerControl: Incomplete
    def __init__(self, title, start_closed, get_graphviz_manager) -> None: ...
    def graphical_frame_layout(self) -> None: ...
    @staticmethod
    @require_evaluation_graph
    def callback_print_chains(tool) -> None: ...
    @staticmethod
    @require_evaluation_graph
    def callback_print_meshes(tool) -> None: ...
    @staticmethod
    @require_evaluation_graph
    def callback_print_selected(tool) -> None: ...
    @staticmethod
    @require_evaluation_graph
    def callback_print_deformer_clusters(tool) -> None: ...
    @staticmethod
    @require_evaluation_graph
    def callback_visualize_deformations(tool) -> None: ...
    @staticmethod
    @require_evaluation_graph
    def callback_visualize_nodes(tool, nodes) -> None: ...
    @staticmethod
    def callback_update_graphical_output_format(tool) -> None: ...
    @staticmethod
    def callback_choose_graphical_output_location(tool) -> None: ...
    @staticmethod
    def callback_reuseDef(tool) -> None: ...
    @staticmethod
    def callback_reuseSnk(tool) -> None: ...
    @staticmethod
    def callback_minVerts(tool) -> None: ...
    @staticmethod
    def callback_downloadRejections(tool) -> None: ...
    @staticmethod
    def callback_downloads(tool) -> None: ...
    def update_ui(self) -> None: ...
    def get_output_file_info(self): ...
    def visualize_deformation_graph(self, deformationInfo) -> None: ...
