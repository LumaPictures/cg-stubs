from __future__ import absolute_import, annotations, division, print_function

import inspect
import subprocess
import os
import pathlib
import re
import pydoc
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, NamedTuple
from functools import lru_cache

import mypy.stubgen
import mypy.stubgenc
import mypy.stubutil
from mypy.stubdoc import ArgSig, FunctionSig, infer_sig_from_docstring
from mypy.stubgen import main as stubgen_main
from mypy.stubgenc import (
    FunctionContext,
    SignatureGenerator,
    ClassInfo,
    infer_c_method_args,
)
from mypy.stubutil import infer_method_ret_type

# this doesn't work with mypy downloaded from pypi because it's been compiled.
# produces "TypeError: tuple[] object expected; got tuple[str, str]"
# mypy.stubutil.NOT_IMPORTABLE_MODULES = (
#     "pxr.Tf.testenv",  # type: ignore[assignment]
#     "pxr.Tf.testenv.testTfScriptModuleLoader_AAA_RaisesError",
# )

from doxygenlib.cdParser import Parser, XMLNode  # type: ignore[import]
from doxygenlib.cdDocElement import DocElement  # type: ignore[import]
from doxygenlib.cdUtils import SetDebugMode  # type: ignore[import]

from stubgenlib import (
    BaseSigFixer,
    BoostDocstringSignatureGenerator,
    CFunctionStub,
    Notifier,
    CppTypeConverter,
    reduce_overloads,
    sig_sort_key,
)

SetDebugMode(False)

# FIXME: there's a python func for this
# a python identifier
PYPATH = r"((?:[a-zA-Z_][a-zA-Z0-9_]*)(?:[.][a-zA-Z_][a-zA-Z0-9_]*)*)"


class CppPath(NamedTuple):
    cpp_dest: str
    py_source: str
    path: str


def is_existing_obj(pypath: str) -> bool:
    try:
        return pydoc.locate(pypath) is not None
    except AttributeError:
        return False


def get_submodules(pacakge_paths: list[str]) -> list[str]:
    """
    Given the name of a python mdoule, get a list of names of its child modules
    """
    import pkgutil

    return [loader.name for loader in pkgutil.iter_modules(pacakge_paths)]


def capitalize(s: str) -> str:
    return s[0].upper() + s[1:]


# def get_fullpath(obj: object) -> str | None:
#     name = getattr(obj, "__qualname__", getattr(obj, "__name__", None))
#     if name is None:
#         return None
#     module_name = getattr(obj, "__module__", None)
#     if module_name:
#         name = "{}.{}".format(module_name, name)
#     return name


class DummyWriter:
    def getDocString(self, node: XMLNode) -> str:
        return ""

    def getDocTags(self, node: XMLNode) -> list[str]:
        return []

    def generate(self, output_file: str, docElements: list[DocElement]) -> None:
        raise NotImplementedError


@dataclass
class CppSigInfo:
    parent: DocElement
    overloads: list[DocElement]


def maybe_result(parts: list[str]) -> bool:
    """
    return if the argument looks like a c++ result
    """
    return "const" not in parts and ("*" in parts or "&" in parts)


class TypeInfo(CppTypeConverter):
    """Get info about types.

    Provides helpers for converting c++ data to python data, using data
    parsed from doxygen docs and source code.
    """

    # FIXME: this appears to no longer be used, but the idea of parsing the type_defs
    #  be easier to maintain
    # TYPE_DEF_INCLUDES = [
    #     "pxr/usd/sdf/types.h",
    #     "pxr/usd/sdf/path.h",
    #     "pxr/usd/sdf/fileFormat.h",
    #     # "pxr/usd/sdf/proxyTypes.h",
    #     "pxr/usd/ndr/declare.h",
    #     "pxr/usd/usdGeom/basisCurves.h",
    # ]
    ARG_TYPE_MAP = CppTypeConverter.ARG_TYPE_MAP + [
        # Sdf mapping types:
        (r"\bSdfLayerHandleSet\b", "typing.Iterable[pxr.Sdf.Layer]"),
        # (r"\bSdfPathSet\b", "typing.Iterable[pxr.Sdf.Path]"),
    ]
    RESULT_TYPE_MAP = CppTypeConverter.RESULT_TYPE_MAP + [
        # Sdf mapping types:
        (r"\bSdfLayerHandleSet\b", "list[pxr.Sdf.Layer]"),
        # (r"\bSdfPathSet\b", "list[pxr.Sdf.Path]"),
    ]
    TYPE_MAP = CppTypeConverter.TYPE_MAP + [
        (r"\bstd::optional\b", "typing.Optional"),
        (r"\bVtArray<\s*SdfAssetPath\s*>", "SdfAssetPathArray"),
        (r"\bint64_t\b", "int"),
        (r"\bUsdSchemaVersion\b", "int"),
        (r"\bGfHalf\b", "float"),
        (r"\bHalf\b", "float"),
        (r"\bboost::python::", ""),
        (r"\bVtValue\b", "Any"),
        # this gets a lot of things right, but does produce a few errors, like list[Error] for PcpErrorVector, instead of list[ErrorBase]
        (r"\b" + CppTypeConverter.IDENTIFIER + r"Vector\b", r"list[\1]"),
        (r"\bTfToken\b", "str"),
        (r"\bVtDictionary\b", "dict"),
        (r"\bUsdMetadataValueMap\b", "dict"),
        # strip suffixes
        (r"RefPtr\b", ""),
        (r"Ptr\b", ""),
        (r"ConstHandle\b", ""),
        (r"Const\b", ""),
        (r"Handle\b", ""),
    ]
    RENAMES = [
        # simple renames:
        (r"\bSdfBatchNamespaceEdit\b", "pxr.Sdf.NamespaceEdit"),
        # Sdf mapping types:
        (r"\bSdfDictionaryProxy\b", "pxr.Sdf.MapEditProxy_VtDictionary"),  # typedef
        (r"\bSdfReferencesProxy\b", "pxr.Sdf.ReferenceTypePolicy"),  # typedef
        (r"\bSdfSubLayerProxy\b", "pxr.Sdf.ListProxy_SdfSubLayerTypePolicy"),  # typedef
        # pathKey
        (
            r"\bSdfInheritsProxy\b",
            "pxr.Sdf.ListEditorProxy_SdfPathKeyPolicy",
        ),  # typedef
        (
            r"\bSdfSpecializesProxy\b",
            "pxr.Sdf.ListEditorProxy_SdfPathKeyPolicy",
        ),  # typedef
        # nameTokenKey
        (
            r"\bSdfNameOrderProxy\b",
            "pxr.Sdf.ListProxy_SdfNameTokenKeyPolicy",
        ),  # typedef
        (
            r"\bSdfNameChildrenOrderProxy\b",
            "pxr.Sdf.ListProxy_SdfNameTokenKeyPolicy",
        ),  # typedef
        (
            r"\bSdfPropertyOrderProxy\b",
            "pxr.Sdf.ListProxy_SdfNameTokenKeyPolicy",
        ),  # typedef
        # nameKey
        (
            r"\bSdfVariantSetNamesProxy\b",
            "pxr.Sdf.ListEditorProxy_SdfNameKeyPolicy",
        ),  # typedef
    ]
    ARRAY_TYPES = {
        "Bool": "bool",
        "Char": "str",
        "Double": "float",
        "Float": "float",
        "Half": "float",
        "Int64": "int",
        "Int": "int",
        "Short": "int",
        "String": "str",
        "UChar": "str",
        "UInt64": "int",
        "UInt": "int",
        "UShort": "int",
        "Token": "str",
    }
    # mapping from c++ operators to python special methods
    OPERATORS = {
        "__neq__": "operator!=",
        "__eq__": "operator==",
        "__lt__": "operator<",
        "__le__": "operator<=",
        "__gt__": "operator>",
        "__ge__": "operator>=",
        "__bool__": "operator bool",
        "__getitem__": "operator[]",
        "__call__": "operator()",
    }
    # even though Usd_PrimFlagsPredicate is mentinoned in the docs it is not in the
    # index, so it is not found by the parser.
    # FIXME: instead of relying on the docs to popluate the py_types dict, we could
    #  simply pre-cache the contents of the python modules.
    MISSING_PY_TYPES = {
        "_PrimFlagsPredicate": ["pxr.Usd._PrimFlagsPredicate"],
        "StringListOp": ["pxr.Sdf.StringListOp"],
        "AssetPathArray": ["pxr.Sdf.AssetPathArray"],
    }

    def __init__(
        self,
        xml_index_file: str,
        pxr_modules: list[str],
        srcdir: str | None = None,
        verbose: bool = False,
    ) -> None:
        self.xml_index_file = xml_index_file
        self.pxr_modules_names = sorted(pxr_modules, key=len, reverse=True)
        self.cpp_sigs: dict[str, CppSigInfo] = {}
        # mapping of short names to full python paths
        self.py_types: defaultdict[str, list[str]] = defaultdict(list)
        self._valid_modules = None
        self._implicitly_convertible_types: dict[str, set[str]] | None = None
        super().__init__(srcdir=srcdir, verbose=verbose)

    # def get_valid_modules(self):
    #     """
    #     get a cached list of modules from the source
    #     """
    #     if self._valid_modules is None:
    #         import pkgutil
    #         macro_dir = os.path.join(self.srcdir, 'cmake/macros')
    #         if not os.path.exists(macro_dir):
    #             raise RuntimeError("Cannot find cmake macro directory: %s" % macro_dir)
    #         sys.path.append(macro_dir)
    #         import pxr
    #         self._valid_modules = sorted(
    #             get_submodules(pxr.__path__),
    #             reverse=True)
    #     return self._valid_modules

    @classmethod
    def py_array_to_sub_type(cls, py_type: str) -> str | None:
        """Takes a short or full python path"""
        m = re.search(
            r"\b((Int|UInt|Bool|Vec|Short|Double|Half|Quat|Range|Rect|Char|Float|Token|Matrix).*)Array$",
            py_type,
        )
        if m:
            sub_type = m.groups()[0]
            return cls.ARRAY_TYPES.get(sub_type, f"pxr.Gf.{sub_type}")
        return None

    @classmethod
    def is_py_array_type(cls, py_type: str) -> bool:
        """Takes a short or full python path"""
        return bool(cls.py_array_to_sub_type(py_type))

    def _get_implicitly_convertible_types(self) -> dict[str, set[str]]:
        """
        inspect the boost-python code to parse the rules for implicitly
        convertible types
        """
        if self.srcdir is None:
            raise RuntimeError(
                "Skipping implicitly convertible types: No source dir provided"
            )

        def get_type_from_path(path: str) -> str:
            parts = path.split(os.path.sep)
            name = os.path.splitext(parts[-1])[0]
            assert name.startswith("wrap")
            return self.to_python_id(capitalize(parts[-2]) + name[4:])

        def process_parsed_type(cpp_type: str) -> str:
            if cpp_type == "This":
                cpp_type = get_type_from_path(path)
            py_type = self.cpp_arg_to_py_type(cpp_type, is_result=True)
            return self.get_full_py_type(py_type) or py_type

        # FIXME: add module prefixes to all types (Output, Input, Parameter, etc are not prefixed)
        # FIXME: parse other conversions defined using TfPyContainerConversions
        if self._implicitly_convertible_types is None:
            output = subprocess.check_output(
                [
                    "grep",
                    "implicitly_convertible",
                    "-r",
                    os.path.join(self.srcdir, "pxr"),
                    "--include=wrap*.cpp",
                ],
                text=True,
            )
            code_reg = re.compile(
                r"\s+implicitly_convertible<\s*(?P<from>(%s|:)+),\s*(?P<to>(%s|:)+)\s*>\(\)"
                % (self.IDENTIFIER, self.IDENTIFIER)
            )
            result = defaultdict(set)
            for line in output.split("\n"):
                line = line.strip()
                if line:
                    path, code = line.split(":", 1)
                    if ".template." in path:
                        # skip jinja templates
                        continue
                    # each line looks like:
                    # 'src/pxr/base/lib/gf/wrapQuatd.cpp:    implicitly_convertible<GfQuatf, GfQuatd>();'
                    m = code_reg.search(code)
                    if m:
                        match = m.groupdict()
                        from_type = process_parsed_type(match["from"])
                        to_type = process_parsed_type(match["to"])
                        result[to_type].add(from_type)
                    elif self.verbose:
                        print("no match", line)

            # data types: vec, matrix, etc
            import pxr.Gf  # type: ignore[import]

            for name, obj in inspect.getmembers(pxr.Gf):
                dimension = getattr(obj, "dimension", None)
                if dimension:
                    if name.endswith("i"):
                        data_type = "int"
                    else:
                        data_type = "float"
                    if isinstance(dimension, int) and dimension > 1:
                        result[f"pxr.Gf.{name}"].add(
                            "tuple[{}]".format(", ".join([data_type] * dimension))
                        )
                        result[f"pxr.Gf.{name}"].add(f"list[{data_type}]")

            # array types
            import pxr.Vt  # type: ignore[import]

            for name, obj in inspect.getmembers(pxr.Vt):
                sub_type = self.py_array_to_sub_type(name)
                if sub_type:
                    result[f"pxr.Vt.{name}"].add(f"typing.Iterable[{sub_type}]")

            self._implicitly_convertible_types = dict(result)

        if not self._implicitly_convertible_types:
            raise RuntimeError("Could not find implicitly convertible types")
        return self._implicitly_convertible_types

    def _populate_map(self, docElemPath: list[DocElement]) -> None:
        """
        docElemPath : list of DocElements from the root to the documented item
        """
        docElem = docElemPath[-1]

        cpp_path = "::".join(d.name for d in docElemPath[1:])
        if docElem.isClass() or docElem.isEnum():
            cpp_path = "::".join(d.name for d in docElemPath[1:])
            py_type = self.cpp_to_py_type(cpp_path)
            if py_type is not None:
                # short to long
                short_name = py_type.split(".")[-1]
                if is_existing_obj(py_type):
                    self.py_types[short_name].append(py_type)

        for childName, childObjectList in docElem.children.items():
            childElem = childObjectList[0]
            if childElem.isFunction():
                info = CppSigInfo(
                    parent=docElem,
                    overloads=childObjectList,
                )
                assert len(docElemPath) in (1, 2), childElem
                parents = docElemPath[1:]
                cppPath = "::".join(x.name for x in parents + [childElem])
                self.cpp_sigs[cppPath] = info

            # recurse through all of this element's children
            for child in childObjectList:
                self._populate_map(docElemPath + [child])

    def populate(self) -> None:
        parser = Parser()
        parser.parseDoxygenIndexFile(self.xml_index_file)
        doc_elements = parser.traverse(DummyWriter())

        for doc_element in doc_elements:
            self._populate_map([doc_element])

        self.py_types.update(self.MISSING_PY_TYPES)

        # cache these:
        self._get_implicitly_convertible_types()

    @staticmethod
    def strip_pxr_namespace(cpp_type_name: str) -> str:
        if cpp_type_name.startswith("pxr::"):
            cpp_type_name = cpp_type_name[len("pxr::") :]
        return cpp_type_name

    def cpp_to_py_type(self, cpp_type_name: str) -> str | None:
        """
        Convert from cpp object path to python object path.

        pxr::SdfPath -> pxr.Sdf.Path
        SdfPath      -> pxr.Sdf.Path
        """
        cpp_type_name = self.strip_pxr_namespace(cpp_type_name)
        for mod in self.pxr_modules_names:
            if cpp_type_name.startswith(mod):
                parts = cpp_type_name[len(mod) :].split("::")
                parts = ["pxr", mod] + parts
                return ".".join(parts)
        return None

    def split_module(self, cpp_type: str) -> list[str]:
        """
        split the c++ type into module name and object name
        """
        for mod in self.pxr_modules_names:
            if cpp_type.startswith(mod):
                s = cpp_type[len(mod) :]
                if s and (s[0].isupper() or s[0] == "_"):
                    return [mod, s]
        return [cpp_type]

    # FIXME: reconcile this with cpp_to_py_type
    def to_python_id(self, cpp_type: str) -> str:
        cpp_type = self.strip_pxr_namespace(cpp_type)
        parts = self.split_module(cpp_type)
        if len(parts) == 1:
            return parts[0]
        else:
            mod = parts[0]
            name = parts[1]
            return f"pxr.{mod}.{name}"

    def should_strip_part(self, x: str) -> bool:
        """
        whether the part looks like a c++ keyword
        """
        return x.endswith("_API") or not x

    @classmethod
    @lru_cache
    def py_to_cpp_func_paths(cls, pypath: str) -> list[CppPath]:
        """
        Convert from python object path to cpp object path

        Returns a list of potential cpp object paths.
        """
        parts = pypath.split(".")
        module = parts[1]
        # pxr.Sdf.Path.FindLongestPrefix -> [
        #   SdfPath::FindLongestPrefix
        #   SdfPathFindLongestPrefix
        # ]
        remainder = parts[2:]
        if len(remainder) >= 2:
            # pxr.Mod.Class.Func = method or property
            func = remainder[-1]
            root_class = f"{module}{remainder[0]}"
            classes = [root_class] + remainder[1:-1]
            prefix = "::".join(classes)
            if func[0].islower():
                # property
                # TODO: special cases:
                #   cpp -> CPP
                #   String -> Token
                if func.startswith("is"):
                    func = capitalize(func)
                else:
                    func = "Get" + capitalize(func)
                results = [
                    # cpp->py
                    CppPath("method", "property", f"{prefix}::{func}"),
                ]
            elif func == "__init__":
                constructor = classes[-1]
                results = [
                    # cpp->py
                    CppPath("method", "method", f"{prefix}::{constructor}"),
                ]
            else:
                # method
                func = cls.OPERATORS.get(func, func)
                results = [
                    # cpp->py
                    CppPath("method", "method", f"{prefix}::{func}"),
                    CppPath("func", "staticmethod", f"{prefix}{func}"),
                ]
        elif len(remainder) == 1:
            # pxr.Mod.Func = function
            func = remainder[0]
            results = [
                # py-cpp
                CppPath("func", "func", f"{module}{func}"),
            ]
        else:
            # notifier.warn("Unexpected number of parts", "%s" % pypath)
            results = []
        return results

    def format_cpp_sig(self, doc_elem: DocElement) -> str:
        params = ", ".join([f"{p[1]}: {p[0]}" for p in doc_elem.params])
        return f"def {doc_elem.name}({params}) -> {doc_elem.returnType}: ..."

    def _get_cpp_sig_info(self, cpp_paths: list[CppPath]) -> CppSigInfo | None:
        """
        Given a list of possible C++ object paths, return the first matching
        C++ Signature
        """
        for _, _, cpp_path in cpp_paths:
            try:
                data = self.cpp_sigs[cpp_path]
            except KeyError:
                pass
            else:
                return data
        return None

    @lru_cache
    def get_full_py_type(
        self,
        short_type_name: str,
        current_module: str | None = None,
        fallback: str | None = None,
        current_func: str | None = None,
    ) -> str | None:
        """Get a full python object path from a short type name.

        Returns None if the type was not found.
        """
        full_type_names = self.py_types.get(short_type_name)
        if not full_type_names:
            # Note: bool, int, list, etc end up here.
            return None  # fallback if fallback is not None else None
        if len(full_type_names) == 1:
            return full_type_names[0]

        if fallback is not None and fallback in full_type_names:
            return fallback

        if short_type_name == "Type":
            return "pxr.Tf.Type"
        elif short_type_name == "TimeCode" and current_module:
            if current_module == "pxr.Sdf":
                return "pxr.Sdf.TimeCode"
            elif current_module.startswith("pxr.Usd"):
                for full_type in full_type_names:
                    if full_type.startswith("pxr.Usd."):
                        return full_type

        if current_func and current_module:
            # get a list of all types from our cpp info. if exactly one of our
            # full_type_names is in that list, then it's the one to use.

            # FIXME: there is a lot of redundant processing here.
            cpp_overloads, is_static = get_filtered_cpp_overloads(
                current_module, current_func
            )
            if cpp_overloads:
                sigs = get_sigs_from_cpp_overloads(
                    mypy.stubutil.FunctionContext(
                        current_module, current_func.rsplit(".")[-1]
                    ),
                    cpp_overloads,
                )
                all_types = set()
                for sig in sigs:
                    for arg in sig.args:
                        if arg.type:
                            all_types.add(arg.type)
                found = all_types.intersection(full_type_names)

                if len(found) == 1:
                    return list(found)[0]

        if current_module:
            # if all else fails, try to find a type in the current module
            for full_type in full_type_names:
                if full_type.startswith(current_module + "."):
                    return full_type

        if current_func is None:
            current_func = "<unknown_func>"
        if current_module is None:
            current_module = "<unknown_module>"

        notifier.warn(
            "Ambiguous type loookup",
            current_module,
            f"{current_func}: {short_type_name!r} -> {full_type_names} (fallback={fallback!r})",
        )
        return None


import pxr

modules = get_submodules(pxr.__path__)

notifier = Notifier()

type_info = TypeInfo(
    os.environ["USD_XML_INDEX"], modules, srcdir=os.environ["USD_SOURCE_ROOT"]
)

# Notes
# - python args do not always match cpp args
# - many classes (Sdf.Spec, Sdf.VariantSpec, Sdf.Path) add a self arg to methods.
#   I have a good heuristic to determine which are self-args
# - some arguments are pointer results. in most cases we can safely assume that these will be added
#   as tuple results, but there are a few exceptions
#       pxr.Sdf.Layer.CanApply: the tuple result is conditional on the main return result
#       pxr.Sdf.PrimSpec.CanSetName: ptr result is ignored
#       pxr.Sdf.Path.GetAllTargetPathsRecursively: ptr is the main result
#       pxr.Sdf.Path.IsValidPathString: returns a tuple-like Sdf_PathIsValidPathStringResult
# - only a few methods seem to properly handle std::string
# - it seems that free functions are not collected by the pixar parser. some of these are added as static
#   methods to python classes: e.g. SdfPathFindLongestPrefix -> Path.FindLongestPrefix
# - it's apparent that the order of overloads differs between boost and doxygen for at least some functions:
#   pxr.Sdf.CopySpec, pxr.Usd.TraverseInstanceProxies.  FIXED (mostly)
# - Matrix3dArray and other math types in Vt don't seem to be in the docs
# - some wrapped c++ functions don't turn pointers into return types, such as UsdSkelExpandConstantInfluencesToVarying
# - the stubs for Sdf.ValueTypeNames can be improved with some more work on stubgen.  FIXED
# - boost python sigs do not always include defaults for keyword args.  See UsdGeom.BBoxCache.__init__


def _filter_overloads(
    module_name: str, fullname: str, cpp_info: CppSigInfo | None
) -> tuple[list[DocElement] | None, bool]:
    """Filter c++ overloads"""
    if fullname == "pxr.Tf.Type.Define":
        # TfType::Define has 4 overloads, 2x static and 2x non-static. It also
        # uses templating to get its args, which are not picked up by doxygen.
        cpp_overloads = None
        is_static = True
    elif cpp_info:
        if len(set(overload.isStatic() for overload in cpp_info.overloads)) != 1:
            summary = "\n"
            for cpp_sig in cpp_info.overloads:
                summary += "   {}({}) [static={}]\n".format(
                    fullname,
                    ", ".join(
                        f"{param.name}: {param.type}" for param in cpp_sig.params
                    ),
                    cpp_sig.isStatic(),
                )
            notifier.warn(
                "Mixture of static and non-static overloads: removing static",
                module_name,
                summary,
            )
            cpp_overloads = [
                overload for overload in cpp_info.overloads if not overload.isStatic()
            ]
            is_static = False
        else:
            is_static = all(overload.isStatic() for overload in cpp_info.overloads)
            cpp_overloads = cpp_info.overloads
    else:
        cpp_overloads = None
        is_static = False
    return cpp_overloads, is_static


@lru_cache
def get_filtered_cpp_overloads(
    module_name: str, py_path: str
) -> tuple[list[DocElement] | None, bool]:
    cpp_paths = type_info.py_to_cpp_func_paths(py_path)
    cpp_info = type_info._get_cpp_sig_info(cpp_paths)
    cpp_overloads, is_static = _filter_overloads(module_name, py_path, cpp_info)
    if cpp_overloads is None:
        summary = "Python path: {}\nC++ paths:\n{}".format(
            py_path, "\n".join(repr(x) for x in cpp_paths)
        )
        notifier.warn("No c++ info found", module_name, summary)
    return cpp_overloads, is_static


def format_py_args(sig: FunctionSig) -> str:
    return ", ".join(f"{arg.name}: {arg.type}" for arg in sig.args)


def format_cpp_args(cpp_sig: DocElement) -> str:
    return ", ".join(f"{param.name}: {param.type}" for param in cpp_sig.params)


def get_sigs_from_cpp_overloads(
    ctx: FunctionContext, cpp_overloads: list[DocElement]
) -> list[FunctionSig]:
    # We only use C++ signatures:
    # convert to FunctionSig
    cpp_sigs: list[FunctionSig] = []
    for cpp_sig in cpp_overloads:
        args: list[ArgSig] = []
        for param in cpp_sig.params:
            py_arg_type = type_info.cpp_arg_to_py_type(param.type, is_result=False)
            has_default = param.default is not None
            args.append(ArgSig(param.name, py_arg_type, default=has_default))

        py_ret_type = type_info.cpp_arg_to_py_type(cpp_sig.returnType, is_result=True)
        cpp_sigs.append(FunctionSig(ctx.name, args, py_ret_type))
    return cpp_sigs


def get_sigs_from_cpp_overloads_with_ptrs(
    ctx: FunctionContext, cpp_overloads: list[DocElement]
) -> tuple[list[FunctionSig], list[FunctionSig]]:
    cpp_sigs_with_ptr: list[FunctionSig] = []
    cpp_sigs_without_ptr: list[FunctionSig] = []
    for cpp_sig in cpp_overloads:
        args_with_ptr: list[ArgSig] = []
        args_without_ptr: list[ArgSig] = []
        ptr_results = []
        for param in cpp_sig.params:
            has_default = param.default is not None
            py_arg_type = type_info.cpp_arg_to_py_type(param.type, is_result=False)
            if "*" in param.type:
                # a pointer result
                ptr_results.append(py_arg_type)
            else:
                args_without_ptr.append(
                    ArgSig(param.name, py_arg_type, default=has_default)
                )
            args_with_ptr.append(ArgSig(param.name, py_arg_type, default=has_default))

        py_ret_type = type_info.cpp_arg_to_py_type(cpp_sig.returnType, is_result=True)
        cpp_sigs_with_ptr.append(FunctionSig(ctx.name, args_with_ptr, py_ret_type))

        if ptr_results:
            # if ctx.name in ("GetKind", "GetConnectedSource"):
            if py_ret_type == "bool":
                # as a general rule skip primary bool return value
                results = ptr_results
            else:
                results = [py_ret_type] + ptr_results
            if len(results) > 1:
                py_ret_type = "tuple[{}]".format(", ".join(results))
            else:
                py_ret_type = results[0]
        cpp_sigs_without_ptr.append(
            FunctionSig(ctx.name, args_without_ptr, py_ret_type)
        )
    return cpp_sigs_with_ptr, cpp_sigs_without_ptr


class UsdBoostDocstringSignatureGenerator(
    BoostDocstringSignatureGenerator, BaseSigFixer
):
    def _fix_self_arg(self, sig: FunctionSig, ctx: FunctionContext) -> FunctionSig:
        "boost erroneously adds a self arg to some methods: remove it"
        if (
            len(sig.args) >= 1
            and ctx.class_info
            and sig.args[0].name == "arg1"
            and not sig.args[0].default
            and sig.args[0].type in ("object", ctx.class_info.name)
        ):
            notifier.warn("Stripping self type", ctx.module_name, ctx.fullname)
            return sig._replace(args=sig.args[1:])
        else:
            return sig

    def cleanup_type(
        self,
        py_type: str,
        ctx: FunctionContext,
        is_result: bool,
        fallback_type: str | None = None,
    ) -> str:
        """
        Called by cleanup_sig_types.

        - Apply fixes for known types/functions.
        - Use the docs to try to determine a full name.
        """
        if ctx.name == "_GetStaticTfType" and is_result:
            return "pxr.Tf.Type"

        if is_result and py_type == "object":
            return "Any"

        # handle generics, like 'list[Attribute]'
        parts = [x for x in re.split(PYPATH, py_type) if x]

        if len(parts) > 1:
            notifier.warn(
                "Ignoring fallback for compound type",
                ctx.module_name,
                f"{py_type} -> {parts}",
            )
            fallback_type = None

        new_parts = []
        for sub_py_type in parts:
            full_type = type_info.get_full_py_type(
                sub_py_type,
                ctx.module_name,
                fallback=fallback_type,
                current_func=ctx.fullname,
            )
            if (
                full_type is None
                and not sub_py_type.startswith("pxr.")
                and type_info.is_py_array_type(sub_py_type)
            ):
                sub_py_type = f"pxr.Vt.{sub_py_type}"
            elif (
                full_type is None
                and is_result
                and ctx.class_info
                and py_type == ctx.class_info.name
            ):
                # this is a fix for nested classes that have methods that return themselves
                # as a type, without using a fully qualified python path. Instead of trying to figure
                # out the path, we can use typing.Self.
                sub_py_type = "typing_extensions.Self"
            elif full_type:
                sub_py_type = full_type

            if not is_result and sub_py_type:
                other_types = type_info._get_implicitly_convertible_types().get(
                    sub_py_type
                )
                if other_types is not None:
                    union_types = [sub_py_type] + sorted(other_types)
                    # special case for lists because they are invariant
                    # FIXME: what if the subtype was converted to a full path?
                    if py_type == f"list[{sub_py_type}]":
                        return " | ".join(f"list[{typ}]" for typ in union_types)
                    else:
                        sub_py_type = " | ".join(union_types)

            new_parts.append(sub_py_type)
        py_type = "".join(new_parts)
        return py_type

    def _infer_type(
        self,
        boost_py_type: str | None,
        converted_py_type: str,
        ctx: FunctionContext,
        is_result: bool = False,
    ) -> str | None:
        """
        Use multiple approaches to create a best guess at a python type name.

        - Try to convert the c++ type to a python type.
        - Apply fixes for known types/functions.
        - Use the docs to try to determine a full name.

        boost_py_type : python type inferred by boost
        converted_py_type : python type converted from c++ type scraped from the docs
        """
        if boost_py_type in (None, "object", "list"):
            # boost is reliable with most other types, such as int, bool, dict, tuple
            return self.cleanup_type(converted_py_type, ctx, is_result)
        elif boost_py_type is not None:
            return self.cleanup_type(
                boost_py_type, ctx, is_result, fallback_type=converted_py_type
            )
        else:
            return None

    def _processs_sigs(
        self, sigs: list[FunctionSig], ctx: FunctionContext
    ) -> list[FunctionSig]:
        def summarize_overload_mismatch(
            sigs: list[FunctionSig], cpp_overloads: list[DocElement], corrected=False
        ):
            summary = ""
            for sig in sigs:
                summary += "   py   ({})\n".format(format_py_args(sig))
            for cpp_sig in cpp_overloads:
                summary += "   cpp  ({}) [static={}]\n".format(
                    format_cpp_args(cpp_sig),
                    cpp_sig.isStatic(),
                )

            notifier.warn(
                "Number of overloads do not match"
                + (" (corrected based on arg names)" if corrected else ""),
                ctx.module_name,
                "(py {} != cpp {}): {}\n{}".format(
                    len(sigs), len(cpp_overloads), ctx.fullname, summary
                ),
            )
            return summary

        match = re.match(r"(pxr\.Sdf.*Spec).__init__$", ctx.fullname)
        if match:
            # these types use a New() class constructor
            fullname = "{}.New".format(match.groups()[0])
            use_cpp_only = True
        else:
            fullname = ctx.fullname
            use_cpp_only = False

        cpp_overloads, is_static = get_filtered_cpp_overloads(ctx.module_name, fullname)

        if use_cpp_only:
            assert cpp_overloads is not None
            sigs = get_sigs_from_cpp_overloads(ctx, cpp_overloads)
        else:
            if not is_static:
                sigs = [self._fix_self_arg(sig, ctx) for sig in sigs]

            if cpp_overloads is not None and len(sigs) != len(cpp_overloads):
                # Overloads do not match between python and C++.
                # This would normally mean we throw out the C++, but before we do,
                # see if we can match cleanly on argument names
                sig_arg_names = [tuple(arg.name for arg in sig.args) for sig in sigs]
                if len(set(sig_arg_names)) == len(sigs):
                    # all sets of python argument names are unique. use them to index into
                    # the C++ overloads
                    cpp_overloads_by_args = defaultdict(list)
                    for cpp_sig in cpp_overloads:
                        cpp_overloads_by_args[
                            tuple(param.name for param in cpp_sig.params)
                        ].append(cpp_sig)
                    new_cpp_overloads = []
                    for sig_names in sig_arg_names:
                        cpp_sigs = cpp_overloads_by_args[sig_names]
                        # if there is more than one match the answer is ambiguous
                        if len(cpp_sigs) == 1:
                            new_cpp_overloads.append(cpp_sigs[0])

                    if len(new_cpp_overloads) == len(sigs):
                        summarize_overload_mismatch(sigs, cpp_overloads, corrected=True)
                        cpp_overloads = new_cpp_overloads

            if cpp_overloads is None or len(sigs) != len(cpp_overloads):
                # We only have python signatures:

                # apply fixes that don't rely on c++ docs:
                sigs = [self.cleanup_sig_types(sig, ctx) for sig in sigs]

                if cpp_overloads is not None:
                    # summarize the C++ <> python incompatibilties
                    summarize_overload_mismatch(sigs, cpp_overloads)
            else:
                # C++ and Python signatures exist and number of overloads is equal:

                (
                    cpp_sigs_with_ptr,
                    cpp_sigs_without_ptr,
                ) = get_sigs_from_cpp_overloads_with_ptrs(ctx, cpp_overloads)

                def matches(sigs1: list[FunctionSig], sigs2: list[FunctionSig]) -> int:
                    """
                    Compare the two signatures, by returning the number of signatures
                    with matching arg length.
                    """
                    return sum(
                        len(sig1.args) == len(sig2.args)
                        for (sig1, sig2) in zip(sigs1, sigs2)
                    )

                # the order of overloads between boost and doxygen do not match. sort based on
                # the list of args.
                sigs = sorted(sigs, key=sig_sort_key)

                # determine whether to move return-by-ptr args to results or not. USD code is not consistent about
                # one approach over the other.
                cpp_sigs_without_ptr = sorted(cpp_sigs_without_ptr, key=sig_sort_key)
                cpp_sigs_with_ptr = sorted(cpp_sigs_with_ptr, key=sig_sort_key)

                without_ptr_matches = matches(sigs, cpp_sigs_without_ptr)
                with_ptr_matches = matches(sigs, cpp_sigs_with_ptr)

                if without_ptr_matches > with_ptr_matches:
                    cpp_sigs = cpp_sigs_without_ptr
                else:
                    cpp_sigs = cpp_sigs_with_ptr

                for overload_num, (py_sig, cpp_sig) in enumerate(zip(sigs, cpp_sigs)):
                    if len(py_sig.args) != len(cpp_sig.args):
                        # C++ and python arg lists doesn't match: use the python sig
                        py_summary = "   py   ({})".format(format_py_args(py_sig))
                        cpp_summary = "   cpp  ({})".format(format_py_args(cpp_sig))
                        cpp_summary1 = " {} cpp! ({})".format(
                            without_ptr_matches,
                            format_py_args(cpp_sigs_without_ptr[overload_num]),
                        )
                        cpp_summary2 = " {} cpp* ({})".format(
                            with_ptr_matches,
                            format_py_args(cpp_sigs_with_ptr[overload_num]),
                        )
                        num_sigs = len(sigs)
                        curr_overload = overload_num + 1
                        notifier.warn(
                            "Sigs differ",
                            ctx.module_name,
                            f"({curr_overload} of {num_sigs}): {ctx.fullname}\n{py_summary}\n{cpp_summary}\n{cpp_summary1}\n{cpp_summary2}",
                        )
                        sigs[overload_num] = self.cleanup_sig_types(py_sig, ctx)
                    else:
                        # create best guesses for python types.
                        args = []
                        for py_arg, cpp_arg in zip(py_sig.args, cpp_sig.args):
                            py_type = self._infer_type(py_arg.type, cpp_arg.type, ctx)
                            args.append(
                                ArgSig(py_arg.name, py_type, default=py_arg.default)
                            )

                        return_type = self._infer_type(
                            py_sig.ret_type, cpp_sig.ret_type, ctx, is_result=True
                        )
                        if (
                            py_sig.ret_type == "list"
                            and return_type
                            and not return_type.startswith("list[")
                        ):
                            # c++ info attempted to change the result type. trust boost over the c++ docs in
                            # this case. It's probably a ptr result.
                            return_type = py_sig.ret_type

                        sigs[overload_num] = FunctionSig(py_sig.name, args, return_type)

        if (
            ctx.class_info is not None
            and ctx.name.startswith("__")
            and ctx.name.endswith("__")
        ):
            # correct special methods which boost may have given bogus args or values
            args = infer_c_method_args(ctx.name, ctx.class_info.self_var)
            if all(arg.type is not None for arg in args[1:]):
                sigs = [sig._replace(args=args) for sig in sigs]
            ret_type = infer_method_ret_type(ctx.name)
            if ret_type is not None:
                sigs = [sig._replace(ret_type=ret_type) for sig in sigs]

        return reduce_overloads(sigs)

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        if ctx.name == "__iter__":
            # stubgen has functionality to add __iter__ when __getitem__ is present to get
            # around an issue with mypy, but we can't process it with UsdBoostDocstringSignatureGenerator
            # because it mangles generic types (replaces [] in types)
            new_sigs = infer_sig_from_docstring(ctx.docstring, ctx.name)
            if new_sigs and new_sigs[0].ret_type != "Any":
                return new_sigs

        sigs = super().get_function_sig(default_sig, ctx)
        if not sigs:
            return None

        # The cpp wrappers use a special no_init object which creates bogus signatures
        if (
            ctx.name == "__init__"
            and len(sigs) == 1
            and [x.name for x in sigs[0].args] == ["tupleargs", "dictkwds"]
        ):
            sigs = [FunctionSig("__init__", [], "None")]

        return self._processs_sigs(sigs, ctx)

    def get_property_type(
        self, default_type: str | None, ctx: FunctionContext
    ) -> str | None:
        sigs = [FunctionSig(ctx.name, [], None)]
        sigs = self._processs_sigs(sigs, ctx)
        ret_type = sigs[0].ret_type
        return ret_type or default_type


def remove_redundant_submodule(module_name: str) -> tuple[str, bool]:
    """Convert 'pxr.Sdf._sdf' to 'pxr.Sdf'."""
    parts = module_name.split(".")
    if len(parts) == 3:
        # e.g. pxr.Sdf._sdf
        if parts[-1].startswith("_"):
            return ".".join(parts[:-1]), False
    elif len(parts) == 2:
        # e.g. pxr.Sdf
        return module_name, True
    return module_name, False


class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    """
    Make objects in pxr.Sdf._sdf appear to be defined in pxr.Sdf.

    The downside of this is that both pxr.Sdf._sdf and pxr.Sdf.__init__ are processed
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.module_name, self.is_c_module = remove_redundant_submodule(
            self.module_name
        )
        self.resort_members = True

    def is_skipped_attribute(self, attr: str) -> bool:
        return super().is_skipped_attribute(attr) or attr == "__reduce__"

    def get_obj_module(self, obj: object) -> str | None:
        """Return module name of the object."""
        module_name = getattr(obj, "__module__", None)
        if module_name:
            return remove_redundant_submodule(module_name)[0]
        return None

    def output(self) -> str:
        output = super().output()
        return '# mypy: disable-error-code="misc, override, no-redef"\n\n' + output

    def get_type_fullname(self, typ: type) -> str:
        type_name = super().get_type_fullname(typ)
        # enums may leave out their parent class, and don't appear to implement __qualname__
        # e.g. pxr.Usd.VersionPolicy should be pxr.Usd.SchemaRegistry.VersionPolicy
        if type_name.startswith("pxr.") and not is_existing_obj(type_name):
            full_type_name = type_info.get_full_py_type(
                type_name.split(".")[-1], self.module_name
            )
            if full_type_name is not None:
                return full_type_name

        return type_name

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [UsdBoostDocstringSignatureGenerator()]

    def is_classmethod(self, class_info: ClassInfo, name: str, obj: object) -> bool:
        if not self.is_c_module:
            return super().is_classmethod(class_info, name, obj)

        # in boost python it is impossible to distinguish between classmethod and instance method
        # so we consult the docs
        fullname = FunctionContext(
            self.module_name, name, class_info=class_info
        ).fullname
        cpp_paths = type_info.py_to_cpp_func_paths(fullname)
        cpp_info = type_info._get_cpp_sig_info(cpp_paths)
        if cpp_info:
            parent = cpp_info.parent
            if parent.isClass():
                return _filter_overloads(self.module_name, fullname, cpp_info)[1]
            else:
                # this is a loose function that has been added as a staticmethod
                return True
        return False


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]


def test():
    assert (
        type_info.cpp_arg_to_py_type("PCP_API SdfLayerHandleSet", is_result=True)
        == "list[pxr.Sdf.Layer]"
    )
    assert (
        type_info.cpp_arg_to_py_type(
            "std::function<bool( UsdAttribute const&)>const&", is_result=True
        )
        == "Callable[[pxr.Usd.Attribute], bool]"
    )


def main(outdir: str) -> None:
    type_info.populate()

    # Change this to only see errors for particular modules:
    notifier.set_modules(
        [
            # "pxr.UsdGeom",
            "pxr.UsdShade",
        ]
    )

    # Sadly, we don't have the ability to filter specific sub-packages, and
    # blindly ignoring all errors is too unsafe (resulted in real errors being
    # silently squashed). Instead we prevent recursion into sub-packages by
    # passing -m instead of -p
    packages = ["-m", "pxr"]
    for module in modules:
        packages.extend(["-m" if module == "Tf" else "-p", f"pxr.{module}"])

    stubgen_main(
        packages
        + [
            "--verbose",
            "--inspect-mode",
            "--include-private",
            f"-o={outdir}",
        ]
    )
    notifier.print_summary()
