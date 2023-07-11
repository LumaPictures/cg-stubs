# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from ViewerAPI.ImplicitOpsManager import ImplicitOpsManager as ImplicitOpsManager
from ViewerAPI.ManipulatorBridge import ManipulatorBridge as ManipulatorBridge
from typing import Set, Tuple

CameraDirtyBits_AllDirty: int
CameraDirtyBits_Clean: int
CameraDirtyBits_DirtyParams: int
kFnViewerDelegateLookThrough: int
kFnViewerDelegatePrimary: int
kFnViewerDelegateSources: int
kFnViewportCameraTypeOrthographic: int
kFnViewportCameraTypePerspective: int
kFnViewportCameraTypeSpherical: int
kFnViewportCameraTypeUnknown: int
kViewportLayerPluginVersion: int
