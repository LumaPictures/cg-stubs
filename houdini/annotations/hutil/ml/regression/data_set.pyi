import torch
from _typeshed import StrPath, SupportsRead, SupportsWrite
from hutil.ml.regression.data_layout import ComponentLayout

dimension_byte_count: int
input_coordinate_byte_count: int
target_coordinate_byte_count: int

class LabeledExampleData:
    input_layout: ComponentLayout
    target_layout: ComponentLayout
    labeled_example_count: int
    labeled_examples: torch.Tensor
    def __init__(self, input_layout: ComponentLayout, target_layout: ComponentLayout, labeled_example_count: int, labeled_examples: torch.Tensor) -> None: ...

class LabeledExampleDataError(Exception):
    message: str
    def __init__(self, message: str) -> None: ...

def labeledExampleLayoutFromFile(data_set_file: SupportsRead[bytes], data_set_file_byte_count: int, /, *, log_file: SupportsWrite[str] | None = ...) -> tuple[ComponentLayout, ComponentLayout]: ...
def labeledExampleLayoutFromPath(data_set_path: StrPath, log_file: SupportsWrite[str] | None) -> tuple[ComponentLayout, ComponentLayout]: ...
def labeledExampleDataFromFile(data_set_file: SupportsRead[bytes], data_set_file_byte_count: int, /, *, shuffle: bool = ..., shuffle_random_seed: int = ..., limit_size: bool = ..., upper_limit: int = ..., log_file: SupportsWrite[str] | None = ...) -> LabeledExampleData: ...
def labeledExampleDataFromPath(data_set_path: StrPath, /, *, shuffle: bool = ..., shuffle_random_seed: int = ..., limit_size: bool = ..., upper_limit: int = ..., log_file: SupportsWrite[str] | None = ...) -> LabeledExampleData: ...
