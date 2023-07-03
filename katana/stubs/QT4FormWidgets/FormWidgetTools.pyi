# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.Conditional as Conditional
from QT4FormWidgets.FWidget import FBoxLayout as FBoxLayout, FButton as FButton, FDisclosureTriangle as FDisclosureTriangle, FLabel as FLabel, FLockIcon as FLockIcon, FMenu as FMenu, FPixmap as FPixmap, FSpacer as FSpacer, FStateBadge as FStateBadge, FSvgIcon as FSvgIcon, FToggleStateBadge as FToggleStateBadge, FWidget as FWidget
from QT4FormWidgets.MultiStateBadge import MultiStateBadge as MultiStateBadge, ToggleStateBadge as ToggleStateBadge, ToggleValuePolicyState as ToggleValuePolicyState
from _typeshed import Incomplete

def DeepPolicyCompare(a, b): ...
def GetTopologyDifferences(formWidgets, valuePolicies): ...
def PaintFormWidgetFrame(painter, width, topHeight, fullHeight, opened, frameWidth: Incomplete | None = ...): ...