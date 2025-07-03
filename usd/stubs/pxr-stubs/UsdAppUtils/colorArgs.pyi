def AddCmdlineArgs(argsParser, defaultValue: str = 'sRGB', altHelpText: str = '') -> None:
    """
    Adds color-related command line arguments to argsParser.

    The resulting 'colorCorrectionMode' argument will be a Python string.
    """
