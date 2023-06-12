# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import MachineInfo.KatanaInfo as Katana
import MachineInfo.KatanaInfo as KatanaInfo
import MachineInfo.MachineInfo as MachineInfo
from MachineInfo.MachineInfo import GetFreeSpaceB as GetFreeSpaceB, GetNumberOfProcessors as GetNumberOfProcessors, GetTotalMemoryKB as GetTotalMemoryKB, GetUsedSpaceB as GetUsedSpaceB
