from collections.abc import Callable

class HprUri:
    # nanobind converts a str of an integer ("4") to the int.
    def setVersion(self, arg: int | str) -> None: ...

class ProjectConfig:
    # The callback gets the shotbuilder.utils.ProjectChangedType value as an int; its result is
    # ignored.
    @staticmethod
    def addProjectChangedCallback(arg: Callable[[int], object]) -> int: ...
