import hou
from collections.abc import Callable as Callable, Iterable, Sequence
from houtypes import ParmCallbackKwargs
from pxr import Usd as Usd

AOV_NAME: str
AOV_CHANNELPREFIX: str
AOV_FORMAT: str
AOV_FILTER: str

class _FrameRange:
    fstart: float
    fend: float
    finc: float
    frames: list[float]
    nframes: int
    animated: list[float]
    def __init__(self, fstart: float, fend: float, finc: float) -> None: ...

def update_rayimport_signature(kwargs: ParmCallbackKwargs) -> None:
    """
    Callback for setting the signature for kma_rayimport::2.0, when the user
    selects one of the ray imports.
    """
def update_rayimport_menu() -> list[str]:
    """
    Provides the menu of options for kma_rayimport::2.0
    """
def renderVars(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float) -> None:
    """ Create render vars for a karmastandardrendervars node.  The node passed
    in is the Python LOP inside the karmastandardrendervars node. This iterates
    over frame context."""
def renderProducts(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float) -> None:
    """ Create render products for karmarenderproducts node. Iterates over
    the frame context."""
def huskImageMetadata(node: hou.LopNode, stage: Usd.Stage, primlist: Iterable[Usd.Prim], fstart: float, fend: float, finc: float) -> None:
    """ Add metadata to a render product/render var. """
def renderProperties(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float, existingvars: Sequence[Usd.Prim]) -> None:
    """ Create a RenderSettings primitive by evaluating the Karma Render Settings LOP.
    Iterates over the frame context passed in."""
def toonShading(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float) -> None:
    """ Method called by the karmatoonshading LOP """
def imagefilter(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float) -> None:
    """
        Create HoudiniImageFilterList and HoudiniImageFilter primitives
        for the slapcomp primitive
    """

slapcomp: Callable[[hou.LopNode, Usd.Stage, float, float, float], None]

def precompile_info_dialog() -> None:
    """ Show dialog for pre-compiling XPU shaders.
        This dialog only runs with GUIs, and non-MacOS platforms (which can't
        have Optix GPUs).
    """
