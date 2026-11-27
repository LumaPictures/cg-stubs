import os
from collections.abc import Mapping, MutableMapping
from types import ModuleType
from typing import Any, Self

from bookish.parser import ParserContext
from bookish.parser.rules import Rule

def make_namespace(
    imports: Mapping[str, str],
    rules: MutableMapping[str, Rule[Any]],
    ns: dict[str, Any] | None = ...,
    snap: bool = ...,
) -> dict[str, Any]: ...

class Parser:
    imports: Mapping[str, str]
    rules: MutableMapping[str, Rule[Any]]
    namespace: dict[str, Any]
    main_rule: Rule[Any]
    def __init__(
        self,
        imports: Mapping[str, str],
        rules: MutableMapping[str, Rule[Any]],
        main: str = ...,
        ns: dict[str, Any] | None = ...,
    ) -> None: ...
    def context(self) -> ParserContext: ...
    def parse(self, stream: str, debug: bool = ..., pos: int = ...) -> Any: ...
    def parse_parser(
        self,
        stream: str,
        debug: bool = ...,
        pos: int = ...,
        main: str = ...,
        ns: dict[str, Any] | None = ...,
    ) -> Self: ...
    def as_python_source(self) -> str: ...
    def write_python_file(self, filepath: str | os.PathLike[str]) -> None: ...
    def as_module(self, name: str) -> ModuleType: ...

def make_rule_dict(localdict: Mapping[str, object]) -> dict[str, Rule[Any]]: ...

rule_dict: dict[str, Rule[Any]]
boot_parser: Parser

def boot_parse_grammar(
    filepath: str | os.PathLike[str],
    debug: bool = ...,
    pos: int = ...,
    main: str = ...,
    ns: dict[str, Any] | None = ...,
) -> Parser: ...
def parse_grammar_file(
    filepath: str | os.PathLike[str],
    pos: int = ...,
    main: str = ...,
    ns: dict[str, Any] | None = ...,
) -> Parser: ...
def compile_grammar_file(
    inpath: str,
    outpath: str | None = ...,
    pos: int = ...,
    main: str = ...,
    ns: dict[str, Any] | None = ...,
) -> None: ...

from bookish.parser import rules as r

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
decnum: r.Seq[int]
hexnum: r.Seq[int]
barenum: r.Or[int]
escchar: r.Seq[str]
identifier: r.Regex
dqstring: r.Seq[str]
sqstring: r.Seq[str]
string: r.Seq[r.String]
among: r.Seq[r.Among]
firsts: r.Seq[r.FirstChars]
value: r.Seq[r.Do]
action1: r.Seq[r.Do]
action2: r.Seq[r.DoCode]
predicate1: r.Seq[r.If]
predicate2: r.Seq[r.IfCode]
wall_: r.Seq[r.Wall]
mixed: r.Seq[r.Mixed[Any]]
fail: r.Seq[r.FailIf]
extent: r.Seq[r.Extent[Any]]
brackets: r.Seq[r.Rule[Any]]
take: r.Seq[r.Take]
regex: r.Seq[r.Regex]
arguments: r.Or[list[str] | None | tuple[()]]
call: r.Seq[r.Call]
call2: r.Seq[r.Call2]
atom: r.Or[r.Rule[Any]]
expr1: r.Or[r.Rule[Any]]
tildable: r.Or[r.Rule[Any]]
repeattimes: r.Seq[tuple[int, int | None]]
repeatable: r.Seq[r.Rule[Any]]
bindable: r.Seq[r.Rule[Any]]
seqable: r.Seq[r.Rule[Any]]
expr: r.Seq[r.Rule[Any]]
dottedname: r.Take
import_: r.Seq[tuple[str, str]]
ruleend: r.Seq[list[str] | type[r.Empty]]
assignment: r.Seq[tuple[str, r.Rule[Any]]]
grammar: r.Seq[tuple[dict[str, str], dict[str, r.Rule[Any]]]]
