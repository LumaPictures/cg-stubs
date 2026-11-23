from hutil.ml.utils.plotter import CSVPlotter as CSVPlotter

class GSplatTrainingMonitor:
    """
    Monitors GSplat training progress and logs metrics to CSV for the ML Training Monitor.

    This class uses a callback pattern to minimize intrusion into the training code.
    It logs step-level metrics including losses, learning rates, and model statistics.
    """
    plot_base_path: str
    enable_validation: bool
    plotter: CSVPlotter
    gaussians_plotter: CSVPlotter
    validation_plotter: CSVPlotter
    current_step: int | None
    def __init__(self, plot_base_path: str, enable_validation: bool = True) -> None:
        '''
        Initialize the training monitor.

        Args:
            plot_base_path: Base path for the CSV file (e.g., "logs/plot")
                           Will create plot_base_path + ".csv" for losses
                           and plot_base_path + ".gaussians.csv" for Gaussian count
            enable_validation: Whether to include validation loss tracking
        '''
    def log_training_step(self, step: int, loss: float, l1_loss: float | None = None, ssim_loss: float | None = None, extra_loss: float | None = None, depth_loss: float | None = None, num_gaussians: int | None = None, learning_rate: float | None = None, **kwargs: float) -> None:
        """
        Log metrics for a training step.

        Args:
            step: Current training step
            loss: Total training loss
            l1_loss: L1 component of loss
            ssim_loss: SSIM component of loss
            extra_loss: Extra features loss (if using feature supervision)
            depth_loss: Depth loss (if using depth supervision)
            num_gaussians: Current number of Gaussian splats
            learning_rate: Current learning rate
            **kwargs: Additional metrics to log
        """
    def log_validation_metrics(self, step: int, psnr: float | None = None, ssim: float | None = None, lpips: float | None = None, **kwargs: float) -> None:
        """
        Log validation metrics for a step.

        If log_training_step was already called for this step, this will update
        the existing row. Otherwise, it will create a new row.

        Args:
            step: Current training step
            psnr: Peak Signal-to-Noise Ratio
            ssim: Structural Similarity Index
            lpips: Learned Perceptual Image Patch Similarity
            **kwargs: Additional validation metrics
        """
    def close(self) -> None:
        """Close the plotter and release resources."""

def create_monitor(plot_base_path: str, enable_validation: bool = True) -> GSplatTrainingMonitor | None:
    """
    Factory function to create a training monitor.

    Args:
        plot_base_path: Base path for the CSV file
        enable_validation: Whether to include validation metrics

    Returns:
        GSplatTrainingMonitor instance, or None if plot_base_path is not provided
    """
