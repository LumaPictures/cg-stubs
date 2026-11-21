from collections.abc import Callable

from bookish.wiki.wikipages import WikiPages

def find_missing(
    pages: WikiPages,
    images: bool = ...,
    links: bool = ...,
    prefix: str = ...,
    callback: Callable[[str], object] | None = ...,
) -> tuple[list[tuple[str, str, str]], set[str]]: ...
