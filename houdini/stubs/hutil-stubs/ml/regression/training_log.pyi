# Houdini stubs generated from Houdini 22.0.466

from hutil.ml.regression.log import Log as Log
from hutil.ml.utils.plotter import BufferedPlotter as BufferedPlotter, CSVPlotter as CSVPlotter, MatPlotLibPlotter as MatPlotLibPlotter, PlotType as PlotType
from torch.utils.tensorboard import SummaryWriter

class TrainingLogReportBatchLoss:
    """
    This helper class is passed down to mini-batch training for
    the purpose of reporting partial training losses.
    """
    def __init__(self, log_file: Log | None, plotter: BufferedPlotter | None, summary_writer: SummaryWriter | None, epoch: int) -> None: ...
    def __call__(self, batch_index: int, batch_loss_sum: float, batch_size: int) -> None: ...

class TrainingLog:
    """
    This class can be used with hutil.ml.regression.training_loop.trainEpochs.
    
    This class is responsible for logging all relevant training statistics,
    including the training losses and the validation losses (optional).
    """
    def __init__(self, log_file: Log | None, plotter: BufferedPlotter | None, summary_writer: SummaryWriter | None, /, *, do_batch_loss: bool, enable_validation: bool) -> None:
        """
        enable_validation == True:
            validation losses are being evaluated and should be logged
        enable_early_stopping == True:
            early stopping based on validation losses is enabled
            (validate must be true in this case)
        """
    def __del__(self) -> None: ...
    def write(self, message: str) -> None: ...
    def reportCurrentBest(self, best_model_training_loss: float | None, best_model_validation_loss: float | None = None) -> None: ...
    def startLoop(self, epoch: int) -> None: ...
    def reportBatchFunction(self, epoch: int) -> TrainingLogReportBatchLoss | None: ...
    def reportEpoch(self, epoch: int, training_loss: float, detected_improvement: bool | None = None, unimproved_count: int | None = None, validation_loss: float | None = None) -> None: ...
    def endLoop(self, epoch: int) -> None: ...

def trainingLogFactory(log_file: Log | None, /, *, plot_base_path: str | None = None, tensorboard_folder_path: str | None = None, do_batch_loss: bool = False, enable_validation: bool = False) -> TrainingLog: ...
