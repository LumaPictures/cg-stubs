from collections.abc import Callable

import _pdgd
import pdgd

ID_KEY: str
ICON_KEY: str
PATH_KEY: str

class NodeVisualizer(pdgd.DataLayerVisualizer):
    node_path: str
    icon: str | None
    top_path: str | None
    top_id: int | None
    def __init__(
        self,
        data_layer: _pdgd.DataLayerInterface,
        node_path: str,
        update_callback: Callable[["NodeVisualizer"], object],
    ) -> None: ...
    def term(self) -> None: ...
