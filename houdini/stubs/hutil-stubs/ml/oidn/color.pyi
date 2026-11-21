from hutil.ml.oidn.utils import *
import numpy as np
import numpy.typing as npt
import torch
import typing
from typing import Protocol

class _TransferConfig(Protocol):
    @property
    def transfer(self) -> str: ...

HDR_Y_MAX: float

@typing.overload
def luminance(r: npt.NDArray[np.floating], g: npt.NDArray[np.floating], b: npt.NDArray[np.floating]) -> npt.NDArray[np.floating]: ...
@typing.overload
def luminance(r: float, g: float, b: float) -> float: ...
@typing.overload
def luminance(r: torch.Tensor, g: torch.Tensor, b: torch.Tensor) -> torch.Tensor: ...

class TransferFunction: ...

def get_transfer_function(cfg: _TransferConfig) -> LinearTransferFunction | SRGBTransferFunction | PUTransferFunction | LogTransferFunction: ...

class LinearTransferFunction(TransferFunction):
    def forward(self, y: torch.Tensor) -> torch.Tensor: ...
    def inverse(self, x: torch.Tensor) -> torch.Tensor: ...

SRGB_A: float
SRGB_B: float
SRGB_C: float
SRGB_D: float
SRGB_Y0: float
SRGB_X0: float

def srgb_forward(y: torch.Tensor) -> torch.Tensor: ...
def srgb_inverse(x: torch.Tensor) -> torch.Tensor: ...

class SRGBTransferFunction(TransferFunction):
    def forward(self, y: torch.Tensor) -> torch.Tensor: ...
    def inverse(self, x: torch.Tensor) -> torch.Tensor: ...

PU_A: float
PU_B: float
PU_C: float
PU_D: float
PU_E: float
PU_F: float
PU_G: float
PU_Y0: float
PU_Y1: float
PU_X0: float
PU_X1: float

def pu_forward(y: torch.Tensor) -> torch.Tensor: ...
def pu_inverse(x: torch.Tensor) -> torch.Tensor: ...

PU_NORM_SCALE: float

class PUTransferFunction(TransferFunction):
    def forward(self, y: torch.Tensor) -> torch.Tensor: ...
    def inverse(self, x: torch.Tensor) -> torch.Tensor: ...

def log_forward(y: torch.Tensor) -> torch.Tensor: ...
def log_inverse(x: torch.Tensor) -> torch.Tensor: ...

LOG_NORM_SCALE: float

class LogTransferFunction(TransferFunction):
    def forward(self, y: torch.Tensor) -> torch.Tensor: ...
    def inverse(self, x: torch.Tensor) -> torch.Tensor: ...

def autoexposure(image: npt.NDArray[np.floating]) -> float: ...
def tonemap(x: torch.Tensor) -> torch.Tensor: ...
