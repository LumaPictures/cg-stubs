from typing import NotRequired, TypedDict

class _HandleCodegenKwargs(TypedDict):
    category: str
    name: str
    name_expr: str
    label: str
    description: str
    icon_name: str
    handler_indices: list[int]
    handler_count: int
    sample_index: int
    debug_menu: NotRequired[bool | int]
    hda_embedded: bool | int

def generateViewerHandleCode(kwargs: _HandleCodegenKwargs) -> str:
    """ Generate the handle code from templates
    """
