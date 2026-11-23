import contextlib
from collections.abc import Generator

def version_info() -> tuple[int, int, int]:
    """
    Get the version_info of Substance 3D Painter. Ie a tuple containing major, minor, patch.

    Returns:
        Tuple[int, int, int]: The major, minor and patch version of Substance 3D Painter.
    """
def version() -> str:
    """
    Get the version of Substance 3D Painter. Do not extract version information out of it,
    rather use :func:`version_info`.

    Returns:
        str: Version of Substance 3D Painter.
    """
def engine_computations_status() -> bool:
    """
    Check whether engine computations are enabled.

    Returns:
        bool: Whether engine computations are enabled.
    """
def enable_engine_computations(enable: bool):
    """
    Enable or disable engine computations.
    """
@contextlib.contextmanager
def disable_engine_computations() -> Generator[None]:
    """
    Context manager to disable engine computations.
    Allows to regroup computation intensive tasks without triggerring the engine so that textures
    are not computed or updated in the layer stack or the viewport.
    This is equivalent to disabling and then reenabling the engine by calling
    :func:`enable_engine_computations`.

    Example:
    ::

        import substance_painter.application as mapplication

        with mapplication.disable_engine_computations():
            # Do some computation intensive tasks
            pass
    """
def close() -> None:
    """
    Close Susbtance 3D Painter.

    Warning:
        Any unsaved data will be lost.
    """
