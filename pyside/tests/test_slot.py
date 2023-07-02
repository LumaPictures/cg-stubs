from typing import Callable, TypeVar, Type, overload, Any

from PySide2.QtCore import Slot


def test():
    some_str: str
    some_int: int

    @Slot(int)
    def f_int_returns_str1(i: int) -> str:
        return "abc"

    some_str = f_int_returns_str1(33)
    some_int = f_int_returns_str1(33)  # type: ignore[assignment]
    some_str = f_int_returns_str1("abc")  # type: ignore[arg-type]

    @Slot(int, result=str)
    def f_int_returns_str2(i: int) -> str:
        return "abc"

    some_str = f_int_returns_str2(33)
    some_int = f_int_returns_str2(33)  # type: ignore[assignment]

    @Slot(int, result=int)  # type: ignore[arg-type]
    def f_int_returns_str3(i: int) -> str:
        return "abc"

    @Slot(int, float)
    def f_int_float_returns_str1(i: int, f: float) -> str:
        return "abc"

    some_str = f_int_float_returns_str1(33, 1.0)
    some_int = f_int_float_returns_str1(33, 1.0)  # type: ignore[assignment]
    some_str = f_int_float_returns_str1("abc", 1.0)  # type: ignore[arg-type]
    some_str = f_int_float_returns_str1(33, "abc")  # type: ignore[arg-type]

    @Slot(int, float, result=int)  # type: ignore[arg-type]
    def f_int_float_returns_str2(i: int, f: float) -> str:
        return "abc"

    @Slot(int, float, str)
    def f_int_float_str_returns_str1(i: int, f: float, s: str) -> str:
        return "abc"

    some_str = f_int_float_str_returns_str1(33, 1.0, "abc")
    some_int = f_int_float_str_returns_str1(33, 1.0, "abc")  # type: ignore[assignment]
    some_str = f_int_float_str_returns_str1("abc", "abc", 33)  # type: ignore[arg-type]

    @Slot(int, float, str, result=float)  # type: ignore[arg-type]
    def f_int_float_str_returns_str2(i: int, f: float, s: str) -> str:
        return "abc"

    @Slot(int, float, str, int)
    def f_int_float_str_int_returns_str1(i: int, f: float, s: str, i2: int) -> str:
        return "abc"

    some_str = f_int_float_str_int_returns_str1(33, 1.0, "abc", 33)
    some_int = f_int_float_str_int_returns_str1(33, 1.0, "abc", 33)  # type: ignore[assignment]
    some_str = f_int_float_str_int_returns_str1(33, 1.0, "abc", "abc")  # type: ignore[arg-type]

    @Slot(int, float, str, int, result=float)  # type: ignore[arg-type]
    def f_int_float_str_int_returns_str2(i: int, f: float, s: str, i2: int) -> str:
        return "abc"

    @Slot(int, float, str, float, result=str)  # type: ignore[arg-type]
    def f_int_float_str_int_returns_str3(i: int, f: float, s: str, i2: int) -> str:
        return "abc"

    @Slot(int, float, str, int, bytes)
    def f_int_float_str_int_bytes_returns_str1(
        i: int, f: float, s: str, i2: int, b: bytes
    ) -> str:
        return "abc"

    some_str = f_int_float_str_int_bytes_returns_str1(33, 1.0, "abc", 33, b"12")
    some_int = f_int_float_str_int_bytes_returns_str1(33, 1.0, "abc", 33, b"12")  # type: ignore[assignment]
    some_str = f_int_float_str_int_bytes_returns_str1(33, 1.0, "abc", 33, "abc")  # type: ignore[arg-type]

    @Slot(int, float, str, int, bytes, result=float)  # type: ignore[arg-type]
    def f_int_float_str_int_bytes_returns_str2(
        i: int, f: float, s: str, i2: int, b: bytes
    ) -> str:
        return "abc"

    @Slot(int, float, str, float, bytes, result=str)  # type: ignore[arg-type]
    def f_int_float_str_int_bytes_returns_str3(
        i: int, f: float, s: str, i2: int, b: bytes
    ) -> str:
        return "abc"

    # For 6 arguments, it still works without the result argument
    @Slot(int, float, str, int, bytes, float)
    def f_int_float_str_int_bytes_float_returns_str(
        i: int, f: float, s: str, i2: int, b1: bytes, f2: float
    ) -> str:
        return "abc"

    some_str = f_int_float_str_int_bytes_float_returns_str(
        33, 1.0, "abc", 33, b"12", 1.0
    )
    some_int = f_int_float_str_int_bytes_float_returns_str(33, 1.0, "abc", 33, b"12", 1.0)  # type: ignore[assignment]
    some_str = f_int_float_str_int_bytes_float_returns_str(33, 1.0, "abc", 33, "abc", "abc")  # type: ignore[arg-type]

    # For 6 arguments, with the result argument, arguments are no longer type-checked.
    @Slot(int, float, str, int, bytes, float, result=str)
    def f_int_float_str_int_bytes_float_returns_str2(s: str) -> str:
        return "abc"

    # but return value is still type-checked
    some_int = f_int_float_str_int_bytes_float_returns_str2("abc")  # type: ignore[assignment]
