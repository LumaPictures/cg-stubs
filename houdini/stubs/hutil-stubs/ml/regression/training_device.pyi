# Houdini stubs generated from Houdini 22.0.466

import torch
from hutil.ml.regression.device_config import DeviceConfig as DeviceConfig
from hutil.ml.regression.log import Log as Log

def obtainTrainingDevice(device_config: DeviceConfig, /, *, log_file: Log | None = None) -> tuple[bool, str, torch.device]: ...
