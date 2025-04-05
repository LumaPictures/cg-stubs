from __future__ import absolute_import, print_function

from typing import Iterable, Iterator


class Barator:
    def __iter__(self) -> Iterator[str]:
        yield "foo"


class Barable:
    def __iter__(self) -> Iterable[str]:
        yield "foo"


class Barext:
    def __init__(self):
        self.called = False

    def __next__(self) -> str:
        if self.called:
            raise StopIteration
        self.called = True
        return "foo"


class Barator2:
    def __iter__(self) -> Barext:
        return Barext()


"foo" in Barator()
print(list(Barator()))

"foo" in Barable()
print(list(Barable()))

"foo" in Barator2()
print(list(Barator2()))
