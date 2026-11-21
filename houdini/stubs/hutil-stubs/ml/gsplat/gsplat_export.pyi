# Houdini stubs generated from Houdini 22.0.466

import torch
from collections.abc import Sequence
from typing import Literal, NotRequired, TypedDict

class _FeatureMeta(TypedDict):
    name: str
    start: int
    width: int
    export: NotRequired[bool]

def sh2rgb(sh: torch.Tensor) -> torch.Tensor:
    """Convert Sphere Harmonics to RGB

    Args:
        sh (torch.Tensor): SH tensor

    Returns:
        torch.Tensor: RGB tensor
    """
def part1by2_vec(x: torch.Tensor) -> torch.Tensor:
    """Interleave bits of x with 0s

    Args:
        x (torch.Tensor): Input tensor. Shape (N,)

    Returns:
        torch.Tensor: Output tensor. Shape (N,)
    """
def encode_morton3_vec(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
    """Compute Morton codes for 3D coordinates

    Args:
        x (torch.Tensor): X coordinates. Shape (N,)
        y (torch.Tensor): Y coordinates. Shape (N,)
        z (torch.Tensor): Z coordinates. Shape (N,)
    Returns:
        torch.Tensor: Morton codes. Shape (N,)
    """
def sort_centers(centers: torch.Tensor, indices: torch.Tensor) -> torch.Tensor:
    """Sort centers based on Morton codes

    Args:
        centers (torch.Tensor): Centers. Shape (N, 3)
        indices (torch.Tensor): Indices. Shape (N,)
    Returns:
        torch.Tensor: Sorted indices. Shape (N,)
    """
def pack_unorm(value: torch.Tensor, bits: int) -> torch.Tensor:
    """Pack a floating point value into an unsigned integer with a given number of bits.

    Args:
        value (torch.Tensor): Floating point value to pack. Shape (N,)
        bits (int): Number of bits to pack into.

    Returns:
        torch.Tensor: Packed value. Shape (N,)
    """
def pack_111011(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
    """Pack three floating point values into a 32-bit integer with 11, 10, and 11 bits.

    Args:
        x (torch.Tensor): X component. Shape (N,)
        y (torch.Tensor): Y component. Shape (N,)
        z (torch.Tensor): Z component. Shape (N,)
    Returns:
        torch.Tensor: Packed values. Shape (N,)
    """
def pack_8888(x: torch.Tensor, y: torch.Tensor, z: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
    """Pack four floating point values into a 32-bit integer with 8 bits each.

    Args:
        x (torch.Tensor): X component. Shape (N,)
        y (torch.Tensor): Y component. Shape (N,)
        z (torch.Tensor): Z component. Shape (N,)
        w (torch.Tensor): W component. Shape (N,)
    Returns:
        torch.Tensor: Packed values. Shape (N,)
    """
def pack_rotation(q: torch.Tensor) -> torch.Tensor:
    """Pack a quaternion into a 32-bit integer.

    Args:
        q (torch.Tensor): Quaternions. Shape (N, 4)

    Returns:
        torch.Tensor: Packed values. Shape (N,)
    """
def splat2ply_bytes_compressed(means: torch.Tensor, scales: torch.Tensor, quats: torch.Tensor, opacities: torch.Tensor, sh0: torch.Tensor, shN: torch.Tensor, chunk_max_size: int = 256, opacity_threshold: float = ...) -> bytes:
    """Return the binary compressed Ply file. Used by Supersplat viewer.

    Args:
        means (torch.Tensor): Splat means. Shape (N, 3)
        scales (torch.Tensor): Splat scales. Shape (N, 3)
        quats (torch.Tensor): Splat quaternions. Shape (N, 4)
        opacities (torch.Tensor): Splat opacities. Shape (N,)
        sh0 (torch.Tensor): Spherical harmonics. Shape (N, 3)
        shN (torch.Tensor): Spherical harmonics. Shape (N, K*3)
        chunk_max_size (int): Maximum number of splats per chunk. Default: 256
        opacity_threshold (float): Opacity threshold. Default: 1 / 255

    Returns:
        bytes: Binary compressed Ply file representing the model.
    """
def splat2ply_bytes(means: torch.Tensor, scales: torch.Tensor, quats: torch.Tensor, opacities: torch.Tensor, sh0: torch.Tensor, shN: torch.Tensor, extra_features: torch.Tensor | None = None, feature_meta: Sequence[_FeatureMeta] | None = None) -> bytes:
    """Return the binary Ply file. Supported by almost all viewers.

    Args:
        means (torch.Tensor): Splat means. Shape (N, 3)
        scales (torch.Tensor): Splat scales. Shape (N, 3)
        quats (torch.Tensor): Splat quaternions. Shape (N, 4)
        opacities (torch.Tensor): Splat opacities. Shape (N,)
        sh0 (torch.Tensor): Spherical harmonics. Shape (N, 3)
        shN (torch.Tensor): Spherical harmonics. Shape (N, K*3)
        extra_features (torch.Tensor): Optional per-splat extra features. Shape (N, F)
        feature_meta (list): Metadata with start/width/name for each feature.

    Returns:
        bytes: Binary Ply file representing the model.
    """
def splat2splat_bytes(means: torch.Tensor, scales: torch.Tensor, quats: torch.Tensor, opacities: torch.Tensor, sh0: torch.Tensor) -> bytes:
    """Return the binary Splat file. Supported by antimatter15 viewer.

    Args:
        means (torch.Tensor): Splat means. Shape (N, 3)
        scales (torch.Tensor): Splat scales. Shape (N, 3)
        quats (torch.Tensor): Splat quaternions. Shape (N, 4)
        opacities (torch.Tensor): Splat opacities. Shape (N,)
        sh0 (torch.Tensor): Spherical harmonics. Shape (N, 3)

    Returns:
        bytes: Binary Splat file representing the model.
    """
def export_splats(means: torch.Tensor, scales: torch.Tensor, quats: torch.Tensor, opacities: torch.Tensor, sh0: torch.Tensor, shN: torch.Tensor, extra_features: torch.Tensor | None = None, extra_feature_meta: object | None = None, format: Literal['ply', 'splat', 'ply_compressed'] = 'ply', source: Literal['colmap', 'houdini'] = 'colmap', save_to: str | None = None, transform: object | None = None) -> bytes:
    '''Export a Gaussian Splats model to bytes.
    The three supported formats are:
    - ply: A standard PLY file format. Supported by most viewers.
    - splat: A custom Splat file format. Supported by antimatter15 viewer.
    - ply_compressed: A compressed PLY file format. Used by Supersplat viewer.

    Args:
        means (torch.Tensor): Splat means. Shape (N, 3)
        scales (torch.Tensor): Splat scales. Shape (N, 3)
        quats (torch.Tensor): Splat quaternions. Shape (N, 4)
        opacities (torch.Tensor): Splat opacities. Shape (N,)
        sh0 (torch.Tensor): Spherical harmonics. Shape (N, 1, 3)
        shN (torch.Tensor): Spherical harmonics. Shape (N, K, 3)
        extra_features (torch.Tensor): Optional per-splat extra features. Shape (N, F)
        extra_feature_meta: Optional metadata describing each feature slice (list of dataclasses or dicts with name/start/width/export).
        format (str): Export format. Options: "ply", "splat", "ply_compressed". Default: "ply"
        sh_viewdir (str): SH view-direction convention used by the consumer.
            - "cam_to_point": dirs = mean - campos (gsplat default)
            - "point_to_cam": dirs = campos - mean (flips all odd SH degrees)
        save_to (str): Output file path. If provided, the bytes will be written to file.
        transform: Optional 4x4 world-to-normalized transform used during training.
            If provided, its inverse (uniform scale + rotation + translation) is applied
            so exported splats end up in the original coordinate frame.
    '''
