# Houdini stubs generated from Houdini 22.0.466

from detectron2.data.detection_utils import create_keypoint_hflip_indices as create_keypoint_hflip_indices
from hutil.ml.cv.config import _CVTrainParms
from hutil.ml.cv.data.dataset import DatasetPreprocess as DatasetPreprocess
from hutil.ml.cv.menu_config import DetectionComposition as DetectionComposition, ImageFormatComposition as ImageFormatComposition, MaskFormatComposition as MaskFormatComposition, SampleStyleComposition as SampleStyleComposition
from omegaconf import DictConfig as DictConfig

def processDatasets(parms: _CVTrainParms) -> tuple[dict[str, tuple[str, ...]], int, int]: ...
def setDataloader(parms: _CVTrainParms) -> DictConfig: ...
