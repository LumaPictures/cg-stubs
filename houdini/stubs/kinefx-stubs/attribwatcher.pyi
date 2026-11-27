import hou
from collections.abc import Iterable

class AttributeWatcher:
    """
    Stores specified geometry attribute data ids and provides methods for determining whether they have changed or not.
    Useful for determining when a geometry has changed. 
    """
    attribute_list: list[str]
    def __init__(self) -> None:
        """
        Constructor method.
        """
    def getDataIds(self, geo: hou.Geometry | None) -> list[hou.AttribDataId | None]:
        """
        Get the **geo** attribute ids for the attributes that have an added interest(see `addInterests`).

        :parm geo: geometry to get the attribute data ids from
        :type geo: hou.Geometry
        :return: attribute ids
        :rtype: list of hou.AttribDataId
        .. note::
            If **geo** is not valid, returns a list of None.
            The length of this list is the same as the number of attributes that have an added interest.
        """
    def updateDataIds(self, geo: hou.Geometry | None = None) -> bool:
        """
        Update the stored attribute data ids from the passed in **geo**.

        :parm geo: geometry to update the attribute data ids from
        :type geo: hou.Geometry
        :return: whether the data ids have been updated or not
        :rtype: bool
        """
    def addInterests(self, attributes: Iterable[str]) -> None:
        """
        Choose which attribute data ids to track.

        :param attributes: name of the attributes which to track
        :type attributes: list or tuple of str
        """
    def setDirty(self) -> None:
        """
        Set the current data id cache to `dirty`.
        """
    def isDirty(self) -> bool:
        """
        Check if the current data id cache has run out of sync with the attribute data ids from the stored geometry.
        The stored geometry gets set in **updateDataIds**.

        :return: whether the current data cache is in sync with the attribute data ids from the stored geometry or not
        :rtype: bool
        """
    def compareDataIds(self, geo: hou.Geometry | None) -> bool:
        """
        Compare the current data id cache with the attribute data ids from **geo**.

        :param geo: geometry to extract the attribute data ids and compare them with the current data cache
        :type geo: hou.Geometry
        :return: whether the current data cache is in sync with the attribute data ids from **geo** or not
        :rtype: bool
        """
