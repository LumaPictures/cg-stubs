from .common import DEBUG_CLIPPING as DEBUG_CLIPPING
from .qt import QtCore as QtCore
from _typeshed import Incomplete
from pxr import Gf as Gf, Tf as Tf

class FreeCamera(QtCore.QObject):
    signalFrustumChanged: Incomplete
    signalFrustumSettingsChanged: Incomplete
    defaultNear: int
    defaultFar: int
    maxSafeZResolution: float
    maxGoodZResolution: float
    _camera: Incomplete
    _overrideNear: Incomplete
    _overrideFar: Incomplete
    _isZUp: Incomplete
    _cameraTransformDirty: bool
    _rotTheta: int
    _rotPhi: int
    _rotPsi: int
    _center: Incomplete
    _dist: int
    _closestVisibleDist: Incomplete
    _lastFramedDist: Incomplete
    _lastFramedClosestDist: Incomplete
    _selSize: int
    _YZUpMatrix: Incomplete
    _YZUpInvMatrix: Incomplete
    def __init__(self, isZUp, fov: float = 60.0, aspectRatio: float = 1.0, overrideNear: Incomplete | None = None, overrideFar: Incomplete | None = None) -> None:
        """FreeCamera can be either a Z up or Y up camera, based on 'zUp'"""
    def clone(self): ...
    def _pushToCameraTransform(self):
        """
        Updates the camera's transform matrix, that is, the matrix that brings
        the camera to the origin, with the camera view pointing down:
           +Y if this is a Zup camera, or
           -Z if this is a Yup camera .
        """
    def _pullFromCameraTransform(self) -> None:
        """
        Updates parameters (center, rotTheta, etc.) from the camera transform.
        """
    def _rangeOfBoxAlongRay(self, camRay, bbox, debugClipping: bool = False): ...
    def setClippingPlanes(self, stageBBox) -> None:
        '''Computes and sets automatic clipping plane distances using the
           camera\'s position and orientation, the bouding box
           surrounding the stage, and the distance to the closest rendered
           object in the central view of the camera (closestVisibleDist).

           If either of the "override" clipping attributes are not None,
           we use those instead'''
    def computeGfCamera(self, stageBBox, autoClip: bool = False):
        '''Makes sure the FreeCamera\'s computed parameters are up-to-date, and
        returns the GfCamera object.  If \'autoClip\' is True, then compute
        "optimal" positions for the near/far clipping planes based on the
        current closestVisibleDist, in order to maximize Z-buffer resolution'''
    def resetClippingPlanes(self) -> None:
        """Set near and far back to their uncomputed defaults."""
    def frameSelection(self, selBBox, frameFit) -> None: ...
    def setClosestVisibleDistFromPoint(self, point) -> None: ...
    def ComputePixelsToWorldFactor(self, viewportHeight):
        """Computes the ratio that converts pixel distance into world units.

        It treats the pixel distances as if they were projected to a plane going
        through the camera center."""
    def Tumble(self, dTheta, dPhi) -> None:
        """ Tumbles the camera around the center point by (dTheta, dPhi) degrees. """
    def AdjustDistance(self, scaleFactor) -> None:
        '''Scales the distance of the freeCamera from it\'s center typically by
        scaleFactor unless it puts the camera into a "stuck" state.'''
    def Truck(self, deltaRight, deltaUp) -> None:
        """ Moves the camera by (deltaRight, deltaUp) in worldspace coordinates. 

        This is similar to a camera Truck/Pedestal.
        """
    def PanTilt(self, dPan, dTilt) -> None:
        """ Rotates the camera around the current camera base (approx. the film
        plane).  Both parameters are in degrees.

        This moves the center point that we normally tumble around.

        This is similar to a camera Pan/Tilt.
        """
    def Walk(self, dForward, dRight) -> None:
        ''' Specialized camera movement that moves it on the "horizontal" plane
        '''
    @staticmethod
    def FromGfCamera(gfCamera, isZUp): ...
    @property
    def rotTheta(self): ...
    @rotTheta.setter
    def rotTheta(self, value) -> None: ...
    @property
    def rotPhi(self): ...
    @rotPhi.setter
    def rotPhi(self, value) -> None: ...
    @property
    def center(self): ...
    @center.setter
    def center(self, value) -> None: ...
    @property
    def dist(self): ...
    @dist.setter
    def dist(self, value) -> None: ...
    @property
    def orthographic(self): ...
    @orthographic.setter
    def orthographic(self, orthographic) -> None: ...
    @property
    def fov(self):
        """The vertical field of view, in degrees, for perspective cameras. 
        For orthographic cameras fov is the height of the view frustum, in 
        world units.
        """
    @fov.setter
    def fov(self, value) -> None: ...
    @property
    def aspectRatio(self): ...
    @aspectRatio.setter
    def aspectRatio(self, value) -> None:
        """Sets the aspect ratio by adjusting the horizontal aperture."""
    @property
    def horizontalAperture(self): ...
    @horizontalAperture.setter
    def horizontalAperture(self, value) -> None: ...
    @property
    def verticalAperture(self): ...
    @verticalAperture.setter
    def verticalAperture(self, value) -> None: ...
    @property
    def focalLength(self): ...
    @focalLength.setter
    def focalLength(self, value) -> None: ...
    @property
    def near(self): ...
    @property
    def far(self): ...
    @property
    def overrideNear(self): ...
    @overrideNear.setter
    def overrideNear(self, value) -> None:
        """To remove the override, set to None"""
    @property
    def overrideFar(self): ...
    @overrideFar.setter
    def overrideFar(self, value) -> None:
        """To remove the override, set to None"""
