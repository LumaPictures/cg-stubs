from __future__ import absolute_import, annotations, division, print_function

import re
from typing import Any

import mypy.stubgen
import mypy.stubgenc
from mypy.stubgen import main
from mypy.stubgenc import DocstringSignatureGenerator as CDocstringSignatureGenerator
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator

import Callbacks.Callbacks
from Callbacks.Callbacks import _TypeEnum

from stubgenlib import (
    DocstringSignatureGenerator,
    CFunctionStub,
    BaseSigFixer,
    Notifier,
    DocstringTypeFixer,
)

notifier = Notifier()

# Remove these to troubleshoot errors:
DISABLED_CODES = '# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"\n\n'


class KatanaDocstringTypeFixer(DocstringTypeFixer):
    SPECIAL_REPLACEMENTS = [
        ('FnGeolib', 'PyFnGeolib'),
        ('FnAttribute', 'PyFnAttribute'),
        ('FnGeolibServices', 'PyFnGeolibServices'),
        ('FnGeolibProducers', 'PyFnGeolibProducers'),
        (
            r'PyFnGeolib.GeolibRuntime\.Transaction',
            'PyFnGeolib.GeolibRuntimeTransaction',
        ),
        (r'PyFnGeolib.GeolibRuntime\.Op', 'PyFnGeolib.GeolibRuntimeOp'),
        (r'NodegraphAPI\.LiveGroupMixin', 'NodegraphAPI.LiveGroup.LiveGroupMixin'),
    ]

    def get_replacements(self) -> list[tuple[str, str]]:
        return self.SPECIAL_REPLACEMENTS + self.REPLACEMENTS

    def get_full_name(self, type_name: str) -> str:
        # FIXME: would be nice to have something that can do a search through known objects
        absolute_names = (
            (
                'TerminalOpDelegate',
                'Nodes3DAPI.TerminalOpDelegates.TerminalOpDelegate.TerminalOpDelegate',
            ),
            ('Nodes?', 'NodegraphAPI.Node'),
            ('GroupNode', 'NodegraphAPI.GroupNode'),
            ('Port', 'NodegraphAPI.Port'),
            ('GraphState', 'NodegraphAPI.GraphState'),
            ('Op', 'PyFnGeolib.GeolibRuntimeOp'),
            ('WorkingSet', 'PyUtilModule.WorkingSet.WorkingSet'),
            ('PortOpClient', 'Nodes3DAPI.PortOpClient.PortOpClient'),
            ('GroupAttribute', 'PyFnAttribute.GroupAttribute'),
        )
        for short_name, full_name in absolute_names:
            type_name = re.sub(
                r'(?<![A-Za-z0-9._]){}\b'.format(short_name), full_name, type_name
            )
        return type_name


class KatanaDocstringSignatureGenerator(
    KatanaDocstringTypeFixer, DocstringSignatureGenerator
):
    pass


class KatanaCSignatureGenerator(
    CDocstringSignatureGenerator, KatanaDocstringTypeFixer, BaseSigFixer
):
    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        sigs = super().get_function_sig(default_sig, ctx)
        if sigs:
            sigs = [self.cleanup_sig_types(sig, ctx) for sig in sigs]
        if ctx.fullname == "NodegraphAPI_cmodule.Parameter.getValue":
            return [sig._replace(ret_type="Any") for sig in sigs]
        elif ctx.fullname == "NodegraphAPI_cmodule.GroupNode.getChild":
            return [sig._replace(ret_type="Node") for sig in sigs]
        elif ctx.fullname == "NodegraphAPI_cmodule.Port.getNode":
            return [sig._replace(ret_type="Node") for sig in sigs]
        return sigs


class NoParseStubGenerator(mypy.stubgenc.NoParseStubGenerator):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.known_modules.extend(['PyQt5.QtCore', 'PyQt5.QtWidgets'])

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [KatanaDocstringSignatureGenerator()]

    def is_defined_in_module(self, obj: object) -> bool:
        # _TypeEnum is a type, but it's created dynamically.  This change ensures
        # that we don't assume things of type _TypeEnum are external to their
        # current module and should thus be imported.
        return super().is_defined_in_module(obj) or type(obj).__name__ == '_TypeEnum'

    def strip_or_import(self, type_name: str) -> str:
        if re.match('^[A-Za-z0-9_.]+$', type_name):
            parts = type_name.split('.')
            # It's impossible to get access to members of certain modules without
            # changing the import style, because the modules are replaced with
            # objects of the same name
            if (len(parts) >= 2 and parts[-2] == parts[-1]) or (
                len(parts) >= 3 and parts[-3] == parts[-2]
            ):
                self.import_tracker.add_import_from(
                    '.'.join(parts[:-1]), [(parts[-1], None)]
                )
                self.import_tracker.require_name(parts[-1])
                return parts[-1]
        return super().strip_or_import(type_name)

    def get_imports(self) -> str:
        imports = super().get_imports()
        return DISABLED_CODES + imports

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        # Note that there is a mix of fixes here for C and non-C modules, but
        # I'm not separating them because it's easy to get mixed uppp
        members = dict(super().get_members(obj))

        if isinstance(obj, type) and obj.__name__ == 'CallbacksManager':
            enums = {
                x: _TypeEnum(x)
                for x in dir(Callbacks.Callbacks.Type)
                if not x.startswith('_')
            }
            enumType = type('_TypeEnumList', (), enums)
            enumType.__module__ = 'Callbacks.Callbacks'
            members['Type'] = enumType

        return list(members.items())


class CStubGenerator(mypy.stubgenc.CStubGenerator):
    DATA_ATTRS = {
        'DataAttribute': 'T',
        'DoubleAttribute': 'float',
        'FloatAttribute': 'float',
        'IntAttribute': 'int',
        'StringAttribute': 'str',
    }

    def get_sig_generators(self) -> list[SignatureGenerator]:
        # sig_gens = super().get_sig_generators()
        return [KatanaCSignatureGenerator()]

    def get_imports(self) -> str:
        if self.module_name == 'PyFnAttribute':
            self.add_typing_import('TypeVar')
            type_vars = 'T = TypeVar("T")\n'
        else:
            type_vars = ''
        imports = super().get_imports()
        return DISABLED_CODES + imports + type_vars

    def get_base_types(self, obj: type) -> list[str]:
        bases = super().get_base_types(obj)
        if obj.__name__ in self.DATA_ATTRS or obj.__name__ == 'ConstVector':
            sub_type = self.DATA_ATTRS.get(obj.__name__, 'T')
            if obj.__name__ in ['DataAttribute', 'ConstVector']:
                self.add_typing_import('Generic')
                return bases + [f'Generic[{sub_type}]']
            else:
                base = bases[0]
                return [f'{base}[{sub_type}]']
        else:
            return bases

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        members = dict(super().get_members(obj))

        def add(x):
            members[x.__name__] = x

        if isinstance(obj, type) and obj.__name__ in self.DATA_ATTRS:
            sub_type = self.DATA_ATTRS[obj.__name__]
            is_abstract = obj.__name__ == 'DataAttribute'
            # Add abstract methods that are shared by all sub-classes
            add(
                CFunctionStub(
                    "getValue",
                    f"getValue(self, defaultValue: {sub_type} = ..., throwOnError: bool = ...) -> {sub_type}",
                    is_abstract=is_abstract,
                )
            )
            add(
                CFunctionStub(
                    "getData",
                    f"getData(self) -> ConstVector[{sub_type}]",
                    is_abstract=is_abstract,
                )
            )
            add(
                CFunctionStub(
                    "getNearestSample",
                    f"getNearestSample(self, sampleTime: float) -> ConstVector[{sub_type}]",
                    is_abstract=is_abstract,
                )
            )
            add(
                CFunctionStub(
                    "getSamples",
                    f"getSamples(self) -> dict[float, ConstVector[{sub_type}]]",
                    is_abstract=is_abstract,
                )
            )
        elif isinstance(obj, type) and obj.__name__ == 'ConstVector':
            add(CFunctionStub("__iter__", "__iter__(self) -> typing.Iterator[T]"))
            add(
                CFunctionStub(
                    "__getitem__",
                    "__getitem__(self, arg0: int) -> T\n"
                    "__getitem__(self, arg0: slice) -> ConstVector[T]",
                )
            )

        return list(members.items())


mypy.stubgen.NoParseStubGenerator = NoParseStubGenerator
mypy.stubgenc.NoParseStubGenerator = NoParseStubGenerator

mypy.stubgen.CStubGenerator = CStubGenerator
mypy.stubgenc.CStubGenerator = CStubGenerator
