from _typeshed import Incomplete
from argparse import _StoreTrueAction
from rez import __version__ as __version__, module_root_path as module_root_path
from rez.cli._util import LazyArgumentParser as LazyArgumentParser, _env_var_true as _env_var_true, subcommands as subcommands
from rez.exceptions import RezError as RezError, RezSystemError as RezSystemError, _NeverError as _NeverError
from rez.utils.logging_ import print_error as print_error
from typing import Any

_hyphened_command: bool

def is_hyphened_command(): ...

class SetupRezSubParser:
    """Callback class for lazily setting up rez sub-parsers.
    """
    module_name: Any
    def __init__(self, module_name) -> None: ...
    def __call__(self, parser_name, parser): ...
    def get_module(self): ...

def _add_common_args(parser) -> None: ...

class InfoAction(_StoreTrueAction):
    def __call__(self, parser, args, values, option_string: Incomplete | None = None) -> None: ...

def setup_parser():
    """Create and setup parser for given rez command line interface.

    Returns:
        LazyArgumentParser: Argument parser for rez command.
    """
def run(command: Incomplete | None = None): ...
