import torch

from hutil.ml.regression.device_config import DeviceConfig
from hutil.ml.regression.log import Log

def obtainTrainingDevice(device_config: DeviceConfig, /, *, log_file: Log | None = ...) -> tuple[bool, str, torch.device]: ...
