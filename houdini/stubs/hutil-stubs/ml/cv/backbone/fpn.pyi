from hutil.ml.cv.config import _CVTrainParms
from hutil.ml.cv.menu_config import BackboneComposition as BackboneComposition, TopBlockComposition as TopBlockComposition
from omegaconf import DictConfig as DictConfig

def createBackbone(parms: _CVTrainParms) -> DictConfig: ...
