from __future__ import absolute_import, annotations, division, print_function

import sys

import textwrap

# FIXME:  maybe we can kill two birds with one stone if we change this code to inject
#  valid signatures into docstrings instead of generating stubs.
# - Run stubgen a first time (we use stubgen just to piggy back the object crawling behavior).
#   During first pass we write sigs to __doc__, or alternately write we write __DOC.py files.
#   disable pyi generation during this crawl.
# - run stubgen a second time, this time parsing the new docstrings with signatures, and writing pyi as normal

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


import inspect
import subprocess
import os
import pathlib
import re
import pydoc
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Callable, DefaultDict, Iterator, Generic, NamedTuple, TypeVar
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
import doxygenlib.cdWriterDocstring

from stubgenlib import (
    insert_typevars,
    BaseSigFixer,
    AdvancedSigMatcher,
    AdvancedSignatureGenerator,
    BoostDocstringSignatureGenerator,
    infer_sig_from_boost_docstring,
    Notifier,
    CppTypeConverter,
    reduce_overloads,
    sig_sort_key,
)

T = TypeVar("T")
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
    """
    Writer class that allows doxygenlib.Parser.traverse() to run without erroring.

    Here's an outline of the doxygenlib process:
    1. The main entry piont creates a `Parser`, then calls `parser.parse()` to parse xml file
       into a tree of `XMLNode`
    2. The main entry point then loops over modules and for each module it instantiates
       a `Writer`.  Then:
    3. `parser.traverse()` is called to create `DocElement` instances from `XMLNode` instances.
        The parser calls `writer.getDocString() to fill in the `DocElement.doc` attribute.
    4. `writer.generate()` is called to actually write the __DOC.py files.
    5. The loop completes.
    """

    def getDocString(self, node: XMLNode) -> str:
        return ""

    def getDocTags(self, node: XMLNode) -> list[str]:
        return []

    def generate(self, output_file: str, docElements: list[DocElement]) -> None:
        raise NotImplementedError


class SimpleDocstringWriter(doxygenlib.cdWriterDocstring.Writer):
    def __init__(self):
        # do not call super.  It requires extra arguments which are not used
        # since we don't support 'generate'
        pass

    def generate(self, output_file: str, docElements: list[DocElement]) -> None:
        raise NotImplementedError

    @classmethod
    def _indent_docstring(cls, docstring: str, indent) -> str:
        """Fix indentation of docstring extracted from pybind11 or other binding generators."""
        lines = docstring.splitlines(keepends=True)
        if len(lines) > 1:
            if not all(line.startswith(indent) or not line.strip() for line in lines):
                # if the docstring is not indented, then indent all but the first line
                for i, line in enumerate(lines[1:]):
                    if line.strip():
                        lines[i + 1] = indent + line
        # if there's a trailing newline, add a final line to visually indent the quoted docstring
        if lines[-1].endswith("\n"):
            if len(lines) > 1:
                lines.append(indent)
            else:
                lines[-1] = lines[-1][:-1]
        return "".join(lines)

    def get_overload_docstring(
        self, fullname, module_name, doxy: DocElement
    ) -> str | None:
        lines = self._Writer__getDocumentation(fullname, None, doxy)
        if not lines:
            return None
        text = "\n".join(lines)
        indent = "    " * (len(fullname.split(".")) - len(module_name.split(".")))
        return self._indent_docstring(text, indent)

    def strip_boost_docstring(self, doc: str | None) -> str | None:
        return self._Writer__stripBoostSig(doc) if doc else None


@dataclass
class CppSigInfo:
    parent: DocElement
    overloads: list[DocElement]


def maybe_result(parts: list[str]) -> bool:
    """
    return if the argument looks like a c++ result
    """
    return "const" not in parts and ("*" in parts or "&" in parts)


# pxr/usd/sdf/proxyTypes.h
"""
typedef SdfListProxy<SdfSubLayerTypePolicy> SdfSubLayerProxy;
typedef SdfListEditorProxy<SdfPayloadTypePolicy> SdfPayloadEditorProxy;
typedef SdfListEditorProxy<SdfReferenceTypePolicy> SdfReferenceEditorProxy;

typedef SdfChildrenProxy<SdfVariantSetView> SdfVariantSetsProxy;

typedef SdfPayloadEditorProxy SdfPayloadsProxy;
typedef SdfReferenceEditorProxy SdfReferencesProxy;

typedef SdfMapEditProxy<VtDictionary> SdfDictionaryProxy;
typedef SdfMapEditProxy<SdfVariantSelectionMap> SdfVariantSelectionProxy;
typedef SdfMapEditProxy<SdfRelocatesMap,
                        SdfRelocatesMapProxyValuePolicy> SdfRelocatesMapProxy;
"""


class TypeInfo(CppTypeConverter):
    """Get info about types.

    Provides helpers for converting c++ data to python data, using data
    parsed from doxygen docs and source code.
    """

    # Used by CppTypeConverter,_get_typedefs()
    TYPE_DEF_INCLUDES = [
        "pxr/usd/sdf/layer.h",
        "pxr/usd/sdf/types.h",
        # "pxr/usd/usdShade/types.h",
        # "pxr/usd/usdShade/input.h",
        "pxr/usd/sdf/path.h",
        "pxr/usd/sdf/fileFormat.h",
        "pxr/usd/sdf/primSpec.h",
        "pxr/usd/sdf/proxyTypes.h",  # this gets special parsing treatment
        "pxr/usd/ndr/declare.h",
        "pxr/usd/usd/prim.h",
        "pxr/usd/usdGeom/basisCurves.h",
        "pxr/usd/usdShade/udimUtils.h",
    ]
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
    TYPE_MAP = [
        (r"\bstd::optional\b", "typing.Optional"),
        # (r"\bVtArray<\s*SdfAssetPath\s*>", "prx.Sdf.AssetPathArray"),
        (r"\bint64_t\b", "int"),
        (r"\bUsdSchemaVersion\b", "int"),
        (r"\bGfHalf\b", "float"),
        (r"\bTfFunctionRef\s*<.*>", "typing.Callable"),
        (r"\bHalf\b", "float"),
        (r"\bboost::python::", ""),
        (r"\bVtValue\b", "Any"),
        (r"\bPcpErrorVector\b", "list[ErrorBase]"),
        # this was intended to be used as a more general rule for SourceInfoVector, but
        # add usdShade/input.h/source.h caused long hangs during typedef resolution.
        # (
        #    r"\bTfSmallVector\s*<\s*(?P<type>.+)\s*,\s*(?P<num>\d+)\s*>",
        #    r"list[\g<type>]",
        # ),
        (r"\b(UsdShade)?SourceInfoVector\b", "list[UsdShadeConnectionSourceInfo]"),
        # this gets a lot of things right, but does produce a few errors, like list[Error] for PcpErrorVector, instead of list[ErrorBase]
        (r"\b" + CppTypeConverter.IDENTIFIER + r"Vector\b", r"list[\1]"),
        (r"\bTfToken\b", "str"),
        (r"\bVtArray\b", "list"),
        (r"\bVtDictionary\b", "dict"),
        (r"\bUsdMetadataValueMap\b", "dict"),
        # strip suffixes
        (r"RefPtr\b", ""),
        (r"Ptr\b", ""),
        (r"ConstHandle\b", ""),
        (r"Const\b", ""),
        (r"Handle\b", ""),
        # this is still too complicated for std::function parsing
        (
            # using UsdUtilsProcessingFunc = UsdUtilsDependencyInfo(
            #     const SdfLayerHandle &layer,
            #     const UsdUtilsDependencyInfo &dependencyInfo);
            r"\bstd::function\s*<\s*UsdUtilsProcessingFunc\s*>",
            "typing.Callable[[pxr.Sdf.Layer,  UsdUtilsDependencyInfo], UsdUtilsDependencyInfo]",
        ),
    ] + CppTypeConverter.TYPE_MAP
    # exact find-and-replace (no regex)
    RENAMES = [
        # simple renames:
        ("SdfBatchNamespaceEdit", "pxr.Sdf.NamespaceEdit"),
        # # childViews --
        (
            # typedef SdfChildrenView<Sdf_AttributeChildPolicy, SdfAttributeViewPredicate> SdfAttributeSpecView;
            "SdfChildrenView<Sdf_AttributeChildPolicy,SdfAttributeViewPredicate>",
            "pxr.Sdf.ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate",
        ),
        (
            # typedef SdfChildrenView<Sdf_VariantChildPolicy> SdfVariantView;
            "SdfChildrenView<Sdf_VariantChildPolicy>",
            "pxr.Sdf.ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec__",
        ),
        (
            # typedef SdfChildrenView<Sdf_PropertyChildPolicy> SdfPropertySpecView;
            "SdfChildrenView<Sdf_PropertyChildPolicy>",
            "pxr.Sdf.ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec__",
        ),
        (
            # typedef SdfChildrenView<Sdf_PrimChildPolicy> SdfPrimSpecView;
            "SdfChildrenView<Sdf_PrimChildPolicy>",
            "pxr.Sdf.ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec__",
        ),
        (
            # typedef SdfChildrenView<Sdf_RelationshipChildPolicy, SdfRelationshipViewPredicate> SdfRelationshipSpecView;
            "SdfChildrenView<Sdf_RelationshipChildPolicy,SdfRelationshipViewPredicate>",
            "pxr.Sdf.ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate",
        ),
        # (
        # typedef SdfChildrenView<Sdf_AttributeChildPolicy > SdfRelationalAttributeSpecView;
        # typedef SdfChildrenView<Sdf_VariantSetChildPolicy> SdfVariantSetView;
        # )
    ]
    # for types in this list we'll try to guess the python type from the template info
    PROXY_TYPES = [
        "SdfListProxy",
        "SdfListEditorProxy",
        # "SdfChildrenView",
        "SdfChildrenProxy",
        # note that some of the MapEditProxy classes have dynamically generated names like
        # MapEditProxy___1_map_SdfPath__SdfPath____1_less_SdfPath_____1_allocator___1_pair_SdfPath_const__SdfPath___
        "SdfMapEditProxy",
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
        writer: SimpleDocstringWriter,
        srcdir: str | None = None,
        verbose: bool = False,
    ) -> None:
        self.xml_index_file = xml_index_file
        self.pxr_modules_names = sorted(pxr_modules, key=len, reverse=True)
        self.cpp_sigs: dict[str, CppSigInfo] = {}
        self.cpp_classes: dict[str, CppSigInfo] = {}
        # mapping of short names to full python paths
        self.py_types: defaultdict[str, list[str]] = defaultdict(list)
        self._valid_modules = None
        self._writer = writer
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

    def _parse_typedefs(self, include_file: pathlib.Path) -> Iterator[tuple[str, str]]:
        it = super()._parse_typedefs(include_file)
        if include_file.name == "proxyTypes.h":
            renames = set(x[0] for x in self.RENAMES)
            for alias, type in it:
                if alias in renames:
                    continue
                for proxyType in self.PROXY_TYPES:
                    if type.startswith(proxyType):
                        type = (
                            type.replace(" ", "")
                            .replace("<", "_")
                            .replace(",", "_")
                            .replace(">", "")
                        )
                        break
                print("proxy", alias, type)
                yield alias, type
        else:
            yield from it

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
            raise RuntimeError("No source dir provided")

        if not os.path.exists(self.srcdir):
            raise RuntimeError(
                "Source directory does not exist: {}".format(self.srcdir)
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
            print("Parsing found {} implicitly convertible types".format(len(result)))

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
                    sub_types = {sub_type}
                    sub_types.update(result[sub_type])
                    result[f"pxr.Vt.{name}"].update(
                        f"typing.Iterable[{sub_type}]" for sub_type in sorted(sub_types)
                    )

            self._implicitly_convertible_types = dict(result)

        if not self._implicitly_convertible_types:
            raise RuntimeError("Could not find implicitly convertible types")
        return self._implicitly_convertible_types

    def _populate_map(self, docElemPath: list[DocElement]) -> None:
        """
        Cache the type information from the parsed documentation.

        docElemPath : list of DocElements from the root to the documented item
        """
        docElem = docElemPath[-1]

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
            elif childElem.isClass():
                info = CppSigInfo(
                    parent=docElem,
                    overloads=childObjectList,
                )
                parents = docElemPath[1:]
                cppPath = "::".join(x.name for x in parents + [childElem])
                self.cpp_classes[cppPath] = info

            # recurse through all of this element's children
            for child in childObjectList:
                self._populate_map(docElemPath + [child])

    def populate(self) -> None:
        parser = Parser()
        parser.parseDoxygenIndexFile(self.xml_index_file)
        # The parser calls `writer.getDocString() to fill in the `DocElement.doc` attribute.
        doc_elements = parser.traverse(self._writer)

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
                )[0]
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
writer = SimpleDocstringWriter()
type_info = TypeInfo(
    os.environ["USD_XML_INDEX"],
    modules,
    srcdir=os.environ["USD_SOURCE_ROOT"],
    writer=writer,
)


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
        summary = "\n  Python path: {}\n  C++ paths:\n{}".format(
            py_path, "\n".join("    " + repr(x) for x in cpp_paths)
        )
        notifier.warn("No C++ function info found", module_name, summary)
    return cpp_overloads, is_static


def format_py_args(sig: FunctionSig) -> str:
    sig_str = sig.format_sig()
    return sig_str[sig_str.find("(") :]


def format_cpp_args(cpp_sig: DocElement) -> str:
    args = ", ".join(f"{param.name}: {param.type}" for param in cpp_sig.params)
    return f"({args}) -> {cpp_sig.returnType}: ..."


def get_sigs_from_cpp_overloads(
    ctx: FunctionContext,
    cpp_overloads: list[DocElement],
    add_docstrings: bool = False,
) -> tuple[list[FunctionSig], list[FunctionSig]]:
    """
    Convert a set of C++ overloads into two sets of python signatures.

    The first set of sigs is a straight conversion from C++ to python.
    The second set of sigs has pointer args converted into return types.
    """
    cpp_sigs_with_ptrs: list[FunctionSig] = []
    cpp_sigs_without_ptrs: list[FunctionSig] = []

    for cpp_sig in cpp_overloads:
        args_ptr: list[ArgSig] = []
        args_no_ptr: list[ArgSig] = []
        ptr_results = []
        for i, param in enumerate(cpp_sig.params):
            has_default = param.default is not None
            if not param.name:
                param_name = f"unknownArg{i + 1}"
                notifier.warn(
                    "C++ argument missing name",
                    ctx.module_name,
                    f"{ctx.fullname}: argument index {i}",
                )
            else:
                param_name = param.name

            py_arg_type = type_info.cpp_arg_to_py_type(param.type, is_result=False)
            # FIXME: develop a better strategy for templates
            if py_arg_type == "T":
                py_arg_type = "Any"
            args_ptr.append(ArgSig(param_name, py_arg_type, default=has_default))

            if "*" in param.type:
                # a pointer result
                ptr_results.append(py_arg_type)
            else:
                args_no_ptr.append(ArgSig(param_name, py_arg_type, default=has_default))

        docstring = (
            writer.get_overload_docstring(ctx.fullname, ctx.module_name, cpp_sig)
            if add_docstrings
            else None
        )
        py_ret_type = type_info.cpp_arg_to_py_type(cpp_sig.returnType, is_result=True)
        # FIXME: develop a better strategy for templates
        if py_ret_type == "T":
            py_ret_type = "Any"
        cpp_sigs_with_ptrs.append(
            FunctionSig(ctx.name, args_ptr, py_ret_type, docstring)
        )

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
        cpp_sigs_without_ptrs.append(
            FunctionSig(ctx.name, args_no_ptr, py_ret_type, docstring)
        )
    return cpp_sigs_with_ptrs, cpp_sigs_without_ptrs


@dataclass
class MatchInfo:
    # name of the SigMatcher
    kind: str
    # cpp overload index:
    source_overload: int
    key: Any


@dataclass
class SigTracker:
    # mapping of boost overload number to FunctionSig
    matches: dict[int, FunctionSig] = field(default_factory=dict)
    # mapping of boost overload number to MatchInfo
    successes: dict[int, MatchInfo] = field(default_factory=dict)
    # mapping of boost overload number to MatchInfo
    failures: defaultdict[int, list[str]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def iter_sigs(self, sigs) -> Iterator[tuple[int, FunctionSig, FunctionSig | None]]:
        """Iterate over signatures in order of cpp overloads.

        This is necessary because the docstrings generated from C++ docs refer to
        overloads 'above' the current one, which is confusing if the overloads
        are not in their original order.
        """
        # create a mapping from C++ overload id to boost overload id
        cpp_overload_ids = {
            info.source_overload: py_overload_id
            for py_overload_id, info in self.successes.items()
        }
        # iterate over matched C++ overloads in order
        for cpp_overload_id in sorted(cpp_overload_ids):
            py_overload_id = cpp_overload_ids[cpp_overload_id]
            boost_sig = sigs[py_overload_id]
            cpp_sig = self.matches[py_overload_id]
            yield py_overload_id, boost_sig, cpp_sig
        # now yield remaining non-matches
        for py_overload_id in sorted(
            set(range(len(sigs))) - set(cpp_overload_ids.values())
        ):
            yield py_overload_id, sigs[py_overload_id], None


class SignatureMatcher(Generic[T]):
    name: str

    def __init__(self, validate: bool = True):
        """
        validate: If this matcher finds a match, ensure that it agrees with previous matches.
        """
        self.validate = validate

    def make_key(self, sig: FunctionSig) -> T:
        raise NotImplementedError

    def _validate_match(
        self, sig1: FunctionSig, sig2: FunctionSig, info: MatchInfo, key: T
    ) -> None:
        """Ensure signatures are equal"""
        # compare using format_sig because it doesn't include the docstring by default
        if sig1.format_sig() != sig2.format_sig():
            msg1 = (
                f"  (prev:  kind={info.kind:<10}, key={info.key})  {sig1.format_sig()}"
            )
            msg2 = f"  (new:   kind={self.name:<10}, key={key})  {sig2.format_sig()}"
            raise TypeError(f"Sigs not equal\n{msg1}\n{msg2}")

    def match(
        self,
        ctx: FunctionContext,
        py_sigs: list[FunctionSig],
        cpp_sigs: list[FunctionSig],
        tracker: SigTracker,
        skip: Callable[[int, FunctionSig], bool] | None = None,
    ) -> set[int]:
        """Use the argument types of boost-python signatures to find matching C++
        signatures.

        Returns the indices of the matching signatures.
        """

        cpp_sigs_map: DefaultDict[T, list[FunctionSig]] = defaultdict(list)
        cpp_overload_map: DefaultDict[T, list[int]] = defaultdict(list)
        for cpp_overload_id, cpp_sig in enumerate(cpp_sigs):
            if skip is not None and skip(cpp_overload_id, cpp_sig):
                continue
            key = self.make_key(cpp_sig)
            sigs = cpp_sigs_map[key]
            if cpp_sig not in sigs:
                sigs.append(cpp_sig)
                cpp_overload_map[key].append(cpp_overload_id)

        found = set()
        for py_overload_id, py_sig in enumerate(py_sigs):
            key = self.make_key(py_sig)
            cpp_sigs = cpp_sigs_map[key]
            # if there is more than one match the answer is ambiguous
            if len(cpp_sigs) == 1:
                if py_overload_id in tracker.matches:
                    tracker.failures[py_overload_id].append(
                        f"{self.name}: Already matched: {key}"
                    )
                    if self.validate:
                        self._validate_match(
                            tracker.matches[py_overload_id],
                            cpp_sigs[0],
                            tracker.successes[py_overload_id],
                            key,
                        )
                else:
                    cpp_overload_ids = cpp_overload_map[key]
                    assert len(cpp_overload_ids) == 1
                    tracker.matches[py_overload_id] = cpp_sigs[0]
                    tracker.successes[py_overload_id] = MatchInfo(
                        kind=self.name, source_overload=cpp_overload_ids[0], key=key
                    )
                    found.add(py_overload_id)
            elif len(cpp_sigs) > 1:
                tracker.failures[py_overload_id].append(
                    f"{self.name}: More than one match: {key}"
                )
            else:
                tracker.failures[py_overload_id].append(
                    f"{self.name}: No matches: {key}"
                )
        return found


class ArgNameMatcher(SignatureMatcher[tuple[str, ...]]):
    name = "names"

    def make_key(self, sig: FunctionSig) -> tuple[str, ...]:
        return tuple(arg.name for arg in sig.args)


class ArgTypeMatcher(SignatureMatcher[tuple["str | None", ...]]):
    name = "types"

    def make_key(self, sig: FunctionSig) -> tuple[str | None, ...]:
        return tuple(arg.type for arg in sig.args)


class ArgNumMatcher(SignatureMatcher[int]):
    name = "num"

    def make_key(self, sig: FunctionSig) -> int:
        return len(sig.args)


class ArgNumAndDefaultMatcher(SignatureMatcher[tuple[int, tuple[bool, ...]]]):
    name = "num+default"

    def make_key(self, sig: FunctionSig) -> tuple[int, tuple[bool, ...]]:
        return len(sig.args), tuple(arg.default for arg in sig.args)


class UsdBoostDocstringSignatureGenerator(AdvancedSignatureGenerator, BaseSigFixer):
    sig_matcher = AdvancedSigMatcher(
        # Full signature replacements.
        # The class name can be "*", in which case it will match any class
        signature_overrides={
            # these docstring sigs are malformed
            # FIXME: revisit this. mypy 1.11 introduced support for python 3.12-style generics, but it must be
            #   enabled using `enable_incomplete_feature = NewGenericSyntax`
            # "pxr.Tf.Notice.Register": "[NoticeT: pxr.Tf.Notice, T](_listener: type[NoticeT], _method: Callable[[NoticeT, T], typing.Any], _sender: T, /) -> pxr.Tf.Listener",
            # TypeVars are created using get_imports()
            # FIXME: add "/" to these when sig parser is made to accept "/" arguments
            "pxr.Tf.Notice.Register": "(_listener: type[NoticeT], _method: Callable[[NoticeT, T], typing.Any], _sender: T) -> pxr.Tf.Listener",
            "pxr.Tf.Notice.RegisterGlobally": "(_listener: type[NoticeT], _method: Callable[[NoticeT, typing.Any], typing.Any]) -> pxr.Tf.Listener",
            # FIXME: add "/" to these when sig parser is made to accept "/" arguments
            "pxr.*.*Array.__init__": [
                "(self) -> None",
                "(self, array: typing.Iterable) -> None",
                "(self, size: int, array: typing.Iterable) -> None",
                "(self, size: int) -> None",
            ],
        }
    )

    def __init__(self):
        super().__init__()
        self._processed_classes: set[str] = set()

    def _fix_self_arg(self, sig: FunctionSig, ctx: FunctionContext) -> FunctionSig:
        """boost erroneously adds a self arg to some methods: remove it"""
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

    # override of BaseSigFixer.cleanup_type()
    # called by BaseSigFixer.get_function_sig (via cleanup_sig_types)
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
                f"{ctx.fullname}: {py_type} -> {parts}",
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
                and ctx.class_info.parent is not None
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
                    # other_types = set(self.cleanup_type(other_type, ctx, is_result) for other_type in other_types)
                    union_types = [sub_py_type] + sorted(other_types)
                    # special case for lists because they are invariant
                    # FIXME: what if the subtype was converted to a full path?
                    if py_type == f"list[{sub_py_type}]":
                        return " | ".join(f"list[{typ}]" for typ in union_types)
                    else:
                        sub_py_type = " | ".join(union_types)

            new_parts.append(sub_py_type)
        new_py_type = "".join(new_parts)
        return new_py_type

    def _infer_type(
        self,
        boost_py_type: str | None,
        cpp_py_type: str | None,
        ctx: FunctionContext,
        is_result: bool = False,
        # FIXME: already_cleaned=False is never used
        already_cleaned: bool = False,
    ) -> str | None:
        """
        Given a python type guessed from boost and one from Doxygen, use multiple
        approaches to find the best.

        - Try to convert the c++ type to a python type.
        - Apply fixes for known types/functions.
        - Use the docs to try to determine a full name.

        boost_py_type : python type inferred by boost
        cpp_py_type : python type converted from c++ type scraped from the docs
        """
        if boost_py_type is None or boost_py_type in ("Any", "object", "list"):
            # None is important here, though I don't remember why.
            # boost is reliable with most other types, such as int, bool, dict, tuple
            if cpp_py_type is None:
                return None
            return (
                cpp_py_type
                if already_cleaned
                else self.cleanup_type(cpp_py_type, ctx, is_result)
            )
        elif boost_py_type is not None:
            if (
                already_cleaned
                and cpp_py_type
                and cpp_py_type.startswith("pxr.")
                and boost_py_type.startswith("pxr.")
                and re.match("^" + PYPATH + "$", cpp_py_type)
                and re.match("^" + PYPATH + "$", boost_py_type)
                and cpp_py_type.split(".")[-1] == boost_py_type.split(".")[-1]
            ):
                # The boost type never includes module namespace, so it can be ambiguous. Currently
                # this tool guesses that the type lives in the current module.
                # The C++ type can be more accurate in this scenario, so use it.
                # For example, pxr.Usd.PrimDefinition.Attribute vs pxr.Usd.Attribute
                return cpp_py_type
            elif already_cleaned and not is_result:
                return boost_py_type
            else:
                return self.cleanup_type(
                    boost_py_type, ctx, is_result, fallback_type=cpp_py_type
                )
        else:
            return None

    def _summarize_overload_mismatch(
        self,
        msg: str,
        ctx: FunctionContext,
        failures: list[str],
        sigs: list[FunctionSig],
        cpp_overloads: list[DocElement],
        overload_num: int | None = None,
        match: FunctionSig | None = None,
        **other_sigs: list[FunctionSig],
    ):
        failures_str = "\n".join(f" - {line}" for line in failures)
        summary = ""
        for i, sig in enumerate(sigs):
            marker = "*" if overload_num == i else " "
            signame = "py"
            summary += f"{marker}  {signame:<14}{format_py_args(sig)}\n"

        for signame, sigs in other_sigs.items():
            for sig in sigs:
                marker = "*" if sig == match else " "
                summary += f"{marker}  {signame:<14}{format_py_args(sig)}\n"

        for cpp_sig in cpp_overloads:
            summary += "   cpp           {}{}\n".format(
                format_cpp_args(cpp_sig),
                "[static]" if cpp_sig.isStatic() else "",
            )

        notifier.warn(
            msg,
            ctx.module_name,
            f"{ctx.fullname}\n{failures_str}\n{summary}",
        )
        return summary

    def _set_class_docstring(self, ctx: FunctionContext) -> None:
        """
        Find docstings parsed from Doxygen and set them on the context.
        """
        if not ctx.class_info:
            return

        full_class_name = ctx.fullname.rsplit(".", 1)[0]
        if full_class_name in self._processed_classes:
            return

        cpp_func_paths = type_info.py_to_cpp_func_paths(ctx.fullname)
        self._processed_classes.add(full_class_name)
        if not cpp_func_paths:
            return

        cpp_cls_path = cpp_func_paths[0].path.rsplit("::", 1)[0]
        cls_info = type_info.cpp_classes.get(cpp_cls_path)
        if not cls_info:
            notifier.warn(
                "No C++ class info found",
                ctx.module_name,
                f"{full_class_name} -> {cpp_cls_path}",
            )
        else:
            ctx.class_info.docstring = writer.get_overload_docstring(
                full_class_name, ctx.module_name, cls_info.overloads[0]
            )

    def _choose_overload_set(
        self,
        ctx: FunctionContext,
        py_sigs: list[FunctionSig],
        cpp_sigs_with_ptrs: list[FunctionSig],
        cpp_sigs_without_ptrs: list[FunctionSig],
    ) -> tuple[list[FunctionSig], list[FunctionSig]]:
        def matches(sigs1: list[FunctionSig], sigs2: list[FunctionSig]) -> int:
            """
            Compare the two sets of overloads, by returning the number of signatures
            with matching arg length.
            """
            return sum(
                len(sig1.args) == len(sig2.args) for (sig1, sig2) in zip(sigs1, sigs2)
            )

        # the order of overloads between boost and doxygen do not match.
        # before we compare them we need to sort all of them based on
        # the list of args. Remember: we've already determined boost/python
        # and C++ have the same number of overloads.

        # boost python signatures:
        py_sigs = sorted(py_sigs, key=sig_sort_key)

        # determine whether to use overloads that return-by-ptr or not.
        # USD code is not consistent about one approach over the other.

        # direct conversion of C++ info to python signatures:
        cpp_sigs_with_ptrs = sorted(cpp_sigs_with_ptrs, key=sig_sort_key)
        # conversion of C++ info to python signatures, with ptr args converted to results
        cpp_sigs_without_ptrs = sorted(cpp_sigs_without_ptrs, key=sig_sort_key)

        # compare the two sets of sigs that were generated from parsed C++ info
        # and determine which set of overloads has the most correspondence to the
        # boost signatures, which is our source of truth.
        num_no_ptr_matches = matches(py_sigs, cpp_sigs_without_ptrs)
        num_ptr_matches = matches(py_sigs, cpp_sigs_with_ptrs)

        # use the set with the most matches
        if num_no_ptr_matches > num_ptr_matches:
            cpp_sigs = cpp_sigs_without_ptrs
        else:
            cpp_sigs = cpp_sigs_with_ptrs

        # loop through and cleanup types
        for overload_num, (py_sig, cpp_sig) in enumerate(zip(py_sigs, cpp_sigs)):
            if len(py_sig.args) != len(cpp_sig.args):
                # arg lists between C++ docs and boost-python don't match: use the boost-python sig
                # C++ and python arg lists doesn't match: use the python sig
                py_summary = "   py   ({})".format(format_py_args(py_sig))
                cpp_summary = "   cpp  ({})".format(format_py_args(cpp_sig))
                cpp_summary1 = " {} cpp! ({})".format(
                    num_no_ptr_matches,
                    format_py_args(cpp_sigs_without_ptrs[overload_num]),
                )
                cpp_summary2 = " {} cpp* ({})".format(
                    num_ptr_matches,
                    format_py_args(cpp_sigs_with_ptrs[overload_num]),
                )
                num_sigs = len(py_sigs)
                curr_overload = overload_num + 1
                notifier.warn(
                    "Number of args between python and C++ signature differs (using python)",
                    ctx.module_name,
                    (
                        f"({curr_overload} of {num_sigs}): {ctx.fullname}\n{py_summary}\n{cpp_summary}\n{cpp_summary1}\n{cpp_summary2}"
                    ),
                )
        return py_sigs, cpp_sigs

    def _add_positional_only_args(
        self, ctx: FunctionContext, py_sig: FunctionSig
    ) -> FunctionSig:
        """
        Analyze the signature and add a '/' argument if necessary to mark
        arguments which cannot be access by named.
        """
        args = []
        requires_pos_only: bool | None = None
        for arg_num, py_arg in enumerate(py_sig.args):
            if BoostDocstringSignatureGenerator.is_default_boost_arg(py_arg.name):
                if requires_pos_only is False:
                    raise ValueError(
                        f"{ctx.fullname}: Unnamed argument appears after named one: {py_sig.format_sig()}"
                    )
                requires_pos_only = True
            else:
                if requires_pos_only:
                    # force arguments before this to be positional only
                    args.append(ArgSig("/"))
                requires_pos_only = False
            args.append(py_arg)

        if requires_pos_only:
            # force arguments before this to be positional only
            args.append(ArgSig("/"))

        return py_sig._replace(args=args)

    def _fix_schema_init(
        self, ctx: FunctionContext, sigs: list[FunctionSig]
    ) -> list[FunctionSig]:
        """
        Many schema classes have the same arguments, and the python bindings have a subtle difference
        that prevents the matcher classes from successfully matching
        """
        if ctx.name == "__init__" and len(sigs) >= 2:
            all_args = [sig.args for sig in sigs]
            args1 = [ArgSig("prim", "pxr.Usd.Prim", default=True)]
            args2 = [ArgSig("schemaObj", "pxr.Usd.SchemaBase")]
            if args1 in all_args and args2 in all_args:
                index1 = all_args.index(args1)
                # replace the use of a default argument with an empty overload
                sigs[index1].args[0].default = False
                return [FunctionSig("__init__", [], None)] + sigs
        return sigs

    def _processs_sigs(
        self, sigs: list[FunctionSig], ctx: FunctionContext
    ) -> list[FunctionSig]:
        """
        sigs: signatures as processed from UsdBoostDocstringSignatureGenerator
        """
        notifier.accumulate("*Total functions*")
        for _ in sigs:
            notifier.accumulate("*Total overloads*")

        ctx.docstring = writer.strip_boost_docstring(ctx.docstring)

        self._set_class_docstring(ctx)

        match = re.match(r"(pxr\.Sdf.*Spec).__init__$", ctx.fullname)
        if match:
            # these types use a New() class constructor
            fullname = "{}.New".format(match.groups()[0])
            use_cpp_only = True
        else:
            fullname = ctx.fullname
            use_cpp_only = False

        cpp_overloads, is_static = get_filtered_cpp_overloads(ctx.module_name, fullname)

        if not is_static and not use_cpp_only:
            sigs = [self._fix_self_arg(sig, ctx) for sig in sigs]

        if use_cpp_only:
            assert cpp_overloads is not None
            sigs = [
                self._add_positional_only_args(ctx, sig)
                for sig in get_sigs_from_cpp_overloads(
                    ctx, cpp_overloads, add_docstrings=True
                )[0]
            ]
        elif cpp_overloads is None:
            # We only have python signatures:
            # apply fixes that don't rely on c++ docs:
            sigs = [
                self._add_positional_only_args(ctx, self.cleanup_sig_types(sig, ctx))
                for sig in sigs
            ]
        else:
            (cpp_sigs_with_ptrs, cpp_sigs_without_ptrs) = get_sigs_from_cpp_overloads(
                ctx, cpp_overloads, add_docstrings=True
            )

            sigs = self.cleanup_sigs_types(sigs, ctx)
            cpp_sigs_with_ptrs = self._fix_schema_init(
                ctx, reduce_overloads(self.cleanup_sigs_types(cpp_sigs_with_ptrs, ctx))
            )
            cpp_sigs_without_ptrs = self._fix_schema_init(
                ctx,
                reduce_overloads(self.cleanup_sigs_types(cpp_sigs_without_ptrs, ctx)),
            )

            tracker = SigTracker()
            arg_names = ArgNameMatcher()
            arg_types = ArgTypeMatcher()
            arg_nums1 = ArgNumAndDefaultMatcher(validate=False)
            arg_nums2 = ArgNumMatcher(validate=False)

            def skip_used(overload: int, sig: FunctionSig) -> bool:
                """
                we use this to introduce some mutual exclusivity, because it's possible
                for two different overloads to match the same C++ overload w/ and w/out pointers.
                see: GetVersionIfHasAPIInFamily.  conceptually, once a C++ overload has been matched,
                its corresonding ptr/noptr overload should no longer be an option.
                """
                return overload in [
                    x.source_overload for x in tracker.successes.values()
                ]

            arg_names.match(
                ctx, sigs, cpp_sigs_with_ptrs + cpp_sigs_without_ptrs, tracker
            )
            arg_types.match(ctx, sigs, cpp_sigs_without_ptrs, tracker)
            arg_types.match(ctx, sigs, cpp_sigs_with_ptrs, tracker)

            arg_nums1.match(ctx, sigs, cpp_sigs_without_ptrs, tracker)
            arg_nums1.match(ctx, sigs, cpp_sigs_with_ptrs, tracker, skip=skip_used)

            arg_nums2.match(ctx, sigs, cpp_sigs_without_ptrs, tracker, skip=skip_used)
            arg_nums2.match(ctx, sigs, cpp_sigs_with_ptrs, tracker, skip=skip_used)

            # special case where we found no matches, so we just take one full set of overloads
            if not tracker.matches and len(sigs) == len(cpp_overloads):
                sigs, cpp_sigs = self._choose_overload_set(
                    ctx, sigs, cpp_sigs_with_ptrs, cpp_sigs_without_ptrs
                )
                for i, sig in enumerate(cpp_sigs):
                    tracker.matches[i] = sig
                    tracker.successes[i] = MatchInfo(
                        kind="fallback for unmatched", source_overload=i, key=None
                    )

            # loop through and cleanup types
            orig_sigs = sigs
            sigs = []
            for py_overload_id, py_sig, cpp_sig in tracker.iter_sigs(orig_sigs):
                if cpp_sig is None:
                    # use sigs from boost-python as-is (cleanup_sig_types has already been applied)
                    self._summarize_overload_mismatch(
                        "Could not find C++ info for overload",
                        ctx,
                        tracker.failures[py_overload_id],
                        orig_sigs,
                        cpp_overloads,
                        py_overload_id,
                        cpp_ptrs=cpp_sigs_with_ptrs,
                        cpp_no_ptrs=cpp_sigs_without_ptrs,
                    )
                    sigs.append(self._add_positional_only_args(ctx, py_sig))
                elif len(py_sig.args) != len(cpp_sig.args):
                    # arg lists between C++ docs and boost-python don't match:
                    # use the boost-python sig. In practice, I don't think this ever happens
                    self._summarize_overload_mismatch(
                        "C++ info for overload has wrong number of args",
                        ctx,
                        tracker.failures[py_overload_id],
                        orig_sigs,
                        cpp_overloads,
                        py_overload_id,
                        cpp_found=[cpp_sig],
                        cpp_ptrs=cpp_sigs_with_ptrs,
                        cpp_no_ptrs=cpp_sigs_without_ptrs,
                    )
                    sigs.append(
                        self._add_positional_only_args(ctx, py_sig)._replace(
                            docstring=cpp_sig.docstring
                        )
                    )
                else:
                    if "HasInfo" in ctx.fullname:
                        self._summarize_overload_mismatch(
                            "Match reason",
                            ctx,
                            [tracker.successes[py_overload_id].kind],
                            orig_sigs,
                            cpp_overloads,
                            py_overload_id,
                            match=cpp_sig,
                            cpp_ptrs=cpp_sigs_with_ptrs,
                            cpp_no_ptrs=cpp_sigs_without_ptrs,
                        )
                    # create best guesses for python types.
                    args = []
                    arg_num = 0
                    fixed_py_sig = self._add_positional_only_args(ctx, py_sig)
                    for py_arg in fixed_py_sig.args:
                        if py_arg.name == "/":
                            args.append(py_arg)
                            continue

                        cpp_arg = cpp_sig.args[arg_num]

                        py_type = self._infer_type(
                            py_arg.type, cpp_arg.type, ctx, already_cleaned=True
                        )

                        # something appears to be wrong with wrapped static methods where
                        # named arguments are offset by one.  For example, SchemaRegistry.MakeMultipleApplyNameInstance
                        # is wrapped like this:
                        #         .def("MakeMultipleApplyNameInstance",
                        #              &This::MakeMultipleApplyNameInstance,
                        #              arg("nameTemplate"),
                        #              arg("instanceName"))
                        #         .staticmethod("MakeMultipleApplyNameInstance")
                        # And yet it produces this boost python signature:
                        #         (arg1: object, nameTemplate: object) -> Any: ...
                        # Notice that "nameTemplate" fills the arg2 spot.
                        if BoostDocstringSignatureGenerator.is_default_boost_arg(
                            py_arg.name
                        ):
                            # this is safe because default args can only be passed positionally and not by name.
                            arg_name = f"_{cpp_arg.name}"
                        else:
                            arg_name = py_arg.name

                        args.append(
                            ArgSig(
                                arg_name,
                                py_type,
                                default=py_arg.default,
                            )
                        )
                        arg_num += 1

                    return_type = self._infer_type(
                        py_sig.ret_type,
                        cpp_sig.ret_type,
                        ctx,
                        is_result=True,
                        already_cleaned=True,
                    )

                    if (
                        py_sig.ret_type == "list"
                        and return_type
                        and not return_type.startswith("list[")
                    ):
                        # c++ info attempted to change the result type.
                        # trust boost over the c++ docs in this case. It's probably a ptr result.
                        return_type = py_sig.ret_type

                    sigs.append(
                        FunctionSig(
                            py_sig.name,
                            args,
                            return_type,
                            docstring=cpp_sig.docstring,
                        )
                    )

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
            # around an issue with mypy, but we can't process it with infer_sig_from_boost_docstring
            # because it mangles generic types (replaces [] in types)
            new_sigs = infer_sig_from_docstring(ctx.docstring, ctx.name)
            if new_sigs and new_sigs[0].ret_type != "Any":
                return new_sigs

        override = self.get_overridden_signatures(ctx)
        if override:
            # early out: fix up the docstrings before we return
            ctx.docstring = writer.strip_boost_docstring(ctx.docstring)
            return override

        if ctx.docstring:
            # USD boost docstrings sometimes include manually authored signatures. They
            # are always indented.
            docstring = "".join(
                line
                for line in ctx.docstring.splitlines(keepends=True)
                if not re.match(" {4}[A-Za-z_]", line)
            )
            sigs = infer_sig_from_boost_docstring(docstring, ctx.name)
            if not sigs:
                return None
        else:
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
        ctx.docstring = sigs[0].docstring or ctx.docstring
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

    def get_imports(self) -> str:
        imports = super().get_imports()
        if self.module_name == "pxr.Tf":
            return insert_typevars(
                imports,
                [
                    "T = typing.TypeVar('T')",
                    "NoticeT = typing.TypeVar('NoticeT', bound='Notice')",
                ],
            )
        else:
            return imports


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]


def test():
    assert (
        type_info.cpp_arg_to_py_type("PCP_API SdfLayerHandleSet", is_result=True)
        == "list[pxr.Sdf.Layer]"
    )
    print(
        type_info.cpp_arg_to_py_type(
            "std::function<bool (const TfToken &propertyName)>", is_result=True
        )
    )
    assert (
        type_info.cpp_arg_to_py_type(
            "std::function<bool( UsdAttribute const&)>const&", is_result=True
        )
        == "typing.Callable[[pxr.Usd.Attribute], bool]"
    )
    # `using` syntax is a bit different from `typedef` because it includes the argument name
    assert (
        type_info.cpp_arg_to_py_type(
            "std::function<bool (const TfToken &propertyName)>", is_result=True
        )
        == "typing.Callable[[str], bool]"
    )


def main(outdir: str) -> None:
    type_info.populate()

    # Change this to only see errors for particular modules:
    notifier.set_modules(
        [
            "pxr.Sdf",
            # "pxr.Pcp",
            # "pxr.Sdr",
            # "pxr.UsdGeom",
            # "pxr.UsdLux",
            # "pxr.UsdShade",
            # "pxr.UsdUtils",
            # "pxr.Usd",
            # "pxr.Ar",
            # "pxr.Tf",
        ]
    )
    # notifier.set_keys(
    #     [
    #         "Could not find C++ info for overload",
    #     ]
    # )

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
            "--include-docstrings",
            f"-o={outdir}",
        ]
    )
    notifier.print_summary()
    percent = notifier.get_key_count(
        "Could not find C++ info for overload"
    ) / notifier.get_key_count("*Total overloads*")
    print("Overload coverage {:.2f}%".format((1 - percent) * 100))
