import enum
import torch.nn

class Normalization(enum.Enum):
    """
    Enumeration of supported normalization types
    """
    Empty = 0
    Batch = 1
    Instance = 2
    def normalization(self, num_features: int) -> torch.nn.BatchNorm2d | torch.nn.InstanceNorm2d | None:
        """
        Returns the an instance of the torch.nn.Module that 
        corresponds to the enum for the specified number of
        features
        """
