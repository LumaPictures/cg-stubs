import _pdgd
import pdgd
from collections.abc import Callable as Callable

ID_KEY: str
ICON_KEY: str
PATH_KEY: str

class NodeVisualizer(pdgd.DataLayerVisualizer):
    """
    Subscribes to both PDG and TOP nodes and
    exposes basic information about them
    """
    node_path: str
    icon: str | None
    top_path: str | None
    top_id: int | None
    def __init__(self, data_layer: _pdgd.DataLayerInterface, node_path: str, update_callback: Callable[[NodeVisualizer], object]) -> None: ...
    def term(self) -> None: ...
