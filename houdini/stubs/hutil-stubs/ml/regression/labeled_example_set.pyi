import torch
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentNumel as componentNumel, componentShapes as componentShapes
from hutil.ml.regression.data_set import LabeledExampleData as LabeledExampleData
from hutil.ml.regression.flat_concat_reshaper import unflattenTensors as unflattenTensors

class FlatLabeledExampleSet(torch.utils.data.Dataset):
    """
    Utility for iterating through labeled_examples.
    
    This is designed to work with DataLoader.
    Each returned labeled example is a pair consisting of
    a flat input tensor and a flat target tensor.
    """
    def __init__(self, input_layout: ComponentLayout, target_layout: ComponentLayout, labeled_examples: torch.Tensor, /, *, device: str | torch.device) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i: int) -> tuple[torch.Tensor, torch.Tensor]: ...

class LabeledExampleLoader:
    """
    Allow labeled examples to be loaded in shaped form, rather than flat
    """
    def __init__(self, /, *, labeled_example_data: LabeledExampleData, begin: int, size: int, max_batch_size: int, shuffle: bool = True, device: str | torch.device) -> None: ...
    def flatLoader(self) -> torch.utils.data.DataLoader[tuple[torch.Tensor, torch.Tensor]]: ...
    def unflattenInputs(self, concat_flat_inputs: torch.Tensor) -> tuple[torch.Tensor, ...]: ...
    def unflattenTargets(self, concat_flat_targets: torch.Tensor) -> tuple[torch.Tensor, ...]: ...
