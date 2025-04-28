from _typeshed import Incomplete
from rez.config import config as config

class Command:
    '''An interface for registering custom Rez subcommand

    To register plugin and expose subcommand, the plugin module..

    * MUST have a module-level docstring (used as the command help)
    * MUST provide a ``setup_parser()`` function
    * MUST provide a ``command()`` function
    * MUST provide a ``register_plugin()`` function
    * SHOULD have a module-level attribute ``command_behavior``

    For example, a plugin named \'foo\' and this is the ``foo.py``:

    .. code-block:: python

        """
        The docstring for command help, this is required.
        """
        from rez.command import Command

        command_behavior = {
            "hidden": False,   # optional: bool
            "arg_mode": None,  # optional: None, "passthrough", "grouped"
        }

        def setup_parser(parser, completions=False):
            parser.add_argument("--hello", ...)

        def command(opts, parser=None, extra_arg_groups=None):
            if opts.hello:
                print("world")

        class CommandFoo(Command):
            schema_dict = {}

            @classmethod
            def name(cls):
                return "foo"

        def register_plugin():
            return CommandFoo

    '''
    type_settings: Incomplete
    settings: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def name(cls) -> str:
        """Return the name of the Command and rez-subcommand."""
