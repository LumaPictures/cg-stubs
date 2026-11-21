# Houdini stubs generated from Houdini 22.0.466

import torch
import torch.nn as nn
from hutil.ml.nca.log import Log as Log

class SinActivation(nn.Module):
    omega_0: float
    def __init__(self, omega_0: float = 10.0) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class Wire2DActivation(nn.Module):
    omega_0: float
    s_0: float
    def __init__(self, omega_0: float = 20.0, s_0: float = 10.0) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class LPPN(torch.nn.Module):
    omega_0: float
    s_0: float
    wire_omega: float
    mode: str
    signature: int
    lppn: nn.Sequential
    def __init__(self, h_layers: int = 2, in_chn: int = 12, h_chn: int = 32, out_chn: int = 3, omega_0: float = 10.0, mode: str = 'siren', s_0: float = 10.0, wire_omega: float = 20.0, wire_h_chn: int = 22, signature: int = 3) -> None: ...
    def log_info(self, log: Log | None = None) -> None: ...
    def init_siren_weights(self) -> None:
        """Initialize all LPPN layers with SIREN initialization"""
    def create_local_coordinates(self, nca_w: torch.Tensor | float, nca_h: torch.Tensor | float, output_w: torch.Tensor | float, output_h: torch.Tensor | float) -> tuple[torch.Tensor, torch.Tensor]:
        """Creates a local coordinate grid [-1:1] between original cell centers."""
    def positional_encoding(self, in_x: torch.Tensor | float, in_y: torch.Tensor | float, out_x: torch.Tensor | float, out_y: torch.Tensor | float) -> torch.Tensor:
        """Encode per-cell local coordinates as two extra input channels."""
    def srgb_to_linear(self, img: torch.Tensor) -> torch.Tensor:
        """sRGB to linear conversion (https://www.color.org/srgb.pdf)"""
    def forward(self, h0: torch.Tensor, h1: torch.Tensor, h2: torch.Tensor, h3: torch.Tensor, scalefactor: torch.Tensor = ...) -> torch.Tensor: ...
