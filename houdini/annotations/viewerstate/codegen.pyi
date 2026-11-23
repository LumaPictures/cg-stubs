from typing import NotRequired, TypedDict

class _StateCodegenKwargs(TypedDict):
    category: str
    name: str
    name_expr: str
    label: str
    description: str
    icon_name: str
    handler_indices: list[int]
    sample_init_marker: int
    sample_index: int
    debug_menu: NotRequired[bool | int]
    hda_embedded: bool | int

def generateViewerStateCode(kwargs: _StateCodegenKwargs) -> str: ...
