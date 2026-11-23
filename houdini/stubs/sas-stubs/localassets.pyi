import hjsonrpc
import hou
import hutil.api
from collections.abc import Callable as Callable, Iterator, Mapping
from past.builtins import cmp as cmp

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_F = TypeVar('_F')
_P = ParamSpec('_P')
_R = TypeVar('_R')
SUPPORTED_URL_HANDLER_API_VERSION: int
URL_HANDLER_NAME: str

def deferred_decorator(callback_returning_decorator: Callable[[], Callable[[_F], Callable[_P, _R]]]) -> Callable[[_F], Callable[_P, _R]]:
    """This decorator defers another decorator from being called until the
    decorated function is actually called.
    """
def get_sync_information(session_key: str) -> list[str]: ...
def get_store_logged_in_user_name(session_key: str) -> str: ...
def update_installed_asset_from_license_number(server: str, session_key: str, license_number: str) -> None: ...
def install_or_update_asset_from_houdinis_browser(server: str, session_key: str, license_number: str) -> None:
    """This function is called when an asset is launched from inside
    houdini's browser.
    """
def install_or_update_asset_from_license_number(session_data: SessionData, license_number: str) -> None:
    """This function is called when the URL scheme handler is told to install
    an asset.
    """
def check_for_asset_updates(current_user: str, skip_if_checked_recently: bool, display_errors: bool, store_server: str | None = None) -> Iterator[None]: ...
def check_for_shelf_tool_assets(store_server: str | None = None) -> Iterator[None]: ...
def check_for_shelf_tool_assets_wrapper() -> None: ...
def asset_store_dir() -> str: ...

class CurrentUser:
    name: str

def upload_asset_inside_houdini_browser(session_key: str, server: str, author_prefix: str) -> str | None:
    """This function is called when selecting an asset to 
    upload inside Houdini's browser.
    """
def upload_screenshot(server: str, session_key: str, unique_name: str, upload_id: str, x: str | int, y: str | int) -> str:
    """Upload a screenshot from Houdini's browser, during the upload process."""


def begin_upload_with_credentials(node: hou.OpNode | None, session_key: str, store_server: str | None = None) -> None:
    """When uploading from Houdini, the user first needs to log into the
    web site, and then the running Houdini is told to upload the asset via
    the websreponder thread.  The webresponder thread calls this function,
    passing in the session key to prove that the user is logged in.
    """
def begin_uploading_dependent_asset(uploading_node: hou.OpNode, session_key: str, containing_node: hou.OpNode | None = None, store_server: str | None = None) -> None:
    """This function is called both after the user logs in to initiate the
    upload process (i.e. from begin_upload_with_credentials) (in which case
    containing_node won't be passed in), when uploading dependent assets from
    the asset dependencies dialog, and when finally uploading the containing
    asset after completing uploading dependencies (containing_node will be None
    in that case too).
    """
def upload_asset(otl_file: str, session_key: str, server: str | None = None) -> None:
    """This function is called by OPUI_UploadAssetDialog to actually upload
    the asset to the store using the web API.
    """
def prepare_node_for_uploading(node: hou.OpNode, author_prefix: str, store_server: str | None = None) -> hou.OpNode | None:
    """Given an instance of an asset, prepare it for uploading to the store by:
    - making sure the node type and its dependencies are in their own otl files
    - ensuring the asset contains the author's prefix in the namespaced node
      type name

    Returns the node (which may have had its type changed) on success, and None
    if the user cancelled the process.
    """
def create_namespaced_otl(otl_file: str, author_prefix: str, new_node_type_name: str | None = None, new_suffix: str = '-with_author', dependencies_must_be_embedded: bool = True, other_old_to_new_node_types: Mapping[hou.OpNodeType, hou.OpNodeType] | None = None) -> tuple[hou.OpNode, hou.OpNodeType]:
    """Given an otl file with one top-level asset, copy it into an otl file
    with the given suffix and add/change an author prefix to the namespace.

    Returns a (node, old_node_type) tuple, where node is the instance of the
    new namespaced node type.

    See _install_otl_and_get_node_type for information about the
    dependencies_must_be_added parameter.
    """
def file_name_with_suffix(original_file: str, new_suffix: str) -> str: ...

class WebResponderAPI:
    """This class forms the API that the URL scheme handler uses to control
    Houdini.
    """
    port: int
    node_path_to_upload: str | None
    callback_to_return_session_key: Callable[[str], object] | None
    cached_session_key: str | None
    cached_session_key_username: str | None
    def __init__(self, port: int) -> None:
        """Each running copy of Houdini runs a server on a different port."""
    @hjsonrpc.rpcMethod
    def begin_upload_with_credentials(self, session_key: str) -> None: ...
    @hjsonrpc.rpcMethod
    def return_session_key(self, session_key: str, username: str | None) -> None: ...
    def invoke_callback_to_return_cached_session_key(self) -> None: ...
    @hjsonrpc.rpcMethod
    def show_asset_in_running_session(self, node_type_category_name: str, node_type_name: str, current_user: str | None = None) -> None: ...

def update_existing_asset_browsers() -> None: ...
def update_asset_browser() -> hou.AssetBrowser: ...

def show_asset_in_running_session(node_type_category_name: str, node_type_name: str, current_user: str | None = None) -> None:
    """Present a prompt to the user to allow them to decide whether or not
    to open the downloaded asset in their current houdini session, or to open
    a new session. 

    If the asset does not have an example hip file, open the asset browser
    pane in the session and create an instance of the asset.  Otherwise,
    merge the example hip file into the current hip file.
    """
def show_asset_in_newly_launched_session(node_type_category_name: str, node_type_name: str, current_user: str) -> None:
    """Now that a new Houdini session has been started, install the asset
    and create an instance of it.

    This function is invoked from the script that starts a new instance of
    Houdini.
    """
def show_asset_for_node_type(node_type_category_name: str, node_type_name: str) -> None: ...
def ensure_webresponder_server_is_running() -> WebResponderAPI | None: ...
def begin_uploading_asset(node: hou.OpNode, server: str | None = None) -> None: ...
def get_session_key(callback: Callable[[str], object], server: str | None = None, username: str | None = None, force_login: bool = False) -> None: ...

class SessionData(hutil.api.ClientSessionData):
    server: str
    def __init__(self, server: str | None, session_key: str | None) -> None: ...

class StoreAPI(hutil.api.ClientAPIConnection):
    def __init__(self, session_data: SessionData) -> None: ...

def install_url_handler() -> None: ...
