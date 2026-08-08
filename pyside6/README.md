
# Type stubs for PySide6

The most accurate type stubs for PySide! They have been tested using `mypy` on a code base with many thousands of lines of PySide code.

## Features and fixes

### Typed signals

`types-PySide6` provides type safe signals and slots and the signal attributes on native classes are populated with the requisite types in the stubs.

In our stubs, `Signal` and `SignalInstance` are generic types, parametrized by one or more *signatures*, where
each signature is a tuple of argument types: e.g.
* `Signal[tuple[int, str]]` expects a slot function like `def myslot(arg1: int, arg2: str)`
* `Signal[tuple[int, int], tuple[str, str]]` has multiple signatures, and can work with a slot function like `def myslot(arg1: int, arg2: str)` or `def myslot(arg1: str, arg2: str)`

This provides type safety in a few ways:

* `SignalInstance.connect()` enforces that the connected callable is compatible with the arguments emitted by
  the signal.
* Signals can be connected to other signals, and the receiving signal's arguments are checked the
  same way as a slot's.
* `SignalInstance.emit()` enforces the number and types of the arguments provided.
* Signals with multiple signatures are checked against their default (first) signature, which is
  the only signature an unsubscripted `connect()`/`emit()` uses at runtime.  Indexing,
  e.g. `mysignal[str, str].connect(...)`, can be used to check against a specific signature: the
  index is validated against the signal's first or last signature (with up to four arguments
  each); the mypy plugin extends this to every declared signature.

The types of custom signals are inferred from the arguments passed to the `Signal` constructor in
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
configurations must be annotated manually.

Note that the actual `Signal` and `SignalInstance` classes are not subscriptable at runtime, so manual annotations must be forward references (wrapped in quotes):

```python
    signal6: "QtCore.Signal[tuple[int, str, float, bool, bytes]]" = QtCore.Signal(
        int, str, float, bool, bytes
    )
```

#### The mypy plugin

The stubs ship with an optional mypy plugin that improves signal type checking in ways that
cannot be expressed in the stubs themselves.

To set it up, install the stubs and add the plugin (distributed inside the
`types-PySide6` package) to your [mypy
configuration](https://mypy.readthedocs.io/en/stable/extending_mypy.html#configuring-mypy-to-use-plugins):

```toml
# pyproject.toml
[tool.mypy]
plugins = ["types_pyside6_mypy_plugin"]
```

or in ini style:

```ini
# mypy.ini / setup.cfg
[mypy]
plugins = types_pyside6_mypy_plugin
```

##### Signal subscripts are validated against every signature

At runtime, subscripting a signal selects one of its declared signatures -- raising
`IndexError` when none matches -- and `connect()`/`emit()` on the result use exactly that
signature.  (An *unsubscripted* `connect()`/`emit()` uses only the default signature;
PySide does not dispatch across signatures by argument types, so the stubs' default-
signature checking is already what happens at runtime.)

The stubs alone can only validate an index against the signal's first or last signature:
an index selecting a middle signature of a three-plus-signature signal is falsely flagged,
and an index that matches no declared signature at all falls through to an unchecked
catch-all, hiding the runtime `IndexError` and leaving everything called on the result
unchecked.  The plugin validates a literal index against every declared signature and
narrows the result to the signature the index selects, so subsequent `connect()`/`emit()`
calls are checked against it -- exactly mirroring the runtime dispatch:

```python
class MyObject(QtCore.QObject):
    signal: "QtCore.Signal[tuple[int, int], tuple[str], tuple[float, float]]" = (
        QtCore.Signal((int, int), (str,), (float, float))
    )

    def use_signatures(self) -> None:
        self.signal[str].emit("one")       # stubs alone flag the valid index [str]
        self.signal[str].emit("one", 2)    # only the plugin catches this TypeError
        self.signal[str].connect(int_slot) # only the plugin catches this bad slot
        self.signal[str, str]              # only the plugin catches this IndexError
        self.signal[bool, bool]            # ... and this one (bool is not int at runtime)
```

##### `Signal(object)` means `typing.Any`

`Signal(object)` is the idiomatic way to declare a signal that emits an arbitrary value (Qt
registers it as `PyObject`).  The proper way to handle this is to add a type annotation:

```python
class MyObject(QtCore.QObject):
    signal1: "Signal[tuple[MyCustomClass]]" = QtCore.Signal(object)
```

However, 
In type-checking terms, its intended meaning is `typing.Any` rather than
`object`: the former accepts any type while the latter rejects any type other than `object`. 
This distinction cannot be expressed in the stubs themselves, so the plugin rewrites `object`
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

If you cannot use the plugin (e.g. with other type checkers), annotate such signals
explicitly instead:

```python
    my_signal: "QtCore.Signal[tuple[Any]]" = QtCore.Signal(object)
```

##### Plugin options

Options are read from the same config file that mypy was invoked with, from a
`[tool.types-pyside6-mypy]` table in `pyproject.toml`, or a `[types-pyside6-mypy]` section
in ini-style files:

```toml
# pyproject.toml
[tool.types-pyside6-mypy]
object_as_any = false
```

```ini
# mypy.ini / setup.cfg
[types-pyside6-mypy]
object_as_any = False
```

* `object_as_any` (default `true`): set to `false` to opt out of rewriting
  `object`/`typing.Any` arguments of `Signal(...)` declarations to `typing.Any`.

### Rule-based fixes

The `types-PySide6` stub generator inspects the annotations extracted from the `PySide6` library and automatically applies the following fixes:

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

As a derived work from PySide6, the stubs are delivered under the LGPL v2.1 . See file LICENSE for more details.

## Installation

Install the latest stub packages from pypi:

    $ pip install types-PySide6

This will add the `PySide6-stubs` and `shiboken6-stubs` packages into your site-packages directory.  
Yes, the name of the pypi package is `types-PySide6` but the python package it installs is `PySide6-stubs`.  
It's confusing, but [PEP 561](https://peps.python.org/pep-0561/) requires that the installed package name is of the form `$PACKAGE-stubs`, so all of us PySide stub developers are installing a package with the same name.

Note, you may need to uninstall other PySide6 stubs first:

    $ pip uninstall PySide6-stubs

## Help improve the stubs

If you notice incorrect or missing typing information (i.e. mypy reports errors even though your code is correct), please report it or make a PR to fix it. 
