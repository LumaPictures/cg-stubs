from collections.abc import Generator, Mapping
from typing import TypeVar, overload

import EC2
import hou
from typing_extensions import TypedDict

# Closed, so that they are JSON (houtypes.JSONLike), which is how they are saved.
class _FileInfo(TypedDict, closed=True):
    path: str
    size: int
    checksum: str

# A cloud render project's parameters, as _computeProjectParms builds them and they are
# saved to the ROP and the remote machine.
class _ProjectParms(TypedDict, closed=True):
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

_T = TypeVar("_T")

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

SUPPORTED_INSTANCE_TYPES: tuple[EC2InstanceType, EC2InstanceType, EC2InstanceType, EC2InstanceType, EC2InstanceType, EC2InstanceType, EC2InstanceType, EC2InstanceType, EC2InstanceType]
SUPPORTED_INSTANCE_TYPE_MODELS: Generator[str, None, None]
DEFAULT_INSTANCE_TYPE_MODEL: str
SUPPORTED_REGIONS: tuple[EC2Region, EC2Region, EC2Region, EC2Region, EC2Region]
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
BASE_IN_CLOUD_API_URL: str

def setAccessKeyAndGetError(access_key_id: str, secret_access_key: str, cloud_region: str) -> str | None: ...
def getAWSKey(cloud_region: str) -> tuple[str | None, str | None]: ...

class CloudOperationFailed(Exception): ...

class AWSConnection:
    cloud_region: str
    aws_connection: EC2.AWSAuthConnection
    def __init__(self, cloud_region: str) -> None: ...
    def getSSHKeyName(self) -> str: ...
    def getSSHKeyPath(self) -> str: ...
    @classmethod
    def getErrorType(cls, response: EC2.Response[_T]) -> str: ...

def getAWSConnection(cloud_region: str) -> AWSConnection | None: ...
@overload
def loadAWSFile(file_name: str, default_value: None = ...) -> str | None: ...
@overload
def loadAWSFile(file_name: str, default_value: _T) -> str | _T: ...
def getDetectedEC2Region() -> str | None: ...
def getCachedDetectedEC2Region() -> str | None: ...
def forceEC2RegionDetection() -> str | None: ...
def instanceIsRunningSESIImage() -> bool: ...
def instanceLicenseCategory() -> str: ...
def showSetUpCloudDialogWithPassphrasePrompt() -> bool: ...
def showSetUpCloudDialog() -> hou.Dialog: ...
def loadReceiveEmailAndAddress() -> tuple[bool, str]: ...
def preFlightScene() -> None: ...
def getCachedProjectParmsFromRop(rop_node: hou.OpNode) -> _ProjectParms | None: ...
def saveProjectParmsToRop(rop_node: hou.OpNode, project_parms: _ProjectParms) -> None: ...
def showFileReferenceDialog(
    rop_node: hou.RopNode, project_name: str, project_dir_variable: str, num_cloud_machines: int, machine_type: str
) -> None: ...
def selectProjectParmsForCloudRender(rop_node: hou.RopNode, num_cloud_machines: int, machine_type: str) -> None: ...
