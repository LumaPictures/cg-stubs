# Houdini stubs generated from Houdini 22.0.466

import hou
import resourceutils as ru
from collections.abc import Callable as Callable, Iterable, Sequence
from houtypes import ViewerStateEventKwargs
from resourceutils import SingleSelectResult as SingleSelectResult

SELECTABLE_SPRITE_NAMES: set[str]
DEFAULT_IMAGE_DIR: str

class SpriteEntry:
    """Metadata for a single named sprite in the sprite overlay system."""
    name: str
    position: hou.Vector3
    image_path: str
    color: hou.Vector3
    size: float
    offset: hou.Vector3
    visible: bool
    point_index: int
    tooltip: str
    fixed_size: float
    screen_clamp: bool
    def __init__(self, name: str, position: hou.Vector3, image_path: str = '', color: hou.Vector3 | None = None, size: float = 1.0, offset: hou.Vector3 | None = None, visible: bool = True, tooltip: str = '', fixed_size: float = 0.0, screen_clamp: bool = False) -> None: ...

class ButtonEntry:
    """A multi-mode button: N sprites sharing metadata, one visible at a time."""
    name: str
    position: hou.Vector3
    image_paths: list[str]
    color: hou.Vector3
    size: float
    offset: hou.Vector3
    visible: bool
    mode: int
    num_modes: int
    tooltip: str
    fixed_size: float
    screen_clamp: bool
    def __init__(self, name: str, position: hou.Vector3, image_paths: Sequence[str], color: hou.Vector3 | None = None, size: float = 1.0, offset: hou.Vector3 | None = None, visible: bool = True, tooltip: str = '', fixed_size: float = 0.0, screen_clamp: bool = False) -> None: ...

class ButtonGroupEntry:
    """A named group of buttons with shared position offset and visibility."""
    name: str
    position: hou.Vector3
    visible: bool
    button_names: list[str]
    def __init__(self, name: str, position: hou.Vector3 | None = None, visible: bool = True) -> None: ...

class SpriteSelector(ru.DrawableSelector):
    """Single-pick selector for sprite points. No box selection."""
    gadget: SpriteGadget
    def __init__(self, scene_viewer: hou.SceneViewer, sprite_drawable: hou.GeometryDrawable, gadget: SpriteGadget) -> None: ...
    def onLocateSingleSelection(self, kwargs: ViewerStateEventKwargs, result: SingleSelectResult) -> bool:
        """Hover: highlight the sprite under cursor (Cd swap), call dispatch."""
    def onSingleSelection(self, kwargs: ViewerStateEventKwargs, result: SingleSelectResult) -> bool:
        """Click: call dispatch."""

class SpriteGadget:
    """Standalone sprite overlay gadget. Manages a single hou.GeometryDrawable of type Sprite
    with named entries, multi-mode buttons, button groups, single-click selection, and hover highlighting.

    Can be used standalone or composed into other gadgets (e.g. JointGadget).
    """
    scene_viewer: hou.SceneViewer
    name: str
    default_image_dir: str
    show_sprites: bool
    sprite_drawable: hou.GeometryDrawable | None
    sprite_geo: hou.Geometry
    sprite_selector: SpriteSelector | None
    _sprite_select_callback: Callable[[str, hou.Vector3, hou.EnumValue[hou.pickModifier]], object] | None
    _sprite_locate_callback: Callable[[str, hou.Vector3, hou.EnumValue[hou.pickModifier]], object] | None
    _button_select_callback: Callable[[str, int, hou.EnumValue[hou.pickModifier]], object] | None
    _button_locate_callback: Callable[[str, int, hou.EnumValue[hou.pickModifier]], object] | None
    _tooltip_drawable: hou.TextDrawable | None
    _tooltip_font_size: float
    sprite_entries: dict[str, SpriteEntry]
    button_entries: dict[str, ButtonEntry]
    button_group_entries: dict[str, ButtonGroupEntry]
    def __init__(self, scene_viewer: hou.SceneViewer, name: str = 'sprites', default_image_dir: str | None = None) -> None: ...
    def initDrawable(self) -> None:
        """Creates the sprite drawable and selector."""
    def onDraw(self, handle: hou.Handle) -> None: ...
    def onDrawInterrupt(self, handle: hou.Handle) -> None: ...
    def show(self, on: bool = True) -> None: ...
    def showSprites(self, on: bool) -> None:
        """Sets the visibility of the sprite overlay layer."""
    def addSprite(self, name: str, position: hou.Vector3, image_path: str = '', color: hou.Vector3 | None = None, size: float = 1.0, offset: hou.Vector3 | None = None, tooltip: str = '', fixed_size: float = 0.0, screen_clamp: bool = False) -> None:
        """Adds or replaces a named sprite for an asset in the scene.

        :param name: unique identifier for the sprite (typically the asset name)
        :param position: world-space position for the sprite
        :param image_path: filesystem path or bare filename (resolved via default_image_dir)
        :param color: RGB tint color applied via per-point Cd
        :param size: uniform scale applied via per-point pscale
        :param offset: projective-space offset via per-point spriteoffset
        :param tooltip: optional label text shown on hover
        :param fixed_size: lock the sprite to a constant **screen-space pixel
            height** by clamping spritesizemin and spritesizemax to this value.
            0.0 (default) = no clamp, i.e. the sprite scales with camera zoom
            normally. Units are pixels, not world units.
        :parm screen_clamp: when True, the sprite will always display within
        the view so it essentially always shows whether the camera is looking
        at it or not.
        """
    def removeSprite(self, name: str) -> None:
        """Removes a named sprite from the collection.

        :param name: the name of the sprite to remove
        """
    def updateSpritePosition(self, name: str, position: hou.Vector3) -> None:
        """Updates the world-space position of a named sprite without rebuilding the geometry.

        :param name: sprite identifier
        :param position: new world-space position
        """
    def updateSpriteColor(self, name: str, color: hou.Vector3) -> None:
        """Updates the tint color of a named sprite.

        :param name: sprite identifier
        :param color: new RGB color
        """
    def updateSpriteImage(self, name: str, image_path: str) -> None:
        """Updates the image path of a named sprite, triggers a geometry rebuild since
        the images param on the drawable must be updated.

        :param name: sprite identifier
        :param image_path: new filesystem path or bare filename (resolved via default_image_dir)
        """
    def updateSpriteSize(self, name: str, size: float) -> None:
        """Updates the display size of a named sprite.

        :param name: sprite identifier
        :param size: new uniform scale (pscale, world units). This is independent
            of any fixed_size pixel clamp already set on the sprite.
        """
    def updateSpriteOffset(self, name: str, offset: hou.Vector3) -> None:
        """Updates the projective-space offset of a named sprite.

        :param name: sprite identifier
        :param offset: new offset (x, y in screen space, z for depth sorting)
        """
    def updateSpriteFixedSize(self, name: str, fixed_size: float) -> None:
        """Set the screen-space pixel clamp on a named sprite.

        :param name: sprite identifier
        :param fixed_size: pixel height to lock the sprite to (both
            spritesizemin and spritesizemax are set to this). 0.0 disables the
            clamp and the sprite scales with camera zoom again.
        """
    def setSpriteVisible(self, name: str, visible: bool) -> None:
        """Shows or hides a named sprite by zeroing pscale (and setting spritehidden).

        :param name: sprite identifier
        :param visible: True to show, False to hide
        """
    def setSpriteSelectCallback(self, callback: Callable[[str, hou.Vector3, hou.EnumValue[hou.pickModifier]], object] | None) -> None:
        """Set the callback for sprite click selection.
        Receives (name: str, position: hou.Vector3, pick_modifier: hou.pickModifier)."""
    def setSpriteLocateCallback(self, callback: Callable[[str, hou.Vector3, hou.EnumValue[hou.pickModifier]], object] | None) -> None:
        """Set the callback for sprite hover/locate.
        Receives (name: str, position: hou.Vector3, pick_modifier: hou.pickModifier)."""
    def setSpriteTintable(self, name: str, tintable: bool = True) -> None:
        """Control whether a sprite gets a Cd highlight on hover."""
    def setSpriteHighlightColor(self, color: hou.Vector3) -> None:
        """Set the highlight color used when hovering tintable sprites."""
    def setSelectableSpriteNames(self, names: Iterable[str] | None) -> None:
        """Override the module-level SELECTABLE_SPRITE_NAMES whitelist for this instance.
        Pass None to revert to the module-level default."""
    def addButton(self, name: str, position: hou.Vector3, image_paths: Iterable[str], color: hou.Vector3 | None = None, size: float = 1.0, offset: hou.Vector3 | None = None, tooltip: str = '', fixed_size: float = 0.0, screen_clamp: bool = False) -> None:
        """Add a multi-mode button. image_paths defines the modes (len >= 2).
        Only the first mode (index 0) is visible initially.

        :param name: unique button identifier
        :param position: world-space position (group offset added if grouped)
        :param image_paths: list of image paths or bare filenames, one per mode
        :param color: shared tint color for all modes
        :param size: shared pscale for all modes
        :param offset: shared spriteoffset for all modes
        :param tooltip: optional label text shown on hover
        :param fixed_size: lock each mode-sprite to a constant screen-space
            pixel height. 0.0 = no clamp.
        """
    def removeButton(self, name: str) -> None:
        """Remove a button and all its internal sprites."""
    def setButtonMode(self, name: str, mode: int) -> None:
        """Explicitly set the active mode of a button."""
    def getButtonMode(self, name: str) -> int:
        """Get the current mode of a button. Returns -1 if button not found."""
    def updateButtonPosition(self, name: str, position: hou.Vector3) -> None:
        """Update the base position of a button. All mode sprites are repositioned."""
    def updateButtonColor(self, name: str, color: hou.Vector3) -> None:
        """Update the tint color of all mode sprites in a button."""
    def updateButtonSize(self, name: str, size: float) -> None:
        """Update the pscale of all mode sprites in a button."""
    def updateButtonOffset(self, name: str, offset: hou.Vector3) -> None:
        """Update the spriteoffset of all mode sprites in a button."""
    def updateButtonFixedSize(self, name: str, fixed_size: float) -> None:
        """Set the screen-space pixel clamp on all mode sprites of a button.
        0.0 disables the clamp.
        """
    def setButtonVisible(self, name: str, visible: bool) -> None:
        """Show/hide the entire button. When visible, only the current mode sprite is shown."""
    def setButtonSelectCallback(self, callback: Callable[[str, int, hou.EnumValue[hou.pickModifier]], object] | None) -> None:
        """Set callback for button mode changes.
        Receives (button_name: str, new_mode: int, pick_modifier: hou.pickModifier)."""
    def setButtonLocateCallback(self, callback: Callable[[str, int, hou.EnumValue[hou.pickModifier]], object] | None) -> None:
        """Set callback for button hover.
        Receives (button_name: str, current_mode: int, pick_modifier: hou.pickModifier)."""
    def addButtonGroup(self, name: str, position: hou.Vector3 | None = None) -> None:
        """Create a named button group with an optional position offset."""
    def removeButtonGroup(self, name: str) -> None:
        """Remove a group. Buttons in the group become ungrouped and revert to their own positions."""
    def addButtonToGroup(self, button_name: str, group_name: str) -> None:
        """Add an existing button to a group. Updates sprite positions to include group offset."""
    def removeButtonFromGroup(self, button_name: str) -> None:
        """Remove a button from its group. Reverts positions to the button's own position."""
    def updateButtonGroupPosition(self, name: str, position: hou.Vector3) -> None:
        """Update the group's position offset. Recomputes all member button sprite positions."""
    def setButtonGroupVisible(self, name: str, visible: bool) -> None:
        """Show/hide all buttons in the group."""
    def updateSpriteTooltip(self, name: str, tooltip: str) -> None:
        """Update the tooltip text of a named sprite.

        :param name: sprite identifier
        :param tooltip: new tooltip text (empty string to disable)
        """
    def updateButtonTooltip(self, name: str, tooltip: str) -> None:
        """Update the tooltip text of a button.

        :param name: button identifier
        :param tooltip: new tooltip text (empty string to disable)
        """
    def setTooltipFontSize(self, size: float) -> None:
        """Set the font size for tooltip labels.

        :param size: HTML font size (default 4.0)
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Handles sprite selection (single pick)."""
    def clear(self) -> None:
        """Cleans up drawable and selector state."""
