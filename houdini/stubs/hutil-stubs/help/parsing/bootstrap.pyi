import pathlib
from . import rules as r
from types import ModuleType
from typing import Any, Self

class Parser:
    imports: dict[str, ModuleType | str]
    rules: r.NsDict
    namespace: r.NsDict
    main_rule: r.Rule
    def __init__(self, imports: dict[str, ModuleType | str], rules: r.NsDict, main: str = 'grammar') -> None: ...
    def parse(self, src: str, pos: int = 0) -> Any: ...
    def parse_parser(self, src: str, pos: int = 0, main: str = 'grammar') -> Self: ...
    def as_python_source(self) -> str: ...
    def write_python_file(self, filepath: pathlib.Path) -> None: ...
    def as_module(self, name: str) -> ModuleType: ...

any_: r.AnyChar
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
emptyline: r.Seq
emptylines: r.Star
indent: r.Seq
noindent: r.Seq
digit: r.Among
hexdigit: r.Among
digits: r.Plus[str]
letters: r.Among
decnum: r.Seq
hexnum: r.Seq
barenum: r.Or
number: r.Seq
escchar: r.Seq
identifier: r.Regex
dqstring: r.Seq
sqstring: r.Seq
string: r.Seq
among: r.Seq
firsts: r.Seq
value: r.Seq
action1: r.Seq
predicate1: r.Seq
predicate2: r.Seq
wall_: r.Seq
mixed: r.Seq
fail: r.Seq
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
ruleend: r.Seq
assignment: r.Seq
grammar: r.Seq

def boot_parser() -> Parser: ...
def boot_parse_grammar(filepath: pathlib.Path, pos: int = 0, main: str = 'grammar') -> Parser: ...
def parse_grammar_file(filepath: pathlib.Path, pos: int = 0, main: str = 'grammar') -> Parser: ...
def compile_grammar_file(inpath: pathlib.Path, outpath: pathlib.Path | None = None, pos: int = 0, main: str = 'grammar') -> None: ...
def rebuild() -> None: ...
