# mypy: disable-error-code="misc, override, no-redef"

def AddCmdlineArgs(argsParser, altHelpText: str = ...):
    """
    Adds Hydra renderer-related command line arguments to argsParser.

    The resulting 'rendererPlugin' argument will be a _RendererPlugin instance
    representing one of the available Hydra renderer plugins.
    """
def GetAllPluginArguments():
    """
    Returns argument strings for all the renderer plugins available.
    """
def GetPluginIdFromArgument(argumentString):
    """
    Returns plugin id, if found, for the passed in argument string.

    Valid argument strings are returned by GetAllPluginArguments().
    """
