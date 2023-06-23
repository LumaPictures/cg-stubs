from __future__ import absolute_import, annotations, division, print_function

import subprocess
import pkgutil
import os
import re
import pydoc
import types
from collections import defaultdict
from dataclasses import dataclass

import mypy.stubgen
import mypy.stubgenc
import mypy.stubutil
from mypy.fastparse import parse_type_comment
from mypy.stubdoc import ArgSig
from mypy.stubgen import main as stubgen_main
from mypy.stubgenc import \
    DocstringSignatureGenerator as FunctionContext, FunctionSig, SignatureGenerator, infer_method_args
from mypy.stubutil import infer_method_ret_type

mypy.stubutil.NOT_IMPORTABLE_MODULES = ('pxr.Tf.testenv', 'pxr.Tf.testenv.testTfScriptModuleLoader_AAA_RaisesError')

from doxygenlib.cdParser import Parser
from doxygenlib.cdWriterDocstring import Writer
from doxygenlib.cdUtils import SetDebugMode

from stubgenlib import BaseSigFixer, BoostDocstringSignatureGenerator


SetDebugMode(False)

# FIXME: there's a python func for this
# a python identifier
IDENTIFIER = r'([a-zA-Z_][a-zA-Z0-9_]*)'
STRIP = r'\b(?:const|friend|constexpr)\b'
TYPE_MAP = [
    (r'\bVtArray<\s*SdfAssetPath\s*>', 'SdfAssetPathArray'),
    (r'\bstd::string\b', 'str'),
    (r'\bstring\b', 'str'),
    (r'\bsize_t\b', 'int'),
    (r'\bchar\b', 'str'),
    (r'\bstd::function<(.+)\((.*)\)>', r'typing.Callable[[\2],\1]'),
    (r'\bstd::vector\b', 'list'),
    (r'\bstd::pair\b', 'tuple'),
    (r'\bstd::set\b', 'list'),
    (r'\bdouble\b', 'float'),
    (r'\bboost::python::', ''),
    (r'\bvoid\b', 'None'),
    (r'\bVtValue\b', 'Any'),
    (r'\b' + IDENTIFIER + r'Vector\b', r'list[\1]'),
    (r'\bTfToken\b', 'str'),
    (r'\bVtDictionary\b', 'dict'),
    (r'\bUsdMetadataValueMap\b', 'dict'),
    # strip suffixes
    (r'RefPtr\b', ''),
    (r'Ptr\b', ''),
    (r'ConstHandle\b', ''),
    (r'Const\b', ''),
    (r'Handle\b', ''),
]

RENAMES =[
    # simple renames:
    (r'\bSdfBatchNamespaceEdit\b', 'pxr.Sdf.NamespaceEdit'),
    # Sdf mapping types:
    (r'\bSdfLayerHandleSet\b', 'list[pxr.Sdf.Layer]'),
    (r'\bSdfDictionaryProxy\b', 'pxr.Sdf.MapEditProxy_VtDictionary'),
    (r'\bSdfReferencesProxy\b', 'pxr.Sdf.ReferenceTypePolicy'),
    (r'\bSdfSubLayerProxy\b', 'pxr.Sdf.ListProxy_SdfSubLayerTypePolicy'),
    # pathKey
    (r'\bSdfInheritsProxy\b', 'pxr.Sdf.ListEditorProxy_SdfPathKeyPolicy'),
    (r'\bSdfSpecializesProxy\b', 'pxr.Sdf.ListEditorProxy_SdfPathKeyPolicy'),
    # nameTokenKey
    (r'\bSdfNameOrderProxy\b', 'pxr.Sdf.ListProxy_SdfNameTokenKeyPolicy'),
    (r'\bSdfNameChildrenOrderProxy\b', 'pxr.Sdf.ListProxy_SdfNameTokenKeyPolicy'),
    (r'\bSdfPropertyOrderProxy\b', 'pxr.Sdf.ListProxy_SdfNameTokenKeyPolicy'),
    # nameKey
    (r'\bSdfVariantSetNamesProxy\b', 'pxr.Sdf.ListEditorProxy_SdfNameKeyPolicy'),
]

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


# class StubHelper(Writer, DummyWriter):

#     def populate_map(self, sig_map, docElemPath: list[DocElement]) -> list[str]:
#         """
#         docElem : list of DocElements from the root to the documented item
#         """
#         docElem = docElemPath[-1]

#         for childName, childObjectList in docElem.children.items():
#             if self.module.__name__ == 'pxr.Sdf' and docElem.name == "Sdf":
#                 print(childObjectList)

#             # Alteranately. don't bother trying to find the python object
#             # (pypath, ppypath1, ppypath2) = self.__pathGenerator(parentPath, overloads)

#             # Work out the possible Python name(s) for this C++ object
#             # Note that some C++ names have both potential corresponding
#             # python method and property names.
#             (pyobj, pypath, proppyobj, proppypath, jumped) \
#                 = self._getPythonObjectAndPath(docElemPath, childObjectList)
#             if self.module.__name__ == 'pxr.Sdf' and \
#                     "SdfPathFindLongestPrefix" in [child.name for child in childObjectList]:
#                 print("HERE", docElem, childName, pyobj, pypath, [child.location for child in childObjectList])

#             if self.module.__name__ == 'pxr.Sdf' and \
#                     "VT_TYPE_IS_CHEAP_TO_COPY" in [child.name for child in childObjectList]:
#                 print("GARBAGE", docElem, childName, pyobj, pypath, [child.location for child in childObjectList])

#             # if docElem.name == "SdfPathFindLongestPrefix":
#             #     print("NAME", pyobj, pypath, proppypath)
#             # pyobj will be None if the object does not exist in self.module
#             if pyobj is not None:
#                 info = {
#                     'parent': docElem,
#                     'definitions': childObjectList,
#                 }
#                 fullPyPath = "{}.{}".format(self.module.__name__, pypath)
#                 sig_map[pypath] = info
#                 sig_map[fullPyPath] = info

#             # recurse through all of this element's children too
#             for child in childObjectList:
#                 if self.module.__name__ == 'pxr.Sdf' and child.name == "SdfPathFindLongestPrefix":
#                     print("CHILD", child)
#                 self.populate_map(sig_map, docElemPath + [child])

# parser = Parser()
# parser.parseDoxygenIndexFile(self.xml_index_file)
# docElements = parser.traverse(DummyWriter())
# for module_name in modules:
#     writer = StubHelper("pxr", module_name)
#     for docElement in docElements:
#         writer.populate_map(cpp_sigs, [docElement])

@dataclass
class SigInfo:
    parent: DocElement
    overloads: list[DocElement]


class Notifier:
    def __init__(self) -> None:
        self._seen_msgs = defaultdict(int)
        self._seen_keys = defaultdict(int)
        self._modules = []

    def set_modules(self, modules: list[str]):
        self._modules = modules

    def warn(self, key: str, module: str, msg: str):
        if (key, module, msg) not in self._seen_msgs:
            if not self._modules or module in self._modules:
                print(f"({module}) {key}: {msg}")
        self._seen_msgs[(key, module, msg)] += 1
        self._seen_keys[key] += 1

    def print_summary(self):
        print()
        print("Warning Summary:")
        for key in sorted(self._seen_keys):
            count = self._seen_keys[key]
            print(f"  {key}: {count}")


def maybe_result(parts: list[str]) -> bool:
    """
    return if the argument looks like a c++ result
    """
    return 'const' not in parts and ('*' in parts or '&' in parts)


def should_strip_part(x: str) -> bool:
    """
    whether the part looks like a c++ keyword
    """
    return x.endswith('_API') or not x


class SourceInfo:
    """
    Helper for converting c++ data to python data, using info parsed from the
    source
    """
    def __init__(self, srcdir: str | None = None, verbose=False):
        self.srcdir = srcdir
        self._valid_modules = None
        self._implicitly_convertible_types = None
        self.verbose = verbose

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

    def get_type_from_path(self, path):
        parts = path.split(os.path.sep)
        name = os.path.splitext(parts[-1])[0]
        assert name.startswith('wrap')
        return doc_info.to_python_id(capitalize(parts[-2]) + name[4:])

    def get_implicitly_convertible_types(self) -> dict[str, set[str]]:
        """
        inspect the boost-python code to parse the rules for implicitly
        convertible types
        """
        if self.srcdir is None:
            return {}

        # FIXME: add module prefixes to all types (Output, Input, Parameter, etc are not prefixed)
        # FIXME: parse other conversions defined using TfPyContainerConversions
        if self._implicitly_convertible_types is None:
            output = subprocess.check_output(
                ['grep', 'implicitly_convertible', '-r',
                 os.path.join(self.srcdir, 'pxr'),
                 '--include=wrap*.cpp'], text=True)
            code_reg = re.compile(r'\s+implicitly_convertible<\s*(?P<from>(%s|:)+),\s*(?P<to>(%s|:)+)\s*>\(\)' %
                                  (IDENTIFIER, IDENTIFIER))
            result = defaultdict(set)
            for line in output.split('\n'):
                line = line.strip()
                if line:
                    path, code = line.split(':', 1)
                    if '.template.' in path:
                        # skip jinja templates
                        continue
                    # each line looks like:
                    # 'src/pxr/base/lib/gf/wrapQuatd.cpp:    implicitly_convertible<GfQuatf, GfQuatd>();'
                    m = code_reg.search(code)
                    if m:
                        match = m.groupdict()
                        from_type = match['from']
                        to_type = match['to']
                        if to_type == 'This':
                            to_type = self.get_type_from_path(path)
                        if from_type == 'This':
                            from_type = self.get_type_from_path(path)
                        to_type = self.cpp_arg_to_py_type(to_type, is_arg=None)[0]
                        from_type = self.cpp_arg_to_py_type(from_type, is_arg=None)[0]
                        result[to_type].add(from_type)
                    elif self.verbose:
                        print("no match", line)
            self._implicitly_convertible_types = dict(result)
            # print(list(self._implicitly_convertible_types.keys()))
        return self._implicitly_convertible_types

    def add_implicit_unions(self, typestr: str) -> str:
        """
        wrap the type string in a Union[] if it is in the list of types with known
        implicit conversions.

        Parameters
        ----------
        typestr : str
            fully qualified python type identifier
        """
        others = self.get_implicitly_convertible_types().get(typestr)
        if others is not None:
            return ' | '.join([typestr] + sorted(others))
        else:
            return typestr

    def cpp_arg_to_py_type(self, typestr: str, is_arg: bool | None = True) -> tuple[str, bool]:
        """
        Convert a c++ type string to a python type string

        Returns the new typestring and whether the type appears to be a return value
        """
        orig = typestr
        parts = typestr.split()
        is_result = maybe_result(parts)

        # remove extraneous bits
        parts = [re.sub(STRIP, '', x) .replace('*', '').replace('&', '').strip() for x in parts]
        parts = [x for x in parts if not should_strip_part(x)]
        typestr = ''.join(parts)

        for pattern, replace in RENAMES:
            new_typestr = re.sub(pattern, replace, typestr)
            if new_typestr != typestr:
                return new_typestr, is_result

        for pattern, replace in TYPE_MAP:
            typestr = re.sub(pattern, replace, typestr)

        # swap container syntax
        typestr = typestr.replace('<', '[')
        typestr = typestr.replace('>', ']')
        # convert to python identifers
        parts = [(doc_info.to_python_id(x) or x) for x in re.split(IDENTIFIER, typestr)]

        # note: None is a valid value for is_arg
        if is_arg is True and not is_result:
            parts = [self.add_implicit_unions(x) for x in parts]

        typestr = ''.join(parts)
        typestr = typestr.replace(',', ', ')
        typestr = typestr.replace('::', '.')
        return typestr, is_result

    # def convert_default(self, valuestr: str ) -> str | None:
    #     for pattern, replace in DEFAULT_VAL_MAP:
    #         valuestr = re.sub(pattern, replace, valuestr)
    #     return self.convert_typestr(valuestr, is_arg=False)[0]


class DocInfo:
    """Get info from parsed doxygen docs"""

    def __init__(self, xml_index_file: str, pxr_modules):
        self.xml_index_file = xml_index_file
        self.pxr_modules_names = sorted(pxr_modules, key=len, reverse=True)
        self.cpp_sigs: dict[str, SigInfo] = {}
        # mapping of short names to full python paths
        self.py_types = defaultdict(list)

    def _populate_map(self, docElemPath: list[DocElement]) -> None:
        """
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
                    print(f"Found type {py_type} ({short_name})")
                    self.py_types[short_name].append(py_type)

        for childName, childObjectList in docElem.children.items():
            childElem = childObjectList[0]
            if childElem.isFunction():
                info = SigInfo(
                    parent=docElem,
                    overloads=childObjectList,
                )
                assert len(docElemPath) in (1, 2), childElem
                parents = docElemPath[1:]
                cppPath = '::'.join(x.name for x in parents + [childElem])
                self.cpp_sigs[cppPath] = info
 
            # recurse through all of this element's children
            for child in childObjectList:
                self._populate_map(docElemPath + [child])

    def populate(self):
        parser = Parser()
        parser.parseDoxygenIndexFile(self.xml_index_file)
        docElements = parser.traverse(DummyWriter())

        for docElement in docElements:
            self._populate_map([docElement])

    @staticmethod
    def strip_pxr_namespace(cpp_type_name):
        if cpp_type_name.startswith('pxr::'):
            cpp_type_name = cpp_type_name[len('pxr::'):]
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
                parts = cpp_type_name[len(mod):].split("::")
                parts = ["pxr", mod] + parts
                return  ".".join(parts)
        return None

    def split_module(self, typestr: str) -> list[str]:
        """
        split the c++ type into module name and object name
        """
        for mod in self.pxr_modules_names:
            if typestr.startswith(mod):
                s = typestr[len(mod):]
                if s and (s[0].isupper() or s[0] == '_'):
                    return [mod, s]
        return [typestr]

    # FIXME: reconcile this with the method above
    def to_python_id(self, cpp_type_name: str) -> str:
        cpp_type_name = self.strip_pxr_namespace(cpp_type_name)
        parts = self.split_module(cpp_type_name)
        if len(parts) == 1:
            return parts[0]
        else:
            mod = parts[0]
            name = parts[1]
            return f'pxr.{mod}.{name}'
    
    @staticmethod
    def py_to_cpp_func_paths(pypath: str) -> list[tuple[str, str]]:
        """
        Convert from python object path to cpp object path
        """
        parts = pypath.split(".")
        module = parts[1]
        # pxr.Sdf.Path.FindLongestPrefix -> 
        #   SdfPath::FindLongestPrefix
        #   SdfPathFindLongestPrefix
        remainder = parts[2:]
        if len(remainder) == 2:
            results = [
                ("method", 
                "{module}{cls}::{func}".format(module=module, cls=remainder[0], func=remainder[1])),
                ("func", 
                "{module}{cls}{func}".format(module=module, cls=remainder[0], func=remainder[1])),
            ]
        elif len(remainder) == 1:
            results = [
                ("func", 
                "{module}{func}".format(module=module, func=remainder[0])),
            ]
        else:
            # notifier.warn("Unexpected number of parts", "%s" % pypath)
            results = []
        return results

    def format_cpp_sig(self, doc_elem: DocElement):
        params = ", ".join([f"{p[1]}: {p[0]}" for p in doc_elem.params])
        return f"def {doc_elem.name}({params}) -> {doc_elem.returnType}: ..."

    def _lookup_sig_info(self, cpp_paths: list[tuple[str, str]]) -> SigInfo | None:
        for _, cpp_path in cpp_paths:
            try:
                data = self.cpp_sigs[cpp_path]
            except KeyError:
                pass
            else:
                return data
        return None
    
    def lookup_sig_info(self, pypath: str) -> SigInfo | None:
        "Get cpp signature info from a full python object path"
        return self._lookup_sig_info(self.py_to_cpp_func_paths(pypath))

    def get_full_py_type(self, short_type_name: str, current_module: str, fallback: str | None = None, current_func: str | None = None) -> str | None:
        """Get a full python object path from a short type name
        
        Returns None if the type was not found.
        """
        full_type_names = self.py_types.get(short_type_name)
        if not full_type_names:
            # Note: bool, int, list, etc end up here.
            return None  # fallback if fallback is not None else None
        if len(full_type_names) > 1:
            for full_type in full_type_names:
                if full_type.startswith(current_module + "."):
                    return full_type
            if fallback is not None and fallback in full_type_names:
                return fallback
            else:
                if current_func is None:
                    current_func = "<unknown_func>"
                notifier.warn("Ambiguous type loookup",
                              current_module,  
                              f"{current_func}: {short_type_name!r} -> {full_type_names} (fallback={fallback!r})")
                return None
        return full_type_names[0]


import pxr
modules = get_submodules(pxr.__path__)

notifier = Notifier()

doc_info = DocInfo(os.environ["USD_XML_INDEX"], modules)

src_info = SourceInfo(srcdir=os.environ["USD_SOURCE_ROOT"])

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
# - the stubs for Sdf.ValueTypeNames can be improved with some more work on stubgen

class UsdBoostDocstringSignatureGenerator(BoostDocstringSignatureGenerator, BaseSigFixer):

    def fix_self_arg(self, sig: FunctionSig, ctx: FunctionContext) -> FunctionSig:
        "boost erroneously adds a self arg to some methods: remove it"
        if (len(sig.args) >= 1 and ctx.class_info and 
                sig.args[0].name == "arg1" and not sig.args[0].default and
                sig.args[0].type in ("object", ctx.class_info.name)):
            return sig._replace(args=sig.args[1:])
        else:
            return sig

    def fix_self_args(self, sigs: list[FunctionSig], ctx: FunctionContext) -> list[FunctionSig]:
        return [self.fix_self_arg(sig, ctx) for sig in sigs]

    def cleanup_type(self, type_name: str, ctx: FunctionContext, is_result: bool, fallback = None) -> str:
        """
        Called by cleanup_sig_types.

        Apply fixes for known types/functions.
        """
        if ctx.name == "_GetStaticTfType" and is_result:
            return "pxr.Tf.Type"

        if is_result and type_name == "object":
            return "Any"
        
        # FIXME: we need to handle generics, like 'list[Attribute]'
        full_type = doc_info.get_full_py_type(type_name, ctx.module_name, fallback=fallback, current_func=ctx.fullname)
        if full_type is None and re.match("(Int|UInt|Bool|Vec|Short|Doublt|Half|Quat|Range|Rect|Char|Float|Token|Matrix).*Array$", type_name):
            return f"pxr.Vt.{type_name}"

        return full_type or type_name

    def infer_type(self, py_type: str | None, cpp_type: str, ctx: FunctionContext, is_result: bool = False) -> str | None:
        """
        Use multiple approaches to create a best guess at a python type name.

        py_type : python type inferred by boost
        cpp_type : c++ type scraped from the docs
        """
        converted_py_type = src_info.cpp_arg_to_py_type(cpp_type, is_arg=not is_result)[0]
        if py_type in ("object", "list"):
            # boost is reliable with most other types, such as int, bool, dict, tuple
            py_type = converted_py_type
        elif py_type is not None:
            py_type = self.cleanup_type(py_type, ctx, is_result, fallback=converted_py_type) or py_type           
        return py_type

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        sigs = super().get_function_sig(default_sig, ctx)
        if not sigs:
            return None

        def format_args(sig):
            return ', '.join(f"{arg.name}: {arg.type}" for arg in sig.args)

        if ctx.class_info is not None and ctx.name.startswith("__") and ctx.name.endswith("__"):
            # correct special methods which boost may have given bogus args or values
            args = infer_method_args(ctx.name, ctx.class_info.self_var)
            if all(arg.type is not None for arg in args[1:]):
                sigs = [sig._replace(args=args) for sig in sigs]
            ret_type = infer_method_ret_type(ctx.name)
            if ret_type is not None:
                sigs = [sig._replace(ret_type=ret_type) for sig in sigs]

        # def cpp_arg_names(cpp_sig: DocElement) -> tuple[int, list[str]]:
        #     return (len(cpp_sig.params), [p[1] for p in cpp_sig.params])
    
        def sig_sort_key(py_sig: FunctionSig) -> tuple[int, tuple[str, ...]]:
            return (len(py_sig.args), tuple([arg.name for arg in py_sig.args]))
    
        cpp_info = doc_info.lookup_sig_info(ctx.fullname)
        if cpp_info is None or len(sigs) != len(cpp_info.overloads):
            sigs = self.fix_self_args(sigs, ctx)
            sigs = [self.cleanup_sig_types(sig, ctx) for sig in sigs]
            if cpp_info is None:
                notifier.warn("No c++ info found", ctx.module_name, ctx.fullname)
            else:
                summary = ""
                for overload_num, sig in enumerate(sigs):
                    summary += "   py   ({})\n".format(format_args(sig))
                for overload_num, sig in enumerate(cpp_info.overloads):
                    summary += "   cpp  ({})\n".format(", ".join(f"{arg}: {type}" for type, arg in sig.params))

                notifier.warn(
                    "Number of overloads do not match",
                    ctx.module_name,
                    "(py {} != cpp {}): {}\n{}".format(len(sigs), len(cpp_info.overloads), ctx.fullname, summary))
        else:
            if not cpp_info.overloads[0].isStatic():
                sigs = self.fix_self_args(sigs, ctx)

            cpp_sigs_with_ptr: list[FunctionSig] = []
            for cpp_sig in cpp_info.overloads:
                cpp_sigs_with_ptr.append(
                    FunctionSig(ctx.name, 
                                [ArgSig(arg_name, arg_type) for arg_type, arg_name in cpp_sig.params],
                                cpp_sig.returnType))

            cpp_sigs_without_ptr: list[FunctionSig] = []
            for cpp_sig in cpp_info.overloads:
                # Fix pointer return types
                cpp_args: list[ArgSig] = []
                ptr_results = []
                for arg_type, arg_name in cpp_sig.params:
                    if "*" in arg_type:
                        # a pointer result
                        ptr_results.append((arg_type, arg_name))
                    else:
                        cpp_args.append(ArgSig(arg_name, arg_type))
                cpp_sigs_without_ptr.append(FunctionSig(ctx.name, cpp_args, cpp_sig.returnType))

            def matches(sigs1, sigs2):
                return sum(len(sig1.args) == len(sig2.args) for (sig1, sig2) in zip(sigs1, sigs2))

            # the order of overloads between boost and doxygen do not match. sort based on
            # the list of arg.
            sigs = sorted(sigs, key=sig_sort_key)
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
                    py_summary = "   py   ({})".format(format_args(py_sig))
                    cpp_summary = "   cpp  ({})".format(format_args(cpp_sig))
                    cpp_summary1 = " {} cpp! ({})".format(without_ptr_matches, format_args(cpp_sigs_without_ptr[overload_num]))
                    cpp_summary2 = " {} cpp* ({})".format(with_ptr_matches, format_args(cpp_sigs_with_ptr[overload_num]))
                    num_sigs = len(sigs)
                    curr_overload = overload_num + 1
                    notifier.warn("Sigs differ", 
                                  ctx.module_name,
                                  f"({curr_overload} of {num_sigs}): {ctx.fullname}\n{py_summary}\n{cpp_summary}\n{cpp_summary1}\n{cpp_summary2}")
                    sigs[overload_num] = self.cleanup_sig_types(py_sig, ctx)
                else:
                    args = []
                    for py_arg, cpp_arg in zip(py_sig.args, cpp_sig.args):
                        py_type = self.infer_type(py_arg.type, cpp_arg.type, ctx)
                        args.append(ArgSig(py_arg.name, py_type, py_arg.default))

                    return_type = self.infer_type(py_sig.ret_type, cpp_sig.ret_type, ctx, is_result=True)
                    if py_sig.ret_type == "list" and not return_type.startswith('list['):
                        # trust boost over the c++ docs in this case. it's probably a ptr result.
                        return_type = py_sig.ret_type
                        
                    sigs[overload_num] = FunctionSig(py_sig.name, args, return_type)

        # FIXME: remove dupes
        return sigs


def remove_redundant_submodule(module_name: str) -> str:
    """Convert 'pxr.Sdf._sdf' to 'pxr.Sdf'."""
    parts = module_name.rsplit('.', 1)
    if len(parts) == 2:
        base, sub = parts
        if sub.startswith('_'):
            return base
    return module_name


class CStubGenerator(mypy.stubgenc.CStubGenerator):
    """
    Make objects in pxr.Sdf._sdf appear to be defined in pxr.Sdf.

    The downside of this is that both pxr.Sdf._sdf and pxr.Sdf.__init__ are processed 
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module_name = remove_redundant_submodule(self.module_name)

    def get_obj_module(self, obj: object) -> str | None:
        """Return module name of the object."""
        module_name = getattr(obj, "__module__", None)
        if module_name:
            return remove_redundant_submodule(module_name)
        return None

    def get_type_fullname(self, typ: type) -> str:
        type_name = super().get_type_fullname(typ)
        # enums may leave out their parent class.  e.g. pxr.Usd.VersionPolicy should be pxr.Usd.SchemaRegistry.VersionPolicy
        if type_name.startswith("pxr.") and not is_existing_obj(type_name):
            full_type_name = doc_info.get_full_py_type(type_name.split(".")[-1], self.module_name)
            if full_type_name is not None:
                return full_type_name

        return type_name

    #     typename = getattr(typ, "__qualname__", typ.__name__)
    #     module_name = self.get_obj_module(typ)
    #     # FIXME: if the module is missing it's not guaranteed to be the current module
    #     if module_name is None:
    #         module_name = self.module_name

    #     if module_name != "builtins":
    #         typename = f"{module_name}.{typename}"
    #     return typename

    # def get_fullpath(self, obj: object) -> str | None:
    #     class_name = self.get_type_fullname()
    #     name = getattr(obj, "__qualname__", getattr(obj, "__name__", None))
    #     if name is None:
    #         return None
    #     module_name = self.get_obj_module(obj)
    #     # FIXME: if the module is missing it's not guaranteed to be the current module
    #     if module_name is None:
    #         module_name = self.module_name
    #     return f"{module_name}.{name}"

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [UsdBoostDocstringSignatureGenerator()]
    
    def is_classmethod(self, class_info: ClassInfo, name: str, obj: object) -> bool:
        # in boost python it is impossible to distinguish between classmethod and instance method
        # so we consult the docs
        sig_info = doc_info.lookup_sig_info(f"{self.module_name}.{class_info.name}.{name}")
        if sig_info:
            parent = sig_info.parent
            if parent.isClass():
                return any(d.isStatic() for d in sig_info.overloads)
            else:
                # this is a loose function that has been added as a staticmethod
                return True
        return False


mypy.stubgen.CStubGenerator = CStubGenerator
mypy.stubgenc.CStubGenerator = CStubGenerator

mypy.stubgen.NoParseStubGenerator = CStubGenerator
mypy.stubgenc.NoParseStubGenerator = CStubGenerator


# class NoParseStubGenerator(mypy.stubgenc.NoParseStubGenerator):
#     """
#     Make objects in pxr.Sdf appear to be defined in pxr.Sdf._sdf.
#
#     The downside of this approach is that types in the stubs are idenfified as pxr.Sdf._sdf.Foo
#     """

#     def get_obj_module(self, obj: object) -> str | None:
#         """Return module name of the object."""
#         module_name = getattr(obj, "__module__", None)
#         if module_name:
#             parts = module_name.split('.')
#             if len(parts) == 2:
#                 module_name = '.'.join(parts + ['_' + parts[-1].lower()])
#                 # print(obj, module_name)
#                 # print(self.known_modules)
#         return module_name


# class CStubGenerator(NoParseStubGenerator):
#     """
#     Make objects in pxr.Sdf appear to be defined in pxr.Sdf._sdf.
#     """

#     def get_sig_generators(self) -> list[SignatureGenerator]:
#         return [BoostDocstringSignatureGenerator()]

# mypy.stubgen.CStubGenerator = CStubGenerator
# mypy.stubgenc.CStubGenerator = CStubGenerator

# mypy.stubgen.NoParseStubGenerator = NoParseStubGenerator
# mypy.stubgenc.NoParseStubGenerator = NoParseStubGenerator

def test():
    assert src_info.cpp_arg_to_py_type('PCP_API SdfLayerHandleSet')[0] == 'list[pxr.Sdf.Layer]'
    assert src_info.cpp_arg_to_py_type('std::function<bool( UsdAttribute const&)>const&')[0] == "Callable[[pxr.Usd.Attribute], bool]"

def main(outdir):
    # test()
    # return
    # import pprint
    # assert src_info.srcdir is not None
    # pprint.pprint(src_info.get_implicitly_convertible_types())
    # return

    doc_info.populate()
    notifier.set_modules(["pxr.UsdUtils"])
    # raise ValueError(doc_info.py_types["PathArray"], doc_info.get_full_py_type("PathArray", "pxr.UsdGeom"))
    # raise ValueError(doc_info.py_types["VersionPolicy"], doc_info.get_full_py_type("VersionPolicy", "pxr.Usd"))
    # raise ValueError(doc_info.py_types["Matrix3dArray"], doc_info.get_full_py_type("Matrix3dArray", "pxr.Usd"))
    # raise ValueError(doc_info.py_types["Type"], doc_info.get_full_py_type("Type", "pxr.Usd"))

    stubgen_main(['-p', 'pxr', '--verbose', '--no-parse', f'-o={outdir}'])
    notifier.print_summary()

# real    2m10.416s
# user    4m9.176s
# sys     0m13.360s