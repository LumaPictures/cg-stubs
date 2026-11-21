
from omegaconf import DictConfig
from hutil.ml.cv.config import _CVTrainParms

def createOptimizer(parms: _CVTrainParms) -> DictConfig: ...
