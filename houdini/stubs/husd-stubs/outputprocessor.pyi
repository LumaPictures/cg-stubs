import hou
from collections.abc import Mapping, Sequence
from pxr import Sdf as Sdf

from typing import TypeAlias
from typing import TypeAlias
_OptionValue: TypeAlias = int | float | str | tuple[int, ...] | tuple[float, ...] | tuple[str, ...]
class OutputProcessor:
    """ Processes outputs (layers and additional files like texture maps and
        volume files) that are referenced by a USD layer. This processing
        happens as the USD layer is being saved to disk by a USD ROP.

        Any output processor method can raise an exception which will stop the
        USD save process, and raise an error on the ROP node. The `beginSave`
        and `endSave` methods of every output processor enabled on the ROP
        node will always be called even if there have been errors during the
        save, and even if exceptions are raised in one or more of the
        `beginSave` method calls.
    """
    config_node: hou.OpNode | None
    lop_node: hou.LopNode | None
    t: float | None
    stage_variables: dict[str, _OptionValue] | None
    SHOULD_SAVE_FALSE: int
    SHOULD_SAVE_TRUE: int
    SHOULD_SAVE_NO_OPINION: int
    def __init__(self) -> None:
        """
        Each time a USD or USD Render ROP operation is initiated, a new
        instance of each output processor to be used in the operation is
        created. When the operation completes (this means all frames have
        been written to disk or rendered), the output processor objects are
        destroyed. This allows an output processor to have global start and
        end operations.
        """
    def __del__(self) -> None:
        """
        Called at the end of a USD or USD Render ROP operation.
        """
    @staticmethod
    def hidden() -> bool:
        """
        If this method returns `True`, this processor is not included in the
        list of output processors shown to the user. The default
        implementation always returns `False`.
        """
    @staticmethod
    def name() -> str:
        """
        The name (token) this output processor is known as.
        """
    @staticmethod
    def displayName() -> str:
        """
        Returns a label to describe the processor, in the list of output
        processors shown to the user. This should be in a form like
        `Save Paths Relative to Output Path`.
        """
    @staticmethod
    def parameters() -> str:
        '''
        Returns a string containing Houdini dialog script describing the
        parameters this processor shows to the user for configuration. You can
        generate the dialog script by building up a `hou.ParmTemplateGroup`
        with `hou.ParmTemplate` objects inside, and then returning the value
        from `hou.ParmTemplateGroup.asDialogScript()`::

            group = hou.ParmTemplateGroup()
            group.append(hou.StringParmTemplate(
                "texturedir",
                "Texture Directory",
                string_type=hou.stringParmType.FileReference
            ))
            return group.asDialogScript()

        The default implementation returns the script for an empty parameter
        group, so if your processor doesn\'t need any parameters, you don\'t need
        to override this method.

        The internal names of any parameters you create here must be unique
        among all other parameters on the render node, so you probably want to
        use a naming scheme like `<modulename>_<parmname>`.
        '''
    def stageVariables(self) -> dict[str, _OptionValue] | None:
        """
        Return the dictionary of stage variables set on the LOP node stage
        being saved to disk.
        """
    def beginSave(self, config_node: hou.OpNode, config_overrides: Mapping[str, _OptionValue] | None, lop_node: hou.LopNode, t: float, stage_variables: dict[str, _OptionValue]) -> None:
        '''
        Called when a node using this processor starts to write out files.
        This gives you the chance to read parameter values (either the
        configuration parameters added by `parameters()`, or the node\'s own
        parameters, depending on what information you need). If the ROP is
        operating with "Flush data after each frame" turned on, this method
        is called before each frame of data is written to disk.

        :param config_node: A `hou.Node` object representing the node.
        :param config_overrides: A `dict` of values that should be used to
            override whatever may be set on the node. See `evalConfig()`.
        :param: lop_node: A [Hom:hou.LopNode] object representing the LOP node
            that generated the stage being saved.
        :param t: A floating point value representing the time (in seconds)
            along the timeline which the node is rendering. If you read
            parameter values from the node, you should use `Parm.evalAtTime(t)`
            in case the parameter is animated.
        :param: stage_variables: A `dict` containing the stage variables set
            on the root layer of the stage being written to disk. This
            parameter should be passed to the base class implementation of
            this method so this dictionary can be accessed from the
            `processReferencePath` and `processReferenceExpression` methods
            through the `stageVariables` method.
        '''
    def endSave(self, config_node: hou.OpNode, config_overrides: Mapping[str, _OptionValue] | None, lop_node: hou.LopNode, t: float, stage_variables: dict[str, _OptionValue], saved_paths: Sequence[str], error_messages: str) -> None:
        '''
        Called when a node using this processor starts to write out files.
        This gives you the chance to read parameter values (either the
        configuration parameters added by `parameters()`, or the node\'s own
        parameters, depending on what information you need). If the ROP is
        operating with "Flush data after each frame" turned on, this method
        is called after each frame of data is written to disk.

        :param config_node: A `hou.Node` object representing the node.
        :param config_overrides: A `dict` of values that should be used to
            override whatever may be set on the node. See `evalConfig()`.
        :param: lop_node: A [Hom:hou.LopNode] object representing the LOP node
            that generated the stage being saved.
        :param t: A floating point value representing the time (in seconds)
            along the timeline which the node is rendering. If you read
            parameter values from the node, you should use `Parm.evalAtTime(t)`
            in case the parameter is animated.
        :param: stage_variables: A `dict` containing the stage variables set
            on the root layer of the stage being written to disk. This
            parameter should be passed to the base class implementation of
            this method so this dictionary can be accessed from the
            `processReferencePath` and `processReferenceExpression` methods
            through the `stageVariables` method.
        :param: saved_paths: A `tuple` of `str` objects containing the final
            full paths to all files written to disk during the current save
            operation.
        :param: error_messages: A string containing any error message generated
            by the save process so far.
        '''
    def processSavePath(self, asset_path: str, referencing_layer_path: str, asset_is_layer: bool) -> str:
        """
        Called when the render node needs to determine where on disk to save
        an asset. The `asset_path` is the file path as Houdini knows it
        (for example, from USD metadata or a Houdini parameter).

        If you return a value from this method, it should be an absolute path
        to the location on disk where the asset should be saved.

        (If you return a relative path from this method, it will be relative to
        the current directory (`os.getcwd()`) which is probably not what you
        want.)

        :param asset_path: The path to the asset, as specified in Houdini.
            This string comes with expressions and environment variables (such
            as `$HIP`) expanded already, so if you want to compare to another
            path, you should also expand that path (for example, with
            `os.path.expandvars()` or `hou.text.expandString()`).
        :param referencing_layer_path: The absolute file path of the file
            containing the reference to the asset. This value will be set for
            all USD layers except the root layer, and for all non-layer assets
            such as a volume file. You can use this to create a save path that
            is in a particular location relative to the referencing file.
        :param asset_is_layer: A boolean value indicating whether this asset is
            a USD layer file. If this is `False`, the asset is something else
            (for example, a texture or volume file).
        """
    def processReferencePath(self, asset_path: str, referencing_layer_path: str, asset_is_layer: bool) -> str:
        '''
        Called when the render node needs to write a file path pointing to an
        asset (to sublayer or reference into the file, or pointing to external
        data files such as texture maps).

        For example, if the render node is writing out `A.usd` and `B.usd`,
        where `A` references in `B`:

        1. It will first call `processSavePath()` to compute where to save
           `B.usd`. Say it calls `processSavePath("B.usd", True)`, and that
           method returns "/Users/aisha/project/usd/B.usd".

        2. As it writes out `A.usd`, when it gets to the part where it refers
           to `B.usd`, it will call this method to compute the file path
           string to use to refer to the asset in the file being written.
           `processReferencePath("/Users/aisha/project/usd/B.usd",
           "/Users/aisha/project/usd/A.usd", True)`. To make the file path
           relative, you could return the result of
           `hou.text.relpath(asset_path, referencing_layer_path)`

        :param asset_path: The path to the asset, as specified in Houdini.
            If this asset is being written to disk, this will be the final
            output of the `processSavePath()` calls on all output
            processors.
        :param referencing_layer_path: The absolute file path of the file
            containing the reference to the asset. You can use this to make
            the path pointer relative.
        :param asset_is_layer: A boolean value indicating whether this asset is
            a USD layer file. If this is `False`, the asset is something else
            (for example, a texture or volume file).
        '''
    def processReferenceExpression(self, asset_expression: str, referencing_layer_path: str, asset_is_layer: bool) -> str:
        """
        Called when the render node needs to write a stage variable expression
        pointing to an asset (to sublayer or reference into the file, or
        pointing to external data files such as texture maps). This method is
        used the same way as processReferencePath, but called if the asset is
        specified using a stage variable expression rather than a plain asset
        path value.

        :param asset_expression: The expression to calculate the path to the
            asset, as specified in Houdini. The output can either be a stage
            variable expression or an explicit asset path (both expressed as
            strings).
        :param referencing_layer_path: The absolute file path of the file
            containing the reference to the asset. You can use this to make
            the path pointer relative.
        :param asset_is_layer: A boolean value indicating whether this asset is
            a USD layer file. If this is `False`, the asset is something else
            (for example, a texture or volume file).
        """
    def processLayer(self, layer: Sdf.Layer, layersavepath: str | None = None) -> bool:
        '''
        Called right before the render node writes a layer to disk. Provides
        an opportunity to make arbitrary modifications to the layer. This
        method is only called once per layer, even if "Flush data after each
        frame" is turned on. It is called before writing the first frame of
        data to the new layer.

        :param layer: The Sdf.Layer object that is going to be written to
            disk.
        :param layersavepath: A string indicating where the layer will be
            written, after passing it through the USD asset resolver.
        :return: True if the layer was modified, otherwise False.
        '''
    def shouldSave(self, save_path: str, layer: Sdf.Layer | None) -> int:
        '''
        Called right before the render node writes a file to disk. Provides
        an opportunity to prevent the saving of the file.

        :param save_path: The path on disk to which the file will be written.
        :param layer: The Sdf.Layer object that is going to be written to disk.
            May be None if the file being written is no a USD layer.
        :return: `self.SHOULD_NOT_SAVE` will not write the file to disk.
            `self.SHOULD_SAVE` to write the file to disk.
            `self.NO_OPINION` to express no opinion either way.
            The last output processor to return `self.SHOULD_SAVE` or
            `self.SHOULD_NOT_SAVE` dictates whether the file should be saved
            to disk. If all output processors return `self.NO_OPINION`, the
            file will be written to disk if permitted by the ROP
            "Files to Save" parameter.
        '''
    def evalConfig(self, parm_name: str, config_node: hou.OpNode | None, config_overrides: Mapping[str, _OptionValue] | None, t: float) -> _OptionValue | dict[str, str] | hou.Ramp | hou.Geometry | None:
        """
        Helper function to retrieve a parameter from either the Houdini node
        running this translator, or an overrides dictionary. Note that the
        overrides takes precedence.
        
        This method should only be called from `beginSave()`.
        
        :param parm_name: The name of the parameter to evaluate. 
        :param config_node: A `hou.Node` to query for the parameter. 
        :param config_overrides: A `dict` of overrides that take precedence
            over parameter values from the node.
        :param t: The time to use for evaluation.
        :return: The retrieved parameter's  value, or `None` if the parameter
            could not be found/evaluated in either the node or overrides.
        """
