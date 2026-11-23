from detectron2.config import instantiate as instantiate
from detectron2.layers import ShapeSpec as ShapeSpec
from detectron2.modeling.anchor_generator import DefaultAnchorGenerator as DefaultAnchorGenerator
from detectron2.modeling.backbone import BasicStem as BasicStem, FPN as FPN, ResNet as ResNet
from detectron2.modeling.backbone.fpn import LastLevelMaxPool as LastLevelMaxPool
from detectron2.modeling.box_regression import Box2BoxTransform as Box2BoxTransform
from detectron2.modeling.matcher import Matcher as Matcher
from detectron2.modeling.poolers import ROIPooler as ROIPooler
from detectron2.modeling.proposal_generator import RPN as RPN, StandardRPNHead as StandardRPNHead
from detectron2.modeling.roi_heads import FastRCNNConvFCHead as FastRCNNConvFCHead, FastRCNNOutputLayers as FastRCNNOutputLayers, MaskRCNNConvUpsampleHead as MaskRCNNConvUpsampleHead, StandardROIHeads as StandardROIHeads
from hutil.ml.cv.config import _CVTrainParms
from hutil.ml.cv.menu_config import ImageFormatComposition as ImageFormatComposition, NeckComposition as NeckComposition, ProposalGeneratorComposition as ProposalGeneratorComposition, ROIHeadsComposition as ROIHeadsComposition
from omegaconf import DictConfig as DictConfig

def createModel(dataloader: DictConfig, parms: _CVTrainParms) -> DictConfig: ...
