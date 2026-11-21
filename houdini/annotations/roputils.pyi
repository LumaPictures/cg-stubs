from typing import TypedDict

import hou

class _RenderButtonKwargs(TypedDict):
    node: hou.OpNode
    mode: str

def onRenderButton(kwargs: _RenderButtonKwargs) -> None: ...
