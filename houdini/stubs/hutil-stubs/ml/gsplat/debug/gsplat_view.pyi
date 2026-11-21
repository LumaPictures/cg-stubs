# Houdini stubs generated from Houdini 22.0.466

import argparse
from hutil.ml.gsplat.gsplat_utils import get_viewer_rotation_matrix as get_viewer_rotation_matrix
from hutil.ml.gsplat.gsplat_viewer import GsplatRenderTabState as GsplatRenderTabState, GsplatViewer as GsplatViewer
from nerfview import CameraState as CameraState, RenderTabState as RenderTabState
from plyfile import PlyElement as PlyElement

def main(local_rank: int, world_rank: int, world_size: int, args: argparse.Namespace) -> None: ...
