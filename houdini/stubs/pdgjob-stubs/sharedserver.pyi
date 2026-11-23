import logging
import subprocess
from collections.abc import Mapping
from pdgjob.pdgcmd import getHostname as getHostname, reportServerStarted as reportServerStarted

logger: logging.Logger

def startSharedServer(*argv: str) -> subprocess.Popen[bytes]:
    """
    Start a server using argv
    """
def sanitizeEnvVars() -> None:
    """Clear out Houdini-related paths from PATH and LD_LIBRARY_PATH."""
def waitOnPort(hostname: str, port: int, proto_type: str, timeout: float, proc: subprocess.Popen[bytes], log_fname: str) -> bool: ...
def findFreePort(hostname: str, port: int) -> int:
    """
    Find a port that's not taken
    Note: when port == 0, we are asking the system to grab
    a random free port.  Otherwise we are searching for one
    from the given range
    """
def shutdownServer(info: Mapping[str, object], timeout: float = 30) -> bool:
    """
    Shutdown the remote server.
    """
def pingServer(hostname: str, server_port: int, socktimeout: float | None) -> None:
    """
    Raises an exception if the server cannot be reached.
    """
def isAddressLoopback(host_address: str) -> bool:
    """
    Return True if address is a loopback
    """
def waitOnConnectionFile(connectionfile_local: str, timeout: float) -> int | None:
    """
    Wait for port number to be written to the given file within
    the given number of seconds timeout.  Return the port number or None
    """
def main() -> None: ...
