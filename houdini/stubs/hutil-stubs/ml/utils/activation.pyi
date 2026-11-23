import enum
import torch.nn
from hutil.ml.utils.menu import indexed_menu as indexed_menu

class Activation(enum.Enum):
    """
    Enumeration of supported activation types.
    """
    ReLU = 0
    Leaky_ReLU = 1
    RReLU = 2
    Sigmoid = 3
    Tanh = 4
    Log_Softmax = 5
    @classmethod
    def menu(cls) -> list[str]:
        """
        Returns a parm menu entry list that matches the values
        specified in this enum
        """
    def activation(self) -> torch.nn.ReLU | torch.nn.LeakyReLU | torch.nn.RReLU | torch.nn.Sigmoid | torch.nn.Tanh | torch.nn.LogSoftmax | None:
        """
        Returns the an instance of the torch.nn.Module that 
        corresponds to the enum entry
        """
