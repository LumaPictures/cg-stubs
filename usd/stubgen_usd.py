from __future__ import absolute_import, annotations, division, print_function

import importlib
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
from mypy.stubgen import main as stubgen_main
from mypy.stubgenc import ArgSig
from mypy.stubgenc import \
    DocstringSignatureGenerator as CDocstringSignatureGenerator
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator

mypy.stubutil.NOT_IMPORTABLE_MODULES = ('pxr.Tf.testenv', 'pxr.Tf.testenv.testTfScriptModuleLoader_AAA_RaisesError')

from doxygenlib.cdParser import Parser
from doxygenlib.cdWriterDocstring import Writer
from doxygenlib.cdUtils import SetDebugMode

from stubgenlib import BaseSigFixer, BoostDocstringSignatureGenerator


SetDebugMode(False)

def get_submodules(pacakge_paths: list[str]) -> list[str]:
    """
    Given the name of a python mdoule, get a list of names of its child modules
    """
    import pkgutil
    return [loader.name for loader in pkgutil.iter_modules(pacakge_paths)]


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

    def warn(self, key, msg):
        #if (key, msg) not in self._seen_msgs:
        print(f"{key}: {msg}")
        self._seen_msgs[(key, msg)] += 1
        self._seen_keys[key] += 1

    def print_summary(self):
        print()
        print("Warning Summary:")
        for key in sorted(self._seen_keys):
            count = self._seen_keys[key]
            print(f"  {key}: {count}")


class DocInfo:
    def __init__(self, xml_index_file: str, pxr_modules):
        self.xml_index_file = xml_index_file
        self.pxr_modules_names = sorted(pxr_modules, key=len, reverse=True)
        self.cpp_sigs: dict[str: SigInfo] = {}
        # mapping of short names to full python paths
        self.py_types = defaultdict(list)

    def _get_py_type_name(self, cpp_type_name: str) -> str | None:
        for mod in self.pxr_modules_names:
            if cpp_type_name.startswith(mod):
                short_py_type = cpp_type_name[len(mod):]
                short_py_type = short_py_type.replace("::", ".")
                long_py_type = f"pxr.{mod}.{short_py_type}"
                return (short_py_type, long_py_type)
        return None

    def _populate_map(self, docElemPath: list[DocElement]) -> None:
        """
        docElemPath : list of DocElements from the root to the documented item
        """
        docElem = docElemPath[-1]

        if docElem.isClass():
            py_type = self._get_py_type_name(docElem.name)
            if py_type is not None:
                # short to long
                short_name, full_name = py_type
                if pydoc.locate(full_name):
                    print("Found type", full_name)
                    self.py_types[short_name].append(full_name)

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
 
            # recurse through all of this element's children too
            for child in childObjectList:
                self._populate_map(docElemPath + [child])

    def populate(self):
        parser = Parser()
        parser.parseDoxygenIndexFile(self.xml_index_file)
        docElements = parser.traverse(DummyWriter())

        for docElement in docElements:
            self._populate_map([docElement])

    @staticmethod
    def get_cpp_func_paths(pypath: str) -> list[tuple[str, str]]:
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
            notifier.warn("Unexpected number of parts", "%s" % pypath)
            results = []
        return results

    def _lookup_sig_info(self, cpp_paths: list[tuple[str, str]]) -> SigInfo | None:
        for _, cpp_path in cpp_paths:
            try:
                data = self.cpp_sigs[cpp_path]
            except KeyError:
                pass
            else:
                return data
        return None
    
    def format_cpp_sig(self, doc_elem: DocElement):
        params = ", ".join([f"{p[1]}: {p[0]}" for p in doc_elem.params])
        return f"def {doc_elem.name}({params}) -> {doc_elem.returnType}: ..."

    def lookup_sig_info(self, pypath: str) -> SigInfo | None:
        "Get cpp signature info from a full python object path"
        return self._lookup_sig_info(self.get_cpp_func_paths(pypath))

    def lookup_py_path(self, short_type_name: str, current_module: str) -> str | None:
        """Get a full python object path from a short type name
        
        Returns None if the type was not found.
        """
        full_type_names = doc_info.py_types.get(short_type_name)
        if not full_type_names:
            # Note: bool, int, list, etc end up here.
            # print(f"No type found for {short_type_name!r} (in {current_module})")
            return None
        if len(full_type_names) > 1:
            # FIXME: this would be best resolved by looking at the ccp sig info
            # favor the type in the current module
            for full_type in full_type_names:
                if full_type.startswith(current_module + "."):
                    return short_type_name
            notifier.warn("Ambiguous type loookup",  
                          f"{short_type_name!r} (in {current_module}) -> {full_type_names}")
            return None
        full_type_name = full_type_names[0]
        if full_type_name.startswith(current_module + "."):
            # the found type is in the current module.  use the short name
            return short_type_name
        else:
            return full_type_name


import pxr
modules = get_submodules(pxr.__path__)

notifier = Notifier()

doc_info = DocInfo(os.environ["USD_XML_INDEX"], modules)
doc_info.populate()

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
#   pxr.Sdf.CopySpec, pxr.Usd.TraverseInstanceProxies
        

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

    def cleanup_type(self, type_name: str, ctx: FunctionContext, is_result: bool) -> str:
        if is_result and type_name == "object":
            return "Any"
        new_type_name = doc_info.lookup_py_path(type_name, ctx.module_name)
        if new_type_name is None:
            # FIXME: type_name not found. this will likely require correction
            new_type_name = type_name
        return new_type_name

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        sigs = super().get_function_sig(default_sig, ctx)
        if not sigs:
            return None

        def cpp_arg_names(cpp_sig: DocElement) -> tuple[int, list[str]]:
            return (len(cpp_sig.params), [p[1] for p in cpp_sig.params])
    
        def py_arg_names(py_sig: FunctionSig) -> tuple[int, list[str]]:
            return (len(py_sig.args), [arg.name for arg in py_sig.args])
    
        cpp_info = doc_info.lookup_sig_info(ctx.fullname)
        if cpp_info is None:
            sigs = self.fix_self_args(sigs, ctx)
        elif len(sigs) != len(cpp_info.overloads):
            notifier.warn(
                "Number of overloads do not match",
                "(py {} != cpp {}): {}".format(len(sigs), len(cpp_info.overloads), ctx.fullname))
            sigs = self.fix_self_args(sigs, ctx)
        else:
            # the order of overloads between boost and doxygen do not match. sort based on
            # the list of arg
            sigs = sorted(sigs, key=py_arg_names)
            cpp_sigs = sorted(cpp_info.overloads, key=cpp_arg_names)

            for overload_num, (py_sig, cpp_sig) in enumerate(zip(sigs, cpp_sigs)):
                # boost erroneously adds a self arg to some methods: remove it
                if not cpp_sig.isStatic():
                    py_sig = self.fix_self_arg(py_sig, ctx)
                    sigs[overload_num] = py_sig
                
                # Fix pointer return types
                if len(py_sig.args) != len(cpp_sig.params):
                    cpp_params = []
                    ptr_results = []
                    for arg_type, arg_name in cpp_sig.params:
                        if "*" in arg_type:
                            # a pointer result
                            ptr_results.append((arg_type, arg_name))
                        else:
                            cpp_params.append((arg_type, arg_name))
                    if cpp_sig.returnType == "void" and py_sig.ret_type in ("object", "Any"):
                        # TODO: use ptr param as return type
                        pass
                    elif py_sig.ret_type == "tuple":
                        # TODO: add ptr params to the tuple return type
                        pass                                
                else:
                    cpp_params = cpp_sig.params
                    
                if len(py_sig.args) != len(cpp_params):
                    notifier.warn("Sigs differ", "(%d of %d): %s" % (overload_num + 1, len(sigs), ctx.fullname))
                    print("   ", [(arg.name, arg.type) for arg in py_sig.args])
                    print("   ", [(arg[1], arg[0]) for arg in cpp_sig.params])

                # if len(sig.args) == len(cpp_sig.params):
                    # for arg, cpp_arg in zip(sig.args, cpp_sig.params):
                    #     if arg.type == 'object':
                    #         print(ctx.fullname)
                    #         print(sigs)
                    #         print(cpp_sigs)
                    #         raise RuntimeError
                            # cpp_sigs
        sigs = [self.cleanup_sig_types(sig, ctx) for sig in sigs]
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

    # def get_type_fullname(self, typ: type) -> str:
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
        # in boost python, it is impossible to distinguish between classmethod and instance method
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

def main(outdir):
    stubgen_main(['-p', 'pxr', '--verbose', '--no-parse', f'-o={outdir}'])
    notifier.print_summary()
