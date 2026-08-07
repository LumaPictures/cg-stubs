from _substance_painter.logging import PYTHON_CHANNEL as PYTHON_CHANNEL
from _typeshed import Incomplete

INFO: Incomplete
WARNING: Incomplete
ERROR: Incomplete
DBG_INFO: Incomplete
DBG_WARNING: Incomplete
DBG_ERROR: Incomplete

def log(severity, channel: str, message: str):
    """Logs a message with level `severity` on the Substance 3D Painter logger.

    Args:
      severity: the severity level, can be ``INFO``, ``WARNING`` or ``ERROR`` for
          messages relevant to the end user, or ``DBG_INFO``, ``DBG_WARNING`` or
          ``DBG_ERROR`` for messages relevant to the developer.
      channel (str): the channel to log into.  This can be any name allowing to
                     identify the origin of the message, for example the name of
                     your plugin.
      message (str): the message to log.
    """
def info(message: str):
    """Logs a message with level ``INFO`` on the Substance 3D Painter logger.

    Args:
        message (str): The message to log.
    """
def warning(message: str):
    """Logs a message with level ``WARNING`` on the Substance 3D Painter logger.

    Args:
        message (str): The warning message to log.
    """
def error(message: str):
    """Logs a message with level ``ERROR`` on the Substance 3D Painter logger.

    Args:
        message (str): The error message to log.
    """
