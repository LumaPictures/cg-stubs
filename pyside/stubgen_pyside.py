from __future__ import absolute_import, print_function, annotations

import fnmatch
import importlib
import inspect
import pydoc
import re
import typing
from functools import lru_cache, total_ordering
from types import ModuleType
from typing import (
    Any,
    List,
    Optional,
    Hashable,
    Mapping,
    Tuple,
    cast,
)

import mypy.stubgen
import mypy.stubgenc
from mypy.stubdoc import ArgSig, FunctionSig, infer_sig_from_docstring
from mypy.stubutil import (
    FunctionContext,
    ClassInfo,
    SignatureGenerator,
)

from stubgenlib import reduce_overloads, AdvancedSignatureGenerator, Optionality

from PySide2 import QtCore, QtWidgets

cache = lru_cache(maxsize=None)

# TODO: support PySide6
PYSIDE = "PySide2"


def pyside(type_name: str) -> str:
    return type_name.replace("PySide2", PYSIDE)


def is_pyside_obj(typ: type) -> bool:
    return typ.__module__.split(".")[0] in PYSIDE


def get_type_fullname(typ: type) -> str:
    typename = getattr(typ, "__qualname__", typ.__name__)
    module_name = getattr(typ, "__module__", None)
    assert module_name is not None, typ
    if module_name != "builtins":
        typename = f"{module_name}.{typename}"
    return typename


@cache
def is_flag(typ: type) -> bool:
    return (
        hasattr(typ, "__pos__")
        and not hasattr(typ, "__invert__")
        and is_pyside_obj(typ)
        and typ.__bases__ == (object,)
    )


@cache
def is_flag_group(typ: type) -> bool:
    return (
        hasattr(typ, "__invert__")
        and not hasattr(typ, "values")
        and is_pyside_obj(typ)
        and typ.__bases__ == (object,)
    )


@cache
def is_flag_item(typ: type) -> bool:
    return (
        hasattr(typ, "__invert__")
        and hasattr(typ, "values")
        and is_pyside_obj(typ)
        and typ.__bases__ == (object,)
    )


_flag_group_to_item: dict[str, str] = {}


@cache
def get_group_from_flag_item(item_type: type) -> type:
    group_type = type(item_type() | item_type())
    _flag_group_to_item[get_type_fullname(group_type)] = get_type_fullname(item_type)
    return group_type


def get_flag_union(type_name: str | None) -> Optional[str]:
    """
    arguments that are group flags should also accept the corresponding item flag
    """
    if type_name:
        item_type_name = _flag_group_to_item.get(type_name)
        if item_type_name:
            result = "typing.Union[{}, {}]".format(type_name, item_type_name)
            return result
    return None


@cache
def get_properties(typ: type) -> Mapping[str, str]:
    """
    Get a mapping of property/signal name to type.
    """
    if not isinstance(typ, type) or not issubclass(typ, QtCore.QObject):
        return {}

    if typ.__bases__:
        base_props = get_properties(typ.__bases__[0])
    else:
        base_props = {}

    try:
        obj = typ()
    except Exception:
        return base_props

    try:
        meta = obj.metaObject()
    except AttributeError:
        return base_props

    def getsig(prop: QtCore.QMetaProperty) -> Tuple[str, str]:
        name = decode(prop.name())
        fallback_type = prop.type()
        # for some reason QtCore.Qt.GlobalColor is returned for many properties even though it's
        # wrong
        if fallback_type is QtCore.Qt.GlobalColor:
            # see if the property has a method since the signature return value can be used to
            # infer the property type.
            func = getattr(obj, name, None)
            if func is not None:
                sig = getattr(func, "__signature__", None)
                if isinstance(sig, inspect.Signature) and sig.return_annotation:
                    return name, typing._type_repr(sig.return_annotation)

            if prop.isEnumType():
                c_type_name = cast(str, prop.typeName())
                maybe_type_name = c_type_name.replace("::", ".")
                if maybe_type_name.startswith("Qt."):
                    maybe_type_name = "PySide2.QtCore." + maybe_type_name
                # elif maybe_type_name.startswith('Qt'):
                #     maybe_type_name = 'PySide2.' + maybe_type_name
                else:
                    maybe_type_name = typing._type_repr(typ) + "." + maybe_type_name

                # check that it's real
                if pydoc.locate(maybe_type_name) is None:
                    # FIXME: this could be improved with a more exhaustive search. seems like there
                    #  should be a better way.
                    print(
                        "{}.{}: Could not determine type of property".format(
                            typing._type_repr(typ), name
                        )
                    )
                    print("  {}".format(c_type_name))
                    print("  {}".format(maybe_type_name))
                    type_name = "typing.Any"
                else:
                    type_name = maybe_type_name
            else:
                type_name = "typing.Any"
            return name, type_name
        return name, typing._type_repr(fallback_type)

    def decode(x: QtCore.QByteArray | str | bytes) -> str:
        if isinstance(x, QtCore.QByteArray):
            return bytes(x).decode()
        elif isinstance(x, bytes):
            return x.decode()
        else:
            return x

    result = dict(base_props)
    props = [meta.property(i) for i in range(meta.propertyCount())]
    result.update(getsig(prop) for prop in props)

    methods = [meta.method(i) for i in range(meta.methodCount())]
    signals = [
        decode(meth.name())
        for meth in methods
        if meth.methodType() == QtCore.QMetaMethod.MethodType.Signal
    ]

    result.update((name, "typing.Callable") for name in signals)
    obj.deleteLater()

    return result


def add_property_args(typ: type, sigs: List[FunctionSig]) -> None:
    """
    Extend the signatures to include keyword arguments for properties and signals.
    """
    properties = get_properties(typ)
    if properties:
        property_names = set(properties)
        for sig in sigs:
            arg_names = [arg.name for arg in sig.args]
            missing = property_names.difference(arg_names)
            if missing:
                try:
                    index = arg_names.index("**kwargs")
                except ValueError:
                    index = len(arg_names)
                sig.args[index:index] = [
                    ArgSig(name=name, type=properties[name], default=True)
                    for name in sorted(missing)
                ]


def short_name(type_name: str) -> str:
    return type_name.split(".")[-1]


class PySideSignatureGenerator(AdvancedSignatureGenerator):
    # Full signature replacements.
    # The class name can be "*", in which case it will match any class
    signature_overrides: dict[str, str | list[str]] = {
        # these docstring sigs are malformed
        "*.VolatileBool.get": "(self) -> bool",
        "*.VolatileBool.set": "(self, a: object) -> None",
        # * Add all signals and make all new-style signal patterns work.  e.g.
        # `myobject.mysignal.connect(func) and `myobject.mysignal[type].connect(func)`
        "*.Signal.__get__": [
            "(self, instance: None, owner: typing.Type[QObject]) -> Signal",
            "(self, instance: QObject, owner: typing.Type[QObject]) -> SignalInstance",
        ],
        "*.Signal.__getitem__": "(self, index) -> SignalInstance",
        "*.SignalInstance.__getitem__": "(self, index) -> SignalInstance",
        # * Fix slot arg of `SignalInstance.connect()` to be `typing.Callable` instead of `object`
        "*.SignalInstance.connect": "(self, slot: typing.Callable, type: typing.Union[type,None] = ...) -> bool",
        "*.SignalInstance.disconnect": "(self, slot: typing.Union[typing.Callable,None] = ...) -> None",
        "*.QObject.disconnect": [
            "(cls, arg__1: PySide2.QtCore.QObject, arg__2: str = ..., arg__3: typing.Callable = ...) -> bool",
            "(cls, arg__1: PySide2.QtCore.QMetaObject.Connection) -> bool",
            "(cls, sender: PySide2.QtCore.QObject, signal: PySide2.QtCore.QMetaMethod, receiver: PySide2.QtCore.QObject = ..., member: PySide2.QtCore.QMetaMethod = ...) -> bool",
        ],
        "*.QWidget.setParent": "(self, parent: typing.Union[PySide2.QtCore.QObject,None], f: PySide2.QtCore.Qt.WindowFlags = ...) -> None",
        # * Correct numerous annotations from `bytes` to `str`
        "*.QObject.setProperty": "(self, name: str, value: typing.Any) -> bool",
        "*.QObject.property": "(self, name: str) -> typing.Any",
        "*.QState.assignProperty": "(self, object: QObject, name: str, value: typing.Any) -> None",
        # ("*", 'propertyName'):
        #     '(self) -> str',
        "*.QCoreApplication.translate": "(cls, context: str, key: str, disambiguation: typing.Union[str,NoneType] = ..., n: int = ...) -> str",
        # * Fix `QTreeWidgetItemIterator.__iter__()` to iterate over `QTreeWidgetItemIterator`
        # Add result type
        "*.QTreeWidgetItemIterator.__iter__": "(self) -> typing.Iterator[QTreeWidgetItemIterator]",
        "*.QTreeWidgetItemIterator.__next__": "(self) -> QTreeWidgetItemIterator",
        # * Make result optional
        "*.QLayout.itemAt": "(self, index: int) -> typing.Optional[PySide2.QtWidgets.QLayoutItem]",
        "*.QLayout.takeAt": "(self, index: int) -> typing.Optional[PySide2.QtWidgets.QLayoutItem]",
        # * Fix QPolygon special methods
        # first and third overloads should return QPolygon
        "*.QPolygon.__lshift__": [
            "(self, l: list[PySide2.QtCore.QPoint]) -> PySide2.QtGui.QPolygon",
            "(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream",
            "(self, t: PySide2.QtCore.QPoint) -> PySide2.QtGui.QPolygon",
        ],
        # should return QPolygon
        "*.QPolygon.__iadd__": "(self, t: PySide2.QtCore.QPoint) -> PySide2.QtGui.QPolygon",
        # * Fix `QByteArray(b'foo')[0]` to return `bytes`
        # missing index and return.
        "*.QByteArray.__getitem__": "(self, index: int) -> bytes",
        # * Fix `QByteArray.__iter__()` to iterate over `bytes`
        # * Fix support for `bytes(QByteArray(b'foo'))`
        "*.QByteArray.__bytes__": "(self) -> bytes",
        # FIXME: make this a general rule
        # * Replace `object` with `typing.Any` in return types
        "*.QSettings.value": (
            "(self, arg__1: str, defaultValue: typing.Union[typing.Any, None] = ..., "
            "type: typing.Union[typing.Any, None] = ...) -> typing.Any"
        ),
        "*.QModelIndex.internalPointer": "(self) -> typing.Any",
        "*.QPersistentModelIndex.internalPointer": "(self) -> typing.Any",
        # Fix other flags:
        "*.QSortFilterProxyModel.filterRole": "(self) -> PySide2.QtCore.Qt.ItemDataRole",
        "*.QStandardItem.type": "(self) -> PySide2.QtGui.QStandardItem.ItemType",
        "*.QTableWidgetItem.setTextAlignment": "(self, alignment: PySide2.QtCore.Qt.Alignment) -> None",
        "*.QFrame.setFrameStyle": "(self, arg__1: typing.Union[PySide2.QtWidgets.QFrame.Shape, PySide2.QtWidgets.QFrame.Shadow, typing.SupportsInt]) -> None",
        # in PySide2 these take int, and in PySide6 it takes Weight, but both seem valid
        "*.QFont.setWeight": "(self, arg__1: typing.Union[int, PySide2.QtGui.QFont.Weight]) -> None",
        "*.QTextEdit.setFontWeight": "(self, w: typing.Union[int, PySide2.QtGui.QFont.Weight]) -> None",
        # ('QFont', 'weight': pyside('(self) -> PySide2.QtGui.QFont.Weight'),  # fixed in PySide6
        # * Fix arguments that accept `QModelIndex` which were typed as `int` in many places
        # known offenders: QAbstractItemView, QItemSelectionModel, QTreeView, QListView
        "*.selectedIndexes": "(self) -> list[PySide2.QtCore.QModelIndex]",
        "*.QItemSelectionModel.selectedColumns": "(self, row: int = ...) -> list[PySide2.QtCore.QModelIndex]",
        "*.QItemSelectionModel.selectedRows": "(self, column: int = ...) -> list[PySide2.QtCore.QModelIndex]",
        "*.QItemSelection.indexes": "(self) -> list[PySide2.QtCore.QModelIndex]",
        "*.QItemSelectionRange.indexes": "(self) -> list[PySide2.QtCore.QModelIndex]",
        "*.QAbstractItemModel.mimeData": "(self, indexes: list[PySide2.QtCore.QModelIndex]) -> PySide2.QtCore.QMimeData",
        "*.QStandardItemModel.mimeData": "(self, indexes: list[PySide2.QtCore.QModelIndex]) -> PySide2.QtCore.QMimeData",
        # * Fix return type for `QApplication.instance()` and `QGuiApplication.instance()` :
        "*.QCoreApplication.instance": "(cls: typing.Type[T]) -> T",
        # * Fix return type for `QObject.findChild()` and `QObject.findChildren()` :
        "*.QObject.findChild": "(self, arg__1: typing.Type[T], arg__2: str = ...) -> T",
        "*.QObject.findChildren": [
            "(self, arg__1: typing.Type[T], arg__2: QRegExp = ...) -> list[T]",
            "(self, arg__1: typing.Type[T], arg__2: QRegularExpression = ...) -> list[T]",
            "(self, arg__1: typing.Type[T], arg__2: str = ...) -> list[T]",
        ],
        "*.qVersion": "() -> str",
        # FIXME: this can be handled by merging with the default sig
        # signatures for these special methods include many inaccurate overloads
        "*.__ne__": "(self, other: object) -> bool",
        "*.__eq__": "(self, other: object) -> bool",
        "*.__lt__": "(self, other: object) -> bool",
        "*.__gt__": "(self, other: object) -> bool",
        "*.__le__": "(self, other: object) -> bool",
        "*.__ge__": "(self, other: object) -> bool",
    }

    # Special methods for flag enums.
    flag_overrides = {
        # FIXME: QFrame.Shape and QFrame.Shadow are meant to be used with each other and return an int
        "__or__": "(self, other: typing.SupportsInt) -> {}",
        "__ror__": "(self, other: typing.SupportsInt) -> {}",
        "__and__": "(self, other: typing.SupportsInt) -> {}",
        "__rand__": "(self, other: typing.SupportsInt) -> {}",
        "__xor__": "(self, other: typing.SupportsInt) -> {}",
        "__rxor__": "(self, other: typing.SupportsInt) -> {}",
        "__lshift__": "(self, other: typing.SupportsInt) -> {}",
        "__rshift__": "(self, other: typing.SupportsInt) -> {}",
        "__add__": "(self, other: typing.SupportsInt) -> {}",
        "__radd__": "(self, other: typing.SupportsInt) -> {}",
        "__mul__": "(self, other: typing.SupportsInt) -> {}",
        "__rmul__": "(self, other: typing.SupportsInt) -> {}",
        "__sub__": "(self, other: typing.SupportsInt) -> {}",
        "__rsub__": "(self, other: typing.SupportsInt) -> {}",
        "__invert__": "(self) -> {}",
    }

    # Types that have implicit alternatives.
    implicit_arg_types: dict[str, list[str]] = {
        "PySide2.QtGui.QKeySequence": ["str"],
        "PySide2.QtGui.QColor": ["PySide2.QtCore.Qt.GlobalColor", "int"],
        "PySide2.QtCore.QByteArray": ["bytes"],
        "PySide2.QtGui.QBrush": [
            "PySide2.QtGui.QColor",
            "PySide2.QtCore.Qt.GlobalColor",
            "PySide2.QtGui.QLinearGradient",
        ],
        "PySide2.QtGui.QCursor": ["PySide2.QtCore.Qt.CursorShape"],
        "PySide2.QtCore.QEasingCurve": ["PySide2.QtCore.QEasingCurve.Type"],
        "PySide2.QtCore.QDate": ["datetime.date"],
        "PySide2.QtCore.QDateTime": ["datetime.datetime"],
    }

    # Override argument types
    arg_type_overrides: dict[tuple[str, str, str | None], str] = {
        # (method, arg, type)
        ("*", "flags", "int"): "typing.SupportsInt",
        ("*", "weight", "int"): "typing.SupportsInt",
        ("*", "format", "typing.Union[bytes,NoneType]"): "typing.Optional[str]",
        ("*", "role", "int"): "PySide2.QtCore.Qt.ItemDataRole",
        ("*.addAction", "*", "object"): "typing.Callable[[], typing.Any]",
    }

    # Find and replace argument names
    arg_name_replacements: dict[tuple[str, str, str | None], str] = {
        # (method, arg, type)
    }

    # Values which should be made Optional[].
    optional_args: dict[tuple[str, str, str | None], Optionality] = {
        # (method, arg, type)
        ("*.QPainter.drawText", "br", "*"): Optionality(
            accepts_none=True, has_default=True
        ),
        ("*.QPainter.drawPolygon", "arg__2", "*"): Optionality(
            accepts_none=True, has_default=True
        ),
        ("*.QProgressDialog.setCancelButton", "button", "*"): Optionality(
            accepts_none=True, has_default=False
        ),
        ("*.setModel", "model", "*"): Optionality(accepts_none=True, has_default=False),
        ("*.QLabel.setPixmap", "arg__1", "*"): Optionality(
            accepts_none=True, has_default=False
        ),
        ("*", "parent", "PySide2.QtWidgets.QWidget"): Optionality(
            accepts_none=True, has_default=False
        ),
        ("*", "parent", "PySide2.QtCore.QObject"): Optionality(
            accepts_none=True, has_default=False
        ),
        ("*.QInputDialog.getText", "echo", "*"): Optionality(
            accepts_none=False, has_default=True
        ),
    }

    # Add new overloads to existing functions.
    new_overloads: dict[str, list[str]] = {
        # * Add `QSpacerItem.__init__/changeSize` overloads that use alternate names: `hData`->`hPolicy`, `vData`->`vPolicy`
        "*.QSpacerItem.__init__": [
            "(self, w:int, h:int, hPolicy:PySide2.QtWidgets.QSizePolicy.Policy=..., vPolicy:PySide2.QtWidgets.QSizePolicy.Policy=...) -> None"
        ],
        "*.QSpacerItem.changeSize": [
            "(self, w:int, h:int, hPolicy:PySide2.QtWidgets.QSizePolicy.Policy=..., vPolicy:PySide2.QtWidgets.QSizePolicy.Policy=...) -> None"
        ],
    }

    new_members = {
        # can use any method as a stand-in.  signatures will come from _signature_overrides
        "QByteArray": [
            ("__bytes__", QtCore.QByteArray.__len__),
        ],
        "QDialog": [
            # this method does not exist at the class-level, and only exists once an instance
            # is created.
            ("exec", QtWidgets.QDialog.exec_),
        ],
    }

    # FIXME: implement?
    def get_property_type(
        self, default_type: str | None, ctx: FunctionContext
    ) -> str | None:
        return default_type

    def is_flag_type(self, ctx: FunctionContext) -> bool:
        if ctx.class_info is None:
            return False
        typ = ctx.class_info.cls
        return (
            typ is not None
            and (is_flag(typ) or is_flag_group(typ) or is_flag_item(typ))
            and ctx.name in self.flag_overrides
        )

    def get_docstr(self, ctx: FunctionContext) -> str | list[str] | None:
        if self.is_flag_type(ctx):
            assert ctx.class_info is not None
            typ = ctx.class_info.cls
            docstr_override = self.flag_overrides[ctx.name]
            if is_flag_item(typ):
                return_type = get_group_from_flag_item(typ)
            elif typ is not None:
                return_type = typ
            else:
                return None
            return docstr_override.format(get_type_fullname(return_type))
        else:
            return super().get_docstr(ctx)

    def process_arg(self, ctx: FunctionContext, arg: ArgSig) -> None:
        """Update ArgSig in place"""

        if not arg.type:
            return

        arg_type = arg.type.replace(" ", "")
        arg_type = re.sub(r"\btyping\.Sequence\b", "typing.Iterable", arg_type)
        arg.type = arg_type

        # if key in self.arg_name_replacements:
        #     arg.name = self.arg_name_replacements[key]

        super().process_arg(ctx, arg)

        # arg + type:
        # note: QDataWidgetMapper.addMapping expects bytes
        if (
            ctx.name != "addMapping"
            and not fnmatch.fnmatch(ctx.fullname, "*.QPropertyAnimation.*")
            and arg.name == "propertyName"
            and short_name(arg_type) == "QByteArray"
        ):
            arg.type = "str"
        else:
            new_type = get_flag_union(arg.type)
            if new_type is not None:
                arg.type = new_type

    def process_sig(self, ctx: FunctionContext, sig: FunctionSig) -> FunctionSig:
        sig = super().process_sig(ctx, sig)

        new_type = get_flag_union(sig.ret_type)
        if new_type is not None:
            return sig._replace(ret_type=new_type)
        if ctx.name == "__init__" and sig.ret_type != "None":
            return sig._replace(ret_type="None")
        return sig

    def process_sigs(
        self, ctx: FunctionContext, results: list[FunctionSig]
    ) -> list[FunctionSig] | None:
        if self.is_flag_type(ctx):
            return results

        results = reduce_overloads(results)

        if (
            ctx.class_info is not None
            and ctx.class_info.cls is not None
            and ctx.name == "__init__"
        ):
            add_property_args(ctx.class_info.cls, results)

        return super().process_sigs(ctx, results)


class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if not _flag_group_to_item:
            seen: set[type] = set()
            for known_module_name in self.known_modules:
                module = importlib.import_module(known_module_name)
                self.walk_objects(module, seen)

    def walk_objects(self, obj: object, seen: set[type]) -> None:
        for _, child in self.get_members(obj):
            if inspect.isclass(child):
                if child in seen:
                    continue
                seen.add(child)
                # add to the cache
                child = cast(type, child)
                get_properties(child)
                if is_flag_item(child):
                    # add to the cache
                    get_group_from_flag_item(child)
                self.walk_objects(child, seen)

    def get_sig_generators(self) -> list[SignatureGenerator]:
        sig_generators = super().get_sig_generators()
        sig_generators.insert(0, PySideSignatureGenerator())
        return sig_generators

    def _is_skipped_pyside_attribute(self, attr: str, value: Any) -> bool:
        if not attr.isidentifier():
            return True
        # these are unecesssary
        if attr in ("__delattr__", "__setattr__", "__reduce__"):
            return True
        # many objects have __hash__ = None which causes mypy errors in the stubs. not sure how best
        # to handle this.  are these objects hashable?
        if attr == "__hash__" and value is None:
            return True
        return False

    def add_name(self, fullname: str, require: bool = True) -> str:
        module, name = fullname.rsplit(".", 1)
        # force use of typing module for safe namespacing.
        self.import_tracker.require_name(module)
        self.import_tracker.add_import(module)
        return f"{module}.{name}"

    def is_method(self, class_info: ClassInfo, name: str, obj: object) -> bool:
        # QtCore.Signal gets mistaken for a method descriptor because it has a __get__
        if type(obj).__name__ == "Signal":
            return False
        return super().is_method(class_info, name, obj)

    def strip_or_import(self, type_name: str) -> str:
        type_name = type_name.replace("Shiboken.", "shiboken2.")
        stripped_type = super().strip_or_import(type_name)
        return stripped_type

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        members = [
            x
            for x in super().get_members(obj)
            if not self._is_skipped_pyside_attribute(x[0], x[1])
        ]
        if isinstance(obj, type):
            return members + PySideSignatureGenerator.new_members.get(obj.__name__, [])
        return members

    def get_imports(self) -> str:
        imports = super().get_imports().split("\n")

        for i, line in enumerate(imports):
            if line.startswith("import typing"):
                imports = (
                    imports[:i] + [line, "T = typing.TypeVar('T')"] + imports[i + 1 :]
                )
                break
        return "\n".join(imports)


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[attr-defined,misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]

if __name__ == "__main__":
    # in order to create and inspect object properties we must create an app
    app = QtWidgets.QApplication()

    mypy.stubgen.main()
