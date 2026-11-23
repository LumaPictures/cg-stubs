
import torch
from detectron2.engine import train_loop
from omegaconf import DictConfig
from pdgjob.pdgjson import WorkItem
from hutil.ml.cv.config import _CVTrainParms

class ValidationHook(train_loop.HookBase):
    def __init__(self, model: torch.nn.Module, work_item: WorkItem, parms: _CVTrainParms, cfg: DictConfig) -> None: ...
    def after_step(self) -> None: ...
