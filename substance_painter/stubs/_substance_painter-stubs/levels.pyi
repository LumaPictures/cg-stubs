class LevelsParams:
    clamp: bool
    gamma: float3  # type: ignore[name-defined]
    input_max: float3  # type: ignore[name-defined]
    input_min: float3  # type: ignore[name-defined]
    output_max: float3  # type: ignore[name-defined]
    output_min: float3  # type: ignore[name-defined]
    def __init__(self) -> None: ...
