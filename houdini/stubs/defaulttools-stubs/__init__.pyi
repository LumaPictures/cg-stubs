import hou
import toolutils
from collections.abc import Callable as Callable, Container, Sequence

def objHasScales(obj: hou.ObjNode) -> bool:
    """ Determines if an Object Node has any scales or shears up to 
        a tolerance.
    """
def calculateBoundingBox(obj: hou.ObjNode | hou.SopNode, exclude_node_list: Container[hou.Node] | None = None, include_nondisplayed: bool = False) -> tuple[bool, hou.BoundingBox]:
    """ Calculates a bounding box for a given object. The bounding box is used
        in the viewer to indicate the size of a object when it is being
        positioned on the construction plane prior to instantiating the object.
    """
def bboxString(minvec: Sequence[float] | hou.Vector3, maxvec: Sequence[float] | hou.Vector3) -> str: ...
def createDefaultNodeTypeToolScript(nodetype: hou.NodeType, toolfile: str, usebbox: bool = True) -> str:
    """Each tool has a python script that is executed when the tool is invoked.
    This function returns a string that represents a python script that should
    be executed when a user invokes a default tool for the given node type. The
    toolfile specifies the utility python module file that should be used by
    the returned script (such as 'objecttoolutils'). 
    """
def addRopNodeTypeKeywords(nodetype: hou.NodeType, keywords: tuple[str, ...]) -> tuple[str, ...]: ...
def addShopNodeTypeLocationsAndKeywords(nodetype: hou.NodeType, locations: tuple[str, ...], keywords: tuple[str, ...]) -> tuple[tuple[str, ...], tuple[str, ...]]: ...
def getSceneViewerCategories(nodetype: hou.NodeType) -> tuple[hou.NodeTypeCategory, ...]:
    """ Obtains a list of type categories (network types such as OBJ, SOP, etc).
        The shelf tool corresponding to a given nodetype will appear in the TAB
        menu if the scene viewer pane path points to a network whose type
        can be found in the list.
    """
def getCop2ViewerCategories(nodetype: hou.NodeType) -> tuple[hou.NodeTypeCategory, ...]:
    """ Obtains a list of type categories (network types such as OBJ, SOP, etc).
        The shelf tool corresponding to a given nodetype will appear in the TAB
        menu if the compositor viewer pane path points to a network whose type
        can be found in the list.
    """
def getNetworkOpTypeOrCategories(nodetype: hou.NodeType) -> tuple[str, tuple[hou.NodeTypeCategory, ...]]:
    """ Obtains an op_type string (may be empty) if the tool should appear in
        contexts in which the operator does. Or, if op_type string is empty,
        a list of type categories (network types such as OBJ, SOP, etc). 
        The shelf tool corresponding to a given nodetype will appear in the TAB
        menu if the network editor pane path points to a network that admits the
        opertor (if the returned type name string not empty) or whose type 
        can be found in the returned list.
    """
def createDefaultHDATool(shelffile: str, nodetype: hou.NodeType, toolname: str, usebbox: bool = True, locations: tuple[str, ...] = ('Digital Assets',)) -> hou.Tool:
    """Creates a default shelf tool for a given asset (identified by nodetype).
    The tool is given a specified name and is saved to the shelf file on the
    file system.
    """
def setHDAToolVariables(tool: hou.Tool, hdadef: hou.HDADefinition) -> None:
    """Sets the variables that evaluate to an asset-dependent values. The
    advantage of using variables is that copying or relabeling the asset does
    not invalidate the tool. If, instead, asset-specific values were used in
    the tool, then if the asset changes, the tool may not match the asset
    parameters (such as name, and label).

    This function replaces the hard-coded values with variable names within the
    tool.
    """
def createDefaultHDAToolsForOTL(otlfile: str, delete_old_tool_section: bool = False) -> None:
    """Generates a default shelf tool for each of the digital assets saved in a
    given otlfile, and saves the tool as part of the asset back in the otlfile.
    """
def createDefaultNodeTypeTool(shelffile: str, nodetype: hou.OpNodeType) -> None:
    """ Generates a default shelf tool for a given operator and saves it into
        a given file name. 
    """
def createDefaultNodeTypeToolsForCategory(shelfdir: str, nodetypecategory: hou.OpNodeTypeCategory) -> None:
    """ Generates default shelf tools for all the operator types that exist
        within a given nodetypecategory (i.e., OBJ, SOP, etc.). All these
        tools are saved into a file that corresponds to the category name and
        that is saved in a given directory.
    """
def createDefaultNodeTypeTools(shelfdir: str) -> None:
    """ Generates all the shelf tools that correspond to various operator types.
        The operators are grouped according to the type categories (ie,
        network types, such as OBJ, SOP), and the tools for operators in
        all such categories are generated and saved in corresponding files
        within the given shelf dir.
        The shelf tools that get generated usually instantiate the node to
        which the tool corresponds. And each node has one such tool.  These
        tools can be invoked from the top level shelf or from the TAB menus.

        Most of the native operators (and states) have a
        corresponding default tool generated automatically. The rest have a more
        complicated hand-crafted tools written for them. Such tools are stored
        in a shelf file. But, each operator needs to have a corresponding tool,
        because it is the only way to instantiate an operator/state in the GUI
        (though, the hscript or python could be used to create nodes too).
        This function generates all the default tools for all the operators
        that don't have a corresponding hand-crafted tool (or other tool that
        has been already loaded into Houdini).
    """
def defaultPythonLopCode() -> str:
    """Return the Python code for the PythonCook section of a newly created
    Python LOP.
    """
def defaultPythonSopCode() -> str:
    """Return the Python code for the PythonCook section of a newly created
    Python SOP.
    """
def defaultPythonObjectCode() -> str:
    """Return the Python code for the PythonCook section of a newly created
    Python Object.
    """
def defaultPythonCop2GeneratorCode() -> str:
    """Return the Python code for the PythonCook section of a newly created
    Python COP generator.
    """
def defaultPythonCop2FilterCode() -> str:
    """Return the Python code for the PythonCook section of a newly created
    Python COP filter.
    """
def defaultPythonDopCode() -> str:
    """Return the Python code for the PythonCook section of a newly created
    Python DOP.
    """
def defaultPythonDopSolverBoilerplate() -> str:
    """ Returns the boiler plate needed for solveForObjects() to be
        prepended.
        NOTE: This is used by the Script Solver in $SIMZ so do not
        change without taking that into consideration!
    """
def defaultPythonDopSolverPrequel() -> str:
    """Return the solveForObjects() example for Python DOP solvers.
    """
def defaultPythonDopSolverCode() -> str:
    """Return the Python code for the PythonCook section of a newly created
    Python DOP solver.
    """

theShaderTypeLocations: dict[hou.EnumValue[hou.shaderType], str]
theRendererKeywords: dict[str, str]
theSopNoObjSelection: list[str]
theSopBothObjAndSopNetContexts: list[str]
theSopObjSopAndLopNetContexts: list[str]
theSopObjSopAndLopViewerContexts: list[str]
theSopBothObjAndSopViewerContexts: list[str]

def lsystemAdjustOrientation(nodename: str) -> str: ...

theOrientationOverrides: dict[str, toolutils.OrientInfo | Callable[[str], str]]
