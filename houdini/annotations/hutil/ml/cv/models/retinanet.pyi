
from omegaconf import DictConfig
from hutil.ml.cv.config import _CVTrainParms

def createModel(dataloader: DictConfig, parms: _CVTrainParms) -> DictConfig: ...
