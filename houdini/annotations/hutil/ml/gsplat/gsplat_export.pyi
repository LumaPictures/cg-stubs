from collections.abc import Sequence
from typing import NotRequired, TypedDict

import torch

class _FeatureMeta(TypedDict):
    name: str
    start: int
    width: int
    export: NotRequired[bool]

def splat2ply_bytes(
    means: torch.Tensor,
    scales: torch.Tensor,
    quats: torch.Tensor,
    opacities: torch.Tensor,
    sh0: torch.Tensor,
    shN: torch.Tensor,
    extra_features: torch.Tensor | None = ...,
    feature_meta: Sequence[_FeatureMeta] | None = ...,
) -> bytes: ...
