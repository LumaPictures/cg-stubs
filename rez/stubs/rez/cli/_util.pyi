from _typeshed import Incomplete
from argparse import ArgumentParser, _SubParsersAction
from typing import Any

subcommands: dict[str, dict[str, Any]]

def load_plugin_cmd():
    '''Load subcommand from command type plugin

    The command type plugin module should have attribute `command_behavior`,
    and the value must be a dict if provided. For example:

        # in your command plugin module
        command_behavior = {
            "hidden": False,   # (bool): default False
            "arg_mode": None,  #  (str): "passthrough", "grouped", default None
        }

    If the attribute not present, default behavior will be given.

    '''

class LazySubParsersAction(_SubParsersAction):
    """Argparse Action which calls the `setup_subparser` function provided to
    `LazyArgumentParser`.
    """
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None): ...
    _choices_actions: Incomplete
    def _setup_subparser(self, parser_name, parser) -> None: ...
    def _find_choice_action(self, parser_name): ...

class LazyArgumentParser(ArgumentParser):
    """
    ArgumentParser sub-class which accepts an additional `setup_subparser`
    argument for lazy setup of sub-parsers.

    `setup_subparser` is passed 'parser_name', 'parser', and can return a help
    string.
    """
    setup_subparser: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def format_help(self):
        """Sets up all sub-parsers when help is requested."""
    def _setup_all_subparsers(self) -> None:
        """Sets up all sub-parsers on demand."""

_handled_int: bool
_handled_term: bool

def _env_var_true(name) -> bool: ...
def print_items(items, stream=...) -> None: ...
def sigbase_handler(signum, frame) -> None: ...
def sigint_handler(signum, frame) -> None:
    """Exit gracefully on ctrl-C."""
def sigterm_handler(signum, frame) -> None:
    """Exit gracefully on terminate."""
