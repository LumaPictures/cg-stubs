# Houdini stubs generated from Houdini 22.0.466

import enum
from hutil.ml.utils.menu import indexed_menu as indexed_menu

class DatasetType(enum.Enum):
    """
    Enumeration of supported dataset types
    """
    Single_Paired = 0
    Multiple_Paired = 1
    Multiple_Unpaired = 2
    Composite_Paired = 3
    @classmethod
    def menu(cls) -> list[str]:
        """
        Returns a parm menu entry list that matches the values
        specified in this enum
        """
