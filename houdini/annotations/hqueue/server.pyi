import decimal
import xmlrpc.client
from collections.abc import Sequence
from typing import TypeAlias

from typing_extensions import Required, TypedDict

# What a call to the HQueue server returns: its ServerProxy keeps xmlrpc's defaults, so dates and
# binary data come back as DateTime and Binary.
_XMLRPCValue: TypeAlias = bool | int | float | str | decimal.Decimal | xmlrpc.client.DateTime | xmlrpc.client.Binary | list["_XMLRPCValue"] | dict[str, "_XMLRPCValue"] | None

class _JobCondition(TypedDict):
    type: str
    name: str
    op: str
    value: str

class _JobSpec(TypedDict, total=False):
    """An HQueue job specification (see HQueue's help, `jobdetails#properties`)."""

    name: Required[str]
    children: "Sequence[_JobSpec]"
    childrenIds: Sequence[int]
    parentIds: Sequence[int]
    command: str
    conditions: Sequence[_JobCondition]
    cpus: int
    description: str
    # hqrop.sendJob() takes the reasons as a list of placeholders, and joins them for the server.
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

def connection() -> xmlrpc.client.ServerProxy: ...
def getJobInfo(job_id: int | None, attribs: list[str] | tuple[str, ...] | None = ...) -> _JobInfo: ...
def getJobCPUAndTagInfo(job_id: int | None = ...) -> _JobCPUAndTagInfo: ...
def getParentJobID() -> int | None: ...
def submitJobs(job_specs: _JobSpec | list[_JobSpec] | tuple[_JobSpec, ...]) -> list[int]: ...
def updateJobName(job_id: int, new_name: str) -> None: ...
