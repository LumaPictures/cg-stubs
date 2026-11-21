# Houdini stubs generated from Houdini 22.0.466

import enum
import torch
from hutil.ml.utils.menu import indexed_menu as indexed_menu

class Initializer(enum.Enum):
    """
    Enumeration of supported weight initializers
    """
    Constant = 0
    Normal = 1
    Orthogonal = 2
    @classmethod
    def menu(cls) -> list[str]:
        """
        Returns a parm menu entry list that matches the values
        specified in this enum
        """
    def initialize(self, tensor: torch.Tensor, mean: float, gain: float) -> None:
        """
        Initializes the specified tensor using the initializer
        function that corresponds to the enum entry
        """
