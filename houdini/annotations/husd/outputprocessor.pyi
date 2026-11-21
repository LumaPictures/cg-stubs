from collections.abc import Mapping, Sequence
from typing import TypeAlias

import hou
from pxr import Sdf

# A value of a UT_Options that Houdini hands an output processor: a bool comes as an int, an
# array as a tuple.
_OptionValue: TypeAlias = int | float | str | tuple[int, ...] | tuple[float, ...] | tuple[str, ...]

class OutputProcessor:
    SHOULD_SAVE_FALSE: int
    SHOULD_SAVE_TRUE: int
    SHOULD_SAVE_NO_OPINION: int
    config_node: hou.OpNode | None
    lop_node: hou.LopNode | None
    t: float | None
    stage_variables: dict[str, _OptionValue] | None
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...
    @staticmethod
    def hidden() -> bool: ...
    @staticmethod
    def name() -> str: ...
    @staticmethod
    def displayName() -> str: ...
    @staticmethod
    def parameters() -> str: ...
    def stageVariables(self) -> dict[str, _OptionValue] | None: ...
    def beginSave(
        self,
        config_node: hou.OpNode,
        config_overrides: Mapping[str, _OptionValue] | None,
        lop_node: hou.LopNode,
        t: float,
        stage_variables: dict[str, _OptionValue],
    ) -> None: ...
    def endSave(
        self,
        config_node: hou.OpNode,
        config_overrides: Mapping[str, _OptionValue] | None,
        lop_node: hou.LopNode,
        t: float,
        stage_variables: dict[str, _OptionValue],
        saved_paths: Sequence[str],
        error_messages: str,
    ) -> None: ...
    def processSavePath(
        self, asset_path: str, referencing_layer_path: str, asset_is_layer: bool
    ) -> str: ...
    def processReferencePath(
        self, asset_path: str, referencing_layer_path: str, asset_is_layer: bool
    ) -> str: ...
    def processReferenceExpression(
        self, asset_expression: str, referencing_layer_path: str, asset_is_layer: bool
    ) -> str: ...
    def processLayer(self, layer: Sdf.Layer, layersavepath: str | None = ...) -> bool: ...
    def shouldSave(self, save_path: str, layer: Sdf.Layer | None) -> int: ...
    def evalConfig(
        self,
        parm_name: str,
        config_node: hou.OpNode | None,
        config_overrides: Mapping[str, _OptionValue] | None,
        t: float,
    ) -> _OptionValue | dict[str, str] | hou.Ramp | hou.Geometry | None: ...
