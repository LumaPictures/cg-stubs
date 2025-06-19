from collections.abc import Generator
from contextlib import contextmanager
from typing import NoReturn

@contextmanager
def with_noop() -> Generator[None]: ...
def reraise(exc, new_exc_cls) -> NoReturn: ...
