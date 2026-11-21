# Houdini stubs generated from Houdini 22.0.466

import jinja2
import weakref
from bookish import functions as functions, paths as paths, util as util
from bookish.stores import Store as Store
from bookish.wiki.wikipages import _WikiContent
from collections.abc import Callable as Callable, Container, Generator, Mapping
from jinja2.runtime import Context as JinjaContext

class JinjaStoreLoader(jinja2.BaseLoader):
    """
    Jinja template loader that loads templates from a Bookish storage object.
    """
    store: weakref.ReferenceType[Store]
    prefix: str
    def __init__(self, store: Store, prefix: str = '/templates/') -> None: ...
    def get_source(self, environment: jinja2.Environment, template_path: str) -> tuple[str, str | None, Callable[[], bool]]: ...
    def list_templates(self, extensions: Container[str] | None = None, filter_func: Callable[[str], object] | None = None) -> Generator[str, None, None]: ...

class Stylesheet:
    env: jinja2.Environment
    templatename: str
    index_page_name: str
    def __init__(self, env: jinja2.Environment, templatename: str, index_page_name: str) -> None: ...
    @staticmethod
    def default_rule(jinctx: JinjaContext, obj: object, render: Callable[[JinjaContext, object], str]) -> str: ...
    def context_and_function(self, basepath: str, jsondata: _WikiContent, extras: Mapping[str, object] | None = None) -> tuple[JinjaContext, Callable[[JinjaContext, object], str]]:
        """
        Returns a Jinja context function you can use to transform a JSON
        document using the rules contained in this style's template.
        """
    def render(self, basepath: str, jsondata: _WikiContent) -> str: ...
