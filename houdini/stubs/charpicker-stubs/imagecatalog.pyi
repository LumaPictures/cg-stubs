import dataclasses
import enum
from collections.abc import Iterable, Mapping

IMAGES_CATALOG_NAME: str
IMAGES_CATALOG_SOURCE: str
TEMPLATE_REF_PREFIX: str
LABEL_REF_PREFIX: str
LABEL_CATALOG_REF: str

class ImageType(enum.Enum):
    RASTER = 'raster'
    SVG = 'svg'

@dataclasses.dataclass
class _CatalogEntry:
    item_id: str
    image_type: ImageType
    raw_data: bytes | None = ...

@dataclasses.dataclass
class ImageLoadResult:
    """Outcome of loading serialized catalog entries."""
    invalid_image_count: int = ...

class ImageCatalog:
    """Image catalog backed by a shared asset data source.

    Data source item_ids are not persisted across sessions, so each
    image is assigned a stable catalog_ref (UUID) stored in the layout
    JSON.
    """
    def __init__(self) -> None: ...
    def addImage(self, raw_bytes: bytes, image_type: ImageType = ...) -> str: ...
    def getData(self, ref_id: str) -> bytes | None: ...
    def getType(self, ref_id: str) -> ImageType: ...
    def hasRef(self, ref_id: str) -> bool: ...
    def toDict(self, ref_ids: Iterable[str]) -> dict[str, str | dict[str, str]]:
        """Return a dict mapping catalog_refs to serializable data."""
    def loadFromDict(self, data: Mapping[str, str | dict[str, str]]) -> ImageLoadResult:
        """Load catalog entries from serialized layout data.

        Undecodable entries are skipped. Returns an ImageLoadResult with
        the skipped image count.
        """
    @staticmethod
    def canDecodeImage(raw_bytes: bytes, image_type: ImageType) -> bool:
        """Return whether raw_bytes decode to a valid image of image_type."""
    def catalogRefFromItemId(self, item_id: str) -> str | None:
        """Return the catalog_ref stored for a data source item."""
    def clear(self) -> None: ...
    @staticmethod
    def imageTypeFromPath(path: str) -> ImageType: ...
    @staticmethod
    def isTemplateRef(ref_id: str) -> bool: ...
    @staticmethod
    def isLabelRef(ref_id: str) -> bool: ...
    @staticmethod
    def isMirroredTemplate(ref_id: str) -> bool: ...
    def loadTemplateImages(self) -> None: ...
    def refresh(self) -> None: ...
