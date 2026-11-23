import dataclasses
import substance_painter.resource
from _typeshed import Incomplete

from _substance_painter.display import ToneMappingFunction as ToneMappingFunction

def get_environment_resource() -> substance_painter.resource.ResourceID | None:
    """
    Get the environment map resource of the active project.

    Returns:
        ResourceID: The environment map resource or None.

    Raises:
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """
def set_environment_resource(new_env_map: substance_painter.resource.ResourceID) -> None:
    """
    Set the environment map resource of the active project.

    Args:
        new_env_map (ResourceID): The new environment map resource.

    Raises:
        ProjectError: If no project is opened.
        TypeError: If ``new_env_map`` is not a ResourceID.
        ResourceNotFoundError: If the environment map ``new_env_map`` is not found.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """
def get_color_lut_resource() -> substance_painter.resource.ResourceID | None:
    """
    Get the color profile LUT resource of the active project.

    Returns:
        ResourceID:  The color profile LUT resource or None.

    Raises:
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """
def set_color_lut_resource(new_color_lut: substance_painter.resource.ResourceID) -> None:
    """
    Set the color profile LUT resource of the active project.

    Args:
        new_color_lut (ResourceID): The new color profile LUT.

    Raises:
        ProjectError: If no project is opened.
        TypeError: If ``new_color_lut`` is not a ResourceID.
        ResourceNotFoundError: If the color profile ``new_color_lut`` is not found.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """
def get_tone_mapping() -> ToneMappingFunction:
    """
    Get the tone mapping operator used to display the current project.

    Note:
        The tone mapping function is disabled when color management is enabled.
        In that case trying to call get_tone_mapping will throw a RuntimeError.

    Returns:
        ToneMappingFunction: The tone mapping function currently used by
            the project.

    Raises:
        RuntimeError: If the project is color managed.
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """
def set_tone_mapping(new_tone_mapping: ToneMappingFunction) -> None:
    """
    Set the tone mapping operator to display the current project.

    Note:
        The tone mapping function is disabled when color management is enabled.
        In that case trying to call set_tone_mapping will throw a RuntimeError.

    Args:
        new_tone_mapping (ToneMappingFunction): The new tone mapping function
            to use in the project.

    Raises:
        TypeError: If ``new_tone_mapping`` is not a ToneMappingFunction.
        RuntimeError: If the project is color managed.
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """

from _substance_painter.display import CameraProjectionType as CameraProjectionType

@dataclasses.dataclass
class Camera:
    '''
    Allows the manipulation of the properties of an existing Camera.
    Coordinates of the camera are defined in the scene space.

    Example:
        ::

            import substance_painter.display
            import substance_painter.project

            substance_painter.project.open("C:/projects/MeetMat.spp")

            # Get the dimensions of the scene
            bounding_box = substance_painter.project.get_scene_bounding_box()

            # Get the main camera
            camera = substance_painter.display.Camera.get_default_camera()

            # Update camera properties
            camera.projection_type = substance_painter.display.CameraProjectionType.Perspective
            # Move the camera away from the center of the scene
            camera.position = [
                bounding_box.center[0] + 15,
                bounding_box.center[1],
                bounding_box.center[2] + 15]
            # Rotate the camera (45° of Y-axis)
            camera.rotation = [0, 45, 0]
            # Update the camera field of view (in degrees)
            camera.field_of_view = 50

    See also:
        `Camera Settings documentation`_.
        :func:`substance_painter.project.get_scene_bounding_box`

        .. _Camera Settings documentation:
            https://substance3d.adobe.com/documentation/spdoc/camera-settings-172818743.html
    '''
    @staticmethod
    def get_default_camera() -> Camera:
        """
        Get the default camera.

        Returns:
            Camera: The default (main) camera.
        Raises:
            ProjectError: If no project is opened.
            RuntimeError: If no camera has been found.
        """
    @property
    def position(self) -> list[float]:
        """
        The position (x,y,z) of the camera.

        :getter: Returns the position of the camera.
        :setter: Sets the position of the camera.
        :type: List[float]

        Raises:
            ProjectError: If no project is opened.
        """
    @position.setter
    def position(self, position: list[float]) -> None: ...
    @property
    def rotation(self) -> list[float]:
        """
        The rotation (x,y,z) of the camera as Euler angles in degrees.

        :getter: Returns the rotation of the camera.
        :setter: Sets the rotation of the camera.
        :type: List[float]

        Raises:
            ProjectError: If no project is opened.
        """
    @rotation.setter
    def rotation(self, rotation: list[float]) -> None: ...
    @property
    def field_of_view(self) -> float:
        """
        The field of view of the camera in degrees.
        This value is only used if the ``CameraProjectionType`` is ``Perspective``.

        :getter: Returns the field of view of the camera.
        :setter: Sets the field of view of the camera. Value is clamped between 3 and 179.
        :type: float

        Note:
            Modifing the field of view will change the focal length.

        Raises:
            ProjectError: If no project is opened.
        """
    @field_of_view.setter
    def field_of_view(self, fov: float) -> None: ...
    @property
    def focal_length(self) -> float:
        """
        The focal length of the camera in mm.
        This value is only used if the ``CameraProjectionType`` is ``Perspective``.

        :getter: Returns the focal length of the camera.
        :setter: Sets the focal length of the camera. Value is clamped between 1 and 500.
        :type: float

        Note:
            Modifing the focal length will change the field of view.

        Raises:
            ProjectError: If no project is opened.
        """
    @focal_length.setter
    def focal_length(self, focal_length: float) -> None: ...
    @property
    def focus_distance(self) -> float:
        """
        The focus distance of the camera.
        Defines the distance at which the focus point is located.

        :getter: Returns the focus distance of the camera.
        :setter: Sets the focus distance of the camera.
            Value is clamped between 0 and 10 * scene radius.
        :type: float

        Raises:
            ProjectError: If no project is opened.
        """
    @focus_distance.setter
    def focus_distance(self, focus_distance: float) -> None: ...
    @property
    def aperture(self) -> float:
        """
        The aperture of the camera. Defines how wide the Depth of Field will be.

        :getter: Returns the lens radius.
        :setter: Sets the lens radius. Value is clamped between 0 and 1 * scene radius.
        :type: float

        Raises:
            ProjectError: If no project is opened.
        """
    @aperture.setter
    def aperture(self, aperture: float) -> None: ...
    @property
    def orthographic_height(self) -> float:
        """
        The orthographic height of the camera.
        This value is only used if the ``CameraProjectionType`` is ``Orthographic``.

        :getter: Returns the orthographic height of the camera.
        :setter: Sets the orthographic height of the camera.
        :type: float

        Raises:
            ProjectError: If no project is opened.
        """
    @orthographic_height.setter
    def orthographic_height(self, orthographic_height: float) -> None: ...
    @property
    def projection_type(self) -> CameraProjectionType:
        """
        The projection type (perspective or orthographic) of the camera.

        :getter: Returns the projection type of the camera.
        :setter: Sets the projection type of the camera.
        :type: CameraProjectionType

        Raises:
            ProjectError: If no project is opened.
        """
    @projection_type.setter
    def projection_type(self, projection_type: CameraProjectionType) -> None: ...
