
from omegaconf import DictConfig
from hutil.ml.cv.config import _CVTrainParms

def createBackbone(parms: _CVTrainParms) -> DictConfig: ...
