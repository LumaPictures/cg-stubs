# Houdini stubs generated from Houdini 22.0.466

import torch
from collections.abc import Callable as Callable, Iterable
from torch import nn
from typing import Protocol, TypedDict

class _SliceResult(TypedDict):
    rgb: torch.Tensor
    rgb_affine_mats: torch.Tensor

class _HasBilGrids(Protocol):
    @property
    def bil_grids(self) -> Iterable[BilateralGrid]: ...

class _HasBilGridTVLossMult(Protocol):
    @property
    def bilgrid_tv_loss_mult(self) -> float: ...

def color_correct(img: torch.Tensor, ref: torch.Tensor, num_iters: int = 5, eps: float = ...) -> torch.Tensor:
    """
    Warp `img` to match the colors in `ref_img` using iterative color matching.

    This function performs color correction by warping the colors of the input image
    to match those of a reference image. It uses a least squares method to find a
    transformation that maps the input image's colors to the reference image's colors.

    The algorithm iteratively solves a system of linear equations, updating the set of
    unsaturated pixels in each iteration. This approach helps handle non-linear color
    transformations and reduces the impact of clipping.

    Args:
        img (torch.Tensor): Input image to be color corrected. Shape: [..., num_channels]
        ref (torch.Tensor): Reference image to match colors. Shape: [..., num_channels]
        num_iters (int, optional): Number of iterations for the color matching process.
                                   Default is 5.
        eps (float, optional): Small value to determine the range of unclipped pixels.
                               Default is 0.5 / 255.

    Returns:
        torch.Tensor: Color corrected image with the same shape as the input image.

    Note:
        - Both input and reference images should be in the range [0, 1].
        - The function works with any number of channels, but typically used with 3 (RGB).
    """
def bilateral_grid_tv_loss(model: _HasBilGrids, config: _HasBilGridTVLossMult) -> torch.Tensor | float:
    """Computes total variations of bilateral grids."""
def color_affine_transform(affine_mats: torch.Tensor, rgb: torch.Tensor) -> torch.Tensor:
    """Applies color affine transformations.

    Args:
        affine_mats (torch.Tensor): Affine transformation matrices. Supported shape: $(..., 3, 4)$.
        rgb  (torch.Tensor): Input RGB values. Supported shape: $(..., 3)$.

    Returns:
        Output transformed colors of shape $(..., 3)$.
    """
def total_variation_loss(x: torch.Tensor) -> torch.Tensor | float:
    """Returns total variation on multi-dimensional tensors.

    Args:
        x (torch.Tensor): The input tensor with shape $(B, C, ...)$, where $B$ is the batch size and $C$ is the channel size.
    """
def slice(bil_grids: BilateralGrid, xy: torch.Tensor, rgb: torch.Tensor, grid_idx: torch.Tensor) -> _SliceResult:
    '''Slices a batch of 3D bilateral grids by pixel coordinates `xy` and gray-scale guidances of pixel colors `rgb`.

    Supports 2-D, 3-D, and 4-D input shapes. The first dimension of the input is the batch size
    and the last dimension is 2 for `xy`, 3 for `rgb`, and 1 for `grid_idx`.

    The return value is a dictionary containing the affine transformations `affine_mats` sliced from bilateral grids and
    the output color `rgb_out` after applying the afffine transformations.

    In the 2-D input case, `xy` is a $(N, 2)$ tensor, `rgb` is  a $(N, 3)$ tensor, and `grid_idx` is a $(N, 1)$ tensor.
    Then `affine_mats[i]` can be obtained via slicing the bilateral grid indexed at `grid_idx[i]` by `xy[i, :]` and `rgb2gray(rgb[i, :])`.
    For 3-D and 4-D input cases, the behavior of indexing bilateral grids and coordinates is the same with the 2-D case.

    .. note::
        This function can be regarded as a wrapper of `color_affine_transform` and `BilateralGrid` with a slight performance improvement.
        When `grid_idx` contains a unique index, only a single bilateral grid will used during the slicing. In this case, this function will not
        perform tensor indexing to avoid data copy and extra memory
        (see [this](https://discuss.pytorch.org/t/does-indexing-a-tensor-return-a-copy-of-it/164905)).

    Args:
        bil_grids (`BilateralGrid`): An instance of $N$ bilateral grids.
        xy (torch.Tensor): The x-y coordinates of shape $(..., 2)$ in the range of $[0,1]$.
        rgb (torch.Tensor): The RGB values of shape $(..., 3)$ for computing the guidance coordinates, ranging in $[0,1]$.
        grid_idx (torch.Tensor): The indices of bilateral grids for each slicing. Shape: $(..., 1)$.

    Returns:
        A dictionary with keys and values as follows:
        ```
        {
            "rgb": Transformed RGB colors. Shape: (..., 3),
            "rgb_affine_mats": The sliced affine transformation matrices from bilateral grids. Shape: (..., 3, 4)
        }
        ```
    '''

class BilateralGrid(nn.Module):
    """Class for 3D bilateral grids.

    Holds one or more than one bilateral grids.
    """
    grid_width: int
    grid_height: int
    grid_guidance: int
    grids: nn.Parameter
    rgb2gray: Callable[[torch.Tensor], torch.Tensor]
    def __init__(self, num: int, grid_X: int = 16, grid_Y: int = 16, grid_W: int = 8) -> None:
        """
        Args:
            num (int): The number of bilateral grids (i.e., the number of views).
            grid_X (int): Defines grid width $W$.
            grid_Y (int): Defines grid height $H$.
            grid_W (int): Defines grid guidance dimension $L$.
        """
    def tv_loss(self) -> torch.Tensor | float:
        """Computes and returns total variation loss on the bilateral grids."""
    def forward(self, grid_xy: torch.Tensor, rgb: torch.Tensor, idx: torch.Tensor | None = None) -> torch.Tensor:
        """Bilateral grid slicing. Supports 2-D, 3-D, 4-D, and 5-D input.
        For the 2-D, 3-D, and 4-D cases, please refer to `slice`.
        For the 5-D cases, `idx` will be unused and the first dimension of `xy` should be
        equal to the number of bilateral grids. Then this function becomes PyTorch's
        [`F.grid_sample`](https://pytorch.org/docs/stable/generated/torch.nn.functional.grid_sample.html).

        Args:
            grid_xy (torch.Tensor): The x-y coordinates in the range of $[0,1]$.
            rgb (torch.Tensor): The RGB values in the range of $[0,1]$.
            idx (torch.Tensor): The bilateral grid indices.

        Returns:
            Sliced affine matrices of shape $(..., 3, 4)$.
        """

def slice4d(bil_grid4d: BilateralGridCP4D, xyz: torch.Tensor, rgb: torch.Tensor) -> _SliceResult:
    '''Slices a 4D bilateral grid by point coordinates `xyz` and gray-scale guidances of radiance colors `rgb`.

    Args:
        bil_grid4d (`BilateralGridCP4D`): The input 4D bilateral grid.
        xyz (torch.Tensor): The xyz coordinates with shape $(..., 3)$.
        rgb (torch.Tensor): The RGB values with shape $(..., 3)$.

    Returns:
        A dictionary with keys and values as follows:
        ```
        {
            "rgb": Transformed radiance RGB colors. Shape: (..., 3),
            "rgb_affine_mats": The sliced affine transformation matrices from the 4D bilateral grid. Shape: (..., 3, 4)
        }
        ```
    '''

class _ScaledTanh(nn.Module):
    scaler: float
    def __init__(self, s: float = 2.0) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class BilateralGridCP4D(nn.Module):
    """Class for low-rank 4D bilateral grids."""
    grid_X: int
    grid_Y: int
    grid_Z: int
    grid_W: int
    rank: int
    learn_gray: bool
    gray_mlp_width: int
    gray_mlp_depth: int
    init_noise_scale: float
    bound: float
    rgb2gray: Callable[[torch.Tensor], torch.Tensor] | None
    num_facs: int
    fac_0: nn.Linear
    def __init__(self, grid_X: int = 16, grid_Y: int = 16, grid_Z: int = 16, grid_W: int = 8, rank: int = 5, learn_gray: bool = True, gray_mlp_width: int = 8, gray_mlp_depth: int = 2, init_noise_scale: float = 1e-06, bound: float = 2.0) -> None:
        """
        Args:
            grid_X (int): Defines grid width.
            grid_Y (int): Defines grid height.
            grid_Z (int): Defines grid depth.
            grid_W (int): Defines grid guidance dimension.
            rank (int): Rank of the 4D bilateral grid.
            learn_gray (bool): If True, an MLP will be learned to convert RGB colors to gray-scale guidances.
            gray_mlp_width (int): The MLP width for learnable guidance.
            gray_mlp_depth (int): The number of MLP layers for learnable guidance.
            init_noise_scale (float): The noise scale of the initialized factors.
            bound (float): The bound of the xyz coordinates.
        """
    def tv_loss(self) -> torch.Tensor | float:
        """Computes and returns total variation loss on the factors of the low-rank 4D bilateral grids."""
    def forward(self, xyz: torch.Tensor, rgb: torch.Tensor) -> torch.Tensor:
        """Low-rank 4D bilateral grid slicing.

        Args:
            xyz (torch.Tensor): The xyz coordinates with shape $(..., 3)$.
            rgb (torch.Tensor): The corresponding RGB values with shape $(..., 3)$.

        Returns:
            Sliced affine matrices with shape $(..., 3, 4)$.
        """
