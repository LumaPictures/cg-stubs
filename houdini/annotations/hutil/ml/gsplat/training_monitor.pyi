from hutil.ml.utils.plotter import CSVPlotter

class GSplatTrainingMonitor:
    plot_base_path: str
    enable_validation: bool
    plotter: CSVPlotter
    gaussians_plotter: CSVPlotter
    validation_plotter: CSVPlotter
    current_step: int | None
    def __init__(self, plot_base_path: str, enable_validation: bool = ...) -> None: ...
    def log_training_step(
        self,
        step: int,
        loss: float,
        l1_loss: float | None = ...,
        ssim_loss: float | None = ...,
        extra_loss: float | None = ...,
        depth_loss: float | None = ...,
        num_gaussians: int | None = ...,
        learning_rate: float | None = ...,
        **kwargs: float,
    ) -> None: ...
    def log_validation_metrics(
        self,
        step: int,
        psnr: float | None = ...,
        ssim: float | None = ...,
        lpips: float | None = ...,
        **kwargs: float,
    ) -> None: ...
    def close(self) -> None: ...

def create_monitor(plot_base_path: str, enable_validation: bool = ...) -> GSplatTrainingMonitor | None: ...
