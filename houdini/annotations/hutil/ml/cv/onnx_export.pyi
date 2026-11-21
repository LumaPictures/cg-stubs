
import torch
from detectron2.engine import train_loop
from pdgjob.pdgjson import WorkItem
from hutil.ml.cv.config import _CVTrainParms

class OnnxExportHook(train_loop.HookBase):
    def __init__(self, model: torch.nn.Module, work_item: WorkItem, parms: _CVTrainParms) -> None: ...
    def after_step(self) -> None: ...
    def after_train(self) -> None: ...
