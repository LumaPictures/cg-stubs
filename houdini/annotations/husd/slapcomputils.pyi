from pxr import Sdf, Usd

def slapcomp_tempname(path: Sdf.Path) -> str: ...
def slapcomp_filterlist(
    stage: Usd.Stage,
    prim: Usd.Prim,
    frame: float,
    aovs: str,
    caovs: str,
    name: str = ...,
) -> bool: ...
