from typing import ClassVar

import hou
import pdg
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class PDGServicePanel(PySide6.QtWidgets.QWidget):
    update_event: ClassVar[PySide6.QtCore.Signal]
    update_pool_size_event: ClassVar[PySide6.QtCore.Signal]
    previous_selection: PySide6.QtWidgets.QTableWidgetItem | None
    service_event_handler: pdg.PyEventHandler
    service_start_begin_handler: pdg.PyEventHandler
    service_start_end_handler: pdg.PyEventHandler
    service_client_started_handler: pdg.PyEventHandler
    service_client_changed_handler: pdg.PyEventHandler
    main_layout: PySide6.QtWidgets.QGridLayout
    service_buttons: PySide6.QtWidgets.QToolBar
    create_service_button: PySide6.QtWidgets.QPushButton
    delete_service_button: PySide6.QtWidgets.QPushButton
    panel_help_button: hou.qt.HelpButton
    service_controls: PySide6.QtWidgets.QWidget
    service_controls_layout: PySide6.QtWidgets.QHBoxLayout
    vsplitter: PySide6.QtWidgets.QSplitter
    service_list: "PDGServiceList"
    client_list: "PDGServiceClientList"
    service_config: "PDGServiceConfigWidget"
    config_scroll_area: PySide6.QtWidgets.QScrollArea
    hsplitter: PySide6.QtWidgets.QSplitter
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def onActivateInterface(self) -> None: ...
    def onDeactivateInterface(self) -> None: ...
    def onNodePathChanged(self, node: hou.Node | None) -> None: ...
    def onDestroyInterface(self) -> None: ...

class PDGServiceClientList(PySide6.QtWidgets.QTableWidget):
    header_labels: list[str]
    icon_size: int
    available_icon: PySide6.QtGui.QIcon
    running_icon: PySide6.QtGui.QIcon
    unavailable_icon: PySide6.QtGui.QIcon
    service: pdg.Service | None
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def update_list(self, service: pdg.Service | None) -> None: ...
    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent) -> None: ...

class PDGServiceConfigWidget(PySide6.QtWidgets.QWidget):
    service_pool_size_updated: ClassVar[PySide6.QtCore.Signal]
    service: pdg.Service | None
    chooser_icon: PySide6.QtGui.QIcon
    margin_size: int
    main_layout: PySide6.QtWidgets.QGridLayout
    service_name_label: PySide6.QtWidgets.QLabel
    service_name: PySide6.QtWidgets.QLabel
    service_type_label: PySide6.QtWidgets.QLabel
    service_type: PySide6.QtWidgets.QLabel
    extra_args_label: PySide6.QtWidgets.QLabel
    extra_args: PySide6.QtWidgets.QLineEdit
    status_label: PySide6.QtWidgets.QLabel
    status: PySide6.QtWidgets.QLabel
    service_owner_label: PySide6.QtWidgets.QLabel
    service_owner: PySide6.QtWidgets.QLabel
    service_scheduler_label: PySide6.QtWidgets.QLabel
    service_scheduler: PySide6.QtWidgets.QLabel
    service_persistent_label: PySide6.QtWidgets.QLabel
    service_persistent: PySide6.QtWidgets.QLabel
    mq_server_authenticated_label: PySide6.QtWidgets.QLabel
    mq_server_authenticated: PySide6.QtWidgets.QLabel
    mq_clients_authenticated_label: PySide6.QtWidgets.QLabel
    mq_clients_authenticated: PySide6.QtWidgets.QLabel
    pool_size_label: PySide6.QtWidgets.QLabel
    connection_timeout_label: PySide6.QtWidgets.QLabel
    start_button: PySide6.QtWidgets.QPushButton
    stop_button: PySide6.QtWidgets.QPushButton
    pool_size_edit: PySide6.QtWidgets.QLineEdit
    connection_timeout: PySide6.QtWidgets.QLineEdit
    auto_start_toggle: PySide6.QtWidgets.QCheckBox
    mqserver_logging_dir_label: PySide6.QtWidgets.QLabel
    mqserver_logging_dir: PySide6.QtWidgets.QLineEdit
    mqserver_logging_level_label: PySide6.QtWidgets.QLabel
    mqserver_logging_level: PySide6.QtWidgets.QComboBox
    client_logging_type_label: PySide6.QtWidgets.QLabel
    client_logging_type: PySide6.QtWidgets.QComboBox
    client_logging_dir_label: PySide6.QtWidgets.QLabel
    client_logging_dir: PySide6.QtWidgets.QLineEdit
    memory_limit_type_label: PySide6.QtWidgets.QLabel
    memory_limit_type: PySide6.QtWidgets.QComboBox
    memory_limit_label: PySide6.QtWidgets.QLabel
    memory_limit: PySide6.QtWidgets.QLineEdit
    add_env_var: PySide6.QtWidgets.QPushButton
    env_editor: PySide6.QtWidgets.QTableWidget
    service_controls: PySide6.QtWidgets.QWidget
    service_controls_layout: PySide6.QtWidgets.QGridLayout
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def get_service(self) -> pdg.Service | None: ...
    def set_service(self, service: pdg.Service | None = ...) -> None: ...
    def childContextMenuEvent(self, local_pos: PySide6.QtCore.QPoint, child_widget: PySide6.QtWidgets.QWidget) -> None: ...

class PDGServiceList(PySide6.QtWidgets.QTableWidget):
    header_labels: list[str]
    icon_size: int
    running_icon: PySide6.QtGui.QIcon
    starting_icon: PySide6.QtGui.QIcon
    stopped_icon: PySide6.QtGui.QIcon
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def update_list(self, service_to_select: pdg.Service | None = ...) -> None: ...
    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent) -> None: ...
    def update_row(self, item: PySide6.QtWidgets.QTableWidgetItem) -> None: ...

class PDGAddServiceDialog(PySide6.QtWidgets.QDialog):
    added_service: pdg.Service | None
    error: str | None
    service_types: dict[str, str]
    margin_size: int
    main_layout: PySide6.QtWidgets.QGridLayout
    service_type_label: PySide6.QtWidgets.QLabel
    service_type: PySide6.QtWidgets.QComboBox
    service_owner_label: PySide6.QtWidgets.QLabel
    service_owner: PySide6.QtWidgets.QComboBox
    service_name_label: PySide6.QtWidgets.QLabel
    service_name: PySide6.QtWidgets.QLineEdit
    auto_start_toggle: PySide6.QtWidgets.QCheckBox
    pool_size_label: PySide6.QtWidgets.QLabel
    pool_size: PySide6.QtWidgets.QLineEdit
    port_label: PySide6.QtWidgets.QLabel
    port_choice: PySide6.QtWidgets.QComboBox
    port_num: PySide6.QtWidgets.QLineEdit
    connection_timeout_label: PySide6.QtWidgets.QLabel
    connection_timeout: PySide6.QtWidgets.QLineEdit
    mqserver_logging_level_label: PySide6.QtWidgets.QLabel
    mqserver_logging_level: PySide6.QtWidgets.QComboBox
    mqserver_logging_dir_label: PySide6.QtWidgets.QLabel
    mqserver_logging_dir: PySide6.QtWidgets.QLineEdit
    client_logging_type_label: PySide6.QtWidgets.QLabel
    client_logging_type: PySide6.QtWidgets.QComboBox
    client_logging_dir_label: PySide6.QtWidgets.QLabel
    client_logging_dir: PySide6.QtWidgets.QLineEdit
    add_button: PySide6.QtWidgets.QPushButton
    cancel_button: PySide6.QtWidgets.QPushButton
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
