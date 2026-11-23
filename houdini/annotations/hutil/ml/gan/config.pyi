from collections.abc import Callable, Sequence

import torch

from hutil.ml.gan.dataset_type import DatasetType
from hutil.ml.gan.paired_model import PairedGANModel
from hutil.ml.gan.unpaired_model import UnpairedGANModel
from hutil.ml.utils.activation import Activation
from hutil.ml.utils.color_config import ColorConfig
from hutil.ml.utils.image_dataset import CompositeImageDataset, MultipleImageDataset, SingleImageDataset
from hutil.ml.utils.initializer import Initializer
from hutil.ml.utils.optimizer import OptimizerConfig
from hutil.ml.utils.plotter import PlotType
from hutil.ml.utils.scheduler import SchedulerConfig
from hutil.ml.utils.storage import Storage

class DataConfig:
    dataset_type: DatasetType
    storage_type: Storage
    device_name: str
    device: torch.device
    training: bool
    batch_size: int
    single_input: str
    single_reference: str
    input_dir: str
    reference_dir: str
    composite_dir: str
    crop_ratio: float
    horizontal_flip: float
    vertical_flip: float
    rotation: float
    max_images: int
    input_channels: int
    image_size: int
    workers: int
    shuffle: bool
    color_config_file: str
    color_src_space: str
    color_dst_space: str
    color_correct: bool
    color_gamma: float
    color_config: ColorConfig | None
    def __init__(
        self,
        dataset_type: DatasetType,
        storage_type: Storage,
        device_name: str,
        training: bool = ...,
        batch_size: int = ...,
        single_input: str = ...,
        single_reference: str = ...,
        input_dir: str = ...,
        reference_dir: str = ...,
        composite_dir: str = ...,
        crop_ratio: float = ...,
        horizontal_flip: float = ...,
        vertical_flip: float = ...,
        rotation: float = ...,
        max_images: int = ...,
        input_channels: int = ...,
        image_size: int = ...,
        workers: int = ...,
        shuffle: bool = ...,
        color_config_file: str = ...,
        color_src_space: str = ...,
        color_dst_space: str = ...,
        color_correct: bool = ...,
        color_gamma: float = ...,
    ) -> None: ...
    def dump(self, printer: Callable[[str], object]) -> None: ...
    def create_dataset(self) -> SingleImageDataset | MultipleImageDataset | CompositeImageDataset | None: ...

class TrainingConfig:
    device_name: str
    device: torch.device
    optimizer: OptimizerConfig
    scheduler: SchedulerConfig
    initializer: Initializer
    initializer_gain: float
    generator_lambda: float
    generator_size: int
    generator_layers: Sequence[int]
    generator_down: Activation
    generator_up: Activation
    discriminator_size: int
    discriminator_layers: Sequence[int]
    discriminator_activation: Activation
    test_dir: str
    test_rate: int
    test_count: int
    test_target_ssim: float
    checkpoint_rate: int
    checkpoint_format: str
    onnx_rate: int
    onnx_format: str
    onnx_version: int
    onnx_dynamic: bool
    onnx_preprocess: bool
    plot_rate: int
    plot_type: PlotType
    ssim_plot_format: str
    loss_plot_format: str
    score_plot_format: str
    load_checkpoints: bool
    def __init__(
        self,
        device_name: str,
        optimizer: OptimizerConfig = ...,
        scheduler: SchedulerConfig = ...,
        initializer: Initializer = ...,
        initializer_gain: float = ...,
        generator_size: int = ...,
        generator_lambda: float = ...,
        generator_down: Activation = ...,
        generator_up: Activation = ...,
        generator_layers: Sequence[int] = ...,
        discriminator_size: int = ...,
        discriminator_activation: Activation = ...,
        discriminator_layers: Sequence[int] = ...,
        test_dir: str = ...,
        test_rate: int = ...,
        test_count: int = ...,
        test_target_ssim: float = ...,
        checkpoint_rate: int = ...,
        checkpoint_format: str = ...,
        onnx_rate: int = ...,
        onnx_format: str = ...,
        onnx_version: int = ...,
        onnx_dynamic: bool = ...,
        onnx_preprocess: bool = ...,
        plot_rate: int = ...,
        plot_type: PlotType = ...,
        ssim_plot_format: str = ...,
        loss_plot_format: str = ...,
        score_plot_format: str = ...,
        load_checkpoints: bool = ...,
    ) -> None: ...
    def dump(self, printer: Callable[[str], object]) -> None: ...
    def create_model(self, input_config: DataConfig, test_config: DataConfig | None) -> PairedGANModel | UnpairedGANModel: ...
