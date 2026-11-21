from typing import Literal

import torch

allowed_padding: list[str]

class SSIM:
    @staticmethod
    def forward(img1: torch.Tensor, img2: torch.Tensor, padding: Literal["same", "valid"] = ..., train: bool = ...) -> torch.Tensor: ...

def os_ssim(img1: torch.Tensor, img2: torch.Tensor, padding: Literal["same", "valid"] = ..., train: bool = ...) -> torch.Tensor: ...
