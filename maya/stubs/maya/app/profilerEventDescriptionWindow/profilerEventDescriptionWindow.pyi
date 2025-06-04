from _typeshed import Incomplete
from maya.common.ui import LayoutManager as LayoutManager

FRAME_MARGIN_WIDTH: int
FRAME_MARGIN_HEIGHT: int
FRAME_LAYOUT: Incomplete
COL_SPACING: int
ROW_SPACING: int
RC_LAYOUT_2_COLUMN: Incomplete
RC_LAYOUT_5_COLUMN: Incomplete
TABLE_HEADER: Incomplete
KEY_MAIN: str
KEY_TYPE: str
KEY_DESCRIPTION: str
KEY_COLOUR: str
KEY_CATEGORY: str
KEY_COUNT: str
PROFILER_EVENT_DESCRIPTION_WINDOW_CONTROLLER: Incomplete

class EventDescriptionWindow:
    window_title: Incomplete
    window_name: Incomplete
    root_layout: Incomplete
    selection_changed_job: Incomplete
    def __init__(self, window_name: str = 'profilerEventDescriptionWindowId') -> None: ...
    @staticmethod
    def populate_event_types(selected_event_types) -> None: ...
    @staticmethod
    def populate_categories(category_info) -> None: ...
    def populate(self): ...
    def create(self) -> None: ...
    def selection_changed(self) -> None: ...
    def window_closed(self) -> None: ...

def create_window() -> None: ...
