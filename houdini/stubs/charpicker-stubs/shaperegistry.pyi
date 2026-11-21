from collections.abc import Callable as Callable
from enum import Enum, StrEnum
from hutil.PySide import QtCore, QtGui

SHAPES_CATALOG_NAME: str
SHAPES_CATALOG_SOURCE: str

class Shape(StrEnum):
    RECTANGLE = 'rectangle'
    SQUARE = 'square'
    CIRCLE = 'circle'
    OVAL = 'oval'
    CAPSULE = 'capsule'
    DIRECTION = 'direction'
    DIAMOND = 'diamond'
    ARROW = 'arrow'
    TRIANGLE = 'triangle'
    RING = 'ring'
    HALF_CIRCLE = 'half_circle'
    HALF_RING = 'half_ring'
    QUARTER_CIRCLE = 'quarter_circle'
    QUARTER_RING = 'quarter_ring'

class ShapeCategory(Enum):
    """Whether a shape enforces equal width and height."""
    SYMMETRIC = 0
    ASYMMETRIC = 1

class ShapeDefinition:
    """Describes how to create and constrain a single shape type."""
    name: str
    display_name: str
    category: ShapeCategory
    default_aspect: float
    text_v_offset: float
    def __init__(self, name: str, display_name: str, category: ShapeCategory, default_aspect: float, path_factory: Callable[[QtCore.QRectF], QtGui.QPainterPath] | None, text_v_offset: float = 0.0) -> None: ...
    def createPath(self, rect: QtCore.QRectF) -> QtGui.QPainterPath: ...
    def isSymmetric(self) -> bool: ...
    def render(self, painter: QtGui.QPainter, rect: QtCore.QRectF, fill_color: QtGui.QColor, border_color: QtGui.QColor | None = None) -> None:
        """Draw the shape. Default uses QPainterPath."""
    def getClipPath(self, rect: QtCore.QRectF) -> QtGui.QPainterPath:
        """Return path for text clipping. Default: shape path."""
    def containsPoint(self, rect: QtCore.QRectF, point: QtCore.QPointF) -> bool:
        """Hit test. Default: path.contains()."""
    def createRegion(self, rect: QtCore.QRectF) -> QtGui.QRegion:
        """Return a QRegion for the shape at the given rect."""
    def strokeMargin(self) -> int:
        """Return the pixel margin needed for this shape's stroke."""

class SvgShapeDefinition(ShapeDefinition):
    """Shape backed by an SVG file with sentinel accent colors."""
    class Element(Enum):
        BASE = 0
        OUTLINE = 1
        INNER_SHADOW = 2
    ELEMENT_VALUES: dict['SvgShapeDefinition.Element', float]
    @staticmethod
    def elementRatio(element: SvgShapeDefinition.Element) -> float: ...
    def __init__(self, name: str, display_name: str, category: ShapeCategory, svg_path: str, default_aspect: float | None = None, text_v_offset: float = 0.0) -> None: ...
    def getSvgTemplate(self) -> str: ...
    @staticmethod
    def deriveElementColor(fill_color: QtGui.QColor, element: SvgShapeDefinition.Element) -> QtGui.QColor:
        """Derive an SVG element color from the user's fill color.

        Scales the HSV value component proportionally to the element's
        brightness relative to the base element.
        """
    def renderThumbnail(self, size: int = 128) -> bytes:
        """Render this shape to a PNG thumbnail as bytes."""
    def createPath(self, rect: QtCore.QRectF) -> QtGui.QPainterPath:
        """Fallback path: bounding rect (used for partial-selection border)."""
    def render(self, painter: QtGui.QPainter, rect: QtCore.QRectF, fill_color: QtGui.QColor, border_color: QtGui.QColor | None = None) -> None: ...
    def strokeMargin(self) -> int: ...
    def containsPoint(self, rect: QtCore.QRectF, point: QtCore.QPointF) -> bool: ...
    def getClipPath(self, rect: QtCore.QRectF) -> QtGui.QPainterPath: ...
    def createRegion(self, rect: QtCore.QRectF) -> QtGui.QRegion: ...

class ShapeCatalog:
    def __init__(self) -> None: ...
    def refresh(self) -> None: ...
    def getShapeDefinition(self, name: str) -> ShapeDefinition: ...
    def getDefaultShape(self) -> str: ...
    def setDefaultShape(self, name: str) -> None: ...
    def shapeNameFromItemId(self, item_id: str) -> str | None:
        """Return the shape name stored for a catalog item, or None."""
    def allShapes(self) -> list[ShapeDefinition]: ...

def createStrokerPath(path: QtGui.QPainterPath, width: float) -> QtGui.QPainterPath:
    """Return the outline of *path* widened by *width*, useful for edge
    detection (hit-test against the border region of the shape)."""
