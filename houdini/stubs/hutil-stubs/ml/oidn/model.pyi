from hutil.ml.oidn.dataset import *
from hutil.ml.oidn.utils import *
import torch
import torch.nn as nn
from hutil.ml.oidn.options import TrainingOptions as TrainingOptions

def get_model(cfg: TrainingOptions) -> UNet:
    """
    Returns the UNet model
    """
def get_unet_model(num_input_channels: int) -> UNet:
    """
    Returns the UNet Model
    """
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
    def __init__(self, in_channels: int = 3, out_channels: int = 3) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...
