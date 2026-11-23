import hou

def getInsertionPointNode(cwd: hou.LopNetwork | hou.LopNode) -> hou.OpNode | None:
    """
        Returns the node for the currently set insertion point.
        If we cannot find the currently set insertion point, then
        it returns None.
        cwd: A hou.LopNetwork or a hou.LopNode inside a hou.LopNetwork.
    """
def getInsertionPoint(cwd: hou.LopNetwork | hou.LopNode) -> str | None:
    """
        Returns the name of the currently set insertion point.
        cwd: A hou.LopNetwork or a hou.LopNode inside a hou.LopNetwork.
    """
def setInsertionPoint(cwd: hou.LopNetwork | hou.LopNode, in_point: str) -> None:
    """
        Function to set the current insertion point if possible.
        cwd: A hou.LopNetwork or a hou.LopNode inside a hou.LopNetwork.
        in_point: String name of insertion point or full path of insertion
        point.
    """
def clearInsertionPoint(cwd: hou.LopNetwork | hou.LopNode) -> None:
    """
        Clears the current insertion point.
        cwd: A hou.LopNetwork or a hou.LopNode inside a hou.LopNetwork.
    """
def getNamesListSorted(include_path: bool = False) -> list[str]:
    """
        Returns sorted list of unique insertion point names in the network.
    """
def getVisibleNameListSorted(cwd: hou.LopNode | hou.LopNetwork) -> list[str]:
    """
        Returns list of insertion point names along the cook path.
        cwd : A hou.LopNode in a hou.LopNetwork.
    """
def getAllNamesList(cwd: hou.LopNode | hou.LopNetwork) -> list[str]: ...
def createExistingNamesMenu() -> list[str]:
    """
        Returns dropdown menu formatted list of unique existing
        insertion point names.
    """
