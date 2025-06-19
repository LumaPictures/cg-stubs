# mypy: disable-error-code="misc, override, no-redef"

def AddCmdlineArgs(argsParser, defaultValue: str = ..., altHelpText: str = ...):
    """
    Adds color-related command line arguments to argsParser.

    The resulting 'colorCorrectionMode' argument will be a Python string.
    """
