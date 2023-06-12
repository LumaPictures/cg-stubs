# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute

_virtualCameraAttributes: None
kVirtualCameraSceneGraphLocation: str

def GetVirtualCameraAttributes() -> PyFnAttribute.GroupAttribute | None: ...
def SetVirtualCameraAttributes(attributes: PyFnAttribute.GroupAttribute | None): ...