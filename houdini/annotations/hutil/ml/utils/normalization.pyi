import torch.nn

class Normalization:
    def normalization(self, num_features: int) -> torch.nn.BatchNorm2d | torch.nn.InstanceNorm2d | None: ...
