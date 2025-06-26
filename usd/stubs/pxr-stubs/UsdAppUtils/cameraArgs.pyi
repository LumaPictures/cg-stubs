# mypy: disable-error-code="misc, override, no-redef"

def AddCmdlineArgs(argsParser, defaultValue, altHelpText: str = ...):
    """
    Adds camera-related command line arguments to argsParser.

    The resulting 'camera' argument will be an Sdf.Path. If no value is given
    and defaultValue is not overridden, 'camera' will be a single-element path
    containing the primary camera name.
    """
