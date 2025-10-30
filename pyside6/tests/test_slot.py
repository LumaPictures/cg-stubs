import pytest

from PySide6.QtCore import Slot
from stubgenlib.test_helpers import TypeCheckError, assert_type


def test() -> None:
    some_str: str
    some_int: int

    @Slot(int)
    def f_int_returns_str1(i: int) -> str:
        assert_type(i, int)
        return "abc"

    # confirm that the decorator preserves the types of the function

    # check return
    assert_type(f_int_returns_str1(33), str)

    with pytest.raises(TypeCheckError):
        # check args
        f_int_returns_str1("abc")  # type: ignore[arg-type]

    @Slot(int, result=str)
    def f_int_returns_str2(i: int) -> str:
        assert_type(i, int)
        return "abc"

    # check return
    assert_type(f_int_returns_str1(33), str)

    @Slot(int, result=int)
    def f_int_returns_str3(i: int) -> str:
        assert_type(i, int)
        return "abc"

    @Slot(int, float)
    def f_int_float_returns_str1(i: int, f: float) -> str:
        assert_type(i, int)
        assert_type(f, float)
        return "abc"

    # check return
    assert_type(f_int_float_returns_str1(33, 1.0), str)

    with pytest.raises(TypeCheckError):
        # check args
        f_int_float_returns_str1("abc", 1.0)  # type: ignore[arg-type]

    with pytest.raises(TypeCheckError):
        # check args
        f_int_float_returns_str1(33, "abc")  # type: ignore[arg-type]

    @Slot(int, float, result=int)
    def f_int_float_returns_str2(i: int, f: float) -> str:
        assert_type(i, int)
        assert_type(f, float)
        return "abc"

    @Slot(int, float, str)
    def f_int_float_str_returns_str1(i: int, f: float, s: str) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        return "abc"

    assert_type(f_int_float_str_returns_str1(33, 1.0, "abc"), str)
    with pytest.raises(TypeCheckError):
        # check args
        f_int_float_str_returns_str1("abc", "abc", 33)  # type: ignore[arg-type]

    # mismatch between Slot result and function result -- our stubs are not good enough to generate an error
    @Slot(int, float, str, result=float)
    def f_int_float_str_returns_str2(i: int, f: float, s: str) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        return "abc"

    @Slot(int, float, str, int)
    def f_int_float_str_int_returns_str1(i: int, f: float, s: str, i2: int) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        assert_type(i2, int)
        return "abc"

    assert_type(f_int_float_str_int_returns_str1(33, 1.0, "abc", 33), str)

    with pytest.raises(TypeCheckError):
        # check args
        f_int_float_str_int_returns_str1(33, 1.0, "abc", "abc")  # type: ignore[arg-type]

    # mismatch between Slot result and function result -- our stubs are not good enough to generate an error
    @Slot(int, float, str, int, result=float)
    def f_int_float_str_int_returns_str2(i: int, f: float, s: str, i2: int) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        assert_type(i2, int)
        return "abc"

    @Slot(int, float, str, float, result=str)
    def f_int_float_str_int_returns_str3(i: int, f: float, s: str, i2: int) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        assert_type(i2, int)
        return "abc"

    @Slot(int, float, str, int, bytes)
    def f_int_float_str_int_bytes_returns_str1(
        i: int, f: float, s: str, i2: int, b: bytes
    ) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        assert_type(i2, int)
        assert_type(b, bytes)
        return "abc"

    assert_type(f_int_float_str_int_bytes_returns_str1(33, 1.0, "abc", 33, b"12"), str)

    with pytest.raises(TypeCheckError):
        f_int_float_str_int_bytes_returns_str1(33, 1.0, "abc", 33, "abc")  # type: ignore[arg-type]

    # mismatch between Slot result and function result -- our stubs are not good enough to generate an error
    @Slot(int, float, str, int, bytes, result=float)
    def f_int_float_str_int_bytes_returns_str2(
        i: int, f: float, s: str, i2: int, b: bytes
    ) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        assert_type(i2, int)
        assert_type(b, bytes)
        return "abc"

    @Slot(int, float, str, float, bytes, result=str)
    def f_int_float_str_int_bytes_returns_str3(
        i: int, f: float, s: str, i2: int, b: bytes
    ) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        assert_type(i2, int)
        assert_type(b, bytes)
        return "abc"

    # For 6 arguments, it still works without the result argument
    @Slot(int, float, str, int, bytes, float)
    def f_int_float_str_int_bytes_float_returns_str(
        i: int, f: float, s: str, i2: int, b1: bytes, f2: float
    ) -> str:
        assert_type(i, int)
        assert_type(f, float)
        assert_type(s, str)
        assert_type(i2, int)
        assert_type(b1, bytes)
        assert_type(f2, float)
        return "abc"

    assert_type(
        f_int_float_str_int_bytes_float_returns_str(33, 1.0, "abc", 33, b"12", 1.0), str
    )

    with pytest.raises(TypeCheckError):
        # check args
        f_int_float_str_int_bytes_float_returns_str(33, 1.0, "abc", 33, "abc", "abc")  # type: ignore

    # For 6 arguments, with the result argument, arguments are no longer type-checked.
    @Slot(int, float, str, int, bytes, float, result=str)
    def f_int_float_str_int_bytes_float_returns_str2(s: str) -> str:
        assert_type(s, str)
        return "abc"

    # but return value is still type-checked
    assert_type(f_int_float_str_int_bytes_float_returns_str2("abc"), str)
