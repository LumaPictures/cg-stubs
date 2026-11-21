import torch
from collections.abc import Sequence

def _fspecial_gauss_1d(size: int, sigma: float) -> torch.Tensor:
    """Create 1-D gauss kernel
    Args:
        size (int): the size of gauss kernel
        sigma (float): sigma of normal distribution

    Returns:
        torch.Tensor: 1D kernel
    """
def gaussian_filter(input: torch.Tensor, win: torch.Tensor) -> torch.Tensor:
    """Blur input with 1-D kernel
    Args:
        input (torch.Tensor): a batch of tensors to be blurred
        window (torch.Tensor): 1-D gauss kernel

    Returns:
        torch.Tensor: blurred tensors
    """
def _ssim_per_channel(X: torch.Tensor, Y: torch.Tensor, win: torch.Tensor, data_range: float = 255, cs_only: bool = False) -> torch.Tensor:
    """Calculate ssim index for each color channel of X and Y
    Args:
        X (torch.Tensor): images
        Y (torch.Tensor): images
        win (torch.Tensor): 1-D gauss kernel
        data_range (float or int, optional): value range of input images. (usually 1.0 or 255)
        size_average (bool, optional): if size_average=True, ssim of all images will be averaged as a scalar
        cs_only (bool, optional): compute only the contrast and structure measures

    Returns:
        torch.Tensor: ssim results
    """
def ssim(X: torch.Tensor, Y: torch.Tensor, win_size: int = 11, win_sigma: float = 1.5, win: torch.Tensor | None = None, data_range: float = 255, size_average: bool = True) -> torch.Tensor:
    """interface of ssim
    Args:
        X (torch.Tensor): a batch of images, (N,C,H,W)
        Y (torch.Tensor): a batch of images, (N,C,H,W)
        win_size: (int, optional): the size of gauss kernel
        win_sigma: (float, optional): sigma of normal distribution
        win (torch.Tensor, optional): 1-D gauss kernel. if None, a new kernel will be created according to win_size and win_sigma
        data_range (float or int, optional): value range of input images. (usually 1.0 or 255)
        size_average (bool, optional): if size_average=True, ssim of all images will be averaged as a scalar

    Returns:
        torch.Tensor: ssim results
    """
def ms_ssim(X: torch.Tensor, Y: torch.Tensor, win_size: int = 11, win_sigma: float = 1.5, win: torch.Tensor | None = None, data_range: float = 255, size_average: bool = True, weights: torch.Tensor | None = None) -> torch.Tensor:
    """interface of ms-ssim
    Args:
        X (torch.Tensor): a batch of images, (N,C,H,W)
        Y (torch.Tensor): a batch of images, (N,C,H,W)
        win_size: (int, optional): the size of gauss kernel
        win_sigma: (float, optional): sigma of normal distribution
        win (torch.Tensor, optional): 1-D gauss kernel. if None, a new kernel will be created according to win_size and win_sigma
        data_range (float or int, optional): value range of input images. (usually 1.0 or 255)
        size_average (bool, optional): if size_average=True, ssim of all images will be averaged as a scalar
        weights (list, optional): weights for different scales

    Returns:
        torch.Tensor: ms-ssim results
    """

class SSIM(torch.nn.Module):
    win: torch.Tensor
    size_average: bool
    data_range: float | None
    def __init__(self, win_size: int = 11, win_sigma: float = 1.5, data_range: float | None = None, size_average: bool = True, channel: int = 3) -> None:
        """class for ssim
        Args:
            win_size: (int, optional): the size of gauss kernel
            win_sigma: (float, optional): sigma of normal distribution
            data_range (float or int, optional): value range of input images. (usually 1.0 or 255)
            size_average (bool, optional): if size_average=True, ssim of all images will be averaged as a scalar
            channel (int, optional): input channels (default: 3)
        """
    def forward(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor: ...

class MS_SSIM(torch.nn.Module):
    win: torch.Tensor
    weights: torch.Tensor
    size_average: bool
    data_range: float | None
    def __init__(self, win_size: int = 11, win_sigma: float = 1.5, data_range: float | None = None, size_average: bool = True, channel: int = 3, weights: Sequence[float] | None = None) -> None:
        """class for ms-ssim
        Args:
            win_size: (int, optional): the size of gauss kernel
            win_sigma: (float, optional): sigma of normal distribution
            data_range (float or int, optional): value range of input images. (usually 1.0 or 255)
            size_average (bool, optional): if size_average=True, ssim of all images will be averaged as a scalar
            channel (int, optional): input channels (default: 3)
            weights (list, optional): weights for different scales
        """
    def forward(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor: ...
