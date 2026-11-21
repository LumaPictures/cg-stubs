# Houdini stubs generated from Houdini 22.0.466

import _pdgd
from _pdgd import _PythonValue
from collections.abc import MutableMapping

class CommandTimeOutException(Exception):
    """ Raised when a command takes too long to complete """

COMMAND_TIME_OUT: int

def command_callback(result_object: MutableMapping[str, _pdgd.ObjectProperty | None], command_result: _pdgd.ObjectProperty) -> None: ...
def callback(result: _pdgd.ObjectProperty) -> None: ...
def send_command_wait_result(data_layer: _pdgd.DataLayerInterface, command_name: str, params: _PythonValue, path: str) -> _PythonValue: ...
