import optparse
from collections.abc import Iterable
from io import BufferedReader
from typing import TextIO

options: optparse.Values
args: list[str]
label: str
usage: str
parser: optparse.OptionParser
f: BufferedReader | TextIO

def speedUp(slow: float, fast: float) -> float:
    """ Computes speed up between slow and fast
    """
def amdahlLaw(slow: float, fast: float, nproc: int | None) -> float:
    """ Computes Amdahl's law in reverse to estimate
        efficiency of the function
    """
def braceSplit(line: Iterable[str]) -> list[str]:
    """ Returns a list of tokens from line, split by spaces.
        However, {} will be used as a grouper to ignore spaces
        within the braced component.
    """
def csvSafe(line: str) -> str:
    """ Munges line so it is safe for CSV files, specifically
        by replacing , with ;
    """
def loadFile(file: Iterable[bytes], byname: bool) -> dict[str, dict[str, float]]:
    """ Loads from the file handle file and returns dictionary
        of dictionary of results.
    """

data: dict[str, dict[str, float]]
cheader: str
cf: BufferedReader
cdata: dict[str, dict[str, float]]
labels: list[str]
totals: dict[str, float]
averages: dict[str, float]
counts: dict[str, float]
minimums: dict[str, float]
maximums: dict[str, float]
outline: str
entry: dict[str, float]
centry: dict[str, float]
