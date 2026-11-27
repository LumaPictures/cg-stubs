import _pdg
from . import local as local, prtractor as prtractor, pythonscheduler as pythonscheduler, tbdeadline as tbdeadline, tbdeadline_utils as tbdeadline_utils
from pdg.utils.mq import MQUtility as MQUtility

has_tractor: bool
has_deadline: bool
deadline_cmd: str

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
