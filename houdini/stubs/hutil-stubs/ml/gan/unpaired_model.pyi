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

class UnpairedGANModel(BaseGANModel):
    """
    Defines a UNet GAN model with two discriminators and generators. Optimizes
    for G_B(G_A(input_A)) == input_A and G_A(G_B(input_B)) == input_B for
    unpaired input images.
    """
    discriminators: list[Discriminator]
    generators: list[UNetGenerator]
    optimizer_d: torch.optim.Optimizer
    optimizer_g: torch.optim.Optimizer
    scheduler_d: torch.optim.lr_scheduler.LRScheduler
    scheduler_g: torch.optim.lr_scheduler.LRScheduler
    gan_loss: torch.nn.BCEWithLogitsLoss
    cycle_loss: torch.nn.L1Loss
    identity_loss: torch.nn.L1Loss
    ssim_train: list[ignite.metrics.SSIM]
    ssim_test: list[ignite.metrics.SSIM]
    ssim_plotters: list[CSVPlotter | MatPlotLibPlotter | None]
    loss_plotters: list[CSVPlotter | MatPlotLibPlotter | None]
    score_plotters: list[CSVPlotter | MatPlotLibPlotter | None]
    def __init__(self, input_config: DataConfig | None = None, test_config: DataConfig | None = None, training_config: TrainingConfig | None = None) -> None: ...
    def train(self) -> None: ...
