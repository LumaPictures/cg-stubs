"""Tests for the types_pyside6_mypy_plugin mypy plugin.

The plugin makes `object` (and `typing.Any`) arguments in ``Signal(...)``
declarations mean ``typing.Any``, validates signal subscripts (``sig[...]``)
against every declared signature, narrowing the result to the signature the
index selects, and treats a native signal's defaulted trailing C++ arguments
as optional.

The type-level assertions live in the generated
mypy_plugin_test_generic_signals.py and mypy_plugin_test_native_signals.py --
produced from test_generic_signals.py and test_native_signals.py by
gen_mypy_plugin_cases.py, identical to their source
except for its ``# type: ignore`` comments -- and in
mypy_plugin_no_object_cases.py.  All are excluded from the project's plain
mypy run and checked here with the plugin enabled.  The ``# REMOVE`` /
``# ADD: ignore[...]`` / ``# REPLACE: ignore[...]`` markers in the source
files document exactly what the plugin changes: runtime errors (asserted with
pytest.raises in the shared content) whose ignore is added only in the
generated file are caught only by the plugin, and ignores marked
``# REMOVE`` are stubs-only false positives the plugin fixes.
"""

from __future__ import absolute_import, print_function

import pathlib
import subprocess
import sys
import typing

import pytest

import gen_mypy_plugin_cases
from PySide6 import QtCore

HERE = pathlib.Path(__file__).parent
# The test files that have a generated twin; gen_mypy_plugin_cases.py reads
# this list when it is run without arguments.
SOURCES = [
    HERE / "test_generic_signals.py",
    HERE / "test_native_signals.py",
]
# the generated twins, which carry the ignores the plugin-enabled run expects
CASES = [gen_mypy_plugin_cases.target_path(source) for source in SOURCES]
GENERIC_CASES = HERE / "mypy_plugin_test_generic_signals.py"
NATIVE_CASES = HERE / "mypy_plugin_test_native_signals.py"
NO_OBJECT_CASES = HERE / "mypy_plugin_no_object_cases.py"
PLUGIN = HERE.parent / "types_pyside6_mypy_plugin" / "__init__.py"


def run_mypy(
    config: pathlib.Path, cache_dir: pathlib.Path, cases: pathlib.Path
) -> "subprocess.CompletedProcess[str]":
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "mypy",
            "--config-file",
            str(config),
            "--cache-dir",
            str(cache_dir),
            str(cases),
        ],
        capture_output=True,
        text=True,
    )


@pytest.mark.parametrize("source", SOURCES, ids=lambda path: path.name)
def test_cases_are_generated(source: pathlib.Path) -> None:
    """Each generated file must match what gen_mypy_plugin_cases.py generates
    from its source, so that the two differ only in their ``# type: ignore``
    comments, as directed by the ``# REMOVE`` / ``# ADD: ignore[...]`` /
    ``# REPLACE: ignore[...]`` markers.
    """
    target = gen_mypy_plugin_cases.target_path(source)
    expected = gen_mypy_plugin_cases.generate(source.read_text(), source.name)
    assert target.read_text() == expected, (
        f"tests/{target.name} is stale:"
        " run tests/gen_mypy_plugin_cases.py to regenerate it"
    )


@pytest.mark.parametrize("cases", CASES, ids=lambda path: path.name)
def test_cases_pass_with_plugin(cases: pathlib.Path, tmp_path: pathlib.Path) -> None:
    result = run_mypy(HERE / "mypy-plugin.ini", tmp_path / "cache", cases)
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize(
    "cases, expected",
    [
        # The false positives the plugin fixes resurface (e.g.
        # `Signal(object).connect(typed_slot)` and indexing a middle
        # signature), and the ignores asserting plugin-only errors (e.g. an
        # index that matches no declared signature) are reported as unused.
        (GENERIC_CASES, ["call-overload", 'Unused "type: ignore" comment']),
        # Without the plugin, a C++ default argument is just another signature:
        # emit() requires the default signature's arguments in full, and a slot
        # taking the defaulted argument cannot be connected.
        (NATIVE_CASES, ["Too few arguments", "incompatible type"]),
    ],
    ids=lambda value: value.name if isinstance(value, pathlib.Path) else "",
)
def test_cases_fail_without_plugin(
    cases: pathlib.Path, expected: "list[str]", tmp_path: pathlib.Path
) -> None:
    """Control: prove that the plugin is what makes the cases pass."""
    no_plugin = tmp_path / "mypy-no-plugin.ini"
    config = (HERE / "mypy-plugin.ini").read_text()
    stripped = "\n".join(
        line for line in config.splitlines() if not line.startswith("plugins")
    )
    no_plugin.write_text(stripped)

    result = run_mypy(no_plugin, tmp_path / "cache", cases)
    assert result.returncode != 0
    for message in expected:
        assert message in result.stdout, result.stdout + result.stderr


def test_object_as_any_opt_out_ini(tmp_path: pathlib.Path) -> None:
    """`object_as_any = False` in the ini-style [types-pyside6-mypy] section
    disables the object/Any rewrite but not the signal index validation.
    """
    result = run_mypy(
        HERE / "mypy-plugin-no-object.ini",
        tmp_path / "cache",
        NO_OBJECT_CASES,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_object_as_any_opt_out_pyproject(tmp_path: pathlib.Path) -> None:
    """The same option is read from a [tool.types-pyside6-mypy] table when
    mypy is configured through a pyproject.toml.
    """
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        f"""
[tool.mypy]
strict = true
plugins = ["{PLUGIN}"]

[[tool.mypy.overrides]]
module = ["PySide6.*", "shiboken6.*"]
disable_error_code = ["no-untyped-def", "type-arg"]

[tool.types-pyside6-mypy]
object_as_any = false
"""
    )
    result = run_mypy(pyproject, tmp_path / "cache", NO_OBJECT_CASES)
    assert result.returncode == 0, result.stdout + result.stderr


class _ObjectSignals(QtCore.QObject):
    signal_obj = QtCore.Signal(object)
    signal_any = QtCore.Signal(typing.Any)


@pytest.mark.usefixtures("qapplication")
def test_object_signals_at_runtime() -> None:
    """The declarations the plugin targets are valid PySide6 at runtime.

    Both `object` and `typing.Any` (a real class since Python 3.11) register
    as PyObject and pass arbitrary values through unchanged.
    """
    obj = _ObjectSignals()
    # Signal.signatures is missing from the stubs
    assert _ObjectSignals.signal_obj.signatures == ("signal_obj(PyObject)",)  # type: ignore[attr-defined]
    assert _ObjectSignals.signal_any.signatures == ("signal_any(PyObject)",)  # type: ignore[attr-defined]

    received: "list[object]" = []
    payload = object()
    obj.signal_obj.connect(received.append)
    obj.signal_obj.emit(payload)
    obj.signal_any.connect(received.append)
    # this file is type-checked without the plugin, so Signal(typing.Any) is
    # nominal and emitting through it is the false positive the plugin fixes
    obj.signal_any.emit(payload)  # type: ignore[arg-type]
    assert received == [payload, payload]
