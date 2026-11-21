import torch
from torch import nn

from hutil.ml.oidn.options import TrainingOptions

def get_model(cfg: TrainingOptions) -> "UNet": ...
def get_unet_model(num_input_channels: int) -> "UNet": ...
def Conv(in_channels: int, out_channels: int) -> nn.Conv2d: ...
def relu(x: torch.Tensor) -> torch.Tensor: ...
def pool(x: torch.Tensor) -> torch.Tensor: ...
def upsample(x: torch.Tensor) -> torch.Tensor: ...
def concat(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor: ...

class UNet(nn.Module):
    enc_conv0: nn.Conv2d
    enc_conv1: nn.Conv2d
    enc_conv2: nn.Conv2d
    enc_conv3: nn.Conv2d
    enc_conv4: nn.Conv2d
    enc_conv5a: nn.Conv2d
    enc_conv5b: nn.Conv2d
    dec_conv4a: nn.Conv2d
    dec_conv4b: nn.Conv2d
    dec_conv3a: nn.Conv2d
    dec_conv3b: nn.Conv2d
    dec_conv2a: nn.Conv2d
    dec_conv2b: nn.Conv2d
    dec_conv1a: nn.Conv2d
    dec_conv1b: nn.Conv2d
    dec_conv0: nn.Conv2d
    alignment: int
    def __init__(self, in_channels: int = ..., out_channels: int = ...) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...
