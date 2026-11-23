from collections.abc import Mapping, Sequence
from houtypes import JSONValue
from typing import TypedDict

class _MaskEntry(TypedDict):
    mask: str
    keypoints: Mapping[int | str, Sequence[float]]

class CocoDataset:
    output_dir: str
    output_path: str
    dataset: Mapping[str, Mapping[int | str, Sequence[_MaskEntry]]]
    class_ids: Sequence[int]
    class_names: Sequence[str]
    class_colors: Sequence[Sequence[float]]
    keypoint_ids: Sequence[int]
    keypoint_names: Sequence[str]
    keypoint_colors: Sequence[Sequence[float]]
    meta_data: dict[str, JSONValue]
    def __init__(self, dataset: Mapping[str, Mapping[int | str, Sequence[_MaskEntry]]] = ..., output_dir: str = '', output_path: str = '', class_ids: Sequence[int] = ..., class_names: Sequence[str] = ..., class_colors: Sequence[Sequence[float]] = ..., keypoint_ids: Sequence[int] = ..., keypoint_names: Sequence[str] = ..., keypoint_colors: Sequence[Sequence[float]] = ..., meta_data: dict[str, JSONValue] = ...) -> None: ...
    def process(self) -> str | None: ...
