import xmlrpc.client
from collections.abc import Sequence
from typing_extensions import Required, TypedDict

from typing import TypeAlias
from typing import TypeAlias
import decimal
_XMLRPCValue: TypeAlias = bool | int | float | str | decimal.Decimal | xmlrpc.client.DateTime | xmlrpc.client.Binary | list['_XMLRPCValue'] | dict[str, '_XMLRPCValue'] | None
class _JobCondition(TypedDict):
    type: str
    name: str
    op: str
    value: str

class _JobSpec(TypedDict, total=False):
    """An HQueue job specification (see HQueue's help, `jobdetails#properties`)."""
    name: Required[str]
    children: Sequence[_JobSpec]
    childrenIds: Sequence[int]
    parentIds: Sequence[int]
    command: str
    conditions: Sequence[_JobCondition]
    cpus: int
    description: str
    emailReasons: str | list[str]
    emailTo: str
    environment: dict[str, str]
    host: str
    hostgroup: str
    inherit_conditions: bool
    onCancel: str
    onError: str
    onChildError: str
    onReschedule: str
    onSuccess: str
    maxHosts: int
    maxTime: int
    minHosts: int
    priority: int
    shell: str
    submittedBy: str
    tags: Sequence[str]
    triesLeft: int | None
    triesDifferentClient: bool | None
    resources: dict[str, int]
    combineOutput: bool

class _JobInfo(TypedDict, total=False, extra_items=_XMLRPCValue):  # type: ignore[call-arg]
    """A job's attributes, as the HQueue server's `getJob()` returns them."""
    id: int
    name: str
    priority: int
    cpus: int
    tags: list[str]
    parents: list[int]
    children: list[int]
    conditions: list[_JobCondition]
    status: str
    uiStatus: str
    progress: float
    overallProgress: float
    triesLeft: int
    resources: dict[str, int] | None
    latestNote: str
    waitingFor: str
    threadId: int | None
    showBlockedClientsWarning: bool

class _JobCPUAndTagInfo(TypedDict, extra_items=_XMLRPCValue):  # type: ignore[call-arg]
    cpus: int
    tags: list[str]

def connection() -> xmlrpc.client.ServerProxy:
    """Return a proxy connection to the HQueue server."""
def getJobInfo(job_id: int | None, attribs: list[str] | tuple[str, ...] | None = None) -> _JobInfo:
    """Return information on the requested attributes for the specified job.

    Attribute information is returned as a dictionary.

    `attribs` can be a list of attribute names.
    If `attribs` is None then all attribute information is returned.

    If `job_id` is None then information on the current job running
    this process is returned.
    """
def getJobCPUAndTagInfo(job_id: int | None = None) -> _JobCPUAndTagInfo:
    """Return the CPU and tag info for the specified job.
        
    If `job_id` is None then return info on the current job running
    this process.
    """
def getParentJobID() -> int | None:
    """Return current job's parent job id.

    The current job is the one running this process.
    If the current job has multiple parents then return the first parent.
    """
def submitJobs(job_specs: _JobSpec | list[_JobSpec] | tuple[_JobSpec, ...]) -> list[int]:
    """Submit jobs to the HQueue server.
    
    Return a sequence of job ids for the new job(s) or None if the submission
    failed.

    `job_specs` can either be a dictionary representing a single job
    specification or a tuple/list of dictionary objects representing
    multiple job specifications.
    """
def updateJobName(job_id: int, new_name: str) -> None:
    """Updates the name of the job associated
    with the given job_id.
    """
