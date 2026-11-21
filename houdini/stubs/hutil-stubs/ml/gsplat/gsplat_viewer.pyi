# Houdini stubs generated from Houdini 22.0.466

import numpy as np
import numpy.typing as npt
import viser
from nerfview import CameraState as CameraState, RenderTabState, Viewer
from pathlib import Path
from typing import Callable as Callable, Literal

class GsplatRenderTabState(RenderTabState):
    total_gs_count: int
    rendered_gs_count: int
    max_sh_degree: int
    near_plane: float
    far_plane: float
    radius_clip: float
    eps2d: float
    backgrounds: tuple[float, float, float]
    render_mode: Literal['rgb', 'depth(accumulated)', 'depth(expected)', 'alpha', 'feature']
    feature_name: str
    normalize_nearfar: bool
    inverse: bool
    colormap: Literal['turbo', 'viridis', 'magma', 'inferno', 'cividis', 'gray']
    rasterize_mode: Literal['classic', 'antialiased']
    camera_model: Literal['pinhole', 'ortho', 'fisheye']

class GsplatViewer(Viewer):
    """
    Viewer for gsplat.
    """
    enable_feature_mode: bool
    stop_requested: bool
    render_tab_state: GsplatRenderTabState
    def __init__(self, server: viser.ViserServer, render_fn: Callable[[CameraState, RenderTabState], npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic], npt.NDArray[np.generic] | None]], output_dir: Path, mode: Literal['rendering', 'training'] = 'rendering', enable_feature_mode: bool = False) -> None: ...
