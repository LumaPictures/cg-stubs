
# Type stubs for PySide6

The most accurate type stubs for PySide! They have been tested using `mypy` on a code base with many thousands of lines of PySide code.

## Features and fixes

### General fixes

* Fixed an issue where methods/attributes were not detected, due to presence of `QObject.__getattr__()`
* Added all signals and made new-style signal patterns work
  * e.g. `myobject.mysignal.connect(func)` and `myobject.mysignal[type].connect(func)`
  * Fixed slot arg of `SignalInstance.connect()` to be `typing.Callable` instead of `object`
  * Fix type arg of `SignalInstance.connect()` to be `QtCore.Qt.ConnectionType` instead of `type | None`
  * Fixed `Signal.emit()`
  * Fixed `Signal.connect()` return value to `bool` instead of `None`
  * Fixed `Object.disconnect()`
* Made `Signal` and `SignalInstance` generic, so that signal arguments are type checked (see [Typed signals](#typed-signals))
* Added all methods to flag classes: `__or__`, `__xor__`, ...

### Typed signals

`Signal` and `SignalInstance` are generic types, parametrized by one or more *signatures*, where
each signature is a tuple of argument types: e.g. `Signal[tuple[int, str]]`, or
`Signal[tuple[int, int], tuple[str, str]]` for a signal with multiple signatures.  This provides
type safety in a few ways:

* `SignalInstance.connect()` enforces that the callable is compatible with the arguments emitted by
  the signal.  Qt allows connecting slots that accept fewer arguments than the signal emits, and
  this is supported for up to the first three arguments.
* Signals can be connected to other signals, and the receiving signal's arguments are checked the
  same way as a slot's.
* `SignalInstance.emit()` enforces the number and types of the arguments provided.
* Signals with multiple signatures are checked against their default (first) signature.  Indexing,
  e.g. `mysignal[str, str].connect(...)`, can be used to check against a specific signature: the
  index is validated against the signal's first or last signature (with up to four arguments each).

Signal attributes on native classes are populated with the requisite types in the stubs, and the
types of custom signals are inferred from the arguments passed to the `Signal` constructor in
common cases:

```python
class MyObject(QtCore.QObject):
    signal1 = QtCore.Signal()                        # Signal[tuple[()]]
    signal2 = QtCore.Signal(int)                     # Signal[tuple[int]]
    signal3 = QtCore.Signal(int, str)                # Signal[tuple[int, str]]
    signal4 = QtCore.Signal((int,), (str,))          # Signal[tuple[int], tuple[str]]
    signal5 = QtCore.Signal((int, int), (str, str))  # Signal[tuple[int, int], tuple[str, str]]
```

Inference is supported for single-signature signals with up to four arguments, and for
multi-signature signals with up to two signatures of up to two arguments each.  Other
configurations must be annotated manually.  Note that the actual `Signal` and `SignalInstance`
classes are not subscriptable at runtime, so manual annotations must be forward references
(wrapped in quotes):

```python
    signal6: "QtCore.Signal[tuple[int, str, float, bool, bytes]]" = QtCore.Signal(
        int, str, float, bool, bytes
    )
```

In keeping with the convention that stubs should avoid false positives, signal usage that cannot
be fully represented in the type system -- such as connecting or emitting through a non-default
signature without indexing -- is allowed without error, even though it is not fully checked.

#### `Signal(object)` and the mypy plugin

`Signal(object)` is the idiomatic way to declare a signal that emits an arbitrary value (Qt
registers it as `PyObject`).  In type checking terms, its intended meaning is `typing.Any` rather than
`object`: the former accepts any type while the latter rejects any type other than `object`. 
This distinction cannot be expressed in the stubs themselves.
Instead, the stubs ship with an optional mypy plugin which rewrites `object`
arguments in `Signal(...)` declarations to `typing.Any`:

* `Signal(object)` infers as `Signal[tuple[Any]]`: any single-argument slot can be connected to it, and any
  value can be emitted through it.
* The rewrite is per-argument, so mixed signals stay strict where they can be:
  `Signal(int, object)` infers as `Signal[tuple[int, Any]]`, and connecting a slot whose
  first argument is not compatible with `int` is still an error.
* `object` arguments are rewritten in every signature of a multi-signature signal, e.g.
  `Signal((object,), (int,))` infers as `Signal[tuple[Any], tuple[int]]`.
* Arguments declared as `typing.Any` (a real class at runtime since Python 3.11, which
  PySide6 likewise registers as `PyObject`) are treated the same way, so `Signal(Any)` also
  works.
* Signals declared without `object` are not affected in any way.

To set it up, install the stubs and add the plugin (distributed inside the
`types-PySide6` package) to your [mypy
configuration](https://mypy.readthedocs.io/en/stable/extending_mypy.html#configuring-mypy-to-use-plugins):

```toml
# pyproject.toml
[tool.mypy]
plugins = ["pyside6_stubs_mypy_plugin"]
```

or in ini style:

```ini
# mypy.ini / setup.cfg
[mypy]
plugins = pyside6_stubs_mypy_plugin
```

If you cannot use the plugin (e.g. with other type checkers), annotate such signals
explicitly instead:

```python
    my_signal: "QtCore.Signal[tuple[Any]]" = QtCore.Signal(object)
```

### Rule-based fixes

* When instantiating subclasses of `QObject` it is possible to pass the values of properties and signals as `**kwargs` to `__init__`.  The stubs have been fix to include these args on all relevant `__init__` methods.
* Removed redundant overlapping overloads, so that satisfying mypy/liskov on subclassed methods is easier
* Corrected all arguments typed as `typing.Sequence` to be `typing.Iterable`.  Tests so far have indicated that this is true as a general rule. 
* Added sub-types to `Iterable` annotations, e.g. `Iterable[str]`,  `Iterable[int]`, etc
* Replaced `object` with `typing.Any` in return types. e.g.:
  * `QSettings.value() -> Any`
  * `QModelIndex.internalPointer() -> Any`
  * `QPersistentModelIndex.internalPointer() -> Any`
* Added support for overloads that mix static and instance methods. `mypy` disallows this using traditional 
  overloads, so this project achieves it by generating specialized decorator classes that hold each of the 
  overloads.

### Specific fixes

* Certain argument types implicitly accept alternative types for brevity.  Below are the known fixes so far (Note that I've debated not including these, since one of the advantages of static typing is it gives you the confidence to be explicit rather than ambiguous. I could introduce a strict mode in the future that would disable these):
  * `QKeySequence`: `str`
  * `QColor`: `Qt.GlobalColor` and `int`
  * `QBrush`: `QLinearGradient` and `QColor` (and by extension `Qt.GlobalColor`)
  * `QCursor`: `Qt.CursorShape`
  * `QEasingCurve`: `QEasingCurve.Type`
* Fixed `QTreeWidgetItemIterator.__iter__()` to return `Iterator[QTreeWidgetItemIterator]`
* Added missing `QDialog.exec()` method
* Fixed numerous methods which accept `None`:
  * `QPainter.drawText(..., br)`
  * `QPainter.drawPolygon(..., arg__2)`
  * `QProgressDialog.setCancelButton(button)`
  * `*.setModel(model)`
  * `QLabel.setPixmap(arg__1)`
* Fixed numerous arguments that accept `QModelIndex` which were typed as `int`
* Fixed return type for `QApplication.instance()` and `QGuiApplication.instance()`
* Fixed return type for `QObject.findChild()` and `QObject.findChildren()`
* Fixed support for initializing `QDate` from `datetime.date`
* Fixed support for initializing `QDateTime` from `datetime.datetime`
* Fixed `QByteArray.__iter__()` to return `Iterator[bytes]`
* Fixed support for `bytes(QByteArray(b'foo'))`
* Added support for all `QSize` and `QSizeF` operations
* Added support for all `QPolygon` operations
* Fixed `QTextEdit.setFontWeight()` to accept `QFont.Weight`
* Fixed return type for `qVersion()`
* Add `QSpacerItem.__init__/changeSize` overloads that use alternate names: `hData`->`hPolicy`, `vData`->`vPolicy`
* Fixed `QAction.menu` to return optional `QMenu` instead of `QOjbect`

## Licensing

As a derived work from PySide2, the stubs are delivered under the LGPL v2.1 . See file LICENSE for more details.

## Installation

Install the latest stub packages from pypi:

    $ pip install types-PySide2

This will add the `PySide2-stubs` and `shiboken2-stubs` packages into your site-packages directory.  
Yes, the name of the pypi package is `types-PySide2` but the python package it installs is `PySide2-stubs`.  
It's confusing, but [PEP 561](https://peps.python.org/pep-0561/) requires that the installed package name is of the form `$PACKAGE-stubs`, so all of us PySide stub developers are installing a package with the same name.

Note, you may need to uninstall other PySide2 stubs first:

    $ pip uninstall PySide2-stubs

## Help improve the stubs

If you notice incorrect or missing typing information (i.e. mypy reports errors even though your code is correct), please report it or make a PR to fix it. 

## Testing

```
python3 -m venv .venv
. .venv/bin/activate
tox
```

## TODO

* Build PySide6 stubs
* Merge overloads where a `Union` would do instead of multiple overloads
