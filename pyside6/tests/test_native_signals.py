"""Runtime and static checks for native signals with C++ default arguments.

Qt registers one signature per defaulted parameter of a C++ signal, so a
signal declared as ``void clicked(bool checked = false)`` arrives in the
stubs as a *multi-signature* signal, indistinguishable in form from a Python
signal declared with genuinely distinct signatures::

    clicked:     Signal[tuple[()], tuple[bool]]                          # default argument
    dataChanged: Signal[tuple[QModelIndex, QModelIndex, Any],
                        tuple[QModelIndex, QModelIndex]]                 # default argument
    py_long_default: Signal[tuple[int, str], tuple[int]]                 # two signatures

The runtime behavior is not the same, though, and the difference shows up in
the stubs as one signature being a *prefix* of another: for a C++ default
argument no dispatch happens at all, C++ simply fills the default in.  On a
native signal, therefore:

- ``emit`` may omit the trailing arguments that a shorter registered
  signature drops -- ``dataChanged.emit(topLeft, bottomRight)`` is valid, and
  slots that take the third argument receive the C++ default;
- ``connect`` accepts a slot taking as many arguments as the *longest*
  signature, because PySide connects a slot to the registered signature whose
  argument count matches the slot's -- so ``clicked.connect(slot)`` does pass
  ``checked`` to a slot that takes it;
- but ``emit`` may not pass *more* arguments than the default signature
  declares: ``clicked.emit(True)`` raises TypeError, since ``clicked()`` is
  the default signature.  Only ``clicked[bool].emit(True)`` emits the other
  one.

None of that holds for a Python-declared signal, where a prefix relation
between signatures is a coincidence: ``py_long_default.emit(1)`` raises
TypeError because unsubscripted ``emit`` uses the default signature and there
is no C++ default to fill in the rest.  This is why the plugin relaxes native
signals only, which the last two tests here pin down for both ``emit`` and
``connect``.

This file is the single source for a pair of files whose executable content
is identical and whose ``# type: ignore[...]`` comments differ; see the
module docstring of test_generic_signals.py for the ``# REMOVE`` /
``# ADD: ignore[code]`` / ``# REPLACE: ignore[code]`` markers that direct
tests/gen_mypy_plugin_cases.py, which generates
mypy_plugin_test_native_signals.py from this file.  In short: an ignore
marked ``# REMOVE`` is a stubs-only false positive that the plugin fixes,
and an unmarked ignore is an error both with and without the plugin.
"""

import pytest

from PySide6 import QtCore, QtGui, QtLocation, QtWidgets


class Model(QtCore.QStringListModel):
    """A subclass, so that its inherited signals are found through the MRO."""

    # Python signals whose signatures happen to form a prefix chain, in both
    # orders: they are declared exactly like the C++ signals above, but a
    # prefix relation carries no meaning for them.
    py_long_default = QtCore.Signal((int, str), (int,))
    py_short_default = QtCore.Signal((int,), (int, str))

    # Plain signals, to be connected to native ones.
    bool_sig = QtCore.Signal(bool)
    str_sig = QtCore.Signal(str)


class Recorder(QtCore.QObject):
    """Records every slot invocation so tests can assert delivery.

    The slots take `object` arguments, so that they can be connected to any
    signal and the number of arguments is all that matters.
    """

    def __init__(self) -> None:
        super().__init__()
        self.calls: "list[tuple[object, ...]]" = []

    def none(self) -> None:
        self.calls.append(())

    def one(self, arg1: object) -> None:
        self.calls.append((arg1,))

    def two(self, arg1: object, arg2: object) -> None:
        self.calls.append((arg1, arg2))

    def three(self, arg1: object, arg2: object, arg3: object) -> None:
        self.calls.append((arg1, arg2, arg3))


def slot_checked(checked: bool) -> None: ...
def slot_str(arg1: str) -> None: ...
def slot_index(arg1: QtCore.QModelIndex) -> None: ...
def slot_object(arg1: QtCore.QObject) -> None: ...
def slot_two_bools(arg1: bool, arg2: bool) -> None: ...


def test_connect_accepts_the_longest_signature() -> None:
    """`clicked(bool checked = false)` is registered as both `clicked()` and
    `clicked(bool)`, and PySide connects a slot to whichever signature has as
    many arguments as the slot: a one-argument slot receives `checked`.
    """
    button = QtWidgets.QPushButton()
    r = Recorder()

    button.clicked.connect(r.none)
    # The default signature takes no arguments, so without the plugin
    # connecting a slot that takes `checked` is a false positive.
    button.clicked.connect(r.one)  # type: ignore[arg-type]  # REMOVE
    button.clicked.connect(slot_checked)  # type: ignore[arg-type]  # REMOVE

    button.click()
    assert r.calls == [(), (False,)]

    # ... and the same slots can be disconnected again.
    r.calls.clear()
    assert button.clicked.disconnect(slot_checked) is True  # type: ignore[arg-type]  # REMOVE
    assert button.clicked.disconnect(r.one) is True  # type: ignore[arg-type]  # REMOVE
    button.click()
    assert r.calls == [()]


def test_connect_beyond_the_longest_signature() -> None:
    """A slot with more arguments than the longest signature can never be
    invoked (Qt prints and swallows the TypeError at emit time), and a slot
    whose argument types do not match is not caught at runtime at all, so
    both are errors with and without the plugin.
    """
    button = QtWidgets.QPushButton()

    button.clicked.connect(slot_two_bools)  # type: ignore[arg-type]
    button.clicked.connect(slot_str)  # type: ignore[arg-type]


def test_connect_signal_to_signal() -> None:
    """A signal can be connected to another signal, whose arguments are
    checked like a slot's, so it may take the defaulted argument too.  Unlike
    a Python callable, an incompatible signal is rejected at runtime.
    """
    button = QtWidgets.QPushButton()
    model = Model(["a"])
    r = Recorder()

    model.bool_sig.connect(r.one)
    button.clicked.connect(model.bool_sig)  # type: ignore[arg-type]  # REMOVE
    button.click()
    assert r.calls == [(False,)]

    # disconnect() with no argument at all drops every connection.
    assert button.clicked.disconnect() is True
    r.calls.clear()
    button.click()
    assert r.calls == []

    # A receiving signal whose argument type does not match is still an error.
    with pytest.raises(RuntimeError):
        button.clicked.connect(model.str_sig)  # type: ignore[arg-type]


def test_connect_three_signatures() -> None:
    """`layoutChanged(parents = {}, hint = NoLayoutChangeHint)` has two
    default arguments, so Qt registers three signatures; every slot arity up
    to the longest one is valid.
    """
    model = Model(["a", "b"])
    r = Recorder()

    model.layoutChanged.connect(r.none)
    model.layoutChanged.connect(r.one)  # type: ignore[arg-type]  # REMOVE
    model.layoutChanged.connect(r.two)  # type: ignore[arg-type]  # REMOVE

    # Emitting the default (no-argument) signature still invokes the slots
    # connected to the longer ones, with the C++ defaults filled in.
    model.layoutChanged.emit()
    assert r.calls == [
        (),
        ([],),
        ([], QtCore.QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint),
    ]


def test_connect_qobject_destroyed() -> None:
    """`destroyed(QObject *obj = nullptr)`: the argument every `destroyed`
    slot is written to take.
    """
    obj = QtCore.QObject()

    obj.destroyed.connect(slot_object)  # type: ignore[arg-type]  # REMOVE


def test_connect_qaction_triggered() -> None:
    """`triggered(bool checked = false)`, the other half of the idiom the
    stubs alone reject.
    """
    action = QtGui.QAction()
    r = Recorder()

    action.triggered.connect(slot_checked)  # type: ignore[arg-type]  # REMOVE
    action.triggered.connect(r.one)  # type: ignore[arg-type]  # REMOVE

    action.trigger()
    assert r.calls == [(False,)]


def test_connect_distinct_signatures_stays_strict() -> None:
    """`QCompleter.activated` has two genuinely distinct one-argument
    signatures -- `activated(QString)` and `activated(QModelIndex)` -- and
    neither is a prefix of the other, so nothing is relaxed: an unsubscripted
    connect only ever delivers the default signature's `str`, and connecting
    a slot that takes a QModelIndex silently receives garbage at runtime.
    """
    completer = QtWidgets.QCompleter(["a"])

    completer.activated.connect(slot_str)
    completer.activated.connect(slot_index)  # type: ignore[call-overload]
    completer.activated[QtCore.QModelIndex].connect(slot_index)


def test_emit_may_omit_default_arguments() -> None:
    """`dataChanged(topLeft, bottomRight, roles = {})`: the default signature
    is the full one, and C++ fills in the arguments that are left out, so
    every connected slot still receives them.
    """
    model = Model(["a", "b"])
    r = Recorder()
    index = model.index(0)

    model.dataChanged.connect(r.two)
    model.dataChanged.connect(r.three)

    # The stubs bind emit() to the default signature, where the third
    # argument is required.
    model.dataChanged.emit(index, index)  # type: ignore[call-arg]  # REMOVE
    assert r.calls == [(index, index), (index, index, [])]

    r.calls.clear()
    model.dataChanged.emit(index, index, [3])
    assert r.calls == [(index, index), (index, index, [3])]

    # Only the *trailing* arguments are optional: the shortest registered
    # signature still has to be satisfied.
    with pytest.raises(TypeError):
        model.dataChanged.emit(index)  # type: ignore[call-arg]


def test_emit_required_arguments_are_still_checked() -> None:
    """`QProcess.finished(int exitCode, ExitStatus exitStatus = NormalExit)`:
    making the trailing argument optional leaves the type of the required one
    checked (a wrong type does not raise at runtime -- Qt coerces it, so mypy
    is the only guard).
    """
    process = QtCore.QProcess()

    process.finished.emit(0)  # type: ignore[call-arg]  # REMOVE
    process.finished.emit(0, QtCore.QProcess.ExitStatus.NormalExit)
    # Once the trailing argument is optional, the wrong type of the first is
    # the only error left.
    process.finished.emit("0")  # type: ignore[arg-type, call-arg]  # REPLACE: ignore[arg-type]
    with pytest.raises(TypeError):
        process.finished.emit()  # type: ignore[call-arg]


def test_emit_optional_arguments_are_still_checked() -> None:
    """An optional argument keeps its type.

    `QGeoCodeReply.errorOccurred(Error error, QString errorString = QString())`
    is one of the few native default arguments whose type survives into the
    stubs (most are C++ types that PySide passes through as PyObject, which
    the stubs can only describe as `Any`).
    """
    reply = QtLocation.QGeoCodeReply()
    error = QtLocation.QGeoCodeReply.Error.NoError

    reply.errorOccurred.emit(error)  # type: ignore[call-arg]  # REMOVE
    reply.errorOccurred.emit(error, "no such place")
    reply.errorOccurred.emit(error, 42)  # type: ignore[arg-type]


def test_emit_cannot_add_arguments() -> None:
    """Where the *default* signature is the shorter one, emit() cannot pass
    the extra argument at all: it dispatches to `clicked()`.  The other
    signature must be selected with an index.
    """
    button = QtWidgets.QPushButton()
    r = Recorder()

    button.clicked.connect(r.one)  # type: ignore[arg-type]  # REMOVE
    button.clicked.emit()
    assert r.calls == [(False,)]

    with pytest.raises(TypeError):
        button.clicked.emit(True)  # type: ignore[call-arg]

    r.calls.clear()
    button.clicked[bool].emit(True)
    assert r.calls == [(True,)]


def test_python_signal_emit_is_not_relaxed() -> None:
    """emit() is not relaxed for a Python signal: it uses the default
    signature and there is no C++ default argument to fill in the rest, even
    though the signatures have the same shape as `dataChanged`'s.
    """
    model = Model(["a"])
    r = Recorder()

    model.py_long_default.connect(r.two)
    model.py_long_default.emit(1, "one")
    assert r.calls == [(1, "one")]

    with pytest.raises(TypeError):
        model.py_long_default.emit(1)  # type: ignore[call-arg]

    # Indexing selects the other signature, as always.
    r.calls.clear()
    model.py_long_default.connect(r.one)
    model.py_long_default[int].emit(2)
    assert r.calls == [(2,)]


def test_python_signal_connect_is_not_relaxed() -> None:
    """connect() is not relaxed for a Python signal either, although the
    signatures have the same shape as `clicked`'s.

    PySide does bind the two-argument slot below to the second signature (it
    connects a slot to the signature that has as many arguments as the slot,
    whether the signal is native or not), so this is a false positive that the
    plugin deliberately leaves in place: a prefix relation between the
    signatures of a Python signal does not mean a default argument -- nothing
    would fill one in on emit -- and the slot is only ever invoked by an
    explicitly indexed emit.
    """
    model = Model(["a"])
    r = Recorder()

    model.py_short_default.connect(r.one)
    model.py_short_default.connect(r.two)  # type: ignore[call-overload]

    model.py_short_default.emit(1)
    model.py_short_default[int, str].emit(2, "two")
    assert r.calls == [(1,), (2, "two")]


def test_signal_read_into_a_variable_is_not_relaxed() -> None:
    """Known limitation: the plugin recognizes a C++ default argument by
    where the signal is *declared*, which it can only see when the signal is
    read directly from the object that declares it.  A signal first stored in
    a variable is checked strictly (the stubs' behavior).
    """
    model = Model(["a", "b"])
    index = model.index(0)

    data_changed = model.dataChanged
    data_changed.emit(index, index)  # type: ignore[call-arg]
    data_changed.emit(index, index, [])
