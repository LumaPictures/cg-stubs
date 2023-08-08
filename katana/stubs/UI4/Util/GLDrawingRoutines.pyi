# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes2DAPI as Nodes2DAPI
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

def drawEllipse(xRadius, yRadius, startAngle, endAngle, steps, filled: bool = ...): ...
def drawSmoothArrow(color, trans, basePt, endPt, lineWidth, filled: bool = ...): ...
def drawSmoothCross(color, trans, px, py, xSize, ySize, lineWidth): ...
def drawSmoothCrosshairs(color, trans, px, py, startRadius, endRadius, lineWidth): ...
def drawSmoothEllipse(color, trans, px, py, xRadius, yRadius, startAngle, endAngle, steps, lineWidth, filled: bool = ...): ...
def drawSmoothHandle(color, trans, edgeSize, px, py, lineWidth, filled: bool = ...): ...
def drawSmoothPoly(color, trans, vertices, lineWidth, stippled: bool = ..., fillColor: Incomplete | None = ...): ...
def drawSmoothText(text, color, trans, px, py, fontSize): ...