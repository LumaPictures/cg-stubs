# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import QT4Widgets as QT4Widgets
import QT4Widgets.FilterablePopupButton
from typing import Set, Tuple

class SetVersionFilterablePopup(QT4Widgets.FilterablePopupButton.FilterablePopup):
    def __init__(self, *args) -> None: ...
    def popupWithAsset(self, assetId, pos): ...
