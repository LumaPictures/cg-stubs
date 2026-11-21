from collections.abc import MutableMapping
import _pdgd
from _pdgd import _PythonValue

COMMAND_TIME_OUT: int

class CommandTimeOutException(Exception): ...

def command_callback(
    result_object: MutableMapping[str, _pdgd.ObjectProperty | None],
    command_result: _pdgd.ObjectProperty,
) -> None: ...
def callback(result: _pdgd.ObjectProperty) -> None: ...
def send_command_wait_result(
    data_layer: _pdgd.DataLayerInterface, command_name: str, params: _PythonValue, path: str
) -> _PythonValue: ...
