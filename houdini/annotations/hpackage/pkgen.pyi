from collections.abc import Iterable
from typing import TypedDict

# The template file name (`basic.pkt`, `ocio.pkt`, ...) and the (token, value) pairs to
# substitute in it.
class _NewPackageArgs(TypedDict, total=False):
    template: str
    tokens: Iterable[tuple[str, str]]

def newPackage(kwargs: _NewPackageArgs) -> str | None: ...
