from hutil.ml.cv.config import _CVTrainParms
from omegaconf import DictConfig as DictConfig

def createBackbone(parms: _CVTrainParms) -> DictConfig: ...
