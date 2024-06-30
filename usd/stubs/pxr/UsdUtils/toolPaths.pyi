# mypy: disable-error-code="misc, override, no-redef"

def FindUsdBinary(name):
    """Returns the full path to the named executable if it can be found, or
        None if the executable cannot be located. This first searches in PATH, and
        if the executable is not found, it then searches in the parent directory
        of the current process, as identified by sys.argv[0].

        On Windows, this function searches for both name.EXE and name.CMD to
        ensure that CMD-wrapped executables are located if they exist.
    """
