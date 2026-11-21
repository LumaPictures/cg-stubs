from collections.abc import Callable, Iterable

import torch
import torch.optim

class Optimizer:
    @classmethod
    def menu(cls) -> list[str]: ...

class OptimizerConfig:
    optimizer: Optimizer
    learning_rate: float
    adam_betas: tuple[float, float]
    adadelta_rho: float
    sgd_momentum: float
    def __init__(self, optimizer: Optimizer = ...) -> None: ...
    def dump(self, printer: Callable[[str], object]) -> None: ...
    def create(
        self, parameters: Iterable[torch.Tensor]
    ) -> torch.optim.Adam | torch.optim.Adadelta | torch.optim.SGD | torch.optim.ASGD: ...
