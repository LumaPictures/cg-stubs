from __future__ import absolute_import, print_function

import fnmatch
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class GeneratorDelegate(Generic[T]):
    """Choose a StubGenerator based on module name rules"""

    def __init__(self, rules: dict[str, type[T]], fallback: type[T]):
        """
        Args:
            rules: mapping of module names (supports globs) to StubGenerator type
            fallback: StubGenerator type to use if there are no matches
        """
        self.rules = rules
        self.fallback = fallback

    def __call__(self, module_name: str, *args: Any, **kwargs: Any) -> T:
        for pattern, generator in self.rules.items():
            if fnmatch.fnmatchcase(module_name, pattern):
                return generator(module_name, *args, **kwargs)
        return self.fallback(module_name, *args, **kwargs)
