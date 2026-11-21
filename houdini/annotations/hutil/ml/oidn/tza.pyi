import os
from types import TracebackType
from typing import Self, TypeAlias

import numpy as np
from numpy.typing import NDArray

_StrPath: TypeAlias = str | os.PathLike[str]
_TensorArray: TypeAlias = NDArray[np.float32 | np.float16 | np.int8 | np.uint8]

VERSION: tuple[int, int]

class Writer:
    def __init__(self, filename: _StrPath) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
    def write(self, name: str, tensor: _TensorArray, layout: str) -> None: ...
    def close(self) -> None: ...

class Reader:
    filename: _StrPath
    def __init__(self, filename: _StrPath) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, name: str) -> tuple[_TensorArray, str]: ...
