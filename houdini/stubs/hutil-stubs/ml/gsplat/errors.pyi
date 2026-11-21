from pdgjob.pdgjson import WorkItem
from typing import Protocol

class _LogWriter(Protocol):
    def write(self, s: str, /) -> object: ...
    def flush(self) -> object: ...

def is_gpu_incompatibility_error(error: BaseException) -> bool:
    '''Return True if `error` is the CUDA "no kernel image is available"
    failure raised when the GPU is too old for the CUDA kernels the installed
    PyTorch build ships.'''
def handle_gpu_incompatibility(error: BaseException, work_item: WorkItem, /, *, log: _LogWriter | None = None) -> bool:
    '''Report an unsupported-GPU CUDA failure as a clean work item error.

    An unsupported GPU (too old for the CUDA kernels the installed PyTorch
    build ships) fails with a "no kernel image is available for execution on
    the device" error -- directly for single-GPU, or re-raised from the worker
    by multiprocessing.spawn for multi-GPU. PyTorch already prints a
    "CUDA capability sm_XX is not compatible" warning with the specifics, so we
    just fail the work item cleanly here instead of surfacing an opaque
    traceback.

    Returns True if `error` was an unsupported-GPU failure (and has been
    reported), otherwise False so the caller can re-raise it.
    '''
