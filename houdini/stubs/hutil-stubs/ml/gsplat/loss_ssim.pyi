# Houdini stubs generated from Houdini 22.0.466

import torch
from typing import Literal

allowed_padding: list[str]

class SSIM:
    """
    OS independent SSIM wrapper.
    """
    @staticmethod
    def forward(img1: torch.Tensor, img2: torch.Tensor, padding: Literal['same', 'valid'] = 'same', train: bool = True) -> torch.Tensor: ...

def os_ssim(img1: torch.Tensor, img2: torch.Tensor, padding: Literal['same', 'valid'] = 'same', train: bool = True) -> torch.Tensor: ...
