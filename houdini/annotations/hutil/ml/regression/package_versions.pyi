from _typeshed import SupportsWrite
from typing import overload

class VersionTable:
    torch_major: int | None
    torch_minor: int | None
    torch_patch: int | None
    onnx_opset_version: int | None
    def __init__(self, work_item: object, log: object) -> None: ...

@overload
def determineVersions(*, log: None = ...) -> None: ...
@overload
def determineVersions(*, log: SupportsWrite[str]) -> type[VersionTable]: ...
