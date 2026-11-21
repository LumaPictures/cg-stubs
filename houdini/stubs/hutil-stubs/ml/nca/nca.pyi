# Houdini stubs generated from Houdini 22.0.466

import torch
import torch.nn as nn
from hutil.ml.nca.log import Log as Log

class NCA(torch.nn.Module):
    chn: int
    ch_base: int
    w1: nn.Conv2d
    w2: nn.Conv2d
    ident: torch.Tensor
    sobel_x: torch.Tensor
    lap_x: torch.Tensor
    lap_y: torch.Tensor
    def __init__(self, chn: int = 16, hidden_n: int = 128, ch_base: int = 4) -> None: ...
    def log_info(self, log: Log | None = None) -> None: ...
    def perchannel_conv(self, x: torch.Tensor, filters: torch.Tensor) -> torch.Tensor:
        """filters: [filter_n, h, w]"""
    def scale_gradients_per_pixel(self, perception_output: torch.Tensor, scale_x_map: torch.Tensor, scale_y_map: torch.Tensor) -> torch.Tensor:
        """Scale gradient vectors based on separate x/y scale maps

        Args:
            perception_output: [B, C*5, H, W] where C*5 = [ident, gx, gy, lap_x, lap_y] repeated per channel
            scale_x_map: x scale factors, can be [1,1,1,1] scalar or [B,1,H,W] per-pixel
            scale_y_map: y scale factors, can be [1,1,1,1] scalar or [B,1,H,W] per-pixel
                         scale=1.0 means no change
                         scale=2.0 means smaller patterns (sharper)
                         scale=0.5 means larger patterns (smoother)

        Returns:
            Scaled and merged perception output [B, C*4, H, W] with lap_x + lap_y merged
        """
    def rotate_gradients_per_pixel(self, perception_output: torch.Tensor, rotation_map: torch.Tensor) -> torch.Tensor:
        """Rotate gradient vectors (gx, gy) per-pixel based on rotation_map

        Args:
            perception_output: [B, C*4, H, W] where C*4 = [ident, gx, gy, lap] repeated per channel
            rotation_map: cos/sin rotation, [B,2,H,W] or [1,2,1,1] with channels (cos, sin)

        Returns:
            Rotated perception output [B, C*4, H, W]
        """
    def merge_lap(self, perception_output: torch.Tensor) -> torch.Tensor:
        """Merge lap_x and lap_y into single laplacian (no scaling)

        Args:
            perception_output: [B, C*5, H, W] where C*5 = [ident, gx, gy, lap_x, lap_y] per channel

        Returns:
            Merged output [B, C*4, H, W]
        """
    def perception(self, x: torch.Tensor, rotation_map: torch.Tensor, scale_x_map: torch.Tensor, scale_y_map: torch.Tensor) -> torch.Tensor:
        """setup perception filters and apply per-pixel rotation and scaling

        Args:
            x: input state [B, C, H, W]
            rotation_map: cos/sin rotation, [B,2,H,W] or [1,2,1,1] with channels (cos, sin)
            scale_x_map: x scale factors for inference
            scale_y_map: y scale factors for inference
        """
    def hash_random_uniform(self, seed: torch.Tensor, b: int, c: int, h: int, w: int) -> torch.Tensor:
        """deterministic, platform-independent random uniform in [0, 1)"""
    def random_uniform(self, seed: torch.Tensor, b: int, c: int, h: int, w: int) -> torch.Tensor: ...
    def forward(self, h1: torch.Tensor, h2: torch.Tensor, h3: torch.Tensor, h4: torch.Tensor, update_rate: torch.Tensor = ..., iterations: torch.Tensor = ..., seed: torch.Tensor = ..., update_map: torch.Tensor = ..., rotation_map: torch.Tensor = ..., scale_map: torch.Tensor = ..., update_map_type: torch.Tensor = ...) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]: ...
    def seed(self, n: int, sz: int = 128) -> torch.Tensor: ...
