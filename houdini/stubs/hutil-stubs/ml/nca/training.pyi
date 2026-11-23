import os
import torch
from collections.abc import Iterable
from hutil.ml.nca.checkpoint_io import NCATrainingRecord as NCATrainingRecord, initialNCATrainingRecord as initialNCATrainingRecord, loadNCATrainingState as loadNCATrainingState, saveNCATrainingState as saveNCATrainingState
from hutil.ml.nca.config import Config as Config
from hutil.ml.nca.export import lppn2onnx as lppn2onnx, lppn2pt as lppn2pt, nca2onnx as nca2onnx, nca2pt as nca2pt
from hutil.ml.nca.log import Log as Log
from hutil.ml.nca.loss import StyleLoss as StyleLoss
from hutil.ml.nca.lppn import LPPN as LPPN
from hutil.ml.nca.nca import NCA as NCA
from hutil.ml.nca.training_monitor import NCATrainingMonitor as NCATrainingMonitor
from hutil.ml.nca.utility import downsample as downsample, expand_to_rgb as expand_to_rgb, export_metadata as export_metadata, random_crop_batch as random_crop_batch, visualize_debug as visualize_debug

def run_nca(nca: NCA, x: torch.Tensor, steps: int, seed: torch.Tensor, chn_base: int) -> torch.Tensor:
    """Run `steps` NCA update iterations on a packed state [B, chn_base*4, H, W].

    update_rate/update_map/update_map_type use the fixed training defaults.
    Returns the updated packed state.
    """
def decode_image(lppn: LPPN, x: torch.Tensor, up_filter: str, chn_base: int, signature: int, *, upsample_factor: float, lppn_scale: float) -> torch.Tensor | None:
    """Upsample a packed NCA state and decode it to an RGB-expanded image.

    upsample_factor: nn.Upsample spatial scale for the upres.
    lppn_scale: coordinate scale passed to the LPPN (training uses the upsample
                factor; inference/eval uses 1 to match COPs and avoid checkerboard).
    """
def build_style_pyramid(image: torch.Tensor, target_size: int, scale_factors: Iterable[int], max_scale: int) -> list[torch.Tensor]:
    """Build the multi-scale crop/downsample list fed to the style loss.
    """
def train(nca: NCA, lppn: LPPN | None = None, style_loss_fn: StyleLoss | None = None, cfg: Config | None = None, log: Log | None = None, training_monitor: NCATrainingMonitor | None = None, checkpoint_path: str | os.PathLike[str] | None = None, max_iterations_partial: int = -1) -> tuple[list[NCA | LPPN | None], bool]: ...
