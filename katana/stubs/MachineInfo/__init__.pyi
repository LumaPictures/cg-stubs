# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from . import KatanaInfo as Katana, KatanaInfo as KatanaInfo, MachineInfo as MachineInfo
from MachineInfo.MachineInfo import GetFreeSpaceB as GetFreeSpaceB, GetNumberOfProcessors as GetNumberOfProcessors, GetTotalMemoryKB as GetTotalMemoryKB, GetUsedSpaceB as GetUsedSpaceB
from typing import Set, Tuple
