import hou

def isExternalReference(self: hou.AgentRig) -> bool:
    """
isExternalReference(self) -> bool

    Returns a bool indicating whether the rig references a file on disk.

"""
def transformNames(self: hou.AgentRig) -> list[str]:
    """
transformNames(self) -> tuple of str

    Returns a list of the transform names in the rig.

"""
def transformHierarchy(self: hou.AgentRig) -> list[tuple[int, ...]]:
    """
transformHierarchy(self) -> tuple of tuple of int

    Returns a list of the child indices for each transform in the rig.

"""
