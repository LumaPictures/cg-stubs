import _substance_painter.async_utils
import dataclasses

@dataclasses.dataclass(frozen=True)
class StopSource:
    """
    An object that can be used to cancel an asynchronous computation.
    """
    stop_source: _substance_painter.async_utils.StopSource
    def __bool__(self) -> bool: ...
    def request_stop(self) -> bool:
        """
        Makes a top request.

        Returns:
            bool: True if the stop request was possible.
        """
    def stop_requested(self) -> bool:
        """
        Check if a stop request as been made.

        Returns:
            bool: True if a stop request has been made.
        """
