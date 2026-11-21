# Houdini stubs generated from Houdini 22.0.466

import torch
from detectron2.engine import train_loop
from hutil.ml.cv.config import _CVTrainParms
from hutil.ml.cv.menu_config import DetectionComposition as DetectionComposition, ImageFormatComposition as ImageFormatComposition, MaskFormatComposition as MaskFormatComposition
from hutil.ml.cv.train import epochToIter as epochToIter, iterToEpoch as iterToEpoch
from omegaconf import DictConfig as DictConfig
from pdgjob.pdgjson import WorkItem

class VisualizerHook(train_loop.HookBase):
    def __init__(self, model: torch.nn.Module, work_item: WorkItem, parms: _CVTrainParms, cfg: DictConfig) -> None: ...
    def after_step(self) -> None: ...
