
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
* Added all methods to flag classes: `__or__`, `__xor__`, ...

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
* Corrected numerous annotations from `bytes/QByteArray` to `str`:
  * `QObject.setProperty()`
  * `QObject.property()`
  * `QState.assignProperty()`
  * `QCoreApplication.translate()`
  * `format` args on all methods
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
* Add type enforcement for signal types, to protect against incorrect callables provided to `connect()`
