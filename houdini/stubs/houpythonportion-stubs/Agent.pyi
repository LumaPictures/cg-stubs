# Houdini stubs generated from Houdini 22.0.466

import hou

def rig(self: hou.Agent) -> hou.AgentRig:
    """
rig(self) -> hou.AgentRig

    Returns the agent's rig. This is equivalent to definition().rig().

"""
def shapeLibrary(self: hou.Agent) -> hou.AgentShapeLibrary:
    """
shapeLibrary(self) -> hou.AgentShapeLibrary

    Returns the agent's shape library. This is equivalent to
    definition().shapeLibrary().

"""
def layers(self: hou.Agent) -> tuple[hou.AgentLayer, ...]:
    """
layers(self) -> tuple of hou.AgentLayer

    Returns all of the layers that are available. This is equivalent to
    definition().layers().

"""
def clipCatalog(self: hou.Agent) -> tuple[hou.AgentClip, ...]:
    """
clipCatalog(self) -> tuple of hou.AgentClip

    Returns all of the animation clips that are available. This is
    equivalent to definition().clips().

"""
