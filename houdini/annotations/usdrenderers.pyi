from collections.abc import Container
from typing import TypeAlias

from houtypes import JSONValue
from typing_extensions import TypedDict

# A renderer's entry in UsdRenderers.json (see the HDK's "Hydra Render Delegates" page). The
# file can hold keys for other renderers and Houdini versions, so others are allowed.
_RendererInfo = TypedDict(
    "_RendererInfo",
    {
        "inherit_from": str,
        # An `env:` or `platform:` expression in the file, resolved to a bool when loaded.
        "valid": bool | str,
        "menulabel": str,
        "menupriority": int,
        "complexitymultiplier": float,
        "aovsupport": bool,
        "needsdepth": bool,
        "depthstyle": str,
        "drawmodesupport": bool,
        "needsselection": bool,
        "allowbackgroundupdate": bool,
        "pauseonupdate": bool,
        "viewportrenderer": bool,
        "showhydraprocedurals": bool,
        "defaultpurposes": list[str],
        "restartrendersettings": list[str],
        "restartcamerasettings": list[str],
        "diskproducttypes": list[str],
        "viewstats": list[str],
        "statsdatapaths": dict[str, str],
        "qmlTemplate": str,
        "husk.default_output": str,
        "husk.fast-exit": int,
        "husk.metadata": dict[str, str],
        "husk.stats_metadata": str,
        "husk.verbose_callback": str,
        "husk.verbose_interval": float,
    },
    total=False,
    extra_items=JSONValue,  # type: ignore[call-arg]
)

# Renderer (delegate) name -> its UsdRenderers.json entry.
theDataMap: dict[str, _RendererInfo] | None
env_prefix: str
platform_prefix: str
relative_path_keys: tuple[str, ...]

def resolve_inherit_from(
    name: str, base: _RendererInfo, datamap: dict[str, _RendererInfo]
) -> _RendererInfo: ...
def resolve_env_vars(info: _RendererInfo) -> bool: ...
def resolve_relative_paths(
    base_pathstr: str, file_data: dict[str, _RendererInfo]
) -> dict[str, _RendererInfo]: ...
def getDataMap() -> dict[str, _RendererInfo]: ...
def isSupported(name: str, renderers: Container[str], default: bool = ...) -> bool: ...
def getRendererInfo(name: str, display_name: str) -> _RendererInfo: ...
