# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.CameraUtil
import pxr.Gf
import pxr.Glf
import pxr.Sdf
import pxr.Usd
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

ALL_INSTANCES: int
__MFB_FULL_PACKAGE_NAME: str

class CullStyle(Boost.Python.enum):
    CULL_STYLE_BACK: ClassVar[CullStyle] = ...
    CULL_STYLE_BACK_UNLESS_DOUBLE_SIDED: ClassVar[CullStyle] = ...
    CULL_STYLE_FRONT: ClassVar[CullStyle] = ...
    CULL_STYLE_NOTHING: ClassVar[CullStyle] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class DrawMode(Boost.Python.enum):
    DRAW_GEOM_FLAT: ClassVar[DrawMode] = ...
    DRAW_GEOM_ONLY: ClassVar[DrawMode] = ...
    DRAW_GEOM_SMOOTH: ClassVar[DrawMode] = ...
    DRAW_POINTS: ClassVar[DrawMode] = ...
    DRAW_SHADED_FLAT: ClassVar[DrawMode] = ...
    DRAW_SHADED_SMOOTH: ClassVar[DrawMode] = ...
    DRAW_WIREFRAME: ClassVar[DrawMode] = ...
    DRAW_WIREFRAME_ON_SURFACE: ClassVar[DrawMode] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class Engine(Boost.Python.instance):
    """
    The UsdImagingGLEngine is the main entry point API for rendering USD
    scenes.
    """

    class Parameters(Boost.Python.instance):
        """
        Parameters to construct UsdImagingGLEngine.
        """
        __instance_size__: ClassVar[int] = ...
        allowAsynchronousSceneProcessing: Incomplete
        driver: Incomplete
        excludedPaths: Incomplete
        gpuEnabled: Incomplete
        invisedPaths: Incomplete
        rendererPluginId: Incomplete
        rootPath: Incomplete
        sceneDelegateID: Incomplete
        def __init__(self) -> None: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, _params: Engine.Parameters, /) -> None: ...
    @overload
    def __init__(self, _driver: pxr.Sdf.Path | str, _rendererPluginId: str | pxr.Ar.ResolvedPath, _gpuEnabled: bool, /) -> None:
        """
        An HdDriver, containing the Hgi of your choice, can be optionally
        passed in during construction.


        This can be helpful if you application creates multiple
        UsdImagingGLEngine that wish to use the same HdDriver / Hgi. The
        C{rendererPluginId} argument indicates the renderer plugin that Hyrda
        should use. If the empty token is passed in, a default renderer plugin
        will be chosen depending on the value of C{gpuEnabled}. The
        C{gpuEnabled} argument determines if this instance will allow Hydra to
        use the GPU to produce images.
        """
    @overload
    def __init__(self) -> None: ...
    def AddSelected(self, _path: pxr.Sdf.Path | str, _instanceIndex: int, /) -> None:
        """
        Add a path with instanceIndex to the list of prim paths that should be
        included in selection highlighting.


        UsdImagingDelegate::ALL_INSTANCES can be used for highlighting all
        instances if path is an instancer.
        """
    def ClearSelected(self) -> None:
        """
        Clear the list of prim paths that should be included in selection
        highlighting.
        """
    @staticmethod
    def GetAvailableRenderSettingsPrimPaths(_root: pxr.Usd.Prim, /) -> list[pxr.Sdf.Path]:
        """
        Utility method to query available render settings prims.
        """
    def GetCurrentRendererId(self) -> str:
        """
        Return the id of the currently used renderer plugin.
        """
    def GetRenderStats(self) -> dict:
        """
        Returns render statistics.


        The contents of the dictionary will depend on the current render
        delegate.
        """
    def GetRendererAovs(self) -> list[str]:
        """
        Return the vector of available renderer AOV settings.
        """
    def GetRendererCommandDescriptors(self) -> list:
        """
        Return command deescriptors for commands supported by the active
        render delegate.
        """
    @staticmethod
    def GetRendererDisplayName(_id: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Return the user-friendly description of a renderer plugin.
        """
    @staticmethod
    def GetRendererPlugins() -> list[str]:
        """
        Return the vector of available render-graph delegate plugins.
        """
    def GetRendererSetting(self, _id: str | pxr.Ar.ResolvedPath, /) -> Any:
        """
        Gets a renderer setting's current value.
        """
    def GetRendererSettingsList(self) -> list:
        """
        Returns the list of renderer settings.
        """
    def InvokeRendererCommand(self, command: str | pxr.Ar.ResolvedPath, args: HdCommandArgs = ...) -> bool:
        """
        Invokes command on the active render delegate.


        If successful, returns C{true}, returns C{false} otherwise. Note that
        the command will not succeeed if it is not among those returned by
        GetRendererCommandDescriptors() for the same active render delegate.
        """
    @staticmethod
    def IsColorCorrectionCapable() -> bool:
        """
        Returns true if the platform is color correction capable.
        """
    def IsConverged(self) -> bool:
        """
        Returns true if the resulting image is fully converged.


        (otherwise, caller may need to call Render() again to refine the
        result)
        """
    def IsPauseRendererSupported(self) -> bool:
        """
        Query the renderer as to whether it supports pausing and resuming.
        """
    def IsStopRendererSupported(self) -> bool:
        """
        Query the renderer as to whether it supports stopping and restarting.
        """
    def PauseRenderer(self) -> bool:
        """
        Pause the renderer.


        Returns C{true} if successful.
        """
    def PollForAsynchronousUpdates(self) -> bool:
        """
        If C{allowAsynchronousSceneProcessing} is true within the Parameters
        provided to the UsdImagingGLEngine constructor, an application can
        periodically call this from the main thread.


        A return value of true indicates that the scene has changed and the
        render should be updated.
        """
    def Render(self, _root: pxr.Usd.Prim, _params: RenderParams, /) -> None:
        """
        Entry point for kicking off a render.
        """
    def RestartRenderer(self) -> bool:
        """
        Restart the renderer.


        Returns C{true} if successful.
        """
    def ResumeRenderer(self) -> bool:
        """
        Resume the renderer.


        Returns C{true} if successful.
        """
    def SetActiveRenderSettingsPrimPath(self, _unknownArg1: pxr.Sdf.Path | str, /) -> None:
        """
        Set active render settings prim to use to drive rendering.
        """
    def SetCameraPath(self, _id: pxr.Sdf.Path | str, /) -> None:
        """
        Scene camera API Set the scene camera path to use for rendering.
        """
    def SetCameraState(self, _viewMatrix: pxr.Gf.Matrix4d, _projectionMatrix: pxr.Gf.Matrix4d, /) -> None:
        """
        Free camera API Set camera framing state directly (without pointing to
        a camera on the USD stage).


        The projection matrix is expected to be pre-adjusted for the window
        policy.
        """
    def SetColorCorrectionSettings(self, _ccType: str | pxr.Ar.ResolvedPath, _ocioDisplay: str | pxr.Ar.ResolvedPath, _ocioView: str | pxr.Ar.ResolvedPath, _ocioColorSpace: str | pxr.Ar.ResolvedPath, _ocioLook: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Set C{ccType} to one of the HdxColorCorrectionTokens: {disabled, sRGB,
        openColorIO}.


        If'openColorIO'is used, C{ocioDisplay}, C{ocioView}, C{ocioColorSpace}
        and C{ocioLook} are options the client may supply to configure OCIO.
        C{ocioColorSpace} refers to the input (source) color space. The
        default value is substituted if an option isn't specified. You can
        find the values for these strings inside the profile/config .ocio
        file. For example:

        displays: rec709g22: !<View>{name: studio, colorspace: linear, looks:
        studio_65_lg2}
        """
    def SetFraming(self, _framing: pxr.CameraUtil.Framing, /) -> None:
        """
        Determines how the filmback of the camera is mapped into the pixels of
        the render buffer and what pixels of the render buffer will be
        rendered into.
        """
    def SetLightingState(self, _lights: list[pxr.Glf.SimpleLight], _material: pxr.Glf.SimpleMaterial, _sceneAmbient: pxr.Gf.Vec4f | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Set lighting state Derived classes should ensure that passing an empty
        lights vector disables lighting.


        lights

        is the set of lights to use, or empty to disable lighting.
        """
    def SetOverrideWindowPolicy(self, _policy: pxr.CameraUtil.ConformWindowPolicy | None, /) -> None:
        """
        Specifies whether to force a window policy when conforming the frustum
        of the camera to match the display window of the camera framing.


        If set to {false, ...}, the window policy of the specified camera will
        be used.

        Note: std::pair<bool, ...>is used instead of std::optional<...>because
        the latter is only available in C++17 or later.
        """
    def SetRenderBufferSize(self, _size: pxr.Gf.Vec2i | list[int] | pxr.Gf.Size2 | tuple[int, int], /) -> None:
        """
        Set the size of the render buffers baking the AOVs.


        GUI applications should set this to the size of the window.
        """
    def SetRenderViewport(self, _viewport: pxr.Gf.Vec4d | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Set the viewport to use for rendering as (x,y,w,h), where (x,y)
        represents the lower left corner of the viewport rectangle, and (w,h)
        is the width and height of the viewport in pixels.


        Deprecated

        Use SetFraming and SetRenderBufferSize instead.
        """
    def SetRendererAov(self, _id: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Set the current renderer AOV to C{id}.
        """
    def SetRendererPlugin(self, _id: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Set the current render-graph delegate to C{id}.


        the plugin will be loaded if it's not yet.
        """
    def SetRendererSetting(self, _id: str | pxr.Ar.ResolvedPath, _value: Any, /) -> None:
        """
        Sets a renderer setting's value.
        """
    def SetSelected(self, _paths: typing.Iterable[pxr.Sdf.Path | str], /) -> None:
        """
        Sets (replaces) the list of prim paths that should be included in
        selection highlighting.


        These paths may include root paths which will be expanded internally.
        """
    def SetSelectionColor(self, _color: pxr.Gf.Vec4f | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Sets the selection highlighting color.
        """
    def SetWindowPolicy(self, _policy: pxr.CameraUtil.ConformWindowPolicy, /) -> None:
        """
        Set the window policy to use.


        XXX: This is currently used for scene cameras set via SetCameraPath.
        See comment in SetCameraState for the free cam.
        """
    def StopRenderer(self) -> bool:
        """
        Stop the renderer.


        Returns C{true} if successful.
        """
    def TestIntersection(self, _viewMatrix: pxr.Gf.Matrix4d, _projectionMatrix: pxr.Gf.Matrix4d, _root: pxr.Usd.Prim, _params: RenderParams, /) -> tuple:
        """
        Finds closest point of intersection with a frustum by rendering.


        This method uses a PickRender and a customized depth buffer to find an
        approximate point of intersection by rendering. This is less accurate
        than implicit methods or rendering with GL_SELECT, but leverages any
        data already cached in the renderer.

        Returns whether a hit occurred and if so, C{outHitPoint} will contain
        the intersection point in world space (i.e. C{projectionMatrix} and
        C{viewMatrix} factored back out of the result), and C{outHitNormal}
        will contain the world space normal at that point.

        C{outHitPrimPath} will point to the gprim selected by the pick.
        C{outHitInstancerPath} will point to the point instancer (if
        applicable) of that gprim. For nested instancing, outHitInstancerPath
        points to the closest instancer.
        """

class RenderParams(Boost.Python.instance):
    """
    Used as an arguments class for various methods in UsdImagingGLEngine.
    """
    __instance_size__: ClassVar[int] = ...
    applyRenderState: Incomplete
    bboxLineColor: Incomplete
    bboxLineDashSize: Incomplete
    bboxes: Incomplete
    clearColor: Incomplete
    clipPlanes: Incomplete
    colorCorrectionMode: Incomplete
    complexity: Incomplete
    cullStyle: Incomplete
    drawMode: Incomplete
    enableIdRender: Incomplete
    enableLighting: Incomplete
    enableSampleAlphaToCoverage: Incomplete
    enableSceneLights: Incomplete
    enableSceneMaterials: Incomplete
    enableUsdDrawModes: Incomplete
    forceRefresh: Incomplete
    frame: Incomplete
    gammaCorrectColors: Incomplete
    highlight: Incomplete
    ocioColorSpace: Incomplete
    ocioDisplay: Incomplete
    ocioLook: Incomplete
    ocioView: Incomplete
    overrideColor: Incomplete
    showGuides: Incomplete
    showProxy: Incomplete
    showRender: Incomplete
    wireframeColor: Incomplete
    def __init__(self) -> None: ...

class RendererCommandArgDescriptor(Boost.Python.instance):
    """Renderer Command Argument Metadata"""
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def argName(self): ...
    @property
    def defaultValue(self): ...

class RendererCommandDescriptor(Boost.Python.instance):
    """Renderer Command Metadata"""
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def commandArgs(self): ...
    @property
    def commandDescription(self): ...
    @property
    def commandName(self): ...

class RendererSetting(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @property
    def defValue(self): ...
    @property
    def key(self): ...
    @property
    def name(self): ...
    @property
    def type(self): ...

class RendererSettingType(Boost.Python.enum):
    FLAG: ClassVar[RendererSettingType] = ...
    FLOAT: ClassVar[RendererSettingType] = ...
    INT: ClassVar[RendererSettingType] = ...
    STRING: ClassVar[RendererSettingType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
