from collections.abc import Sequence
from typing import Required

import hou
from vopcallbacks import ShaderFxCallbacks
from voptoolutils import _VopFxMenuKwargs

class _VopFxMenuActionKwargs(_VopFxMenuKwargs, total=False):
    """The `kwargs` of a `VOPFXmenu.xml` dynamic menu's script, for the item picked."""

    selectedtoken: Required[str]
    selectedlabel: Required[str]

class VopEffect:
    node_type: str | None
    preset: str | None
    data_types: Sequence[str] | None
    custom_creator: ShaderFxCallbacks | None
    output: int | str
    label: str
    passthrough_input: int | str | None
    promote_child_parms: bool
    def __init__(
        self,
        node_type: str | None = ...,
        preset: str | None = ...,
        label: str | None = ...,
        data_types: Sequence[str] | None = ...,
        custom_creator: ShaderFxCallbacks | None = ...,
        passthrough_input: int | str | None = ...,
        output: int | str = ...,
        promote_child_parms: bool = ...,
    ) -> None: ...
    def execute(self, target_node: hou.VopNode, input_idx: int | str) -> tuple[hou.VopNode, ...]: ...
    def _executeEffect(
        self,
        target_node: hou.VopNode,
        input_index_or_name: int | str,
        mix_with_existing_type: str | None = ...,
        mix_node_input: int | str | None = ...,
        replace_existing: bool = ...,
        parm_gen_type: hou.EnumValue[hou.vopParmGenType] | None = ...,
        output_index_or_name: int | str = ...,
    ) -> tuple[hou.VopNode, ...]: ...
    def supportsDataType(self, data_type: str) -> bool: ...
    def __repr__(self) -> str: ...

vex_effects: dict[str, list[VopEffect]]
mtlx_effects: dict[str, list[VopEffect]]
effects_menus: dict[str, dict[str, list[VopEffect]]]

def generateMenuItems(kwargs: _VopFxMenuKwargs, submenu_name: str) -> list[str]: ...
def executeMenuAction(kwargs: _VopFxMenuActionKwargs, submenu_name: str) -> None: ...
def canCreateSubnetInput(kwargs: _VopFxMenuKwargs) -> bool: ...
def deleteInputNodes(kwargs: _VopFxMenuKwargs) -> None: ...
