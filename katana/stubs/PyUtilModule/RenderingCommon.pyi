# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import FnAttribute

_virtualCameraAttributes: None
kVirtualCameraSceneGraphLocation: str

def GetVirtualCameraAttributes() -> FnAttribute.GroupAttribute | None: ...
def SetVirtualCameraAttributes(attributes: FnAttribute.GroupAttribute | None): ...