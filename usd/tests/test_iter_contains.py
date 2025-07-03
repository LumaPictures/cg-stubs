from __future__ import absolute_import, print_function

from typing import Iterable, Iterator


class ImplementsIter:
    def __iter__(self) -> Iterator[str]:
        yield "foo"


class ImplementsIter2:
    def __iter__(self) -> Iterable[str]:
        yield "foo"


class ImplementsNext:
    def __init__(self):
        self.called = False

    def __next__(self) -> str:
        if self.called:
            raise StopIteration
        self.called = True
        return "foo"


class ImplementsIter3:
    def __iter__(self) -> ImplementsNext:
        return ImplementsNext()


class ProperIterator:
    def __init__(self):
        self.called = False

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.called:
            raise StopIteration
        self.called = True
        return "foo"


def test_contains():
    # even though these all work at runtime, mypy complains.
    # see https://github.com/LumaPictures/cg-stubs/issues/9
    assert "foo" in ImplementsIter()
    print(list(ImplementsIter()))  # type: ignore[call-overload]

    assert "foo" in ImplementsIter2()  # type: ignore[operator]
    print(list(ImplementsIter2()))  # type: ignore[call-overload]

    assert "foo" in ImplementsIter3()  # type: ignore[operator]
    print(list(ImplementsIter3()))  # type: ignore[call-overload]

    assert "foo" in ProperIterator()
    print(list(ProperIterator()))
