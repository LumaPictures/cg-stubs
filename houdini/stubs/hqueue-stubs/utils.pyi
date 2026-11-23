import subprocess
from collections.abc import Callable as Callable, Iterable
from houtypes import JSONValue
from hqueue.server import _JobSpec

def runJob(function: Callable[[], object]) -> None:
    """Main entry point for running an HQueue job.
        
    Call the given function and handle any raised exceptions.
    Exits the application when this function completes.
    """
def logInfo(msg: str) -> None:
    """Log the specified message."""
def logWarning(msg: str) -> None:
    """Log the specified warning message."""
def logProgress(progress_pct: float) -> None:
    """Log the job's reported progress percentage."""
def logSubprocessOutput(pipe: subprocess.Popen[str]) -> str:
    """Log the output of a spawned subprocess.

    The output is retrieved from the given subprocess pipe.
    This function returns when the subprocess exits.
    This function returns the complete subprocess output.
    """
def failWithError(msg: str) -> None:
    """Print the specified message to stderr and then exit the process
       with a non-zero error code."""
def getJobArgs(args: Iterable[str]) -> dict[str, JSONValue]:
    """Scans the job environment for the given list of arguments
    and returns a dictionary mapping argument names to their values.

    If an argument does not exist in the environment then an error
    is raised and the job fails.
    """
def replaceWithHQROOT(file_path: str) -> str:
    """Replace the beginning of the given path with $HQROOT.
    
    If the path is not under HQ's shared network file system return the
    original path.
    """
def replaceWithEnvVar(env: str, file_path: str) -> str:
    """Replace the beginning of the given path with the environment variable 
    for the matching shared folder path.
    
    If the path is not under HQ's shared network file system, return the 
    original path.
    """
def setPreservedEnvVar(name: str, value: str) -> None:
    """Set an environment variable that will be preserved in child jobs."""
def updateJobEnvWithPreservedVars(job_spec: _JobSpec) -> None:
    """Update a job spec to set environment variables that are to be preserved.

    The variables to preserve are in the HQ_PRESERVE_ENV_VARS environment
    variable in a comma-separated list, and HQ_PRESERVE_ENV_VARS is not
    explicitly in this list.
    """
