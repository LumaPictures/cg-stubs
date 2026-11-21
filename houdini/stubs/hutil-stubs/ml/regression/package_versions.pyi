# Houdini stubs generated from Houdini 22.0.466

import typing
from _typeshed import SupportsWrite

class VersionTable:
    """ Stores versions of packages and opsets that are relevant for training """
    torch_major: int | None
    torch_minor: int | None
    torch_patch: int | None
    onnx_opset_version: int | None
    def __init__(self, work_item: object, log: object) -> None: ...

@typing.overload
def determineVersions(*, log: None = ...) -> None: ...
@typing.overload
def determineVersions(*, log: SupportsWrite[str]) -> type[VersionTable]: ...
