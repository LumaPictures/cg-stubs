# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Sequence
from hutil.ml.utils.plotter import CSVPlotter as CSVPlotter

class NCATrainingMonitor:
    """
    Monitors NCA training progress and logs metrics to CSV for the ML Training Monitor.

    This class uses a callback pattern to minimize intrusion into the training code.
    It logs step-level metrics including losses, learning rates, and model statistics.
    """
    plot_base_path: str
    plotter: CSVPlotter
    comp_plotter: CSVPlotter
    current_step: int | None
    def __init__(self, plot_base_path: str) -> None:
        '''
        Initialize the training monitor.

        Args:
            plot_base_path: Base path for the CSV file (e.g., "logs/plot")
                           Will create plot_base_path + ".csv" for losses
        '''
    def log_training_step(self, step: int, loss: float, overflow_loss: float | None = None, ot_loss: float | None = None, autocorr_loss: float | None = None, **kwargs: float) -> None:
        """
        Log metrics for a training step.

        Args:
            step: Current training step
            loss: Total training loss
            overflow_loss: Overflow loss component
            ot_loss: Optimal transport style loss component
            autocorr_loss: Autocorrelation loss component
            **kwargs: Additional metrics to log
        """
    def replay_history(self, loss_log: Sequence[float], start_step: int = 0, log_interval: int = 1) -> None:
        """
        Replay historical loss values to the plotter.

        This is used when resuming from a checkpoint to restore the plot
        with all previous training data before continuing.

        Args:
            loss_log: List of loss values from previous training
            start_step: Step number of the first entry in loss_log
            log_interval: Interval between consecutive entries
        """
    def close(self) -> None:
        """Close the plotter and release resources."""

def create_monitor(plot_base_path: str) -> NCATrainingMonitor | None:
    """
    Factory function to create a training monitor.

    Args:
        plot_base_path: Base path for the CSV file

    Returns:
        NCATrainingMonitor instance, or None if plot_base_path is not provided
    """
