from hutil.ml.cv.config import _CVTrainParms
from omegaconf import DictConfig as DictConfig

def createProposalGenerator(parms: _CVTrainParms) -> DictConfig: ...
