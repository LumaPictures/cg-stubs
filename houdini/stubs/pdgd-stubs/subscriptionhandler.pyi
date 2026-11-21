# Houdini stubs generated from Houdini 22.0.466

import _pdgd
from pdg.callback import PythonCallback

class PyDataLayerSubscriptionHandler(PythonCallback):
    """
    Base class for subscription handlers implemented in Python
    """
    def __init__(self, handler: _pdgd.SubscriptionHandler) -> None:
        """
        __init__(self, _pdgd.DataLayerSubscriptionHandler) -> NoneType
        """
    def onVisualizerAdded(self, visualizer: _pdgd.DataLayerVisualizer) -> None:
        """
        onVisualizerAdded(self, _pdgd.DataLayerVisualizer) -> NoneType
        
        Called when a visualizer was added to this handler
        """
    def createPlaceHolderChildHandler(self, handler_name: str) -> None:
        """
        createPlaceHolderChildHandler(self, str) -> NoneType

        Called before trying to access a child handler, giving an opportunity
        to create it if needed
        """
    def buildSnapshot(self) -> _pdgd.ObjectSnapshot:
        """
        buildSnapshot(self) -> _pdgd.ObjectSnapshot

        [virtual] Returns a snapshot of the object represented by this handler
        """
    def processCommand(self, command: _pdgd.Command) -> None:
        """
        processCommand(self, _pdgd.Command) -> NoneType
        
        Called when commands are sent to the subscription handler's path
        """
    def processCommandWithCallback(self, command: _pdgd.Command) -> _pdgd.ObjectProperty | None:
        """
        processCommand(self, _pdgd.Command) -> NoneType

        Called when commands are sent to the subscriptions handler's path
        and allows a value to be returned
        """
