# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import UI4.Widgets.MessageBox as MessageBox
import NodegraphAPI as NodegraphAPI
import PyFCurve as PyFCurve
import QT4Browser as QT4Browser
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.ValuePolicy
import QTFCurve as QTFCurve
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4FormWidgets.FormWidget import FormWidget
from QT4Widgets.MenuButton import MenuButton as MenuButton
from QT4Widgets.StretchBox import StretchBox as StretchBox
from QTFCurve.FCurveGraphValueListWidget import FCurveGraphValueListWidget
from UI4.FormMaster.Editors.AssetId import AssetIdWidget as AssetIdWidget
from UI4.Util.AssetId import BrowseForAsset as BrowseForAsset
from typing import Set, Tuple

class FCurveFormWidget(FormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _FCurveFormWidget__actionMenuAboutToShow(self): ...
    def _FCurveFormWidget__configureEditor(self): ...
    def _FCurveFormWidget__curveChanged(self, curve, force: bool = ...): ...
    def _FCurveFormWidget__exportFcurve(self): ...
    def _FCurveFormWidget__fileEditorActive(self): ...
    def _FCurveFormWidget__importFcurve(self): ...
    def _FCurveFormWidget__setControlAreaLabel(self): ...
    def _FCurveFormWidget__subscribeContainer(self): ...
    def _FCurveFormWidget__switchToFCurve(self): ...
    def _FCurveFormWidget__switchToFileName(self): ...
    def _FCurveFormWidget__switchToMulti(self): ...
    def _FCurveFormWidget__unsubscribeContainer(self): ...
    def _buildControlWidget(self, hbox): ...
    def _thaw(self): ...
    def valueChangedEvent(self, event): ...

class _CurveEditor(FCurveGraphValueListWidget):
    def __init__(self, ratio, *args) -> None: ...
    def heightForWidth(self, w): ...

class _FileNamePolicyProxy(QT4FormWidgets.ValuePolicy.ValuePolicyProxy):
    def __init__(self, policy, hints) -> None: ...
    def getWidgetHints(self): ...
    def shouldDisplayState(self): ...
    def shouldDisplayWrench(self): ...

class _SimpleContainerObserver(PyFCurve.ContainerObserver):
    def __init__(self, observer, policy, setLabelFunc) -> None: ...
    def containerChanged(self, container): ...

class _SimpleObserver(PyFCurve.FCurveObserver):
    def __init__(self) -> None: ...
    def beginValueChange(self, curve): ...
    def curveChanged(self, curve): ...
    def emitter(self): ...
    def endValueChange(self, curve): ...
