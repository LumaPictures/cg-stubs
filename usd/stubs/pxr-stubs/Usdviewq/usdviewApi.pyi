from .qt import QtCore as QtCore
from _typeshed import Incomplete
from pxr import Gf as Gf

class UsdviewApi:
    """This class is an interface that provides access to Usdview context for
    Usdview plugins and other clients. It abstracts away the implementation of
    Usdview so that the core can change without affecting clients.
    """
    __appController: Incomplete
    def __init__(self, appController) -> None: ...
    @property
    def dataModel(self):
        """Usdview's active data model object."""
    @property
    def stage(self):
        """The current Usd.Stage."""
    @property
    def frame(self):
        """The current frame."""
    @property
    def prim(self):
        """The focus prim from the prim selection."""
    @property
    def selectedPoint(self):
        """The currently selected world space point."""
    @property
    def selectedPrims(self):
        """A list of all currently selected prims."""
    @property
    def selectedPaths(self):
        """A list of the paths of all currently selected prims."""
    @property
    def selectedInstances(self):
        """The current prim instance selection. This is a dictionary where each
        key is a prim and each value is a set of instance ids selected from that
        prim.
        """
    @property
    def spec(self):
        """The currently selected Sdf.Spec from the Composition tab."""
    @property
    def layer(self):
        """The currently selected Sdf.Layer in the Composition tab."""
    @property
    def cameraPrim(self):
        """The current camera prim."""
    @property
    def currentGfCamera(self):
        """A copy of the last computed Gf Camera."""
    @property
    def viewportSize(self):
        """The width and height of the viewport in pixels."""
    @property
    def configDir(self):
        """The config dir, typically ~/.usdview/."""
    @property
    def stageIdentifier(self):
        """The identifier of the open Usd.Stage's root layer."""
    @property
    def qMainWindow(self):
        """A QWidget object that other widgets can use as a parent."""
    @property
    def viewerMode(self):
        """Whether the app is in viewer mode, with the additional UI around the
        stage view collapsed."""
    @viewerMode.setter
    def viewerMode(self, value) -> None: ...
    @property
    def property(self):
        """The focus property from the property selection."""
    def ComputeModelsFromSelection(self):
        '''Returns selected models.  this will walk up to find the nearest model.
        Note, this may return "group"\'s if they are selected.
        '''
    def ComputeSelectedPrimsOfType(self, schemaType):
        """Returns selected prims of the provided schemaType (TfType)."""
    def UpdateGUI(self) -> None:
        """Updates the main UI views"""
    def PrintStatus(self, msg) -> None:
        """Prints a status message."""
    def GetSettings(self):
        """Returns the settings object."""
    def ClearPrimSelection(self) -> None: ...
    def AddPrimToSelection(self, prim) -> None: ...
    def GrabWindowShot(self):
        """Returns a QImage of the full usdview window."""
    def GrabViewportShot(self):
        """Returns a QImage of the current stage view in usdview."""
    def UpdateViewport(self) -> None:
        """Schedules a redraw."""
    def SetViewportRenderer(self, plugId) -> None:
        """Sets the renderer based on the given ID string.

        The string should be one of the items in GetViewportRendererNames().
        """
    def GetViewportRendererNames(self):
        """Returns the list of available renderer plugins that can be passed to
        SetViewportRenderer().
        """
    def GetViewportCurrentRendererId(self): ...
    def _ExportSession(self, stagePath, defcamName: str = 'usdviewCam', imgWidth: Incomplete | None = None, imgHeight: Incomplete | None = None) -> None:
        """Export the free camera (if currently active) and session layer to a
        USD file at the specified stagePath that references the current-viewed
        stage.
        """
