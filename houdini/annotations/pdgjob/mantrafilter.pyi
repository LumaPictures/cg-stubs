from collections.abc import Iterable, Sequence

# Each asset is a list [name, [[file, filetype], ...]].
def filterOutputAssets(assets: Iterable[Sequence[str | Sequence[Sequence[str | int]]]]) -> None: ...
