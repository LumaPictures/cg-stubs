import optparse
from collections.abc import Iterable
from io import BufferedReader
from typing import TextIO

usage: str
parser: optparse.OptionParser
options: optparse.Values
args: list[str]
f: BufferedReader | TextIO
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
label: str
outline: str
entry: dict[str, float]
centry: dict[str, float]

def speedUp(slow: float, fast: float) -> float: ...
def amdahlLaw(slow: float, fast: float, nproc: int | None) -> float: ...
def braceSplit(line: Iterable[str]) -> list[str]: ...
def csvSafe(line: str) -> str: ...
def loadFile(file: Iterable[bytes], byname: bool) -> dict[str, dict[str, float]]: ...
