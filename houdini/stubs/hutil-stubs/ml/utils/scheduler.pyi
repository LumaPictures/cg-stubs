# Houdini stubs generated from Houdini 22.0.466

import enum
import torch.optim
import torch.optim.lr_scheduler
from collections.abc import Callable as Callable
from hutil.ml.utils.menu import indexed_menu as indexed_menu

class Scheduler(enum.Enum):
    """
    Enumeration of supported learning rate schedulers
    """
    Cosine_Annealing = 0
    Linear = 1
    Step = 2
    Exponential = 3
    @classmethod
    def menu(cls) -> list[str]:
        """
        Returns a parm menu entry list that matches the values
        specified in this enum
        """

class SchedulerExponentialStyle(enum.Enum):
    """
    How the multiplicative factor of learning rate decay is specified
    """
    Multiplicative_Factor = 0
    End_Learning_Rate = 1
    @classmethod
    def menu(cls) -> list[str]:
        """
        Returns a parm menu entry list that matches the values
        specified in this enum
        """

class SchedulerConfig:
    """
    Configuration options for defining a learning rate scheduler
    """
    scheduler: Scheduler
    epochs: int
    start_learning_rate: float
    linear_decay: int
    step_size: int
    step_gamma: float
    exponential_style: SchedulerExponentialStyle
    exponential_gamma: float
    exponential_end_learning_rate: float
    def __init__(self, scheduler: Scheduler = ...) -> None: ...
    def dump(self, printer: Callable[[str], object]) -> None:
        """
        Prints the details about this configuration object using the
        specified print function
        """
    def create(self, optimizer: torch.optim.Optimizer) -> torch.optim.lr_scheduler.CosineAnnealingLR | torch.optim.lr_scheduler.LambdaLR | torch.optim.lr_scheduler.StepLR | torch.optim.lr_scheduler.ExponentialLR:
        """
        Creates a learning rate scheduler from the specified optimizer
        and the settings on this configuration object
        """
