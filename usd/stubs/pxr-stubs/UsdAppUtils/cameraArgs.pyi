# mypy: disable-error-code="misc, override, no-redef"

from _typeshed import Incomplete

def AddCmdlineArgs(argsParser, defaultValue: Incomplete | None = ..., altHelpText: str = ...):
    """
    Adds camera-related command line arguments to argsParser.

    The resulting 'camera' argument will be an Sdf.Path. If no value is given
    and defaultValue is not overridden, 'camera' will be a single-element path
    containing the primary camera name.
    """
