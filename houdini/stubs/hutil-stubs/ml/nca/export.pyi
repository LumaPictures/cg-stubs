import os
import torch
from hutil.ml.nca.log import Log as Log
from hutil.ml.nca.lppn import LPPN as LPPN
from hutil.ml.nca.nca import NCA as NCA

def nca2pt(model: NCA, outputpath: str | os.PathLike[str], log: Log | None = None) -> None:
    """Export NCA model weights and architecture to .pt file.

    Args:
        model: NCA model instance
        outputpath: Path to save the .pt file
        log: Optional logger
    """
def lppn2pt(model: LPPN, outputpath: str | os.PathLike[str], log: Log | None = None) -> None:
    """Export LPPN model weights and architecture to .pt file.

    Args:
        model: LPPN model instance
        outputpath: Path to save the .pt file
        log: Optional logger
    """
def nca2onnx(model: NCA, outputpath: str | os.PathLike[str], channels: int, log: Log | None = None) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]: ...
def lppn2onnx(model: LPPN, outputpath: str | os.PathLike[str], channels: int, log: Log | None = None) -> None: ...
