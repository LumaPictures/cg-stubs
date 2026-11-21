# Houdini stubs generated from Houdini 22.0.466

import hou
from typing import TypedDict

class _RenderButtonKwargs(TypedDict):
    node: hou.OpNode
    mode: str

def onRenderButton(kwargs: _RenderButtonKwargs) -> None:
    """ Invoked when the render button is pressed.

        kwargs['node'] - Node that is hit
        kwargs['mode'] - Which render button style is hit:
            render - Normal render
            preview - Render to MPlay style
            background - Render in background
            controls - Render control pop up
        There are other internal modes that may show up, they should
        be ignored.
    """
