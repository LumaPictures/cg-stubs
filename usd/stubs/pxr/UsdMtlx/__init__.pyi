# mypy: disable-error-code="misc, override, no-redef"

import pxr.Usd

__MFB_FULL_PACKAGE_NAME: str

def _TestFile(pathname: object, nodeGraphs: bool = ...) -> pxr.Usd.Stage: ...
def _TestString(buffer: object, nodeGraphs: bool = ...) -> pxr.Usd.Stage: ...
