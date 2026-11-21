import hou
import resourceutils as ru
import typing
from collections.abc import Mapping, Sequence
from enum import Enum
from houtypes import ViewerStateEventKwargs
from typing import Any, Callable as Callable, Literal, TypeIs

from typing import TypeAlias
from typing import TypeAlias
_Viewer: TypeAlias = hou.SceneViewer | hou.CompositorViewer
_ExecInput: TypeAlias = hou.ImageLayer | hou.Geometry | None
_MouseEvent: TypeAlias = hou.ViewerEvent | hou.CompositorViewerEvent
_VerbParms: TypeAlias = Mapping[str, hou.OptionMultiArgType | Sequence[Mapping[str, hou.OptionMultiArgType]]]
thePickerStateName: str
theCryptomatteStateName: str
theInspectorHotkey: str
theShowLayerDrawableHotkey: str
theShowLayerLabel: str
theVDBWarning: str
theDoAreaSamplingName: str
theToggleDisplayName: str
theTextDisplayName: str
thePickerName: str
theBlocksDirectory: str
theRelevantEvents: list[hou.EnumValue[hou.nodeEventType]]

def isCompositor(viewer: hou.SceneViewer | hou.CompositorViewer) -> TypeIs[hou.CompositorViewer]:
    """
    I hate this    
    """

class Hotkeys:
    """
    The hotkey symbols used in the COPs picker state.
    This mimics what the APEX Animate State is doing
    """
    tool_key_h: str
    tool_key_ctrl_h: str
    tool_key_shift_h: str
    tool_key_o: str
    tool_key_ctrl_e: str
    tool_key_enter: str
    def __init__(self, state_typename: str, state_cat: hou.NodeTypeCategory) -> None: ...
    def definitions(self) -> hou.PluginHotkeyDefinitions:
        """
        Returns the hotkey definitions which can be registered with the
        viewer state template.
        """
    def context(self) -> str:
        """
        The hotkey context symbol for the state.
        """

class PickerMode(Enum):
    BUFFER = 0
    IMAGE_COORDS = 1

class BufferProcessor(Enum):
    NONE = 0
    MIN = 1
    MAX = 2
    MONO = 3
    UV = 4
    RGB = 5
    LUMINANCE = 6

class PickerCursorLabel(ru.CursorLabel):
    def __init__(self, viewer: hou.SceneViewer | hou.CompositorViewer) -> None: ...
    def update(self, kwargs: ViewerStateEventKwargs[hou.CompositorViewerEvent]) -> None: ...
    def setLabelFromBuffer(self, buffer: str | Sequence[float]) -> None: ...

class PickingAreaDrawable(hou.Drawable2D):
    """
    Wrapper around Drawable2D.
    Rectangle that follows the mouse cursor to indicate that the user is
    sampling an area    
    """
    viewer: hou.SceneViewer | hou.CompositorViewer
    name: str
    size: hou.Vector2
    drawable: hou.Drawable2D
    def __init__(self, viewer: hou.SceneViewer | hou.CompositorViewer, name: str) -> None: ...
    def draw(self, handle: hou.Handle) -> None: ...
    def getDrawableAttribute(self, name: str) -> Any: ...
    def setSize(self, size: hou.Vector2) -> None: ...
    def getSize(self) -> hou.Vector2: ...
    def setPosition(self, position: hou.Vector2) -> None: ...
    def updatePosition(self, event: _MouseEvent, viewport: hou.SceneViewer | hou.CompositorViewer, layer: hou.ImageLayer) -> None: ...
    def show(self, on: bool) -> None: ...

class LayerDrawable:
    """
    Wrapper around hou.Drawable2D to make it easier 
    to wrangle layer drawables    
    """
    drawable: hou.Drawable2D
    def __init__(self, scene_viewer: hou.SceneViewer | hou.CompositorViewer, layer: hou.ImageLayer, pickable: bool = False, name: str = 'layer_drawable', show: bool = True) -> None: ...
    def show(self) -> None: ...
    def draw(self, draw_handle: hou.Handle) -> None: ...
    def setVisible(self, i_see_you: bool) -> None: ...
    def isVisible(self) -> bool: ...
    def update(self, layer: hou.ImageLayer) -> None: ...
    def toggleDisplay(self) -> None: ...
    @staticmethod
    def shouldRender(node: hou.Node) -> bool:
        """
        We've decided that if the node display flag is not set on the node
        then its layer drawable should not render    
        """
    def setCopOutputVisibility(self, scene_viewer: hou.SceneViewer | hou.CompositorViewer, node: hou.Node, show: bool) -> None:
        """
        To prevent z-fighting, it's better to hide the COP output    
        When the layer drawable is being displayed, hide the
        COP output
        """
    def toggleCopOutputVisibility(self, scene_viewer: hou.SceneViewer | hou.CompositorViewer, node: hou.Node) -> None: ...

class CopInputType(Enum):
    INVALID = 0
    LAYER = 1
    VDB = 2
    HEIGHTFIELD = 3

class InputCache:
    node: hou.CopNode
    input: hou.ImageLayer | hou.NanoVDB | None
    index: int
    def __init__(self, node: hou.CopNode, the_input: hou.ImageLayer | hou.NanoVDB | None, index: int) -> None: ...
    def update(self) -> None: ...
    def getLayerAsGeometry(self) -> hou.Geometry | None: ...
    def __call__(self) -> hou.ImageLayer | hou.NanoVDB | None: ...
    def setNode(self, node: hou.CopNode) -> None: ...
    def isLayer(self) -> bool: ...
    def isHeightfield(self) -> bool: ...
    def isVDB(self) -> bool: ...
    def isSampleable(self) -> bool: ...
    @property
    def type(self) -> CopInputType: ...
    def isValid(self) -> bool: ...

class CopPicker:
    """
    A class that stores the picked indices and serializes them.
    Used by COP ID to Mask    
    """
    def __init__(self) -> None: ...
    def authorIndices(self, the_id: int, device: hou.UIEventDevice) -> None: ...
    def serializeIndices(self) -> str:
        """
        Convert the indices array into a string that the group field can use    
        """
    def setIndices(self, indices: list[int]) -> None: ...

class CopCryptomattePicker(CopPicker):
    """
    A class that stores cryptomatte indices and serializes them
    attribs is equal to HOM_ImageLayer.attributes()  
    """
    manifest: dict[int, str]
    def __init__(self, attribs: Mapping[str, Any]) -> None: ...
    def authorIndices(self, crypto_buffers: Sequence[bytes], device: hou.UIEventDevice) -> None:
        """
        converts the crypto buffer into an id and then adds it to the
        indices array        
        returns a serialized string to be used by the picker
        """
    def cryptoBufferToID(self, crypto_buffer: bytes) -> list[int]:
        """
        Get an id from the raw crypto buffer    
        """
    def unionedManifestFromAttributes(self, attribs: Mapping[str, Any]) -> dict[int, str]:
        """
        From a HOM_ImageLayer, generate a unioned manifest to use
        as a map to look into with our indices 
        cryptomatte manifests should have a key formatted like
        cryptomatte/*/manifest
        we then reverse the keys and values and convert the hex str to int
        
        example manifest: 
        {
            3447975093: '/World/volume/volume_0',
            173481706:  '/World/sphere/mesh_0'
        }
           
        """
    def serializeIndices(self) -> str:
        """
        Convert the indices array into a string that the group field can use    
        """
    def buffersToLabel(self, buffers: Sequence[bytes], truncate: bool = True) -> str:
        """
        Generate label from crypto buffers
        useful to set cursor icon label    
        """
    def isValid(self) -> dict[int, str]: ...
    def setIndicesFromStr(self, prims: str) -> None:
        """
        When we start the clicking interaction we actually set indices
        from the parameter. This does the conversion from string to indices
        This is needed so Undos can function properly    
        """
    def expandPatterns(self, pattern: str) -> str:
        """
        Cryptomatte now supports string matching ! Yay ! 
        But this means we need to expand these because the picker does not    
        """
    @staticmethod
    def getAllCryptoKeysAsString(attribs: Mapping[str, Any]) -> str: ...

class Transform2dStaticBinder:
    """
    A convenience wrapper to bind a static transform2d handle to cop node
    viewer states...    
    This object should be created in onEnter, then bound using self.bind
    unbind should be called onExit
    """
    scene_viewer: hou.SceneViewer | hou.CompositorViewer
    parms: list[tuple[str, str]]
    type: str
    name: str
    def __init__(self, scene_viewer: hou.SceneViewer | hou.CompositorViewer, name: str, tx: str | None = None, ty: str | None = None, rz: str | None = None, s: str | None = None) -> None: ...
    def bind(self) -> None: ...
    def unbind(self) -> None: ...

class LayerBuilder:
    @staticmethod
    def buildHighlightLayer(scene_viewer: hou.SceneViewer | hou.CompositorViewer, layer: hou.ImageLayer | None = None) -> hou.ImageLayer: ...
    @staticmethod
    def buildPreHighlightLayer(scene_viewer: hou.SceneViewer | hou.CompositorViewer, dev: hou.UIEventDevice | None = None, layer: hou.ImageLayer | None = None) -> hou.ImageLayer: ...
    @staticmethod
    def buildColorLayer(layer: hou.ImageLayer | None = None, color: Sequence[float] = [0.0, 0.0, 0.0]) -> hou.ImageLayer: ...
    @staticmethod
    def getPrimHighlightColor(scene_viewer: hou.SceneViewer | hou.CompositorViewer) -> tuple[float, ...]: ...
    @staticmethod
    def getPrimPreHighlightColor(scene_viewer: hou.SceneViewer | hou.CompositorViewer, pick_mod: hou.EnumValue[hou.pickModifier]) -> tuple[float, ...]: ...

class VerbExecutioner:
    verb: hou.CopVerb
    output_key: str
    execution_parms: dict[str, _ExecInput]
    def __init__(self, verb: str, verb_parms: _VerbParms, execution_parms: dict[str, _ExecInput] = ...) -> None: ...
    def __call__(self) -> hou.ImageLayer | None: ...
    def updateExecutionParms(self, parms: Mapping[str, _ExecInput]) -> None: ...
    def setExecutionParms(self, parms: dict[str, _ExecInput]) -> None: ...
    def setVerbParms(self, parms: _VerbParms) -> None: ...

class CryptoMatteVerbExecutioner(VerbExecutioner):
    execution_parms: dict[str, _ExecInput]
    def __init__(self, verb_parms: _VerbParms = {'selection': ''}) -> None: ...
    def setSelection(self, selection: str) -> None: ...
    def updateInput(self, data: hou.ImageLayer | None) -> None: ...

class Resampler(VerbExecutioner):
    execution_parms: dict[str, _ExecInput]
    def __init__(self, scale: float, signature: str = 'f4') -> None: ...
    def updateInput(self, data: hou.ImageLayer) -> None: ...
    @staticmethod
    def resample(layer: hou.ImageLayer, scale: float, signature: str = 'f4') -> hou.ImageLayer | None: ...

class BlockExecutioner(VerbExecutioner):
    program: hou.Geometry
    def __init__(self, program_file_path: str, verb_parms: _VerbParms) -> None: ...
    def loadProgram(self, file_path: str) -> None: ...

class CryptoMatteBlockExecutioner(BlockExecutioner):
    selmask: hou.ImageLayer | None
    parms: dict[str, list[dict[str, str | int]]]
    program: hou.Geometry
    hicolor: hou.ImageLayer | None
    cryptomatte: hou.ImageLayer | None
    mask: hou.ImageLayer | None
    prehicolor: hou.ImageLayer | None
    preselmask: hou.ImageLayer | None
    def __init__(self, hi_color: hou.ImageLayer | None, prehi_color: hou.ImageLayer | None, crypto: hou.ImageLayer | None, sel_mask: hou.ImageLayer | None, pre_sel_mask: hou.ImageLayer | None) -> None: ...
    def update(self, hi_color: hou.ImageLayer | None, prehi_color: hou.ImageLayer | None, crypto: hou.ImageLayer | None, sel_mask: hou.ImageLayer | None, pre_sel_mask: hou.ImageLayer | None) -> None: ...

class CryptoMatteExecutionManager:
    block_executioner: CryptoMatteBlockExecutioner
    verb_executioner: CryptoMatteVerbExecutioner
    def __init__(self) -> None: ...
    def update(self, hi_color: hou.ImageLayer, prehi_color: hou.ImageLayer, crypto: hou.ImageLayer | None, selection: str, pre_selection: str) -> None: ...
    def __call__(self) -> hou.ImageLayer | None: ...

class ImagetoMaskBlockExecutioner(BlockExecutioner):
    parms: dict[str, list[dict[str, str | int]]]
    def __init__(self) -> None: ...
    def update(self, rgb: hou.ImageLayer, mask: hou.ImageLayer, highlight_color: hou.ImageLayer) -> None: ...

class ImagetoMaskExecutionManager:
    block_executioner: ImagetoMaskBlockExecutioner
    def __init__(self) -> None: ...
    def update(self, rgb: hou.ImageLayer, mask: hou.ImageLayer, highlight_color: hou.ImageLayer) -> None: ...
    def __call__(self) -> hou.ImageLayer | None: ...

class IDtoMaskExecutionManager:
    mask_creator: BlockExecutioner
    visualiser_creator: BlockExecutioner
    def __init__(self) -> None: ...
    def update(self, id_layer: hou.ImageLayer, hi_color: hou.ImageLayer, prehi_color: hou.ImageLayer, sel: str, pre_sel: str) -> None: ...
    def __call__(self) -> hou.ImageLayer | None: ...
    def setIndices(self, geo: hou.Geometry, indices: str) -> None: ...
    def checkForNegativeIndices(self, indices: str) -> bool: ...

@typing.overload
def bufferFromMouse(ui_event: _MouseEvent, scene_viewer: hou.SceneViewer | hou.CompositorViewer, layer: hou.ImageLayer, raw: Literal[False] = ...) -> float | tuple[float, ...]: ...
@typing.overload
def bufferFromMouse(ui_event: _MouseEvent, scene_viewer: hou.SceneViewer | hou.CompositorViewer, layer: hou.ImageLayer, raw: Literal[True]) -> bytes: ...
@typing.overload
def bufferFromMouse(ui_event: _MouseEvent, scene_viewer: hou.SceneViewer | hou.CompositorViewer, layer: hou.ImageLayer, raw: bool = ...) -> float | tuple[float, ...] | bytes: ...
def imageCoordsFromMouse(ui_event: _MouseEvent, scene_viewer: hou.SceneViewer | hou.CompositorViewer, layer: hou.ImageLayer) -> hou.Vector2:
    """
    Given a mouse position returns the image space coords 
    where the layer has been clicked    
    """
def mousePosToWorld(ui_event: _MouseEvent, viewport: hou.GeometryViewport | hou.Viewport2D, layer: hou.ImageLayer) -> hou.Vector3:
    """ 
    Given a mouse position, a viewport and a layer, find the 
    world space position where the mouse intersects the COP 
    layer.
    """
def mousePosToImage(ui_event: _MouseEvent, viewport: hou.GeometryViewport, layer: hou.ImageLayer) -> hou.Vector2:
    """
    Given a mouse position, a viewport and a layer,
    find the image space coords where the mouse intersects the COP layer    
    """
def handleExpansion(buffer: float | list[float] | tuple[float, ...], target_count: int) -> list[float] | tuple[float, ...]:
    """
    If you've implicitly converted from mono to rgba for example
    and are trying to set an rgba parm from a mono input
    we need to handle that expansion ...
    """
def layerIsHeight(layer: hou.ImageLayer) -> bool: ...
def getInputLayer(node: hou.Node | None, index: int = 0) -> hou.ImageLayer | None:
    """
    Gets the layer plugged into the index-th input of this node
    """
def getInputLayerAsGeo(node: hou.Node | None, index: int = 0) -> hou.Geometry | None:
    """
    Gets the layer as geomtry plugged into the index-th input of this node
    """
def getInputLayers(node: hou.Node) -> list[hou.ImageLayer | None]:
    """
    Grab all the layers plugged into the node    
    """
def getInputLayerOrVDB(node: hou.Node | None, index: int = 0) -> hou.ImageLayer | hou.NanoVDB | None:
    """
    Gets the layer or VDB plugged into the index-th input of this node
    when convert is set to True, Height layers get converted to geometry
    """
def layerOrVDB(node: hou.CopNode) -> hou.ImageLayer | hou.NanoVDB | None:
    """
    Gets node layer or VDB if no layer is found or None if nothing is found
    if the layer has type info set to height then we return a hou.geometry
    with the volume primitive    
    if convert is set to True, then height layers get converted to geometry
    """
def canRunState(node: hou.Node | None) -> bool:
    """
    Checks if a node can actually run the state.
    Returns false if the node is in an error state     
    This might need to check inputs as well
    """
def enterPickerState(node: hou.CopNode, parm: str, index: int = 0, mode: PickerMode = ..., processor: BufferProcessor | Callable[[Sequence[float]], Sequence[float]] = ...) -> None:
    '''
    Convenience function used to enter the picker state. This is used
    by pretty much all the COP nodes that have a picker state.
    Parms
    
    Node: should be kwargs["node"]
    
    Parm: The name of the parameter to set, eg. threshold. Name, not label !
    This should be set to kwargs[\'parm\'].name()
    
    Index: get the layer that\'s input into this port. 
    -1 means get the node\'s layer. Use if the node does not require any inputs

    Mode: either PickerMode.BUFFER or PickerMode.IMAGE_COORDS
    PickerMode.BUFFER returns the value of the buffer at the coordinates we got from
    the mouse
    PickerMode.IMAGE_COORDS returns image space coordinates

    Processor: either a custom callable ( see Glow COP for example) or
    a BufferProcessor Enum
    "using BufferProcessor":
    .NONE -> passthrough
    .MIN -> returns the min component, ex [1.0, 0.5, 0.0] -> 0.0
    .MAX -> returns the max component
    .MONO -> returns the first index
    .UV -> returns the first two indices
    .RGB -> returns the first three indices
    .LUMINANCE -> returns the luminance of the incoming layer
    
    '''
def enterCryptomatteState(node: hou.CopNode) -> None:
    """
    Utility Function used by the Cryptomatte COP to enter the state from
    its action button    
    """
def setAndConfigureState(state_name: str, viewer: hou.SceneViewer | hou.CompositorViewer | hou.ContextViewer, args: Mapping[str, object]) -> None:
    """
    Wrapper that handles hou.OperationFailed    
    """
def exitState(viewer: hou.SceneViewer | hou.CompositorViewer) -> bool:
    """
    Composite view can't call enterViewState...
    but according to the docs it can
    and it works from the shell ???
    but if I remove this check then I get a crash when hitting enter
    in the idtomask state...    
    """
def getCOPCapableViewer() -> hou.SceneViewer | hou.CompositorViewer | None:
    """
    Returns a scene viewer and if not, get a composite viewer and if not
    return None  
    """
def setPickerCursor(on: bool, do_tab_check: bool = True) -> bool:
    """
     on ? Sets the cursor to crosshair
    !on ? Reset Mouse Cursor to default
    from_command needs to be turned on when launched from
    onCommand    
    """
def warn(viewer: hou.SceneViewer | hou.CompositorViewer, warning: str) -> None: ...
def warnAboutVDBs(viewer: hou.SceneViewer | hou.CompositorViewer) -> None: ...
def bindPickerStateMenu(template: hou.ViewerStateTemplate, hotkeys: Hotkeys, display_default: bool = True) -> None: ...
def bindPickerTemplateParameters(template: hou.ViewerStateTemplate, display_default: bool = True) -> None: ...
