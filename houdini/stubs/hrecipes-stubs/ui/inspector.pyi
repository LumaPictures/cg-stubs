import PySide6.QtCore
import PySide6.QtWidgets
from .. import api as api, models as models, utils as utils
from .viewer import RecipeDataViewer as RecipeDataViewer
from hutil.PySide import QtWidgets
from typing import ClassVar, Sequence

class RecipeDataInspector(QtWidgets.QDialog):
    """ Dialog for inspecting and comparing recipe data (wip)
    """
    diffChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, refs: Sequence[api.Ref], parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def start(self, diff_dir: str) -> int:
        """ Start a diff tool for comparing the 2 recipes being 
            inspected. The inspector uses the diff tool configured
            with the external tool preferences. 
            
            Return values:
            1: launching the diff tool was sucessful
            0: No diff tool found.
            -1: Diff tool launch failed 
        """
