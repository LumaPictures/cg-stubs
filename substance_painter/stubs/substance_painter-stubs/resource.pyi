import _substance_painter.resource
import dataclasses
import enum
from _typeshed import Incomplete

class ResourceLocation(enum.Enum):
    '''Each resource has a location determined by where its data lives.

    Members:

    =========== ====================
    Name        Data location
    =========== ====================
    ``SESSION`` Current session; those ressources will be lost after a restart of the application.
    ``PROJECT`` A Substance 3D Painter project; those resources are embedded in the spp file.
    ``SHELF``   One of the Substance 3D Painter Shelves.
    =========== ====================

    Example:
        ::

            import substance_painter.resource

            # For a resource from the default shelf
            aluminium = substance_painter.resource.ResourceID(
                context="starter_assets", name="Aluminium Insulator");

            # This will print:
            # ResourceLocation.SHELF
            print(aluminium.location())

            # For an embedded resource, like a baked map
            aomap = substance_painter.resource.ResourceID.from_project(
                name="ambient_occlusion");

            # This will print:
            # ResourceLocation.PROJECT
            print(aomap.location())

            # Finally, for a temporary resource
            test_envmap = substance_painter.resource.ResourceID.from_session(
                name="Test Envmap");

            # This will print:
            # ResourceLocation.SESSION
            print(test_envmap.location())

    '''
    SESSION = ...
    PROJECT = ...
    SHELF = ...

@dataclasses.dataclass(frozen=True)
class ResourceID:
    """
    A `Substance 3D Painter` resource identifier.

    The resource is identified by a context, a name, and a version. The context
    and the name are mandatory while the version is optional. The version is a
    string that looks like a hash, and may also contain an extension.

    Note:
        A ResourceID object is only an identifier. It provides no guarantees that
        the resource actually exists.

    See also:
        :mod:`substance_painter.display`.
    """
    context: str
    name: str
    version: str = ...
    @classmethod
    def from_url(cls, url: str):
        """
        Create a `ResourceID` object from its URL.
        URLs must have ``resource://`` as a scheme. The version is encoded as a query
        string, that looks like a hash.

        A resource URL looks like this:

        ``resource://context/name?version=0123456789abcdef0123456789abcdef01234567.image``

        Args:
            url (str): The resource URL.

        Returns:
            ResourceID: The resource corresponding to the given URL.

        Raises:
            ValueError: If ``url`` is not a valid URL.
            ValueError: If the URL scheme is not ``resource://``.
            ValueError: If the resource name is invalid.
        """
    @classmethod
    def from_project(cls, name: str, version: str = None):  # type: ignore[assignment]
        """
        Create a `ResourceID` object for a resource located in the current project.

        Args:
            name (str): The resource name.
            version (str, optional): The resource version (hash-like string).

        Returns:
            ResourceID: The resource corresponding to the given name.
        """
    @classmethod
    def from_session(cls, name: str, version: str = None):  # type: ignore[assignment]
        """
        Create a `ResourceID` object for a resource located in the current session.

        Args:
            name (str): The resource name.
            version (str, optional): The resource version (hash-like string).

        Returns:
            ResourceID: The resource corresponding to the given name.
        """
    def url(self) -> str:
        """
        Get the URL form of this `ResourceID`.

        Returns:
            str: The URL of the resource.

        Raises:
            ValueError: If the `ResourceID` doesn't have a context.
            ValueError: If the `ResourceID` doesn't have a name.
        """
    def location(self) -> ResourceLocation:
        """
        Get the location of this `ResourceID`.

        Returns:
            ResourceLocation: The location of this resource.
        """

class Usage(enum.Enum):
    """
    Enumeration describing how a given resource is meant to be used.

    Members:

    ===================== ====================
    Name                  Usage
    ===================== ====================
    ``ALPHA``             A brush alpha.
    ``BASE_MATERIAL``     A material.
    ``BRUSH``             A brush definition.
    ``COLOR_LUT``         A color look-up table.
    ``EMITTER``           A particle emitter script.
    ``ENVIRONMENT``       An environment map.
    ``EXPORT``            An export preset.
    ``FILTER``            A layer stack filter.
    ``FONT``              A text font.
    ``GENERATOR``         A mask generator.
    ``PARTICLE``          A particles effect.
    ``PROCEDURAL``        A procedural substance, like a noise.
    ``RECEIVER``          A particle receiver script.
    ``SHADER``            A shader.
    ``SMART_MASK``        A smart mask.
    ``SMART_MATERIAL``    A smart material.
    ``TEXTURE``           A UV space map like bakes.
    ``TOOL``              A painting tool preset.
    ===================== ====================

    See also:
        :func:`import_project_resource`,
        :func:`import_session_resource`,
        :meth:`Shelf.import_resource`.
    """
    ALPHA = ...
    BASE_MATERIAL = ...
    BRUSH = ...
    COLOR_LUT = ...
    EMITTER = ...
    ENVIRONMENT = ...
    EXPORT = ...
    FILTER = ...
    FONT = ...
    GENERATOR = ...
    PARTICLE = ...
    PROCEDURAL = ...
    RECEIVER = ...
    SHADER = ...
    SMART_MASK = ...
    SMART_MATERIAL = ...
    TEXTURE = ...
    TOOL = ...

class Type(enum.Enum):
    """
    Enumeration describing the type of a given resource.

    Members:

    ===================== ====================
    Name                  Usage
    ===================== ====================
    ``ABR_PACKAGE``       A photoshop brushes package.
    ``BRUSH``             A brush.
    ``EXPORT``            An export preset.
    ``FONT``              A text font.
    ``IMAGE``             An image.
    ``PRESET``            A resource preset.
    ``RESOURCE``          A resource.
    ``SCRIPT``            A particle emitter script.
    ``SHADER``            A shader.
    ``SMART_MASK``        A smart mask.
    ``SMART_MATERIAL``    A smart material.
    ``SUBSTANCE``         A substance.
    ``SUBSTANCE_PACKAGE`` A substance package.
    ``VECTORIAL``         A vectorial image.
    ===================== ====================
    """
    ABR_PACKAGE = ...
    BRUSH = ...
    EXPORT = ...
    FONT = ...
    IMAGE = ...
    PRESET = ...
    RESOURCE = ...
    SCRIPT = ...
    SHADER = ...
    SMART_MASK = ...
    SMART_MATERIAL = ...
    SUBSTANCE = ...
    SUBSTANCE_PACKAGE = ...
    VECTORIAL = ...

@dataclasses.dataclass(frozen=True)
class Resource:
    """
    A `Substance 3D Painter` resource.
    """
    handle: _substance_painter.resource.ResourceHandle
    def __eq__(self, other):
        """Compare inner handles"""
    def __hash__(self):
        """Hash based on inner handle"""
    def identifier(self) -> ResourceID:
        """
        Get this resource identifier.

        Returns:
            ResourceID: The resource identifier.

        Raises:
            RuntimeError: If the resource is invalid.

        See also:
            :class:`ResourceID`.
        """
    def location(self) -> ResourceLocation:
        """
        Get the location of this `Resource`.

        Returns:
            ResourceLocation: The location of this resource.

        Raises:
            RuntimeError: If the resource is invalid.
        """
    @staticmethod
    def retrieve(identifier: ResourceID):
        """
        Retrieve a list of resources matching the given identifier.

        Args:
            identifier (ResourceID): A resource identifier.

        Raises:
            ValueError: If the name of the identifier is empty
                or if the context of the identifier doesn't exists.
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        Returns:
            typing.List[Resource]: The list of resources matching the given identifier.
            If the identifier has a valid version, this method will return only one or
            zero resources, otherwise the list may contain several resources. In case
            of several resources are returned, the most up to date resource will be at
            the begining of the list.
        """
    def set_custom_preview(self, preview_image: str) -> None:
        """
        Replace the current preview of this resource with a custom image.

        Args:
            preview_image (str): File path to an image on the disk to use as the new
                preview.

        Raises:
            ValueError: If the resource metadata cannot be modified.
            ValueError: If ``preview_image`` is not a valid path to a valid image.
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        Note:
            The preview image can be a JPEG, a PNG or an XPM.
        """
    def category(self) -> str:
        '''
        Get the category of this resource, ex: "wood" for a material.

        Raises:
            RuntimeError: If the resource is invalid.

        Returns:
            str: the category of this resource
        '''
    def usages(self) -> list[Usage]:
        """
        Get the usages of this resource.

        Raises:
            RuntimeError: If the resource is invalid.

        Returns:
            typing.List[Usage]: the usages of this resource

        See also:
            :class:`Usage`
        """
    def gui_name(self) -> str:
        """
        Get the GUI name of this resource.

        Raises:
            RuntimeError: If the resource is invalid.

        Returns:
            str: the GUI name of this resource
        """
    def type(self) -> Type:
        """
        Get the type of this resource.

        Raises:
            RuntimeError: If the resource is invalid.

        Returns:
            Type: the type of this resource

        See also:
            :class:`Type`
        """
    def tags(self) -> list[str]:
        """
        Get the tags of this resource.

        Raises:
            RuntimeError: If the resource is invalid.

        Returns:
            typing.List[str]: the tags of this resource
        """
    def internal_properties(self) -> dict:
        """
        Get a dictionnary of the resource internal properties.
        The current implementation only extracts metadata on Substance resources.

        Raises:
            RuntimeError: If the resource is invalid.

        Returns:
            dict: a dictionnary containing internal properties about this resource
        """
    def children(self) -> list['Resource']:
        """
        Get child resources.
        For example substance graphs of a substance package.

        Raises:
            RuntimeError: If the resource is invalid.

        Returns:
            typing.List[Resource]: Resources contained in this resource.
        """
    def parent(self) -> Resource | None:
        """
        Get parent resource.
        For example the substance package a substance graph is originating from.

        Raises:
            RuntimeError: If the resource is invalid.

        Returns:
            typing.Optional[Resource]: The parent resource that owns this resource.
        """
    def reset_preview(self) -> None:
        """
        Remove any custom preview for this resource and resets to the default one.

        Raises:
            ValueError: If the resource metadata cannot be modified.
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.
        """
    def show_in_ui(self) -> None:
        """
        Highlight this resource in the application shelf UI (Assets window).

        Raises:
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        See also:
            :func:`show_resources_in_ui`.
        """

def show_resources_in_ui(resources: list[Resource]) -> None:
    """
    Highlight a list of resources in the application shelf UI (Assets window).

    Args:
        resources (List[Resource]): Resources to highlight

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.

    See also:
        :func:`Resource.show_in_ui`.
    """
def import_project_resource(file_path: str, resource_usage: Usage, name: str = None, group: str = None) -> Resource:  # type: ignore[assignment]
    """
    Import a resource into the current opened project.

    Args:
        file_path (str): The file path to the resource to be imported.
        resource_usage (Usage): The resource usage.
        name (str, optional): The name of the resource if different from the
            file name.
        group (str, opional): An optional group name, can be used in resource
            queries.

    Returns:
        Resource: The imported resource object.

    Raises:
        ProjectError: If no project is opened.
        ValueError: If parameters validation failed.
        RuntimeError: If import failed.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """
def import_session_resource(file_path: str, resource_usage: Usage, name: str = None, group: str = None) -> Resource:  # type: ignore[assignment]
    """
    Import a resource into the current session.

    Args:
        file_path (str): The file path to the resource to be imported.
        resource_usage (Usage): The resource usage.
        name (str, optional): The name of the resource if different from the
            file name.
        group (str, opional): An optional group name, can be used in resource
            queries.

    Returns:
        Resource: The imported resource object.

    Raises:
        ValueError: If parameters validation failed.
        RuntimeError: If import failed.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """

class StandardQuery:
    """
    Standard resource queries.

    Members:

    ====================== ====================
    Name                   Query
    ====================== ====================
    ``ALL_RESOURCES``      All resources.
    ``PROJECT_RESOURCES``  Resources that belongs to the current project.
    ``SESSION_RESOURCES``  Resources that belongs to the current session.
    ``SHELVES_RESOURCES``  All shelves resources.
    ====================== ====================

    See also:
        :func:`search`.
    """
    ALL_RESOURCES: str
    PROJECT_RESOURCES: str
    SESSION_RESOURCES: str
    SHELVES_RESOURCES: str

def search(query: str) -> list[Resource]:
    """
    List Substance 3D Painter resources that match the given query.

    Args:
        query (str): A resource query string. See `text query documentation`_.

    Returns:
        List[Resource]: The list of resources that match the given query.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.

    See also:
        :class:`StandardQuery`.

    .. _text query documentation:
        https://www.adobe.com/go/painter-filtering-shelf-content
    """
def list_layer_stack_resources() -> list[ResourceID]:
    """
    List the resources referenced by the layer stacks and mesh maps of the current
    project.

    Returns:
        List[ResourceID]: The list of resource identifiers referenced.

    Raises:
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.

    Warning:
        Deprecated since 0.3.4, use :func:`list_project_resources` instead.

    See also:
        :func:`update_layer_stack_resource`,
        :mod:`substance_painter.display`.
    """
def update_layer_stack_resource(old_resource_id: ResourceID, new_resource: Resource) -> list[ResourceID]:
    """
    Replace resources from the layer stacks and mesh maps in the current project.

    Given a resource identifier, replace any resource having the same identifier
    with the new resource. The new resource must be compatible with the ones it
    replaces (see note); otherwise, an error is thrown.

    Note:
        The new resource must be of the same type as the resources it replaces.
        For example a base material resource cannot be updated with a vectorial resource.

        Moreover:

        - If the resource is a Substance material, it must have the same number
          and names of outputs.
        - If the resource is a Substance filter, it must have the same number
          and names of inputs and outputs.

    Returns:
        List[ResourceID]: The list of identifiers of all the resources that have
        been replaced.

    Args:
        old_resource_id (ResourceID): The identifier of the resource(s) to update.
        new_resource (Resource): The new resource to use instead.

    Raises:
        ProjectError: If no project is opened.
        TypeError: If ``old_resource_id`` is not a ResourceID.
        TypeError: If ``new_resource`` is not a Resource.
        RuntimeError: If ``new_resource`` is not a valid resource.
        RuntimeError: If ``new_resource`` cannot be used in place of
            ``old_resource_id``.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.

    Warning:
        Using this function in a loop to replace a lot of resources can be time-consuming and
        can cause a temporary freeze of the application. See
        :func:`replace_project_resources` which is more efficient.

    Warning:
        Deprecated since 0.3.4, use :func:`replace_project_resources` instead.

    See also:
        :func:`list_layer_stack_resources`,
        :class:`Usage`,
        :mod:`substance_painter.display`.
    """
def list_project_resources() -> list[ResourceID]:
    """
    List the resources used in the current project. Project resources are all
    the resources used in the project (in the layerstack, shaders, environment map, etc.).

    Returns:
        List[ResourceID]: The list of resource identifiers.

    Raises:
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.

    See also:
        :func:`replace_project_resources`.
    """
def list_project_outdated_resources() -> dict[ResourceID, ResourceID]:
    """
    List the resources used in the current project that are outdated. Project resources are all
    the resources used in the project (in the layerstack, shaders, environment map, etc.).
    An outdated resource is a resource that has been reloaded in the application, but not yet
    updated in the project.

    Returns:
        Dict[ResourceID,ResourceID]: A dictionary with the old resources identifier as key and
        the new resources identifier as value.

    Raises:
        ProjectError: If no project is opened.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.

    See also:
        :func:`replace_project_resources`.
    """

from _substance_painter.resource import UpdateProjectStatus as UpdateProjectStatus  # type: ignore[attr-defined]

@dataclasses.dataclass(frozen=True)
class UpdateProjectError:
    """
    Error that occurred during the :func:`replace_project_resources` operation.

    :param old_id: The identifier of the resource that could not be updated.
    :param new_id: The identifier of the resource that was supposed to replace the old one.
    :param details: A list of errors messages.

    See also:
        :func:`replace_project_resources`, :class:`UpdateProjectResult`.
    """
    old_resource_id: ResourceID
    new_resource_id: ResourceID
    details: list[str]

@dataclasses.dataclass(frozen=True)
class UpdateProjectResult:
    """
    Result of the :func:`replace_project_resources` operation.

    :param status: The status of the operation.
    :param errors: A list of errors if the operation failed. If the operation
        was successful, this list is empty.

    See also:
        :func:`replace_project_resources`, :class:`UpdateProjectStatus`,
        :class:`UpdateProjectError`.
    """
    status: UpdateProjectStatus
    errors: list[UpdateProjectError]

def replace_project_resources(ids: dict[ResourceID, ResourceID], allow_parameters_mismatch: bool = False) -> UpdateProjectResult:
    """
    Replace resources in the current project. Project resources are all
    the resources used in the project (in the layerstack, shaders, environment map, etc.).

    Given a pair of resource identifiers:

    - the first element is the old resource identifier used in the project,
    - the second element is the new resource identifier to use instead.

    The operation will replace any resource having the same identifier
    with the new resource. The new resource must be compatible with the ones it
    replaces (see note); otherwise, the operation will fail.

    If an error occurs during the update, no operation is performed on the project
    and the :class:`UpdateProjectStatus` provides a list of errors.

    Note:
        The new resource must be of the same type as the resources it replaces.
        For example a :class:`SUBSTANCE<Type>` resource cannot be updated with
        a :class:`VECTORIAL<Type>` resource.

        For more details on the rules to replace a resource, see the `Auto-Update documentation`_

    .. _Auto-Update documentation:
        https://www.adobe.com/go/painter-auto-update

    Args:
        ids (Dict[ResourceID, ResourceID]): A dictionary of resource identifiers
            to update (key: old, value: new).
            The dictionary must contain valid :class:`ResourceID`. If any resource identifier is
            invalid or if the key does not correspond to an existing resource
            in the project, the operation will fail.
            If the dictionary is empty, no operation is performed.
        allow_parameters_mismatch (bool, optional): By default (``False``), prevents resources with
            parameters (e.g., .sbsar, .ai files) used in the project from updating if parameters
            have been renamed or removed in the new version, so as to avoid unintended changes to
            the texturing results. If any parameter mismatch is detected, the operation will fail.
            If ``True``, any unmatched parameters will reset to their default values.

    Returns:
        UpdateProjectResult: The result of the operation.

    Raises:
        ProjectError: If no project is opened.
        RuntimeError: If the application is not in Painting mode.
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.

    Warning:
        This operation can be time-consuming if many resources are replaced or if the resources
        are used a lot in the project. It can cause a temporary freeze of the application.
        To avoid this issue, it is recommanded to split the operation in several batches.

    See also:
        :func:`list_project_resources`, :func:`list_project_outdated_resources`,
        :class:`UpdateProjectResult`, `Auto-Update documentation`_.
    """

@dataclasses.dataclass(frozen=True)
class Shelf:
    """
    Class providing information on a given `Substance 3D Painter` shelf. A shelf
    is identified by a unique `name`.
    """
    def name(self) -> str:
        """
        Returns:
            The shelf name.
            Each shelf is identified by a unique `name`.
        """
    def path(self) -> str:
        """
        Returns:
            The associated path

        Raises:
            ValueError: If the shelf doesn't exist anymore.
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.
        """
    def resources(self, query: str = ...) -> list[Resource]:
        """
        Get resources contained in this shelf. An optional query string can be given
        to narrow the results.

        Args:
            query (str, optional): A resource query string.

        Returns:
            This shelf's list of resources.

        See also:
            :func:`search`.
        """
    def can_import_resources(self) -> bool:
        """
        Check if resources can be imported into this shelf.
        Resources can be imported into a shelf, as long as it is not a read-only shelf.
        The Substance shelf, installed along the application, is read-only. A shelf is
        also read-only if its path on the file system is read-only.

        Returns:
            bool: ``True`` if resources can be imported.

        Raises:
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        See also:
            :class:`substance_painter.event.ShelfCrawlingEnded`.
        """
    def import_resource(self, file_path: str, resource_usage: Usage, name: str = None, group: str = None, uuid: str = None) -> Resource:  # type: ignore[assignment]
        """
        Import a resource into this shelf.

        Args:
            file_path (str): The file path to the resource to be imported.
            resource_usage (Usage): The resource usage.
            name (str, optional): The name of the resource if different from the
                file name.
            group (str, opional): An optional group name, can be used in resource
                queries.
            uuid (str, opional): An optional uuid. If a resource already exists with
                the same uuid, it will be replaced.

        Returns:
            Resource: The imported resource object.

        Raises:
            ValueError: If parameters validation failed.
            RuntimeError: If import failed.
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.
        """
    def is_crawling(self) -> bool:
        """
        Check if this shelf is currently discovering resources in folders.

        Returns:
            bool: ``True`` if this shelf is discovering resources, ``False`` otherwise.

        Raises:
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        See also:
            :class:`substance_painter.event.ShelfCrawlingEnded`.
        """
    def refresh(self) -> None:
        """
        Forces discovering of resources in shelf folders.
        Discovering is also done automatically when the application window gets focus.

        Raises:
            ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        """

class Shelves:
    """
    Collection of static methods to manipulate shelves.
    """
    @staticmethod
    def all() -> list[Shelf]:
        """
        List all shelves.

        Returns:
            typing.List[Shelf]: List of existing shelves.

        Raises:
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.
        """
    @staticmethod
    def exists(name: str) -> bool:
        """
        Tell whether a shelf with the given name exists.

        Args:
            name (str): Shelf name to searh for.

        Returns:
            bool: ``True`` if a shelf with the given name exists.

        Raises:
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.
        """
    @staticmethod
    def add(name: str, path: str) -> Shelf:
        """
        Add a new shelf. This shelf will only be valid during the application session.
        The shelf will not be visible from application general settings menu.

        Args:
            name (str): Name of the new shelf. This name must be unique and must only
                contain lowercase letters, numbers, underscores or hyphens.
                Use :func:`Shelves.exists` to check if name is already used.
            path (str): Folder path to monitor.

        Returns:
            Shelf: Newly added shelf.

        Raises:
            ValueError: If ``name`` or ``str`` are invalid. See logs for details.
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        See also:
            :meth:`Shelves.exists`.
            :meth:`Shelf.refresh`.
        """
    @staticmethod
    def remove(name: str):
        """
        Removes a shelf.
        No project must be opened.
        Deleting a shelf which was not created by the Python API is not possible and
        will raise an exception.

        Args:
            name (str): Name of the shelf to delete.
                Use :meth:`Shelves.exists` to check if a shelf exists.

        Raises:
            ProjectError: If a project is opened.
            ValueError: If the shelf doesn't exist.
            ValueError: If the shelf was not created with the Python API.
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        See also:
            :meth:`Shelves.exists`.
        """
    @staticmethod
    def refresh_all() -> None:
        """
        Forces discovering of resources in all shelves folders.
        Discovering is also done automatically when the application window gets focus.

        Raises:
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        See also:
            :meth:`Shelf.refresh`.
        """
    @staticmethod
    def user_shelf() -> Shelf:
        """
        This is the shelf located in the user Documents folder where new resources
        are created by default. The user can select a different default shelf in the
        settings, and this will be reflected when using this function.

        Raises:
            ServiceNotFoundError: If Substance 3D Painter has not started all its
                services yet.

        See also:
            `Default shelf documentation`_.

        .. _Default shelf documentation:
            https://docs.substance3d.com/spdoc/shelf-configuration-124059665.html
        """
    @staticmethod
    def application_shelf() -> Shelf:
        """
        This is the shelf containing the default content shipped with the application.
        """

@dataclasses.dataclass
class AllResourcesFilter:
    """
    Filter used to reload all modified resources known to Substance 3D Painter, which includes
    resources in all shelves, session-scoped resources, and project-scoped resources.

    See also:
        :func:`reload_modified_resources_async`
    """
@dataclasses.dataclass
class ProjectFilter:
    """
    Filter used to reload modified resources contained in the project context.
    This does not include resources used by the project (in the layerstack, shaders, environment
    map, etc.) if they are contained in a shelf or the session.

    See also:
        :func:`reload_modified_resources_async`
    """

@dataclasses.dataclass
class ResourcesListFilter:
    """
    Filter used to reload modified resources amongst a given list of resources.

    :param resources: The list of reources to reload.

    See also:
        :func:`reload_modified_resources_async`
    """
    resources: list[ResourceID]

@dataclasses.dataclass
class ResourcesUsedByProjectFilter:
    """
    Filter used to reload modified resources currently in use by the project.
    This includes resources from any contexts (project, shelves, session), as long as they are
    currently referenced by the project.

    See also:
        :func:`reload_modified_resources_async`
    """
@dataclasses.dataclass
class SessionFilter:
    """
    Filter used to reload modified resources contained in the session.

    See also:
        :func:`reload_modified_resources_async`
    """

@dataclasses.dataclass
class ShelvesListFilter:
    """
    Filter used to reload modified resources contained in designated shelves.

    :param shelves: The list of Shelves to reload.

    See also:
        :func:`reload_modified_resources_async`
    """
    shelves: list[Shelf]
ReloadResourcesFilter = AllResourcesFilter | ProjectFilter | ResourcesListFilter | ResourcesUsedByProjectFilter | SessionFilter | ShelvesListFilter

def reload_modified_resources_async(resource_filter: ReloadResourcesFilter) -> bool:
    """
    Triggers a reload of the modified resources found using the given filter. Outdated resources
    are excluded.

    If a reload operation is already running, this function will return ``False``.
    One can check if a reload operation is already running with
    :func:`is_reload_modified_resources_running`.

    This function being asynchronous, events will be sent to notify the progress of the operation:

    - :class:`substance_painter.event.ReloadResourcesStarted` when the operation starts.
    - :class:`substance_painter.event.ReloadResourcesEnded` when the operation ends.

    Args:
        resource_filter (AllResourcesFilter|ResourcesListFilter|ShelvesListFilter): A filter
            identifying which modified resources to reload.

    Returns:
        bool: ``True`` if the reload operation has started, ``False`` if it is already running.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its services yet.
        ValueError: When the given filter is now of a known type.
        ValueError: When the given filter is ill formed (eg points to unexisting resources). The
            exception provides one message per problems, as a List[str]

    See also:
        :func:`is_reload_modified_resources_running`
        :class:`substance_painter.event.ReloadResourcesStarted`
        :class:`substance_painter.event.ReloadResourcesEnded`
        :class:`AllResourcesFilter`
        :class:`ProjectFilter`
        :class:`ResourcesListFilter`
        :class:`ResourcesUsedByProjectFilter`
        :class:`SessionFilter`
        :class:`ShelvesListFilter`
    """
def is_reload_modified_resources_running() -> bool:
    """
    Check if a reload modified resources operation is currently running.

    Raises:
        ServiceNotFoundError: If Substance 3D Painter has not started all its
            services yet.
    """
