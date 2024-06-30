# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
import pxr.Gf as Gf
import pxr.UsdGeom as UsdGeom
from pxr.Usdviewq.adjustFreeCameraUI import Ui_AdjustFreeCamera as Ui_AdjustFreeCamera
from pxr.Usdviewq.common import FixableDoubleValidator as FixableDoubleValidator
from typing import ClassVar

class AdjustFreeCamera(PySide6.QtWidgets.QDialog):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent, dataModel, signalFrustumChanged) -> None: ...
    def _aspectSpinBoxChanged(self, value):
        """Updates the camera's aspect ratio based on the spin box value."""
    def _farChanged(self, value):
        """Called when the Far spin box changed.  This can happen when we
                are updating the value but the widget is actually inactive - don't
                do anything in that case."""
    def _freeCamFovChanged(self, value): ...
    def _frustumChanged(self):
        """Updates the UI to reflect the current camera frustum."""
    def _getCurrentAspectRatio(self):
        """Returns the current aspect ratio that should be displayed in the spin
                box.

                If a camera prim is active, reflect that value. Otherwise, use the
                current setting."""
    def _getCurrentClippingRange(self):
        """Returns the current clipping range (near, far) that should be
                displayed in the spin boxes.

                If the view settings have values for freeCameraOverrideNear/Far, then
                those values should be chosen. Otherwise, take the clipping range from
                the current camera (whether a camera prim or the free camera)."""
    def _getCurrentFov(self):
        """Returns the current vertical field of view that should be displayed
                in the spin box.

                If a camera prim is active, reflect that value. Otherwise, use the
                current setting."""
    def _lockFreeCamAspectToggled(self, state): ...
    def _nearChanged(self, value):
        """Called when the Near spin box changed.  This can happen when we
                are updating the value but the widget is actually inactive - don't
                do anything in that case."""
    def _overrideFarToggled(self, state):
        '''Called when the "Override Far" checkbox is toggled'''
    def _overrideNearToggled(self, state):
        '''Called when the "Override Near" checkbox is toggled'''
    def closeEvent(self, event): ...
