from collections.abc import Mapping
from typing import NoReturn

import hou
from PySide6 import QtWidgets

from autorigs.ui import uiGeometryParams
from autorigs.ui.uiParamName import UiParamName

class UiGeometryInfo(QtWidgets.QWidget):
    GEO_SOURCE_OPERATOR: int
    GEO_SOURCE_FILE: int
    GEO_SOURCE_STANDIN: int
    PLACEMENT_AS_IS: int
    PLACEMENT_AUTO_PLACE: int
    OBJFILE_SWITCH_OPERATOR: int
    OBJFILE_SWITCH_FILE: int
    PLACEMENT_SWITCH_OBJFILE: int
    PLACEMENT_SWITCH_PLACEGEO: int
    PLACEMENT_SWITCH_STANDIN: int
    DEFAULT_GEO_NAME: str
    GEO_SOURCES: list[str]
    GEO_PLACEMENTS: list[str]
    geometryguides: Mapping[str, hou.OpNode]
    geosource_combobox: hou.qt.ComboBox
    geoplacement_label: QtWidgets.QLabel
    geoplacement_combobox: hou.qt.ComboBox
    embedcheck: QtWidgets.QCheckBox
    customgeoname_checkbox: QtWidgets.QCheckBox
    customgeoname_widget: UiParamName
    operator_params_widget: uiGeometryParams.UiGeometryOperator
    file_params_widget: uiGeometryParams.UiGeometryFile
    standin_params_widget: uiGeometryParams.UiGeometryStandIn
    geooptions_stack: QtWidgets.QStackedWidget

    def __init__(self, geometryguides: Mapping[str, hou.OpNode]) -> None: ...
    def getCustomGeoName(self) -> str: ...
    def getSourceOption(self) -> int: ...
    def getOperatorPath(self) -> str: ...
    def getFilePath(self) -> NoReturn: ...
    def getIsEmbedded(self) -> bool: ...
    def getPlacementIndex(self) -> int: ...
    def getInvertedGeoOffset(self) -> list[float]: ...
