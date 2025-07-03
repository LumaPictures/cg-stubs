from .adjustFreeCameraUI import Ui_AdjustFreeCamera as Ui_AdjustFreeCamera
from .common import FixableDoubleValidator as FixableDoubleValidator
from .qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete
from pxr import Gf as Gf, UsdGeom as UsdGeom

class AdjustFreeCamera(QtWidgets.QDialog):
    """Dialog to adjust the free camera settings (clipping, fov, aspect ratio).
    """
    _ui: Incomplete
    _dataModel: Incomplete
    _signalFrustumChanged: Incomplete
    def __init__(self, parent, dataModel, signalFrustumChanged) -> None: ...
    def _overrideNearToggled(self, state) -> None:
        '''Called when the "Override Near" checkbox is toggled'''
    def _overrideFarToggled(self, state) -> None:
        '''Called when the "Override Far" checkbox is toggled'''
    def _nearChanged(self, value) -> None:
        """Called when the Near spin box changed.  This can happen when we
        are updating the value but the widget is actually inactive - don't
        do anything in that case."""
    def _farChanged(self, value) -> None:
        """Called when the Far spin box changed.  This can happen when we
        are updating the value but the widget is actually inactive - don't
        do anything in that case."""
    def _lockFreeCamAspectToggled(self, state) -> None: ...
    def _aspectSpinBoxChanged(self, value) -> None:
        """Updates the camera's aspect ratio based on the spin box value."""
    def _getCurrentAspectRatio(self):
        """Returns the current aspect ratio that should be displayed in the spin
        box.

        If a camera prim is active, reflect that value. Otherwise, use the
        current setting."""
    def _getCurrentFov(self):
        """Returns the current vertical field of view that should be displayed
        in the spin box.

        If a camera prim is active, reflect that value. Otherwise, use the
        current setting."""
    def _getCurrentClippingRange(self):
        """Returns the current clipping range (near, far) that should be
        displayed in the spin boxes.

        If the view settings have values for freeCameraOverrideNear/Far, then
        those values should be chosen. Otherwise, take the clipping range from
        the current camera (whether a camera prim or the free camera)."""
    def _freeCamFovChanged(self, value) -> None: ...
    def _frustumChanged(self) -> None:
        """Updates the UI to reflect the current camera frustum."""
    def closeEvent(self, event) -> None: ...
