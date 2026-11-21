# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Iterable
from typing import TypedDict

class _NewPackageArgs(TypedDict, total=False):
    template: str
    tokens: Iterable[tuple[str, str]]

def newPackage(kwargs: _NewPackageArgs) -> str | None:
    """ Generate the package content from templates
    """
