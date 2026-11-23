import torch
from _typeshed import StrPath as StrPath, SupportsRead, SupportsWrite
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentLayoutFlat as componentLayoutFlat, componentNumel as componentNumel

dimension_byte_count: int
input_coordinate_byte_count: int
target_coordinate_byte_count: int

class LabeledExampleData:
    """
    An array of labeled_examples (input-target pairs).
    """
    input_layout: ComponentLayout
    target_layout: ComponentLayout
    labeled_example_count: int
    labeled_examples: torch.Tensor
    def __init__(self, input_layout: ComponentLayout, target_layout: ComponentLayout, labeled_example_count: int, labeled_examples: torch.Tensor) -> None: ...

class LabeledExampleDataError(Exception):
    """
    Exception type that gets thrown if a data set cannot be formed.
    """
    message: str
    def __init__(self, message: str) -> None: ...

def labeledExampleLayoutFromFile(data_set_file: SupportsRead[bytes], data_set_file_byte_count: int, /, *, log_file: SupportsWrite[str] | None = None) -> tuple[ComponentLayout, ComponentLayout]:
    """
    Extract the layout for each labeled example in the data set.

    The expected byte order is little endian.
    """
def labeledExampleLayoutFromPath(data_set_path: StrPath, log_file: SupportsWrite[str] | None) -> tuple[ComponentLayout, ComponentLayout]:
    """
    Obtain the component layouts of each input and each target from a path to raw data.
    """
def labeledExampleDataFromFile(data_set_file: SupportsRead[bytes], data_set_file_byte_count: int, /, *, shuffle: bool = True, shuffle_random_seed: int = 205, limit_size: bool = False, upper_limit: int = -1, log_file: SupportsWrite[str] | None = None) -> LabeledExampleData:
    """
    Given a raw data file, read an array of labeled_examples,
    optionally shuffle the labeled_examples, and return as LabeledExampleData.

    The expected byte order is little endian.
    """
def labeledExampleDataFromPath(data_set_path: StrPath, /, *, shuffle: bool = True, shuffle_random_seed: int = 205, limit_size: bool = False, upper_limit: int = -1, log_file: SupportsWrite[str] | None = None) -> LabeledExampleData:
    """
    Given a path to a raw data file, read an array of labeled_examples,
    optionally shuffle the labeled_examples, and return as LabeledExampleData.

    The expected byte order is little endian.
    """
