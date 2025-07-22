from .lib import sgsix as sgsix, sgutils as sgutils
from .lib.httplib2 import Http as Http, ProxyInfo as ProxyInfo, socks as socks, ssl_error_classes as ssl_error_classes  # type: ignore[attr-defined]
from .lib.sgtimezone import SgTimezone as SgTimezone
from .lib.six import BytesIO as BytesIO  # type: ignore[import-not-found]
from .lib.six.moves import http_client as http_client, http_cookiejar as http_cookiejar, map as map, urllib as urllib  # type: ignore[import-not-found]
from .lib.six.moves.xmlrpc_client import Error as Error, ProtocolError as ProtocolError, ResponseError as ResponseError  # type: ignore[import-not-found]
from _typeshed import Incomplete
from typing import Any, BinaryIO, Iterable, Literal, NoReturn, TypeVar, TypedDict

T = TypeVar('T')
LOG: Incomplete

class OrderItem(TypedDict):
    field_name: str
    direction: str

class GroupingItem(TypedDict):
    field: str
    type: str
    direction: str

class BaseEntity(TypedDict, total=False):
    id: int
    type: str

def _is_mimetypes_broken():
    """
    Checks if this version of Python ships with a broken version of mimetypes

    :returns: True if the version of mimetypes is broken, False otherwise.
    """

SG_TIMEZONE: Incomplete
SHOTGUN_API_DISABLE_ENTITY_OPTIMIZATION: bool
NO_SSL_VALIDATION: bool
__version__: str

class ShotgunError(Exception):
    """
    Base for all Shotgun API Errors.
    """
class ShotgunFileDownloadError(ShotgunError):
    """
    Exception for file download-related errors.
    """
class ShotgunThumbnailNotReady(ShotgunError):
    """
    Exception for when trying to use a 'pending thumbnail' (aka transient thumbnail) in an operation
    """
class Fault(ShotgunError):
    """
    Exception when server-side exception detected.
    """
class AuthenticationFault(Fault):
    """
    Exception when the server side reports an error related to authentication.
    """
class MissingTwoFactorAuthenticationFault(Fault):
    """
    Exception when the server side reports an error related to missing two-factor authentication
    credentials.
    """
class UserCredentialsNotAllowedForSSOAuthenticationFault(Fault):
    """
    Exception when the server is configured to use SSO. It is not possible to use
    a username/password pair to authenticate on such server.
    """
class UserCredentialsNotAllowedForOxygenAuthenticationFault(Fault):
    """
    Exception when the server is configured to use Oxygen. It is not possible to use
    a username/password pair to authenticate on such server.
    """

class ServerCapabilities:
    """
    Container for the servers capabilities, such as version enabled features.

    .. warning::

        This class is part of the internal API and its interfaces may change at any time in
        the future. Therefore, usage of this class is discouraged.
    """
    host: Incomplete
    server_info: Incomplete
    version: Incomplete
    is_dev: bool
    def __init__(self, host: str, meta: dict[str, Any]) -> None:
        """
        ServerCapabilities.__init__

        :param str host: Host name for the server excluding protocol.
        :param dict meta: dict of meta data for the server returned from the info() api method.

        :ivar str host:
        :ivar dict server_info:
        :ivar tuple version: Simple version of the Shotgun server. ``(major, minor, rev)``
        :ivar bool is_dev: ``True`` if server is running a development version of the Shotgun
            codebase.
        """
    def _ensure_python_version_supported(self) -> None:
        """
        Checks the if current Python version is supported.
        """
    def _ensure_support(self, feature: dict[str, Any], raise_hell: bool = True) -> bool:
        """
        Checks the server version supports a given feature, raises an exception if it does not.

        :param dict feature: dict where **version** key contains a 3 integer tuple indicating the
            supported server version and **label** key contains a human-readable label str::

                { 'version': (5, 4, 4), 'label': 'project parameter }
        :param bool raise_hell: Whether to raise an exception if the feature is not supported.
            Defaults to ``True``
        :raises: :class:`ShotgunError` if the current server version does not support ``feature``
        :rtype: bool
        """
    def _ensure_json_supported(self) -> None:
        """
        Ensures server has support for JSON API endpoint added in v2.4.0.
        """
    def ensure_include_archived_projects(self) -> None:
        """
        Ensures server has support for archived Projects feature added in v5.3.14.
        """
    def ensure_per_project_customization(self) -> bool:
        """
        Ensures server has support for per-project customization feature added in v5.4.4.
        """
    def ensure_support_for_additional_filter_presets(self) -> bool:
        """
        Ensures server has support for additional filter presets feature added in v7.0.0.
        """
    def ensure_user_following_support(self) -> bool:
        """
        Ensures server has support for listing items a user is following, added in v7.0.12.
        """
    def ensure_paging_info_without_counts_support(self):
        """
        Ensures server has support for optimized pagination, added in v7.4.0.
        """
    def ensure_return_image_urls_support(self):
        """
        Ensures server has support for returning thumbnail URLs without additional round-trips, added in v3.3.0.
        """
    def __str__(self) -> str: ...

class ClientCapabilities:
    """
    Container for the client capabilities.

    .. warning::

        This class is part of the internal API and its interfaces may change at any time in
        the future. Therefore, usage of this class is discouraged.

    :ivar str platform: The current client platform. Valid values are ``mac``, ``linux``,
        ``windows``, or ``None`` (if the current platform couldn't be determined).
    :ivar str local_path_field: The PTR field used for local file paths. This is calculated using
        the value of ``platform``. Ex. ``local_path_mac``.
    :ivar str py_version: Simple version of Python executable as a string. Eg. ``2.7``.
    :ivar str ssl_version: Version of OpenSSL installed. Eg. ``OpenSSL 1.0.2g  1 Mar 2016``. This
        info is only available in Python 2.7+ if the ssl module was imported successfully.
        Defaults to ``unknown``
    """
    platform: str
    local_path_field: Incomplete
    py_version: Incomplete
    ssl_version: str
    def __init__(self) -> None: ...
    def __str__(self) -> str: ...

class _Config:
    """
    Container for the client configuration.
    """
    _sg: Incomplete
    max_rpc_attempts: int
    rpc_attempt_interval: int
    timeout_secs: float | None
    api_ver: str
    convert_datetimes_to_utc: bool
    _records_per_page: int | None
    api_key: str | None
    script_name: str | None
    user_login: str | None
    user_password: str | None
    auth_token: str | None
    sudo_as_login: str | None
    extra_auth_params: dict[str, Any] | None
    session_uuid: str | None
    scheme: str | None
    server: str | None
    api_path: str | None
    raw_http_proxy: str | None
    proxy_handler: urllib.request.ProxyHandler | None
    proxy_server: str | None
    proxy_port: int
    proxy_user: str | None
    proxy_pass: str | None
    session_token: str | None
    authorization: str | None
    no_ssl_validation: bool
    localized: bool
    def __init__(self, sg: Shotgun) -> None:
        """
        :param sg: Shotgun connection.
        """
    def set_server_params(self, base_url: str) -> None:
        """
        Set the different server related fields based on the passed in URL.

        This will impact the following attributes:

        - scheme: http or https
        - api_path: usually /api3/json
        - server: usually something.shotgunstudio.com

        :param str base_url: The server URL.

        :raises ValueError: Raised if protocol is not http or https.
        """
    @property
    def records_per_page(self) -> int:
        """
        The records per page value from the server.
        """

class Shotgun:
    """
    Shotgun Client connection.
    """
    _DATE_PATTERN: Incomplete
    _DATE_TIME_PATTERN: Incomplete
    _MULTIPART_UPLOAD_CHUNK_SIZE: int
    MAX_ATTEMPTS: int
    BACKOFF: float
    config: _Config
    _connection: Http | None
    __ca_certs: Incomplete
    base_url: Incomplete
    client_caps: Incomplete
    _server_caps: ServerCapabilities | None
    def __init__(self, base_url: str, script_name: str | None = None, api_key: str | None = None, convert_datetimes_to_utc: bool = True, http_proxy: str | None = None, ensure_ascii: bool = True, connect: bool = True, ca_certs: str | None = None, login: str | None = None, password: str | None = None, sudo_as_login: str | None = None, session_token: str | None = None, auth_token: str | None = None) -> None:
        """
        Initializes a new instance of the Shotgun client.

        :param str base_url: http or https url of the Shotgun server. Do not include the trailing
            slash::

                https://example.shotgunstudio.com
        :param str script_name: name of the Script entity used to authenticate to the server.
            If provided, then ``api_key`` must be as well, and neither ``login`` nor ``password``
            can be provided.

            .. seealso:: :ref:`authentication`
        :param str api_key: API key for the provided ``script_name``. Used to authenticate to the
            server.  If provided, then ``script_name`` must be as well, and neither ``login`` nor
            ``password`` can be provided.

            .. seealso:: :ref:`authentication`
        :param bool convert_datetimes_to_utc: (optional) When ``True``, datetime values are converted
            from local time to UTC time before being sent to the server. Datetimes received from
            the server are then converted back to local time. When ``False`` the client should use
            UTC date time values. Default is ``True``.
        :param str http_proxy: (optional) URL for a proxy server to use for all connections. The
            expected str format is ``[username:password@]111.222.333.444[:8080]``. Examples::

                192.168.0.1
                192.168.0.1:8888
                joe:user@192.168.0.1:8888
        :param bool connect: (optional) When ``True``, as soon as the :class:`~shotgun_api3.Shotgun`
            instance is created, a connection will be made to the Shotgun server to determine the
            server capabilities and confirm this version of the client is compatible with the server
            version. This is mostly used for testing. Default is ``True``.
        :param str ca_certs: (optional) path to an external SSL certificates file. By default, the
            Shotgun API will use its own built-in certificates file which stores root certificates
            for the most common Certificate Authorities (CAs). If you are using a corporate or
            internal CA, or are packaging an application into an executable, it may be necessary to
            point to your own certificates file. You can do this by passing in the full path to the
            file via this parameter or by setting the environment variable ``SHOTGUN_API_CACERTS``.
            In the case both are set, this parameter will take precedence.
        :param str login: The user login str to use to authenticate to the server when using user-based
            authentication. If provided, then ``password`` must be as well, and neither
            ``script_name`` nor ``api_key`` can be provided.

            .. seealso:: :ref:`authentication`
        :param str password: The password str to use to authenticate to the server when using user-based
            authentication. If provided, then ``login`` must be as well and neither ``script_name``
            nor ``api_key`` can be provided.

            See :ref:`authentication` for more info.
        :param str sudo_as_login: A user login string for the user whose permissions will be applied
            to all actions. Event log entries will be generated showing this user performing all
            actions with an additional extra meta-data parameter ``sudo_actual_user`` indicating the
            script or user that is actually authenticated.
        :param str session_token: The session token to use to authenticate to the server. This
            can be used as an alternative to authenticating with a script user or regular user.
            You can retrieve the session token by running the
            :meth:`~shotgun_api3.Shotgun.get_session_token()` method.

            .. todo: Add this info to the Authentication section of the docs
        :param str auth_token: The authentication token required to authenticate to a server with
            two-factor authentication turned on. If provided, then ``login`` and ``password`` must
            be provided as well, and neither ``script_name`` nor ``api_key`` can be provided.

            .. note:: These tokens can be short lived so a session is established right away if an
                ``auth_token`` is provided. A
                :class:`~shotgun_api3.MissingTwoFactorAuthenticationFault` will be raised if the
                ``auth_token`` is invalid.
            .. todo: Add this info to the Authentication section of the docs

        .. note:: A note about proxy connections: If you are using Python <= v2.6.2, HTTPS
            connections through a proxy server will not work due to a bug in the :mod:`urllib2`
            library (see http://bugs.python.org/issue1424152). This will affect upload and
            download-related methods in the Shotgun API (eg. :meth:`~shotgun_api3.Shotgun.upload`,
            :meth:`~shotgun_api3.Shotgun.upload_thumbnail`,
            :meth:`~shotgun_api3.Shotgun.upload_filmstrip_thumbnail`,
            :meth:`~shotgun_api3.Shotgun.download_attachment`. Normal CRUD methods for passing JSON
            data should still work fine. If you cannot upgrade your Python installation, you can see
            the patch merged into Python v2.6.3 (http://hg.python.org/cpython/rev/0f57b30a152f/) and
            try and hack it into your installation but YMMV. For older versions of Python there
            are other patches that were proposed in the bug report that may help you as well.
        """
    def _split_url(self, base_url: str) -> tuple[str, str]:
        """
        Extract the hostname:port and username/password/token from base_url
        sent when connect to the API.

        In python 3.8 `urllib.parse.splituser` was deprecated warning devs to
        use `urllib.parse.urlparse`.
        """
    @property
    def server_info(self) -> dict[str, Any]:
        """
        Property containing server information.

        >>> sg.server_info
        {'full_version': [6, 3, 15, 0], 'version': [6, 3, 15], ...}

        .. note::

            Beyond ``full_version`` and ``version`` which differ by the inclusion of the bugfix number,
            you should expect these values to be unsupported and for internal use only.

        :returns: dict of server information from :class:`ServerCapabilities` object
        :rtype: dict
        """
    @property
    def server_caps(self) -> ServerCapabilities:
        """
        Property containing :class:`ServerCapabilities` object.

        >>> sg.server_caps
        <shotgun_api3.shotgun.ServerCapabilities object at 0x10120d350>

        :returns: :class:`ServerCapabilities` object that describe the server the client is
            connected to.
        :rtype: :class:`ServerCapabilities` object
        """
    def connect(self) -> None:
        """
        Connect client to the server if it is not already connected.

        .. note:: The client will automatically connect to the server on demand. You only need to
            call this function if you wish to confirm the client can connect.
        """
    def close(self) -> None:
        """
        Close the current connection to the server.

        If the client needs to connect again it will do so automatically.
        """
    def info(self) -> dict[str, Any]:
        """
        Get API-related metadata from the Shotgun server.

        >>> sg.info()
        {'full_version': [8, 2, 1, 0], 'version': [8, 2, 1], 'user_authentication_method': 'default', ...}

        ::

            Token                       Value
            --------                    ---------
            full_version                An ordered array of the full Shotgun version.
                                        [major, minor, patch, hotfix]
            version                     An ordered array of the Shotgun version.
                                        [major, minor, patch]
            user_authentication_method  Indicates the authentication method used by Shotgun.
                                        Will be one of the following values:
                                            default: regular username/password.
                                            ldap:    username/password from the company's LDAP.
                                            saml2:   SSO used, over SAML2.

        .. note::

            Beyond the documented tokens, you should expect
            the other values to be unsupported and for internal use only.

        :returns: dict of the server metadata.
        :rtype: dict
        """
    def find_one(self, entity_type: str, filters: list | tuple | dict[str, Any], fields: list[str] | None = None, order: list[OrderItem] | None = None, filter_operator: Literal['all', 'any'] | None = None, retired_only: bool = False, include_archived_projects: bool = True, additional_filter_presets: list[dict[str, Any]] | None = None) -> BaseEntity | None:
        '''
        Shortcut for :meth:`~shotgun_api3.Shotgun.find` with ``limit=1`` so it returns a single
        result.

            >>> sg.find_one("Asset", [["id", "is", 32]], ["id", "code", "sg_status_list"])
            {\'code\': \'Gopher\', \'id\': 32, \'sg_status_list\': \'ip\', \'type\': \'Asset\'}

        :param str entity_type: Shotgun entity type as a string to find.
        :param list filters: list of filters to apply to the query.

            .. seealso:: :ref:`filter_syntax`

        :param list fields: Optional list of fields to include in each entity record returned.
            Defaults to ``["id"]``.
        :param list order: Optional list of fields to order the results by. List has the format::

                [
                    {\'field_name\':\'foo\', \'direction\':\'asc\'},
                    {\'field_name\':\'bar\', \'direction\':\'desc\'}
                ]

            Defaults to sorting by ``id`` in ascending order.
        :param str filter_operator: Operator to apply to the filters. Supported values are ``"all"``
            and ``"any"``. These are just another way of defining if the query is an AND or OR
            query. Defaults to ``"all"``.
        :param bool retired_only: Optional boolean when ``True`` will return only entities that have
            been retired. Defaults to ``False`` which returns only entities which have not been
            retired. There is no option to return both retired and non-retired entities in the
            same query.
        :param bool include_archived_projects: Optional boolean flag to include entities whose projects
            have been archived. Defaults to ``True``.
        :param list additional_filter_presets: Optional list of presets to further filter the result
            set, list has the form::

                [{
                    "preset_name": <preset_name>,
                    <optional_param1>: <optional_value1>,
                    ...
                }]

            Note that these filters are ANDed together and ANDed with the \'filter\'
            argument.

            For details on supported presets and the format of this parameter see
            :ref:`additional_filter_presets`
        :returns: Dictionary representing a single matching entity with the requested fields,
            and the defaults ``"id"`` and ``"type"`` which are always included.

            .. seealso:: :ref:`entity-fields`

        :rtype: dict
        '''
    def find(self, entity_type: str, filters: list | tuple | dict[str, Any], fields: list[str] | None = None, order: list[OrderItem] | None = None, filter_operator: Literal['all', 'any'] | None = None, limit: int = 0, retired_only: bool = False, page: int = 0, include_archived_projects: bool = True, additional_filter_presets: list[dict[str, Any]] | None = None) -> list[BaseEntity]:
        '''
        Find entities matching the given filters.

            >>> # Find Character Assets in Sequence 100_FOO
            >>> # -------------
            >>> fields = [\'id\', \'code\', \'sg_asset_type\']
            >>> sequence_id = 2 # Sequence "100_FOO"
            >>> project_id = 4 # Demo Project
            >>> filters = [
            ...     [\'project\', \'is\', {\'type\': \'Project\', \'id\': project_id}],
            ...     [\'sg_asset_type\', \'is\', \'Character\'],
            ...     [\'sequences\', \'is\', {\'type\': \'Sequence\', \'id\': sequence_id}]
            ... ]
            >>> assets= sg.find("Asset",filters,fields)
            [{\'code\': \'Gopher\', \'id\': 32, \'sg_asset_type\': \'Character\', \'type\': \'Asset\'},
             {\'code\': \'Cow\', \'id\': 33, \'sg_asset_type\': \'Character\', \'type\': \'Asset\'},
             {\'code\': \'Bird_1\', \'id\': 35, \'sg_asset_type\': \'Character\', \'type\': \'Asset\'},
             {\'code\': \'Bird_2\', \'id\': 36, \'sg_asset_type\': \'Character\', \'type\': \'Asset\'},
             {\'code\': \'Bird_3\', \'id\': 37, \'sg_asset_type\': \'Character\', \'type\': \'Asset\'},
             {\'code\': \'Raccoon\', \'id\': 45, \'sg_asset_type\': \'Character\', \'type\': \'Asset\'},
             {\'code\': \'Wet Gopher\', \'id\': 149, \'sg_asset_type\': \'Character\', \'type\': \'Asset\'}]

        You can drill through single entity links to filter on fields or display linked fields.
        This is often called "deep linking" or using "dot notation".

            .. seealso:: :ref:`filter_syntax`

            >>> # Find Versions created by Tasks in the Animation Pipeline Step
            >>> # -------------
            >>> fields = [\'id\', \'code\']
            >>> pipeline_step_id = 2 # Animation Step ID
            >>> project_id = 4 # Demo Project
            >>> # you can drill through single-entity link fields
            >>> filters = [
            ...     [\'project\',\'is\', {\'type\': \'Project\',\'id\': project_id}],
            ...     [\'sg_task.Task.step.Step.id\', \'is\', pipeline_step_id]
            >>> ]
            >>> sg.find("Version", filters, fields)
            [{\'code\': \'scene_010_anim_v001\', \'id\': 42, \'type\': \'Version\'},
             {\'code\': \'scene_010_anim_v002\', \'id\': 134, \'type\': \'Version\'},
             {\'code\': \'bird_v001\', \'id\': 137, \'type\': \'Version\'},
             {\'code\': \'birdAltBlue_v002\', \'id\': 236, \'type\': \'Version\'}]

        :param str entity_type: Shotgun entity type to find.
        :param list filters: list of filters to apply to the query.

            .. seealso:: :ref:`filter_syntax`, :ref:`combining-related-queries`

        :param list fields: Optional list of fields to include in each entity record returned.
            Defaults to ``["id"]``.

            .. seealso:: :ref:`combining-related-queries`

        :param list order: Optional list of dictionaries defining how to order the results of the
            query. Each dictionary contains the ``field_name`` to order by and  the ``direction``
            to sort::

                [
                    {\'field_name\':\'foo\', \'direction\':\'asc\'},
                    {\'field_name\':\'bar\', \'direction\':\'desc\'}
                ]

            Defaults to sorting by ``id`` in ascending order.
        :param str filter_operator: Operator to apply to the filters. Supported values are ``"all"``
            and ``"any"``. These are just another way of defining if the query is an AND or OR
            query. Defaults to ``"all"``.
        :param int limit: Optional limit to the number of entities to return. Defaults to ``0`` which
            returns all entities that match.
        :param int page: Optional page of results to return. Use this together with the ``limit``
            parameter to control how your query results are paged. Defaults to ``0`` which returns
            all entities that match.
        :param bool retired_only: Optional boolean when ``True`` will return only entities that have
            been retired. Defaults to ``False`` which returns only entities which have not been
            retired. There is no option to return both retired and non-retired entities in the
            same query.
        :param bool include_archived_projects: Optional boolean flag to include entities whose projects
            have been archived. Defaults to ``True``.
        :param list additional_filter_presets: Optional list of presets to further filter the result
            set, list has the form::

                [{
                    "preset_name": <preset_name>,
                    <optional_param1>: <optional_value1>,
                    ...
                }]

            Note that these filters are ANDed together and ANDed with the \'filter\'
            argument.

            For details on supported presets and the format of this parameter see
            :ref:`additional_filter_presets`
        :returns: list of dictionaries representing each entity with the requested fields, and the
            defaults ``"id"`` and ``"type"`` which are always included.

            .. seealso:: :ref:`entity-fields`

        :rtype: list
        '''
    def _construct_read_parameters(self, entity_type: str, fields: list[str] | None, filters: dict[str, Any], retired_only: bool, order: list[dict[str, Any]] | None, include_archived_projects: bool, additional_filter_presets: list[dict[str, Any]] | None) -> dict[str, Any]: ...
    def _add_project_param(self, params: dict[str, Any], project_entity) -> dict[str, Any]: ...
    def _translate_update_params(self, entity_type: str, entity_id: int, data, multi_entity_update_modes) -> dict[str, Any]: ...
    def summarize(self, entity_type: str, filters: list | dict[str, Any], summary_fields: list[dict[str, str]], filter_operator: str | None = None, grouping: list[GroupingItem] | None = None, include_archived_projects: bool = True) -> dict[str, Any]:
        '''
        Summarize field data returned by a query.

        This provides the same functionality as the summaries in the UI. You can specify one or
        more fields to summarize, choose the summary type for each, and optionally group the
        results which will return summary information for each group as well as the total for
        the query.

        **Example: Count all Assets for a Project**

        >>> sg.summarize(entity_type=\'Asset\',
        ...              filters = [[\'project\', \'is\', {\'type\':\'Project\', \'id\':4}]],
        ...              summary_fields=[{\'field\':\'id\', \'type\':\'count\'}])
        {\'groups\': [], \'summaries\': {\'id\': 15}}

        ``summaries`` contains the total summary for the query. Each key is the field summarized
        and the value is the result of the summary operation for the entire result set.

        .. note::
            You cannot perform more than one summary on a field at a time, but you can summarize
            several different fields in the same call.

        **Example: Count all Assets for a Project, grouped by sg_asset_type**

        >>> sg.summarize(entity_type=\'Asset\',
        ...              filters=[[\'project\', \'is\', {\'type\': \'Project\', \'id\': 4}]],
        ...              summary_fields=[{\'field\': \'id\', \'type\': \'count\'}],
        ...              grouping=[{\'field\': \'sg_asset_type\', \'type\': \'exact\', \'direction\': \'asc\'}])
        {\'groups\': [{\'group_name\': \'Character\',\'group_value\': \'Character\', \'summaries\': {\'id\': 3}},
                    {\'group_name\': \'Environment\',\'group_value\': \'Environment\', \'summaries\': {\'id\': 3}},
                    {\'group_name\': \'Matte Painting\', \'group_value\': \'Matte Painting\', \'summaries\': {\'id\': 1}},
                    {\'group_name\': \'Prop\', \'group_value\': \'Prop\', \'summaries\': {\'id\': 4}},
                    {\'group_name\': \'Vehicle\', \'group_value\': \'Vehicle\', \'summaries\': {\'id\': 4}}],
         \'summaries\': {\'id\': 15}}

        - ``summaries`` contains the total summary for the query.
        - ``groups`` contains the summary for each group.

            - ``group_name`` is the display name for the group.
            - ``group_value`` is the actual value of the grouping value. This is often the same as
              ``group_name`` but in the case when grouping by entity, the ``group_name`` may be
              ``PuppyA`` and the group_value would be
              ``{\'type\':\'Asset\',\'id\':922,\'name\':\'PuppyA\'}``.
            - ``summaries`` contains the summary calculation dict for each field requested.

        **Example: Count all Tasks for a Sequence and find the latest due_date**

        >>> sg.summarize(entity_type=\'Task\',
        ...              filters = [
        ...                 [\'entity.Shot.sg_sequence\', \'is\', {\'type\':\'Sequence\', \'id\':2}],
        ...                 [\'sg_status_list\', \'is_not\', \'na\']],
        ...              summary_fields=[{\'field\':\'id\', \'type\':\'count\'},
        ...                              {\'field\':\'due_date\',\'type\':\'latest\'}])
        {\'groups\': [], \'summaries\': {\'due_date\': \'2013-07-05\', \'id\': 30}}

        This shows that the there are 30 Tasks for Shots in the Sequence and the latest ``due_date``
        of any Task is ``2013-07-05``.

        **Example: Count all Tasks for a Sequence, find the latest due_date and group by Shot**

        >>> sg.summarize(entity_type=\'Task\',
        ...              filters = [
        ...                 [\'entity.Shot.sg_sequence\', \'is\', {\'type\': \'Sequence\', \'id\': 2}],
        ...                 [\'sg_status_list\', \'is_not\', \'na\']],
        ...              summary_fields=[{\'field\': \'id\', \'type\': \'count\'}, {\'field\': \'due_date\', \'type\': \'latest\'}],
        ...              grouping=[{\'field\': \'entity\', \'type\': \'exact\', \'direction\': \'asc\'}]))
        {\'groups\': [{\'group_name\': \'shot_010\',
                     \'group_value\': {\'id\': 2, \'name\': \'shot_010\', \'type\': \'Shot\', \'valid\': \'valid\'},
                     \'summaries\': {\'due_date\': \'2013-06-18\', \'id\': 10}},
                    {\'group_name\': \'shot_020\',
                     \'group_value\': {\'id\': 3, \'name\': \'shot_020\', \'type\': \'Shot\', \'valid\': \'valid\'},
                     \'summaries\': {\'due_date\': \'2013-06-28\', \'id\': 10}},
                    {\'group_name\': \'shot_030\',
                     \'group_value\': {\'id\': 4, \'name\': \'shot_030\', \'type\': \'Shot\', \'valid\': \'valid\'},
                     \'summaries\': {\'due_date\': \'2013-07-05\', \'id\': 10}}],
         \'summaries\': {\'due_date\': \'2013-07-05\', \'id\': 30}}

        This shows that the there are 30 Tasks for Shots in the Sequence and the latest ``due_date``
        of any Task is ``2013-07-05``. Because the summary is grouped by ``entity``, we can also
        see the summaries for each Shot returned. Each Shot has 10 Tasks and the latest ``due_date``
        for each Shot. The difference between ``group_name`` and ``group_value`` is highlighted in
        this example as the name of the Shot is different from its value.

        **Example: Count all Tasks for a Sequence, find the latest due_date, group by Shot and
        Pipeline Step**

        >>> sg.summarize(entity_type=\'Task\',
        ...                 filters = [
        ...                    [\'entity.Shot.sg_sequence\', \'is\', {\'type\': \'Sequence\', \'id\': 2}],
        ...                    [\'sg_status_list\', \'is_not\', \'na\']],
        ...                 summary_fields=[{\'field\': \'id\', \'type\': \'count\'},
        ...                                 {\'field\': \'due_date\', \'type\': \'latest\'}],
        ...                 grouping=[{\'field\': \'entity\', \'type\': \'exact\', \'direction\': \'asc\'},
        ...                           {\'field\': \'step\', \'type\': \'exact\', \'direction\': \'asc\'}])
        {\'groups\': [{\'group_name\': \'shot_010\',
                     \'group_value\': {\'id\': 2, \'name\': \'shot_010\', \'type\': \'Shot\', \'valid\': \'valid\'},
                     \'groups\': [{\'group_name\': \'Client\',
                                 \'group_value\': {\'id\': 1, \'name\': \'Client\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-05-04\', \'id\': 1}},
                                {\'group_name\': \'Online\',
                                 \'group_value\': {\'id\': 2, \'name\': \'Online\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-05-05\', \'id\': 1}},
                                ...
                                ... truncated for brevity
                                ...
                                {\'group_name\': \'Comp\',
                                 \'group_value\': {\'id\': 8, \'name\': \'Comp\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-06-18\', \'id\': 1}}],
                     \'summaries\': {\'due_date\': \'2013-06-18\', \'id\': 10}},
                    {\'group_name\': \'shot_020\',
                     \'group_value\': {\'id\': 3, \'name\': \'shot_020\', \'type\': \'Shot\', \'valid\': \'valid\'},
                     \'groups\': [{\'group_name\': \'Client\',
                                 \'group_value\': {\'id\': 1, \'name\': \'Client\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-05-15\', \'id\': 1}},
                                {\'group_name\': \'Online\',
                                 \'group_value\': {\'id\': 2, \'name\': \'Online\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-05-16\', \'id\': 1}},
                                ...
                                ... truncated for brevity
                                ...
                                {\'group_name\': \'Comp\',
                                 \'group_value\': {\'id\': 8, \'name\': \'Comp\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-06-28\', \'id\': 1}}],
                     \'summaries\': {\'due_date\': \'2013-06-28\', \'id\': 10}},
                    {\'group_name\': \'shot_030\',
                     \'group_value\': {\'id\': 4, \'name\': \'shot_030\', \'type\': \'Shot\', \'valid\': \'valid\'},
                     \'groups\': [{\'group_name\': \'Client\',
                                 \'group_value\': {\'id\': 1, \'name\': \'Client\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-05-20\', \'id\': 1}},
                                {\'group_name\': \'Online\',
                                 \'group_value\': {\'id\': 2, \'name\': \'Online\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-05-21\', \'id\': 1}},
                                ...
                                ... truncated for brevity
                                ...
                                {\'group_name\': \'Comp\',
                                 \'group_value\': {\'id\': 8, \'name\': \'Comp\', \'type\': \'Step\', \'valid\': \'valid\'},
                                 \'summaries\': {\'due_date\': \'2013-07-05\', \'id\': 1}}],
                     \'summaries\': {\'due_date\': \'2013-07-05\', \'id\': 10}}],
        \'summaries\': {\'due_date\': \'2013-07-05\', \'id\': 30}}

        When grouping my more than one field, the grouping structure is repeated for each sub-group
        and summary values are returned for each group on each level.

        :param str entity_type: The entity type to summarize
        :param list filters: A list of conditions used to filter the find query. Uses the same
            syntax as :meth:`~shotgun_api3.Shotgun.find` method.
        :param list summary_fields: A list of dictionaries with the following keys:

            :field: The internal Shotgun field name you are summarizing.
            :type: The type of summary you are performing on the field. Summary types can be any of
                ``record_count``, ``count``, ``sum``, ``maximum``, ``minimum``, ``average``,
                ``earliest``, ``latest``, ``percentage``, ``status_percentage``, ``status_list``,
                ``checked``, ``unchecked`` depending on the type of field you\'re summarizing.

        :param str filter_operator: Operator to apply to the filters. Supported values are ``"all"``
            and ``"any"``. These are just another way of defining if the query is an AND or OR
            query. Defaults to ``"all"``.
        :param list grouping: Optional list of dicts with the following keys:

                :field: a string indicating the internal Shotgun field name on ``entity_type`` to
                    group results by.
                :type: A string indicating the type of grouping to perform for each group.
                    Valid types depend on the type of field you are grouping on and can be one of
                    ``exact``, ``tens``, ``hundreds``, ``thousands``, ``tensofthousands``,
                    ``hundredsofthousands``, ``millions``, ``day``, ``week``, ``month``,
                    ``quarter``,``year``, ``clustered_date``, ``oneday``, ``fivedays``,
                    ``entitytype``, ``firstletter``.
                :direction: A string that sets the order to display the grouped results. Valid
                    options are ``asc`` and  ``desc``. Defaults to ``asc``.

        :returns: dictionary containing grouping and summaries keys.
        :rtype: dict
        '''
    def create(self, entity_type: str, data: dict[str, Any], return_fields: list | None = None) -> dict[str, Any]:
        '''
        Create a new entity of the specified ``entity_type``.

            >>> data = {
            ...     "project": {"type": "Project", "id": 161},
            ...     "sg_sequence": {"type": "Sequence", "id": 109},
            ...     "code": "001_100",
            ...     \'sg_status_list\': "ip"
            ... }
            >>> sg.create(\'Shot\', data)
            {\'code\': \'001_100\',
             \'id\': 2557,
             \'project\': {\'id\': 161, \'name\': \'Pied Piper\', \'type\': \'Project\'},
             \'sg_sequence\': {\'id\': 109, \'name\': \'Sequence 001\', \'type\': \'Sequence\'},
             \'sg_status_list\': \'ip\',
             \'type\': \'Shot\'}

        :param str entity_type: Shotgun entity type to create.
        :param dict data: Dictionary of fields and corresponding values to set on the new entity. If
            ``image`` or ``filmstrip_image`` fields are provided, the file path will be uploaded
            to the server automatically.
        :param list return_fields: Optional list of additional field values to return from the new
            entity. Defaults to ``id`` field.

            .. seealso:: :ref:`combining-related-queries`

        :returns: Shotgun entity dictionary containing the field/value pairs of all of the fields
            set from the ``data`` parameter as well as the defaults ``type`` and ``id``. If any
            additional fields were provided using the ``return_fields`` parameter, these would be
            included as well.

            .. seealso:: :ref:`entity-fields`

        :rtype: dict
        '''
    def update(self, entity_type: str, entity_id: int, data: dict[str, Any], multi_entity_update_modes: dict[str, Any] | None = None) -> BaseEntity:
        '''
        Update the specified entity with the supplied data.

        >>> shots = [
        ...    {\'type\':\'Shot\', \'id\':\'40435\'},
        ...    {\'type\':\'Shot\', \'id\':\'40438\'},
        ...    {\'type\':\'Shot\', \'id\':\'40441\'}]
        >>> data = {
        ...    \'shots\': shots_asset_is_in,
        ...    \'sg_status_list\':\'rev\'}
        >>> sg.update("Asset", 55, data)
        {\'type\': \'Shot\',
         \'id\': 55,
         \'sg_status_`list`\': \'rev\',
         \'shots\': [{\'id\': 40435, \'name\': \'100_010\', \'type\': \'Shot\', \'valid\': \'valid\'},
                   {\'id\': 40438, \'name\': \'100_040\', \'type\': \'Shot\', \'valid\': \'valid\'},
                   {\'id\': 40441, \'name\': \'100_070\', \'type\': \'Shot\', \'valid\': \'valid\'}]
        }

        :param str entity_type: Entity type to update.
        :param id entity_id: int of the entity to update.
        :param dict data: key/value pairs where key is the field name and value is the value to set
            for that field. This method does not restrict the updating of fields hidden in the web
            UI via the Project Tracking Settings panel.
        :param dict multi_entity_update_modes: Optional dict indicating what update mode to use
            when updating a multi-entity link field. The keys in the dict are the fields to set
            the mode for, and the values from the dict are one of ``set``, ``add``, or ``remove``.
            Defaults to ``set``.
            ::

                multi_entity_update_modes={"shots": "add", "assets": "remove"}

        :returns: Dictionary of the fields updated, with the default keys `type` and `id` added as well.
        :rtype: dict
        '''
    def delete(self, entity_type: str, entity_id: int) -> bool:
        '''
        Retire the specified entity.

        Entities in Shotgun are not "deleted" destructively, they are instead, "retired". This
        means they are placed in the trash where they are no longer accessible to users.

        The entity can be brought back to life using :meth:`~shotgun_api3.Shotgun.revive`.

            >>> sg.delete("Shot", 2557)
            True

        :param str entity_type: Shotgun entity type to delete.
        :param id entity_id: ``id`` of the entity to delete.
        :returns: ``True`` if the entity was deleted, ``False`` otherwise (for example, if the
            entity was already deleted).
        :rtype: bool
        :raises: :class:`Fault` if entity does not exist (deleted or not).
        '''
    def revive(self, entity_type: str, entity_id: int) -> bool:
        '''
        Revive an entity that has previously been deleted.

        >>> sg.revive("Shot", 860)
        True

        :param str entity_type: Shotgun entity type to revive.
        :param int entity_id: int of the entity to revive.
        :returns: ``True`` if the entity was revived, ``False`` otherwise (e.g. if the
            entity is not currently retired).
        :rtype: bool
        '''
    def batch(self, requests: list) -> list:
        '''
        Make a batch request of several :meth:`~shotgun_api3.Shotgun.create`,
        :meth:`~shotgun_api3.Shotgun.update`, and :meth:`~shotgun_api3.Shotgun.delete` calls.

        All requests are performed within a transaction, so either all will complete or none will.

        Ex. Make a bunch of shots::

            batch_data = []
            for i in range(1,100):
                data = {
                    "code": "shot_%04d" % i,
                    "project": project
                }
                batch_data.append({"request_type": "create", "entity_type": "Shot", "data": data})
            sg.batch(batch_data)

        Example output::

             [{\'code\': \'shot_0001\',
               \'type\': \'Shot\',
               \'id\': 3624,
               \'project\': {\'id\': 4, \'name\': \'Demo Project\', \'type\': \'Project\'}},
              ...
              ... and a bunch more ...
              ...
              {\'code\': \'shot_0099\',
               \'type\': \'Shot\',
               \'id\': 3722,
               \'project\': {\'id\': 4, \'name\': \'Demo Project\', \'type\': \'Project\'}}]

        Ex. All three types of requests in one batch::

            batch_data = [
              {"request_type": "create", "entity_type": "Shot", "data": {"code": "New Shot 1", "project": project}},
              {"request_type": "update", "entity_type": "Shot", "entity_id": 3624, "data": {"code": "Changed 1"}},
              {"request_type": "delete", "entity_type": "Shot", "entity_id": 3624}
            ]
            sg.batch(batch_data)

        Example output::

             [{\'code\': \'New Shot 1\', \'type\': \'Shot\', \'id\': 3723,
               \'project\': {\'id\': 4, \'name\': \'Demo Project\', \'type\': \'Project\'}},
              {\'code\': \'Changed 1\', \'type\': \'Shot\', \'id\': 3624},
              True]

        :param list requests: A list of dict\'s of the form which have a request_type key and also
            specifies:

            - create: ``entity_type``, data dict of fields to set
            - update: ``entity_type``, ``entity_id``, data dict of fields to set,
                      and optionally ``multi_entity_update_modes``
            - delete: ``entity_type`` and entity_id
        :returns: A list of values for each operation. Create and update requests return a dict of
            the fields updated. Delete requests return ``True`` if the entity was deleted.
        :rtype: list
        '''
    def work_schedule_read(self, start_date: str, end_date: str, project: dict[str, Any] | None = None, user: dict[str, Any] | None = None) -> dict[str, Any]:
        '''
        Return the work day rules for a given date range.

        .. versionadded:: 3.0.9
            Requires Shotgun server v3.2.0+

        This returns the defined WorkDayRules between the ``start_date`` and ``end_date`` inclusive
        as a dict where the key is the date and the value is another dict describing the rule for
        that date.

        Rules are represented by a dict with the following keys:

        :description: the description entered into the work day rule exception if applicable.
        :reason: one of six options:

            - STUDIO_WORK_WEEK: standard studio schedule applies
            - STUDIO_EXCEPTION: studio-wide exception applies
            - PROJECT_WORK_WEEK: standard project schedule applies
            - PROJECT_EXCEPTION: project-specific exception applies
            - USER_WORK_WEEK: standard user work week applies
            - USER_EXCEPTION: user-specific exception applies

        :working: boolean indicating whether it is a "working" day or not.

        >>> sg.work_schedule_read("2015-12-21", "2015-12-25")
        {\'2015-12-21\': {\'description\': None,
                        \'reason\': \'STUDIO_WORK_WEEK\',
                        \'working\': True},
         \'2015-12-22\': {\'description\': None,
                        \'reason\': \'STUDIO_WORK_WEEK\',
                        \'working\': True},
         \'2015-12-23\': {\'description\': None,
                        \'reason\': \'STUDIO_WORK_WEEK\',
                        \'working\': True},
         \'2015-12-24\': {\'description\': \'Closed for Christmas Eve\',
                        \'reason\': \'STUDIO_EXCEPTION\',
                        \'working\': False},
         \'2015-12-25\': {\'description\': \'Closed for Christmas\',
                        \'reason\': \'STUDIO_EXCEPTION\',
                        \'working\': False}}


        :param str start_date: Start date of date range. ``YYYY-MM-DD``
        :param str end_date: End date of date range. ``YYYY-MM-DD``
        :param dict project: Optional Project entity to query `WorkDayRules` for.
        :param dict user: Optional HumanUser entity to query WorkDayRules for.
        :returns: Complex dict containing each date and the WorkDayRule defined for that date
            between the ``start_date`` and ``end date`` inclusive. See above for details.
        :rtype: dict
        '''
    def work_schedule_update(self, date: str, working: bool, description: str | None = None, project: dict[str, Any] | None = None, user: dict[str, Any] | None = None, recalculate_field: str | None = None) -> dict[str, Any]:
        '''
        Update the work schedule for a given date.

        .. versionadded:: 3.0.9
            Requires Shotgun server v3.2.0+

        If neither ``project`` nor ``user`` are passed in, the studio work schedule will be updated.
        ``project`` and ``user`` can only be used exclusively of each other.

        >>> sg.work_schedule_update ("2015-12-31", working=False,
        ...                          description="Studio closed for New Years Eve", project=None,
        ...                          user=None, recalculate_field=None)
        {\'date\': \'2015-12-31\',
         \'description\': "Studio closed for New Years Eve",
         \'project\': None,
         \'user\': None,
         \'working\': False}

        :param str date: Date of WorkDayRule to update. ``YYY-MM-DD``
        :param bool working: Indicates whether the day is a working day or not.
        :param str description: Optional reason for time off.
        :param dict project: Optional Project entity to assign the rule to. Cannot be used with the
            ``user`` param.
        :param dict user: Optional HumanUser entity to assign the rule to. Cannot be used with the
            ``project`` param.
        :param str recalculate_field: Optional schedule field that will be recalculated on Tasks
            when they are affected by a change in working schedule. Options are ``due_date`` or
            ``duration``. Defaults to the value set in the Shotgun web application\'s Site
            Preferences.
        :returns: dict containing key/value pairs for each value of the work day rule updated.
        :rtype: dict
        '''
    def follow(self, user: dict[str, Any], entity: dict[str, Any]) -> dict[str, Any]:
        '''
        Add the entity to the user\'s followed entities.

        If the user is already following the entity, the method will succeed but nothing will be
        changed on the server-side.

            >>> sg.follow({"type": "HumanUser", "id": 42}, {"type": "Shot", "id": 2050})
            {\'followed\': True, \'user\': {\'type\': \'HumanUser\', \'id\': 42},
             \'entity\': {\'type\': \'Shot\', \'id\': 2050}}

        :param dict user: User entity that will follow the entity.
        :param dict entity: Shotgun entity to be followed.
        :returns: dict with ``"followed": True`` as well as key/values for the params that were
            passed in.
        :rtype: dict
        '''
    def unfollow(self, user: dict[str, Any], entity: dict[str, Any]) -> dict[str, Any]:
        '''
        Remove entity from the user\'s followed entities.

        This does nothing if the user is not following the entity.

        >>> sg.unfollow({"type": "HumanUser", "id": 42}, {"type": "Shot", "id": 2050})
        {\'entity\': {\'type\': \'Shot\', \'id\': 2050}, \'user\': {\'type\': \'HumanUser\', \'id\': 42},
         \'unfollowed\': True}

        :param dict user: User entity that will unfollow the entity.
        :param dict entity: Entity to be unfollowed
        :returns: dict with ``"unfollowed": True`` as well as key/values for the params that were
            passed in.
        :rtype: dict
        '''
    def followers(self, entity: dict[str, Any]) -> list:
        '''
        Return all followers for an entity.

            >>> sg.followers({"type": "Shot", "id": 2050})
            [{\'status\': \'act\', \'valid\': \'valid\', \'type\': \'HumanUser\', \'name\': \'Richard Hendriks\',
              \'id\': 42},
             {\'status\': \'act\', \'valid\': \'valid\', \'type\': \'HumanUser\', \'name\': \'Bertram Gilfoyle\',
              \'id\': 33},
             {\'status\': \'act\', \'valid\': \'valid\', \'type\': \'HumanUser\', \'name\': \'Dinesh Chugtai\',
              \'id\': 57}]

        :param dict entity: Entity to find followers of.
        :returns: list of dicts representing each user following the entity
        :rtype: list
        :versionadded:
        '''
    def following(self, user: dict[str, Any], project: dict[str, Any] | None = None, entity_type: str | None = None) -> list[BaseEntity]:
        '''
        Return all entity instances a user is following.

        Optionally, a project and/or entity_type can be supplied to restrict returned results.

            >>> user = {"type": "HumanUser", "id": 1234}
            >>> project = {"type": "Project", "id": 1234}
            >>> entity_type = "Task"
            >>> sg.following(user, project=project, entity_type=entity_type)
            [{"type":"Task", "id":1},
             {"type":"Task", "id":2},
             {"type":"Task", "id":3}]

        :param dict user: Find what this person is following.
        :param dict project: Optional filter to only return results from a specific project.
        :param str entity_type: Optional filter to only return results from one entity type.
        :returns: list of dictionaries, each containing entity type & id\'s being followed.
        :rtype: list
        '''
    def schema_entity_read(self, project_entity: BaseEntity | None = None) -> dict[str, dict[str, Any]]:
        """
        Return all active entity types, their display names, and their visibility.

        If the project parameter is specified, the schema visibility for the given project is
        being returned. If the project parameter is omitted or set to ``None``, a full listing is
        returned where per-project entity type visibility settings are not considered.

        >>> sg.schema_entity_read()
        {'ActionMenuItem': {'name': {'editable': False, 'value': 'Action Menu Item'},
                            'visible': {'editable': False, 'value': True}},
         'ApiUser': {'name': {'editable': False, 'value': 'Script'},
                     'visible': {'editable': False, 'value': True}},
         'AppWelcomeUserConnection': {'name': {'editable': False,
                                               'value': 'App Welcome User Connection'},
                                      'visible': {'editable': False, 'value': True}},
         'Asset': {'name': {'editable': False, 'value': 'Asset'},
                   'visible': {'editable': False, 'value': True}},
         'AssetAssetConnection': {'name': {'editable': False,
                                           'value': 'Asset Asset Connection'},
                                  'visible': {'editable': False, 'value': True}},
         '...'
        }

        :param dict project_entity: Optional Project entity specifying which project to return
            the listing for. If omitted or set to ``None``, per-project visibility settings are
            not taken into consideration and the global list is returned. Example:
            ``{'type': 'Project', 'id': 3}``
        :returns: dict of Entity Type to dict containing the display name.
        :rtype: dict

        .. note::
            The returned display names for this method will be localized when the ``localize`` Shotgun config property is set to ``True``. See :ref:`localization` for more information.
        """
    def schema_read(self, project_entity: BaseEntity | None = None) -> dict[str, dict[str, Any]]:
        """
        Get the schema for all fields on all entities.

        .. note::
            If ``project_entity`` is not specified, everything is reported as visible.

        >>> sg.schema_read()
        {'ActionMenuItem': {'created_at': {'data_type': {'editable': False, 'value': 'date_time'},
                                           'description': {'editable': True,  'value': ''},
                                           'editable': {'editable': False, 'value': False},
                                           'entity_type': {'editable': False, 'value': 'ActionMenuItem'},
                                           'mandatory': {'editable': False, 'value': False},
                                           'name': {'editable': True, 'value': 'Date Created'},
                                           'properties': {'default_value': {'editable': False, 'value': None},
                                                          'summary_default': {'editable': True, 'value': 'none'}},
                                           'unique': {'editable': False, 'value': False},
                                           'visible': {'editable': False, 'value': True}},
                            'created_by': {'data_type': {'editable': False,'value': 'entity'},
                                           'description': {'editable': True,'value': ''},
                                           'editable': {'editable': False,'value': False},
                                           'entity_type': {'editable': False,'value': 'ActionMenuItem'},
                                           'mandatory': {'editable': False,'value': False},
                                           'name': {'editable': True,'value': 'Created by'},
                                           'properties': {'default_value': {'editable': False,'value': None},
                                                          'summary_default': {'editable': True,'value': 'none'},
                                                          'valid_types': {'editable': True,'value':
                                                                          ['HumanUser','ApiUser']}},
                                           'unique': {'editable': False,'value': False},
                                           'visible': {'editable': False,'value': True}},
                            ...
                            ...
         ...
         ...
         'Version': {'client_approved': {'data_type': {'editable': False,'value': 'checkbox'},
                                         'description': {'editable': True,'value': ''},
                                         'editable': {'editable': False,'value': True},
                                         'entity_type': {'editable': False,'value': 'Version'},
                                         'mandatory': {'editable': False,'value': False},
                                         'name': {'editable': True,'value': 'Client Approved'},
                                         'properties': {'default_value': {'editable': False,'value': False},
                                                        'summary_default': {'editable': False,'value': 'none'}},
                                         'unique': {'editable': False,'value': False},
                                         'visible': {'editable': False,'value': True}},
                     ...
                     ...
         ...
         ...
        }

        :param dict project_entity: Optional, Project entity specifying which project to return
            the listing for. If omitted or set to ``None``, per-project visibility settings are
            not taken into consideration and the global list is returned. Example:
            ``{'type': 'Project', 'id': 3}``. Defaults to ``None``.
        :returns: A nested dict object containing a key/value pair for all fields of all entity
            types. Properties that are ``'editable': True``, can be updated using the
            :meth:`~shotgun_api3.Shotgun.schema_field_update` method.
        :rtype: dict

        .. note::
            The returned display names for this method will be localized when the ``localize`` Shotgun config property is set to ``True``. See :ref:`localization` for more information.
        """
    def schema_field_read(self, entity_type: str, field_name: str | None = None, project_entity: BaseEntity | None = None) -> dict[str, dict[str, Any]]:
        """
        Get schema for all fields on the specified entity type or just the field name specified
        if provided.

        .. note::
            Unlike how the results of a :meth:`~shotgun_api3.Shotgun.find` can be pumped into a
            :meth:`~shotgun_api3.Shotgun.create` or :meth:`~shotgun_api3.Shotgun.update`, the
            results of :meth:`~shotgun_api3.Shotgun.schema_field_read` are not compatible with
            the format used for :meth:`~shotgun_api3.Shotgun.schema_field_create` or
            :meth:`~shotgun_api3.Shotgun.schema_field_update`. If you need to pipe the results
            from :meth:`~shotgun_api3.Shotgun.schema_field_read` into a
            :meth:`~shotgun_api3.Shotgun.schema_field_create` or
            :meth:`~shotgun_api3.Shotgun.schema_field_update`, you will need to reformat the
            data in your script.

        .. note::
            If you don't specify a ``project_entity``, everything is reported as visible.

        .. note::
            The returned display names for this method will be localized when the ``localize`` Shotgun config property is set to ``True``. See :ref:`localization` for more information.

        >>> sg.schema_field_read('Asset', 'shots')
        {'shots': {'data_type': {'editable': False, 'value': 'multi_entity'},
                   'description': {'editable': True, 'value': ''},
                   'editable': {'editable': False, 'value': True},
                   'entity_type': {'editable': False, 'value': 'Asset'},
                   'mandatory': {'editable': False, 'value': False},
                   'name': {'editable': True, 'value': 'Shots'},
                   'properties': {'default_value': {'editable': False,
                                                    'value': None},
                                  'summary_default': {'editable': True,
                                                      'value': 'none'},
                                  'valid_types': {'editable': True,
                                                  'value': ['Shot']}},
                   'unique': {'editable': False, 'value': False},
                   'visible': {'editable': False, 'value': True}}}

        :param str entity_type: Entity type to get the schema for.
        :param str field_name: Optional internal Shotgun name of the field to get the schema
            definition for. If this parameter is excluded or set to ``None``, data structures of
            all fields will be returned. Defaults to ``None``. Example: ``sg_temp_field``.
        :param dict project_entity: Optional Project entity specifying which project to return
            the listing for. If omitted or set to ``None``, per-project visibility settings are
            not taken into consideration and the global list is returned. Example:
            ``{'type': 'Project', 'id': 3}``
        :returns: a nested dict object containing a key/value pair for the ``field_name`` specified
            and its properties, or if no field_name is specified, for all the fields of the
            ``entity_type``. Properties that are ``'editable': True``, can be updated using the
            :meth:`~shotgun_api3.Shotgun.schema_field_update` method.
        :rtype: dict
        """
    def schema_field_create(self, entity_type: str, data_type: str, display_name: str, properties: dict[str, Any] | None = None) -> str:
        '''
        Create a field for the specified entity type.

        .. note::
            If the internal Shotgun field name computed from the provided ``display_name`` already
            exists, the internal Shotgun field name will automatically be appended with ``_1`` in
            order to create a unique name. The integer suffix will be incremented by 1 until a
            unique name is found.

        >>> properties = {"summary_default": "count", "description": "Complexity breakdown of Asset"}
        >>> sg.schema_field_create("Asset", "text", "Complexity", properties)
        \'sg_complexity\'

        :param str entity_type: Entity type to add the field to.
        :param str data_type: Shotgun data type for the new field.
        :param str display_name: Specifies the display name of the field you are creating. The
            system name will be created from this display name and returned upon successful
            creation.
        :param dict properties: dict of valid properties for the new field. Use this to specify
            other field properties such as the \'description\' or \'summary_default\'.
        :returns: The internal Shotgun name for the new field, this is different to the
            ``display_name`` parameter passed in.
        :rtype: str
        '''
    def schema_field_update(self, entity_type: str, field_name: str, properties: dict[str, Any], project_entity: BaseEntity | None = None) -> bool:
        '''
        Update the properties for the specified field on an entity.

        .. note::
            Although the property name may be the key in a nested dictionary, like
            \'summary_default\', it is treated no differently than keys that are up
            one level, like \'description\'.

        >>> properties = {"name": "Test Number Field Renamed", "summary_default": "sum",
        ...               "description": "this is only a test"}
        >>> sg.schema_field_update("Asset", "sg_test_number", properties)
        True

        :param str entity_type: Entity type of field to update.
        :param str field_name: Internal Shotgun name of the field to update.
        :param dict properties: Dictionary with key/value pairs where the key is the property to be
            updated and the value is the new value.
        :param dict project_entity: Optional Project entity specifying which project to modify the
            ``visible`` property for. If ``visible`` is present in ``properties`` and
            ``project_entity`` is not set, an exception will be raised. Example:
            ``{\'type\': \'Project\', \'id\': 3}``
        :returns: ``True`` if the field was updated.

        .. note::
            The ``project_entity`` parameter can only affect the state of the ``visible`` property
            and has no impact on other properties.

        :rtype: bool
        '''
    def schema_field_delete(self, entity_type: str, field_name: str) -> bool:
        '''
        Delete the specified field from the entity type.

        >>> sg.schema_field_delete("Asset", "sg_temp_field")
        True

        :param str entity_type: Entity type to delete the field from.
        :param str field_name: Internal Shotgun name of the field to delete.
        :returns: ``True`` if the field was deleted.
        :rtype: bool
        '''
    def add_user_agent(self, agent: str) -> None:
        '''
        Add agent to the user-agent header.

        Appends agent to the user-agent string sent with every API request.

        >>> sg.add_user_agent("my_tool 1.0")

        :param str agent: string to append to user-agent.
        '''
    _user_agents: Incomplete
    def reset_user_agent(self) -> None:
        """
        Reset user agent to the default value.

        Example default user-agent::

            shotgun-json (3.0.17); Python 2.6 (Mac); ssl OpenSSL 1.0.2d 9 Jul 2015 (validate)

        """
    def set_session_uuid(self, session_uuid: str) -> None:
        '''
        Set the browser session_uuid in the current Shotgun API instance.

        When this is set, any events generated by the API will include the ``session_uuid`` value
        on the corresponding EventLogEntries. If there is a current browser session open with
        this ``session_uuid``, the browser will display updates for these events.

        >>> sg.set_session_uuid("5a1d49b0-0c69-11e0-a24c-003048d17544")

        :param str session_uuid: The uuid of the browser session to be updated.
        '''
    def share_thumbnail(self, entities: list[dict[str, Any]], thumbnail_path: str | None = None, source_entity: BaseEntity | None = None, filmstrip_thumbnail: bool = False, **kwargs: Any) -> int:
        """
        Associate a thumbnail with more than one Shotgun entity.

        .. versionadded:: 3.0.9
            Requires Shotgun server v4.0.0+

        Share the thumbnail from between entities without requiring uploading the thumbnail file
        multiple times. You can use this in two ways:

        1) Upload an image to set as the thumbnail on multiple entities.
        2) Update multiple entities to point to an existing entity's thumbnail.

        .. note::
            When sharing a filmstrip thumbnail, it is required to have a static thumbnail in
            place before the filmstrip will be displayed in the Shotgun web UI.
            If the :ref:`thumbnail is still processing and is using a placeholder
            <interpreting_image_field_strings>`, this method will error.

        Simple use case:

        >>> thumb = '/data/show/ne2/100_110/anim/01.mlk-02b.jpg'
        >>> e = [{'type': 'Version', 'id': 123}, {'type': 'Version', 'id': 456}]
        >>> sg.share_thumbnail(entities=e, thumbnail_path=thumb)
        4271

        >>> e = [{'type': 'Version', 'id': 123}, {'type': 'Version', 'id': 456}]
        >>> sg.share_thumbnail(entities=e, source_entity={'type':'Version', 'id': 789})
        4271

        :param list entities: The entities to update to point to the shared  thumbnail provided in
            standard entity dict format::

                [{'type': 'Version', 'id': 123},
                 {'type': 'Version', 'id': 456}]
        :param str thumbnail_path: The full path to the local thumbnail file to upload and share.
            Required if ``source_entity`` is not provided.
        :param dict source_entity: The entity whos thumbnail will be the source for sharing.
            Required if ``source_entity`` is not provided.
        :param bool filmstrip_thumbnail: ``True`` to share the filmstrip thumbnail. ``False`` to
            share the static thumbnail. Defaults to ``False``.
        :returns: ``id`` of the Attachment entity representing the source thumbnail that is shared.
        :rtype: int
        :raises: :class:`ShotgunError` if not supported by server version or improperly called,
            or :class:`ShotgunThumbnailNotReady` if thumbnail is still pending.
        """
    def upload_thumbnail(self, entity_type: str, entity_id: int, path: str, **kwargs: Any) -> int:
        """
        Upload a file from a local path and assign it as the thumbnail for the specified entity.

        .. note::
            Images will automatically be re-sized on the server to generate a size-appropriate image
            file. However, the original file is retained as well and is accessible when you click
            on the thumbnail image in the web UI. If you are using a local install of Shotgun and
            have not enabled S3, this can eat up disk space if you're uploading really large source
            images for your thumbnails.

        You can un-set (aka clear) a thumbnail on an entity using the
        :meth:`~shotgun_api3.Shotgun.update` method and setting the **image** field to ``None``.
        This will also unset the ``filmstrip_thumbnail`` field if it is set.

        Supported image file types include ``.jpg` and ``.png`` (preferred) but will also accept.
        ``.gif```, ``.tif``, ``.tiff``, ``.bmp``, ``.exr``, ``.dpx``, and ``.tga``.

        This method wraps over :meth:`~shotgun_api3.Shotgun.upload`. Additional keyword arguments
        passed to this method will be forwarded to the :meth:`~shotgun_api3.Shotgun.upload` method.

        :param str entity_type: Entity type to set the thumbnail for.
        :param int entity_id: Id of the entity to set the thumbnail for.
        :param str path: Full path to the thumbnail file on disk.
        :returns: Id of the new attachment
        :rtype: int
        """
    def upload_filmstrip_thumbnail(self, entity_type: str, entity_id: int, path: str, **kwargs: Any) -> int:
        '''
        Upload filmstrip thumbnail to specified entity.

        .. versionadded:: 3.0.9
            Requires Shotgun server v3.1.0+

        Uploads a file from a local directory and assigns it as the filmstrip thumbnail for the
        specified entity. The image must be a horizontal strip of any number of frames that are
        exactly 240 pixels wide. Therefore the whole strip must be an exact multiple of 240 pixels
        in width. The height can be anything (and will depend on the aspect ratio of the frames).
        Any image file type that works for thumbnails will work for filmstrip thumbnails.

        Filmstrip thumbnails will only be visible in the Thumbnail field on an entity if a
        regular thumbnail image is also uploaded to the entity. The standard thumbnail is
        displayed by default as the poster frame. Then, on hover, the filmstrip thumbnail is
        displayed and updated based on your horizontal cursor position for scrubbing. On mouseout,
        the default thumbnail is displayed again as the poster frame.

        The url for a filmstrip thumbnail on an entity is available by querying for the
        ``filmstrip_image field``.

        You can un-set (aka clear) a thumbnail on an entity using the
        :meth:`~shotgun_api3.Shotgun.update` method and setting the **image** field to ``None``.
        This will also unset the ``filmstrip_thumbnail`` field if it is set.

        This method wraps over :meth:`~shotgun_api3.Shotgun.upload`. Additional keyword arguments
        passed to this method will be forwarded to the :meth:`~shotgun_api3.Shotgun.upload` method.

        >>> filmstrip_thumbnail = \'/data/show/ne2/100_110/anim/01.mlk-02b_filmstrip.jpg\'
        >>> sg.upload_filmstrip_thumbnail("Version", 27, filmstrip_thumbnail)
        87

        :param str entity_type: Entity type to set the filmstrip thumbnail for.
        :param int entity_id: Id of the entity to set the filmstrip thumbnail for.
        :param str path: Full path to the filmstrip thumbnail file on disk.
        :returns: Id of the new Attachment entity created for the filmstrip thumbnail
        :rtype: int
        '''
    def upload(self, entity_type: str, entity_id: int, path: str, field_name: str | None = None, display_name: str | None = None, tag_list: str | None = None) -> int:
        '''
        Upload a file to the specified entity.

        Creates an Attachment entity for the file in Shotgun and links it to the specified entity.
        You can optionally store the file in a field on the entity, change the display name, and
        assign tags to the Attachment.

        .. note::
          Make sure to have retries for file uploads. Failures when uploading will occasionally happen.
          When it does, immediately retrying to upload usually works

        >>> mov_file = \'/data/show/ne2/100_110/anim/01.mlk-02b.mov\'
        >>> sg.upload("Shot", 423, mov_file, field_name="sg_latest_quicktime",
        ...           display_name="Latest QT")
        72

        :param str entity_type: Entity type to link the upload to.
        :param int entity_id: Id of the entity to link the upload to.
        :param str path: Full path to an existing non-empty file on disk to upload.
        :param str field_name: The internal Shotgun field name on the entity to store the file in.
            This field must be a File/Link field type.
        :param str display_name: The display name to use for the file. Defaults to the file name.
        :param str tag_list: comma-separated string of tags to assign to the file.
        :returns: Id of the Attachment entity that was created for the image.
        :rtype: int
        :raises: :class:`ShotgunError` on upload failure.
        '''
    def _upload_to_storage(self, entity_type: str, entity_id: int, path: str, field_name: str | None, display_name: str | None, tag_list: str | None, is_thumbnail: bool) -> int:
        """
        Internal function to upload a file to the Cloud storage and link it to the specified entity.

        :param str entity_type: Entity type to link the upload to.
        :param int entity_id: Id of the entity to link the upload to.
        :param str path: Full path to an existing non-empty file on disk to upload.
        :param str field_name: The internal Shotgun field name on the entity to store the file in.
            This field must be a File/Link field type.
        :param str display_name: The display name to use for the file. Defaults to the file name.
        :param str tag_list: comma-separated string of tags to assign to the file.
        :param bool is_thumbnail: indicates if the attachment is a thumbnail.
        :returns: Id of the Attachment entity that was created for the image.
        :rtype: int
        """
    def _upload_to_sg(self, entity_type: str, entity_id: int, path: str, field_name: str | None, display_name: str | None, tag_list: str | None, is_thumbnail: bool) -> int:
        """
        Internal function to upload a file to Shotgun and link it to the specified entity.

        :param str entity_type: Entity type to link the upload to.
        :param int entity_id: Id of the entity to link the upload to.
        :param str path: Full path to an existing non-empty file on disk to upload.
        :param str field_name: The internal Shotgun field name on the entity to store the file in.
            This field must be a File/Link field type.
        :param str display_name: The display name to use for the file. Defaults to the file name.
        :param str tag_list: comma-separated string of tags to assign to the file.
        :param bool is_thumbnail: indicates if the attachment is a thumbnail.

        :returns: Id of the Attachment entity that was created for the image.
        :rtype: int
        """
    def _get_attachment_upload_info(self, is_thumbnail: bool, filename: str, is_multipart_upload: bool) -> dict[str, Any]:
        """
        Internal function to get the information needed to upload a file to Cloud storage.

        :param bool is_thumbnail: indicates if the attachment is a thumbnail.
        :param str filename: name of the file that will be uploaded.
        :param bool is_multipart_upload: Indicates if we want multi-part upload information back.

        :returns: dictionary containing upload details from the server.
            These details are used throughout the upload process.
        :rtype: dict
        """
    def download_attachment(self, attachment: dict[str, Any] | Literal[False] = False, file_path: str | None = None, attachment_id: int | None = None) -> str | bytes | None:
        '''
        Download the file associated with a Shotgun Attachment.

            >>> version = sg.find_one("Version", [["id", "is", 7115]], ["sg_uploaded_movie"])
            >>> local_file_path = "/var/tmp/%s" % version["sg_uploaded_movie"]["name"]
            >>> sg.download_attachment(version["sg_uploaded_movie"], file_path=local_file_path)
            /var/tmp/100b_scene_output_v032.mov

        .. warning::

            On older (< v5.1.0) Shotgun versions, non-downloadable files
            on Shotgun don\'t raise exceptions, they cause a server error which
            returns a 200 with the page content.

        :param dict attachment: Usually a dictionary representing an Attachment entity.
            The dictionary should have a ``url`` key that specifies the download url.
            Optionally, the dictionary can be a standard entity hash format with ``id`` and
            ``type`` keys as long as ``"type"=="Attachment"``. This is only supported for
            backwards compatibility (#22150).

            If an int value is passed in, the Attachment entity with the matching id will
            be downloaded from the Shotgun server.
        :param str file_path: Optional file path to write the data directly to local disk. This
            avoids loading all of the data in memory and saves the file locally at the given path.
        :param int attachment_id: (deprecated) Optional ``id`` of the Attachment entity in Shotgun to
            download.

            .. note:
                This parameter exists only for backwards compatibility for scripts specifying
                the parameter with keywords.
        :returns: If ``file_path`` is provided, returns the path to the file on disk.  If
            ``file_path`` is ``None``, returns the actual data of the file, as str in Python 2 or
            bytes in Python 3.
        :rtype: str | bytes
        '''
    def get_auth_cookie_handler(self) -> urllib.request.HTTPCookieProcessor:
        """
        Return an urllib cookie handler containing a cookie for FPTR
        authentication.

        Looks up session token and sets that in a cookie in the :mod:`urllib2`
        handler.
        This is used internally for downloading attachments from FPTR.
        """
    def get_attachment_download_url(self, attachment: int | dict[str, Any] | None) -> str:
        """
        Return the URL for downloading provided Attachment.

        :param mixed attachment: Usually a dict representing An Attachment entity in Shotgun to
            return the download url for. If the ``url`` key is present, it will be used as-is for
            the download url. If the ``url`` key is not present, a url will be constructed pointing
            at the current Shotgun server for downloading the Attachment entity using the ``id``.

            If ``None`` is passed in, it is silently ignored in order to avoid raising an error when
            results from a :meth:`~shotgun_api3.Shotgun.find` are passed off to
            :meth:`~shotgun_api3.Shotgun.download_attachment`

        .. note::
            Support for passing in an int representing the Attachment ``id`` is deprecated

        :returns: the download URL for the Attachment or ``None`` if ``None`` was passed to
            ``attachment`` parameter.
        :rtype: str
        """
    def authenticate_human_user(self, user_login: str, user_password: str, auth_token: str | None = None) -> dict[str, Any]:
        '''
        Authenticate Shotgun HumanUser.

        Authenticates a user given the login, password, and optionally, one-time auth token (when
        two-factor authentication is required). The user must be a ``HumanUser`` entity and the
        account must be active.

        >>> sg.authenticate_human_user("rhendriks", "c0mPre$Hi0n", None)
        {"type": "HumanUser", "id": 123, "name": "Richard Hendriks"}

        :param str user_login: Login name of Shotgun HumanUser
        :param str user_password: Password for Shotgun HumanUser
        :param str auth_token: One-time token required to authenticate Shotgun HumanUser
            when two-factor authentication is turned on.
        :returns: Standard Shotgun dictionary representing the HumanUser if authentication
            succeeded. ``None`` if authentication failed for any reason.
        :rtype: dict
        '''
    def update_project_last_accessed(self, project: dict[str, Any], user: dict[str, Any] | None = None) -> None:
        '''
        Update a Project\'s ``last_accessed_by_current_user`` field to the current timestamp.

        This helps keep track of the recent Projects each user has worked on and enables scripts
        and apps to use this information to display "Recent Projects" for users as a convenience.

        .. versionadded::
            Requires Shotgun v5.3.20+

        >>> sg.update_project_last_accessed({"type": "Project", "id": 66},
        ...                                 {"type": "HumanUser", "id": 43})

        :param dict project: Standard Project entity dictionary
        :param dict user: Standard user entity dictionary. This is optional if the current API
            instance is using user-based authenitcation, or has specified ``sudo_as_login``. In
            these cases, if ``user`` is not provided, the ``sudo_as_login`` value or ``login``
            value from the current instance will be used instead.
        '''
    def note_thread_read(self, note_id: int, entity_fields: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        '''
        Return the full conversation for a given note, including Replies and Attachments.

        Returns a complex data structure on the following form::

            [{\'content\': \'Please add more awesomeness to the color grading.\',
              \'created_at\': \'2015-07-14 21:33:28 UTC\',
              \'created_by\': {\'id\': 38,
                             \'name\': \'John Pink\',
                             \'status\': \'act\',
                             \'type\': \'HumanUser\',
                             \'valid\': \'valid\'},
              \'id\': 6013,
              \'type\': \'Note\'},
             {\'created_at\': \'2015-07-14 21:33:32 UTC\',
              \'created_by\': {\'id\': 38,
                             \'name\': \'John Pink\',
                             \'status\': \'act\',
                             \'type\': \'HumanUser\',
                             \'valid\': \'valid\'},
              \'id\': 159,
              \'type\': \'Attachment\'},
             {\'content\': \'More awesomeness added\',
              \'created_at\': \'2015-07-14 21:54:51 UTC\',
              \'id\': 5,
              \'type\': \'Reply\',
              \'user\': {\'id\': 38,
                       \'name\': \'David Blue\',
                       \'status\': \'act\',
                       \'type\': \'HumanUser\',
                       \'valid\': \'valid\'}}]

        The list is returned in descending chronological order.

        If you wish to include additional fields beyond the ones that are
        returned by default, you can specify these in an entity_fields
        dictionary. This dictionary should be keyed by entity type and each
        key should contain a list of fields to retrieve, for example::

            { "Note":       ["created_by.HumanUser.image",
                             "addressings_to",
                             "playlist",
                             "user" ],
              "Reply":      ["content"],
              "Attachment": ["filmstrip_image",
                            "local_storage",
                            "this_file",
                            "image"]
            }

        :param int note_id: The id for the note to be retrieved
        :param dict entity_fields: Additional fields to retrieve as part of the request.
            See above for details.
        :returns: A list of dictionaries. See above for example.
        :rtype: list
        '''
    def text_search(self, text: str, entity_types: dict[str, Any], project_ids: list | None = None, limit: int | None = None) -> dict[str, Any]:
        '''
        Search across the specified entity types for the given text.

        This method can be used to implement auto completion or a Shotgun global search. The method
        requires a text input phrase that is at least three characters long, or an exception will
        be raised.

        Several ways to limit the results of the query are available:

        - Using the ``project_ids`` parameter, you can provide a list of Project ids to search
          across. Leaving this at its default value of ``None`` will search across all Shotgun data.

        - You need to define which subset of entity types to search using the ``entity_types``
          parameter. Each of these entity types can be associated with a filter query to further
          reduce the list of matches. The filter list is using the standard filter syntax used by
          for example the :meth:`~shotgun_api3.Shotgun.find` method.

        **Example: Constrain the search to all Tasks but Character Assets only**

        >>> entity_types = {
        ...     "Asset": [["sg_asset_type", "is", "Character"]],
        ...     "Task": []
        ... }
        >>> sg.text_search("bunny", entity_types)
        {\'matches\': [{\'id\': 734,
                      \'type\': \'Asset\',
                      \'name\': \'Bunny\',
                      \'project_id\': 65,
                      \'image\': \'https://...\',
                      \'links\': [\'\', \'\'],
                      \'status\': \'fin\'},
                      ...
                      {\'id\': 558,
                       \'type\': \'Task\'
                       \'name\': \'FX\',
                       \'project_id\': 65,
                       \'image\': \'https://...\',
                       \'links\': [\'Shot\', \'bunny_010_0010\'],
                       \'status\': \'fin\'}],
            \'terms\': [\'bunny\']}

        The links field will contain information about any linked entity. This is useful when, for
        example, presenting Tasks and you want to display what Shot or Asset the Task is associated
        with.

        :param str text: Text to search for. This must be at least three characters long, or an
            exception will be raised.
        :param dict entity_types: Dictionary to specify which entity types to search across. See
            above for usage examples.
        :param list project_ids: List of Projects to search. By default, all projects will be
            searched.
        :param int limit: Specify the maximum number of matches to return.
        :returns: A complex dictionary structure, see above for example.
        :rtype: dict
        '''
    def activity_stream_read(self, entity_type: str, entity_id: int, entity_fields: dict[str, Any] | None = None, min_id: int | None = None, max_id: int | None = None, limit: int | None = None) -> dict[str, Any]:
        '''
        Retrieve activity stream data from Shotgun.

        This data corresponds to the data that is displayed in the
        Activity tab for an entity in the Shotgun Web UI.

        A complex data structure on the following form will be
        returned from Shotgun::

            {\'earliest_update_id\': 50,
             \'entity_id\': 65,
             \'entity_type\': \'Project\',
             \'latest_update_id\': 79,
             \'updates\': [{\'created_at\': \'2015-07-15 11:06:55 UTC\',
                          \'created_by\': {\'id\': 38,
                                         \'image\': \'6641\',
                                         \'name\': \'John Smith\',
                                         \'status\': \'act\',
                                         \'type\': \'HumanUser\'},
                          \'id\': 79,
                          \'meta\': {\'entity_id\': 6004,
                                   \'entity_type\': \'Version\',
                                   \'type\': \'new_entity\'},
                          \'primary_entity\': {\'id\': 6004,
                                             \'name\': \'Review_turntable_v2\',
                                             \'status\': \'rev\',
                                             \'type\': \'Version\'},
                          \'read\': False,
                          \'update_type\': \'create\'},
                         {...},
                        ]
            }

        The main payload of the return data can be found inside the \'updates\'
        key, containing a list of dictionaries. This list is always returned
        in descending date order. Each item may contain different fields
        depending on their update type. The primary_entity key represents the
        main Shotgun entity that is associated with the update. By default,
        this entity is returned with a set of standard fields. By using the
        entity_fields parameter, you can extend the returned data to include
        additional fields. If for example you wanted to return the asset type
        for all assets and the linked sequence for all Shots, pass the
        following entity_fields::

            {"Shot": ["sg_sequence"], "Asset": ["sg_asset_type"]}

        Deep queries can be used in this syntax if you want to
        traverse into connected data.

        :param str entity_type: Entity type to retrieve activity stream for
        :param int entity_id: Entity id to retrieve activity stream for
        :param dict entity_fields: Dict of additional fields to include.
                              See above for details
        :param int max_id: Do not retrieve ids greater than this id.
                       This is useful when implementing paging.
        :param int min_id: Do not retrieve ids lesser than this id.
                       This is useful when implementing caching of
                       the event stream data and you want to
                       "top up" an existing cache.
        :param int limit: Limit the number of returned records. If not specified,
                      the system default will be used.
        :returns: A complex activity stream data structure. See above for details.
        :rtype: dict
        '''
    def nav_expand(self, path: str, seed_entity_field=None, entity_fields=None):
        """
        Expand the navigation hierarchy for the supplied path.

        .. warning::

            This is an experimental method that is not officially part of the
            python-api. Usage of this method is discouraged. This method's name,
            arguments, and argument types may change at any point.

        """
    def nav_search_string(self, root_path: str, search_string: str, seed_entity_field=None):
        """
        Search function adapted to work with the navigation hierarchy.

        .. warning::

            This is an experimental method that is not officially part of the
            python-api. Usage of this method is discouraged. This method's name,
            arguments, and argument types may change at any point.
        """
    def nav_search_entity(self, root_path: str, entity, seed_entity_field=None):
        """
        Search function adapted to work with the navigation hierarchy.

        .. warning::

            This is an experimental method that is not officially part of the
            python-api. Usage of this method is discouraged. This method's name,
            arguments, and argument types may change at any point.

        """
    def get_session_token(self) -> str:
        """
        Get the session token associated with the current session.

        If a session token has already been established, this is returned, otherwise a new one is
        generated on the server and returned.

        >>> sg.get_session_token()
        dd638be7d07c39fa73d935a775558a50

        :returns: String containing a session token.
        :rtype: str
        """
    def preferences_read(self, prefs: list | None = None) -> dict[str, Any]:
        '''
        Get a subset of the site preferences.

        >>> sg.preferences_read()
        {
            "pref_name": "pref value"
        }

        :param list prefs: An optional list of preference names to return.
        :returns: Dictionary of preferences and their values.
        :rtype: dict
        '''
    def user_subscriptions_read(self) -> list:
        """
        Get the list of user subscriptions.

        :returns: A list of user subscriptions where each subscription is a
            dictionary containing the ``humanUserId`` and ``subscription``
            fields.
        :rtype: list
        """
    def user_subscriptions_create(self, users: list[dict[str, str | list[str] | None]]) -> bool:
        """
        Assign subscriptions to users.

        :param list users: list of user subscriptions to assign.
            Each subscription must be a dictionary with the ``humanUserId`` and
            ``subscription`` fields.
            The ``subscription`` is either ``None``, a single string, or an
            array of strings with subscription information.

        :returns: ``True`` if the request succedeed, ``False`` if otherwise.
        :rtype: bool
        """
    def _build_opener(self, handler) -> urllib.request.OpenerDirector:
        """
        Build urllib2 opener with appropriate proxy handler.
        """
    @classmethod
    def _get_certs_file(cls, ca_certs):
        """
        The following method tells the API where to look for
        certificate authorities certificates (we will be referring to these
        as CAC from now on). Here's how the Python API interacts with those.

        Auth and CRUD operations
        ========================
        These operations are executed with httplib2. httplib2 ships with a
        list of CACs instead of asking Python's ssl module for them.

        Upload/Downloads
        ================
        These operations are executed using urllib2. urllib2 asks a Python
        module called `ssl` for CACs. We have bundled certifi with the API
        so that we can be sure the certs are correct at the time of the API
        release. This does however mean when the certs change we must update
        the API to contain the latest certifi.
        This approach is preferable to not using certifi since, on Windows,
        ssl searches for CACs in the Windows Certificate Store, on
        Linux/macOS, it asks the OpenSSL library linked with Python for CACs.
        Depending on how Python was compiled for a given DCC, Python may be
        linked against the OpenSSL from the OS or a copy of OpenSSL distributed
        with the DCC. This impacts which versions of the certificates are
        available to Python, as an OS level OpenSSL will be aware of system
        wide certificates that have been added, while an OpenSSL that comes
        with a DCC is likely bundling a list of certificates that get update
        with each release and may not contain system wide certificates.

        Using custom CACs
        =================
        When a user requires a non-standard CAC, the SHOTGUN_API_CACERTS
        environment variable allows to provide an alternate location for
        the CACs.

        :param ca_certs: A default cert can be provided
        :return: The cert file path to use.
        """
    def _turn_off_ssl_validation(self) -> None:
        """
        Turn off SSL certificate validation.
        """
    def schema(self, entity_type: str) -> NoReturn:
        """
        .. deprecated:: 3.0.0
           Use :meth:`~shotgun_api3.Shotgun.schema_field_read` instead.
        """
    def entity_types(self) -> NoReturn:
        """
        .. deprecated:: 3.0.0
           Use :meth:`~shotgun_api3.Shotgun.schema_entity_read` instead.
        """
    def _call_rpc(self, method: str, params: Any, include_auth_params: bool = True, first: bool = False) -> Any:
        """
        Call the specified method on the Shotgun Server sending the supplied payload.
        """
    def _auth_params(self) -> dict[str, Any]:
        """
        Return a dictionary of the authentication parameters being used.
        """
    def _sanitize_auth_params(self, params: dict[str, Any]) -> dict[str, Any]:
        """
        Given an authentication parameter dictionary, sanitize any sensitive
        information and return the sanitized dict copy.
        """
    def _build_payload(self, method: str, params, include_auth_params: bool = True) -> dict[str, Any]:
        """
        Build the payload to be send to the rpc endpoint.
        """
    def _encode_payload(self, payload) -> bytes:
        """
        Encode the payload to a string to be passed to the rpc endpoint.

        The payload is json encoded as a unicode string if the content
        requires it. The unicode string is then encoded as 'utf-8' as it must
        be in a single byte encoding to go over the wire.
        """
    def _make_call(self, verb: str, path: str, body, headers: dict[str, Any] | None) -> tuple[tuple[int, str], dict[str, Any], str]:
        """
        Make an HTTP call to the server.

        Handles retry and failure.
        """
    def _http_request(self, verb: str, path: str, body, headers: dict[str, Any]) -> tuple[tuple[int, str], dict[str, Any], str]:
        """
        Make the actual HTTP request.
        """
    def _make_upload_request(self, request, opener: urllib.request.OpenerDirector) -> urllib.request._UrlopenRet:
        """
        Open the given request object, return the
        response, raises URLError on protocol errors.
        """
    def _parse_http_status(self, status: tuple) -> None:
        """
        Parse the status returned from the http request.

        :param tuple status: Tuple of (code, reason).
        :raises: RuntimeError if the http status is non success.
        """
    def _decode_response(self, headers: dict[str, Any], body: str) -> str | dict[str, Any]:
        """
        Decode the response from the server from the wire format to
        a python data structure.

        :param dict headers: Headers from the server.
        :param str body: Raw response body from the server.
        :returns: If the content-type starts with application/json or
            text/javascript the body is json decoded. Otherwise the raw body is
            returned.
        :rtype: str
        """
    def _json_loads(self, body: str): ...
    def _json_loads_ascii(self, body):
        """
        See http://stackoverflow.com/questions/956867
        """
    def _response_errors(self, sg_response) -> None:
        """
        Raise any API errors specified in the response.

        :raises ShotgunError: If the server response contains an exception.
        """
    def _visit_data(self, data: T, visitor) -> T:
        """
        Walk the data (simple python types) and call the visitor.
        """
    def _transform_outbound(self, data: T) -> T:
        """
        Transform data types or values before they are sent by the client.

        - changes timezones
        - converts dates and times to strings
        """
    def _transform_inbound(self, data: T) -> T:
        """
        Transforms data types or values after they are received from the server.
        """
    def _get_connection(self) -> Http:
        """
        Return the current connection or creates a new connection to the current server.
        """
    def _close_connection(self) -> None:
        """
        Close the current connection.
        """
    def _parse_records(self, records: list) -> list:
        """
        Parse 'records' returned from the api to do local modifications:

        - Insert thumbnail urls
        - Insert local file paths.
        - Revert &lt; html entities that may be the result of input sanitization
          mechanisms back to a litteral < character.

        :param records: List of records (dicts) to process or a single record.

        :returns: A list of the records processed.
        """
    def _build_thumb_url(self, entity_type: str, entity_id: int) -> str:
        """
        Return the URL for the thumbnail of an entity given the entity type and the entity id.

        Note: This makes a call to the server for every thumbnail.

        :param str entity_type: Entity type the id is for.
        :param int entity_id: int of the entity to get the thumbnail for.
        :returns: Fully qualified url to the thumbnail.
        """
    def _dict_to_list(self, d: dict[str, Any] | None, key_name: str = 'field_name', value_name: str = 'value', extra_data=None) -> list:
        """
        Utility function to convert a dict into a list dicts using the key_name and value_name keys.

        e.g. d {'foo' : 'bar'} changed to [{'field_name':'foo', 'value':'bar'}]

        Any dictionary passed in via extra_data will be merged into the resulting dictionary.
        e.g. d as above and extra_data of {'foo': {'thing1': 'value1'}} changes into
        [{'field_name': 'foo', 'value': 'bar', 'thing1': 'value1'}]
        """
    def _dict_to_extra_data(self, d: dict | None, key_name: str = 'value') -> dict:
        '''
        Utility function to convert a dict into a dict compatible with the extra_data arg
        of _dict_to_list.

        e.g. d {\'foo\' : \'bar\'} changed to {\'foo\': {"value": \'bar\'}]
        '''
    def _upload_file_to_storage(self, path: str, storage_url: str) -> None:
        """
        Internal function to upload an entire file to the Cloud storage.

        :param str path: Full path to an existing non-empty file on disk to upload.
        :param str storage_url: Target URL for the uploaded file.
        """
    def _multipart_upload_file_to_storage(self, path: str, upload_info: dict[str, Any]) -> None:
        """
        Internal function to upload a file to the Cloud storage in multiple parts.

        :param str path: Full path to an existing non-empty file on disk to upload.
        :param dict upload_info: Contains details received from the server, about the upload.
        """
    def _get_upload_part_link(self, upload_info: dict[str, Any], filename: str, part_number: int) -> str:
        """
        Internal function to get the url to upload the next part of a file to the
        Cloud storage, in a multi-part upload process.

        :param dict upload_info: Contains details received from the server, about the upload.
        :param str filename: Name of the file for which we want the link.
        :param int part_number: Part number for the link.
        :returns: upload url.
        :rtype: str
        """
    def _upload_data_to_storage(self, data: BinaryIO, content_type: str, size: int, storage_url: str) -> str:
        """
        Internal function to upload data to Cloud storage.

        :param stream data: Contains details received from the server, about the upload.
        :param str content_type: Content type of the data stream.
        :param int size: Number of bytes in the data stream.
        :param str storage_url: Target URL for the uploaded file.
        :returns: upload url.
        :rtype: str
        """
    def _complete_multipart_upload(self, upload_info: dict[str, Any], filename: str, etags: Iterable[str]) -> None:
        """
        Internal function to complete a multi-part upload to the Cloud storage.

        :param dict upload_info: Contains details received from the server, about the upload.
        :param str filename: Name of the file for which we want to complete the upload.
        :param tuple etags: Contains the etag of each uploaded file part.
        """
    def _requires_direct_s3_upload(self, entity_type: str, field_name: str | None) -> bool:
        """
        Internal function that determines if an entity_type + field_name combination
        should be uploaded to cloud storage.

        The info endpoint should return `s3_enabled_upload_types` which contains an object like the following:
            {
                'Version': ['sg_uploaded_movie'],
                'Attachment': '*',
                '*': ['this_file']
            }

        :param str entity_type: The entity type of the file being uploaded.
        :param str field_name: The matching field name for the file being uploaded.

        :returns: Whether the field + entity type combination should be uploaded to cloud storage.
        :rtype: bool
        """
    def _send_form(self, url: str, params: dict[str, Any]) -> str:
        """
        Utility function to send a Form to Shotgun and process any HTTP errors that
        could occur.

        :param url: endpoint where the form is sent.
        :param params: form data
        :returns: result from the server.
        """

class CACertsHTTPSConnection(http_client.HTTPConnection):
    ''' "
    This class allows to create an HTTPS connection that uses the custom certificates
    passed in.
    '''
    default_port: Incomplete
    __ca_certs: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        :param args: Positional arguments passed down to the base class.
        :param ca_certs: Path to the custom CA certs file.
        :param kwargs: Keyword arguments passed down to the bas class
        """
    sock: Incomplete
    def connect(self) -> None:
        """Connect to a host on a given (SSL) port."""

class CACertsHTTPSHandler(urllib.request.HTTPHandler):
    """
    Handler that ensures https connections are created with the custom CA certs.
    """
    __ca_certs: Incomplete
    def __init__(self, cacerts) -> None: ...
    def https_open(self, req): ...
    def create_https_connection(self, *args, **kwargs): ...

class FormPostHandler(urllib.request.BaseHandler):
    """
    Handler for multipart form data
    """
    handler_order: Incomplete
    def http_request(self, request): ...
    def encode(self, params, files, boundary=None, buffer=None): ...
    def https_request(self, request): ...

def _translate_filters(filters: list | tuple, filter_operator) -> dict[str, Any]:
    """
    Translate filters params into data structure expected by rpc call.
    """
def _translate_filters_dict(sg_filter: dict[str, Any]) -> dict[str, Any]: ...
def _translate_filters_list(filters): ...
def _translate_filters_simple(sg_filter): ...
def _version_str(version):
    """
    Convert a tuple of int's to a '.' separated str.
    """
def _get_type_and_id_from_value(value):
    """
    For an entity dictionary, returns a new dictionary with only the type and id keys.
    If any of these keys are not present, the original dictionary is returned.
    """
