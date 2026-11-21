# Houdini stubs generated from Houdini 22.0.466

from .simplehandler import *
from .pdgdobject import *
import _pdgd
import hou

def start_server(server_type: str = 'DataLayerWSServer', iface: str = '0.0.0.0', port: int = 0) -> tuple[str, int]:
    """
    Creates and starts a new data layer server
    FIXME: bind to the given interface
    """
def get_local_data_layer() -> _pdgd.DataLayerInterface: ...
def terminateRemoteSession(node: hou.TopNode) -> bool: ...
