from collections.abc import Sequence
from typing import ClassVar
import PySide6.QtCore
import PySide6.QtWidgets

from hrecipes import api

class RecipeDataInspector:
    diffChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, refs: Sequence[api.Ref], parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def start(self, diff_dir: str) -> int: ...
