# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import pxr.Gf as Gf
import pxr.Sdf as Sdf
import typing
from _typeshed import Incomplete
from pxr.Usdviewq.customAttributes import BoundingBoxAttribute as BoundingBoxAttribute, ComputedPropertyFactory as ComputedPropertyFactory, ComputedPropertyNames as ComputedPropertyNames, LocalToWorldXformAttribute as LocalToWorldXformAttribute
from typing import Callable, ClassVar

ALL_INSTANCES: int

class Blocker:
    """Object which can be used to temporarily block the execution of a body of
    code. This object is a context manager, and enters a 'blocked' state when
    used in a 'with' statement. The 'blocked()' method can be used to find if
    the Blocker is in this 'blocked' state.
    """
    def __init__(self, exitCallback: Callable = ...) -> None: ...
    def blocked(self):
        """Returns True if in the 'blocked' state, and False otherwise."""
    def __enter__(self):
        """Enter the 'blocked' state until the context is exited."""
    def __exit__(self, *args):
        """Exit the 'blocked' state."""

class SelectionDataModel(PySide6.QtCore.QObject):
    signalComputedPropSelectionChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalPrimSelectionChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalPropSelectionChanged: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, rootDataModel, _computedPropFactory: Incomplete | None = ...) -> None: ...
    def _buildPropPath(self, primPath, propName):
        """Build a new property path from a prim path and a property name."""
    def _computedPropSelectionChanged(self):
        """Should be called whenever a change is made to _computedPropSelection.
        """
    def _ensureValidPrimPath(self, path):
        """Validate an input path. If it is a string path, convert it to an
                Sdf.Path object.
        """
    def _ensureValidPropPath(self, prop):
        """Validate a property."""
    def _ensureValidTargetPath(self, targetPath):
        """Validate a property target or connection."""
    def _getComputedPropFromPath(self, primPath, propName):
        """Get a CustomAttribute object from a prim path and property name.
                Raise an error if the property name does not match any known
                CustomAttribute.
        """
    def _getPropFromPath(self, path):
        """Get a Usd property object from a property path."""
    def _getTargetFromPath(self, path):
        """Get the Usd object from a target path. It can be either a Usd prim or
                Usd property.
        """
    def _primSelectionChanged(self, emitSelChangedSignal: bool = ...):
        """Should be called whenever a change is made to _primSelection. Some
                final work is done then the prim selection changed signal is emitted.
        """
    def _propSelectionChanged(self):
        """Should be called whenever a change is made to _propSelection."""
    def _requireNotBatchingComputedProps(self):
        """Raise an error if we are currently batching prop selection changes.
                We don't want to allow reading prop selection state in the middle of a
                batch.
        """
    def _requireNotBatchingPrims(self):
        """Raise an error if we are currently batching prim selection changes.
                We don't want to allow reading prim selection state in the middle of a
                batch.
        """
    def _requireNotBatchingProps(self):
        """Raise an error if we are currently batching prop selection changes.
                We don't want to allow reading prop selection state in the middle of a
                batch.
        """
    def _switchProps(self, fromPrimPath, toPrimPath):
        '''Switch all selected properties from one prim to another. Only do this
                if all properties currently belong to the "from" prim.
        '''
    def _validateComputedPropName(self, propName):
        """Validate a computed property name."""
    def _validateInstanceIndexParameter(self, instance):
        """Validate an instance used as a parameter. This can be any positive
                int or ALL_INSTANCES."""
    def addComputedProp(self, prop):
        """Add a computed property to the selection."""
    def addComputedPropPath(self, primPath, propName):
        """Add a computed property to the selection."""
    def addPrim(self, prim, instance: int = ...):
        """Add a prim's path to the path selection. If an instance is given,
                only add that instance.
        """
    def addPrimPath(self, path, instance: int = ...):
        """Add a path to the path selection. If an instance is given, only add
                that instance.
        """
    def addProp(self, prop):
        """Add a property to the selection."""
    def addPropPath(self, path):
        """Add a property to the selection."""
    def addPropTarget(self, prop, target):
        """Select a property's target or connection."""
    def addPropTargetPath(self, path, targetPath):
        """Select a property's target or connection."""
    def clear(self):
        """Clear all selections."""
    def clearComputedProps(self):
        """Clear the computed property selection."""
    def clearPoint(self): ...
    def clearPrims(self):
        """Clear the prim selection (same as path selection)."""
    def clearProps(self):
        """Clear the property selection."""
    def getComputedPropPaths(self):
        """Get a list of all selected computed properties."""
    def getComputedProps(self):
        """Get a list of all selected computed properties."""
    def getFocusComputedProp(self):
        """Get the focus computed property from the property selection."""
    def getFocusComputedPropPath(self):
        """Get the focus computed property from the property selection."""
    def getFocusPrim(self):
        """Get the prim whose path is currently in focus."""
    def getFocusPrimPath(self):
        """Get the path currently in focus."""
    def getFocusProp(self):
        """Get the focus property from the property selection."""
    def getFocusPropPath(self):
        """Get the focus property from the property selection."""
    def getLCDPaths(self):
        '''Get a list of paths from the selection who do not have an ancestor
                that is also in the selection. The "Least Common Denominator" paths.
        '''
    def getLCDPrims(self):
        '''Get a list of prims whose paths are both selected and do not have an
                ancestor that is also in the selection. The "Least Common Denominator"
                prims.
        '''
    def getPoint(self): ...
    def getPrimInstances(self):
        """Get a dictionary which maps each prim whose path is selected to a set
                of its selected instances. If all of a path's instances are selected,
                the value is ALL_INSTANCES rather than a set.
        """
    def getPrimPathInstances(self):
        """Get a dictionary which maps each selected prim to a set of its
                selected instances. If all of a path's instances are selected, the value
                is ALL_INSTANCES rather than a set.
        """
    def getPrimPaths(self):
        """Get a list of all selected paths."""
    def getPrims(self):
        """Get a list of all prims whose paths are selected."""
    def getPropPaths(self):
        """Get a list of all selected properties."""
    def getPropTargetPaths(self):
        """Get a dictionary which maps selected properties to a set of their
                selected targets or connections.
        """
    def getPropTargets(self):
        """Get a dictionary which maps selected properties to a set of their
                selected targets or connections.
        """
    def getProps(self):
        """Get a list of all selected properties."""
    def removeAbstractPrims(self):
        """Remove all abstract prims"""
    def removeComputedProp(self, prop):
        """Remove a computed property from the selection."""
    def removeComputedPropPath(self, primPath, propName):
        """Remove a computed property from the selection."""
    def removeInactivePrims(self):
        """Remove all inactive prims"""
    def removePrim(self, prim, instance: int = ...):
        """Remove a prim from the prim selection. If an instance is given, only
                remove that instance. If the target does not exist in the selection, do
                nothing.
        """
    def removePrimPath(self, path, instance: int = ...):
        """Remove a path from the path selection. If an instance is given, only
                remove that instance. If the target does not exist in the selection, do
                nothing.
        """
    def removeProp(self, prop):
        """Remove a property from the selection."""
    def removePropPath(self, path):
        """Remove a property from the selection."""
    def removePropTarget(self, prop, target):
        """Deselect a property's target or connection."""
    def removePropTargetPath(self, path, targetPath):
        """Deselect a property's target or connection."""
    def removePrototypePrims(self):
        """Remove all prototype prims"""
    def removeUndefinedPrims(self):
        """Remove all undefined prims"""
    def removeUnpopulatedPrims(self):
        """Remove all prim paths whose corresponding prims do not currently
                exist on the stage.  It is the application's responsibility to
                call this method while it is processing changes to the stage,
                *before* querying this object for selections.  Because this is a
                synchronization operation rather than an expression of GUI state
                change, it does *not* perform any notifications/signals, which could
                cause reentrant application change processing."""
    def setComputedProp(self, prop):
        """Clear the computed property selection, then add a single computed
                property back to the selection.
        """
    def setComputedPropPath(self, primPath, propName):
        """Clear the computed property selection, then add a single computed
                property path back to the selection.
        """
    def setPoint(self, point): ...
    def setPrim(self, prim, instance: int = ...):
        """Clear the prim selection then add a single prim back to the
                selection. If an instance is given, only add that instance.
        """
    def setPrimPath(self, path, instance: int = ...):
        """Clear the prim selection then add a single prim path back to the
                selection. If an instance is given, only add that instance.
        """
    def setProp(self, prop):
        """Clear the property selection, then add a single property back to the
                selection.
        """
    def setPropPath(self, path):
        """Clear the property selection, then add a single property path back to
                the selection.
        """
    def setPropTarget(self, prop, target):
        """Clear the property selection, then add a single property back to the
                selection with a target.
        """
    def setPropTargetPath(self, path, targetPath):
        """Clear the property selection, then add a single property path back to
                the selection with a target.
        """
    def switchToPrim(self, prim, instance: int = ...):
        """Select only the given prim. If only a single prim was selected before
                and all selected properties belong to this prim, select the
                corresponding properties on the new prim instead.
        """
    def switchToPrimPath(self, path, instance: int = ...):
        """Select only the given prim path. If only a single prim was selected
                before and all selected properties belong to this prim, select the
                corresponding properties on the new prim instead. If an instance is
                given, only select that instance.
        """
    def togglePrim(self, prim, instance: int = ...):
        """Toggle a prim's path in the path selection. If an instance is given,
                only that instance is toggled.
        """
    def togglePrimPath(self, path, instance: int = ...):
        """Toggle a path in the path selection. If an instance is given, only
                that instance is toggled.
        """

class _PrimSelection:
    """This class keeps track of the core data for prim selection: paths and
    instances. The methods here can be called in any order required without
    corrupting the path selection state.
    """
    def __init__(self) -> None: ...
    def _allInstancesSelected(self, path):
        """Returns True if all instances of a specified path are selected and
                False otherwise.
        """
    def _clearPrimPath(self, path):
        """Clears a path from the selection and updates the diff."""
    def _discardInstance(self, path, instance):
        """Discards an instance from the selection, then deletes the path from
                the selection if it has no more instances.
        """
    def _noInstancesSelected(self, path):
        """Returns True if all instances of a specified path are selected and
                False otherwise.
        """
    def addPrimPath(self, path, instance: int = ...):
        """Add a path to the selection. If an instance is given, then only add
                that instance. If all instances are selected when this happens then the
                single instance will become the only selected one.
        """
    def clear(self):
        """Clear the path selection."""
    def getDiff(self) -> typing.Any: ...
    def getPrimPathInstances(self):
        """Get the full selection of paths and their corresponding selected
                instances.
        """
    def getPrimPaths(self):
        """Get a list of paths that are at least partially selected."""
    def removeMatchingPaths(self, matches):
        """Remove any paths that pass the given predicate"""
    def removePrimPath(self, path, instance: int = ...):
        """Remove a path from the selection. If an instance is given, then only
                remove that instance. If all instances are selected when this happens,
                deselect all instances. If the target does not exist in the selection,
                do nothing.
        """
    def togglePrimPath(self, path, instance: int = ...):
        """Toggle the selection of a path. If an instance is given, only toggle
                that instance's selection.
        """

class _PropSelection:
    """This class keeps track of the state of property selection."""
    def __init__(self) -> None: ...
    def addPropPath(self, primPath, propName):
        """Add a property to the selection."""
    def addTarget(self, primPath, propName, target):
        """Add a target to the selection. Also add the target's property if it
                is not already in the selection.
        """
    def clear(self):
        """Clears the property selection."""
    def getPropPaths(self):
        """Get the list of properties."""
    def getTargets(self):
        """Get a dictionary which maps selected properties to a set of their
                selected targets or connections.
        """
    def removePropPath(self, primPath, propName):
        """Remove a property from the selection."""
    def removeTarget(self, primPath, propName, target):
        """Remove a target from the selection. If the target or its property are
                not already in the selection, nothing is changed.
        """
