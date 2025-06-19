from _typeshed import Incomplete

def warn(message, category, pre_formatted: bool = False, stacklevel: int = 1, filename: Incomplete | None = None, **kwargs) -> None:
    """
    Wrapper around warnings.warn that allows to pass a pre-formatter
    warning message. This allows to warn about things that aren't coming
    from python files, like environment variables, etc.
    """

class RezDeprecationWarning(DeprecationWarning): ...
