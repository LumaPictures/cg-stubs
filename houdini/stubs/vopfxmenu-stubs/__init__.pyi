import hou
from collections.abc import Sequence
from typing import Required
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
    def __init__(self, node_type: str | None = None, preset: str | None = None, label: str | None = None, data_types: Sequence[str] | None = None, custom_creator: ShaderFxCallbacks | None = None, passthrough_input: int | str | None = None, output: int | str = 0, promote_child_parms: bool = True) -> None:
        """ Describes a Shader Effect

            node_type
                The type of node to create. Inputs of the created node will be
                created recursively using input presets. A named preset may be
                specified using 'preset'

            preset
                The name of the input preset to use. If this is None and node_type
                is specified, the default preset for the node type will be used.

            custom_creator
                A callback to create a custom setup.
        """
    def execute(self, target_node: hou.VopNode, input_idx: int | str) -> tuple[hou.VopNode, ...]: ...
    def _executeEffect(self, target_node: hou.VopNode, input_index_or_name: int | str, mix_with_existing_type: str | None = None, mix_node_input: int | str | None = None, replace_existing: bool = True, parm_gen_type: hou.EnumValue[hou.vopParmGenType] | None = ..., output_index_or_name: int | str = 0) -> tuple[hou.VopNode, ...]:
        """
            mix_with_existing_type
                If this is a node type, any existing node plugged into the input
                will be kept and newly created nodes will be mixed with the original
                input using the node_type specified, i.e. 'multiply', 'colormix', etc.

            parm_gen_type
                Specifies the parmscope to use when creating Parameter VOPs.
        """
    def supportsDataType(self, data_type: str) -> bool: ...

vex_effects: dict[str, list[VopEffect]]
mtlx_effects: dict[str, list[VopEffect]]
effects_menus: dict[str, dict[str, list[VopEffect]]]

def generateMenuItems(kwargs: _VopFxMenuKwargs, submenu_name: str) -> list[str]: ...
def executeMenuAction(kwargs: _VopFxMenuActionKwargs, submenu_name: str) -> None: ...
def canCreateSubnetInput(kwargs: _VopFxMenuKwargs) -> bool: ...
def deleteInputNodes(kwargs: _VopFxMenuKwargs) -> None: ...
