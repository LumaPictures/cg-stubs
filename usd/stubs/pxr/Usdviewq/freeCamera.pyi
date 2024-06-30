# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import pxr.Gf as Gf
import pxr.Tf as Tf
from _typeshed import Incomplete
from typing import ClassVar

DEBUG_CLIPPING: str

class FreeCamera(PySide6.QtCore.QObject):
    defaultFar: ClassVar[int] = ...
    defaultNear: ClassVar[int] = ...
    maxGoodZResolution: ClassVar[float] = ...
    maxSafeZResolution: ClassVar[float] = ...
    signalFrustumChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalFrustumSettingsChanged: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    aspectRatio: Incomplete
    center: Incomplete
    dist: Incomplete
    focalLength: Incomplete
    fov: Incomplete
    horizontalAperture: Incomplete
    orthographic: Incomplete
    overrideFar: Incomplete
    overrideNear: Incomplete
    rotPhi: Incomplete
    rotTheta: Incomplete
    verticalAperture: Incomplete
    def __init__(self, isZUp, fov: float = ..., aspectRatio: float = ..., overrideNear: Incomplete | None = ..., overrideFar: Incomplete | None = ...) -> None:
        """FreeCamera can be either a Z up or Y up camera, based on 'zUp'"""
    def AdjustDistance(self, scaleFactor):
        '''Scales the distance of the freeCamera from it\'s center typically by
                scaleFactor unless it puts the camera into a "stuck" state.'''
    def ComputePixelsToWorldFactor(self, viewportHeight):
        """Computes the ratio that converts pixel distance into world units.

                It treats the pixel distances as if they were projected to a plane going
                through the camera center."""
    @staticmethod
    def FromGfCamera(gfCamera, isZUp): ...
    def PanTilt(self, dPan, dTilt):
        """ Rotates the camera around the current camera base (approx. the film
                plane).  Both parameters are in degrees.

                This moves the center point that we normally tumble around.

                This is similar to a camera Pan/Tilt.
        """
    def Truck(self, deltaRight, deltaUp):
        """ Moves the camera by (deltaRight, deltaUp) in worldspace coordinates. 

                This is similar to a camera Truck/Pedestal.
        """
    def Tumble(self, dTheta, dPhi):
        """ Tumbles the camera around the center point by (dTheta, dPhi) degrees. """
    def Walk(self, dForward, dRight):
        ''' Specialized camera movement that moves it on the "horizontal" plane
        '''
    def _pullFromCameraTransform(self):
        """
        Updates parameters (center, rotTheta, etc.) from the camera transform.
        """
    def _pushToCameraTransform(self):
        """
        Updates the camera's transform matrix, that is, the matrix that brings
        the camera to the origin, with the camera view pointing down:
           +Y if this is a Zup camera, or
           -Z if this is a Yup camera .
        """
    def _rangeOfBoxAlongRay(self, camRay, bbox, debugClipping: bool = ...): ...
    def clone(self): ...
    def computeGfCamera(self, stageBBox, autoClip: bool = ...):
        '''Makes sure the FreeCamera\'s computed parameters are up-to-date, and
                returns the GfCamera object.  If \'autoClip\' is True, then compute
                "optimal" positions for the near/far clipping planes based on the
                current closestVisibleDist, in order to maximize Z-buffer resolution'''
    def frameSelection(self, selBBox, frameFit): ...
    def resetClippingPlanes(self):
        """Set near and far back to their uncomputed defaults."""
    def setClippingPlanes(self, stageBBox):
        '''Computes and sets automatic clipping plane distances using the
                   camera\'s position and orientation, the bouding box
                   surrounding the stage, and the distance to the closest rendered
                   object in the central view of the camera (closestVisibleDist).

                   If either of the "override" clipping attributes are not None,
                   we use those instead'''
    def setClosestVisibleDistFromPoint(self, point): ...
    @property
    def far(self): ...
    @property
    def near(self): ...
