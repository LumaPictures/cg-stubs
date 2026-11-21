# Houdini stubs generated from Houdini 22.0.466

import _pdgd
from pdg.callback import PythonCallback

class PyDataLayerVisualizer(PythonCallback):
    """
    Base class for visualizers implemented in Python
    """
    def __init__(self, visualizer: _pdgd.DataLayerVisualizer) -> None:
        """
        __init__(self, _pdgd.DataLayerVisualizer) -> NoneType

        """
    def processMessage(self, message: _pdgd.Message, objectName: str) -> None:
        """
        processMessage(self, _pdgd.Message, str) -> NoneType

        [virtual] called when a new message is sent by the handler
        """
    def subscriptionLost(self, objectName: str) -> None:
        """
        subscriptionLost(self, str) -> NoneType

        called when a subscription is removed by the handler
        """
