import torch

class ColorConfig:
    """
    Color space configuration info for an image dataset
    """
    src_space: str
    dst_space: str
    config_file: str
    def __init__(self, src_space: str = '', dst_space: str = '', config_file: str = '') -> None: ...
    def convertInput(self, tensor: torch.Tensor) -> torch.Tensor:
        """
        Converts an input tensor in the source color space into an tensor
        in the destination color space
        """
    def convertOutput(self, tensor: torch.Tensor) -> torch.Tensor:
        """
        Converts an output tensor in the destination color space into an tensor
        in the source color space
        """
