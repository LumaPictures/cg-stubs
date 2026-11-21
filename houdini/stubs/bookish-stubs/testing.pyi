# Houdini stubs generated from Houdini 22.0.466

from bookish import functions as functions, paths as paths, util as util
from bookish.wiki.wikipages import WikiPages as WikiPages
from collections.abc import Callable as Callable

def find_missing(pages: WikiPages, images: bool = True, links: bool = True, prefix: str = '/', callback: Callable[[str], object] | None = None) -> tuple[list[tuple[str, str, str]], set[str]]: ...
