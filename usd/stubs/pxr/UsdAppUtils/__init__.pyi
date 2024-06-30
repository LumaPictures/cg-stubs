# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Usd
import pxr.UsdGeom
from . import cameraArgs as cameraArgs, colorArgs as colorArgs, complexityArgs as complexityArgs, framesArgs as framesArgs, rendererArgs as rendererArgs
from typing import ClassVar

__MFB_FULL_PACKAGE_NAME: str

class FrameRecorder(Boost.Python.instance):
    """
    A utility class for recording images of USD stages.


    UsdAppUtilsFrameRecorder uses Hydra to produce recorded images of a
    USD stage looking through a particular UsdGeomCamera on that stage at
    a particular UsdTimeCode. The images generated will be effectively the
    same as what you would see in the viewer in usdview.

    Note that it is assumed that an OpenGL context has already been setup
    for the UsdAppUtilsFrameRecorder if OpenGL is being used as the
    underlying HGI device. This is not required for Metal or Vulkan.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self, rendererPluginId: object = ..., gpuEnabled: bool = ..., renderSettingsPrimPath: pxr.Sdf.Path | str = ...) -> None: ...
    def GetCurrentRendererId(self) -> str:
        """
        Gets the ID of the Hydra renderer plugin that will be used for
        recording.
        """
    def Record(self, stage: pxr.Usd.Stage, usdCamera: pxr.UsdGeom.Camera, timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, outputImagePath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Records an image and writes the result to C{outputImagePath}.


        The recorded image will represent the view from C{usdCamera} looking
        at the imageable prims on USD stage C{stage} at time C{timeCode}.

        If C{usdCamera} is not a valid camera, a camera will be computed to
        automatically frame the stage geometry.

        When we are using a RenderSettings prim, the generated image will be
        written to the file indicated on the connected RenderProducts, instead
        of the given C{outputImagePath}. Note that in this case the given
        C{usdCamera} will later be overridden by the one authored on the
        RenderSettings Prim.

        Returns true if the image was generated and written successfully, or
        false otherwise.
        """
    def SetCameraLightEnabled(self, cameraLightEnabled: bool) -> None:
        '''
        Turns the built-in camera light on or off.


        When on, this will add a light at the camera\'s origin. This is
        sometimes called a"headlight".
        '''
    def SetColorCorrectionMode(self, colorCorrectionMode: str | pxr.Ar.ResolvedPath) -> None:
        """
        Sets the color correction mode to be used for recording.


        By default, color correction is disabled.
        """
    def SetComplexity(self, complexity: float) -> None:
        '''
        Sets the level of refinement complexity.


        The default complexity is"low"(1.0).
        '''
    def SetImageWidth(self, imageWidth: int) -> None:
        """
        Sets the width of the recorded image.


        The height of the recorded image will be computed using this value and
        the aspect ratio of the camera used for recording.

        The default image width is 960 pixels.
        """
    def SetIncludedPurposes(self, purposes: list[str] | list[pxr.Ar.ResolvedPath]) -> None:
        '''
        Sets the UsdGeomImageable purposes to be used for rendering.


        We will B{always} include"default"purpose, and by default, we will
        also include UsdGeomTokens->proxy. Use this method to explicitly
        enumerate an alternate set of purposes to be included along
        with"default".
        '''
    def SetRendererPlugin(self, id: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Sets the Hydra renderer plugin to be used for recording.


        This also resets the presentation flag on the HdxPresentTask to false,
        to avoid the need for an OpenGL context.

        Note that the renderer plugins that may be set will be restricted if
        this UsdAppUtilsFrameRecorder instance has disabled the GPU.
        """

def GetCameraAtPath(stage: pxr.Usd.Stage, cameraPath: pxr.Sdf.Path | str) -> pxr.UsdGeom.Camera:
    """
    Gets the UsdGeomCamera matching C{cameraPath} from the USD stage
    C{stage}.


    If C{cameraPath} is an absolute path, this is equivalent to
    UsdGeomCamera::Get() . Otherwise, if C{cameraPath} is a single-element
    path representing just the name of a camera prim, then C{stage} will
    be searched looking for a UsdGeomCamera matching that name. The
    UsdGeomCamera schema for that prim will be returned if found, or an
    invalid UsdGeomCamera will be returned if not.

    Note that if C{cameraPath} is a multi-element path, a warning is
    issued and it is just made absolute using the absolute root path
    before searching. In the future, this could potentially be changed to
    use a suffix-based match.
    """
