# mypy: disable-error-code="misc, override, no-redef"

import pxr.Gf as Gf
from _typeshed import Incomplete

class UsdviewApi:
    """This class is an interface that provides access to Usdview context for
    Usdview plugins and other clients. It abstracts away the implementation of
    Usdview so that the core can change without affecting clients.
    """
    viewerMode: Incomplete
    def __init__(self, appController) -> None: ...
    def AddPrimToSelection(self, prim): ...
    def ClearPrimSelection(self): ...
    def ComputeModelsFromSelection(self):
        '''Returns selected models.  this will walk up to find the nearest model.
                Note, this may return "group"\'s if they are selected.
        '''
    def ComputeSelectedPrimsOfType(self, schemaType):
        """Returns selected prims of the provided schemaType (TfType)."""
    def GetSettings(self):
        """Returns the settings object."""
    def GetViewportCurrentRendererId(self): ...
    def GetViewportRendererNames(self):
        """Returns the list of available renderer plugins that can be passed to
                SetViewportRenderer().
        """
    def GrabViewportShot(self):
        """Returns a QImage of the current stage view in usdview."""
    def GrabWindowShot(self):
        """Returns a QImage of the full usdview window."""
    def PrintStatus(self, msg):
        """Prints a status message."""
    def SetViewportRenderer(self, plugId):
        """Sets the renderer based on the given ID string.

                The string should be one of the items in GetViewportRendererNames().
        """
    def UpdateGUI(self):
        """Updates the main UI views"""
    def UpdateViewport(self):
        """Schedules a redraw."""
    def _ExportSession(self, stagePath, defcamName: str = ..., imgWidth: Incomplete | None = ..., imgHeight: Incomplete | None = ...):
        """Export the free camera (if currently active) and session layer to a
                USD file at the specified stagePath that references the current-viewed
                stage.
        """
    @property
    def cameraPrim(self): ...
    @property
    def configDir(self): ...
    @property
    def currentGfCamera(self): ...
    @property
    def dataModel(self): ...
    @property
    def frame(self): ...
    @property
    def layer(self): ...
    @property
    def prim(self): ...
    @property
    def property(self): ...
    @property
    def qMainWindow(self): ...
    @property
    def selectedInstances(self): ...
    @property
    def selectedPaths(self): ...
    @property
    def selectedPoint(self): ...
    @property
    def selectedPrims(self): ...
    @property
    def spec(self): ...
    @property
    def stage(self): ...
    @property
    def stageIdentifier(self): ...
    @property
    def viewportSize(self): ...
