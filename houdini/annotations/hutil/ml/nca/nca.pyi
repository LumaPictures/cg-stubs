import torch
from torch import nn

from hutil.ml.nca.log import Log

class NCA(torch.nn.Module):
    chn: int
    ch_base: int
    w1: nn.Conv2d
    w2: nn.Conv2d
    ident: torch.Tensor
    sobel_x: torch.Tensor
    lap_x: torch.Tensor
    lap_y: torch.Tensor
    def __init__(self, chn: int = ..., hidden_n: int = ..., ch_base: int = ...) -> None: ...
    def log_info(self, log: Log | None = ...) -> None: ...
    def perchannel_conv(self, x: torch.Tensor, filters: torch.Tensor) -> torch.Tensor: ...
    def scale_gradients_per_pixel(
        self, perception_output: torch.Tensor, scale_x_map: torch.Tensor, scale_y_map: torch.Tensor
    ) -> torch.Tensor: ...
    def rotate_gradients_per_pixel(
        self, perception_output: torch.Tensor, rotation_map: torch.Tensor
    ) -> torch.Tensor: ...
    def merge_lap(self, perception_output: torch.Tensor) -> torch.Tensor: ...
    def perception(
        self,
        x: torch.Tensor,
        rotation_map: torch.Tensor,
        scale_x_map: torch.Tensor,
        scale_y_map: torch.Tensor,
    ) -> torch.Tensor: ...
    def hash_random_uniform(
        self, seed: torch.Tensor, b: int, c: int, h: int, w: int
    ) -> torch.Tensor: ...
    def random_uniform(self, seed: torch.Tensor, b: int, c: int, h: int, w: int) -> torch.Tensor: ...
    def forward(
        self,
        h1: torch.Tensor,
        h2: torch.Tensor,
        h3: torch.Tensor,
        h4: torch.Tensor,
        update_rate: torch.Tensor = ...,
        iterations: torch.Tensor = ...,
        seed: torch.Tensor = ...,
        update_map: torch.Tensor = ...,
        rotation_map: torch.Tensor = ...,
        scale_map: torch.Tensor = ...,
        update_map_type: torch.Tensor = ...,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]: ...
    def seed(self, n: int, sz: int = ...) -> torch.Tensor: ...
