# Houdini stubs generated from Houdini 22.0.466

import _pdgd
from collections.abc import Sequence, Set as AbstractSet
from pdg.callback import PythonCallback

class PyDataLayerBackend(PythonCallback):
    """
    Base class for backends implemented in Python
    """
    def __init__(self, backend: _pdgd.DataBackend) -> None:
        """
        __init__(self, _pdgd.DataBackend) -> NoneType
        """
    def hasObject(self, path: str) -> bool:
        """
        hasObject(self, str) -> bool

        [virtual] returns if an object exists for the given path
        """
    def storeObject(self, path: str, snapshot: _pdgd.ObjectSnapshot) -> None:
        """
        storeObject(self, str, _pdgd.ObjectSnapshot) -> NoneType

        [virtual] stores an object under the given path
        """
    def loadObject(self, path: str) -> _pdgd.ObjectSnapshot:
        """
        loadObject(self, str) -> _pdgd.ObjectSnapshot

        [virtual] returns a snapshot describing the object stored under path
        """
    def renameObject(self, path: str, newPath: str) -> None:
        """
        renameObject(self, str, str) -> NoneType

        [virtual] moves an object from path to newPath
        """
    def removeObject(self, path: str) -> None:
        """
        removeObject(self, str) -> NoneType

        [virtual] Removes the object under the given path
        """
    def setProperty(self, path: str, propName: str, propValue: _pdgd.ObjectProperty) -> None:
        """
        setProperty(self, str, str, _pdgd.ObjectProperty) -> NoneType

        [virtual] Adds or replaces a property using propValue
        """
    def setPropertyValues(self, path: str, propName: str, propArray: Sequence[_pdgd.ObjectProperty]) -> None:
        """
        setPropertyValues(self, str, str, list) -> NoneType

        [virtual] Replaces the property values with the values from propArray
        """
    def setPropertyValuesSet(self, path: str, propName: str, propSet: AbstractSet[_pdgd.ObjectProperty]) -> None:
        """
        setPropertyValuesSet(self, str, str, set) -> NoneType

        [virtual] Replaces the property values with the values from propSet
        """
    def appendPropertyValue(self, path: str, propName: str, prop: _pdgd.ObjectProperty) -> None:
        """
        appendPropertyValue(self, str, str, propArray) -> NoneType

        [virtual] Appends the property value to a property
        """
    def appendPropertyValues(self, path: str, propName: str, propArray: Sequence[_pdgd.ObjectProperty]) -> None:
        """
        appendPropertyValues(self, str, str, propArray) -> NoneType

        [virtual] Appends the values from propArray to a property
        """
    def removePropertyValueAtIndex(self, path: str, propName: str, index: int) -> None:
        """
        removePropertyValueAtIndex(self, str, str, int) -> NoneType

        [virtual] Remove from the property the value at the given index
        """
    def removePropertyValues(self, path: str, propName: str, propArray: Sequence[_pdgd.ObjectProperty]) -> None:
        """
        removePropertyValues(self, str, str, list) -> NoneType

        [virtual] Removes property values matching any of the values in propArray
        """
    def removeProperty(self, path: str, propName: str) -> None:
        """
        removeProperty(self, str, str) -> NoneType

        [virtual] Removes a property from an object
        """
    def queryObjects(self, queryDefinition: _pdgd.QueryDefinition) -> _pdgd.DataBackendQueryResults:
        """
        queryObjects(self, _pdgd.QueryDefinition) -> _pdgd.DataBackendQueryResults

        [virtual] Performs an object query
        """
    def toJson(self) -> str:
        """
        toJson(self) -> str
        
        Returns a json representation of the entire data backend
        """
