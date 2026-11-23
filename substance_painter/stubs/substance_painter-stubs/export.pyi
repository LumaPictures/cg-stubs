import dataclasses
import substance_painter.resource
import substance_painter.textureset
from _typeshed import Incomplete

from _substance_painter.export import ExportStatus as ExportStatus

def list_project_textures(json_config: dict) -> dict[tuple[str, str], list[str]]:
    """
    Get list of textures that would be exported according to the given JSON configuration.

    Args:
        json_config (dict): JSON object representing the export configuration to be used.
            See `JSON configuration <#full-json-config-dict-possibilities>`_.

    Returns:
        typing.Dict[typing.Tuple[str, str], typing.List[str]]: List of texture files
        that would be exported, grouped by stack (Texture Set name, stack name).

    Raises:
        ProjectError: If no project is opened.
        ValueError: If ``json_config`` is ill-formed, or is invalid in the context
            of the current project.
            Contains a human readable message.

    See also:
        :func:`export_project_textures`.
    """

@dataclasses.dataclass(frozen=True)
class TextureExportResult:
    """
    Result of the export textures process

    :param status: Status code.
    :param message: Human readable status message.
    :param textures: List of texture files
            written to disk, grouped by stack (Texture Set name, stack name).
    """
    status: ExportStatus
    message: str
    textures: dict[tuple[str, str], list[str]]

def export_project_textures(json_config: dict) -> TextureExportResult:
    '''
    Export document textures according to the given JSON configuration. The
    return value contains the list of texture files written to disk.

    The status of the return value can never be `Error`, any error causing the
    export to fail will raise an exception instead. However if the export fails,
    the associated event `ExportTextureEnded` will indeed receive `Error` as a
    status.
    If the export is cancelled by the user, the function return value will have
    the status `Cancelled` and contain the list of texture files written to disk
    before export was cancelled.

    Args:
        json_config (dict): JSON object representing the export configuration to be used.
            See `JSON configuration <#full-json-config-dict-possibilities>`_.

    Returns:
        TextureExportResult: Result of the export process.

    Raises:
        ProjectError: If no project is opened.
        ValueError: If ``json_config`` is ill-formed, or is invalid in the context
            of the current project. Contains a human readable message detailing
            the problem.

    See also:
        :class:`substance_painter.event.ExportTexturesAboutToStart`,
        :class:`substance_painter.event.ExportTexturesEnded`.


    Example:
    ::

        import substance_painter.export

        # Open a project we want to export from (see substance_painter.project
        # for details). This step is not necessary if there is already a project
        # opened in Substance 3D Painter.
        import substance_painter.project
        substance_painter.project.open("C:/projects/MeetMat.spp")

        # Choose an export preset to use (see substance_painter.resource). This
        # step is not mandatory as you can alternatively describe the export
        # preset entirely in JSON (see the full example at the bottom of the
        # page).
        # Note: in this example the preset file format and bit depth are
        # overridden below for \'03_Base\', but otherwise follow the export preset
        # configuration.
        import substance_painter.resource
        export_preset = substance_painter.resource.ResourceID(
            context="starter_assets", name="Arnold (AiStandard)")

        # Set the details of the export (a comprehensive example of all the
        # configuration options is presented at the bottom of the page):
        export_config = {
            "exportShaderParams": False,
            "exportPath": "C:/export",
            "defaultExportPreset" : export_preset.url(),
            "exportList": [
                {
                    "rootPath": "01_Head"
                },
                {
                    "rootPath": "02_Body"
                },
                {
                    "rootPath": "03_Base"
                }],
            "exportParameters": [
                # No filters: those parameters apply to all exported maps
                {
                    "parameters": {
                        "dithering": True,
                        "paddingAlgorithm": "infinite"
                    }
                },
                # Force file format and bitDepth for all maps in \'03_Base\'
                {
                    "filter": {"dataPaths": ["03_Base"]},
                    "parameters": {
                        "fileFormat" : "png",
                        "bitDepth" : "8"
                    }
                },
                # Force 2K size for all maps in \'01_Head\'
                {
                    "filter": {"dataPaths": ["01_Head"]},
                    "parameters": {
                        "sizeLog2": 11
                    }
                }]
            }

        # Display the list of textures that should be exported, according to the
        # configuration:
        export_list = substance_painter.export.list_project_textures(export_config)
        for k,v in export_list.items():
            print("Stack {0}:".format(k))
            for to_export in v:
                print(to_export)

        # Actual export operation:
        export_result = substance_painter.export.export_project_textures(export_config)

        # In case of error, display a human readable message:
        if export_result.status != substance_painter.export.ExportStatus.Success:
            print(export_result.message)

        # Display the details of what was exported:
        for k,v in export_result.textures.items():
            print("Stack {0}:".format(k))
            for exported in v:
                print(exported)

    See also:
        :mod:`substance_painter.project`,
        :mod:`substance_painter.resource`,
        `Export documentation`_.

    .. _Export documentation:
        https://www.adobe.com/go/painter-export
    '''
def get_default_export_path() -> str:
    """
    Get the application default export path used for exporting textures.
    This path does not depend on the project and is the default value used when
    creating a new project.

    Returns:
        str: The default export path of the application.
    """

@dataclasses.dataclass(frozen=True)
class PredefinedExportPreset:
    '''
    An export preset (output template) controls the behavior of the export process.
    A predefined preset has a dynamic list of maps exported depending on the project and can have
    pre/post processes that generates custom data (e.g. glTF).
    This type of export preset is embedded in the application and cannot be edited.

    Example:
    ::

        import substance_painter.export
        import substance_painter.project
        import substance_painter.textureset

        # A project needs to be opened to introspect the output maps of a predefined export preset
        substance_painter.project.open("C:/projects/MeetMat.spp")

        # Retrieve all predefined export presets
        predefined_presets = substance_painter.export.list_predefined_export_presets()

        # Retrieve data of the first preset
        predefined_preset = predefined_presets[0]
        print("Name: " + predefined_preset.name + ", url: " + predefined_preset.url)
        stack = substance_painter.textureset.get_active_stack()
        print(predefined_preset.list_output_maps(stack))

    :param name: The name of the preset.
    :param url: The URL of the preset.

    See also:
        `Predefined presets documentation`_.

    .. _Predefined presets documentation:
        https://helpx.adobe.com/substance-3d-painter/getting-started/export/export-presets/predefined-presets.html
    '''
    name: str
    url: str
    def list_output_maps(self, stack: substance_painter.textureset.Stack) -> list:
        """
        Get the list of output maps based on the channels available on the given stack. The output
        maps have the same format as the ``maps`` list in the JSON configuration.

        Args:
            stack (substance_painter.textureset.Stack): The stack to get the output maps from.

        Returns:
            dict:
                The list of output maps on the channels available on the given stack. The output
                maps have the same format as the ``maps`` list in the JSON configuration.
                See `JSON configuration <#full-json-config-dict-possibilities>`_.

        Raises:
            ProjectError: If no project is opened.
            ValueError: If the given stack is invalid.

        See also:
            :mod:`substance_painter.textureset`
        """

def list_predefined_export_presets() -> list[PredefinedExportPreset]:
    """
    Get the list of predefined export presets (output templates).

    Returns:
        List[PredefinedExportPreset]: The list of predefined export presets.

    See also:
        Example in :class:`PredefinedExportPreset`
    """

@dataclasses.dataclass(frozen=True)
class ResourceExportPreset:
    '''
    An export preset (output template) controls the behavior of the export process.
    A shelf export preset is a resource with the ``Export``
    :class:`substance_painter.resource.Type`. It can be modified by the user via the UI.

    Example:
    ::

        import substance_painter.export
        import substance_painter.project

        substance_painter.project.open("C:/projects/MeetMat.spp")

        # Retrieve all resource export presets
        resource_presets = substance_painter.export.list_resource_export_presets()

        # Retrieve PBR Metalllic Roughness export preset
        preset = ""
        match = "PBR Metallic Roughness"
        for resource_preset in resource_presets :
            if resource_preset.resource_id.name == "PBR Metallic Roughness":
                print("Name: {}, url: {}".format(
                    resource_preset.resource_id.name,
                    resource_preset.resource_id.url()))
                preset = resource_preset
                break

        maps = preset.list_output_maps()
        # Add new output map 2D View
        maps.append({
            \'channels\': [{
                \'destChannel\': \'R\',
                \'srcChannel\': \'R\',
                \'srcMapName\': \'View_2D\',
                \'srcMapType\': \'virtualMap\',
                \'srcPath\': \'\'
            }, {
                \'destChannel\': \'G\',
                \'srcChannel\': \'G\',
                \'srcMapName\': \'View_2D\',
                \'srcMapType\': \'virtualMap\',
                \'srcPath\': \'\'
            }, {
                \'destChannel\': \'B\',
                \'srcChannel\': \'B\',
                \'srcMapName\': \'View_2D\',
                \'srcMapType\': \'virtualMap\',
                \'srcPath\': \'\'
            }, {
                \'destChannel\': \'A\',
                \'srcChannel\': \'A\',
                \'srcMapName\': \'View_2D\',
                \'srcMapType\': \'virtualMap\',
                \'srcPath\': \'\'
            }],
            \'fileName\':
            \'$mesh_$textureSet_2D_View\',
            \'parameters\': {
                \'bitDepth\': \'8\',
                \'dithering\': False,
                \'fileFormat\': \'png\'
            }
        })

        # Create a new preset
        newPresetName = "PBR Metallic Roughness 2D View"
        newPreset = {
            "name": newPresetName,
            "maps": maps
        }
        # Use the preset in the export configuration
        export_config = {
            "exportShaderParams": False,
            "exportPath": "C:/export",
            "defaultExportPreset" : newPresetName,
            "exportPresets": [newPreset],
            "exportList": [
                {
                    "rootPath": "01_Head"
                },
                {
                    "rootPath": "02_Body"
                },
                {
                    "rootPath": "03_Base"
                }],
            "exportParameters": [
                {
                    "parameters": {
                        "dithering": True,
                        "paddingAlgorithm": "infinite"
                    }
                }]
            }

        substance_painter.export.export_project_textures(export_config)

    :param resource_id: The resource ID of the export preset.

    See also:
        :mod:`substance_painter.resource`,
        `Creating export presets`_.

    .. _Creating export presets:
        https://helpx.adobe.com/substance-3d-painter/getting-started/export/creating-export-presets.html
    '''
    resource_id: substance_painter.resource.ResourceID
    def list_output_maps(self) -> list:
        """
        Get the list of output maps for the given preset. The output maps have the same format as
        the ``maps`` list in the JSON configuration.

        Returns:
            dict:
                The list of output maps for the given preset. The output maps have the same format
                as the ``maps`` list in the JSON configuration.
                See `JSON configuration <#full-json-config-dict-possibilities>`_.

        Raises:
            ValueError: If the given preset is invalid.
        """

def list_resource_export_presets() -> list[ResourceExportPreset]:
    """
    Get the list of export presets (output templates). This list contains all export presets
    available in the shelves (presets provided by default and custom ones if any).

    Returns:
        List[ResourceExportPreset]: The list of export presets.

    See also:
        Example in :class:`ResourceExportPreset`
    """

from _substance_painter.export import MeshExportOption as MeshExportOption

def scene_is_triangulated() -> bool:
    """
    Check if the scene has only triangles (polygons with only 3 sides).

    Returns:
        bool: True if the current scene has only triangles, False otherwise.

    Raises:
        ProjectError: If no project is opened.
    """
def scene_has_tessellation() -> bool:
    """
    Check if the scene has displacement/tessellation enabled.

    Returns:
        bool: True if the current scene has displacement/tessellation, False otherwise.

    Raises:
        ProjectError: If no project is opened.
    """

@dataclasses.dataclass(frozen=True)
class MeshExportResult:
    """
    Result of the export mesh process

    :param status: Status code.
    :param message: Human readable status message.
    """
    status: ExportStatus
    message: str

def export_mesh(file_path: str, option: MeshExportOption) -> MeshExportResult:
    '''
    Export the current mesh to the given file path.

    Args:
        file_path (string): The complete file path where to export the mesh. The file format is
            deduced from the extension.
            Supported extensions are: ``.usd``, ``.obj``, ``.fbx``, ``.dae``, ``.ply``, ``.gltf``.
        option (MeshExportOption): The export option to use.

    Returns:
        MeshExportResult: Result of the export process.

    Raises:
        ProjectError: If no project is opened.
        ValueError: If ``file_path`` or ``option`` are invalid in the context
            of the current project. Contains a human readable message detailing
            the problem.

    Example:
    ::

        import substance_painter.export

        # Open a project we want to export from (see substance_painter.project
        # for details). This step is not necessary if there is already a project
        # opened in Substance 3D Painter.
        import substance_painter.project
        substance_painter.project.open("C:/projects/MeetMat.spp")

        # Choose an export option to use
        export_option = substance_painter.export.MeshExportOption.BaseMesh
        if not substance_painter.export.scene_is_triangulated():
            export_option = substance_painter.export.MeshExportOption.TriangulatedMesh
        if substance_painter.export.scene_has_tessellation():
            export_option = substance_painter.export.MeshExportOption.TessellationNormalsBaseMesh

        # Actual export mesh operation:
        filename = "C:/projects/MeetMat.obj"
        export_result = substance_painter.export.export_mesh(filename, export_option)

        # In case of error, display a human readable message:
        if export_result.status != substance_painter.export.ExportStatus.Success:
            print(export_result.message)

    See also:
        :mod:`substance_painter.project`,
        `Export documentation`_.

    .. _Export documentation:
        https://www.adobe.com/go/painter-export
    '''
