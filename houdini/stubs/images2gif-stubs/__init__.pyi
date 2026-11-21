# Houdini stubs generated from Houdini 22.0.466

import numpy
import numpy.typing as npt
import typing
from PIL import Image
from _typeshed import StrPath as StrPath, SupportsWrite
from collections.abc import Iterable, Sequence
from scipy.spatial import cKDTree
from typing import Literal

from typing import TypeAlias
from typing import Any
from typing import TypeAlias
_Array: TypeAlias = npt.NDArray[numpy.number[Any]]
_Image: TypeAlias = Image.Image | _Array
def get_cKDTree() -> type[cKDTree] | None: ...
def checkImages(images: Iterable[_Image]) -> list[_Image]:
    """ checkImages(images)
    Check numpy images and correct intensity range etc.
    The same for all movie formats.
    """
def intToBin(i: int) -> bytes:
    """ Integer to two bytes """

class GifWriter:
    """ GifWriter()

    Class that contains methods for helping write the animated GIF file.

    """
    def getheaderAnim(self, im: Image.Image) -> bytes:
        """ getheaderAnim(im)

        Get animation header. To replace PILs getheader()[0]

        """
    def getImageDescriptor(self, im: Image.Image, xy: tuple[int, int] | None = None) -> bytes:
        """ getImageDescriptor(im, xy=None)

        Used for the local color table properties per image.
        Otherwise global color table applies to all frames irrespective of
        whether additional colors comes in play that require a redefined
        palette. Still a maximum of 256 color per frame, obviously.

        Written by Ant1 on 2010-08-22
        Modified by Alex Robinson in Janurary 2011 to implement subrectangles.

        """
    def getAppExt(self, loops: float = ...) -> bytes:
        """ getAppExt(loops=float('inf'))

        Application extension. This part specifies the amount of loops.
        If loops is 0 or inf, it goes on infinitely.

        """
    def getGraphicsControlExt(self, duration: float = 0.1, dispose: int = 2) -> bytes:
        """ getGraphicsControlExt(duration=0.1, dispose=2)

        Graphics Control Extension. A sort of header at the start of
        each image. Specifies duration and transparancy.

        Dispose
        -------
          * 0 - No disposal specified.
          * 1 - Do not dispose. The graphic is to be left in place.
          * 2 - Restore to background color. The area used by the graphic
            must be restored to the background color.
          * 3 -\tRestore to previous. The decoder is required to restore the
            area overwritten by the graphic with what was there prior to
            rendering the graphic.
          * 4-7 -To be defined.

        """
    def handleSubRectangles(self, images: list[_Image], subRectangles: bool | Sequence[tuple[int, int]]) -> tuple[list[_Image], list[tuple[int, int]]]:
        """ handleSubRectangles(images)

        Handle the sub-rectangle stuff. If the rectangles are given by the
        user, the values are checked. Otherwise the subrectangles are
        calculated automatically.

        """
    def getSubRectangles(self, ims: list[_Array]) -> tuple[list[_Array], list[tuple[int, int]]]:
        """ getSubRectangles(ims)

        Calculate the minimal rectangles that need updating each frame.
        Returns a two-element tuple containing the cropped images and a
        list of x-y positions.

        Calculating the subrectangles takes extra time, obviously. However,
        if the image sizes were reduced, the actual writing of the GIF
        goes faster. In some cases applying this method produces a GIF faster.

        """
    def convertImagesToPIL(self, images: Iterable[_Image], dither: bool, nq: int = 0) -> list[Image.Image]:
        """ convertImagesToPIL(images, nq=0)

        Convert images to Paletted PIL images, which can then be
        written to a single animated GIF.

        """
    def writeGifToFile(self, fp: SupportsWrite[bytes], images: Sequence[Image.Image], durations: Sequence[float], loops: int, xys: Sequence[tuple[int, int]], disposes: Sequence[int]) -> int:
        """ writeGifToFile(fp, images, durations, loops, xys, disposes)

        Given a set of images writes the bytes to the specified stream.

        """

def writeGif(filename: StrPath, images: Sequence[_Image], duration: float | Sequence[float] = 0.1, repeat: bool | int = True, dither: bool = False, nq: int = 0, subRectangles: bool | Sequence[tuple[int, int]] = True, dispose: int | Sequence[int] | None = None) -> None:
    """ writeGif(filename, images, duration=0.1, repeat=True, dither=False,
                    nq=0, subRectangles=True, dispose=None)

    Write an animated gif from the specified images.

    Parameters
    ----------
    filename : string
        The name of the file to write the image to.
    images : list
        Should be a list consisting of PIL images or numpy arrays.
        The latter should be between 0 and 255 for integer types, and
        between 0 and 1 for float types.
    duration : scalar or list of scalars
        The duration for all frames, or (if a list) for each frame.
    repeat : bool or integer
        The amount of loops. If True, loops infinitetely.
    dither : bool
        Whether to apply dithering
    nq : integer
        If nonzero, applies the NeuQuant quantization algorithm to create
        the color palette. This algorithm is superior, but slower than
        the standard PIL algorithm. The value of nq is the quality
        parameter. 1 represents the best quality. 10 is in general a
        good tradeoff between quality and speed. When using this option,
        better results are usually obtained when subRectangles is False.
    subRectangles : False, True, or a list of 2-element tuples
        Whether to use sub-rectangles. If True, the minimal rectangle that
        is required to update each frame is automatically detected. This
        can give significant reductions in file size, particularly if only
        a part of the image changes. One can also give a list of x-y
        coordinates if you want to do the cropping yourself. The default
        is True.
    dispose : int
        How to dispose each frame. 1 means that each frame is to be left
        in place. 2 means the background color should be restored after
        each frame. 3 means the decoder should restore the previous frame.
        If subRectangles==False, the default is 2, otherwise it is 1.

    """
@typing.overload
def readGif(filename: StrPath, asNumpy: Literal[True] = ...) -> list[npt.NDArray[numpy.uint8]]: ...
@typing.overload
def readGif(filename: StrPath, asNumpy: Literal[False]) -> list[Image.Image]: ...
@typing.overload
def readGif(filename: StrPath, asNumpy: bool = ...) -> list[npt.NDArray[numpy.uint8]] | list[Image.Image]: ...

class NeuQuant:
    ''' NeuQuant(image, samplefac=10, colors=256)

    samplefac should be an integer number of 1 or higher, 1
    being the highest quality, but the slowest performance.
    With avalue of 10, one tenth of all pixels are used during
    training. This value seems a nice tradeoff between speed
    and quality.

    colors is the amount of colors to reduce the image to. This
    should best be a power of two.

    See also:
    http://members.ozemail.com.au/~dekker/NEUQUANT.HTML

    License of the NeuQuant Neural-Net Quantization Algorithm
    ---------------------------------------------------------

    Copyright (c) 1994 Anthony Dekker
    Ported to python by Marius van Voorden in 2010

    NEUQUANT Neural-Net quantization algorithm by Anthony Dekker, 1994.
    See "Kohonen neural networks for optimal colour quantization"
    in "network: Computation in Neural Systems" Vol. 5 (1994) pp 351-367.
    for a discussion of the algorithm.
    See also  http://members.ozemail.com.au/~dekker/NEUQUANT.HTML

    Any party obtaining a copy of these files from the author, directly or
    indirectly, is granted, free of charge, a full and unrestricted irrevocable,
    world-wide, paid up, royalty-free, nonexclusive right and license to deal
    in this software and documentation files (the "Software"), including without
    limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons who receive
    copies from any such party to do so, with the only requirement being
    that this copyright notice remain intact.

    '''
    NCYCLES: int
    NETSIZE: int
    SPECIALS: int
    BGCOLOR: int
    CUTNETSIZE: int
    MAXNETPOS: int
    INITRAD: int
    RADIUSBIASSHIFT: int
    RADIUSBIAS: int
    INITBIASRADIUS: int
    RADIUSDEC: int
    ALPHABIASSHIFT: int
    INITALPHA: int
    GAMMA: float
    BETA: float
    BETAGAMMA: float
    network: npt.NDArray[numpy.float64]
    colormap: npt.NDArray[numpy.int32]
    netindex: npt.NDArray[numpy.int32]
    bias: npt.NDArray[numpy.float64]
    freq: npt.NDArray[numpy.float64]
    pimage: Image.Image | None
    PRIME1: int
    PRIME2: int
    PRIME3: int
    PRIME4: int
    MAXPRIME: int
    pixels: npt.NDArray[numpy.uint32] | None
    samplefac: int
    a_s: dict[tuple[float, int], npt.NDArray[numpy.float64]]
    def setconstants(self, samplefac: int, colors: int) -> None: ...
    def __init__(self, image: Image.Image, samplefac: int = 10, colors: int = 256) -> None: ...
    def writeColourMap(self, rgb: bool, outstream: SupportsWrite[numpy.int32]) -> int: ...
    def setUpArrays(self) -> None: ...
    def altersingle(self, alpha: float, i: int | numpy.intp, b: int | numpy.uint32, g: int | numpy.uint32, r: int | numpy.uint32) -> None:
        """Move neuron i towards biased (b,g,r) by factor alpha"""
    def geta(self, alpha: float, rad: int) -> npt.NDArray[numpy.float64]: ...
    def alterneigh(self, alpha: float, rad: int, i: int | numpy.intp, b: int | numpy.uint32, g: int | numpy.uint32, r: int | numpy.uint32) -> None: ...
    def contest(self, b: int | numpy.uint32, g: int | numpy.uint32, r: int | numpy.uint32) -> numpy.intp:
        """ Search for biased BGR values
                Finds closest neuron (min dist) and updates self.freq
                finds best neuron (min dist-self.bias) and returns position
                for frequently chosen neurons, self.freq[i] is high and self.bias[i] is negative
                self.bias[i] = self.GAMMA*((1/self.NETSIZE)-self.freq[i])"""
    def specialFind(self, b: int | numpy.uint32, g: int | numpy.uint32, r: int | numpy.uint32) -> int: ...
    def learn(self) -> None: ...
    def fix(self) -> None: ...
    def inxbuild(self) -> None: ...
    def paletteImage(self) -> Image.Image:
        """ PIL weird interface for making a paletted image: create an image which
            already has the palette, and use that in Image.quantize. This function
            returns this palette image. """
    def quantize(self, image: Image.Image) -> Image.Image:
        """ Use a kdtree to quickly find the closest palette colors for the pixels """
    def quantize_with_scipy(self, image: Image.Image) -> Image.Image: ...
    def quantize_without_scipy(self, image: Image.Image) -> Image.Image:
        '''" This function can be used if no scipy is availabe.
        It\'s 7 times slower though.
        '''
    def convert(self, *color: int | numpy.uint8) -> npt.NDArray[numpy.int32]: ...
    def inxsearch(self, r: int | numpy.uint8, g: int | numpy.uint8, b: int | numpy.uint8) -> numpy.intp:
        """Search for BGR values 0..255 and return colour index"""
