# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Callable as Callable
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs
from sidefx_stroke import StrokeData as StrokeData
from typing import Any

class BrushInterface:
    name: str
    def __init__(self) -> None: ...
    def initSpareParms(self, parm_template: hou.FolderParmTemplate) -> None:
        """
        Given a hou.ParmTemplateFolder object parm_template,
        add hou.ParmTemplates for parameters specific to this
        brush.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, update_cb: Callable[..., object]) -> None:
        '''
        Called when we want to apply this brush, kwargs contains
        the following special arguments:

        - new_points    Geometry to add new points to

        - hit_point         hou.Vector3 describing the position of
                            intersection in world space.

        - hit_normal        hou.Vector3 describint the normal at the
                            intersected point in world space.

        - mouse_x           int describing the x position of the
                            cursor.

        - mouse_y           int describing the y position of the
                            cursor.

        - working_set            List of asset identifiers for current
                            working set.


        To create an asset you must add a point to point_geometry and
        assign it certain attributes. This should be done in an HDA but
        technically you could write a fully python brush if you wanted to.

        Example:
            point = kwargs[\'new_geometry\'].createPoint()
            point.setPosition(some_position)
            point.setAttribValue("orient", some_quaternion)
            point.setAttribValue("pscale", some_float)
            point.setAttribValue("asset", some_asset_index)
        '''
    def onBrushParmTupleChange(self, metadata: dict[str, Any]) -> None:
        """
        This function is called by the state when a parameter on the currently active
        brush has been changed. This triggers an invocation of the current brush, telling
        the brush that it has been called due to a parameter change with the parm_changed
        and parm_name parameters.
        """
    def onDraw(self, draw_handle: ViewerStateDrawKwargs) -> None:
        """
        Optionally override this function to handle drawing guides for brushes.
        """
    def onDrawText(self, draw_handle: object) -> None:
        """
        Optionally override this function to handle drawing text for brushes.
        """
    def strokeData(self) -> hou.Geometry | None:
        '''
        This function should return the geometry data needed to restore the current stroke
        if "Apply to last stroke" option is enabled in the state. It is called when the state
        decides to end a stroke.
        '''
    def setStrokeData(self, strokeData: hou.Geometry | None) -> None:
        """
        This function is called when the state needs to restore the previous stroke to apply
        some parameter changes to the previous stroke. The strokeData parameter is the same
        data that is returned in self.strokeData().
        """

def registerBrushInterface(id: str, defn: Callable[[], BrushInterface]) -> None: ...
def build(id: str) -> BrushInterface: ...
def loadPlugins() -> None: ...
