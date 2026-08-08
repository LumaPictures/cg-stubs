"""Tests for the pyside6_stubs_mypy_plugin mypy plugin.

The plugin makes `object` (and `typing.Any`) arguments in ``Signal(...)``
declarations mean ``typing.Any``.  The type-level assertions live in
signal_object_plugin_cases.py, which is excluded from the project's plain mypy
run and checked here with the plugin enabled (tests/mypy-plugin.ini).
"""

from __future__ import absolute_import, print_function

import pathlib
import subprocess
import sys
import typing

import pytest

from PySide6 import QtCore

HERE = pathlib.Path(__file__).parent
CASES = HERE / "signal_object_plugin_cases.py"


def run_mypy(config: pathlib.Path, cache_dir: pathlib.Path) -> "subprocess.CompletedProcess[str]":
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "mypy",
            "--config-file",
            str(config),
            "--cache-dir",
            str(cache_dir),
            str(CASES),
        ],
        capture_output=True,
        text=True,
    )


def test_cases_pass_with_plugin(tmp_path: pathlib.Path) -> None:
    result = run_mypy(HERE / "mypy-plugin.ini", tmp_path / "cache")
    assert result.returncode == 0, result.stdout + result.stderr


def test_cases_fail_without_plugin(tmp_path: pathlib.Path) -> None:
    """Control: prove that the plugin is what makes the cases pass.

    Without the plugin, `Signal(object)` infers as `Signal[tuple[object]]` and
    connecting a typed slot to it is reported as an error.
    """
    no_plugin = tmp_path / "mypy-no-plugin.ini"
    config = (HERE / "mypy-plugin.ini").read_text()
    stripped = "\n".join(
        line for line in config.splitlines() if not line.startswith("plugins")
    )
    no_plugin.write_text(stripped)

    result = run_mypy(no_plugin, tmp_path / "cache")
    assert result.returncode != 0
    # the idiomatic Signal(object).connect(typed_slot) is a false positive
    # without the plugin
    assert "call-overload" in result.stdout, result.stdout + result.stderr


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
