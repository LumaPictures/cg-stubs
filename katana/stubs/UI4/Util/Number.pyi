# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import NodegraphAPI as NodegraphAPI
import PyFCurve as PyFCurve
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from typing import Set, Tuple

def BakeToCurve(policy): ...
def ExportCurveToFile(policy, defaultOptions): ...
def ImportCurveFromFile(policy, context: str = ...): ...
