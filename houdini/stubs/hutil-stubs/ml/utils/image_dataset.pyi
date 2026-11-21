import torch
from PIL import Image
from collections.abc import Callable as Callable, Sequence
from hutil.ml.utils.color_config import ColorConfig as ColorConfig
from hutil.ml.utils.storage import Storage as Storage
from torch.utils.data import Dataset

def load_exr(image_file: str) -> torch.Tensor: ...
def load_image(image_file: str) -> Image.Image | torch.Tensor: ...

class SingleImageDataset(Dataset):
    """
    Defines a dataset that consists of N individual image files. It represents
    a dataset containing that contains a single training or test sample.
    """
    tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor]
    image_transform: Callable[[torch.Tensor], torch.Tensor]
    image_files: Sequence[str]
    tensors: list[torch.Tensor]
    def __init__(self, device: torch.device | str, storage_type: Storage, image_files: Sequence[str], tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor], image_transform: Callable[[torch.Tensor], torch.Tensor], channels: int = 0, color_config: ColorConfig | None = None) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> tuple[torch.Tensor, ...]: ...

class MultipleImageDataset(Dataset):
    """
    Defines a dataset that consists of a multiple images loaded from N
    distinct input directories. The directory contents are sorted based on
    file name before loading images -- it's up to the user to ensure that the
    files are correctly named/paired across the directories. Images can also
    be treated as unpaired.
    """
    tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor]
    image_transform: Callable[[torch.Tensor], torch.Tensor]
    image_files: list[list[str]]
    paired: bool
    size: int
    tensors: list[list[torch.Tensor]]
    def __init__(self, device: torch.device | str, storage_type: Storage, image_directories: Sequence[str], tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor], image_transform: Callable[[torch.Tensor], torch.Tensor], max_images: int = 0, channels: int = 0, color_config: ColorConfig | None = None, paired: bool = True) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> tuple[torch.Tensor, ...]: ...

class CompositeImageDataset(Dataset):
    """
    Defines an image dataset that consists of composite images that contain
    their data side-by-side in the same image.
    """
    image_count: int
    tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor]
    image_transform: Callable[[torch.Tensor], torch.Tensor]
    image_files: list[str]
    size: int
    tensors: list[list[torch.Tensor]]
    def __init__(self, device: torch.device | str, storage_type: Storage, image_directory: str, image_count: int, tensor_transform: Callable[[Image.Image | torch.Tensor], torch.Tensor], image_transform: Callable[[torch.Tensor], torch.Tensor], max_images: int = 0, channels: int = 0, color_config: ColorConfig | None = None) -> None:
        """
        Configures the dataset using the specified root directory, image
        channel count, and image size
        """
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> tuple[torch.Tensor, ...]: ...
