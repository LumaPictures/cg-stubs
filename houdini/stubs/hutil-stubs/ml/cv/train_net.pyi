# Houdini stubs generated from Houdini 22.0.466

import argparse
from collections.abc import Iterable
from detectron2.config import LazyConfig as LazyConfig, get_cfg as get_cfg
from detectron2.engine import train_loop
from detectron2.model_zoo import get_config as get_config
from detectron2.modeling import build_model as build_model
from detectron2.solver.build import get_default_optimizer_params as get_default_optimizer_params
from detectron2.utils.events import EventWriter
from hutil.ml.cv.config import _CVTrainParms, modelConfig as modelConfig
from hutil.ml.cv.data.validate import ValidationHook as ValidationHook
from hutil.ml.cv.data.visualize import VisualizerHook as VisualizerHook
from hutil.ml.cv.onnx_export import OnnxExportHook as OnnxExportHook
from hutil.ml.cv.train import epochToIter as epochToIter, iterToEpoch as iterToEpoch
from hutil.ml.utils.plotter import CSVPlotter as CSVPlotter
from omegaconf import DictConfig as DictConfig
from pdgjob.pdgjson import WorkItem

class BatchHook(train_loop.HookBase):
    def __init__(self, work_item: WorkItem, parms: _CVTrainParms) -> None: ...
    def before_step(self) -> None: ...
    def after_train(self) -> None: ...

class LossPlotter(EventWriter):
    def __init__(self, parms: _CVTrainParms, max_iter: int, plot_path: str) -> None: ...
    def write(self) -> None: ...

class DatasetManager:
    @staticmethod
    def validateDatasets(parms: _CVTrainParms) -> list[str]:
        """
        Manage dataset extraction and validation 
        """

class DirectoryManager:
    """
    Manage directory creation and validation
    """
    @staticmethod
    def createDirs(paths: Iterable[str]) -> None: ...

def do_train(args: argparse.Namespace, cfg: DictConfig, work_item: WorkItem, parms: _CVTrainParms) -> None: ...
def setup(args: argparse.Namespace, work_item: WorkItem, parms: _CVTrainParms) -> DictConfig: ...
def main(args: argparse.Namespace) -> None: ...
def invoke_main() -> None: ...
