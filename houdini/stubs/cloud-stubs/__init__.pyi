import EC2
import hou
import typing
from collections.abc import Generator, Mapping as Mapping
from typing import Any
from typing_extensions import TypedDict

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class _FileInfo(TypedDict, closed=True):  # type: ignore[call-arg]
    path: str
    size: int
    checksum: str

class _ProjectParms(TypedDict, closed=True):  # type: ignore[call-arg]
    version: int
    files: list[_FileInfo] | tuple[_FileInfo, ...]
    houdini_version: str
    license_category: str
    cloud_region: str
    project_name: str
    relative_hip_path: str
    rop_node_path: str
    relative_otl_dirs: list[str]
    relative_vex_dirs: list[str]
    environment: dict[str, str]

class EC2InstanceType:
    model: str
    ec2_units: float
    num_cpus: int
    memory: float
    def __init__(self, model: str, ec2_units: float, num_cpus: int, memory: float) -> None: ...
    def description(self) -> str: ...

class EC2Region:
    code: str
    name: str
    location: tuple[float, float]
    def __init__(self, code: str, name: str, location: tuple[float, float]) -> None: ...

SUPPORTED_INSTANCE_TYPES: tuple[EC2InstanceType, ...]
SUPPORTED_INSTANCE_TYPE_MODELS: Generator[str, None, None]
DEFAULT_INSTANCE_TYPE_MODEL: str
SUPPORTED_REGIONS: tuple[EC2Region, ...]
SUPPORTED_REGION_CODES: Generator[str, None, None]
DEFAULT_REGION_CODE: str
ACCESS_KEY_ID_FILE_NAME: str
SECRET_ACCESS_KEY_FILE_NAME: str
ENCRYPTED_SECRET_ACCESS_KEY_FILE_NAME: str
EMAIL_NOTIFICATION_FILE_NAME: str
AMAZON_ACCOUNT_URL: str
AMAZON_SIGNUP_URL: str
HOUDINI_CLOUD_FAQ_URL: str
SESI_AWS_ACCOUNT_ID: str
SESI_AWS_PRODUCT_CODE: str
SESI_AMI_NAME_PATTERN: str
SESI_IAM_ROLE_NAME: str
SESI_IAM_INSTANCE_PROFILE_NAME: str
SESI_IAM_TRUST_POLICY: str
AWS_EC2_FULL_ACCESS_POLICY_ARN: str
SUBMISSION_ABORTED_MESSAGE: str

def setAccessKeyAndGetError(access_key_id: str, secret_access_key: str, cloud_region: str) -> str | None:
    """Set the access key and return an error message if it's not valid, or
    None if it is.

    This function sets the global variables _access_key_id and
    _secret_access_key.  It is called from cloudsubmit when it reads the
    (decrypted) secret access key from a temporary file.
    """
def getAWSKey(cloud_region: str) -> tuple[str | None, str | None]:
    """Return the access key id and secret access key if possible."""

class CloudOperationFailed(Exception): ...

class AWSConnection:
    """An Amazon Web Services connection.  Use getAWSConnection to get an
    instance of this class.
    """
    cloud_region: str
    aws_connection: EC2.AWSAuthConnection
    def __init__(self, cloud_region: str) -> None: ...
    def getSSHKeyName(self) -> str: ...
    def getSSHKeyPath(self) -> str: ...
    @classmethod
    def getErrorType(cls, response: EC2.Response[Any]) -> str: ...

def getAWSConnection(cloud_region: str) -> AWSConnection | None:
    """Return an AWSConnection that has been tested to be valid, or None if the
    Amazon Web Services key could not be read or the key is not valid.
    """
@typing.overload
def loadAWSFile(file_name: str, default_value: None = ...) -> str | None: ...
@typing.overload
def loadAWSFile(file_name: str, default_value: _T) -> str | _T: ...
def getDetectedEC2Region() -> str | None:
    """Return the detected region, using the cached version if it exists.
    Returns None if nothing could be detected."""
def getCachedDetectedEC2Region() -> str | None:
    """Return the cached region that was detected, or None if nothing was
    cached.

    This function is also called from the rop.
    """
def forceEC2RegionDetection() -> str | None:
    """Force detection of the region, bypassing the cache.  Returns None if
    the region could not be detected.
    """

BASE_IN_CLOUD_API_URL: str

def instanceIsRunningSESIImage() -> bool: ...
def instanceLicenseCategory() -> str: ...
def showSetUpCloudDialogWithPassphrasePrompt() -> bool: ...
def showSetUpCloudDialog() -> hou.Dialog: ...
def loadReceiveEmailAndAddress() -> tuple[bool, str]:
    """Load the setting that says what email address to send notifications to.

    Return a tuple of two values: the first indicates if receiving emails is
    enabled, and the second indicates which email address to send to.
    """
def preFlightScene() -> None: ...
def getCachedProjectParmsFromRop(rop_node: hou.OpNode) -> _ProjectParms | None: ...
def saveProjectParmsToRop(rop_node: hou.OpNode, project_parms: _ProjectParms) -> None: ...
def showFileReferenceDialog(rop_node: hou.RopNode, project_name: str, project_dir_variable: str, num_cloud_machines: int, machine_type: str) -> None: ...
def selectProjectParmsForCloudRender(rop_node: hou.RopNode, num_cloud_machines: int, machine_type: str) -> None: ...
