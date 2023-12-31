# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI
import Utils as Utils
import PyFnGeolibServices.XFormUtil as XFormUtil
from _typeshed import Incomplete
from typing import Set, Tuple

_TransformParameterHints: dict
_xyz: list

def CanOverrideTransform(node: NodegraphAPI.Node, attrName): ...
def FindOverrideParameterTransform(node: NodegraphAPI.Node, path, attrName, time, index: Incomplete | None = ..., editable: bool = ...): ...
def GetEnableableNodesWithTransforms(): ...
def GetRotateAttr(attr, param, frameTime): ...
def GetRotateXAttr(attr, param, frameTime): ...
def GetRotateYAttr(attr, param, frameTime): ...
def GetRotateZAttr(attr, param, frameTime): ...
def GetScaleAttr(attr, param, frameTime): ...
def GetTransformAttr(attr, param, frameTime): ...
def GetTransformAttrWithMotionUsingGraphState(param, graphState: NodegraphAPI.GraphState): ...
def GetTransformAttr_WithMotion(attr, param, shutterOpenTime, timeWindowDuration, timeNumSamples, sampleOffset: float = ...): ...
def GetTransformParameterAttrsForNodeTypeBuilder(): ...
def GetTransformParameterHints(): ...
def GetTransformXML(): ...
def GetTranslateAttr(attr, param, frameTime): ...
def PushInteractiveTransform(attr, scale, rotate, translate, _time): ...
def ResetTransformParams(param, time): ...
def SetOverrideTransform(node: NodegraphAPI.Node, path, attrName, time, attrData, index: Incomplete | None = ..., *args, **kwargs): ...
def SetTransformParamsSRTXYZ(param, scale, rotate, translate, time): ...
def _AppendMatrix(attr, matrixParam, shutterOpenTime, timeWindowDuration, timeNumSamples, sampleOffset): ...
def _AppendRotate(attr, param, shutterOpenTime, timeWindowDuration, timeNumSamples, sampleOffset): ...
def _AppendRotateX(attr, param, shutterOpenTime, timeWindowDuration, timeNumSamples, sampleOffset): ...
def _AppendRotateY(attr, param, shutterOpenTime, timeWindowDuration, timeNumSamples, sampleOffset): ...
def _AppendRotateZ(attr, param, shutterOpenTime, timeWindowDuration, timeNumSamples, sampleOffset): ...
def _AppendScale(attr, prm, shutterOpenTime, timeWindowDuration, timeNumSamples, sampleOffset): ...
def _AppendTransformItem(inGroup, itemName, itemAttr): ...
def _AppendTranslate(attr, prm, shutterOpenTime, timeWindowDuration, timeNumSamples, sampleOffset): ...
