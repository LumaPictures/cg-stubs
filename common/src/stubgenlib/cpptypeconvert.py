from __future__ import absolute_import, annotations, division, print_function

import pathlib
import re
from functools import lru_cache
from typing import Iterator


class CppTypeConverter:
    IDENTIFIER = r"([a-zA-Z_][a-zA-Z0-9_]*)"
    TYPE_DEF_INCLUDES: list[str] = []

    STRIP = r"\b(?:const|friend|constexpr|class)\b"
    ARG_TYPE_MAP = [
        (r"\bstd::vector\b", "typing.Iterable"),
        (r"\bstd::set\b", "typing.Iterable"),
        (r"\bstd::unordered_set\b", "typing.Iterable"),
    ]
    RESULT_TYPE_MAP = [
        (r"\bstd::vector\b", "list"),
        (r"\bstd::set\b", "list"),
        (r"\bstd::unordered_set\b", "list"),
    ]
    TYPE_MAP = [
        (r"\bstd::string\b", "str"),
        (r"\bstd::map\b", "dict"),
        (r"\bstd::unordered_map\b", "dict"),
        (r"\bstd::unique_ptr\b", ""),
        (r"\bstd::ostream\b", "typing.TextIO"),
        (r"\bstring\b", "str"),
        (r"\bsize_t\b", "int"),
        (r"\bint64\b", "int"),
        (r"\bshort\b", "int"),
        (r"\bchar\b", "str"),
        # note that argname gets stripped. see stubgen_usd.test
        (
            r"\bstd::function\s*<\s*(?P<result>.+)\(\s*(?P<argtype>\w+)(?P<argname>.*)\)>",
            r"typing.Callable[[\g<argtype>], \g<result>]",
        ),
        (r"\bstd::pair\b", "tuple"),
        (r"\bdouble\b", "float"),
        (r"\bvoid\b", "None"),
    ]
    RENAMES: list[tuple[str, str]] = []

    def __init__(
        self,
        srcdir: str | None = None,
        verbose: bool = False,
    ) -> None:
        self.srcdir = srcdir
        self._typedefs: list[tuple[str, str]] | None = None
        self.verbose = verbose

        self._typedef_reg = re.compile(r"\btypedef ([^;]+);")
        self._using_reg = re.compile(
            r"\busing\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^;]+);"
        )

    def _get_typedefs(self) -> list[tuple[str, str]]:
        if not self.srcdir:
            return []

        if self._typedefs is None:
            self._typedefs = []

            srcdir = pathlib.Path(self.srcdir)
            for include_file in self.TYPE_DEF_INCLUDES:
                for alias, type in self._parse_typedefs(srcdir.joinpath(include_file)):
                    self._typedefs.append((alias, type))

        return self._typedefs

    def _parse_typedefs(self, include_file: pathlib.Path) -> Iterator[tuple[str, str]]:
        text = include_file.read_text().replace("\n", " ")
        for match in self._typedef_reg.finditer(text):
            typedef_str = match.group(1)
            type, alias = typedef_str.rsplit(" ", 1)
            alias = alias.replace(" ", "")
            type = type.strip()
            # fixup type.  kinda ugly, but it's easier to do it now before types are
            # full expanded
            if type.startswith("std::unordered_map<"):
                parts = type.split(",")
                if len(parts) == 3:
                    type = ",".join(parts[:-1]) + ">"
            yield alias, type
        for match in self._using_reg.finditer(text):
            alias = match.group(1).strip()
            type = match.group(2).strip()
            yield alias, type

    def _replace_typedefs(self, typestr: str) -> str:
        typedefs = self._get_typedefs()
        if not typedefs:
            return typestr

        def replace_typedefs(typ: str) -> str:
            for alias, replace in typedefs:
                typ = re.sub(rf"\b{alias}\b", replace, typ)
            return typ

        replacements = [typestr]
        while True:
            new_typestr = replace_typedefs(typestr)
            if new_typestr == typestr:
                break
            replacements.append(new_typestr)
            typestr = new_typestr
        if len(replacements) > 1:
            chain = "  >>  ".join(repr(r) for r in replacements)
            print(f"Typedef resolution: {chain}")
        return typestr

    @lru_cache
    def cpp_arg_to_py_type(self, cpp_type: str, is_result: bool) -> str:
        """
        Convert a c++ type string to a python type string

        Returns the new typestring and whether the type appears to be a return value
        """
        typestr = cpp_type
        is_ptr = "*" in typestr

        typestr = self._replace_typedefs(typestr)

        parts = typestr.split()

        # remove extraneous bits
        parts = [
            re.sub(self.STRIP, "", x).replace("*", "").replace("&", "").strip()
            for x in parts
        ]
        parts = [x for x in parts if not self.should_strip_part(x)]
        typestr = " ".join(parts)

        renames = dict(self.RENAMES)
        new_typestr = renames.get(typestr.replace(" ", ""))
        if new_typestr is not None:
            return new_typestr

        for pattern, replace in self.TYPE_MAP + (
            self.RESULT_TYPE_MAP if is_ptr or is_result else self.ARG_TYPE_MAP
        ):
            typestr = re.sub(pattern, replace, typestr)

        # swap container syntax
        typestr = typestr.replace("<", "[")
        typestr = typestr.replace(">", "]")

        # convert to python identifers
        parts = [x for x in re.split(self.IDENTIFIER, typestr) if x]
        parts = [(self.to_python_id(x) or x) for x in parts]

        typestr = "".join(parts)
        typestr = typestr.replace("::", ".")

        typestr = typestr.replace(" ", "")
        typestr = typestr.replace(",", ", ")

        if is_ptr:
            typestr = self.process_ptr(typestr, is_result)
        return typestr

    def process_ptr(self, converted_type: str, is_result: bool) -> str:
        return converted_type

    def to_python_id(self, cpp_type: str) -> str:
        return cpp_type

    def should_strip_part(self, x: str) -> bool:
        """
        whether the part looks like a c++ keyword
        """
        return not x
