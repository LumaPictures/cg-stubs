# mypy: disable-error-code="misc, override, no-redef"

import pxr.Ar
import pxr.Usd
import pxr.UsdShade

__MFB_FULL_PACKAGE_NAME: str

def BakeMaterial(mtlxMaterial: pxr.UsdShade.Material, bakedMtlxDir: str | pxr.Ar.ResolvedPath, textureWidth: int, textureHeight: int, bakeHdr: bool, bakeAverage: bool) -> str:
    """
    Convert the given MaterialX Material from a UsdShadeaMaterial into a
    MaterialX Document and Bake it using MaterialX::TextureBaker, storing
    the resulting mtlx Document at C{bakedMtlxFilename}.


    Any resulting textures from the baking process will live in the same
    directory.
    """
def ReadFileToStage(pathname: object, stage: object) -> pxr.Usd.Stage: ...
