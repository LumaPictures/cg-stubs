import os

def makeUDIMFilename(filename: str, tilex: int, tiley: int, stride: int = 10) -> str:
    """ Generates a UDIM filename by adding _N before the extension
        based on the tilex, tiley, and stride parameters.
    """
def makeUVTileFilename(filename: str, tilex: int, tiley: int, pad: int = 1) -> str:
    """ Generates a UVTile filename by adding _X_Y before the extension
        based on the tilex and tiley parameters. Numbers are zero padded
        to pad digits.
    """
def makeTileSeqFilename(filename: str, tilex: int, tiley: int, stride: int, pad: int = 1) -> str:
    """ Generates a UVTile filename by adding _X_Y before the extension
        based on the tilex and tiley parameters. Numbers are zero padded
        to pad digits.
    """
def makeXYTileFilename(filename: str, tilex: int, tiley: int) -> str:
    """ Generates a XYTile filename by adding _X_Y before the extension
        based on the tilex and tiley parameters. Numbers are zero padded
        to pad digits.
    """
def revealFile(path: str | os.PathLike[str]) -> None:
    """
    Opens the containing folder of the given file in the operating system's
    desktop environment (e.g. Folder, Windows Explorer).
    """
