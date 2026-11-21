# Houdini stubs generated from Houdini 22.0.466

import jinja2
from . import functions as functions
from .blocks import BlockType as BlockType, SpanType as SpanType, WikiType as WikiType
from .paths import WikiPath as WikiPath
from .stores import Store as Store
from collections.abc import Mapping
from jinja2.runtime import Context as Context
from markupsafe import Markup as Markup
from time import perf_counter as perf_counter
from typing import Callable as Callable, Sequence

@jinja2.pass_context
def rel(jinctx: Context, pathstring: str, default_ext: str | None = '.html') -> str | WikiPath: ...

class Renderer:
    def __init__(self) -> None: ...
    def __call__(self, jinctx: Context, obj: object) -> str: ...
    def default_rule(self, jinctx: Context, block: WikiType) -> str: ...

class JinjaStoreLoader(jinja2.BaseLoader):
    """
    Jinja template loader that loads templates from a storage object.
    """
    store: Store
    prefix: WikiPath
    def __init__(self, store: Store, prefix: str | WikiPath = '/templates/') -> None: ...
    def get_source(self, environment: jinja2.Environment, template_path: str) -> tuple[str, str, Callable[[], bool]]: ...
    def list_templates(self, extensions: Sequence[str] | None = None, filter_func: Callable[[str], bool] | None = None) -> list[str]: ...

def render_block(jinja_env: jinja2.Environment, path: WikiPath, root: BlockType, templatename: str, extras: Mapping[str, object] | None = None, index_page_name: str = 'index') -> str: ...
