import torch
from torch import nn

from hutil.ml.nca.log import Log

class SinActivation(nn.Module):
    omega_0: float
    def __init__(self, omega_0: float = ...) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class Wire2DActivation(nn.Module):
    omega_0: float
    s_0: float
    def __init__(self, omega_0: float = ..., s_0: float = ...) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class LPPN(torch.nn.Module):
    omega_0: float
    s_0: float
    wire_omega: float
    mode: str
    signature: int
    lppn: nn.Sequential
    def __init__(
        self,
        h_layers: int = ...,
        in_chn: int = ...,
        h_chn: int = ...,
        out_chn: int = ...,
        omega_0: float = ...,
        mode: str = ...,
        s_0: float = ...,
        wire_omega: float = ...,
        wire_h_chn: int = ...,
        signature: int = ...,
    ) -> None: ...
    def log_info(self, log: Log | None = ...) -> None: ...
    def init_siren_weights(self) -> None: ...
    def create_local_coordinates(
        self,
        nca_w: torch.Tensor | float,
        nca_h: torch.Tensor | float,
        output_w: torch.Tensor | float,
        output_h: torch.Tensor | float,
    ) -> tuple[torch.Tensor, torch.Tensor]: ...
    def positional_encoding(
        self,
        in_x: torch.Tensor | float,
        in_y: torch.Tensor | float,
        out_x: torch.Tensor | float,
        out_y: torch.Tensor | float,
    ) -> torch.Tensor: ...
    def srgb_to_linear(self, img: torch.Tensor) -> torch.Tensor: ...
    def forward(
        self,
        h0: torch.Tensor,
        h1: torch.Tensor,
        h2: torch.Tensor,
        h3: torch.Tensor,
        scalefactor: torch.Tensor = ...,
    ) -> torch.Tensor: ...
