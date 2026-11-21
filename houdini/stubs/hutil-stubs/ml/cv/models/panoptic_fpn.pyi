from hutil.ml.cv.config import _CVTrainParms
from hutil.ml.cv.menu_config import NeckComposition as NeckComposition, ROIHeadsComposition as ROIHeadsComposition
from omegaconf import DictConfig as DictConfig

def createModel(dataloader: DictConfig, parms: _CVTrainParms) -> DictConfig: ...
