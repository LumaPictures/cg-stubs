# Houdini stubs generated from Houdini 22.0.466

import enum
import torch
import torch.optim
from collections.abc import Callable as Callable, Iterable
from hutil.ml.utils.menu import indexed_menu as indexed_menu

class Optimizer(enum.Enum):
    """
    Enumeration of supported optimizers
    """
    Adam = 0
    Ada_Delta = 1
    SGD = 2
    ASGD = 3
    @classmethod
    def menu(cls) -> list[str]:
        """
        Returns a parm menu entry list that matches the values
        specified in this enum
        """

class OptimizerConfig:
    """
    Defines a configuration object for creating model optimizers
    """
    optimizer: Optimizer
    learning_rate: float
    adam_betas: tuple[float, float]
    adadelta_rho: float
    sgd_momentum: float
    def __init__(self, optimizer: Optimizer = ...) -> None: ...
    def dump(self, printer: Callable[[str], object]) -> None:
        """
        Prints the details about this configuration object using the
        specified print function
        """
    def create(self, parameters: Iterable[torch.Tensor]) -> torch.optim.Adam | torch.optim.Adadelta | torch.optim.SGD | torch.optim.ASGD:
        """
        Constructs an optimizer for the specified parameters, using
        the configuration settings on this instance
        """
