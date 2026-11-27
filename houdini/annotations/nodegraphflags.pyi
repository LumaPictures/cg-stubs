from collections.abc import Sequence

import hou

theRopManagers: tuple[str, str, str, str, str, str, str]
theFlagEnumLookup: dict[str, hou.EnumValue[hou.nodeFlag]]

def getFlagEnumFromIndex(uidata: int) -> hou.EnumValue[hou.nodeFlag] | None: ...
def getFlagForIndex(flagindex: int, node: hou.Node | None = ..., category: hou.NodeTypeCategory | None = ...) -> hou.EnumValue[hou.nodeFlag] | None: ...
def getPureToggleForIndex(flagindex: int, node: hou.Node | None = ..., category: hou.NodeTypeCategory | None = ...) -> bool: ...
def handleFlagClick(
    editor: hou.NetworkEditor,
    items: Sequence[hou.Node],
    flag: hou.EnumValue[hou.nodeFlag] | None,
    uiname: str,
    shift: bool,
    ctrl: bool,
    alt: bool,
    volatile: bool,
    puretoggle: bool,
) -> None: ...
