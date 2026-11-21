
from omegaconf import DictConfig
from hutil.ml.cv.config import _CVTrainParms

def createHead(dataloader: DictConfig, parms: _CVTrainParms) -> DictConfig: ...
