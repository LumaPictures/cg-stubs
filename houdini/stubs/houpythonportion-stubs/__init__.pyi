from houpythonportion.Agent import *
from houpythonportion.AgentClip import *
from houpythonportion.AgentLayer import *
from houpythonportion.AgentMetadata import *
from houpythonportion.AgentRig import *
from houpythonportion.AgentShape import *
from houpythonportion.AgentShapeBinding import *
from houpythonportion.AgentShapeLibrary import *
from houpythonportion.AgentTransformGroup import *
from houpythonportion.clone import *
from houpythonportion.CompositorViewer import *
from houpythonportion.CompositorViewerEvent import *
from houpythonportion.EdgeGroup import *
from houpythonportion.FloatingPanel import *
from houpythonportion.Geometry import *
from houpythonportion.hda import *
from houpythonportion.HDADefinition import *
from houpythonportion.HDASection import *
from houpythonportion.ik import *
from houpythonportion.Keyframe import *
from houpythonportion.logging import *
from houpythonportion.lop import *
from houpythonportion.NetworkDot import *
from houpythonportion.NetworkEditor import *
from houpythonportion.NetworkMovableItem import *
from houpythonportion.Node import *
from houpythonportion.ObjNode import *
from houpythonportion.OpNode import *
from houpythonportion.Pane import *
from houpythonportion.PaneTab import *
from houpythonportion.Parm import *
from houpythonportion.ParameterEditor import *
from houpythonportion.ParmTuple import *
from houpythonportion.ParmTemplate import *
from houpythonportion.PerfMonProfile import *
from houpythonportion.Point import *
from houpythonportion.PointGroup import *
from houpythonportion.Prim import *
from houpythonportion.PrimGroup import *
from houpythonportion.SceneViewer import *
from houpythonportion.SopNode import *
from houpythonportion.StringKeyframe import *
from houpythonportion.TopNode import *
from houpythonportion.VertexGroup import *
from houpythonportion.data import *
from houpythonportion.hipFile import *
import hou

def clipInfo(data: bytes, binary: bool = True, blosc_compressed: bool = True) -> dict[str, str | list[str]]:
    '''
hou.clipInfo

USAGE
  clipInfo(data, binary=True, blosc_compressed=True) -> dict

Returns a dictionary with information about the clip specified by
<data>. The returned dictionary contains the following keys:

  * "start" -> the start frame in the clip

  * "length" -> the clip length

  * "rate" -> the clip\'s sample rate

  * "tracks" -> a list of the track names in the clip

All values in the returned dictionary are strings (or list of strings
for "tracks").

<binary> and <blosc_compressed> specify the format of the given <data>.

  * If <binary> is True, the given data is binary clip data otherwise it
    is plain text (ASCII) clip data.

  * If <blosc_compressed> is True, the given data is blosc compressed
    binary clip data. This cannot be used with ASCII clip data.

The data must be a bytes object in Python 3 and a str object in Python
2. See HOM binary data for more information.

Raises a hou.InvalidInput exception if binary = False and
blosc_compressed = True.

Raises a hou.OperationFailed exception if the given <data> is invalid.

'''
def encode(str_value: str) -> str: ...
def decode(str_value: str) -> str: ...
def expandString(str_value: str) -> str: ...
def expandStringAtFrame(str_value: str, frame: float) -> str: ...
def hscriptExpandString(str_value: str) -> str: ...
def incrementNumberedString(str_value: str) -> str: ...
def assertTrue(true_or_false: object) -> None:
    """If true_or_false evaluates to True, then no-op.

    Otherwise:
    - If UT_ASSERTs are enabled, spawn a debug dialog.
    - If the env variable to enable hom asserts is set, then raise an
      AssertionError.

    """
def thirdPartyLibraryVersions() -> dict[str, dict[str, str]]: ...
def sceneFileExtension(license: hou.EnumValue[hou.licenseCategoryType] | None = None) -> str: ...
