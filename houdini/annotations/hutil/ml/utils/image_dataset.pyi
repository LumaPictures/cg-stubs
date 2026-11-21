from collections.abc import Callable, Sequence

import torch
from PIL import Image

from hutil.ml.utils.color_config import ColorConfig
from hutil.ml.utils.storage import Storage

def load_exr(image_file: str) -> torch.Tensor: ...
def load_image(image_file: str) -> Image.Image | torch.Tensor: ...

class SingleImageDataset:
    tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor]
    image_transform: Callable[[torch.Tensor], torch.Tensor]
    image_files: Sequence[str]
    tensors: list[torch.Tensor]
    def __init__(
        self,
        device: torch.device | str,
        storage_type: Storage,
        image_files: Sequence[str],
        tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor],
        image_transform: Callable[[torch.Tensor], torch.Tensor],
        channels: int = ...,
        color_config: ColorConfig | None = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> tuple[torch.Tensor, ...]: ...

class MultipleImageDataset:
    tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor]
    image_transform: Callable[[torch.Tensor], torch.Tensor]
    image_files: list[list[str]]
    paired: bool
    size: int
    tensors: list[list[torch.Tensor]]
    def __init__(
        self,
        device: torch.device | str,
        storage_type: Storage,
        image_directories: Sequence[str],
        tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor],
        image_transform: Callable[[torch.Tensor], torch.Tensor],
        max_images: int = ...,
        channels: int = ...,
        color_config: ColorConfig | None = ...,
        paired: bool = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> tuple[torch.Tensor, ...]: ...

class CompositeImageDataset:
    image_count: int
    tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor]
    image_transform: Callable[[torch.Tensor], torch.Tensor]
    image_files: list[str]
    size: int
    tensors: list[list[torch.Tensor]]
    def __init__(
        self,
        device: torch.device | str,
        storage_type: Storage,
        image_directory: str,
        image_count: int,
        tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor],
        image_transform: Callable[[torch.Tensor], torch.Tensor],
        max_images: int = ...,
        channels: int = ...,
        color_config: ColorConfig | None = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> tuple[torch.Tensor, ...]: ...
