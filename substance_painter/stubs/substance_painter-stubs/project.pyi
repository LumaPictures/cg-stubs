import dataclasses
import enum
import types
import uuid
from . import event as event
from _typeshed import Incomplete
from typing import Any, Callable

from _substance_painter.project import ProjectSaveMode as ProjectSaveMode
from _substance_painter.project import NormalMapFormat as NormalMapFormat
from _substance_painter.project import TangentSpace as TangentSpace
from _substance_painter.project import ProjectWorkflow as ProjectWorkflow

@dataclasses.dataclass
class UsdSettings:
    '''
    Specific settings for USD files.

    This corresponds to the options that are available in the File type-specific settings section
    in the "New project" and "Project configuration" dialogs.

    :param scope_name: Scope name of the primitive to load in the hierarchy. The path must be
        absolute. Expected syntax: ``"/my/path/name"``.
        If not specified, default scope name is the root ``"/"``. Only available for USD files.
    :param variants: Define which variant to use for each primitive path. Values are expected in
        JSON format.
        ::

            [
                {
                    "primPath": "/my/path/name",
                    "selectionName: "variantName",
                    "setName": "variantSetName"
                }
            ]

        Only available for USD files.
    :param subdivision_level: The subdivision level is applied only on geometry built with
        subdivision. Only available for USD files.
    :param frame: The frame to import. Only available for animated USD files.
    '''
    scope_name: str = ...
    variants: dict = ...
    subdivision_level: int = ...
    frame: int = ...

@dataclasses.dataclass
class GltfSettings:
    '''
    Specific settings for GLTF files.

    This corresponds to the options that are available in the File type-specific settings section
    in the "New project" dialog.

    :param invert_normal_maps: Invert normal maps at import. Only available for GLTF files.
    '''
    invert_normal_maps: bool = ...

@dataclasses.dataclass
class Settings:
    '''
    Project configuration options. All options can be set to ``None`` to use the default values.

    This corresponds to the options that are available in the "New project" dialog.

    See also:
        :class:`NormalMapFormat`,
        :class:`TangentSpace`,
        :class:`ProjectWorkflow`,
        :func:`create`,
        `Project configuration documentation`_.

    .. _Project configuration documentation:
        https://www.adobe.com/go/painter-project-configuration

    :param default_save_path: The default save path.
    :param normal_map_format: Normal map system coordinates. OpenGL or DirectX format.
    :param tangent_space_mode: Per vertex or per fragment tangent space.
    :param project_workflow: Project workflow, selected at project creation time.
    :param export_path: Use this path as the default map export path.
    :param default_texture_resolution: Default resolution for all the Texture Sets.
    :param import_cameras: Import cameras from the mesh file.
    :param mesh_unit_scale: Use custom unit scale for input mesh. Painter unit is centimeters.
        If set to 0 or None, use mesh file internal unit scale.
        This setting is necessary for .obj meshes that use units other than centimeters.
    :param mesh_settings: Specific mesh settings.
    :param usd_settings: Deprecated, use mesh_settings instead.
    :type usd_settings: UsdSettings
    '''
    default_save_path: str = ...
    normal_map_format: NormalMapFormat = ...
    tangent_space_mode: TangentSpace = ...
    project_workflow: ProjectWorkflow = ...
    export_path: str = ...
    default_texture_resolution: int = ...
    import_cameras: bool = ...
    mesh_unit_scale: float = ...
    mesh_settings: UsdSettings | GltfSettings = ...
    @property
    def usd_settings(self):
        """
        :meta private:
        """
    @usd_settings.setter
    def usd_settings(self, value) -> None:
        """
        :meta private:
        """

@dataclasses.dataclass
class MeshReloadingSettings:
    '''
    Settings used when reloading a mesh.

    This corresponds to the mesh related options that are available in the
    "Project configuration" dialog.

    See also:
        :func:`reload_mesh`,
        `Project configuration documentation`_.

    .. _Project configuration documentation:
        https://www.adobe.com/go/painter-project-configuration

    :param import_cameras: Import cameras from the mesh file.
    :param preserve_strokes: Preserve strokes positions on mesh.
    :param mesh_settings: Specific settings for USD files.
    :param usd_settings: Deprecated, use mesh_settings instead.
    '''
    import_cameras: bool = ...
    preserve_strokes: bool = ...
    mesh_settings: UsdSettings = ...
    @property
    def usd_settings(self):
        """
        :meta private:
        """
    @usd_settings.setter
    def usd_settings(self, value) -> None:
        """
        :meta private:
        """

class _ActionLock:
    """
    Utility class to perform project operations which require locking the project first.
    For some operations, such as :func:`save`, :func:`save_as_copy` and :func:`save_as_template`,
    the project must be locked before the operation can be performed.
    Once the operation is done, the project must be unlocked.
    This class provides a context manager to make lock and unlock regardless of raised errors.

    Example:
        ::

            with substance_painter.project._ActionLock():
                _substance_painter.project.save()

    """
    def __enter__(self): ...
    def __exit__(self, err_type: type[BaseException] | None, err_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def name() -> str | None:
    """
    Return the name of the current project.

    Returns:
        str: The name of the current project, or ``None`` if the project hasn't
        been saved yet.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        ProjectError: If no project is opened.
    """
def file_path() -> str | None:
    """
    Return the file path of the current project. This is the path where the
    project will be written to when it is saved.

    Returns:
        str: The file path of the current project, or ``None`` if the project
        hasn't been saved yet.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        ProjectError: If no project is opened.

    See also:
        :func:`save`,
        :func:`save_as`.
    """
def close() -> None:
    """
    Close the current project.

    Warning:
        Any unsaved data will be lost.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        ProjectError: If no project is opened.
    """
def open(project_file_path: str) -> None:
    """
    Open the project located at ``project_file_path``.

    Args:
        project_file_path (str): The path to the project file (with the extension ``.spp``).

    Raises:
        ProjectError: If Substance 3D Painter cannot open the file ``project_file_path``.
        ProjectError: If there is already an opened project.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
    """
def is_open() -> bool:
    """
    Check if a project is already opened.

    Returns:
        bool: ``True`` if a project is opened, ``False`` otherwise.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
    """
def needs_saving() -> bool:
    """
    Check if the current project needs to be saved.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        ProjectError: If no project is opened.

    Returns:
        bool: ``True`` if the project has modifications and needs to be saved,
        ``False`` otherwise.
    """
def is_in_edition_state() -> bool:
    """
    Check if the current project is ready to work with.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        ProjectError: If no project is opened.

    Returns:
        bool: ``True`` if the project is ready to work with,
        ``False`` otherwise.

    See also:
        :class:`substance_painter.event.ProjectEditionEntered`,
        :class:`substance_painter.event.ProjectEditionLeft`.
    """
def is_busy() -> bool:
    """
    Check if Substance 3D Painter is currently busy.
    If busy, the project cannot be saved at the moment.
    The application may be busy because no project is in edition state,
    or a long process such as baking/export/unwrap process is ongoing.
    The corresponding BusyStatusChanged event is fired when the busy state changes.

    Returns:
        bool: ``True`` if the project is ready to be saved,
        ``False`` otherwise.

    See also:
        :func:`execute_when_not_busy`,
        :class:`substance_painter.event.BusyStatusChanged`.
    """
def execute_when_not_busy(callback: Callable[[], None]) -> None:
    """
    Execute the given callback when Substance 3D Painter is not busy.

    Args:
        callback (Callable[[], None]): The callback to be executed.

    See also:
        :func:`is_busy`,
        :class:`substance_painter.event.BusyStatusChanged`.
    """
def save_as(project_file_path: str, mode: ProjectSaveMode = ...) -> None:
    """
    Save the current project by writing it to the file path ``project_file_path``.

    Note:
        If the path ``project_file_path`` doesn't exist yet, new folders will be
        created as needed.
        Save is disabled when Substance 3D Painter is busy and will throw a ProjectError.

    Args:
        project_file_path (string): The file path to save the project to.
        mode (ProjectSaveMode): The save mode (Incremental or Full).

    Raises:
        ProjectError: If Substance 3D Painter cannot save the project.
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.

    See also:
        :class:`ProjectSaveMode`,
        :func:`save`,
        :func:`save_as_copy`.
        :func:`is_busy`.
    """
def save(mode: ProjectSaveMode = ...) -> None:
    """
    Save the current project by overwriting the previous save.

    Note:
        Save is disabled when Substance 3D Painter is busy and will throw a ProjectError.

    Args:
        mode (ProjectSaveMode): The save mode (Incremental or Full).

    Raises:
        ProjectError: If Substance 3D Painter cannot save the project.
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.

    See also:
        :class:`ProjectSaveMode`,
        :func:`save_as`,
        :func:`save_as_copy`.
        :func:`is_busy`.
    """
def save_as_copy(backup_file_path: str, mode: ProjectSaveMode = ...) -> None:
    """
    Save a copy of the current project by writing it to the file path
    ``backup_file_path``. This can be used to save backups of the opened project
    without modifying the original file.

    After `save_as_copy` the project is still considered to be located at the
    location it was previously saved to. If the project was not saved, it is
    still considered to not have a saved location.

    Note:
        If the path ``backup_file_path`` doesn't exist yet, new folders will be
        created as needed.
        Save is disabled when Substance 3D Painter is busy and will throw a ProjectError.

    Args:
        backup_file_path (string): The path to write the copy of the project to.
        mode (ProjectSaveMode): The save mode (Incremental or Full).

    Raises:
        ProjectError: If Substance 3D Painter cannot save the copy.
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.

    See also:
        :class:`ProjectSaveMode`,
        :func:`save`,
        :func:`save_as`.
        :func:`is_busy`.
    """
def save_as_template(template_file_path: str, texture_set_name: str) -> ProjectSaveMode:
    """
    Save a template based of the current Texture Set or the one specified.

    Note:
        New folders will be created if they are missing.
        Save is disabled when Substance 3D Painter is busy and will throw a ProjectError.

    Warning:
        If the file already exists, it will be overwritten.

    Args:
        template_file_path (string): The save path.
        texture_set_name (string): Name of the Texture Set used as a template.

    Raises:
        ProjectError: If Substance 3D Painter cannot save the template.
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.

    See also:
        :func:`is_busy`.
    """
def create(mesh_file_path: str, mesh_map_file_paths: list[str] = None, template_file_path: str = None, settings: Settings = ...):  # type: ignore[assignment]
    """
    Create a new project.
    If an ``OCIO`` environment variable is set, pointing to a .ocio configuration file,
    the project is setup to use the OCIO color management mode defined by that file.
    If the configuration defined by that file is invalid, a ``ProjectError`` is raised and
    no project is created.
    Similary, if a ``PAINTER_ACE_CONFIG`` environment variable is set, pointing to a .json
    preset file, the project is setup to use the ACE color management mode defined by that file.
    If the preset defined in that file is invalid, a ``ProjectError`` is raised and no project
    is created.
    If both environment variables are set, ``OCIO`` will be used.
    If there is not such environment variable, the project uses the Legacy color management mode.

    Note:
        Project settings override the template parameters.

    Args:
        mesh_file_path (string): File path of the mesh to edit.
            Supported file formats: fbx, obj, dae, ply, usd.
        mesh_map_file_paths (list of string): Paths to the additional mesh maps.
        template_file_path (string): Template file path to use to create the project.
        settings (Settings): Configuration options of the new project.

    Raises:
        ProjectError: If Substance 3D Painter cannot create the project.
        ProjectError: If there is already an opened project.
        ProjectError: If an ``OCIO`` environment variable is set to an invalid configuration.
        ProjectError: If an ``PAINTER_ACE_CONFIG`` environment variable is set to an invalid preset.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        TypeError: If ``settings`` is not an instance of Settings.
        ValueError: If the file format of ``mesh_file_path`` is not supported.
        ValueError: If the mesh file ``mesh_file_path`` does not exist.
        ValueError: If any of the mesh map files in ``mesh_map_file_paths`` do not exist.
        ValueError: If the template file ``template_file_path`` doesn't exist.
        ValueError: If the template file ``template_file_path`` is invalid.
        ValueError: If ``settings`` are not valid project settings (see documentation
            of :class:`Settings`).
        ValueError: If ``settings.default_texture_resolution`` is not a valid resolution.

    See also:
        :class:`Settings`,
        `Project creation documentation`_.

    .. _Project creation documentation:
        https://www.adobe.com/go/painter-project-creation
    """
def last_imported_mesh_path() -> str:
    """
    Return the path to the last imported mesh.

    Returns:
        str: The file path of the mesh that was last imported to the project.

    Raises:
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
    """
def last_saved_substance_painter_version() -> tuple[int, int, int] | None:
    """
    Return the version of Substance 3D Painter used to last save the project, or None
    if the project is unsaved or was saved with version <= 8.2.0.

    Returns:
        Tuple(int, int, int): The concerned version of Substance 3D Painter, as a major/minor/patch
        tuple.

    Raises:
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
    """

class ReloadMeshStatus(enum.Enum):
    """
    Reload mesh status, used in mesh reload asynchronous callback.

    See also:
        :func:`reload_mesh`,
    """
    SUCCESS = 0
    ERROR = 2

def reload_mesh(mesh_file_path: str, settings: MeshReloadingSettings, loading_status_cb: Callable[[ReloadMeshStatus], Any]):
    """
    Import a new mesh to the current project, using the given settings.
    Uses the automatic UV unwrapping settings defined at the project level.

    The loading is asynchronous: this function returns immediately; when
    the loading attempt is finished ``loading_status_cb`` is called with
    an argument indicating if loading was successful.

    Args:
        mesh_file_path (string): File path of the mesh to edit.
            Supported file formats: fbx, obj, dae, ply, usd.
        settings (MeshReloadingSettings): Configuration options for the mesh loading.
        loading_status_cb (Callable[[ReloadMeshStatus], Any]): Loading status notification callback.

    Raises:
        ProjectError: If no project is opened or Substance 3D Painter is busy.
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.

    See also:
        :class:`ReloadMeshStatus`,
        :class:`MeshReloadingSettings`,
        :func:`is_busy`,
        `Project creation documentation`_.

    .. _Project creation documentation:
        https://www.adobe.com/go/painter-project-creation
    """

@dataclasses.dataclass(frozen=True)
class BoundingBox:
    """
    Axis-aligned bounding box (AABB).

    :param dimensions: The dimensions (x,y,z) of the bounding box.
    :param center: The center (x,y,z) of the bounding box..
    :param radius: The radius of the bounding box.

    See also:
        :func:`get_scene_bounding_box`,
    """
    dimensions: list[float]
    center: list[float]
    radius: float

def get_scene_bounding_box() -> BoundingBox:
    """
    Return the bounding box of the scene.

    Returns:
        BoundingBox: The bounding box of the scene.

    Raises:
        ProjectError: If no project is opened.
    """
def get_uuid() -> uuid.UUID:
    """
    Return the UUID of the current project.

    Returns:
        uuid.UUID: The UUID of the current project.

    Raises:
        ProjectError: If no project is opened.
    """

class Metadata:
    '''
    Project metadata are arbitrary data that can be attached to a `Substance
    Painter` project. When the project is saved, the metadata are saved with it,
    so it is still available the next time the project is loaded.

    Metadata can only be accessed when a project is opened. If no project is
    opened, the methods will raise an exception.

    The constructor of the class ``Metadata`` takes a context name as an
    argument. This context name can be for example the name of your plugin. It
    should be unique, to avoid conflict with other plugins.

    Example:
        ::

            import substance_painter

            # Instantiate the Metadata utility, for the plugin "MyPlugin".
            metadata = substance_painter.project.Metadata("MyPlugin")

            # Store a version number under the key "version".
            plugin_version = { "major": 1, "minor": 0 }
            metadata.set("version", plugin_version)

            # List the project\'s metadata keys. The key "version" is now present.
            keys = metadata.list()
            print(keys)

            # Retrieve the metadata "version".
            plugin_version = metadata.get("version")
            print("Version: " + str(plugin_version))
    '''
    def __init__(self, context: str) -> None: ...
    def list(self) -> list:
        """
        Return the list of project metadata keys.

        Raises:
            ProjectError: If no project is opened.
            ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        """
    def get(self, key: str):
        """
        Retrieve the project metadata under the given key.

        The supported data types are:
            - Primitive types: `bool`, `int`, `float`, `str`.
            - `list`
               - Items can be any of the supported data types.
            - `dict`
               - Keys must be of type `str`.
               - Values can be any of the supported data types.

        Args:
            key (str): The key identifying the metadata to retrieve.

        Raises:
            ProjectError: If no project is opened.
            RuntimeError: If the metadata under ``key`` use a type that is not supported.
            ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        """
    def set(self, key: str, value):
        """
        Store project metadata under the given key.

        The supported data types are:
            - Primitive types: `bool`, `int`, `float`, `str`.
            - `list`
               - Items can be any of the supported data types.
            - `dict`
               - Keys must be of type `str`.
               - Values can be any of the supported data types.

        Args:
            key (str): The key identifying the metadata to store.
            value: The metadata to store.

        Raises:
            ProjectError: If no project is opened.
            RuntimeError: If ``value`` uses a type that is not supported.
            ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        """
