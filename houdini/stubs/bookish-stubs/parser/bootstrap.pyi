import os
from bookish.parser import ParserContext as ParserContext, rules as r
from bookish.parser.rules import Rule as Rule
from bookish.util import find_object as find_object
from collections.abc import Mapping, MutableMapping
from types import ModuleType
from typing import Any, Self

def make_namespace(imports: Mapping[str, str], rules: MutableMapping[str, Rule], ns: dict[str, Any] | None = None, snap: bool = True) -> dict[str, Any]: ...

class Parser:
    imports: Mapping[str, str]
    rules: MutableMapping[str, Rule]
    namespace: dict[str, Any]
    main_rule: Rule
    def __init__(self, imports: Mapping[str, str], rules: MutableMapping[str, Rule], main: str = 'grammar', ns: dict[str, Any] | None = None) -> None: ...
    def context(self) -> ParserContext: ...
    def parse(self, stream: str, debug: bool = False, pos: int = 0) -> Any: ...
    def parse_parser(self, stream: str, debug: bool = False, pos: int = 0, main: str = 'grammar', ns: dict[str, Any] | None = None) -> Self: ...
    def as_python_source(self) -> str: ...
    def write_python_file(self, filepath: str | os.PathLike[str]) -> None: ...
    def as_module(self, name: str) -> ModuleType: ...

any_: r.Any
alphanum: r.AlphaNum
streamstart: r.StreamStart
linestart: r.LineStart
lineend: r.LineEnd
streamend: r.StreamEnd
blockbreak: r.BlockBreak
comment: r.Regex
hspace: r.Regex
hspaces: r.Star[str]
vspace: r.Regex
vspaces: r.Star[str]
ws: r.Star[str]
emptyline: r.Seq[str]
emptylines: r.Star[str]
indent: r.Seq[str]
noindent: r.Seq[type[r.Empty]]
digit: r.Among
hexdigit: r.Among
digits: r.Plus[str]
letters: r.Among
decnum: r.Seq
hexnum: r.Seq
barenum: r.Or
escchar: r.Seq
identifier: r.Regex
dqstring: r.Seq
sqstring: r.Seq
string: r.Seq
among: r.Seq
firsts: r.Seq
value: r.Seq
action1: r.Seq
action2: r.Seq
predicate1: r.Seq
predicate2: r.Seq
wall_: r.Seq
mixed: r.Seq
fail: r.Seq
extent: r.Seq
brackets: r.Seq
take: r.Seq
regex: r.Seq
arguments: r.Or
call: r.Seq
call2: r.Seq
atom: r.Or
expr1: r.Or
tildable: r.Or
repeattimes: r.Seq
repeatable: r.Seq
bindable: r.Seq
seqable: r.Seq
expr: r.Seq
dottedname: r.Take
import_: r.Seq
ruleend: r.Seq[list[str] | type[r.Empty]]
assignment: r.Seq
grammar: r.Seq

def make_rule_dict(localdict: Mapping[str, object]) -> dict[str, Rule]: ...

rule_dict: dict[str, Rule]
boot_parser: Parser

def boot_parse_grammar(filepath: str | os.PathLike[str], debug: bool = False, pos: int = 0, main: str = 'grammar', ns: dict[str, Any] | None = None) -> Parser: ...
def parse_grammar_file(filepath: str | os.PathLike[str], pos: int = 0, main: str = 'grammar', ns: dict[str, Any] | None = None) -> Parser: ...
def compile_grammar_file(inpath: str, outpath: str | None = None, pos: int = 0, main: str = 'grammar', ns: dict[str, Any] | None = None) -> None: ...
