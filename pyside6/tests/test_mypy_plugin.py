"""Tests for the types_pyside6_mypy_plugin mypy plugin.

The plugin makes `object` (and `typing.Any`) arguments in ``Signal(...)``
declarations mean ``typing.Any``, and validates signal subscripts
(``sig[...]``) against every declared signature, narrowing the result to the
signature the index selects.

The type-level assertions live in mypy_plugin_cases.py -- generated from
test_generic_signals.py by gen_mypy_plugin_cases.py, identical except for
its ``# type: ignore`` comments -- and mypy_plugin_no_object_cases.py.  Both
are excluded from the project's plain mypy run and checked here with the
plugin enabled.  The ``# REMOVE`` / ``# ADD: ignore[...]`` /
``# REPLACE: ignore[...]`` markers in test_generic_signals.py document
exactly what the plugin changes: runtime errors (asserted with
pytest.raises in the shared content) whose ignore is added only in
mypy_plugin_cases.py are caught only by the plugin, and ignores marked
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
CASES = HERE / "mypy_plugin_cases.py"
GENERIC_SIGNALS = HERE / "test_generic_signals.py"
NO_OBJECT_CASES = HERE / "mypy_plugin_no_object_cases.py"
PLUGIN = HERE.parent / "types_pyside6_mypy_plugin" / "__init__.py"


def run_mypy(
    config: pathlib.Path, cache_dir: pathlib.Path, cases: pathlib.Path = CASES
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


def test_cases_are_generated() -> None:
    """mypy_plugin_cases.py must match what gen_mypy_plugin_cases.py
    generates from test_generic_signals.py, so the two files differ only in
    their ``# type: ignore`` comments, as directed by the ``# REMOVE`` /
    ``# ADD: ignore[...]`` markers.
    """
    expected = gen_mypy_plugin_cases.generate(GENERIC_SIGNALS.read_text())
    assert CASES.read_text() == expected, (
        "tests/mypy_plugin_cases.py is stale:"
        " run tests/gen_mypy_plugin_cases.py to regenerate it"
    )


def test_cases_pass_with_plugin(tmp_path: pathlib.Path) -> None:
    result = run_mypy(HERE / "mypy-plugin.ini", tmp_path / "cache")
    assert result.returncode == 0, result.stdout + result.stderr


def test_cases_fail_without_plugin(tmp_path: pathlib.Path) -> None:
    """Control: prove that the plugin is what makes the cases pass.

    Without the plugin, the false positives the plugin fixes resurface (e.g.
    `Signal(object).connect(typed_slot)` and indexing a middle signature),
    and the ignores asserting plugin-only errors (e.g. an index that matches
    no declared signature) are reported as unused.
    """
    no_plugin = tmp_path / "mypy-no-plugin.ini"
    config = (HERE / "mypy-plugin.ini").read_text()
    stripped = "\n".join(
        line for line in config.splitlines() if not line.startswith("plugins")
    )
    no_plugin.write_text(stripped)

    result = run_mypy(no_plugin, tmp_path / "cache")
    assert result.returncode != 0
    assert "call-overload" in result.stdout, result.stdout + result.stderr
    assert 'Unused "type: ignore" comment' in result.stdout, (
        result.stdout + result.stderr
    )


def test_object_as_any_opt_out_ini(tmp_path: pathlib.Path) -> None:
    """`object_as_any = False` in the ini-style [types-pyside6-mypy] section
    disables the object/Any rewrite but not the signal index validation.
    """
    result = run_mypy(
        HERE / "mypy-plugin-no-object.ini", tmp_path / "cache", NO_OBJECT_CASES
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
