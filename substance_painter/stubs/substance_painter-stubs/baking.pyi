import dataclasses
from _typeshed import Incomplete
from substance_painter.async_utils import StopSource as StopSource
from substance_painter.properties import Property as Property, PropertyValue as PropertyValue
from substance_painter.textureset import MeshMapUsage as MeshMapUsage, TextureSet as TextureSet, UVTile as UVTile

from _substance_painter.baking import BakingStatus as BakingStatus
from _substance_painter.baking import CurvatureMethod as CurvatureMethod

@dataclasses.dataclass(frozen=True)
class BakingParameters:
    """
    Baking parameters for a given texture set.

    Example:
        ::

            # This example shows how to discover the names of the baking parameters
            import substance_painter as sp

            # Get the first texture set of the current project
            textureset = sp.textureset.all_texture_sets()[0]
            # Retrieve baking parameters
            baking_params = sp.baking.BakingParameters.from_texture_set(textureset)

            # Print the keys of the common baking parameters
            print(f'Common: {baking_params.common().keys()}')
            # Print the keys of the baking parameters of the AO mesh map
            print(f'AO: {baking_params.baker(sp.baking.MeshMapUsage.AO).keys()}')

    See also:
        :class:`substance_painter.textureset.TextureSet`,
        :class:`substance_painter.textureset.MeshMapUsage`
    """
    material_id: int
    @staticmethod
    def from_texture_set(texture_set: TextureSet) -> BakingParameters:
        """
        Get the baking parameters for the given texture set object.

        Args:
            texture_set (TextureSet): The texture set.

        Returns:
            BakingParameters: The baking parameters for the given texure set.

        See also:
            :class:`substance_painter.textureset.TextureSet`
        """
    @staticmethod
    def from_texture_set_name(texture_set_name: str) -> BakingParameters:
        """
        Get the baking parameters for the given texture set name.

        Args:
            texture_set_name (str): The texture set name.

        Returns:
            BakingParameters: The baking parameters for the given texure set.

        See also:
            :class:`substance_painter.properties.Property`
        """
    def texture_set(self) -> TextureSet:
        """
        Get the associated texture set.

        Returns:
            TextureSet: The texture set associated with this BakingParameters instance.

        See also:
            :class:`substance_painter.textureset.TextureSet`
        """
    def common(self) -> dict[str, Property]:
        """
        Get the parameters common to all bakers, like baking resolution.

        Returns:
            Dict[str, Property]: The common parameters.

        See also:
            :class:`substance_painter.properties.Property`
        """
    def baker(self, baked_map: MeshMapUsage) -> dict[str, Property]:
        """
        Get the parameters specific to a given baked map.

        Args:
            baked_map (MeshMapUsage): The baked map usage.

        Returns:
            Dict[str, Property]: The corresponding baked map parameters.

        See also:
            :class:`substance_painter.textureset.MeshMapUsage`,
            :class:`substance_painter.properties.Property`
        """
    @staticmethod
    def set(property_values: dict[Property, PropertyValue]) -> None:
        """
        Set property values in batch.

        Args:
            property_values (Dict[Property, PropertyValue]): A dict of properties
                to be set with their corresponding new values.

        See also:
            :class:`substance_painter.properties.Property`
        """
    def get_curvature_method(self) -> CurvatureMethod:
        """
        Get the curvature method used for baking

        Returns:
            CurvatureMethod: The curvature method used for baking

        See Also:
            `set_curvature_method`
        """
    def set_curvature_method(self, method: CurvatureMethod):
        """
        Set the curvature method to use for baking

        Args:
            method (CurvatureMethod): The new method to use for baking

        See Also:
            `get_curvature_method`
        """
    def is_baker_enabled(self, usage: MeshMapUsage) -> bool:
        """
        Whether some usage is enabled for baking.

        Args:
            usage (MeshMapUsage): The baked map usage.

        Returns:
            bool: True if the corresponding usage is enabled for baking.
        """
    def set_baker_enabled(self, usage: MeshMapUsage, enable: bool) -> None:
        """
        Enable or disable a usage for baking.

        Args:
            usage (MeshMapUsage): The baked map usage.
            enable (bool): Enable or disable.
        """
    def get_enabled_bakers(self) -> list[MeshMapUsage]:
        """
        Get all usages enabled for baking.

        Returns:
            List[MeshMapUsage]: Enabled usages.
        """
    def set_enabled_bakers(self, enabled_usages: list[MeshMapUsage]) -> None:
        """
        Set usages enabled for baking. Usages not in this list will be disabled.

        Args:
            enabled_usages (List[MeshMapUsage]): Enabled usages.
        """
    def is_textureset_enabled(self) -> bool:
        """
        Whether this Texture Set is enabled for baking.

        Returns:
            bool: True if this Texture Set is enabled for baking.
        """
    def set_textureset_enabled(self, enable: bool) -> None:
        """
        Enable or disable this Texture Set for baking.

        Args:
            enable (bool): Enable or disable.
        """
    def is_uv_tile_enabled(self, uv_tile: UVTile) -> bool:
        """
        Whether a UV Tile is enabled for baking.

        Args:
            tile (UVTile): The UV Tile.

        Returns:
            bool: True if the UV Tile is enabled for baking.

        See also:
            :class:`substance_painter.textureset.TextureSet`,
            :class:`substance_painter.textureset.UVTile`
        """
    def set_uv_tile_enabled(self, uv_tile: UVTile, enable: bool) -> None:
        """
        Enable or disable an UV Tile for baking.

        Args:
            uv_tile (UVTile): The UV Tile.
            enable (bool): Enable or disable.

        See also:
            :class:`substance_painter.textureset.TextureSet`,
            :class:`substance_painter.textureset.UVTile`
        """
    def get_enabled_uv_tiles(self) -> list[UVTile]:
        """
        Get all UV Tiles enabled for baking.

        Returns:
            List[UVTile]: Enabled UV Tiles.

        See also:
            :class:`substance_painter.textureset.TextureSet`,
            :class:`substance_painter.textureset.UVTile`
        """
    def set_enabled_uv_tiles(self, enabled_uv_tiles: list[UVTile]) -> None:
        """
        Set UV Tiles enabled for baking. All other tiles will be disabled.

        Args:
            enabled_uv_tiles (List[UVTile]): Enabled UV Tiles.

        See also:
            :class:`substance_painter.textureset.TextureSet`,
            :class:`substance_painter.textureset.UVTile`
        """

def set_linked_group(group: list[TextureSet], reference: TextureSet, usage: MeshMapUsage) -> None:
    """
    Make a group of Texture Sets share the same baking parameters for the given 'usage'. After that,
    editing the 'usage' parameters of one of the group's Texture Set will impact the whole group.

    Args:
        group (List[TextureSet]): Texture Sets to be included in the new group.
        reference (TextureSet): Texture Set which parameters are applied to the whole group.
        usage (MeshMapUsage): Usage of the group.
    """
def set_linked_group_common_parameters(group: list[TextureSet], reference: TextureSet) -> None:
    """
    Make a group of Texture Sets share the same baking common parameters. After that, editing a
    common parameter of one of the group's Texture Set will impact the whole group.

    Args:
        group (List[TextureSet]): Texture Sets to be included in the new group.
        reference (TextureSet): Texture Set which parameters are applied to the whole group.
    """
def unlink_all(usage: MeshMapUsage) -> None:
    """
    Unlink all Texture Sets for a given usage. That is, remove the group if it exists, so that all
    Texture Sets have their own copy of the parameters.

    Args:
        usage (MeshMapUsage): Usage to unlink.
    """
def unlink_all_common_parameters() -> None:
    """
    Unlink all Texture Sets for common parameters. That is, remove the group if exists, so that all
    Texture Sets have their own copy of the parameters.
    """
def get_link_group(usage: MeshMapUsage) -> list[TextureSet]:
    """
    Get the list of Texture Sets that share baking parameters for a given usage.

    Args:
        usage (MeshMapUsage): Usage to query.

    Returns:
        List[TextureSet]: All linked Texture Sets for the usage. Empty list if no Texture Set are
        linked.
    """
def get_link_group_common_parameters() -> list[TextureSet]:
    """
    Get the list of Texture Sets that share common baking parameters.

    Returns:
        List[TextureSet]: All linked Texture Sets for common parameters. Empty list if no Texture
        Set are linked.
    """
def get_linked_texture_sets(texture_set: TextureSet, usage: MeshMapUsage) -> list[TextureSet]:
    """
    Get the list of Texture Sets that share the same parameters as some Texture Set, for a given
    usage.

    Args:
        texture_set (TextureSet): The Texture Set to query
        usage (MeshMapUsage): The usage to query

    Returns:
        List[TextureSet]: The list of Texture Sets sharing parameters with the input Texture Set.
        Contains at least the input Texture Set if no group exists for the usage.
    """
def get_linked_texture_sets_common_parameters(texture_set: TextureSet) -> list[TextureSet]:
    """
    Get the list of Texture Sets that share the same parameters as some Texture Set, for common
    parameters.

    Args:
        texture_set (TextureSet): The Texture Set to query

    Returns:
        List[TextureSet]: The list of Texture Sets sharing common parameters with the input Texture
        Set. Contains at least the input Texture Set if no group exists for common parameters.
    """
def bake_async(texture_set: TextureSet) -> StopSource:
    """
    Launch the baking process for a Texture Set, using the current baking configuration.
    The configuration is set by setting baking parameters, enabling Texture Set, selecting UV Tiles
    for baking, setting curvature method etc.
    This function is asynchronous. When the baking process is finished, the
    :class:`substance_painter.event.BakingProcessEnded` event is sent.

    Args:
        texture_set (TextureSet): The Texture Set to bake.

    Returns:
        StopSource: Can be used to cancel the asynchronous computation.

    See Also:
        :class:`BakingParameters`
        :class:`substance_painter.event.BakingProcessAboutToStart`
        :class:`substance_painter.event.BakingProcessProgress`
        :class:`substance_painter.event.BakingProcessEnded`
        :class:`substance_painter.async_utils.StopSource`
    """
def bake_selected_textures_async() -> StopSource:
    """
    Launch the baking process, using the current baking configuration.
    The configuration is set by setting baking parameters, enabling Texture Set, selecting UV Tiles
    for baking, setting curvature method etc.
    This function is asynchronous. When the baking process is finished, the
    :class:`substance_painter.event.BakingProcessEnded` event is sent.

    Returns:
        StopSource: Can be used to cancel the asynchronous computation.

    See Also:
        :class:`BakingParameters`
        :class:`substance_painter.event.BakingProcessAboutToStart`
        :class:`substance_painter.event.BakingProcessProgress`
        :class:`substance_painter.event.BakingProcessEnded`
        :class:`substance_painter.async_utils.StopSource`
    """
