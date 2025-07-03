from .customAttributes import BoundingBoxAttribute as BoundingBoxAttribute, ComputedPropertyFactory as ComputedPropertyFactory, ComputedPropertyNames as ComputedPropertyNames, LocalToWorldXformAttribute as LocalToWorldXformAttribute
from .qt import QtCore as QtCore
from _typeshed import Incomplete
from pxr import Gf as Gf, Sdf as Sdf

ALL_INSTANCES: int

class Blocker:
    """Object which can be used to temporarily block the execution of a body of
    code. This object is a context manager, and enters a 'blocked' state when
    used in a 'with' statement. The 'blocked()' method can be used to find if
    the Blocker is in this 'blocked' state.
    """
    _count: int
    _exitCallback: Incomplete
    def __init__(self, exitCallback=...) -> None: ...
    def __enter__(self) -> None:
        """Enter the 'blocked' state until the context is exited."""
    def __exit__(self, *args) -> None:
        """Exit the 'blocked' state."""
    def blocked(self):
        """Returns True if in the 'blocked' state, and False otherwise."""

class _PrimSelection:
    """This class keeps track of the core data for prim selection: paths and
    instances. The methods here can be called in any order required without
    corrupting the path selection state.
    """
    _selection: Incomplete
    _added: Incomplete
    _removed: Incomplete
    def __init__(self) -> None: ...
    def _clearPrimPath(self, path) -> None:
        """Clears a path from the selection and updates the diff."""
    def _discardInstance(self, path, instance) -> None:
        """Discards an instance from the selection, then deletes the path from
        the selection if it has no more instances.
        """
    def _allInstancesSelected(self, path):
        """Returns True if all instances of a specified path are selected and
        False otherwise.
        """
    def _noInstancesSelected(self, path):
        """Returns True if all instances of a specified path are selected and
        False otherwise.
        """
    def clear(self) -> None:
        """Clear the path selection."""
    def removeMatchingPaths(self, matches) -> None:
        """Remove any paths that pass the given predicate"""
    def addPrimPath(self, path, instance=...) -> None:
        """Add a path to the selection. If an instance is given, then only add
        that instance. If all instances are selected when this happens then the
        single instance will become the only selected one.
        """
    def removePrimPath(self, path, instance=...) -> None:
        """Remove a path from the selection. If an instance is given, then only
        remove that instance. If all instances are selected when this happens,
        deselect all instances. If the target does not exist in the selection,
        do nothing.
        """
    def togglePrimPath(self, path, instance=...) -> None:
        """Toggle the selection of a path. If an instance is given, only toggle
        that instance's selection.
        """
    def getPrimPaths(self):
        """Get a list of paths that are at least partially selected."""
    def getPrimPathInstances(self):
        """Get the full selection of paths and their corresponding selected
        instances.
        """
    def getDiff(self):
        """Get the prims added to or removed from the selection since the last
        time getDiff() was called.
        """

class _PropSelection:
    """This class keeps track of the state of property selection."""
    _selection: Incomplete
    def __init__(self) -> None: ...
    def clear(self) -> None:
        """Clears the property selection."""
    def addPropPath(self, primPath, propName) -> None:
        """Add a property to the selection."""
    def removePropPath(self, primPath, propName) -> None:
        """Remove a property from the selection."""
    def addTarget(self, primPath, propName, target) -> None:
        """Add a target to the selection. Also add the target's property if it
        is not already in the selection.
        """
    def removeTarget(self, primPath, propName, target) -> None:
        """Remove a target from the selection. If the target or its property are
        not already in the selection, nothing is changed.
        """
    def getPropPaths(self):
        """Get the list of properties."""
    def getTargets(self):
        """Get a dictionary which maps selected properties to a set of their
        selected targets or connections.
        """

class SelectionDataModel(QtCore.QObject):
    """Data model managing the current selection of prims and properties.
    Please note that the owner of an instance of this class is
    responsible for calling SelectionDataModel.removeUnpopulatedPrims() when
    appropriate, lest methods like getPrims() return invalid prims."""
    signalPrimSelectionChanged: Incomplete
    signalPropSelectionChanged: Incomplete
    signalComputedPropSelectionChanged: Incomplete
    _rootDataModel: Incomplete
    _computedPropFactory: Incomplete
    batchPrimChanges: Incomplete
    batchPropChanges: Incomplete
    batchComputedPropChanges: Incomplete
    _pointSelection: Incomplete
    _primSelection: Incomplete
    _lcdPathSelection: Incomplete
    _propSelection: Incomplete
    _computedPropSelection: Incomplete
    def __init__(self, rootDataModel, _computedPropFactory: Incomplete | None = None) -> None: ...
    def _primSelectionChanged(self, emitSelChangedSignal: bool = True) -> None:
        """Should be called whenever a change is made to _primSelection. Some
        final work is done then the prim selection changed signal is emitted.
        """
    def _propSelectionChanged(self) -> None:
        """Should be called whenever a change is made to _propSelection."""
    def _computedPropSelectionChanged(self) -> None:
        """Should be called whenever a change is made to _computedPropSelection.
        """
    def _ensureValidPrimPath(self, path):
        """Validate an input path. If it is a string path, convert it to an
        Sdf.Path object.
        """
    def _validateInstanceIndexParameter(self, instance) -> None:
        """Validate an instance used as a parameter. This can be any positive
        int or ALL_INSTANCES."""
    def _ensureValidPropPath(self, prop):
        """Validate a property."""
    def _ensureValidTargetPath(self, targetPath):
        """Validate a property target or connection."""
    def _getPropFromPath(self, path):
        """Get a Usd property object from a property path."""
    def _getTargetFromPath(self, path):
        """Get the Usd object from a target path. It can be either a Usd prim or
        Usd property.
        """
    def _requireNotBatchingPrims(self) -> None:
        """Raise an error if we are currently batching prim selection changes.
        We don't want to allow reading prim selection state in the middle of a
        batch.
        """
    def _requireNotBatchingProps(self) -> None:
        """Raise an error if we are currently batching prop selection changes.
        We don't want to allow reading prop selection state in the middle of a
        batch.
        """
    def _getComputedPropFromPath(self, primPath, propName):
        """Get a CustomAttribute object from a prim path and property name.
        Raise an error if the property name does not match any known
        CustomAttribute.
        """
    def _requireNotBatchingComputedProps(self) -> None:
        """Raise an error if we are currently batching prop selection changes.
        We don't want to allow reading prop selection state in the middle of a
        batch.
        """
    def _buildPropPath(self, primPath, propName):
        """Build a new property path from a prim path and a property name."""
    def _validateComputedPropName(self, propName) -> None:
        """Validate a computed property name."""
    def _switchProps(self, fromPrimPath, toPrimPath) -> None:
        '''Switch all selected properties from one prim to another. Only do this
        if all properties currently belong to the "from" prim.
        '''
    def clear(self) -> None:
        """Clear all selections."""
    def clearPoint(self) -> None: ...
    def setPoint(self, point) -> None: ...
    def getPoint(self): ...
    def clearPrims(self) -> None:
        """Clear the prim selection (same as path selection)."""
    def addPrimPath(self, path, instance=...) -> None:
        """Add a path to the path selection. If an instance is given, only add
        that instance.
        """
    def removePrimPath(self, path, instance=...) -> None:
        """Remove a path from the path selection. If an instance is given, only
        remove that instance. If the target does not exist in the selection, do
        nothing.
        """
    def togglePrimPath(self, path, instance=...) -> None:
        """Toggle a path in the path selection. If an instance is given, only
        that instance is toggled.
        """
    def setPrimPath(self, path, instance=...) -> None:
        """Clear the prim selection then add a single prim path back to the
        selection. If an instance is given, only add that instance.
        """
    def getFocusPrimPath(self):
        """Get the path currently in focus."""
    def getPrimPaths(self):
        """Get a list of all selected paths."""
    def getLCDPaths(self):
        '''Get a list of paths from the selection who do not have an ancestor
        that is also in the selection. The "Least Common Denominator" paths.
        '''
    def getPrimPathInstances(self):
        """Get a dictionary which maps each selected prim to a set of its
        selected instances. If all of a path's instances are selected, the value
        is ALL_INSTANCES rather than a set.
        """
    def switchToPrimPath(self, path, instance=...) -> None:
        """Select only the given prim path. If only a single prim was selected
        before and all selected properties belong to this prim, select the
        corresponding properties on the new prim instead. If an instance is
        given, only select that instance.
        """
    def addPrim(self, prim, instance=...) -> None:
        """Add a prim's path to the path selection. If an instance is given,
        only add that instance.
        """
    def removePrim(self, prim, instance=...) -> None:
        """Remove a prim from the prim selection. If an instance is given, only
        remove that instance. If the target does not exist in the selection, do
        nothing.
        """
    def togglePrim(self, prim, instance=...) -> None:
        """Toggle a prim's path in the path selection. If an instance is given,
        only that instance is toggled.
        """
    def setPrim(self, prim, instance=...) -> None:
        """Clear the prim selection then add a single prim back to the
        selection. If an instance is given, only add that instance.
        """
    def getFocusPrim(self):
        """Get the prim whose path is currently in focus."""
    def getPrims(self):
        """Get a list of all prims whose paths are selected."""
    def getLCDPrims(self):
        '''Get a list of prims whose paths are both selected and do not have an
        ancestor that is also in the selection. The "Least Common Denominator"
        prims.
        '''
    def getPrimInstances(self):
        """Get a dictionary which maps each prim whose path is selected to a set
        of its selected instances. If all of a path's instances are selected,
        the value is ALL_INSTANCES rather than a set.
        """
    def switchToPrim(self, prim, instance=...) -> None:
        """Select only the given prim. If only a single prim was selected before
        and all selected properties belong to this prim, select the
        corresponding properties on the new prim instead.
        """
    def removeInactivePrims(self) -> None:
        """Remove all inactive prims"""
    def removePrototypePrims(self) -> None:
        """Remove all prototype prims"""
    def removeAbstractPrims(self) -> None:
        """Remove all abstract prims"""
    def removeUndefinedPrims(self) -> None:
        """Remove all undefined prims"""
    def removeUnpopulatedPrims(self):
        """Remove all prim paths whose corresponding prims do not currently
        exist on the stage.  It is the application's responsibility to
        call this method while it is processing changes to the stage,
        *before* querying this object for selections.  Because this is a
        synchronization operation rather than an expression of GUI state
        change, it does *not* perform any notifications/signals, which could
        cause reentrant application change processing."""
    def clearProps(self) -> None:
        """Clear the property selection."""
    def addPropPath(self, path) -> None:
        """Add a property to the selection."""
    def removePropPath(self, path) -> None:
        """Remove a property from the selection."""
    def setPropPath(self, path) -> None:
        """Clear the property selection, then add a single property path back to
        the selection.
        """
    def addPropTargetPath(self, path, targetPath) -> None:
        """Select a property's target or connection."""
    def removePropTargetPath(self, path, targetPath) -> None:
        """Deselect a property's target or connection."""
    def setPropTargetPath(self, path, targetPath) -> None:
        """Clear the property selection, then add a single property path back to
        the selection with a target.
        """
    def getFocusPropPath(self):
        """Get the focus property from the property selection."""
    def getPropPaths(self):
        """Get a list of all selected properties."""
    def getPropTargetPaths(self):
        """Get a dictionary which maps selected properties to a set of their
        selected targets or connections.
        """
    def addProp(self, prop) -> None:
        """Add a property to the selection."""
    def removeProp(self, prop) -> None:
        """Remove a property from the selection."""
    def setProp(self, prop) -> None:
        """Clear the property selection, then add a single property back to the
        selection.
        """
    def addPropTarget(self, prop, target) -> None:
        """Select a property's target or connection."""
    def removePropTarget(self, prop, target) -> None:
        """Deselect a property's target or connection."""
    def setPropTarget(self, prop, target) -> None:
        """Clear the property selection, then add a single property back to the
        selection with a target.
        """
    def getFocusProp(self):
        """Get the focus property from the property selection."""
    def getProps(self):
        """Get a list of all selected properties."""
    def getPropTargets(self):
        """Get a dictionary which maps selected properties to a set of their
        selected targets or connections.
        """
    def clearComputedProps(self) -> None:
        """Clear the computed property selection."""
    def addComputedPropPath(self, primPath, propName) -> None:
        """Add a computed property to the selection."""
    def removeComputedPropPath(self, primPath, propName) -> None:
        """Remove a computed property from the selection."""
    def setComputedPropPath(self, primPath, propName) -> None:
        """Clear the computed property selection, then add a single computed
        property path back to the selection.
        """
    def getFocusComputedPropPath(self):
        """Get the focus computed property from the property selection."""
    def getComputedPropPaths(self):
        """Get a list of all selected computed properties."""
    def addComputedProp(self, prop) -> None:
        """Add a computed property to the selection."""
    def removeComputedProp(self, prop) -> None:
        """Remove a computed property from the selection."""
    def setComputedProp(self, prop) -> None:
        """Clear the computed property selection, then add a single computed
        property back to the selection.
        """
    def getFocusComputedProp(self):
        """Get the focus computed property from the property selection."""
    def getComputedProps(self):
        """Get a list of all selected computed properties."""
