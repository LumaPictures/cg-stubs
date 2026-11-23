from collections.abc import Callable, Mapping, Sequence

import jinja2
from jinja2.runtime import Context

from hutil.help.paths import WikiPath
from hutil.help.stores import Store
from hutil.help.blocks import BlockType

def rel(jinctx: Context, pathstring: str, default_ext: str | None = ...) -> str | WikiPath: ...

class Renderer:
    def __init__(self) -> None: ...
    def __call__(self, jinctx: Context, obj: object) -> str: ...

class JinjaStoreLoader(jinja2.BaseLoader):
    store: Store
    prefix: WikiPath
    def __init__(self, store: Store, prefix: str | WikiPath = ...) -> None: ...
    def list_templates(self, extensions: Sequence[str] | None = ..., filter_func: Callable[[str], bool] | None = ...) -> list[str]: ...

def render_block(jinja_env: jinja2.Environment, path: WikiPath, root: BlockType, templatename: str, extras: Mapping[str, object] | None = ..., index_page_name: str = ...) -> str: ...
