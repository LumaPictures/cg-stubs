import torch
from detectron2.engine import train_loop
from hutil.ml.cv.config import _CVTrainParms
from hutil.ml.cv.menu_config import DetectionComposition as DetectionComposition
from hutil.ml.cv.train import epochToIter as epochToIter, iterToEpoch as iterToEpoch
from hutil.ml.utils.plotter import CSVPlotter as CSVPlotter
from omegaconf import DictConfig as DictConfig
from pdgjob.pdgjson import WorkItem

class ValidationHook(train_loop.HookBase):
    def __init__(self, model: torch.nn.Module, work_item: WorkItem, parms: _CVTrainParms, cfg: DictConfig) -> None: ...
    def after_step(self) -> None: ...
