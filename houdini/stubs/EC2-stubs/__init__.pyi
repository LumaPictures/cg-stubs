# Houdini stubs generated from Houdini 22.0.466

import http.client
import typing
from collections.abc import Iterable, MutableMapping, Sequence
from elementtree import ElementTree as ET
from typing import Generic, Literal, TypedDict, Unpack

from typing import TypeVar
from typing import TypeVar
_S = TypeVar('_S')
class _AuthRevokeKwargs(TypedDict, total=False):
    groupName: str
    ipProtocol: str | None
    fromPort: int | str | None
    toPort: int | str | None
    cidrIp: str | None
    sourceSecurityGroupName: str | None
    sourceSecurityGroupOwnerId: str | None

DEFAULT_HOST: str
DEFAULT_IAM_HOST: str
PORTS_BY_SECURITY: dict[bool, int]
API_VERSION: str
IAM_API_VERSION: str
RELEASE_VERSION: str

class AWSAuthConnection:
    """
    Creates an authorized connection to EC2 containing wrappers for
    Query API calls.

    Each API call has a matching method on this class to perform the
    appropriate E2 action.

    @ivar verbose: Verbosity flag, defaults to false.  If set to true,
    some debug information is printed.

    """
    verbose: bool
    aws_access_key_id: str
    aws_secret_access_key: str
    server: str
    iam_server: str
    region: str | None
    connection: http.client.HTTPConnection
    iam_connection: http.client.HTTPConnection
    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str, is_secure: bool = True, server: str = ..., iam_server: str = ..., port: int | None = None, region: str | None = None) -> None: ...
    def pathlist(self, key: str, arr: Iterable[str]) -> dict[str, str]:
        """Converts a key and an array of values into AWS query param format."""
    def allocate_address(self) -> AllocateAddressResponse:
        """Makes an C{AllocateAddress} call.

        """
    def describe_addresses(self, publicIps: Iterable[str] | None = None) -> DescribeAddressesResponse:
        """Makes a C{DescribeAddresses} call.

        @param publicIps: List of addresses to describe.  If empty or
        omitted, all addresses will be described.

        """
    def release_address(self, publicIp: str) -> ReleaseAddressResponse:
        """Makes a C{ReleaseAddress} call.

        @param publicIp: Address to release

        """
    def associate_address(self, publicIp: str, instanceId: str) -> AssociateAddressResponse:
        """Makes an C{AssociateAddress} call.

        @param publicIp: Address to associate
        @param instanceId: Instance to associate address with

        """
    def disassociate_address(self, publicIp: str) -> DisassociateAddressResponse:
        """Makes a C{DisassociateAddress} call.

        @param publicIp: Address to disassociate

        """
    def describe_availability_zones(self, zoneNames: Iterable[str] | None = None) -> DescribeAvailabilityZonesResponse:
        """Makes a C{DescribeAvailabilityZones} call.

        @param zoneNames: List of availability zones to describe.  If
        empty or omitted, all availability zones will be described.

        """
    def register_image(self, imageLocation: str) -> RegisterImageResponse:
        """Makes a C{RegisterImage} call.

        @param imageLocation: The location of the image manifest to
        register in S3.
        
        """
    def describe_images(self, imageIds: Iterable[str] | None = None, owners: Iterable[str] | None = None, executableBy: Iterable[str] | None = None) -> DescribeImagesResponse:
        """Makes a C{DescribeImages} call.

        @param imageIds: List of images to describe.  If empty or omitted, all
        images visible to the user are returned.

        @param owners: List of users to filter returned images by
        owner.  If empty or omitted, no filtering is done.

        @param executableBy: List of users (or user groups) to filter
        returned images by execution permissions.  If empty or
        omitted, no filtering is done.

        """
    def deregister_image(self, imageId: str) -> DeregisterImageResponse:
        """Makes a C{DeregisterImage} call.

        @param imageId: The image id to deregister.

        """
    def create_keypair(self, keyName: str) -> CreateKeyPairResponse:
        """Makes a C{CreateKeypair} call.

        @param keyName: Name for the new keypair.

        """
    def describe_keypairs(self, keyNames: Iterable[str] | None = None) -> DescribeKeyPairsResponse:
        """Makes a C{DescribeKeypairs} call.

        @param keyNames: List of keypairs to describe.  If empty or
        omitted, all keypairs are returned.

        """
    def delete_keypair(self, keyName: str) -> DeleteKeyPairResponse:
        """Makes a C{DeleteKeypair} call.

        @param keyName: Name of keypair to delete.

        """
    def run_instances(self, imageId: str, minCount: int = 1, maxCount: int = 1, keyName: str | None = None, groupIds: Iterable[str] | None = None, userData: str | None = None, base64Encode: bool = True, addressingType: str | None = None, instanceType: str | None = None, availabilityZone: str | None = None, kernelId: str | None = None, ramdiskId: str | None = None, blockDeviceMapping: Iterable[Sequence[str]] | None = None, iamInstanceProfile: str | None = None) -> RunInstancesResponse:
        '''Makes a C{RunInstances} call.

        @param imageId: AMI id to launch instances of.

        @param minCount: Minimum number of instances to launch.  If
        EC2 cannot launch at least this many, the call will fail.

        @param maxCount: Maximum number of instances to launch.  EC2
        will make a best-effort attempt to launch this many instances,
        but will not fail unless fewer than C{minCount} are available.

        @param keyName: Name of keypair to launch instances with.

        @param groupIds: List of security groups to launch instances
        in.

        @param userData: String containing user data to inject into
        launched instances.

        @param base64Encode: Specifies whether C{userData} string
        qshould be base64 encoded.  Defaults to True.

        @param addressingType: Specifies the address scheme to use for
        the instance. The supported (default) type is C{"public"}, or
        C{None} for the default. See the "Instance Addressing" section
        of the latest developer guide for more information.

        @param availabilityZone: Specifies the availability zone to
        launch in.

        @param kernelId: Kernel to launch the instances with.

        @param ramdiskId: Ramdisk to launch the instances with.

        @param blockDeviceMapping: Specifies the virtual block device
        mapping. This parameter is a list of two element lists or
        tuples. The first element is the virtual name and the second
        is the device name.

        @param iamInstanceProfile: The IAM instance profile.  This is used to
        grant the instances permission to access AWS services.

        '''
    def describe_instances(self, instanceIds: Iterable[str] = ...) -> DescribeInstancesResponse:
        """Makes a C{DescribeInstances} call.

        @param instanceIds: List of instances to describe.  If empty
        or omitted, all instances will be returned.

        """
    def describe_instance_attribute(self, instanceId: str, attribute: str) -> DescribeInstanceAttributeResponse:
        """Makes a C{DescribeInstanceAttribute} call.

        @param instanceId: instance to retrieve the attribute from

        @param attribute: Name of attribute to retrieve

        """
    def get_console_output(self, instanceId: str) -> GetConsoleOutputResponse:
        """Makes a C{GetConsoleOutput} call.

        @param instanceId: Instance from which to get console output.

        """
    def reboot_instances(self, instanceIds: Iterable[str]) -> RebootInstancesResponse:
        """Makes a C{RebootInstances} call.

        @param instanceIds: List of instances to reboot.

        """
    def terminate_instances(self, instanceIds: Iterable[str]) -> TerminateInstancesResponse:
        """Makes a C{TerminateInstances} call.

        @param instanceIds: List of instances to terminate.

        """
    def create_securitygroup(self, groupName: str, groupDescription: str) -> CreateSecurityGroupResponse:
        """Makes a C{CreateSecurityGroup} call.

        @param groupName: Name of group to create.

        @param groupDescription: Brief description of security group.

        """
    def describe_securitygroups(self, groupNames: Iterable[str] | None = None) -> DescribeSecurityGroupsResponse:
        """Makes a C{DescribeSecurityGroups} call.

        @param groupNames: List of security groups to describe.  If
        empty or omitted, all security groups will be described.

        """
    def delete_securitygroup(self, groupName: str) -> DeleteSecurityGroupResponse:
        """Makes a C{DeleteSecurityGroup} call.

        @param groupName: Name of security group to delete.

        """
    def authorize(self, *args: str | int | None, **kwargs: Unpack[_AuthRevokeKwargs]) -> AuthorizeSecurityGroupIngressResponse:
        """Makes an C{AuthorizeSecurityGroupIngress} call.

        L{authorize} and L{revoke} share parameter parsing code.
        See L{auth_revoke_impl} for parameters.  Also, see API docs
        for details of valid parameter combinations.

        """
    def revoke(self, *args: str | int | None, **kwargs: Unpack[_AuthRevokeKwargs]) -> RevokeSecurityGroupIngressResponse:
        """Makes an C{RevokeSecurityGroupIngress} call.

        L{authorize} and L{revoke} share parameter parsing code.
        See L{auth_revoke_impl} for parameters.  Also, see API docs
        for details of valid parameter combinations.

        """
    def modify_image_attribute(self, imageId: str, attribute: str, operationType: str, **kwargs: Iterable[str]) -> ModifyImageAttributeResponse:
        """Makes a C{ModifyImageAttribute} call.

        @param imageId: AMI to modify attribute of.

        @param attribute: Name of attribute to modify.

        @param operationType: Operation to perform on attribute.

        @param kwargs: Values for the attribute operation, documented below.

        @kwarg userIds: List of userIds (valid with
        C{'launchPermission'} attribute.)

        @kwarg userGroups: List of userGroups (valid with
        C{'launchPermission'} attribute.)

        """
    def reset_image_attribute(self, imageId: str, attribute: str) -> ResetImageAttributeResponse:
        """Makes a C{ResetImageAttribute} call.

        @param imageId: AMI to reset attribute of.

        @param attribute: Name of attribute to reset.

        """
    def describe_image_attribute(self, imageId: str, attribute: str) -> DescribeImageAttributeResponse:
        """Makes a C{DescribeImageAttribute} call.

        @param imageId: AMI to describe attribute of.

        @param attribute: Name of attribute to describe.

        """
    def auth_revoke_impl(self, groupName: str, ipProtocol: str | None = None, fromPort: int | str | None = None, toPort: int | str | None = None, cidrIp: str | None = None, sourceSecurityGroupName: str | None = None, sourceSecurityGroupOwnerId: str | None = None) -> dict[str, str]:
        """Processes parameters for C{authorize} and C{revoke}.

        @param groupName: Name of security group to modify.

        @param ipProtocol: IP protocol in rule.  Valid vlaues are
        C{'tcp'}, C{'udp'} and C{'icmp'}.

        @param fromPort: Bottom of IP port range in rule.

        @param toPort: Top of IP port range in rule.

        @param cidrIp: CIDR IP range in rule.

        @param sourceSecurityGroupName: Security group name in rule.

        @param sourceSecurityGroupOwnerId: User id of security group
        in rule.

        """
    def confirm_product_instance(self, productCode: str, instanceId: str) -> ConfirmProductInstanceResponse:
        """Makes a C{ConfirmProdcutInstance} call.

        @param productCode: The product code to confirm

        @param instanceId: The instance for which to confirm the product code.
        
        """
    def create_role(self, name: str, policy: str, path: str | None = None) -> CreateRoleResponse:
        """Makes an IAM C{CreateRole} call.

        @param name: The name of the role to create.

        @param policy: String containing the trust relationship policy document
        that grants an entity permission to assume the role.

        @path: The path to the role.
        """
    def attach_role_policy(self, policy_arn: str, role_name: str) -> AttachRolePolicyResponse:
        """Makes an IAM C{AttachRolePolicy} call.

        @param policy_arn: The Amazon Resource Name (ARN).

        @param role_name: The name (friendly name, not ARN) of the role to
        attach the policy to.
        """
    def get_role(self, name: str) -> GetRoleResponse:
        """Makes an IAM C{GetRole} call.

        @param name: The name of the role to get information about.
        """
    def create_instance_profile(self, name: str, path: str | None = None) -> CreateInstanceProfileResponse:
        """Makes an IAM C{CreateInstanceProfile} call.

        @param name: The name of the instance profile to create.

        @path: The path to the instance profile.
        """
    def get_instance_profile(self, name: str) -> GetInstanceProfileResponse:
        """Makes an IAM C{GetInstanceProfile} call.

        @param name: The name of the instance profile to get information about.
        """
    def add_role_to_instance_profile(self, instance_profile_name: str, role_name: str) -> AddRoleToInstanceProfileResponse:
        """Makes an IAM C{AddRoleToInstanceProfile} call.

        @param name: The name of the instance profile to update.

        @param name: The name of the role to add.

        """
    def make_request(self, action: str, params: MutableMapping[str, str], data: str = '', service: str = 'ec2', signature_version: int | None = None) -> http.client.HTTPResponse: ...
    def sign(self, key: bytes, msg: str) -> bytes: ...
    def signature_key(self, key: str, dateStamp: str, regionName: str, serviceName: str) -> bytes: ...
    def get_signature_version_4(self, params: Iterable[tuple[str, str]], service: str) -> str: ...
    def get_signature_version_2(self, params: Iterable[tuple[str, str]], aws_secret_access_key: str) -> str: ...
    def get_aws_auth_param(self, params: Iterable[tuple[str, str]], aws_secret_access_key: str) -> str: ...
    def encoded_params(self, params: Iterable[tuple[str, str]]) -> str: ...
    @typing.overload
    def encode(self, aws_secret_access_key: str, str: str, urlencode: Literal[True] = ...) -> str: ...
    @typing.overload
    def encode(self, aws_secret_access_key: str, str: str, urlencode: Literal[False]) -> bytes: ...
    @typing.overload
    def encode(self, aws_secret_access_key: str, str: str, urlencode: bool = ...) -> str | bytes: ...

class Response(Generic[_S]):
    """Base class for XML response parsers.

    This class does everything except the API-call dependent parsing,
    which is handled in the child classes below.  Each child class
    should override the L{parse} method.
    
    """
    service: str
    http_response: http.client.HTTPResponse
    http_xml: bytes
    is_error: bool
    structure: _S | list[list[str]]
    ERROR_XPATH: str
    IAM_ERROR_XPATH: str
    NAMESPACE: str
    IAM_NAMESPACE: str
    def __init__(self, http_response: http.client.HTTPResponse, service: str = 'ec2') -> None: ...
    def parse_error(self) -> list[list[str]]: ...
    def parse(self) -> _S: ...
    def fixxpath(self, xpath: str) -> str: ...
    def findtext(self, element: ET.Element, xpath: str) -> str | None: ...
    def findall(self, element: ET.Element, xpath: str) -> list[ET.Element]: ...
    def find(self, element: ET.Element, xpath: str) -> ET.Element | None: ...
    def fixnone(self, strnone: str | None) -> str: ...

class DescribeImagesResponse(Response[list[list[str | None]]]):
    """Response parser class for C{DescribeImages} API call."""
    ELEMENT_XPATH: str
    def translate_isPublic(self, isPublic: str) -> str: ...
    def parse(self) -> list[list[str | None]]: ...

class RegisterImageResponse(Response[list[list[str | None]]]):
    """Response parser class for C{RegisterImage} API call."""
    ELEMENT_XPATH: str
    def parse(self) -> list[list[str | None]]: ...

class DeregisterImageResponse(Response[list[list[str]]]):
    """Response parser class for C{DeregisterImage} API call."""
    def parse(self) -> list[list[str]]: ...

class CreateKeyPairResponse(Response[list[list[str | None]]]):
    """Response parser class for C{CreateKeyPair} API call."""
    def parse(self) -> list[list[str | None]]: ...

class DescribeKeyPairsResponse(Response[list[list[str | None]]]):
    """Response parser class for C{DescribeKeyPairs} API call."""
    ELEMENT_XPATH: str
    def parse(self) -> list[list[str | None]]: ...

class DeleteKeyPairResponse(Response[list[list[str]]]):
    """Response parser class for C{DeleteKeyPair} API call."""
    def parse(self) -> list[list[str]]: ...

class InstanceSetResponse(Response[list[list[str | None]]]):
    """ Response containing instance set items """
    def parseInstanceSet(self, root: ET.Element) -> list[list[str | None]]:
        """ Parse a set of instanceSet/item nodes """

class RunInstancesResponse(InstanceSetResponse):
    """Response parser class for C{RunInstances} API call."""
    def parse(self) -> list[list[str | None]]: ...

class DescribeInstancesResponse(InstanceSetResponse):
    """Response parser class for C{DescribeInstances} API call."""
    ELEMENT_XPATH: str
    def parse(self) -> list[list[str | None]]: ...

class DescribeInstanceAttributeResponse(Response[list[str | None]]):
    """Response parser class for C{DescribeInstanceAttribute} API call."""
    def parse(self) -> list[str | None]: ...

class GetConsoleOutputResponse(Response[list[list[str | None]]]):
    def parse(self) -> list[list[str | None]]: ...

class TerminateInstancesResponse(Response[list[list[str | None]]]):
    """Response parser class for C{TerminateInstances} API call."""
    ELEMENT_XPATH: str
    def parse(self) -> list[list[str | None]]: ...

class RebootInstancesResponse(Response[list[list[str]]]):
    """Response parser class for C{RebootInstances} API call."""
    def parse(self) -> list[list[str]]: ...

class CreateSecurityGroupResponse(Response[list[list[str]]]):
    """Response parser class for C{CreateSecurityGroup} API call."""
    def parse(self) -> list[list[str]]: ...

class DescribeSecurityGroupsResponse(Response[list[list[str | None]]]):
    """Response parser class for C{DescribeSecurityGroups} API call."""
    ELEMENT_XPATH: str
    def parse(self) -> list[list[str | None]]: ...

class DeleteSecurityGroupResponse(Response[list[list[str]]]):
    """Response parser class for C{DeleteSecurityGroup} API call."""
    def parse(self) -> list[list[str]]: ...

class AuthorizeSecurityGroupIngressResponse(Response[list[list[str]]]):
    """Response parser class for C{AuthorizeSecurityGroupIngress} API call."""
    def parse(self) -> list[list[str]]: ...

class RevokeSecurityGroupIngressResponse(Response[list[list[str]]]):
    """Response parser class for C{RevokeSecurityGroupIngress} API call."""
    def parse(self) -> list[list[str]]: ...

class ModifyImageAttributeResponse(Response[list[list[str]]]):
    """Response parser class for C{ModifyImageAttribute} API call."""
    def parse(self) -> list[list[str]]: ...

class ResetImageAttributeResponse(Response[list[list[str]]]):
    """Response parser class for C{ResetImageAttribute} API call."""
    def parse(self) -> list[list[str]]: ...

class DescribeImageAttributeResponse(Response[list[list[str | None]]]):
    """Response parser class for C{DescribeImageAttribute} API call."""
    def parse(self) -> list[list[str | None]]: ...

class AllocateAddressResponse(Response[list[list[str | None]]]):
    """Response parser class for C{AllocateAddress} API call."""
    def parse(self) -> list[list[str | None]]: ...

class DescribeAddressesResponse(Response[list[list[str | None]]]):
    """Response parser class for C{DescribeAddresses} API call."""
    ELEMENT_XPATH: str
    def parse(self) -> list[list[str | None]]: ...

class ReleaseAddressResponse(Response[list[list[str]]]):
    """Response parser class for C{ReleaseAddress} API call."""
    def parse(self) -> list[list[str]]: ...

class AssociateAddressResponse(Response[list[list[str]]]):
    """Response parser class for C{AssociateAddress} API call."""
    def parse(self) -> list[list[str]]: ...

class DisassociateAddressResponse(Response[list[list[str]]]):
    """Response parser class for C{DisassociateAddress} API call."""
    def parse(self) -> list[list[str]]: ...

class ConfirmProductInstanceResponse(Response[None]):
    """Response parser class for C{ConfirmProductInstance} API call."""
    def parse(self) -> None: ...

class DescribeAvailabilityZonesResponse(Response[list[list[str | None]]]):
    """Response parser class for C{DescribeAvailabilityZones} API call."""
    ELEMENT_XPATH: str
    def parse(self) -> list[list[str | None]]: ...

class CreateRoleResponse(Response[list[list[str]]]):
    """Response parser class for C{CreateRole} API call."""
    def __init__(self, http_response: http.client.HTTPResponse) -> None: ...
    def parse(self) -> list[list[str]]: ...

class AttachRolePolicyResponse(Response[list[list[str]]]):
    """Response parser class for C{AttachRolePolicy} API call."""
    def __init__(self, http_response: http.client.HTTPResponse) -> None: ...
    def parse(self) -> list[list[str]]: ...

class GetRoleResponse(Response[list[list[str | None]]]):
    """Response parser class for C{GetRole} API call."""
    ELEMENT_XPATH: str
    def __init__(self, http_response: http.client.HTTPResponse) -> None: ...
    def parse(self) -> list[list[str | None]]: ...

class CreateInstanceProfileResponse(Response[list[list[str]]]):
    """Response parser class for C{CreateInstanceProfile} API call."""
    def __init__(self, http_response: http.client.HTTPResponse) -> None: ...
    def parse(self) -> list[list[str]]: ...

class GetInstanceProfileResponse(Response[list[list[str | list[list[str | None]] | None]]]):
    """Response parser class for C{GetInstanceProfile} API call."""
    ELEMENT_XPATH: str
    def __init__(self, http_response: http.client.HTTPResponse) -> None: ...
    def parse(self) -> list[list[str | list[list[str | None]] | None]]: ...

class AddRoleToInstanceProfileResponse(Response[list[list[str]]]):
    """Response parser class for C{AddRoleToInstanceProfile} API call."""
    def __init__(self, http_response: http.client.HTTPResponse) -> None: ...
    def parse(self) -> list[list[str]]: ...
