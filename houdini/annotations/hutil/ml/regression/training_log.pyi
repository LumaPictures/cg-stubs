from torch.utils.tensorboard import SummaryWriter

from hutil.ml.regression.log import Log
from hutil.ml.utils.plotter import BufferedPlotter

class TrainingLogReportBatchLoss:
    def __init__(
        self,
        log_file: Log | None,
        plotter: BufferedPlotter | None,
        summary_writer: SummaryWriter | None,
        epoch: int,
    ) -> None: ...
    def __call__(self, batch_index: int, batch_loss_sum: float, batch_size: int) -> None: ...

class TrainingLog:
    def __init__(
        self,
        log_file: Log | None,
        plotter: BufferedPlotter | None,
        summary_writer: SummaryWriter | None,
        /,
        *,
        do_batch_loss: bool,
        enable_validation: bool,
    ) -> None: ...
    def __del__(self) -> None: ...
    def write(self, message: str) -> None: ...
    def reportCurrentBest(
        self, best_model_training_loss: float | None, best_model_validation_loss: float | None = ...
    ) -> None: ...
    def startLoop(self, epoch: int) -> None: ...
    def reportBatchFunction(self, epoch: int) -> TrainingLogReportBatchLoss | None: ...
    def reportEpoch(
        self,
        epoch: int,
        training_loss: float,
        detected_improvement: bool | None = ...,
        unimproved_count: int | None = ...,
        validation_loss: float | None = ...,
    ) -> None: ...
    def endLoop(self, epoch: int) -> None: ...

def trainingLogFactory(
    log_file: Log | None,
    /,
    *,
    plot_base_path: str | None = ...,
    tensorboard_folder_path: str | None = ...,
    do_batch_loss: bool = ...,
    enable_validation: bool = ...,
) -> TrainingLog: ...
