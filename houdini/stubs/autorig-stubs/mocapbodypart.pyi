import hou
import types

class MocapBodyPart:
    """ Create an object that stores data for a Mocap body part asset.

        A MocapBodyPart stores links to Houdini assets, parameters,
        and series of position and control mappings.
    """
    typename: str
    mocappart: hou.OpNode | None
    partname: str
    otherpart: hou.OpNode
    partmapping: types.ModuleType
    maplocations: list[str]
    parameters: list[str]
    useend: bool
    customtwist: tuple[bool, *tuple[str, ...]]
    autocontrols: list[str]
    animcontrols: list[str]
    pretransforms: list[str]
    animchannels: list[tuple[str, str]]
    autosetupskip: bool
    extrapositions: list[tuple[str, str, tuple[int, int, int]]]
    mappoints: list[str]
    parm_names: list[str]
    bonelengths: list[float]
    def __init__(self, parttype: str, mocappart: hou.OpNode | None = None, otherpart: hou.OpNode | None = None) -> None:
        """ Creates a MocapBodyPart object.

            Creates a MocapBodyPart object of a specific type.

            mocappart and otherpart are optional links to
            digital assets that can be used with a Mocap object.
        """
    def name(self) -> str:
        """ Return the name of the body part."""
    def type(self) -> str:
        """ Return the type of the object as a string."""
    def otherPart(self) -> hou.OpNode:
        """ Return an object representing the corresponding animation
            rig node.
        """
    def mocapPart(self) -> hou.OpNode | None:
        """ Return an object representing the physical mocap rig node."""
    def initializeRootMap(self, point: str) -> None:
        """ Take a point string and insert it to be the first map point
            and add the 'root' map location to the list.
        """
    def mapLocations(self) -> list[str]:
        """ Return a list of the map locations."""
    def insertMapLocation(self, toadd: str, index: int) -> None:
        """ Insert a location into the list of Map Locations at a 
            specific position.
        """
    def resetMapLocations(self) -> None:
        """ Set the Map Locations back to the default values for this
            type of mocap object.
        """
    def setMapPoints(self, points: list[str]) -> None:
        """ Set the Map Points to a list of specified locations."""
    def addMapPoint(self, point: str) -> None:
        """ Add a single map point to the list."""
    def insertMapPoint(self, index: int, point: str) -> None:
        """ Insert a single map point into the list at a specific
            location.
        """
    def mapPoints(self) -> list[str]:
        """Return the list of Map Points."""
    def modifyMapPoint(self, index: int, point: str) -> None:
        """ Change a Map Point in place."""
    def autoControls(self) -> list[str]:
        """ Returns a list of auto rig control object names."""
    def animControls(self) -> list[str]:
        """ Returns a list of animation rig control object names."""
    def setParmNames(self, parms: list[str]) -> None:
        """ Set the list of parm names."""
    def parmNames(self) -> list[str]:
        """ Returns a list of parameter names."""
    def addLength(self, length: float) -> None:
        """ Add a length to the list of bone lengths."""
    def lengths(self) -> list[float]:
        """ Returns the list of bone lengths."""
    def channels(self) -> list[tuple[str, str]]:
        """ Get the list of corresponding animation channels."""
    def parms(self) -> list[str]:
        """ Returns the list of parameters."""
    def useEnd(self) -> bool:
        """ Returns whether a part uses End."""
    def useTwist(self) -> bool:
        """ Returns whether a part uses a custom twist."""
    def twistTarget(self) -> str:
        """ Returns a parts custom twist target."""
    def twistExtra(self) -> str:
        """ Returns an objects extra twist information."""
    def setPretransforms(self) -> None:
        """ Set the pretransforms of the mocap body part to the 
            positions of the controls from the corresponding auto 
            rig part.
        """
    def skipFirstMap(self) -> bool:
        """ Returns wether a node should skip the first map point."""
    def extraPositions(self) -> list[tuple[str, str, tuple[int, int, int]]]:
        """ Returns a nodes extra position locations."""
