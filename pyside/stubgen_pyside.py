from __future__ import absolute_import, annotations, print_function

import atexit
import enum
import fnmatch
import importlib
import inspect
import json
import pydoc
import re
import types
import typing
from collections import defaultdict
from functools import cached_property, lru_cache
from pathlib import Path
from typing import (
    Any,
    List,
    Mapping,
    Optional,
    Tuple,
    cast,
)

import mypy.stubgen
import mypy.stubgenc
from mypy.stubdoc import ArgSig, FunctionSig
from mypy.stubutil import (
    ClassInfo,
    FunctionContext,
    SignatureGenerator,
)

from stubgenlib.siggen import (
    AdvancedSigMatcher,
    AdvancedSignatureGenerator,
    Optionality,
)
from stubgenlib.siggen.advanced import Overridden
from stubgenlib.utils import (
    insert_typevars,
    remove_overlapping_overloads,
)

cache = lru_cache(maxsize=None)


def short_name(type_name: str) -> str:
    return type_name.split(".")[-1]


def get_type_fullname(typ: type) -> str:
    typename = getattr(typ, "__qualname__", typ.__name__)
    module_name = getattr(typ, "__module__", None)
    assert module_name is not None, typ
    if module_name != "builtins":
        typename = f"{module_name}.{typename}"
    return typename


class PySideHelper:
    _flag_group_to_item: dict[str, str] = {}
    _flag_short_name_to_full_name: defaultdict[str, set[str]] = defaultdict(set)
    _flag_item_short_name_to_full_name: defaultdict[str, dict[str, object]] = (
        defaultdict(dict)
    )
    _signals: dict[str, list[str]] = {}

    def __init__(self) -> None:
        self._pyside_package: str | None = None
        self._shiboken_package: str | None = None
        self.QtCore: types.ModuleType = None  # type: ignore[assignment]
        self.QtWidgets: types.ModuleType = None  # type: ignore[assignment]

    def is_pyside_obj(self, typ: type) -> bool:
        return typ.__module__.split(".")[0] in self.pyside_package

    @cached_property
    def primary_pyside_modules(self) -> tuple[str, ...]:
        return (
            f"{self.pyside_package}.QtCore",
            f"{self.pyside_package}.QtGui",
            f"{self.pyside_package}.QtWidgets",
        )

    @cache
    def is_flag(self, typ: type) -> bool:
        """A flag enum

        is_flag(PySide2.QtCore.QDir.Filter) is True
        is_flag(PySide6.QtCore.QDir.Filter) is True
        """
        if self.pyside_package == "PySide6":
            # FIXME: flag groups such as PySide6.QtCore.QDir.Filters will return True here
            return isinstance(typ, type) and issubclass(typ, enum.Flag)
        else:
            # in PySide2, the type of a flag item is a flag
            return self.is_flag_item_type(typ)

    @cache
    def is_enum(self, typ: type) -> bool:
        """An enum

        unlike flags, enums cannot be combined.

        is_enum(PySide2.QtCore.QLocale.Language) is True
        is_enum(PySide6.QtCore.QLocale.Language) is True
        """
        if self.pyside_package == "PySide6":
            # FIXME: flag groups such as PySide6.QtCore.QDir.Filters will return True here
            return isinstance(typ, type) and issubclass(typ, enum.Enum)
        else:
            return (
                hasattr(typ, "__pos__")
                and not hasattr(typ, "__invert__")
                and self.is_pyside_obj(typ)
                and typ.__bases__ == (object,)
            )

    def is_enum_item(self, obj: object) -> bool:
        """An individual enum item

        e.g.

        is_enum_item(PySide2.QtCore.QLocale.Language.Abkhazian) is True
        is_enum_item(PySide6.QtCore.QLocale.Language.Abkhazian) is True
        """
        if self.pyside_package == "PySide6":
            return isinstance(obj, enum.Enum) and not isinstance(obj, enum.Flag)
        else:
            return self.is_enum(type(obj))

    @cache
    def is_flag_group(self, typ: type) -> bool:
        """The result of joining two flag items

        In PySide6, with the switch to enum.Enum, the group and enum are the same
        object.

        e.g. PySide2.QtCore.QDir.Filters
        """
        if self.pyside_package == "PySide6":
            return False
        else:
            return (
                hasattr(typ, "__invert__")
                and not hasattr(typ, "values")
                and self.is_pyside_obj(typ)
                and typ.__bases__ == (object,)
            )

    @cache
    def is_flag_item_type(self, typ: type) -> bool:
        """The type of an individual flag item

        e.g.

        is_flag_item_type(type(PySide2.QtCore.QDir.Filter.AllDirs)) is True
        is_flag_item_type(type(PySide6.QtCore.QDir.Filter.AllDirs)) is True
        """
        if self.pyside_package == "PySide6":
            return isinstance(typ, type) and issubclass(typ, enum.Enum)
        else:
            return (
                hasattr(typ, "__invert__")
                and hasattr(typ, "values")
                and self.is_pyside_obj(typ)
                and typ.__bases__ == (object,)
            )

    def is_flag_item(self, obj: object) -> bool:
        """An individual flag item

        e.g.

        is_flag_item(PySide2.QtCore.QDir.Filter.AllDirs) is True
        is_flag_item(PySide6.QtCore.QDir.Filter.AllDirs) is True
        """
        if self.pyside_package == "PySide6":
            return isinstance(obj, enum.Flag)
        else:
            return self.is_flag_item_type(type(obj))

    def record_flag(self, flag: enum.EnumType) -> None:
        flag_full_name = get_type_fullname(flag)
        self.__class__._flag_short_name_to_full_name[short_name(flag_full_name)].add(
            flag_full_name
        )
        if flag_full_name.startswith(self.primary_pyside_modules):
            # we're gathering these to know the members of PySide6.QtCore.Qt so we only check the
            # key modules
            for flag_item_name in dir(flag):
                if flag_item_name[0].isupper():
                    flag_item = getattr(flag, flag_item_name)
                    self.__class__._flag_item_short_name_to_full_name[flag_item_name][
                        flag_full_name
                    ] = flag_item

    def record_signal(
        self,
        cls: type,
        signal_name: str,
        signal: "QtCore.Signal",  # type: ignore[name-defined]
    ) -> None:
        full_class_name = get_type_fullname(cls)

        signatures = signal.signatures
        if signatures:
            # FIXME: should we skip signals with multiple overloads?  Is there a way to represent multiple?
            # Take the first signature (there might be multiple overloads)
            signature = signatures[0]

            # Parse the signature string to extract argument types
            # Format is like "timeout()" or "columnsAboutToBeInserted(QModelIndex,int,int)"
            if "(" in signature and ")" in signature:
                args_part = signature.split("(")[1].split(")")[0]
                if args_part.strip():
                    # Split by comma and clean up whitespace
                    arg_types = [
                        self.c_type_to_python_type(
                            full_class_name, arg_type.strip(), signal_name
                        )
                        for arg_type in args_part.split(",")
                    ]
                else:
                    arg_types = []
            else:
                arg_types = []
            self.__class__._signals[f"{full_class_name}.{signal_name}"] = arg_types

    def get_signal(self, cls: type, signal_name: str) -> list[str] | None:
        full_class_name = get_type_fullname(cls)
        try:
            return self.__class__._signals[f"{full_class_name}.{signal_name}"]
        except KeyError:
            return None

    @cache
    def get_group_from_flag_item(self, item_type: type) -> type:
        if self.pyside_package == "PySide6":
            raise RuntimeError("Should not get here")
        else:
            group_type = type(item_type() | item_type())
            self.__class__._flag_group_to_item[get_type_fullname(group_type)] = (
                get_type_fullname(item_type)
            )
            return group_type

    def get_flag_union(self, type_name: str | None) -> Optional[str]:
        """
        arguments that are group flags should also accept the corresponding item flag
        """
        if type_name:
            item_type_name = self.__class__._flag_group_to_item.get(type_name)
            if item_type_name:
                result = "typing.Union[{}, {}]".format(type_name, item_type_name)
                return result
        return None

    @cache
    def c_type_to_python_type(
        self, parent_type_name: str, c_type_name: str, prop_name: str
    ) -> str:
        maybe_type = {
            "bool": "bool",
            "int": "int",
            "uint": "int",
            "qlonglong": "int",
            "QLibrary::LoadHints": "int",
            "float": "float",
            "double": "float",
            "QString": "str",
        }.get(c_type_name)
        if maybe_type is not None:
            return maybe_type

        maybe_type_name = c_type_name.replace("::", ".").replace("*", "")

        options = []
        # search on the current class first
        options.append(f"{parent_type_name}.{maybe_type_name}")
        parts = parent_type_name.split(".")
        parent_module = ".".join(parts[:2])
        # next look in the parent module
        options.append(f"{parent_module}.{maybe_type_name}")

        # next look in key modules
        for module in self.primary_pyside_modules:
            if module == parent_module:
                continue
            options.append(f"{module}.{maybe_type_name}")

        for search_name in options:
            # check that it's real
            if pydoc.locate(search_name) is not None:
                return search_name

        # finally, look in our collection of enums, but only if it's an unambiguous match
        known_types = self._flag_short_name_to_full_name.get(maybe_type_name)
        if known_types:
            if len(known_types) == 1:
                return list(known_types)[0]

            for item in sorted(known_types):
                if item.startswith(parent_module + "."):
                    return item

            print(f"{parent_type_name}.{prop_name}: more than one known match")

        print(f"{parent_type_name}.{prop_name}: Could not determine type of property")
        print("  {}".format(c_type_name))
        print("  {}".format(maybe_type_name))
        return "typing.Any"

    @cache
    def get_properties(self, typ: type) -> Mapping[str, str]:
        """
        Get a mapping of property/signal name to type.
        """
        if not isinstance(typ, type) or not issubclass(typ, self.QtCore.QObject):
            return {}

        if typ.__bases__:
            base_props = self.get_properties(typ.__bases__[0])
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

        def getsig(prop: "QtCore.QMetaProperty") -> Tuple[str, str]:  # type: ignore[name-defined]
            prop_name = decode(prop.name())
            c_type_name = cast(str, prop.typeName())
            # do a search based on what we know of the parent type and the C++ type name
            type_name = self.c_type_to_python_type(
                typing._type_repr(typ), c_type_name, prop_name
            )
            if type_name == "typing.Any":
                # see if the property has a method since the signature return value can be used to
                # infer the property type.
                # FIXME: it's unclear whether this approach should take higher priority than
                #  c_type_to_python_type.  It results in seemingly subtle differences for about
                #  20 properties.  This seems super niche.
                func = getattr(obj, prop_name, None)
                if func is not None:
                    sig = getattr(func, "__signature__", None)
                    if isinstance(sig, inspect.Signature) and sig.return_annotation:
                        return prop_name, typing._type_repr(sig.return_annotation)

            return prop_name, type_name

        def decode(x: "QtCore.QByteArray" | str | bytes) -> str:  # type: ignore[name-defined]
            if isinstance(x, self.QtCore.QByteArray):
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
            if meth.methodType() == self.QtCore.QMetaMethod.MethodType.Signal
        ]

        result.update((name, "typing.Callable") for name in signals)
        obj.deleteLater()

        return result

    def add_property_args(self, typ: type, sigs: List[FunctionSig]) -> None:
        """
        Extend the signatures to include keyword arguments for properties and signals.
        """
        properties = self.get_properties(typ)
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

    def set_pyside_version(self, version: int) -> None:
        import importlib

        self._pyside_package = f"PySide{version}"
        self._shiboken_package = f"shiboken{version}"

        self.QtCore = importlib.import_module(f"{self._pyside_package}.QtCore")
        self.QtWidgets = importlib.import_module(f"{self._pyside_package}.QtWidgets")

    @cached_property
    def pyside_package(self) -> str:
        if self._pyside_package is None:
            raise RuntimeError("Must call set_pyside_version before generating stubs")
        return self._pyside_package

    @cached_property
    def shiboken_package(self) -> str:
        if self._shiboken_package is None:
            raise RuntimeError("Must call set_pyside_version before generating stubs")
        return self._shiboken_package

    @cached_property
    def new_members(self) -> dict[str, list[tuple[str, object]]]:
        return {
            # can use any method as a stand-in.  signatures will come from _signature_overrides
            "QByteArray": [
                ("__bytes__", self.QtCore.QByteArray.__len__),
            ],
            "QDialog": [
                # this method does not exist at the class-level, and only exists once an instance
                # is created.
                ("exec", self.QtWidgets.QDialog.exec_),
            ],
        }

    def add_version_info(self) -> None:
        init = Path("stubs").joinpath(self.pyside_package, "__init__.pyi")
        init.write_text(
            init.read_text()
            + "__version__: str\n__version_info__: tuple[int, int, float, str, str]\n"
        )


class PySideSignatureGenerator(AdvancedSignatureGenerator):
    @cached_property
    def sig_matcher(self) -> AdvancedSigMatcher:  # type: ignore[override]
        PYSIDE = helper.pyside_package

        matcher = AdvancedSigMatcher(
            # Full signature replacements.
            # The class name can be "*", in which case it will match any class
            signature_overrides={
                # these docstring sigs are malformed
                "*.VolatileBool.get": "(self) -> bool",
                "*.VolatileBool.set": "(self, a: object) -> None",
                # * Add all signals and make all new-style signal patterns work.  e.g.
                # `myobject.mysignal.connect(func) and `myobject.mysignal[type].connect(func)`
                "PySide6.QtCore.Signal.__get__": [
                    "(self, instance: None, owner: type[QObject]) -> Signal[*_SignalTypes]",
                    "(self, instance: QObject, owner: type[QObject]) -> SignalInstance[*_SignalTypes]",
                ],
                "PySide6.QtCore.Signal.__getitem__": "(self, index) -> SignalInstance[*_SignalTypes]",
                # "PySide6.QtCore.Signal.__init__": [
                #     # no args
                #     "(self: Signal[()], /, name: str | None = ..., arguments: Optional[List[str]] = ...) -> None: ...",
                #     # 1-4 args
                #     "(self: Signal[_T1], arg1: type[_T1], /, name: str | None = ..., arguments: Optional[List[str]] = ...) -> None: ...",
                #     "(self: Signal[_T1, _T2], arg1: type[_T1], arg2: type[_T2], /, name: str | None = ..., arguments: Optional[List[str]] = ...) -> None: ...",
                #     "(self: Signal[_T1, _T2, _T3], arg1: type[_T1], arg2: type[_T2], arg3: type[_T3], /, name: str | None = ..., arguments: Optional[List[str]] = ...) -> None: ...",
                #     "(self: Signal[_T1, _T2, _T3, _T4], arg1: type[_T1], arg2: type[_T2], arg3: type[_T3], arg4: type[_T4], /, name: str | None = ..., arguments: Optional[List[str]] = ...) -> None: ...",
                #     # catchall for everything else, including tuple args
                #     "(self, /, *types: type, name: str | None = ..., arguments: Optional[List[str]] = ...) -> None: ...",
                # ],
                "PySide6.QtCore.Signal.__init__": [
                    # no args
                    FunctionSig(
                        "__init__",
                        [
                            ArgSig("self", "Signal[()]"),
                            ArgSig("/"),
                            ArgSig("name", "str | None", default=True),
                            ArgSig("arguments", "Optional[List[str]]", default=True),
                        ],
                        ret_type="None",
                    ),
                    # 1-4 args
                    FunctionSig(
                        "__init__",
                        [
                            ArgSig("self", "Signal[_T1]"),
                            ArgSig("arg1", "type[_T1]"),
                            ArgSig("/"),
                            ArgSig("name", "str | None", default=True),
                            ArgSig("arguments", "Optional[List[str]]", default=True),
                        ],
                        ret_type="None",
                    ),
                    FunctionSig(
                        "__init__",
                        [
                            ArgSig("self", "Signal[_T1, _T2]"),
                            ArgSig("arg1", "type[_T1]"),
                            ArgSig("arg2", "type[_T2]"),
                            ArgSig("/"),
                            ArgSig("name", "str | None", default=True),
                            ArgSig("arguments", "Optional[List[str]]", default=True),
                        ],
                        ret_type="None",
                    ),
                    FunctionSig(
                        "__init__",
                        [
                            ArgSig("self", "Signal[_T1, _T2, _T3]"),
                            ArgSig("arg1", "type[_T1]"),
                            ArgSig("arg2", "type[_T2]"),
                            ArgSig("arg3", "type[_T3]"),
                            ArgSig("/"),
                            ArgSig("name", "str | None", default=True),
                            ArgSig("arguments", "Optional[List[str]]", default=True),
                        ],
                        ret_type="None",
                    ),
                    FunctionSig(
                        "__init__",
                        [
                            ArgSig("self", "Signal[_T1, _T2, _T3, _T4]"),
                            ArgSig("arg1", "type[_T1]"),
                            ArgSig("arg2", "type[_T2]"),
                            ArgSig("arg3", "type[_T3]"),
                            ArgSig("arg4", "type[_T4]"),
                            ArgSig("/"),
                            ArgSig("name", "str | None", default=True),
                            ArgSig("arguments", "Optional[List[str]]", default=True),
                        ],
                        ret_type="None",
                    ),
                    # catchall for tuples
                    FunctionSig(
                        "__init__",
                        [
                            ArgSig("self"),
                            ArgSig("/"),
                            ArgSig("*types", "tuple"),
                            ArgSig("name", "str | None", default=True),
                            ArgSig("arguments", "Optional[List[str]]", default=True),
                        ],
                        ret_type="None",
                    ),
                    # catchall for types
                    FunctionSig(
                        "__init__",
                        [
                            ArgSig("self"),
                            ArgSig("/"),
                            ArgSig("*types", "type"),
                            ArgSig("name", "str | None", default=True),
                            ArgSig("arguments", "Optional[List[str]]", default=True),
                        ],
                        ret_type="None",
                    ),
                ],
                "PySide6.QtCore.SignalInstance.__getitem__": "(self, index) -> SignalInstance[*_SignalTypes]",
                # * Fix `QTreeWidgetItemIterator.__iter__()` to iterate over `QTreeWidgetItemIterator`
                "*.QTreeWidgetItemIterator.__iter__": "(self) -> typing.Iterator[QTreeWidgetItemIterator]",
                "*.QTreeWidgetItemIterator.__next__": "(self) -> QTreeWidgetItemIterator",
                # * Fix `QByteArray(b'foo')[0]` to return `bytes`
                # missing index and return.
                "*.QByteArray.__getitem__": "(self, index: int) -> bytes",
                # * Fix `QByteArray.__iter__()` to iterate over `bytes`
                # * Fix support for `bytes(QByteArray(b'foo'))`
                "*.QByteArray.__bytes__": "(self) -> bytes",
                # * Fix return type for `QApplication.instance()` and `QGuiApplication.instance()` :
                "*.QCoreApplication.instance": "(cls: type[typing_extensions.Self]) -> typing_extensions.Self",
                # FIXME: this can be handled by merging with the default sig
                # signatures for these special methods include many inaccurate overloads
                "*.__ne__": "(self, other: object) -> bool",
                "*.__eq__": "(self, other: object) -> bool",
                "*.__lt__": "(self, other: object) -> bool",
                "*.__gt__": "(self, other: object) -> bool",
                "*.__le__": "(self, other: object) -> bool",
                "*.__ge__": "(self, other: object) -> bool",
                # Slot
                "*.Slot.__call__": "(self, _func: typing.Callable[P, T]) -> typing.Callable[P, T]",
            },
            # Types that have implicit alternatives.
            implicit_arg_types={
                f"{PYSIDE}.QtGui.QKeySequence": ["str"],
                f"{PYSIDE}.QtGui.QColor": [f"{PYSIDE}.QtCore.Qt.GlobalColor", "int"],
                f"{PYSIDE}.QtCore.QByteArray": ["bytes"],
                f"{PYSIDE}.QtGui.QBrush": [
                    f"{PYSIDE}.QtGui.QColor",
                    f"{PYSIDE}.QtCore.Qt.GlobalColor",
                    f"{PYSIDE}.QtGui.QLinearGradient",
                ],
                f"{PYSIDE}.QtGui.QCursor": [f"{PYSIDE}.QtCore.Qt.CursorShape"],
                f"{PYSIDE}.QtCore.QEasingCurve": [f"{PYSIDE}.QtCore.QEasingCurve.Type"],
                f"{PYSIDE}.QtCore.QDate": ["datetime.date"],
                f"{PYSIDE}.QtCore.QDateTime": ["datetime.datetime"],
            },
            # Override argument types
            arg_type_overrides={
                # (method, arg, type)
                ("*", "flags", "int"): "typing.SupportsInt",
                ("*", "weight", "int"): "typing.SupportsInt",
                ("*", "format", "typing.Union[bytes,NoneType]"): "typing.Optional[str]",
                ("*", "role", "int"): f"{PYSIDE}.QtCore.Qt.ItemDataRole",
                ("*.addAction", "*", "object"): "typing.Callable[[], typing.Any]",
                ("*.Slot.__init__", "result", "*"): "type",
                # * Fix arguments that accept `QModelIndex` which were typed as `int` in many places
                # known offenders: QAbstractItemView, QItemSelectionModel, QTreeView, QListView
                (
                    "*.QAbstractItemModel.mimeData",
                    "indexes",
                    "*",
                ): f"list[{PYSIDE}.QtCore.QModelIndex]",
                (
                    "*.QStandardItemModel.mimeData",
                    "indexes",
                    "*",
                ): f"list[{PYSIDE}.QtCore.QModelIndex]",
                (
                    "*.QAbstractItemModel.changePersistentIndexList",
                    "from_",
                    "*",
                ): f"list[{PYSIDE}.QtCore.QModelIndex]",
                (
                    "*.QAbstractItemModel.changePersistentIndexList",
                    "to",
                    "*",
                ): f"list[{PYSIDE}.QtCore.QModelIndex]",
                # * Fix slot arg of `SignalInstance.connect()` to support validating the types of the callable args
                (
                    "PySide6.QtCore.SignalInstance.connect",
                    "slot",
                    "*",
                ): "_SlotFunc[*_SignalTypes]",
                (
                    "PySide6.QtCore.SignalInstance.disconnect",
                    "slot",
                    "*",
                ): "_SlotFunc[*_SignalTypes] | None",
                (
                    "PySide6.QtCore.SignalInstance.emit",
                    "*args",
                    "Any",
                ): "*_SignalTypes",
                #
                (
                    "PySide6.QtCore.QObject.findChild*",
                    "type",
                    "*",
                ): "type[T]",
                # Fix QWidget.setParent to allow passing QObject
                (
                    "*.QtWidgets.QWidget.setParent",
                    "parent",
                    "*",
                ): f"{PYSIDE}.QtCore.QObject | None",
                # Allow int for font weight
                (
                    "*.QFont.setWeight",
                    "weight",
                    "*",
                ): f"int | {PYSIDE}.QtGui.QFont.Weight",
                (
                    "*.QTextEdit.setFontWeight",
                    "w",
                    "*",
                ): f"int | {PYSIDE}.QtGui.QFont.Weight",
            },
            result_type_overrides={
                ("*.toTuple", "object"): "tuple",
                ("*.__iter__", "object"): "typing.Iterator",
                # * Replace `object` with `typing.Any` in return types
                ("*", "object"): "typing.Any",
                # * Fix arguments that accept `QModelIndex` which were typed as `int` in many places
                ("*.selectedIndexes", "*"): f"list[{PYSIDE}.QtCore.QModelIndex]",
                (
                    "*.QItemSelectionModel.selectedColumns",
                    "*",
                ): f"list[{PYSIDE}.QtCore.QModelIndex]",
                (
                    "*.QItemSelectionModel.selectedRows",
                    "*",
                ): f"list[{PYSIDE}.QtCore.QModelIndex]",
                ("*.QItemSelection.indexes", "*"): f"list[{PYSIDE}.QtCore.QModelIndex]",
                (
                    "*.QItemSelectionRange.indexes",
                    "*",
                ): f"list[{PYSIDE}.QtCore.QModelIndex]",
                (
                    "*.QAbstractItemModel.persistentIndexList",
                    "*",
                ): f"list[{PYSIDE}.QtCore.QModelIndex]",
                ("*", "Self"): "typing_extensions.Self",
                (
                    "PySide6.QtCore.QObject.findChild",
                    "*",
                ): "T",  # PySide6-only
                (
                    "PySide6.QtCore.QObject.findChildren",
                    "*",
                ): "list[T]",  # (PySide6-only)
                # * Make result optional
                (
                    "PySide2.QtWidgets.QLayout.itemAt",
                    "*",
                ): f"{PYSIDE}.QtWidgets.QLayoutItem | None",  # (PySide2-only)
                (
                    "*.QtWidgets.QLayout.takeAt",
                    "*",
                ): f"{PYSIDE}.QtWidgets.QLayoutItem | None",  # (PySide2 & PySide6)
                # Fix flags
                (
                    "*.QSortFilterProxyModel.filterRole",
                    "*",
                ): f"{PYSIDE}.QtCore.Qt.ItemDataRole",
                (
                    "*.QStandardItem.type",
                    "*",
                ): f"{PYSIDE}.QtGui.QStandardItem.ItemType",
            },
            # Find and replace argument names
            # arg_name_replacements = {
            #     # (method, arg, type)
            # },
            # Values which should be made Optional[].
            optional_args={
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
                ("*.setModel", "model", "*"): Optionality(
                    accepts_none=True, has_default=False
                ),
                ("*.QLabel.setPixmap", "arg__1", "*"): Optionality(
                    accepts_none=True, has_default=False
                ),
                ("*", "parent", f"{PYSIDE}.QtWidgets.QWidget"): Optionality(
                    accepts_none=True, has_default=False
                ),
                ("*", "parent", f"{PYSIDE}.QtCore.QObject"): Optionality(
                    accepts_none=True, has_default=False
                ),
                ("*.QInputDialog.getText", "echo", "*"): Optionality(
                    accepts_none=False, has_default=True
                ),
            },
            # Add new overloads to existing functions.
            new_overloads={
                # * Add `QSpacerItem.__init__/changeSize` overloads that use alternate names: `hData`->`hPolicy`, `vData`->`vPolicy`
                "*.QSpacerItem.__init__": [
                    f"(self, w:int, h:int, hPolicy:{PYSIDE}.QtWidgets.QSizePolicy.Policy=..., vPolicy:{PYSIDE}.QtWidgets.QSizePolicy.Policy=...) -> None"
                ],
                "*.QSpacerItem.changeSize": [
                    f"(self, w:int, h:int, hPolicy:{PYSIDE}.QtWidgets.QSizePolicy.Policy=..., vPolicy:{PYSIDE}.QtWidgets.QSizePolicy.Policy=...) -> None"
                ],
            },
        )
        if PYSIDE == "PySide2":
            matcher.signature_overrides.update(
                {
                    # * Fix passing QOjbect to QWidget.setParent
                    # (PySide6 fix is in arg_type_overrides)
                    "PySide2.QtWidgets.QWidget.setParent": f"(self, parent: typing.Union[{PYSIDE}.QtCore.QObject,None], f: {PYSIDE}.QtCore.Qt.WindowFlags = ...) -> None",
                    "PySide2.QtCore.Signal.__get__": [
                        "(self, instance: None, owner: type[QObject]) -> Signal",
                        "(self, instance: QObject, owner: type[QObject]) -> SignalInstance",
                    ],
                    "PySide2.QtCore.Signal.__getitem__": "(self, index) -> SignalInstance",
                    "PySide2.QtCore.SignalInstance.__getitem__": "(self, index) -> SignalInstance",
                    # * Fix slot arg of `SignalInstance.connect()` to be `typing.Callable` instead of `object`
                    # * Fix type arg of `SignalInstance.connect()` to be `QtCore.Qt.ConnectionType` instead of `type | None`
                    # (PySide6 fix is in arg_type_overrides)
                    "PySide2.QtCore.SignalInstance.connect": f"(self, slot: typing.Callable, type: {PYSIDE}.QtCore.Qt.ConnectionType = ...) -> bool",
                    "PySide2.QtCore.SignalInstance.disconnect": "(self, slot: typing.Union[typing.Callable,None] = ...) -> None",
                    "PySide2.QtCore.QObject.disconnect": [
                        f"(cls, arg__1: {PYSIDE}.QtCore.QObject, arg__2: str = ..., arg__3: typing.Callable = ...) -> bool",
                        f"(cls, arg__1: {PYSIDE}.QtCore.QMetaObject.Connection) -> bool",
                        f"(cls, sender: {PYSIDE}.QtCore.QObject, signal: {PYSIDE}.QtCore.QMetaMethod, receiver: {PYSIDE}.QtCore.QObject = ..., member: {PYSIDE}.QtCore.QMetaMethod = ...) -> bool",
                    ],
                    # * Fix QPolygon special methods
                    # first and third overloads should return QPolygon
                    "PySide2.QtGui.QPolygon.__lshift__": [
                        f"(self, l: list[{PYSIDE}.QtCore.QPoint]) -> {PYSIDE}.QtGui.QPolygon",
                        f"(self, stream: {PYSIDE}.QtCore.QDataStream) -> {PYSIDE}.QtCore.QDataStream",
                        f"(self, t: {PYSIDE}.QtCore.QPoint) -> {PYSIDE}.QtGui.QPolygon",
                    ],
                    # should return QPolygon
                    # (PySide2-only.  there is not an __iadd__ in PySide6)
                    "PySide2.QtGui.QPolygon.__iadd__": f"(self, t: {PYSIDE}.QtCore.QPoint) -> {PYSIDE}.QtGui.QPolygon",
                    # * Correct numerous annotations from `bytes` to `str`
                    "PySide2.QtCore.QObject.setProperty": "(self, name: str, value: typing.Any) -> bool",
                    "PySide2.QtCore.QObject.property": "(self, name: str) -> typing.Any",
                    "PySide2.QtCore.QState.assignProperty": "(self, object: QObject, name: str, value: typing.Any) -> None",
                    "PySide2.QtCore.QCoreApplication.translate": "(cls, context: str, key: str, disambiguation: typing.Union[str,NoneType] = ..., n: int = ...) -> str",
                    # Fix other flags:
                    "*.QTableWidgetItem.setTextAlignment": f"(self, alignment: {PYSIDE}.QtCore.Qt.Alignment) -> None",
                    "*.QFrame.setFrameStyle": f"(self, arg__1: typing.Union[{PYSIDE}.QtWidgets.QFrame.Shape, {PYSIDE}.QtWidgets.QFrame.Shadow, typing.SupportsInt]) -> None",
                    # in PySide2 these take int, and in PySide6 it takes Weight, but both seem valid
                    # (PySide6 fix is in arg_type_overrides)
                    "*.QFont.setWeight": f"(self, arg__1: typing.Union[int, {PYSIDE}.QtGui.QFont.Weight]) -> None",
                    # ('QFont', 'weight': pyside('(self) -> {PYSIDE}.QtGui.QFont.Weight'),  # fixed in PySide6
                    # * Fix return type for `QObject.findChild()` and `QObject.findChildren()` :
                    "PySide2.QtCore.QObject.findChild": "(self, arg__1: type[T], arg__2: str) -> T",
                    "PySide2.QtCore.QObject.findChildren": [
                        "(self, arg__1: type[T], arg__2: QRegExp) -> list[T]",
                        "(self, arg__1: type[T], arg__2: QRegularExpression) -> list[T]",
                        "(self, arg__1: type[T], arg__2: str = ...) -> list[T]",
                    ],
                    "*.qVersion": "() -> str",
                }
            )
        if helper.pyside_package == "PySide6":
            matcher.arg_type_overrides.update(
                {
                    (
                        "PySide6.QtCore.QSequentialAnimationGroup.__init__",
                        "currentAnimation",
                        "*",
                    ): "PySide6.QtCore.QAbstractAnimation | None",
                    (
                        "PySide6.QtMultimedia.QMediaCaptureSession.__init__",
                        "camera",
                        "*",
                    ): "PySide6.QtMultimedia.QCamera | None",
                }
            )
        return matcher

    # Special methods for flag enums.
    @cached_property
    def flag_overrides(self) -> dict[str, str]:
        return (
            {
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
            if helper.pyside_package == "PySide2"
            else {}
        )

    # FIXME: implement?
    def get_property_type(
        self, default_type: str | None, ctx: FunctionContext
    ) -> str | None:
        return default_type

    def _is_flag_type(self, ctx: FunctionContext) -> bool:
        if ctx.class_info is None:
            return False
        typ = ctx.class_info.cls
        return (
            typ is not None
            and (
                helper.is_flag(typ)
                or helper.is_enum(typ)
                or helper.is_flag_group(typ)
                or helper.is_flag_item_type(typ)
            )
            and ctx.name in self.flag_overrides
        )

    def get_signature_str(
        self, ctx: FunctionContext
    ) -> str | list[str] | list[FunctionSig] | None:
        """
        Provide signature overrides for PySide2 flag item special methods
        """
        if helper.pyside_package == "PySide2" and self._is_flag_type(ctx):
            assert ctx.class_info is not None
            typ = ctx.class_info.cls
            docstr_override = self.flag_overrides[ctx.name]
            if helper.is_flag_item_type(typ):
                return_type = helper.get_group_from_flag_item(typ)
            elif typ is not None:
                return_type = typ
            else:
                return None
            return docstr_override.format(get_type_fullname(return_type))
        else:
            return super().get_signature_str(ctx)

    def process_arg(self, ctx: FunctionContext, arg: ArgSig) -> None:
        """Update ArgSig in place"""

        if not arg.type:
            return

        arg_type = arg.type.replace(" ", "")
        arg_type = re.sub(
            r"\b(?:typing|collections[.]abc)\.Sequence\b", "typing.Iterable", arg_type
        )
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
            new_type = helper.get_flag_union(arg.type)
            if new_type is not None:
                arg.type = new_type

    def process_sig(self, ctx: FunctionContext, sig: FunctionSig) -> FunctionSig:
        sig = super().process_sig(ctx, sig)

        new_type = helper.get_flag_union(sig.ret_type)
        if new_type is not None:
            return sig._replace(ret_type=new_type)
        if ctx.name == "__init__" and sig.ret_type != "None":
            return sig._replace(ret_type="None")
        return sig

    def process_sigs(
        self, ctx: FunctionContext, results: list[FunctionSig]
    ) -> list[FunctionSig]:
        if self._is_flag_type(ctx):
            return results

        if (
            ctx.class_info is not None
            and ctx.class_info.cls is not None
            and ctx.name == "__init__"
        ):
            helper.add_property_args(ctx.class_info.cls, results)

        # use the type of results, it may be of type Overridden
        new_sigs = type(results)()
        # remove duplicates: FunctionSig is not hashable!
        for sig in results:
            if sig not in new_sigs:
                new_sigs.append(sig)
        return super().process_sigs(ctx, new_sigs)

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        if ctx.docstring:
            # some PySide sigs have type vars with ~ in their name. Remove it so that it can
            # be successfully parsed.
            ctx.docstring = ctx.docstring.replace("~", "")
        return super().get_function_sig(default_sig, ctx)


class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    OVERLOAD_TEMPLATE = '''\
class {overload_class_name}:
    """
    Overloads for {class_name}.{method_name}.

    This descriptor-based workflow allows us to describe overloads that mix static and instance
    methods. 
    """
    class StaticOverloads:
        class {method_name}:
{static_body}

    class InstanceOverloads:
        class {method_name}:
{instance_body}

    def __init__(self, cb: typing.Callable) -> None: ...

    @typing.overload
    def __get__(self, object: None, owner: typing.Any) -> StaticOverloads.{method_name}: ...

    @typing.overload
    def __get__(self, object: {class_name}, owner: typing.Any) -> InstanceOverloads.{method_name}: ...\n\n'''

    _seen: set[type] = set()
    _pyside_sig_generator: PySideSignatureGenerator | None = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if not self.__class__._seen:
            for known_module_name in self.known_modules:
                print(f"Importing {known_module_name}")
                try:
                    module = importlib.import_module(known_module_name)
                except ModuleNotFoundError:
                    print(f"Module could not be imported: {known_module_name}")
                else:
                    self.walk_objects(module, self.__class__._seen)
        self.current_function_context: FunctionContext | None = None
        self.custom_overloads: list[str] = []

    def walk_objects(self, obj: object, seen: set[type]) -> None:
        for child_name, child in self.get_members(obj):
            if isinstance(child, type):
                if child in seen:
                    continue
                seen.add(child)
                docstring = getattr(child, "__doc__", None)
                if docstring is not None and not isinstance(docstring, str):
                    print(f"Bad docstring: {child}")
                    child.__doc__ = ""

                # populate caches
                if helper.pyside_package == "PySide2" and helper.is_flag(child):
                    helper.get_group_from_flag_item(child)
                elif (
                    helper.is_enum(child)
                    or helper.is_flag(child)
                    or helper.is_flag_group(child)
                ):
                    helper.record_flag(child)

                self.walk_objects(child, seen)

            elif helper.pyside_package == "PySide6" and isinstance(
                child, helper.QtCore.Signal
            ):
                assert isinstance(obj, type)
                helper.record_signal(obj, child_name, child)

    @classmethod
    def get_pyside_sig_generator(cls) -> PySideSignatureGenerator:
        # InspectionStubGenerator is instantiated for every module processed, but we want to
        # reuse a single PySideSignatureGenerator so that it can generate usage reports, so
        # we store it at the class level.
        if cls._pyside_sig_generator is None:
            # re-use the generator so that we can generate match reports for all classes
            cls._pyside_sig_generator = PySideSignatureGenerator(strict=False)
            # atexit.register(cls._pyside_sig_generator.print_info)
        return cls._pyside_sig_generator

    def get_sig_generators(self) -> list[SignatureGenerator]:
        sig_generators = super().get_sig_generators()
        sig_generators.insert(0, self.get_pyside_sig_generator())
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
        if "*" in type_name:
            # variadic type vars can't be parsed by parse_type_comment()
            return type_name
        type_name = type_name.replace("Shiboken.", f"{helper.shiboken_package}.")
        stripped_type = super().strip_or_import(type_name)
        return stripped_type

    def _get_members_base(self, obj: object) -> list[tuple[str, Any]]:
        if isinstance(obj, types.ModuleType) and getattr(obj, "__name__", None) not in [
            "PySide6.QtNfc"
        ]:
            # It's unclear why (possibly related to collecting modules via subprocesses) but
            # when we collect members there are many modules which have a nearly empty __dict__
            # so we use `dir` which is reliable.
            # we don't want to use dir on classes, because it collects inherited members.
            obj_dict = dir(obj)
        else:
            obj_dict = list(getattr(obj, "__dict__"))  # noqa: B009

        results = []
        for name in sorted(obj_dict):
            if self.is_skipped_attribute(name):
                continue
            # Try to get the value via getattr
            try:
                value = getattr(obj, name)
            except AttributeError:
                continue
            else:
                if (
                    isinstance(obj, types.ModuleType)
                    and hasattr(value, "__module__")
                    and (
                        value.__module__ != obj.__name__
                        or "." in getattr(value, "__qualname__", "")
                    )
                ):
                    # if the object that we're collecting members from is a module, and the
                    # member is defined in another module, OR the class is a nested class that
                    # somehow found its way into the module namespace then skip it.
                    # The latter case happened with the move to PySide6 (see
                    # QtCore.QDirListing.DirEntry)
                    continue
                results.append((name, value))
        return results

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        if helper.pyside_package == "PySide6":
            members = self._get_members_base(obj)
        else:
            members = super().get_members(obj)
        members = [
            x for x in members if not self._is_skipped_pyside_attribute(x[0], x[1])
        ]
        if isinstance(obj, type):
            return members + helper.new_members.get(obj.__name__, [])
        return members

    def get_imports(self) -> str:
        imports = super().get_imports()

        boilerplate = """\
T = typing.TypeVar('T')
P = typing.ParamSpec('P')\n"""

        if self.module_name == "PySide6.QtCore":
            boilerplate += """
_T1 = typing.TypeVar('_T1')
_T2 = typing.TypeVar('_T2')
_T3 = typing.TypeVar('_T3')
_T4 = typing.TypeVar('_T4')
_SignalTypes = typing.TypeVarTuple('_SignalTypes')

class _SlotFunc(typing.Protocol[*_SignalTypes]):
    def __call__(self, *args: *_SignalTypes) -> typing.Any:
        pass\n\n"""

        if helper.pyside_package == "PySide6":
            # something changed that makes this required now.  could be new behavior of stubgen.
            boilerplate = (
                "from typing import Any, Dict, List, Optional, OrderedDict, Set, Tuple, Union\n"
                + boilerplate
            )

        for custom_overload in self.custom_overloads:
            boilerplate += custom_overload

        return insert_typevars(imports, boilerplate.splitlines(keepends=False))

    def output(self) -> str:
        output = super().output()
        if helper.pyside_package == "PySide6":
            shiboken_module = f"{helper.shiboken_package}.Shiboken"
        else:
            shiboken_module = f"{helper.shiboken_package}.{helper.shiboken_package}"
        if self.module_name == shiboken_module:
            output += "\nclass Object: ...\n"
        return output

    def get_default_function_sig(
        self, func: object, ctx: FunctionContext
    ) -> FunctionSig:
        # set the ctx so that it's available in format_func_def.
        self.current_function_context = ctx
        return super().get_default_function_sig(func, ctx)

    def format_func_def(
        self,
        sigs: list[FunctionSig],
        is_coroutine: bool = False,
        decorators: list[str] | None = None,
        docstring: str | None = None,
    ) -> list[str]:
        """
        Handle methods that can be used as both static methods and instance methods.
        """
        lines: list[str] = []
        staticmethods = []
        instancemethods = []
        for sig in sigs:
            if sig.args and sig.args[0].name == "self":
                instancemethods.append(sig)
            else:
                staticmethods.append(sig)

        if staticmethods and instancemethods:
            # mypy does not support overloads that mix class/static methods and instance methods.
            assert self.current_function_context is not None
            assert self.current_function_context.class_info is not None
            method_name = self.current_function_context.name
            class_name = self.current_function_context.class_info.name

            staticmethods = [sig._replace(name="__call__") for sig in staticmethods]
            static_body = super().format_func_def(
                staticmethods,
                decorators=["@staticmethod"]
                + (["@typing.overload"] if len(staticmethods) > 1 else []),
            )

            instancemethods = [sig._replace(name="__call__") for sig in instancemethods]
            # add static methods to instance methods, because they can also be called from an
            # instance:
            instancemethods += [
                sig._replace(name="__call__", args=[ArgSig("self")] + sig.args)
                for sig in staticmethods
            ]
            instance_body = super().format_func_def(
                instancemethods,
                decorators=["@typing.overload"] if len(instancemethods) > 1 else [],
            )

            overload_class_name = f"_add_{class_name}_{method_name}_overloads"
            self.custom_overloads.append(
                self.OVERLOAD_TEMPLATE.format(
                    class_name=class_name,
                    overload_class_name=overload_class_name,
                    method_name=method_name,
                    static_body="\n".join(" " * 8 + x for x in static_body),
                    instance_body="\n".join(" " * 8 + x for x in instance_body),
                )
            )

            methods = [
                FunctionSig(
                    name=method_name, args=[ArgSig("self")], ret_type="typing.Any"
                )
            ]
            decorators = [f"@{overload_class_name}"]
        else:
            if staticmethods:
                methods = staticmethods
            else:
                methods = instancemethods

            methods = remove_overlapping_overloads(
                methods, sort=not isinstance(sigs, Overridden)
            )

            # quick and dirty fix
            if (
                len(methods) == 1
                and decorators == ["@staticmethod"]
                and methods[0].args
                and methods[0].args[0].name == "cls"
            ):
                decorators = ["@classmethod"]

        # quick and dirty fix
        if (
            len(methods) == 1
            and decorators == ["@staticmethod"]
            and methods[0].args
            and methods[0].args[0].name == "cls"
        ):
            decorators = ["@classmethod"]

        lines += super().format_func_def(methods, is_coroutine, decorators, docstring)

        return lines

    def get_base_types(self, obj: type) -> list[str]:
        if self.module_name == "PySide6.QtCore" and obj.__name__ in [
            "Signal",
            "SignalInstance",
        ]:
            return ["typing.Generic[*_SignalTypes]"]
        return super().get_base_types(obj)

    def generate_class_attr(self, cls: type, attr: str, value: object) -> str | None:
        signal_types = (
            helper.get_signal(cls, attr) if helper.pyside_package == "PySide6" else None
        )
        if signal_types is not None:
            prop_type_name = self.strip_or_import(self.get_type_annotation(value))
            signal_types_str = ", ".join(signal_types) if signal_types else "()"
            classvar = self.add_name("typing.ClassVar")
            return f"{self._indent}{attr}: {classvar}[{prop_type_name}[{signal_types_str}]] = ..."
        else:
            return super().generate_class_attr(cls, attr, value)


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[attr-defined]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]

helper = PySideHelper()


if __name__ == "__main__":
    dump_mappings = False
    helper.set_pyside_version(2)

    # in order to create and inspect object properties we must create an app
    app = helper.QtWidgets.QApplication()

    # from stubgenlib.moduleinspect import patch
    #
    # # I don't think this works because mypy is compiled
    # patch()

    # in PySide2 there are 5 types of enums (these terms are not official)
    # - flag:       holder of flag items.                                  PySide2.QtCore.QDir.Filter
    # - flag item:  a specific flag.  can be combined with other flags.    PySide2.QtCore.QDir.Filter.AllDirs
    # - enum:       holder of enum itmes                                   PySide2.QtCore.QLocale.Language
    # - enum item:  a specific enum.  cannot be combined with other enums  PySide2.QtCore.QLocale.Language.Abkhazian
    # - flag group: the result of combining flag items                     PySide2.QtCore.QDir.Filters

    # Issues / concerns / observations
    # - what we call a flag is more accurately an enum.
    # - we appear to conflate flag items and flags, because we identify flag items by their type,
    #   and the type of a flag item is a flag.
    # - we implemented PySide6 support without changing the generated output from Pyside2, which
    #   means that these discrepancies are a problem of terminology, and especially how this differs
    #   between PySide2 and PySide6
    # - is_flag_item_type is only ever called in PySide2 context or alongside a checks for all enum varieties types (_is_flag_type)
    # - is_flag_item_type operates on the type instead of the instance because that's what's available on the ctx.

    mypy.stubgen.main(
        [
            f"-p={helper.shiboken_package}",
            f"-p={helper.pyside_package}",
            "--include-private",
            "-o=stubs",
        ]
    )

    helper.add_version_info()

    if dump_mappings:
        import pprint

        from PySide2.QtCore import Qt

        print()
        flags = defaultdict(set)
        for name, member in inspect.getmembers(Qt):
            if isinstance(member, type) and (
                helper.is_flag(member) or helper.is_flag_item_type(member)
            ):
                flag_name = name
                for child_name in dir(member):
                    child = getattr(member, child_name)
                    if helper.is_flag(type(child)) or helper.is_flag_item_type(
                        type(child)
                    ):
                        flags[child_name].add(flag_name)

        mapping = {}
        for name, member in inspect.getmembers(Qt):
            if helper.is_flag(type(member)) or helper.is_flag_item_type(type(member)):
                matches = list(flags[name])
                if len(matches) > 1:
                    raise RuntimeError(f"{name} has more than one match: {matches}")
                mapping[f"PySide2.QtCore.Qt.{name}"] = (
                    f"PySide2.QtCore.Qt.{matches[0]}.{name}"
                )

        with open("../pyside6/enum-mappings.json", "w") as f:
            json.dump(mapping, f)

        pprint.pprint(mapping)

    # InspectionStubGenerator._pyside_sig_generator.print_info()
