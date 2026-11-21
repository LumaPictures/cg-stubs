# Houdini stubs generated from Houdini 22.0.466

from pxr import Sdf as Sdf, Usd

def slapcomp_tempname(path: Sdf.Path) -> str:
    """ Return a temporary name for a slapcomp primitive based on the USD prim """
def slapcomp_filterlist(stage: Usd.Stage, prim: Usd.Prim, frame: float, aovs: str, caovs: str, name: str = '') -> bool:
    """
        Create or update a Houdini COP Filter List primitive based on a USD
        HoudiniImageFilterList primitive given by the prim argument.

        If the filter list doesn't exist, or if the filter list has bad
        topology (incorrect number/type of children), it will be recreated.

        The values of all the contained filters will be update to reflect the
        current time.

        If the name is specified, it will be used as the filter list name,
        otherwise a temporary name will be generated based on the primitive
        path.
    """
