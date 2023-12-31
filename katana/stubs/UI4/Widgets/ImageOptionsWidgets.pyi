# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.IconManager as IconManager
import Nodes2DAPI as Nodes2DAPI
import PyOpenColorIO as OCIO
import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
from UI4.Widgets.ComboBoxNoWheel import ComboBoxNoWheel as ComboBoxNoWheel
from _typeshed import Incomplete
from typing import Set, Tuple

class ColorspaceSelectionWidget(OptionComboBase):
    def __init__(self, parent, default: Incomplete | None = ...) -> None: ...

class ExrBitDepthWidget(OptionComboBase):
    def __init__(self, parent, default: str = ...) -> None: ...

class ExrCompressionWidget(OptionComboBase):
    def __init__(self, parent, default: str = ...) -> None: ...

class ImageOptionsWidget(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent, defaultExtension: str = ..., defaultValue: Incomplete | None = ...) -> None: ...
    def setColorspace(self, csname): ...
    def setExtension(self, extension): ...
    def setValue(self, optionsDict): ...
    def value(self): ...

class JpgQualityWidget(PyQt5.QtWidgets.QSpinBox):
    def __init__(self, parent, default: str = ...) -> None: ...
    def setValue(self, value): ...
    def value(self): ...

class OptionComboBase(ComboBoxNoWheel):
    def __init__(self, parent, optionList, default) -> None: ...
    def setOptions(self, optionList): ...
    def setValue(self, option): ...
    def value(self): ...

class OutputImageExtensionWidget(OptionComboBase):
    def __init__(self, parent, default: str = ...) -> None: ...

class PngBitDepthWidget(OptionComboBase):
    def __init__(self, parent, default: str = ...) -> None: ...

class RlaBitDepthWidget(OptionComboBase):
    def __init__(self, parent, default: str = ...) -> None: ...

class TifBitDepthWidget(OptionComboBase):
    def __init__(self, parent, default: str = ...) -> None: ...

class TifCompressionWidget(OptionComboBase):
    def __init__(self, parent, default: str = ...) -> None: ...
