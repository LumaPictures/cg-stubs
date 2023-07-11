# mypy: disable-error-code="misc, override, no-redef"

import pxr.Ar
import pxr.Usd
import pxr.UsdShade

__MFB_FULL_PACKAGE_NAME: str

def BakeMaterial(mtlxMaterial: pxr.UsdShade.Material, bakedMtlxDir: str | pxr.Ar.ResolvedPath, textureWidth: int, textureHeight: int, bakeHdr: bool, bakeAverage: bool) -> str: ...
def ReadFileToStage(pathname: object, stage: object) -> pxr.Usd.Stage: ...
