import ignite.metrics
import torch
import torch.nn
import torch.optim
import torch.optim.lr_scheduler

from hutil.ml.gan.base_model import BaseGANModel
from hutil.ml.gan.config import DataConfig, TrainingConfig
from hutil.ml.gan.discriminator import Discriminator
from hutil.ml.gan.generator import UNetGenerator
from hutil.ml.utils.plotter import CSVPlotter, MatPlotLibPlotter

class UnpairedGANModel(BaseGANModel):
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
    def __init__(
        self,
        input_config: DataConfig | None = ...,
        test_config: DataConfig | None = ...,
        training_config: TrainingConfig | None = ...,
    ) -> None: ...
    def train(self) -> None: ...
