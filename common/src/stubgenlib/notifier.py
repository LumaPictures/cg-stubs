from __future__ import absolute_import, annotations, division, print_function

from collections import defaultdict


class Notifier:
    """
    Class to display and filter warnings
    """

    def __init__(self) -> None:
        self._seen_msgs: defaultdict[tuple[str, str, str], int] = defaultdict(int)
        self._seen_keys: defaultdict[str, int] = defaultdict(int)
        self._modules: list[str] | None = None
        self._keys: list[str] | None = None

    def set_modules(self, modules: list[str]) -> None:
        self._modules = modules

    def set_keys(self, keys: list[str]) -> None:
        self._keys = keys

    def warn(self, key: str, module: str, msg: str) -> None:
        if (key, module, msg) not in self._seen_msgs:
            if (self._modules is None or module in self._modules) and (
                self._keys is None or key in self._keys
            ):
                print(f"({module}) {key}: {msg}")
        self._seen_msgs[(key, module, msg)] += 1
        self._seen_keys[key] += 1

    def accumulate(self, key: str) -> None:
        self._seen_keys[key] += 1

    def print_summary(self) -> None:
        print()
        print("Warning Summary:")
        for key in sorted(self._seen_keys):
            count = self._seen_keys[key]
            print(f"  {key}: {count}")

    def get_key_count(self, key: str) -> int:
        return self._seen_keys[key]
