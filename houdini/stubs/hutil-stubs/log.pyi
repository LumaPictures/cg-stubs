# Houdini stubs generated from Houdini 22.0.466

import logging

def createLogger(debug: bool, verbose: bool, name: str, log_file_name: str) -> logging.Logger:
    """Create and return a logger, and also redirect stdout and stderr to
    the logger.  If debug is True, the logging level is set to logging.DEBUG;
    otherwise it is set to logging.INFO.  If verbose is True, log output is
    also sent to stdout.
    """
