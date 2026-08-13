# mypy: no-warn-unreachable
"""Pin the runtime and typing behaviour of PySide6's QFlags-based enums.

Originally generated from PyQt5-stubs' ``qflags_test_template.py`` for the
Qt5-era pair of a flag class and a distinct QFlags class
(``Qt3DCore.ChangeFlag``/``Qt3DCore.ChangeFlags``).  Qt removed that API
entirely, and PySide6 no longer has separate QFlags wrapper types at all:
combining two flag members yields the *same* class rather than a distinct
"multi flag" type.

What is left is a split into two families, which behave differently enough to
be worth pinning separately:

- ``enum.Flag`` (e.g. ``QDir.Filter``): no interoperability with ``int`` at
  all -- neither ``int(value)`` nor mixing with ``int`` in bitwise operators.
- ``enum.IntFlag`` (e.g. ``Qt.AlignmentFlag``): a real ``int`` subclass, so
  ``int()`` and arithmetic work, and bitwise operators accept ``int`` on
  either side.

Which family a given Qt enum lands in is decided by Qt, so the stubs must get
it right per-class; that is what these tests check.
"""

from typing import TypeAlias, Union

import pytest

from PySide6 import QtCore

### Specific part
# a QFlags enum *without* int interoperability
FlagClass: TypeAlias = QtCore.QDir.Filter
flagRefValue1 = QtCore.QDir.Filter.AllDirs
flagRefValue2 = QtCore.QDir.Filter.Files

# a QFlags enum *with* int interoperability
IntFlagClass: TypeAlias = QtCore.Qt.AlignmentFlag
intFlagRefValue1 = QtCore.Qt.AlignmentFlag.AlignLeft
intFlagRefValue2 = QtCore.Qt.AlignmentFlag.AlignTop
### End of specific part


def assert_type_of_value_int(value: int) -> None:
    """Raise an exception if the value is not a plain int"""
    assert isinstance(value, int)
    assert type(value) == type(123)


def assert_type_of_value_flag(value: FlagClass) -> None:
    """Raise an exception if the value is not of type FlagClass"""
    assert type(value) == FlagClass


def assert_type_of_value_intFlag(value: IntFlagClass) -> None:
    """Raise an exception if the value is not of type IntFlagClass"""
    assert type(value) == IntFlagClass


def test_flag_construction() -> None:
    flagValue1 = flagRefValue1
    flagValueTest: FlagClass = flagValue1

    # this is not supported type-safely for a good reason
    flagValueTest = 1  # type: ignore[assignment]

    # correct ways to do it
    flagValueTest = FlagClass(0)
    flagValueTest = FlagClass(1)
    flagValueTest = FlagClass(flagValue1)
    assert_type_of_value_flag(flagValueTest)


def test_flag_operators() -> None:
    flagValue1 = flagRefValue1
    flagValue2 = flagRefValue2

    # combining two members yields the same class -- PySide6 has no separate
    # QFlags type to widen to
    assert_type_of_value_flag(flagValue1 | flagValue2)
    assert_type_of_value_flag(flagValue1 & flagValue2)
    assert_type_of_value_flag(flagValue1 ^ flagValue2)
    assert_type_of_value_flag(~flagValue1)

    flagValueTest = flagValue1
    flagValueTest |= flagValue2
    assert_type_of_value_flag(flagValueTest)

    flagValueTest = flagValue1
    flagValueTest &= flagValue2
    assert_type_of_value_flag(flagValueTest)

    flagValueTest = flagValue1
    flagValueTest ^= flagValue2
    assert_type_of_value_flag(flagValueTest)


def test_flag_has_no_int_interop() -> None:
    """enum.Flag is not an int: no conversion, no mixing, no arithmetic."""
    flagValue1 = flagRefValue1

    pytest.raises(TypeError, lambda: int(flagValue1))  # type: ignore[call-overload]

    # right operand int
    pytest.raises(TypeError, lambda: flagValue1 | 1)  # type: ignore[operator]
    pytest.raises(TypeError, lambda: flagValue1 & 1)  # type: ignore[operator]
    pytest.raises(TypeError, lambda: flagValue1 ^ 1)  # type: ignore[operator]

    # left operand int
    pytest.raises(TypeError, lambda: 1 | flagValue1)  # type: ignore[operator]
    pytest.raises(TypeError, lambda: 1 & flagValue1)  # type: ignore[operator]
    pytest.raises(TypeError, lambda: 1 ^ flagValue1)  # type: ignore[operator]

    # +/- operations are forbidden
    pytest.raises(TypeError, lambda: flagValue1 + 1)  # type: ignore[operator]
    pytest.raises(TypeError, lambda: flagValue1 - 1)  # type: ignore[operator]
    pytest.raises(TypeError, lambda: 1 + flagValue1)  # type: ignore[operator]
    pytest.raises(TypeError, lambda: 1 - flagValue1)  # type: ignore[operator]

    def f1() -> None:
        value = FlagClass(0)
        value += flagValue1  # type: ignore[operator]

    def f2() -> None:
        value = FlagClass(0)
        value -= flagValue1  # type: ignore[operator]

    pytest.raises(TypeError, f1)
    pytest.raises(TypeError, f2)


def test_intFlag_construction() -> None:
    intFlagValue1 = intFlagRefValue1
    intFlagValueTest: IntFlagClass = intFlagValue1
    flagOrIntValue: Union[int, IntFlagClass] = intFlagValue1

    # even though IntFlagClass is an int subclass, a plain int is not a member
    intFlagValueTest = 1  # type: ignore[assignment]

    # correct ways to do it
    intFlagValueTest = IntFlagClass(0)
    intFlagValueTest = IntFlagClass(1)
    intFlagValueTest = IntFlagClass(intFlagValue1)
    assert_type_of_value_intFlag(intFlagValueTest)

    # upcast to int is allowed: IntFlagClass *is* an int
    flagOrIntValue = 1
    intValue: int = intFlagValue1
    assert intValue == 1


def test_intFlag_operators() -> None:
    intFlagValue1 = intFlagRefValue1
    intFlagValue2 = intFlagRefValue2

    assert_type_of_value_intFlag(intFlagValue1 | intFlagValue2)
    assert_type_of_value_intFlag(intFlagValue1 & intFlagValue2)
    assert_type_of_value_intFlag(intFlagValue1 ^ intFlagValue2)
    assert_type_of_value_intFlag(~intFlagValue1)

    # mixing with int is allowed in both directions and stays an IntFlagClass
    assert_type_of_value_intFlag(intFlagValue1 | 1)
    assert_type_of_value_intFlag(intFlagValue1 & 1)
    assert_type_of_value_intFlag(intFlagValue1 ^ 1)

    assert_type_of_value_intFlag(1 | intFlagValue1)
    assert_type_of_value_intFlag(1 & intFlagValue1)
    assert_type_of_value_intFlag(1 ^ intFlagValue1)

    intFlagValueTest = intFlagValue1
    intFlagValueTest |= intFlagValue2
    assert_type_of_value_intFlag(intFlagValueTest)

    intFlagValueTest = intFlagValue1
    intFlagValueTest |= 1
    assert_type_of_value_intFlag(intFlagValueTest)

    intFlagValueTest = intFlagValue1
    intFlagValueTest &= 1
    assert_type_of_value_intFlag(intFlagValueTest)

    intFlagValueTest = intFlagValue1
    intFlagValueTest ^= 1
    assert_type_of_value_intFlag(intFlagValueTest)


def test_intFlag_arithmetic_degrades_to_int() -> None:
    """+/- are inherited from int, and drop back to a plain int."""
    intFlagValue1 = intFlagRefValue1

    assert_type_of_value_int(int(intFlagValue1))
    assert_type_of_value_int(intFlagValue1 + 1)
    assert_type_of_value_int(intFlagValue1 - 1)
    assert_type_of_value_int(1 + intFlagValue1)
    assert_type_of_value_int(1 - intFlagValue1)
