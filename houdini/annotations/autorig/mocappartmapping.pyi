from typing import Literal

autocontrols: dict[str, list[str]]
animcontrols: dict[str, list[str]]
mappings: dict[str, list[str]]
parms: dict[str, list[str]]
useend: dict[str, bool]
customtwist: dict[str, tuple[Literal[False]] | tuple[Literal[True], str, str]]
pretransforms: dict[str, list[str]]
animationchannels: dict[str, list[tuple[str, str]]]
skipstart: dict[str, bool]
extrapositions: dict[str, list[tuple[str, str, tuple[int, int, int]]]]
