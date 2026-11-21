import numpy as np
import numpy.typing as npt
import torch

SRGB_A: float
SRGB_B: float
SRGB_C: float
SRGB_D: float
SRGB_Y0: float
SRGB_X0: float
HDR_Y_MAX: float
PU_A: float
PU_B: float
PU_C: float
PU_D: float
PU_E: float
PU_F: float
PU_G: float
PU_Y0: float
PU_Y1: float
PU_X0: float
PU_X1: float
PU_NORM_SCALE: np.float64
LOG_NORM_SCALE: np.float64

def apply_transfer_forward(image: npt.NDArray[np.floating], transfer: str) -> npt.NDArray[np.floating]:
    '''Apply forward transfer function to compress dynamic range.

    Encodes linear HDR values into a more compact range suitable for training.

    Args:
        image: Linear float image (H, W, C) or any shape
        transfer: "linear", "srgb", "log", or "pu"

    Returns:
        Encoded image (same shape)
    '''
def apply_transfer_forward_torch(image: torch.Tensor, transfer: str) -> torch.Tensor:
    """Torch version of apply_transfer_forward (differentiable)."""
def apply_transfer_inverse(image: npt.NDArray[np.floating], transfer: str) -> npt.NDArray[np.floating]:
    '''Apply inverse transfer function to expand dynamic range.

    Decodes encoded values back to linear HDR for export/rendering.

    Args:
        image: Encoded image (H, W, C) or any shape
        transfer: "linear", "srgb", "log", or "pu"

    Returns:
        Linear HDR image (same shape)
    '''
def apply_transfer_inverse_torch(image: torch.Tensor, transfer: str) -> torch.Tensor:
    """Torch version of apply_transfer_inverse (differentiable)."""
