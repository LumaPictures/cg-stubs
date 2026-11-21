import hjsonrpc
import hutil.enum
from collections.abc import Sequence
from hutil.enum import _EnumeratedValue
from typing import TypedDict

class _ChangedFrames(TypedDict):
    reload_project_list: bool
    frames: list[tuple[int, int, float]]
    seconds_left: int

HQUEUE_PORT: int
RenderStatuses: hutil.enum.Enumeration

def getConnection(machine_name: str, port: int | None = None) -> hjsonrpc.ServiceProxy | None:
    """Return a connection to the render tracker's RPC server.

    This function is called by users of this module, not by the render tracker
    process.

    Return None if the render tracker is not running.  May return a cached
    cached connection from the previous successful call.
    """
def applyProjectNameFormula(user: str, local_hip_path: str) -> str:
    """Apply the formula to generate a project name.

    Note that this formula does not guarantee that the project name is unique.
    To get a unique name, call suggestInactiveProjectName on the active
    render tracker.
    """

class Frame:
    """A frame in a render project.
    
    A Frame represents the current state and log of notable events for one
    frame in a render.
    """
    project: Project
    number: int
    job_id: str | None
    last_event_id: int
    status: _EnumeratedValue
    render_start_time: float | None
    image_path: str | None
    fraction_complete: float
    log: list[tuple[float, str]]
    error_message: str
    def __init__(self, project: Project, number: int, job_id: str | None) -> None:
        """'project' is a Project object, 'number' is an integer for the frame
           number, and 'job_id' is the HQueue job id.  Initially, the job
           id is the one used to generate IFds, but it will later change to
           the job used to render the individual frame.
        """
    def setRenderFraction(self, fraction: float) -> None:
        """Record how complete the render is.
        
        The fraction is a float from 0.0 to 1.0.
        """
    def setDownloadFraction(self, fraction: float) -> None:
        """Record how complete the download is.
        
        The fraction is a float from 0.0 to 1.0.
        """
    def setStatus(self, status: _EnumeratedValue) -> None:
        """Change the status, logging an appropriate event."""
    def setErrorMessage(self, error_message: str) -> None:
        """Mark this frame as having generated an error."""

class Project:
    """A render project.
    
    A Project contains one or more frames and is identified by a unique
    name.
    """
    rpc_service: RPCService
    name: str
    frame_numbers: Sequence[int]
    generate_ifds: bool
    job_id: str
    last_event_id: int
    frames: dict[int, Frame]
    def __init__(self, rpc_service: RPCService, name: str, frame_numbers: Sequence[int], generate_ifds: bool, job_id: str) -> None: ...
    def incrementAndGetLastEventId(self) -> int: ...
    def getChangedFrames(self, since_event_id: int) -> list[Frame]: ...
    def isDone(self) -> bool: ...

class RPCService:
    projects: dict[str, Project]
    last_event_id: int
    last_project_set_event_id: int
    def __init__(self) -> None: ...
    def incrementAndGetLastEventId(self) -> int: ...
    @hjsonrpc.rpcMethod
    def isRunning(self) -> bool:
        """Return whether or not the RPC server is running.
        
        The caller can check if this server is running by creating an RPC
        connection to it, calling a function, and catching a socket.error
        exception.  This is the recommended function to call.
           
        Note that the dummy connection returned from hqlib.getRenderTrackerRPC
        implements this function and returns False, so you can use this
        function to differentiate between a real render tracker and a dummy
        one.
        """
    @hjsonrpc.rpcMethod
    def getAllProjects(self) -> list[str]:
        """Return a sorted list of all project names.
        
        Note that some of these projects may have completed.
        """
    @hjsonrpc.rpcMethod
    def doesProjectGenerateIFDs(self, project_name: str) -> bool:
        """Return True if the project generates IFDs before rendering.

        Return False if the given project name is not registered
        with the render tracker.
        """
    @hjsonrpc.rpcMethod
    def removeProject(self, project_name: str) -> None: ...
    @hjsonrpc.rpcMethod
    def suggestInactiveProjectName(self, requested_project_name: str) -> str:
        """Return a name for a project that isn't being rendered.

        If the requested name is available, it is returned.
        """
    @hjsonrpc.rpcMethod
    def startedRenderProject(self, project_name: str, frame_numbers: Sequence[int], generate_ifds: bool, job_id: str) -> None:
        """Record that a project to render frames has started.
        
        It is up to the caller to make sure any previous project with this
        name has completed.  We blow away the old project and create a new
        one.

        job_id -- either for the job generating ifds or for the job that will
            submit the jobs to render directly from the hip files
        """
    @hjsonrpc.rpcMethod
    def isProjectRunning(self, project_name: str) -> bool:
        """Return whether the project name is valid and it is still running."""
    @hjsonrpc.rpcMethod
    def isProjectDone(self, project_name: str) -> bool:
        """Return whether all frames in the project are done.  The name must be
        for a project that exists.
        """
    @hjsonrpc.rpcMethod
    def setFrameError(self, project_name: str, frame_number: int, error_message: str) -> None:
        """Set an error message for a frame."""
    @hjsonrpc.rpcMethod
    def setProjectError(self, project_name: str, error_message: str) -> None:
        """Set an error message for all frames in the project."""
    @hjsonrpc.rpcMethod
    def startedGeneratingFrameIFD(self, project_name: str, frame_number: int) -> None:
        """Record that an IFD is being generated for a frame."""
    @hjsonrpc.rpcMethod
    def endedGeneratingFrameIFD(self, project_name: str, frame_number: int) -> None:
        """Record that an IFD is finished being generated for a frame."""
    @hjsonrpc.rpcMethod
    def startedFrameRender(self, project_name: str, frame_number: int, job_id: str, image_path: str) -> None:
        """Record a frame is starting to be rendered.
        
        job_id -- for the HQueue job rendering the frame
        image_path -- the full path on the server to the output image
        """
    @hjsonrpc.rpcMethod
    def setFrameRenderFraction(self, project_name: str, frame_number: int, fraction: float) -> None:
        """Set the fraction completed for a frame being rendered."""
    @hjsonrpc.rpcMethod
    def setFrameDownloadFraction(self, project_name: str, frame_number: int, fraction: float) -> None:
        """Set the fraction completed for a frame being downloaded."""
    @hjsonrpc.rpcMethod
    def getImagePath(self, project_name: str, frame_number: int) -> str | None:
        """Return the path to the output image, or None if it is not set."""
    @hjsonrpc.rpcMethod
    def getFrameJobID(self, project_name: str, frame_number: int) -> str | None:
        """Return the HQueue job id for a frame.

        Note that we update this job id as frame-specific jobs are started.
        """
    @hjsonrpc.rpcMethod
    def getAllFramesInfo(self, project_name: str) -> list[tuple[int, int, float]]:
        """Return a list of 3-tuples containing the frame number, status,
        and fraction complete.

        Note that we use a more compact representation for the frame states by
        returning the index of the enumeration value.  You can index into the
        enumeration to get the enumerated value back.
        """
    @hjsonrpc.rpcMethod
    def getFrameLog(self, project_name: str, frame_number: int) -> list[tuple[float, str]] | None:
        """Return the message log for a particular frame."""
    @hjsonrpc.rpcMethod
    def getChangedFrames(self, project_name: str, since_event_id: int) -> tuple[_ChangedFrames, int]:
        """Return information about the frames that have changed since a
        particular event id.

        Return a dictionary containing the changes and a new event id to
        pass in to the next call to this function.
        
        The caller can pass in 0 for 'since_event_id' to get all the frames.
        """
    @hjsonrpc.rpcMethod
    def getEstimatedRenderSecondsLeft(self, project_name: str) -> float: ...

def start(debug: bool, verbose: bool) -> None: ...
def startWithSysArgs() -> None: ...
