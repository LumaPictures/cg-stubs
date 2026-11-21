from hutil.ml.utils.image_dataset import *
import torch
from collections.abc import Callable as Callable, Sequence
from hutil.ml.gan.dataset_type import DatasetType as DatasetType
from hutil.ml.gan.paired_model import PairedGANModel as PairedGANModel
from hutil.ml.gan.unpaired_model import UnpairedGANModel as UnpairedGANModel
from hutil.ml.utils.activation import Activation as Activation
from hutil.ml.utils.color_config import ColorConfig as ColorConfig
from hutil.ml.utils.image_dataset import CompositeImageDataset as CompositeImageDataset, MultipleImageDataset as MultipleImageDataset, SingleImageDataset as SingleImageDataset
from hutil.ml.utils.initializer import Initializer as Initializer
from hutil.ml.utils.optimizer import OptimizerConfig as OptimizerConfig
from hutil.ml.utils.plotter import PlotType as PlotType
from hutil.ml.utils.scheduler import SchedulerConfig as SchedulerConfig
from hutil.ml.utils.storage import Storage as Storage

class DataConfig:
    """
    Configuration options for input image data, e.g the location, size
    and channel count for the inputs
    """
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
    def __init__(self, dataset_type: DatasetType, storage_type: Storage, device_name: str, training: bool = True, batch_size: int = 1, single_input: str = '', single_reference: str = '', input_dir: str = '', reference_dir: str = '', composite_dir: str = '', crop_ratio: float = 1.0, horizontal_flip: float = 0.0, vertical_flip: float = 0.0, rotation: float = 0.0, max_images: int = 0, input_channels: int = 1, image_size: int = 512, workers: int = 0, shuffle: bool = True, color_config_file: str = '', color_src_space: str = '', color_dst_space: str = '', color_correct: bool = False, color_gamma: float = 0.0) -> None: ...
    def dump(self, printer: Callable[[str], object]) -> None:
        """
        Prints a summary of the settings
        """
    def create_dataset(self) -> SingleImageDataset | MultipleImageDataset | CompositeImageDataset | None:
        """
        Creates a dataset from the config
        """

class TrainingConfig:
    """
    Configuration options for the model training process, e.g. learning
    rates, optimizer settings, save rate, etc
    """
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
    def __init__(self, device_name: str, optimizer: OptimizerConfig = ..., scheduler: SchedulerConfig = ..., initializer: Initializer = ..., initializer_gain: float = 0.02, generator_size: int = 4, generator_lambda: float = 100, generator_down: Activation = ..., generator_up: Activation = ..., generator_layers: Sequence[int] = [64, 128, 256, 512, 512, 512, 512, 512], discriminator_size: int = 4, discriminator_activation: Activation = ..., discriminator_layers: Sequence[int] = [64, 128, 256, 512], test_dir: str = '', test_rate: int = 2, test_count: int = 10, test_target_ssim: float = 0.0, checkpoint_rate: int = 25, checkpoint_format: str = '{network}.pth.tar', onnx_rate: int = 25, onnx_format: str = 'model.{epoch}.onnx', onnx_version: int = 10, onnx_dynamic: bool = False, onnx_preprocess: bool = True, plot_rate: int = 5, plot_type: PlotType = ..., ssim_plot_format: str = 'ssim.{index}.{epoch}.png', loss_plot_format: str = 'loss.{index}.{epoch}.png', score_plot_format: str = 'score.{index}.{epoch}.png', load_checkpoints: bool = False) -> None: ...
    def dump(self, printer: Callable[[str], object]) -> None:
        """
        Prints a summary of the settings
        """
    def create_model(self, input_config: DataConfig, test_config: DataConfig | None) -> PairedGANModel | UnpairedGANModel: ...
