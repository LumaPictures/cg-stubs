from collections.abc import Callable

import torch.optim
import torch.optim.lr_scheduler

class Scheduler:
    @classmethod
    def menu(cls) -> list[str]: ...

class SchedulerExponentialStyle:
    @classmethod
    def menu(cls) -> list[str]: ...

class SchedulerConfig:
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
    def dump(self, printer: Callable[[str], object]) -> None: ...
    def create(
        self, optimizer: torch.optim.Optimizer
    ) -> (
        torch.optim.lr_scheduler.CosineAnnealingLR
        | torch.optim.lr_scheduler.LambdaLR
        | torch.optim.lr_scheduler.StepLR
        | torch.optim.lr_scheduler.ExponentialLR
    ): ...
