from __future__ import absolute_import, annotations, division, print_function

import pathlib
import re

import mypy.stubgen
import mypy.stubgenc
from mypy.stubgen import FunctionContext, FunctionSig
from mypy.stubgenc import SignatureGenerator

import mari

from stubgenlib import DocstringTypeFixer, FixableDocstringSigGen

# the mari.so module patches in the Mari pure python package using __path__. Undo that
# so that mypy will just process mari.so as a single c extension.
mari.__path__ = []


class MariDocstringSignatureGenerator(DocstringTypeFixer, FixableDocstringSigGen):
    PYPATH = re.compile(r"((?:[a-zA-Z_][a-zA-Z0-9_]*)(?:[.][a-zA-Z_][a-zA-Z0-9_]*)*)")

    def prepare_docstring(self, docstr):
        # remove :obj: from docstring because it breaks the parser
        return re.sub(r":(?:[a-z_]+):", "", docstr).replace("`", "")

    def cleanup_type(
        self, type_name: str, ctx: FunctionContext, is_result: bool
    ) -> str:
        type_name = super().cleanup_type(type_name, ctx, is_result)
        if type_name == "int" and not is_result:
            # docstrings specify the type of enums as int, but they're not.
            # rather than try to keep track of which args are enums, we just
            # say all int are SupportsInt, which is probably accurate (need to test)
            return "typing.SupportsInt"

        parts = []
        for part in self.PYPATH.split(type_name):
            if (
                part
                and part[0].isalpha()
                and not part.startswith("mari.")
                and not part.startswith("PySide")
            ):
                if part[0] == "Q":
                    part = f"PySide2.QtWidgets.{part}"
                else:
                    part = f"mari.{part}"
            parts.append(part)
        return "".join(parts)


class CStubGenerator(mypy.stubgenc.CStubGenerator):
    """
    mari has a number of idiosyncracies wrt its module name, which have to be corrected.

    What we get:
    >>> mari.__name__
    'mari'
    >>> mari.AppVersion.__module__
    'mari.Mari'
    >>> mari.AppVersion.Stage.__module__
    'mari.Mari.AppVersion'
    >>> mari.AppVersion.Stage.__qualname__
    'Stage'
    >>> mari.Mari is mari
    True

    What we should get:
    >>> mari.__name__
    'mari'
    >>> mari.AppVersion.__module__
    'mari'
    >>> mari.AppVersion.Stage.__module__
    'mari'
    >>> mari.AppVersion.Stage.__qualname__
    'AppVersion.Stage'
    """

    def is_skipped_attribute(self, attr: str) -> bool:
        # skip the Mari object because it causes self.strip_or_import("mari.API") -> "Mari.API"
        # by adding a "mari" -> "Mari" alias lookup to import_tracker.reverse_alias
        return super().is_skipped_attribute(attr) or attr == "Mari"

    def get_obj_module(self, obj: object) -> str | None:
        """Return module name of the object."""
        module_name = getattr(obj, "__module__", None)

        if module_name and module_name.startswith("mari.Mari"):
            # convert invalid 'mari.Mari.AppVersion' to 'mari'
            return "mari"
        return module_name

    def get_type_fullname(self, typ: type) -> str:
        # mari C objects displace part of __qualname__ into __module__, so while
        # adding __module__ and __qualname__ produces the correct full type name,
        # if we use the *corrected* get_obj_module(), which the base class does,
        # it is not correct.
        typename = getattr(typ, "__qualname__", typ.__name__)
        module_name = typ.__module__.replace("mari.Mari", "mari")
        if module_name != "builtins":
            typename = f"{module_name}.{typename}"
        return typename

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [MariDocstringSignatureGenerator(default_sig_handling="merge")]

    def get_imports(self) -> str:
        output = super().get_imports()
        if self.module_name == "mari":
            output = "from . import current, session, system, utils\n" + output
        return output


mypy.stubgen.CStubGenerator = CStubGenerator  # type: ignore[attr-defined,misc]
mypy.stubgenc.CStubGenerator = CStubGenerator  # type: ignore[misc]


def main(outdir: str):
    import shutil
    out = pathlib.Path(outdir)
    # pure python package
    print("Converting Mari python package")
    mypy.stubgen.main(['-p=Mari', '--verbose', '--parse-only', '-o', outdir])

    dest = out.joinpath("mari")
    if dest.exists():
        shutil.rmtree(dest)
    src = out.joinpath("Mari")
    print()
    print("Renaming {} to {}".format(src, dest))
    src.rename(dest)
    print()

    # c module
    print("Converting mari.so c module")
    mypy.stubgen.main(['-m=mari', '--verbose', '-o', outdir])
    out.joinpath("mari.pyi").rename(dest.joinpath("__init__.pyi"))
