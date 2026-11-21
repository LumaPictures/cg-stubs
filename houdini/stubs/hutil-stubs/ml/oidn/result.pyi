# Houdini stubs generated from Houdini 22.0.466

from hutil.ml.oidn.utils import *
import torch
from typing import Any, Literal, Protocol, TypedDict

class _ResultConfig(Protocol):
    @property
    def result(self) -> str: ...
    @property
    def results_dir(self) -> str: ...

class _Checkpoint(TypedDict):
    epoch: int
    step: int
    model_state: dict[str, torch.Tensor]
    optimizer_state: dict[str, Any]

def get_result_dir(cfg: _ResultConfig, result: str | None = None) -> str:
    """
    Gets the path to the result directory
    """
def get_checkpoint_dir(result_dir: str) -> str:
    """
    Gets the path to the result checkpoint directory
    """
def get_checkpoint_filename(result_dir: str, epoch: int) -> str:
    """
    Gets the path to a checkpoint file
    """
def get_checkpoint_state_filename(result_dir: str) -> str:
    """
    Gets the path to the file that contains the checkpoint state (latest epoch)
    """
def validate_latest_checkpoint_epoch(result_dir: str) -> bool: ...
def get_latest_checkpoint_epoch(result_dir: str) -> int:
    """
    Gets the latest checkpoint epoch
    """
def get_result_log_dir(result_dir: str) -> str:
    """
    Gets the path to result log directory
    """
def save_checkpoint(result_dir: str, epoch: int, step: int, model: torch.nn.Module, optimizer: torch.optim.Optimizer) -> None:
    """
    Saves a training checkpoint
    """
def validate_checkpoint(result_dir: str, device: torch.device, epoch: int | None = None) -> tuple[Literal[False], None] | tuple[Literal[True], _Checkpoint]:
    """
    Validates the checkpoint from the result directory
    Returns tuple where first entry is True if the checkpoint is valid,
    and False otherwise
    """
def load_checkpoint(result_dir: str, device: torch.device, epoch: int | None = None, model: torch.nn.Module | None = None, optimizer: torch.optim.Optimizer | None = None) -> _Checkpoint:
    """
    Loads and returns a training checkpoint
    """
