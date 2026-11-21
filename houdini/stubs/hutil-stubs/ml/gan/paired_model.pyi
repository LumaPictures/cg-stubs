import ignite.metrics
import torch.nn
import torch.optim
import torch.optim.lr_scheduler
from hutil.ml.gan.base_model import BaseGANModel as BaseGANModel
from hutil.ml.gan.config import DataConfig as DataConfig, TrainingConfig as TrainingConfig
from hutil.ml.gan.discriminator import Discriminator as Discriminator
from hutil.ml.gan.generator import UNetGenerator as UNetGenerator
from hutil.ml.utils.normalization import Normalization as Normalization
from hutil.ml.utils.plotter import CSVPlotter as CSVPlotter, MatPlotLibPlotter as MatPlotLibPlotter

class PairedGANModel(BaseGANModel):
    """
    Defines a UNet GAN model with a discriminator and generator. Pulls
    various configuration options from the input config objects, such as
    the working directory for writing models, the data sources, and the
    training parameters
    """
    discriminator: Discriminator
    generator: UNetGenerator
    optimizer_d: torch.optim.Optimizer
    optimizer_g: torch.optim.Optimizer
    scheduler_d: torch.optim.lr_scheduler.LRScheduler
    scheduler_g: torch.optim.lr_scheduler.LRScheduler
    gan_loss: torch.nn.BCEWithLogitsLoss
    l1_loss: torch.nn.L1Loss
    ssim_train: ignite.metrics.SSIM
    ssim_test: ignite.metrics.SSIM
    ssim_plotter: CSVPlotter | MatPlotLibPlotter | None
    loss_plotter: CSVPlotter | MatPlotLibPlotter | None
    score_plotter: CSVPlotter | MatPlotLibPlotter | None
    def __init__(self, input_config: DataConfig | None = None, test_config: DataConfig | None = None, training_config: TrainingConfig | None = None) -> None: ...
    def train(self) -> None: ...
