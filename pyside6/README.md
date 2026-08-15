
# Type stubs for PySide6

The most accurate type stubs for PySide! They have been tested using `mypy` on a code base with many thousands of lines of PySide code.

## Features

- **Type-safe signals**: supports both custom and native signals.  A `mypy` plugin works around edge cases not currently supported by the Python type system ([mapping/transforming `TypeVarTuple`](https://github.com/python/typing/issues/1216)).
- **Attention to detail**: supports Qt subtleties such as passing property values to `__init__` and implicitly convertible types.
- **Battle-tested**: used in complex production code and backed by a test framework that confirms runtime and static equivalence.

### Typed signals

`types-PySide6` provides type safe signals and populates signal types on native classes.

In our stubs, `Signal` and `SignalInstance` are generic types, parametrized by one or more *signatures*, where
each signature is a tuple of argument types: e.g.
* `Signal(int, str)` is automatically detected as type `Signal[tuple[int, str]]`
* `Signal[tuple[int, str]]` expects a slot function like `def myslot(arg1: int, arg2: str)`
* Signals with multiple signatures are also supported, e.g.  `Signal((int, int), (str, str))` produces the type `Signal[tuple[int, int], tuple[str, str]]`, and can work with a slot function like `def myslot(arg1: int, arg2: str)` or `def myslot(arg1: str, arg2: str)`

This provides type safety in a few ways:

* `SignalInstance.connect()` enforces that the connected callable is compatible with the arguments emitted by
  the signal.
* Signals can be connected to other signals, and the receiving signal's arguments are checked the
  same way as a slot's.
* `SignalInstance.emit()` enforces the number and types of the arguments provided.
* Signals with multiple signatures are checked against their default (first) signature, which is
  the only signature an non-index `connect()`/`emit()` uses at runtime.  Indexing,
  e.g. `mysignal[str, str].connect(...)`, can be used to check against a specific signature: the
  index is validated against the signal's first or last signature (with up to four arguments
  each); the mypy plugin extends this to every declared signature.
* A native signal with a defaulted C++ parameter, e.g. `void clicked(bool checked = false)`, is
  *also* declared with multiple signatures, because that is how Qt registers it
  (`Signal[tuple[()], tuple[bool]]`).  There the trailing arguments genuinely are optional; the
  mypy plugin recognizes this case (see below).

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

Note that the actual `Signal` and `SignalInstance` classes are not indexable at runtime, so manual annotations must be forward references (wrapped in quotes):

```python
    signal6: "QtCore.Signal[tuple[int, str, float, bool, bytes]]" = QtCore.Signal(
        int, str, float, bool, bytes
    )
```

### Upstream fixes

The `types-PySide6` stub generator inspects the annotations extracted from the `PySide6` library and automatically applies numerous fixes.

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

### The mypy plugin

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

#### Signal indices are fully validated

At runtime, indexing a signal (e.g. `mysignal[int, str]`) selects the correspond signature,
while a *non-indexed* `connect()`/`emit()` uses the default (first) signature.
However, the stubs alone can only validate an index that matches the signal's first or last signature:
an index selecting a middle signature of a three-plus-signature signal is falsely flagged,
and an index that matches no declared signature at all falls through to an unchecked
catch-all, hiding the runtime `IndexError` and leaving everything called on the result
unchecked.  The plugin, on the other hand, validates an index against every declared signature and
narrows the result to the signature the index selects, so subsequent `connect()`/`emit()`
calls are checked against it -- exactly mirroring the runtime dispatch:

```python
def int_slot(arg: int) -> None:
    print(arg)


class MyObject(QtCore.QObject):
    signal: "QtCore.Signal[tuple[int, int], tuple[str], tuple[float, float]]" = (
        QtCore.Signal((int, int), (str,), (float, float))
    )

    def use_signatures(self) -> None:
        self.signal.emit(1, 2)                 # non-indexed signal defaults to the first signature, so this passes
        self.signal[int, int].emit("one", 2)   # stubs alone catches this error
        self.signal[str].emit("one", 2)        # only the plugin catches this TypeError
        self.signal[str].connect(int_slot)     # only the plugin catches this bad slot
        self.signal[str, str]                  # only the plugin catches this invalid index
        self.signal[bool, bool]                # ... and this one (bool is not int at runtime)
```

#### Signatures with C++ default arguments are checked correctly

Qt registers a separate signature for each parameter of a C++ signal with a default, 
so Qt's `void clicked(bool checked = false)` becomes PySide' `Signal[tuple[()], tuple[bool]]` -- the same as if the
Python signal were declared with two distinct signatures.  The two do not behave the same
way, though: for a default argument C++ simply fills in the default.
Wherever one signature of a *native* signal is a prefix of another, the plugin ensures that
runtime behavior is reflected in the static check:

* `connect()` accepts a slot taking as many arguments as the longest signature, because PySide
  connects a slot to the registered signature that has as many arguments as the slot.  So
  `button.clicked.connect(self.on_click)` type checks for an `on_click(self, checked: bool)`,
  and `checked` really is delivered.  This is the case that made
  `clicked`/`triggered`/`destroyed` slots hard to type.
* `emit()` may leave the defaulted arguments out:
  `model.dataChanged.emit(topLeft, bottomRight)` type checks, and slots taking the third
  argument still receive it, filled in by C++.
* What `emit()` may *not* do is pass more arguments than the default signature declares:
  `button.clicked.emit(True)` raises `TypeError` at runtime, because `clicked()` is the default
  signature.  Use `button.clicked[bool].emit(True)` to emit the other signature.

Signals declared in python are deliberately kept strict: a signal with a similar prefix-like
relationship between the signatures -- e.g. `Signal((int, str), (int,))` -- does not 
make anything optional -- `emit(1)` raises `TypeError` at runtime, and thus the mypy plugin
enforces this statically.

Note: The plugin recognizes a native signal by where it is declared, which it can only see when the signal is used directly
(`obj.sig.emit(...)`, `self.sig.connect(...)`); a signal read into a variable first
(`sig = button.clicked`) is checked strictly as if it were not a native C++ signal.

#### Use of `object` in signal instantiation can be configured to mean `typing.Any`

`Signal(object)` is the idiomatic way to declare a signal that emits an arbitrary value (Qt
registers it as `PyObject`).

```python
class MyObject(QtCore.QObject):
    signal1 = QtCore.Signal(object)  # signal takes MyCustomClass
```

Since an argument typed as `object` accepts only values of type `object` or `Any` this
common pattern will lead to numerous errors in a typical codebase. 

The proper way to handle this is to add a type annotation:

```python
class MyObject(QtCore.QObject):
    signal1: "Signal[tuple[MyCustomClass]]" = QtCore.Signal(object)
```

However, adding annotations throughout a codebase may be a heavy lift that you'd like to
defer till later, so the `mypy` plugin defaults to loosening this check by internally overriding `object`
arguments in `Signal(...)` declarations to `typing.Any`:

* `Signal(object)` becomes `Signal[tuple[Any]]`: any single-argument slot can be connected to it, and any
  value can be emitted through it.
* The override is per-argument, so mixed signals stay strict where they can be:
  `Signal(int, object)` infers as `Signal[tuple[int, Any]]`, and connecting a slot whose
  first argument is not compatible with `int` is still an error.
* Arguments declared as `typing.Any` (a real class at runtime since Python 3.11, which
  PySide6 likewise registers as `PyObject`) are treated the same way, so `Signal(Any)` also
  works.

#### Plugin options

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

## License

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
