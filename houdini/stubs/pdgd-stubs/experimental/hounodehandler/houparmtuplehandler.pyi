import _pdgd
import hou
import pdgd.util
from _pdgd import _PythonValue
from collections.abc import Sequence

class HouParmTupleHandler(pdgd.util.SimpleHandler):
    """
    Provides access to hou parm data and operations
    """
    parmTuple: hou.ParmTuple
    def __init__(self, handler: _pdgd.SubscriptionHandler, parmTuple: hou.ParmTuple) -> None:
        """
        Initialize some values
        """
    def update(self) -> None: ...
    def updateRawValue(self) -> None: ...
    def setRawValue(self, params: Sequence[_PythonValue]) -> None: ...
    def pressButton(self, params: _PythonValue) -> None: ...
