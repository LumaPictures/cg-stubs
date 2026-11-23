
from omegaconf import DictConfig
from hutil.ml.cv.config import _CVTrainParms

def createProposalGenerator(parms: _CVTrainParms) -> DictConfig: ...
