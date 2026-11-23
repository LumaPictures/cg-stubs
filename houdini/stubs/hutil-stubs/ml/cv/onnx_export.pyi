import torch
from detectron2.config import LazyConfig as LazyConfig, instantiate as instantiate
from detectron2.engine import train_loop
from hutil.ml.cv.config import _CVTrainParms
from hutil.ml.cv.menu_config import DetectionComposition as DetectionComposition
from hutil.ml.cv.train import epochToIter as epochToIter, iterToEpoch as iterToEpoch
from pdgjob.pdgjson import WorkItem

class OnnxExportHook(train_loop.HookBase):
    def __init__(self, model: torch.nn.Module, work_item: WorkItem, parms: _CVTrainParms) -> None: ...
    def after_step(self) -> None: ...
    def after_train(self) -> None: ...
