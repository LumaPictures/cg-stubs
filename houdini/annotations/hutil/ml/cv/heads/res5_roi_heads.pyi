
from omegaconf import DictConfig
from hutil.ml.cv.config import _CVTrainParms

def createROIHeads(dataloader: DictConfig, parms: _CVTrainParms) -> DictConfig: ...
