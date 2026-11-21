from typing import TypeAlias

# A value of a parameter in a dictionary attribute made by attributefromparameters: toggles are
# bools, menus ints (or strs for string menus), and vector parameters lists of floats.
_ParmValue: TypeAlias = bool | int | float | str | list[float]

training_parms: dict[str, _ParmValue]
ply_file: str
viewer_scale: float
feature: str
port: int
module_name: str
