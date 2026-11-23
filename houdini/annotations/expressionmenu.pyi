from collections.abc import Iterable, Sequence

from houtypes import ParmMenuScriptKwargs

def ensureExpressionsAreLoaded() -> None: ...
def buildExpressionsMenu(
    snippetnames: str | Iterable[str],
    multiparm_indices: Sequence[int] = ...,
    kwargs: ParmMenuScriptKwargs = ...,
) -> list[str]: ...
