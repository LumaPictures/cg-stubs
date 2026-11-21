# Houdini stubs generated from Houdini 22.0.466

import torch
from collections.abc import Callable as Callable
from hutil.ml.gan.config import DataConfig as DataConfig, TrainingConfig as TrainingConfig
from hutil.ml.utils.image_dataset import CompositeImageDataset as CompositeImageDataset, MultipleImageDataset as MultipleImageDataset, SingleImageDataset as SingleImageDataset
from hutil.ml.utils.initializer import Initializer as Initializer
from hutil.ml.utils.plotter import CSVPlotter as CSVPlotter, MatPlotLibPlotter as MatPlotLibPlotter, PlotType as PlotType
from hutil.ml.utils.storage import Storage as Storage
from torch.utils.data import DataLoader

class BaseGANModel:
    """
    Base class for GAN models
    """
    input_config: DataConfig
    test_config: DataConfig | None
    training_config: TrainingConfig
    callback_step_start: Callable[[int], object] | None
    callback_step_end: Callable[[int], object] | None
    callback_abort: Callable[[int], object] | None
    callback_test: Callable[[int, int, list[str]], object] | None
    callback_checkpoint: Callable[[int, str], object] | None
    callback_onnx: Callable[[int, str], object] | None
    callback_print: Callable[[str], object]
    callback_attribute: Callable[[int, str, float | list[float]], object] | None
    training_data_source: SingleImageDataset | MultipleImageDataset | CompositeImageDataset | None
    training_data: DataLoader[tuple[torch.Tensor, ...]]
    test_data_source: SingleImageDataset | MultipleImageDataset | CompositeImageDataset | None
    test_data: DataLoader[tuple[torch.Tensor, ...]] | None
    def __init__(self, input_config: DataConfig | None = None, test_config: DataConfig | None = None, training_config: TrainingConfig | None = None) -> None: ...
