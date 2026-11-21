from collections.abc import Sequence

from hutil.ml.utils.plotter import CSVPlotter

class NCATrainingMonitor:
    plot_base_path: str
    plotter: CSVPlotter
    comp_plotter: CSVPlotter
    current_step: int | None
    def __init__(self, plot_base_path: str) -> None: ...
    def log_training_step(
        self,
        step: int,
        loss: float,
        overflow_loss: float | None = ...,
        ot_loss: float | None = ...,
        autocorr_loss: float | None = ...,
        **kwargs: float,
    ) -> None: ...
    def replay_history(
        self, loss_log: Sequence[float], start_step: int = ..., log_interval: int = ...
    ) -> None: ...
    def close(self) -> None: ...

def create_monitor(plot_base_path: str) -> NCATrainingMonitor | None: ...
