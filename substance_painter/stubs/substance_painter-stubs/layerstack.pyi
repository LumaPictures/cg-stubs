import dataclasses
import substance_painter
import substance_painter.resource
import types
from .colormanagement import Color as Color
from _typeshed import Incomplete
from enum import Enum
from substance_painter import levels as levels
from substance_painter._utility import ReadOnlyUid as ReadOnlyUid
from substance_painter.levels import LevelsParams as LevelsParams
from substance_painter.source import ActiveChannelsMixin as ActiveChannelsMixin, SourceEditorMixin as SourceEditorMixin, SourceSubstance as SourceSubstance
from substance_painter.textureset import ChannelType as ChannelType, Stack as Stack, TextureSet as TextureSet, UVTile as UVTile

from _substance_painter.layerstack import BlendingMode as BlendingMode
from _substance_painter.layerstack import NodeType as NodeType

class NodeStack(Enum):
    """
    Indicate which node stack you want to insert in.

    Members:

    ================= ===========================
    Name              Description
    ================= ===========================
    ``Substack``      Insert in the substack of a node (only valid for a Folder node).
    ``Content``       Insert in the content stack of the node.
    ``Mask``          Insert in the mask stack of the node.
    ================= ===========================
    """
    Substack = ...
    Content = ...
    Mask = ...

from _substance_painter.layerstack import MaskBackground as MaskBackground
from _substance_painter.layerstack import ColorSelectionBackgroundColor as ColorSelectionBackgroundColor
from _substance_painter.layerstack import GeometryMaskType as GeometryMaskType
from _substance_painter.layerstack import ProjectionMode as ProjectionMode

def is_3d_projection_mode(projection_mode: ProjectionMode) -> bool:
    """
    Check if the projection mode is a 3D projection.

    :param projection_mode: Projection mode to check.
    :returns: True if the current projection mode is a 3D projection.
    """

from _substance_painter.layerstack import FilteringMode as FilteringMode
from _substance_painter.layerstack import UVWrapMode as UVWrapMode
from _substance_painter.layerstack import ShapeCropMode as ShapeCropMode
from _substance_painter.layerstack import ScaleMode as ScaleMode
from _substance_painter.layerstack import CompareMaskEffectOperand as CompareMaskEffectOperand
from _substance_painter.layerstack import CompareMaskEffectOperation as CompareMaskEffectOperation
from _substance_painter.layerstack import SelectionType as SelectionType
from _substance_painter.layerstack import SymmetryAxis as SymmetryAxis  # type: ignore[attr-defined]
from _substance_painter.layerstack import SymmetryMode as SymmetryMode  # type: ignore[attr-defined]

class ScopedModification:
    '''
    :class:`ScopedModification` can be used to group many layerstack modification calls
    in a single undoable command.

    `name` will be displayed in the software history.

    This object is usefull to:
       * Avoid poluting the history by grouping logically layerstack
         modifications behind a unique name.
       * The computation will only happen when we leave the ``with`` statement
         meaning that we don\'t waste time computing intermedietary result that we
         don\'t need.

    This object is a context manager usable with the python ``with`` statement

    Example:
        .. code-block:: python

            import substance_painter as sp

            def insert_many_fills():
                # Insert many layers inside the current texture set layer stack
                # and set their projection mode to tri-planar
                insert_position = sp.layerstack.InsertPosition.from_textureset_stack(
                    sp.textureset.get_active_stack())
                fill = sp.layerstack.insert_fill(insert_position)
                fill.set_projection_mode(sp.layerstack.ProjectionMode.Triplanar)
                fill = sp.layerstack.insert_fill(insert_position)
                fill.set_projection_mode(sp.layerstack.ProjectionMode.Triplanar)
                fill = sp.layerstack.insert_fill(insert_position)
                fill.set_projection_mode(sp.layerstack.ProjectionMode.Triplanar)

            # Calling this method will generate many history entries (1 for each
            # inserted fill and 1 for each projection mode update) and
            # Substance Painter will compute the textures each time a modification
            # happens.
            #
            # Expected history:
            #   * Add fill
            #   * Update projection mode
            #   * Add fill
            #   * Update projection mode
            #   * Add fill
            #   * Update projection mode
            #
            # Potential texture update in the viewport: 6 (one for each modification)
            insert_many_fills()

            # With the ScopedModification below, only one entry will be added to Painter
            # history. A single undo will remove all the fill inserted inside the

            # Calling this method inside a ScopedModification will only generate one history
            # entry and Substance Painter will compute the textures only once.
            #
            # Expected history:
            #   * Insert many layers
            #
            # Potential texture update in the viewport: 1
            with sp.layerstack.ScopedModification("Insert many layers"):
                insert_many_fills()

    '''
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_traceback: types.TracebackType | None) -> None: ...

class FillParamsEditorMixin:
    """
    A mixin allowing manipulation of this fill parameters.

    :meta private:
    """
    def get_projection_mode(self) -> ProjectionMode:
        """
        Get the current projection mode.

        :returns: The current projection mode.
        """
    def set_projection_mode(self, projection_mode: ProjectionMode):
        """
        Switch to a new projection mode.

        :param projection_mode: The new projection mode.
        :raises ValueError: If the projection mode is not supported in the current context.
        """
    def get_projection_parameters(self) -> ProjectionParams | None:
        """
        Get the current projection parameters.
        Each kind of Projection Mode returns a specific kind of ProjectionParams, supporting a
        different set of features.
        `Fill` mode support no parameters, and returns None.

        :returns: The current projection parameters, or None for `Fill`.

        See also:
            :meth:`get_projection_mode`,
            `Fill projections documentation`_
        """
    def set_projection_parameters(self, projection_parameters: ProjectionParams):
        """
        Set projection parameters and update the current projection mode accordingly.

        :param projection_parameters: The new parameters to apply.
        :raises ValueError: If the projection parameters are not supported in the current context.

        See also:
            :meth:`get_projection_parameters`,
            `Fill projections documentation`_
        """
    def is_symmetry_enabled(self) -> bool:
        """
        Check if symmetry is enabled.
        Symmetry is only available for 3D projection modes. See
        :func:`substance_painter.layerstack.is_3d_projection_mode`.

        :raises ValueError: If the symmetry is not supported in the current context.
        :returns: True if symmetry is enabled, False otherwise.
        """
    def set_symmetry_enabled(self, enabled: bool):
        """
        Set the symmetry enabled state.
        Symmetry is only available for 3D projection modes. See
        :func:`substance_painter.layerstack.is_3d_projection_mode`.

        :param enabled: True to enable symmetry, False to disable it.
        :raises ValueError: If the symmetry is not supported in the current context.
        """
    def get_symmetry_parameters(self) -> SymmetryParams:
        """
        Get the current symmetry parameters.
        Each kind of symmetry mode returns a specific kind of SymmetryParams, supporting a
        different set of features.
        Symmetry is only available for 3D projection modes. See
        :func:`substance_painter.layerstack.is_3d_projection_mode`.

        :raises ValueError: If the symmetry is not supported in the current context.
        :returns: The current symmetry parameters.
        """
    def set_symmetry_parameters(self, symmetry_parameters: SymmetryParams):
        """
        Set the symmetry parameters and update the current symmetry mode accordingly.
        This does not enable symmetry. Explicitely use :meth:`set_symmetry_enabled` to enable it.
        Symmetry is only available for 3D projection modes. See
        :func:`substance_painter.layerstack.is_3d_projection_mode`.

        Example to set and enable radial symmetry::

            symmetry_parameters = sp.layerstack.RadialSymmetryParams()
            symmetry_parameters.axis = sp.layerstack.SymmetryAxis.X
            symmetry_parameters.flip_u = False
            symmetry_parameters.flip_v = True
            symmetry_parameters.axis_position = [0, 0.1, -0.1]
            symmetry_parameters.angle_span = 70
            symmetry_parameters.count = 10
            my_layer.set_symmetry_parameters(symmetry_parameters)
            my_layer.set_symmetry_enabled(True)

        :param symmetry_parameters: The new parameters to apply.
        :raises ValueError: If the symmetry is not supported in the current context.
        """

class Node(ReadOnlyUid):
    """
    Abstract class to manipulate common properties of a layer stack node.
    Each node is identified by a node uid.

    Calling methods of a Node with an incorrect `uid` throws a ValueError.
    This could happen when instanciating a Node providing its `uid` by hand, or when the Node no
    longer refers to existing data in the Layer Stack.

    See also:
        :func:`substance_painter.layerstack.get_node_by_uid`,
        :ref:`layerstack_edition_insertion` section.
    """
    def __eq__(self, other): ...
    def __hash__(self): ...
    def get_type(self) -> NodeType:
        """
        Check the type of the node.

        :returns: The node type.
        """
    def get_texture_set(self) -> TextureSet:
        """
        Get the TextureSet this node belongs to.

        :returns: the TextureSet this node belongs to.
        """
    def is_visible(self) -> bool:
        """
        Check whether this node is rendered.

        :returns: Whether this node is rendered.
        """
    def set_visible(self, visible: bool):
        """
        Enable this node for rendering.

        :param visible: Whether to enable this node for rendering.
        """
    def get_name(self) -> str:
        """
        Get the name assigned to this Node.

        :returns: The Node name.
        """
    def set_name(self, name: str):
        """
        Change this node name.

        :param name: New name to use.
        """
    def is_in_mask_stack(self) -> bool:
        """
        Check whether this node is part of a mask stack.

        :returns: Whether this node is part of a mask stack.
        """
    def has_blending(self) -> bool:
        """
        Check whether this node supports blending information (blending mode + opacity).
        The blending might be per Channel Type for regular nodes, or monochannel for nodes
        inside a mask stack.

        :returns: Whether this node supports blending information.

        See also:
            :meth:`is_in_mask_stack`,
            `Blending modes documentation`_
        """
    def get_blending_mode(self, channel: ChannelType | None = None) -> BlendingMode:
        """
        Get the blending mode for a Node.
        If the node is not in a mask stack, a Channel Type must be provided.
        If the node is in a mask stack, Channel Type must be None.

        :param channel: Channel Type to query or None for mask nodes.
        :raises ValueError: If the node has blending information per Channel Type and no Channel
                Type is provided, or if the node has blending information without Channel Type and
                a Channel Type is provided.
        :returns: The blending mode of this node for the given Channel Type or for the mask.

        See also:
            :meth:`is_in_mask_stack`,
            :meth:`has_blending`,
            `Blending modes documentation`_
        """
    def set_blending_mode(self, blending_mode: BlendingMode, channel: ChannelType | None = None):
        """
        Set the blending mode for a Node.
        If the node is not in a mask stack, a Channel Type must be provided.
        If the node is in a mask stack, Channel Type must be None.

        :param blending_mode: New blending mode to apply.
        :param channel: Channel type to update or None for mask nodes.
        :raises ValueError: If the node has blending information per Channel Type and no Channel
                Type is provided, or if the node has blending information without Channel Type and
                a Channel Type is provided.

        See also:
            :meth:`is_in_mask_stack`,
            :meth:`has_blending`,
            `Blending modes documentation`_
        """
    def get_opacity(self, channel: ChannelType | None = None) -> float:
        """
        Get the opacity for a Node.
        If the node is not in a mask stack, a Channel Type must be provided.
        If the node is in a mask stack, Channel Type must be None.

        :param channel: Channel Type to query or None for mask nodes.
        :raises ValueError: If the node has blending information per Channel Type and no Channel
                Type is provided, or if the node has blending information without Channel Type and
                a Channel Type is provided.
        :returns: The opacity of this node for the given Channel Type or for the mask.

        See also:
            :meth:`is_in_mask_stack`
            :meth:`has_blending`
        """
    def set_opacity(self, opacity: float, channel: ChannelType | None = None):
        """
        Set the opacity for a node.
        If the node is not in a mask stack, a Channel Type must be provided.
        If the node is in a mask stack, Channel Type must be None.

        :param opacity: New opacity to apply, value between 0.0 and 1.0.
        :param channel: Channel Type to update or None for mask nodes.
        :raises ValueError: If the node has blending information per Channel Type and no Channel
                Type is provided, or if the node has blending information without Channel Type and
                a Channel Type is provided.

        See also:
            :meth:`is_in_mask_stack`
            :meth:`has_blending`
        """
    def get_stack(self) -> Stack:
        """
        Get the stack that contains this node.

        :returns: The stack that contains this node.
        """
    def get_parent(self) -> Node:
        """
        Get the parent of this node.

        :returns: The parent of this node, or None if this node is a root layer.
        """
    def get_next_sibling(self) -> Node:
        """
        Get the next sibling of this node.

        :returns: The next sibling of this node, or None if this node is the first sibling.
        """
    def get_previous_sibling(self) -> Node:
        """
        Get the previous sibling of this node.

        :returns: The previous sibling of this node, or None if this node is the last sibling.
        """

class LayerNode(Node):
    """
    A Node that is part of the main hierarchy. Every Layer such as a paint or fill layer, as well as
    groups, are organized into this hierarchy.
    As such, you can query sub layers (in the case the LayerNode is a group), but also associate
    content effects and mask effects (such as levels and filters and so on).

    See also:
        :func:`substance_painter.layerstack.get_node_by_uid`,
        :ref:`layerstack_edition_insertion` section.
    """
    def content_effects(self) -> list[EffectNode]:
        """
        Query the content effects of this node, ordered like in the layer stack.

        :returns: The content effects of this node.
        """
    def mask_effects(self) -> list[EffectNode]:
        """
        Query the mask effects of this node, ordered like in the layer stack.

        :returns: The mask effects of this node.
        """
    def instances(self) -> list[LayerNode]:
        """
        Return the list of instances of this layer.
        See the documentation on layer instancing if you are not familiar with the
        concept: `Layer instancing documentation`_.

        .. _Layer instancing documentation:
            https://helpx.adobe.com/substance-3d-painter/interface/layer-stack/layer-instancing.html

        :returns: The instances of this node.
        """
    def get_geometry_mask_type(self) -> GeometryMaskType:
        """
        Query the geometry mask type currently applied to this node.

        :returns: The type of geometry mask for this layer node.

        See also:
            `Geometry mask documentation`_

        .. _Geometry mask documentation:
            https://helpx.adobe.com/substance-3d-painter/interface/layer-stack/geometry-mask.html

        """
    def set_geometry_mask_type(self, geometry_mask_type: GeometryMaskType):
        """
        Set the geometry mask type to apply to this node.
        :class:`GeometryMaskType.UVTile <GeometryMaskType>` is only
        supported when the corresponding Texture Set uses UV Tiles.

        :param geometry_mask_type: The type of geometry mask for this layer node.
        :raises ValueError: When GeometryMaskType.UVTile is requested and the project does not
                support UV Tiles.

        See also:
            :meth:`substance_painter.textureset.TextureSet.has_uv_tiles`,
            `Geometry mask documentation`_

        """
    def get_geometry_mask_enabled_meshes(self) -> list[str]:
        """
        Get the list of enabled meshes for the geometry mask. Meshes that are not in this list are
        disabled.
        To get the complete list of meshes, see
        :meth:`substance_painter.textureset.TextureSet.all_mesh_names`.

        :returns: The list of enabled meshes for the geometry mask.

        See also:
            `Geometry mask documentation`_
        """
    def set_geometry_mask_enabled_meshes(self, mesh_names: list[str]):
        """
        Set the list of enabled meshes for the geometry mask. Meshes that are not in this list will
        be disabled. To get the complete list of meshes, see
        :meth:`substance_painter.textureset.TextureSet.all_mesh_names`.

        :param mesh_names: The list of meshes to enable for the geometry mask.
        :raises ValueError: If a mesh name does not belongs to this texture set.

        See also:
            `Geometry mask documentation`_
        """
    def get_geometry_mask_enabled_uv_tiles(self) -> list[UVTile]:
        """
        Get the list of enabled UV Tiles for the geometry mask. UV Tiles that are not in this list
        are disabled. To get the complete list of UV Tiles, see
        :meth:`substance_painter.textureset.TextureSet.all_uv_tiles`.

        :returns: The list of enabled UV Tiles for the geometry mask.

        See also:
            `Geometry mask documentation`_
        """
    def set_geometry_mask_enabled_uv_tiles(self, uv_tiles: list[UVTile]):
        """
        Set the list of enabled UV Tiles for the geometry mask. UV Tiles that are not in this list
        will de disabled. To get the complete list of UV Tiles, see
        :meth:`substance_painter.textureset.TextureSet.all_uv_tiles`.

        :param uv_tiles: The list of UV Tiles to enable for the geometry mask.
        :raises ValueError: If a UV Tile does not belong to this texture set.

        See also:
            `Geometry mask documentation`_
        """
    def has_mask(self) -> bool:
        """
        Check whether this node has a mask.

        :returns: Whether this node has a mask.
        """
    def add_mask(self, background: MaskBackground):
        """
        Add a mask on this node with the specified background.

        :raises ValueError: If a mask is already set on this node.
                Use :meth:`has_mask` to check if the node has a mask.
        """
    def remove_mask(self) -> None:
        """
        Remove this node mask, including all its effects.

        :raises ValueError: If no mask exists on this node.
                Use :meth:`has_mask` to check if the node has a mask.
        """
    def get_mask_background(self) -> MaskBackground:
        """
        Query the type of mask used by this node.

        :raises ValueError: If no mask exists on this node.
                Use :meth:`has_mask` to check if the node has a mask.
        :returns: The mask background applied to this node.
        """
    def set_mask_background(self, background: MaskBackground):
        """
        Set the mask background on this node.

        :param background: The mask background to be applied on this node mask.
        :raises ValueError: If no mask exists on this node.
                Use :meth:`has_mask` to check if the node has a mask.
        """
    def is_mask_enabled(self) -> bool:
        """
        Query whether the mask is currently enabled.

        :raises ValueError: If no mask exists on this node.
                Use :meth:`has_mask` to check if the node has a mask.
        :returns: Whether the mask is currently enabled.
        """
    def enable_mask(self, enabled: bool):
        """
        Set whether the mask is currently enabled.

        :param enabled: Whether to enable the mask.
        :raises ValueError: If no mask exists on this node.
                Use :meth:`has_mask` to check if the node has a mask.
        """

class GroupLayerNode(LayerNode):
    """
    A node allowing manipulation of a Group layer of the Layer Stack.
    """
    def sub_layers(self) -> list[LayerNode]:
        """
        Query sub layers of this node. Only get the direct children, ordered like in the layer
        stack.

        :returns: The sub layers of this node.
        """
    def is_collapsed(self) -> bool:
        """
        Query if the group is in collapsed state.

        :returns: Whether this group is collapsed.
        """
    def set_collapsed(self, collapsed: bool):
        """
        Set the collapsed state of the group.

        :param collapsed: Whether to collapse the group.
        """

class PaintLayerNode(LayerNode):
    """
    A node allowing manipulation of a Paint layer.

    Note:
        Strokes are not accessible from the Python API.
    """

class InstanceLayerNode(LayerNode):
    """
    A node allowing manipulation of an Instance layer.

    To retrieve the list of :class:`InstanceLayerNode` from the source layer,
    see :meth:`LayerNode.instances`
    """
    def instance_source(self) -> LayerNode:
        """
        Return the source layer of this instance.

        :returns: The source layer if this instance.
        """

class FillLayerNode(FillParamsEditorMixin, SourceEditorMixin, LayerNode):
    """
    A node allowing manipulation of a Fill layer.
    """
HierarchicalNode = LayerNode | GroupLayerNode | PaintLayerNode | InstanceLayerNode | FillLayerNode

class GeneratorEffectNode(ActiveChannelsMixin, Node):
    """
    A node allowing manipulation of a Generator effect.
    """
    def get_source(self) -> SourceSubstance:
        """
        Get the source procedural of the generator, or None if no generator is set.

        :returns: The generator's source.
        """
    def set_source(self, res: substance_painter.resource.ResourceID) -> SourceSubstance:
        """
        Create and assign a source from the given resource and return the created source.
        The resource must have a :class:`Usage.GENERATOR <substance_painter.resource.Usage>` usage.

        :param res: The generator material to apply.
        :raises ValueError: If `res` is not a valid resource or does not have
                :class:`Usage.GENERATOR <substance_painter.resource.Usage>` usage.
        :returns: The generator's source.
        """
    def remove_source(self) -> None:
        """
        Remove the currently used source.
        """

class PaintEffectNode(Node):
    """
    A node allowing manipulation of a Paint effect.

    Note:
        Strokes are not accessible from the Python API.
    """
class FillEffectNode(FillParamsEditorMixin, SourceEditorMixin, Node):
    """
    A node allowing manipulation of a Fill effect.
    """

class LevelsEffectNode(Node):
    """
    A node allowing manipulation of a Levels effect.

    See also:
        `Levels effect documentation`_

    .. _Levels effect documentation:
        https://helpx.adobe.com/substance-3d-painter/features/effects/levels.html
    """
    @property
    def affected_channel(self) -> ChannelType:
        """
        The channel affected by the current level effect.

        :getter: Returns the affected channel.
        :setter: Set the affected channel.
        :type: ChannelType
        """
    @affected_channel.setter
    def affected_channel(self, channel: ChannelType) -> None: ...
    def get_parameters(self) -> LevelsParams:
        """
        Get the current parameters of this levels effect.

        :returns: The current level parameters.
        """
    def set_parameters(self, params: LevelsParams) -> None:
        """
        Set new parameters for this levels effect.

        :param params: The new parameters.
        """

@dataclasses.dataclass
class CompareMaskEffectParams:
    """
    A compare mask effect parameters.

    :param channel: The channel to compare between the source and the target to create a
        mask from. Only used when some operands refers to Layers.
    :param left_operand: The left operand of the comparison.
    :param right_operand: The right operand of the comparison.
    :param operation: The comparison operation to perform.
    :param constant: Value to compare against when some operand is
        :class:`CompareMaskEffectOperand.Constant <CompareMaskEffectOperand>`. Between 0.0 and 1.0.
    :param tolerance: Tolerance value to use when `operation` is
        :class:`CompareMaskEffectOperation.WithinTolerance <CompareMaskEffectOperand>`.
        Between 0.0 and 1.0.
    :param hardness: Controls the smoothness/hardness of the resulting mask comparison.
        Between 0.0 and 1.0.
    """
    channel: ChannelType
    left_operand: CompareMaskEffectOperand
    right_operand: CompareMaskEffectOperand
    operation: CompareMaskEffectOperation
    constant: float
    tolerance: float
    hardness: float

class CompareMaskEffectNode(Node):
    """
    A node allowing manipulation of a Compare Mask effect.

    See also:
        `Compare Mask effect documentation`_

    .. _Compare Mask effect documentation:
        https://helpx.adobe.com/substance-3d-painter/features/effects/compare-mask.html
    """
    def get_parameters(self) -> CompareMaskEffectParams:
        """
        Get the current parameters of this compare mask effect.

        :returns: The current parameters of this compare mask effect.
        """
    def set_parameters(self, params: CompareMaskEffectParams) -> None:
        """
        Set new parameters of this compare mask effect.

        :param params: The new parameters.
        """

class FilterEffectNode(ActiveChannelsMixin, Node):
    """
    A node allowing manipulation of a Filter effect.
    """
    def get_source(self) -> SourceSubstance:
        """
        Get the source procedural of the filter, or None if no filter is set.

        :returns: The filter's source.
        """
    def set_source(self, res: substance_painter.resource.ResourceID) -> SourceSubstance:
        """
        Create and assign a source from the given resource and return the created source.
        The resource must have a :class:`Usage.FILTER <substance_painter.resource.Usage>` usage.

        :param res: The filter material to apply.
        :raises ValueError: If `res` is not a valid resource or does not have
                :class:`Usage.FILTER <substance_painter.resource.Usage>` usage.
        :returns: The filter's source.
        """
    def remove_source(self) -> None:
        """
        Remove the currently used source.
        """

@dataclasses.dataclass
class ColorSelectionEffectParams:
    """
    A color selection effect parameters.

    :param id_mask: Which color map to use.
        Typically the ID Mask baked map. Must have
        :class:`Usage.TEXTURE <substance_painter.resource.Usage>` and be part of the project.
    :param output_value: Output value when selection matches. Between 0.0 and 1.0.
    :param hardness: Hardness of the selection. Between 0.0 and 1.0.
    :param tolerance: Tolerance of the selection. Between 0.0 and 1.0.
    :param background_color: Output value when selection does not match.
    :param colors: List of colors to match in the id_mask.
    """
    id_mask: substance_painter.resource.ResourceID | None
    output_value: float
    hardness: float
    tolerance: float
    background_color: ColorSelectionBackgroundColor
    colors: list[Color]

class ColorSelectionEffectNode(Node):
    """
    A node allowing manipulation of a Color Selection effect.
    """
    def get_parameters(self) -> ColorSelectionEffectParams:
        """
        Get the current parameters of this color selection effect.

        :returns: The current parameters of this color selection effect.
        """
    def set_parameters(self, params: ColorSelectionEffectParams) -> None:
        """
        Set new parameters of this compare mask effect.

        :param params: The new parameters.
        :raises ResourceNotFoundError: If the resource ``params.id_mask`` is not found or is not of
                :class:`Type.IMAGE <substance_painter.resource.Type>`.
        """

class AnchorPointEffectNode(Node):
    """
    A node allowing manipulation of an Anchor Point effect.
    """
EffectNode = GeneratorEffectNode | PaintEffectNode | FillEffectNode | LevelsEffectNode | CompareMaskEffectNode | FilterEffectNode | ColorSelectionEffectNode | AnchorPointEffectNode

def get_root_layer_nodes(stack: Stack) -> list[HierarchicalNode]:
    """
    Get the root layers of a stack, ordered like in the layer stack.

    :param stack: Stack to query.
    :raises ValueError: If `stack` is invalid.
    :returns: The root layers of the stack.
    """
def get_node_by_uid(node_id: int) -> list[HierarchicalNode | EffectNode]:
    """
    Get a node by its internal identifier.

    :param node_id: The node uid.
    :raises ValueError: If the given uid doesn't correspond to a valid node.
    :returns: The node with the given uid.
    """
def get_selected_nodes(stack: Stack) -> list[HierarchicalNode | EffectNode]:
    """
    Get the selected nodes of a Stack, ordered like in the layer stack.

    :param stack: Stack to query.
    :returns: The selected nodes of the stack.
    """
def set_selected_nodes(nodes: list[EffectNode] | list[LayerNode]):
    """
    Select the given nodes in the layer stack UI.

    :pararm nodes: Nodes to select.
    :raises ValueError: If the nodes doesn't belong to the currently selected texture set.
    :raises RuntimeError: If called from a :class:`ScopedModification` section
    """
def get_selection_type(layer: LayerNode) -> SelectionType:
    """
    Return which part of a layer is selected (content, mask, etc...).

    :param layer: Layer to query.
    :raises ValueError: If the layer doesn't belong to the currently selected texture set.
    :returns: The part of the layer that is selected.
    """
def set_selection_type(layer: LayerNode, layer_selection_type: SelectionType):
    """
    Select which part of the layer you want to select.

    :param layer: Layer to select.
    :param layer_selection_type: Part of the layer you want to select (content, mask, etc...).
    :raises ValueError: If the layer doesn't belong to the currently selected texture set.
    :raises RuntimeError: If called from a :class:`ScopedModification` section
    """
def delete_node(node: Node):
    """
    Delete the given node.

    :param node: Node to delete.
    """

@dataclasses.dataclass
class UVTransformationParams:
    """
    UV projection transformation parameters.

    :param scale_mode: How `scale` should be interpreted.
        For a :class:`ProjectionMode.Spherical <ProjectionMode>` projection,
        only :class:`ScaleMode.Factors <ScaleMode>` is supported.
        Using :class:`ScaleMode.MaterialPhysicalSize <ScaleMode>` is only possible when
        applied to a resource with physical size information.
    :param scale: The u/v stretch applied to the texture.
        When `scale_mode` is :class:`ScaleMode.Factors <ScaleMode>`,
        use plain factor for stretching.
        When `scale_mode` is :class:`ScaleMode.MaterialPhysicalSize <ScaleMode>`, scale must be None
        and the value will be forced to the actual material physical size.
        When `scale_mode` is :class:`ScaleMode.CustomPhysicalSize <ScaleMode>`, then scale is
        expressed in centimeters and overrides the size defined by the material
        (useful when material has no physical size information).
    :param rotation: Rotation applied to the texture.
    :param offset: Offset applied to the texture.
        The offset is unavailable for a :class:`ProjectionMode.Triplanar <ProjectionMode>`
        projection.
    """
    scale_mode: ScaleMode = ...
    scale: list[float] = ...
    rotation: float = ...
    offset: list[float] = ...

@dataclasses.dataclass
class Projection3DParams:
    """
    3D projection transformation parameters.

    :param offset: 3D offset.
    :param rotation: 3D rotation.
    :param scale: 3D scale.
        Z scaling is unavalaible when projection mode is
        :class:`ProjectionMode.Planar <ProjectionMode>` and depth culling is disabled.
    """
    offset: list[float] = ...
    rotation: list[float] = ...
    scale: list[float] = ...

@dataclasses.dataclass
class ProjectionCullingParams:
    """
    Projection culling parameters.
    Either a depth culling or a backface culling.

    :param enabled: Whether the culling is enabled or not.
    :param hardness: Hardness of the culling, between 0 and 1.
    """
    enabled: bool = ...
    hardness: float = ...

@dataclasses.dataclass
class UVProjectionParams:
    """
    Parameters that control the fill behaviour when the projection mode is
    :class:`ProjectionMode.UV <ProjectionMode>`.
    For a complete description of the parameters, see
    `UV Projection documentation`_.

    .. _UV Projection documentation:
        https://helpx.adobe.com/substance-3d-painter/painting/fill-projections/uv-projection.html

    :param filtering_mode: How to filter the image.
    :param uv_wrapping: UV Wrapping behaviour.
    :param uv_transformation: UV transformation.

    See also:
        :meth:`FillLayerNode.get_projection_mode`
        :meth:`FillLayerNode.get_projection_parameters`
    """
    filtering_mode: FilteringMode = ...
    uv_wrapping_mode: UVWrapMode = ...
    uv_transformation: UVTransformationParams = dataclasses.field(default_factory=UVTransformationParams)

@dataclasses.dataclass
class TriplanarProjectionParams:
    """
    Parameters that control the fill behaviour when the projection mode is
    :class:`ProjectionMode.Triplanar <ProjectionMode>`.
    For a complete description of the parameters, see
    `Triplanar Projection documentation`_.

    .. _Triplanar Projection documentation:
        https://helpx.adobe.com/substance-3d-painter/painting/fill-projections/tri-planar-projection.html

    :param filtering_mode: How to filter the image.
    :param shape_crop_mode: How the fill is cropped.
    :param hardness: How hard is the transition between planes of the projection.
    :param uv_transformation: UV transformation.
    :param projection_3d: 3D projection.

    See also:
        :meth:`FillLayerNode.get_projection_mode`
        :meth:`FillLayerNode.get_projection_parameters`
    """
    filtering_mode: FilteringMode = ...
    shape_crop_mode: ShapeCropMode = ...
    hardness: float = ...
    uv_transformation: UVTransformationParams = dataclasses.field(default_factory=UVTransformationParams)
    projection_3d: Projection3DParams = dataclasses.field(default_factory=Projection3DParams)

@dataclasses.dataclass
class PlanarProjectionParams:
    """
    Parameters that control the fill behaviour when the projection mode is
    :class:`ProjectionMode.Planar <ProjectionMode>`.
    For a complete description of the parameters, see
    `Planar Projection documentation`_.

    .. _Planar Projection documentation:
        https://helpx.adobe.com/substance-3d-painter/painting/fill-projections/planar-projection.html

    :param filtering_mode: How to filter the image.
    :param uv_wrapping_mode: UV Wrapping behaviour.
    :param shape_crop_mode: How the fill is cropped.
    :param depth_culling: Depth culling settings.
    :param backface_culling: Backface culling settings.
    :param backface_culling_angle: Minimum angle which determines when faces that are looking
        away should be ignored, between 45 and 135.
    :param uv_transformation: UV transformation.
    :param projection_3d: 3D projection.

    See also:
        :meth:`FillLayerNode.get_projection_mode`
        :meth:`FillLayerNode.get_projection_parameters`
    """
    filtering_mode: FilteringMode = ...
    uv_wrapping_mode: UVWrapMode = ...
    shape_crop_mode: ShapeCropMode = ...
    depth_culling: ProjectionCullingParams = dataclasses.field(default_factory=ProjectionCullingParams)
    backface_culling: ProjectionCullingParams = dataclasses.field(default_factory=ProjectionCullingParams)
    backface_culling_angle: float = ...
    uv_transformation: UVTransformationParams = dataclasses.field(default_factory=UVTransformationParams)
    projection_3d: Projection3DParams = dataclasses.field(default_factory=Projection3DParams)

@dataclasses.dataclass
class WarpProjectionParams:
    """
    Parameters that control the fill behaviour when the projection mode is
    :class:`ProjectionMode.Warp <ProjectionMode>`.
    For a complete description of the parameters, see
    `Warp Projection documentation`_.

    .. _Warp Projection documentation:
        https://helpx.adobe.com/substance-3d-painter/painting/fill-projections/warp-projection.html

    :param filtering_mode: How to filter the image.
    :param uv_wrapping_mode: UV Wrapping behaviour.
    :param shape_crop_mode: How the fill is cropped.
    :param projection_depth: How far the projection goes along its Z axis.
    :param depth_culling: Depth culling parameters.
    :param uv_transformation: UV transformation.
    :param projection_3d: 3D projection.

    See also:
        :meth:`FillLayerNode.get_projection_mode`
        :meth:`FillLayerNode.get_projection_parameters`
    """
    filtering_mode: FilteringMode = ...
    uv_wrapping_mode: UVWrapMode = ...
    shape_crop_mode: ShapeCropMode = ...
    projection_depth: float = ...
    depth_culling: ProjectionCullingParams = dataclasses.field(default_factory=ProjectionCullingParams)
    uv_transformation: UVTransformationParams = dataclasses.field(default_factory=UVTransformationParams)
    projection_3d: Projection3DParams = dataclasses.field(default_factory=Projection3DParams)

@dataclasses.dataclass
class SphericalProjectionParams:
    """
    Parameters that control the fill behaviour when the projection mode is
    :class:`ProjectionMode.Spherical <ProjectionMode>`.
    For a complete description of the parameters, see
    `Spherical Projection documentation`_.

    .. _Spherical Projection documentation:
        https://helpx.adobe.com/substance-3d-painter/painting/fill-projections/spherical-projection.html

    :param filtering_mode: How to filter the image.
    :param uv_wrapping_mode: UV Wrapping behaviour.
    :param shape_crop_mode: How the fill is cropped.
    :param uv_transformation: UV transformation.
        Spherical projection do not support UV transformation physical size options.
    :param projection_3d: 3D projection.

    See also:
        :meth:`FillLayerNode.get_projection_mode`
        :meth:`FillLayerNode.get_projection_parameters`
    """
    filtering_mode: FilteringMode = ...
    uv_wrapping_mode: UVWrapMode = ...
    shape_crop_mode: ShapeCropMode = ...
    uv_transformation: UVTransformationParams = dataclasses.field(default_factory=UVTransformationParams)
    projection_3d: Projection3DParams = dataclasses.field(default_factory=Projection3DParams)

@dataclasses.dataclass
class CylindricalProjectionParams:
    """
    Parameters that control the fill behaviour when the projection mode is
    :class:`ProjectionMode.Cylindrical <ProjectionMode>`.
    For a complete description of the parameters, see
    `Cylindrical Projection documentation`_.

    .. _Cylindrical Projection documentation:
        https://helpx.adobe.com/substance-3d-painter/painting/fill-projections/cylindrical-projection.html

    :param filtering_mode: How to filter the image.
    :param uv_wrapping_mode: UV Wrapping behaviour.
    :param shape_crop_mode: How the fill is cropped.
    :param angle: Size of the projection on the perimeter of the cylinder.
    :param backface_culling: Backface culling parameters.
    :param uv_transformation: UV transformation.
    :param projection_3d: 3D projection.

    See also:
        :meth:`FillLayerNode.get_projection_mode`
        :meth:`FillLayerNode.get_projection_parameters`
    """
    filtering_mode: FilteringMode = ...
    uv_wrapping_mode: UVWrapMode = ...
    shape_crop_mode: ShapeCropMode = ...
    angle: float = ...
    backface_culling: ProjectionCullingParams = dataclasses.field(default_factory=ProjectionCullingParams)
    uv_transformation: UVTransformationParams = dataclasses.field(default_factory=UVTransformationParams)
    projection_3d: Projection3DParams = dataclasses.field(default_factory=Projection3DParams)

@dataclasses.dataclass
class UVSetToUVSetProjectionParams:
    """
    Parameters that control the fill behaviour when the projection mode is
    :class:`ProjectionMode.UVSetToUVSet <ProjectionMode>`.
    For a complete description of the parameters, see
    `UVSetToUVSet Projection documentation`_.

    .. _UVSetToUVSet Projection documentation:
        https://helpx.adobe.com/substance-3d-painter/painting/fill-projections/uv-set-to-uv-set-projection.html

    :param source_uv_set: Mesh UV set index used as projection source (0: no effect).
    :param filtering_mode: How to filter the image.
    :param uv_wrapping: UV Wrapping behaviour.
    :param uv_transformation: UV transformation.

    See also:
        :meth:`FillLayerNode.get_projection_mode`
        :meth:`FillLayerNode.get_projection_parameters`
    """
    source_uv_set: int = ...
    filtering_mode: FilteringMode = ...
    uv_wrapping_mode: UVWrapMode = ...
    uv_transformation: UVTransformationParams = dataclasses.field(default_factory=UVTransformationParams)
ProjectionParams = UVProjectionParams | TriplanarProjectionParams | PlanarProjectionParams | WarpProjectionParams | SphericalProjectionParams | CylindricalProjectionParams | UVSetToUVSetProjectionParams

@dataclasses.dataclass
class MirrorSymmetryParams:
    """
    Parameters that control the mirror symmetry behaviour.

    :param axis: Axis along which to mirror.
    :param flip_u: Whether to flip UVs along the U axis.
    :param flip_v: Whether to flip UVs along the V axis.
    :param axis_position: Position of the mirror plane along each axis, clamped between [-10, -10,
        -10] and [10, 10, 10].

    See also:
        :meth:`FillLayerNode.get_symmetry_mode`
        :meth:`FillLayerNode.get_symmetry_parameters`
    """
    axis: SymmetryAxis = ...
    flip_u: bool = ...
    flip_v: bool = ...
    axis_position: list[float] = ...

@dataclasses.dataclass
class RadialSymmetryParams:
    """
    Parameters that control the radial symmetry behaviour.

    When setting symmetry, some parameters will get clamped:

    :param axis: Axis along which to mirror.
    :param flip_u: Whether to flip UVs along the U axis.
    :param flip_v: Whether to flip UVs along the V axis.
    :param axis_position: Position of the mirror plane along each axis, clamped between [-10, -10,
        -10] and [10, 10, 10].
    :param count: Number of copies, clamped between 2 and 16.
    :param angle_span: Angle span of the copies, in degrees, clamped between -360 and 360.

    See also:
        :meth:`FillLayerNode.get_symmetry_mode`
        :meth:`FillLayerNode.get_symmetry_parameters`
    """
    axis: SymmetryAxis = ...
    flip_u: bool = ...
    flip_v: bool = ...
    axis_position: list[float] = ...
    count: int = ...
    angle_span: float = ...
SymmetryParams = MirrorSymmetryParams | RadialSymmetryParams

@dataclasses.dataclass(frozen=True)
class InsertPosition:
    '''
    :class:`InsertPosition` is the object used by all the insert methods to express
    where you want the insertion to happen in the layer stack hierarchy.

    Create instances using the appropriate static methods depending on what
    you want to do. See the following examples.

    Example:
        ::

            import substance_painter as sp

            # Insert at the top of the given textureset layer stack
            insert_position = sp.layerstack.InsertPosition.from_textureset_stack(
                sp.textureset.get_active_stack())
            new_layer = sp.layerstack.insert_fill(insert_position)
            new_layer.set_name("First layer")

            # Insert a layer above new_layer
            insert_position = sp.layerstack.InsertPosition.above_node(new_layer)
            sp.layerstack.insert_fill(insert_position)

            # Insert an effect in the content stack of new_layer
            insert_position = sp.layerstack.InsertPosition.inside_node(
                new_layer, sp.layerstack.NodeStack.Content)
            new_effect = sp.layerstack.insert_fill(insert_position)
            new_effect.set_name("First effect")

            # Insert an effect below new_effect
            insert_position = sp.layerstack.InsertPosition.below_node(new_effect)
            sp.layerstack.insert_fill(insert_position)
    '''
    node_id: int
    node_stack: int | None
    @staticmethod
    def from_textureset_stack(stack: substance_painter.textureset.Stack) -> InsertPosition:
        """
        Generate an :class:`InsertPosition` on the top of a stack.

        Only a :class:`LayerNode` can be inserted at the top of the stack.
        For more details, see :ref:`insertion_rules_layer`.

        :pararm stack: Stack in which you wish to insert.
        """
    @staticmethod
    def above_node(node: Node) -> InsertPosition:
        """
        Generate an :class:`InsertPosition` to insert above the given node.

        Only a :class:`LayerNode` can be inserted above a :class:`LayerNode`.
        Only an :class:`EffectNode` can be inserted above an :class:`EffectNode`.
        For more details, see :ref:`insertion_rules_layer` and :ref:`insertion_rules_effect`.

        :param node: the node.
        """
    @staticmethod
    def below_node(node: Node) -> InsertPosition:
        """
        Generate an :class:`InsertPosition` to insert below the given node.

        Only a :class:`LayerNode` can be inserted above a :class:`LayerNode`.
        Only an :class:`EffectNode` can be inserted above an :class:`EffectNode`.
        For more details, see :ref:`insertion_rules_layer` and :ref:`insertion_rules_effect`.

        :param node: the node.
        """
    @staticmethod
    def inside_node(node: Node, node_stack: NodeStack) -> InsertPosition:
        """
        Generate an :class:`InsertPosition` to insert inside the given stack of a node.

        Only a :class:`LayerNode` can be inserted inside a :class:`GroupLayerNode` if `node_stack`
        is :class:`NodeStack.Substack <NodeStack>`.
        Only an :class:`EffectNode` can be inserted inside a :class:`LayerNode` if `node_stack`
        is :class:`NodeStack.Content <NodeStack>` or :class:`NodeStack.Mask <NodeStack>`.
        For more details, see :ref:`insertion_rules_layer` and :ref:`insertion_rules_effect`.

        :param node: the node.
        :param node_stack: indicate in which layer's stack you want
                to insert (Only valid for nodes which are layers).
        """

def insert_fill(position: InsertPosition) -> FillLayerNode | FillEffectNode:
    """
    Insert a Fill effect or layer (depending on the insert position).

    :param position: Insert position.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :returns: The inserted node.
    """
def insert_paint(position: InsertPosition) -> PaintLayerNode | PaintEffectNode:
    """
    Insert a Paint effect or layer (depending on the insert position).

    :param position: Insert position.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :returns: The inserted node.
    """
def insert_group(position: InsertPosition) -> GroupLayerNode:
    """
    Insert a group layer.

    :param position: The insert position must be either inside
            a :class:`GroupLayerNode` with :class:`NodeStack.Substack <NodeStack>`
            or above/below a :class:`LayerNode`.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :returns: The inserted node.
    """
def instantiate(position: InsertPosition, layer: LayerNode) -> InstanceLayerNode:
    """
    Instantiate the given layer.
    See the documentation on layer instancing if you are not familiar with the
    concept: `Layer instancing documentation`_.

    .. _Layer instancing documentation:
        https://helpx.adobe.com/substance-3d-painter/interface/layer-stack/layer-instancing.html

    :param position: Insert position.
    :param layer: Layer to instantiate.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :returns: The inserted node.
    """
def insert_levels_effect(position: InsertPosition) -> LevelsEffectNode:
    """
    Insert a levels effect with default parameters.

    :param position: The insert position must be either inside
            a :class:`LayerNode` with :class:`NodeStack.Content <NodeStack>`
            or :class:`NodeStack.Mask <NodeStack>`
            or above/below an :class:`EffectNode`.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :returns: The inserted node.
    """
def insert_compare_mask_effect(position: InsertPosition) -> CompareMaskEffectNode:
    """
    Insert a compare mask effect with default parameters.

    :param position: The insert position must be either inside
            a :class:`LayerNode` with :class:`NodeStack.Mask <NodeStack>`
            or above/below an :class:`EffectNode` in the mask stack.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :returns: The inserted node.
    """
def insert_filter_effect(position: InsertPosition, filter_substance: substance_painter.resource.ResourceID | None = None) -> FilterEffectNode:
    """
    Insert a filter effect, either empty or with the given filter resource.

    :param position: The insert position must be either inside
            a :class:`LayerNode` with :class:`NodeStack.Content <NodeStack>`
            or :class:`NodeStack.Mask <NodeStack>`
            or above/below an :class:`EffectNode`.
    :param filter_substance: Resource to use as filter. The resource must have a
            :class:`Usage.FILTER <substance_painter.resource.Usage>` usage.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :raises ValueError: If `filter_substance` is not a valid resource or
            does not have :class:`Usage.FILTER <substance_painter.resource.Usage>` usage.
    :returns: The inserted node.
    """
def insert_generator_effect(position: InsertPosition, generator_substance: substance_painter.resource.ResourceID | None = None) -> GeneratorEffectNode:
    """
    Insert a Generator effect, either empty or with the given filter resource.

    :param position: The insert position must be either inside
            a :class:`LayerNode` with :class:`NodeStack.Content <NodeStack>` or
            :class:`NodeStack.Mask <NodeStack>` or above/below an :class:`EffectNode`.
    :param generator_substance: Resource to use as generator. The resource must have a
            :class:`Usage.GENERATOR <substance_painter.resource.Usage>` usage.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :raises ValueError: If `generator_substance` is not a valid resource or
            does not have :class:`Usage.GENERATOR <substance_painter.resource.Usage>` usage.
    :returns: The inserted node.
    """
def insert_anchor_point_effect(position: InsertPosition, name: str) -> AnchorPointEffectNode:
    """
    Insert an anchor point effect.

    :param position: The insert position must be either inside
            a :class:`LayerNode` with :class:`NodeStack.Content <NodeStack>`
            or :class:`NodeStack.Mask <NodeStack>`
            or above/below an :class:`EffectNode`.
    :param name: Name of the anchor point.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :returns: The new anchor point.
    """
def insert_color_selection_effect(position: InsertPosition) -> ColorSelectionEffectNode:
    """
    Insert a color selection effect.

    :param position: The insert position must be either inside
            a :class:`LayerNode` with :class:`NodeStack.Mask <NodeStack>`
            or above/below an :class:`EffectNode` in the mask stack.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :returns: The inserted node.
    """
def insert_smart_material(position: InsertPosition, smart_material: substance_painter.resource.ResourceID) -> GroupLayerNode:
    """
    Insert a smart material at the given position.

    :param position: The insert position must be either inside
            a :class:`GroupLayerNode` with :class:`NodeStack.Substack <NodeStack>`
            or above/below a :class:`LayerNode`.
    :param smart_material: The smart material to instantiate. The resource must have a
            :class:`Usage.SMART_MATERIAL <substance_painter.resource.Usage>` usage.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :raises ValueError: If `smart_material` is not a valid resource or does not have
            :class:`Usage.SMART_MATERIAL <substance_painter.resource.Usage>` usage.
    :returns: The inserted node.
    """
def create_smart_material(group: GroupLayerNode, name: str) -> substance_painter.resource.Resource:
    """
    Create a smart material with name ``name`` from the given ``group``.

    :param group: The root folder of the smart material.
    :param name: The name of the smart material.
    :returns: The created smart material as a resource.
    """
def insert_smart_mask(position: InsertPosition, smart_mask: substance_painter.resource.ResourceID) -> list[EffectNode]:
    """
    Insert a smart mask in a mask stack.

    :param position: The insert position must be either inside
            a :class:`LayerNode` with :class:`NodeStack.Mask <NodeStack>`
            or above/below an :class:`EffectNode` in the mask stack.
    :param smart_mask: The smart mask to instantiate. The resource must have a
            :class:`Usage.SMART_MASK <substance_painter.resource.Usage>` usage.
    :raises ValueError: If insertion failed due to an invalid `position`.
            See :class:`InsertPosition`.
    :raises ValueError: If `smart_mask` is not a valid resource or does not have
            :class:`Usage.SMART_MASK <substance_painter.resource.Usage>` usage.
    :returns: The inserted nodes.
    """
def create_smart_mask(layer: LayerNode, name: str) -> substance_painter.resource.Resource:
    """
    Create a smart mask with name ``name`` from the mask stack of the given ``layer``.

    :param layer: The parent layer of the mask stack to create.
    :param name: The name of the smart mask.
    :returns: The created smart mask as a resource.
    """
