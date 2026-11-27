import abc
import hou
from collections.abc import Iterator
from contextlib import contextmanager as contextmanager
from kinefx import rigapi as rigapi
from typing import Self

PYTHON_FILE_NAME: str
ALWAYS_REIMPORT: bool

class Key:
    PELVIS: str
    SPINE: str
    NECK: str
    HEAD: str
    L_ARM: str
    R_ARM: str
    L_HAND: str
    R_HAND: str
    L_LEG: str
    R_LEG: str
    L_FOOT: str
    R_FOOT: str
    ROOT: str
    L_CLAVICLE: str
    R_CLAVICLE: str
    L_KNEE: str
    R_KNEE: str
    L_ELBOW: str
    R_ELBOW: str
    L_BALL: str
    R_BALL: str
    L_THUMB: str
    L_INDEX: str
    L_MIDDLE: str
    L_RING: str
    L_PINKY: str
    R_THUMB: str
    R_INDEX: str
    R_MIDDLE: str
    R_RING: str
    R_PINKY: str
    @classmethod
    def required(c: type[Self]) -> list[str]: ...
    @classmethod
    def optional(c: type[Self]) -> list[str]: ...

class CharacterizeException(Exception): ...

class Matcher(abc.ABC, metaclass=abc.ABCMeta):
    skeleton: rigapi.GeoSkeleton
    mapping: dict[str, str]
    name: str
    @abc.abstractmethod
    def prefixSeparators(self) -> list[str]: ...
    @abc.abstractmethod
    def match(self) -> None: ...
    def __init__(self, node: hou.SopNode) -> None: ...
    def iterPoints(self) -> Iterator[rigapi.KinefxPoint]: ...
    def matchName(self, a: str, b: str) -> bool: ...
    def findExactName(self, name: str, key: str) -> None:
        """
        Finds an exact matching name and stores it in self.mapping
        """
    def findLastWithName(self, name: str, start_index: int, key: str) -> None:
        '''
        Finds the joint with the last matching number. 
        Ie
        findLastWithName("spine", 1, Key.SPINE) 
        1. Try to find                      "spine1"
        2. If it finds it, tries to  find   "spine2"
        3. If it cant find "spine3" it will store "spine2" and exit
        '''
    def findChain(self, name: str, index: int, key: str, key_index: int = 0) -> None:
        """
        findChain()
        """
    def doMatch(self, *, check_required: bool) -> None: ...

def get_template_files() -> tuple[str, ...]: ...
def find_and_import() -> list[type[Matcher]]: ...
def get_matchers() -> list[type[Matcher]]:
    """ Using the subclasses function of the MatcherBase we can figure out
    what classes that has been registered. If the list is empty we try to import everything """
def do_auto_match(node: hou.SopNode) -> Matcher | None: ...
