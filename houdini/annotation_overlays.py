"""Apply annotation overlays to Houdini's python sources.

Most of the python modules Houdini ships are unannotated.  Their annotations are kept in
`annotations/`, one partial stub per source file at the same relative path (e.g.
`annotations/pdg/node.pyi` for `pdg/node.py`).  An overlay only needs the definitions it
annotates.

Before stubgen runs, each overlay is merged into a copy of its source file:

- Functions and methods are matched by qualified name and parameter names, and take the
  overlay's annotations, replacing any in the source.  `@overload` variants in the overlay are
  added ahead of the implementation.
- Variables (`name: type`) annotate the matching assignment at module or class level, or are
  declared there if the source has none (e.g. instance attributes assigned in `__init__`).
  An instance attribute the source annotates in a method (`self.x: T = ...`) takes the
  overlay's type there too.
- A class's bare generic bases (`class Config(dict)`) take the type arguments the overlay's
  class gives them (`class Config(dict[str, Any])`), and a class the source does not make
  generic takes the `Generic[...]` base the overlay's class adds (`class MenuMapping(Generic[_V])`),
  or the type parameters it adds to the source's (`Generic[T, J]` for `Generic[T]`); a
  subscripted base takes the type arguments the overlay adds to it (`Base[T, J]` for `Base[T]`).
- A method an overlay class marks `@type_check_only` is declared in the source's class, which
  does not define it: a stub-only override, for a method a subclass inherits whose type
  depends on the subclass (`def __getitem__(self, key: str) -> Port` in a class whose base's
  `__getitem__` returns the wrapped object's), or for a member the source lacks (in `hou`,
  the methods `houpythonportion` adds).  The marker is dropped, and the declaration's body is
  `...` (with the overlay's comment on it, e.g. `...  # type: ignore[override]`).  A class
  marked `@type_check_only` in a class, or a public one at module level, is declared the same
  way, body and all; a private one at module level is a helper class (below), which keeps the
  marker.  Declarations go at the end of their class or module, in the overlay's order, with
  the comments above them.  In a stub, a declaration replaces the stub's member of that name.
  Declarations are deliberate additions, so they are never reported as stale.
- A function or method marked `@replace` replaces the signature of the source's definition of
  that name, whatever its parameters: it takes the overlay's parameters (names, order, kinds,
  defaults and `/`) and return type, and keeps the source's decorators and body (in a stub,
  its docstring).  `@replace` `@overload` variants replace it with those overloads, which in a
  stub each take the source's decorators and docstring.  This is for signatures the source
  gets wrong (in `hou`, those SideFX's docs get wrong).  Unlike a declaration, a `@replace`
  entry whose definition is gone from the source is reported.
- TypeVars, type aliases and private helper classes (TypedDicts, Protocols) at module level
  are copied ahead of the source's code; a helper class only if the source has no class of
  that name (otherwise it annotates that class's members).
- The overlay's imports are added to the source, so its annotations resolve.

Anything in an overlay that does not match the source is reported, so overlays that have gone
stale with a new Houdini version are found.
"""

from __future__ import annotations

import dataclasses
import pathlib
from typing import Sequence

import libcst as cst

HERE = pathlib.Path(__file__).parent
OVERLAYS_DIR = HERE / "annotations"


def overlay_path(source_rel: str) -> pathlib.Path:
    """The overlay for a source file, given its path relative to the libs directory."""
    return OVERLAYS_DIR / pathlib.Path(source_rel).with_suffix(".pyi")


def param_names(params: cst.Parameters) -> tuple[str, ...]:
    names = [p.name.value for p in (*params.posonly_params, *params.params)]
    if isinstance(params.star_arg, cst.Param):
        names.append("*" + params.star_arg.name.value)
    names.extend(p.name.value for p in params.kwonly_params)
    if params.star_kwarg is not None:
        names.append("**" + params.star_kwarg.name.value)
    return tuple(names)


def all_params(params: cst.Parameters) -> list[cst.Param]:
    result = [*params.posonly_params, *params.params]
    if isinstance(params.star_arg, cst.Param):
        result.append(params.star_arg)
    result.extend(params.kwonly_params)
    if params.star_kwarg is not None:
        result.append(params.star_kwarg)
    return result


def is_overload(func: cst.FunctionDef) -> bool:
    for decorator in func.decorators:
        expr = decorator.decorator
        name = expr.attr.value if isinstance(expr, cst.Attribute) else getattr(expr, "value", None)
        if name == "overload":
            return True
    return False


def is_type_check_only(decorator: cst.Decorator) -> bool:
    expr = decorator.decorator
    name = expr.attr.value if isinstance(expr, cst.Attribute) else getattr(expr, "value", None)
    return name == "type_check_only"


def is_replace(decorator: cst.Decorator) -> bool:
    expr = decorator.decorator
    return isinstance(expr, cst.Name) and expr.value == "replace"


def is_declaration(statement: cst.CSTNode, scope: Sequence[str]) -> bool:
    """Whether an overlay statement is a `@type_check_only` member to declare in its scope.

    A private class at module level marked `@type_check_only` is a stub-only helper class
    instead (see `Overlay.preamble`), and keeps its marker.
    """
    if isinstance(statement, cst.FunctionDef):
        declared_here = bool(scope)
    elif isinstance(statement, cst.ClassDef):
        declared_here = bool(scope) or not statement.name.value.startswith("_")
    else:
        return False
    return declared_here and any(map(is_type_check_only, statement.decorators))


def is_type_alias(statement: cst.AnnAssign) -> bool:
    annotation = statement.annotation.annotation
    name = annotation.attr.value if isinstance(annotation, cst.Attribute) else getattr(annotation, "value", None)
    return name == "TypeAlias"


@dataclasses.dataclass
class Overlay:
    imports: list[cst.SimpleStatementLine]
    functions: dict[str, list[cst.FunctionDef]]
    overloads: dict[str, list[cst.FunctionDef]]
    variables: dict[str, cst.Annotation]
    # Class-level type aliases (`TreeView: TypeAlias = _QtTreeView`), by qualified name.
    class_aliases: dict[str, cst.AnnAssign] = dataclasses.field(default_factory=dict)
    # Public module-level classes, which replace a functional definition of the same name in
    # the source (`Event = namedtuple("Event", "id index")`, `Data = TypedDict("Data", {...})`).
    classes: dict[str, cst.ClassDef] = dataclasses.field(default_factory=dict)
    # Module-level definitions the annotations rely on, copied into the source in order:
    # TypeVars, ParamSpecs, type aliases, and private helper classes (TypedDicts, Protocols).
    # A helper class is only copied if the source has no class of that name.
    preamble: list[tuple[str | None, cst.BaseStatement]] = dataclasses.field(default_factory=list)
    # The bases of every class the overlay declares, by qualified name.
    class_bases: dict[str, Sequence[cst.Arg]] = dataclasses.field(default_factory=dict)
    # Members (`@type_check_only` methods and classes) to declare, by the qualified name of their
    # class ("" for the module).
    declared: dict[str, list[cst.FunctionDef | cst.ClassDef]] = dataclasses.field(
        default_factory=dict
    )
    # `@replace` signatures (one, or `@overload` variants), by qualified name.
    replacements: dict[str, list[cst.FunctionDef]] = dataclasses.field(default_factory=dict)

    @classmethod
    def parse(cls, text: str) -> Overlay:
        module = cst.parse_module(text)
        overlay = cls([], {}, {}, {})
        overlay._collect(module.body, [])
        return overlay

    def _collect(self, body: Sequence[cst.CSTNode], scope: list[str]) -> None:
        for statement in body:
            if isinstance(statement, cst.SimpleStatementLine):
                for small in statement.body:
                    if isinstance(small, (cst.Import, cst.ImportFrom)) and not scope:
                        self.imports.append(statement)
                        break
                    if not scope and (
                        isinstance(small, (cst.Assign, cst.TypeAlias))
                        or (isinstance(small, cst.AnnAssign) and is_type_alias(small))
                    ):
                        self.preamble.append((None, statement))
                        break
                    if isinstance(small, cst.AnnAssign) and isinstance(small.target, cst.Name):
                        qualname = ".".join([*scope, small.target.value])
                        self.variables[qualname] = small.annotation
                        if is_type_alias(small) and small.value is not None:
                            self.class_aliases[qualname] = small
                continue
            if is_declaration(statement, scope):
                assert isinstance(statement, (cst.FunctionDef, cst.ClassDef))
                self.declared.setdefault(".".join(scope), []).append(statement)
                continue
            if isinstance(statement, cst.ClassDef):
                self.class_bases[".".join([*scope, statement.name.value])] = statement.bases
            if (
                isinstance(statement, cst.ClassDef)
                and not scope
                and statement.name.value.startswith("_")
                and not statement.name.value.startswith("__")
            ):
                self.preamble.append((statement.name.value, statement))
                # Its members still annotate a source class of the same name, if there is one.
                if isinstance(statement.body, cst.IndentedBlock):
                    self._collect(statement.body.body, [statement.name.value])
            elif isinstance(statement, cst.FunctionDef) and any(map(is_replace, statement.decorators)):
                qualname = ".".join([*scope, statement.name.value])
                variants = self.replacements.setdefault(qualname, [])
                variants.append(statement)
                if len(variants) > 1 and not all(map(is_overload, variants)):
                    raise ValueError(f"@replace def {qualname}: several, but not all @overload")
            elif isinstance(statement, cst.FunctionDef):
                qualname = ".".join([*scope, statement.name.value])
                target = self.overloads if is_overload(statement) else self.functions
                target.setdefault(qualname, []).append(statement)
            elif isinstance(statement, cst.ClassDef):
                if not scope:
                    self.classes[statement.name.value] = statement
                body = statement.body
                if isinstance(body, cst.IndentedBlock):
                    self._collect(body.body, [*scope, statement.name.value])
            elif isinstance(statement, (cst.If, cst.Try)):
                self._collect(statement.body.body, scope)


@dataclasses.dataclass
class MergeResult:
    code: str
    # Overlay definitions that matched nothing in the source.
    unmatched: list[str]


def annotate_params(source: cst.Parameters, overlay: cst.Parameters) -> cst.Parameters:
    annotations = {p.name.value: p.annotation for p in all_params(overlay)}

    def update(param: cst.Param) -> cst.Param:
        annotation = annotations.get(param.name.value)
        return param.with_changes(annotation=annotation) if annotation else param

    star_arg = source.star_arg
    if isinstance(star_arg, cst.Param):
        star_arg = update(star_arg)
    return source.with_changes(
        posonly_params=[update(p) for p in source.posonly_params],
        params=[update(p) for p in source.params],
        star_arg=star_arg,
        kwonly_params=[update(p) for p in source.kwonly_params],
        star_kwarg=update(source.star_kwarg) if source.star_kwarg else None,
    )


def as_typing_overload(func: cst.FunctionDef) -> cst.FunctionDef:
    """An overlay `@overload` variant, as a definition that can go in the source."""
    decorators = [d for d in func.decorators if not _is_overload_decorator(d)]
    overload = cst.Decorator(cst.Attribute(cst.Name("typing"), cst.Name("overload")))
    body = cst.SimpleStatementSuite([cst.Expr(cst.Ellipsis())])
    return func.with_changes(decorators=[overload, *decorators], body=body)


def stub_only_declaration(
    node: cst.FunctionDef | cst.ClassDef,
) -> cst.FunctionDef | cst.ClassDef:
    """An overlay `@type_check_only` method or class, as a declaration that can go in the source."""
    decorators = [d for d in node.decorators if not is_type_check_only(d)]
    if isinstance(node, cst.ClassDef) or is_ellipsis_body(node.body):
        # A `...` body keeps its comment (`...  # type: ignore[override]`).
        return node.with_changes(decorators=decorators)
    body = cst.SimpleStatementSuite([cst.Expr(cst.Ellipsis())])
    return node.with_changes(decorators=decorators, body=body)


def is_ellipsis_body(body: cst.BaseSuite) -> bool:
    return (
        isinstance(body, cst.SimpleStatementSuite)
        and len(body.body) == 1
        and isinstance(body.body[0], cst.Expr)
        and isinstance(body.body[0].value, cst.Ellipsis)
    )


def declared_key(statement: cst.CSTNode) -> tuple[bool, str] | None:
    """What a declaration of a member replaces: (whether it is a class, its name)."""
    if isinstance(statement, (cst.FunctionDef, cst.ClassDef)):
        return isinstance(statement, cst.ClassDef), statement.name.value
    return None


def _is_overload_decorator(decorator: cst.Decorator) -> bool:
    expr = decorator.decorator
    name = expr.attr.value if isinstance(expr, cst.Attribute) else getattr(expr, "value", None)
    return name == "overload"


def declaration(
    name: str, annotation: cst.Annotation, alias: cst.AnnAssign | None = None
) -> cst.SimpleStatementLine:
    if alias is not None:
        return cst.SimpleStatementLine([alias])
    return cst.SimpleStatementLine(
        [cst.AnnAssign(target=cst.Name(name), annotation=annotation, value=None)]
    )


def imports_typing(statement: cst.CSTNode) -> bool:
    """Whether a statement is `import typing`."""
    return (
        isinstance(statement, cst.SimpleStatementLine)
        and isinstance(statement.body[0], cst.Import)
        and any(
            alias.asname is None and cst.Module([]).code_for_node(alias.name) == "typing"
            for alias in statement.body[0].names
        )
    )


def defined_name(statement: cst.CSTNode) -> str | None:
    """The name a module-level assignment or type alias statement defines, if any."""
    if not isinstance(statement, cst.SimpleStatementLine) or len(statement.body) != 1:
        return None
    small = statement.body[0]
    if isinstance(small, cst.Assign) and len(small.targets) == 1:
        target = small.targets[0].target
    elif isinstance(small, cst.AnnAssign):
        target = small.target
    elif isinstance(small, cst.TypeAlias):
        target = small.name
    else:
        return None
    return target.value if isinstance(target, cst.Name) else None


def insert_after_docstring(
    body: Sequence[cst.BaseStatement], statements: Sequence[cst.BaseStatement]
) -> list[cst.BaseStatement]:
    """Insert statements after a leading docstring and `from __future__` imports."""
    index = 0
    for index, statement in enumerate(body):  # noqa: B007
        if not isinstance(statement, cst.SimpleStatementLine):
            break
        small = statement.body[0]
        is_docstring = index == 0 and isinstance(small, cst.Expr) and isinstance(
            small.value, (cst.SimpleString, cst.ConcatenatedString)
        )
        is_future = isinstance(small, cst.ImportFrom) and isinstance(
            small.module, cst.Name
        ) and small.module.value == "__future__"
        if not (is_docstring or is_future):
            break
    else:
        index = len(body)
    return [*body[:index], *statements, *body[index:]]


def with_source_defaults(overlay_class: cst.ClassDef, call: cst.Call) -> cst.ClassDef:
    """Give an overlay's NamedTuple the field defaults of the namedtuple call it replaces.

    The overlay writes them as `= ...`, which is not a valid default in the merged source.
    """
    defaults = next(
        (arg.value for arg in call.args if arg.keyword and arg.keyword.value == "defaults"), None
    )
    if not isinstance(defaults, (cst.Tuple, cst.List)) or not isinstance(
        overlay_class.body, cst.IndentedBlock
    ):
        return overlay_class
    values = [element.value for element in defaults.elements]
    fields = [
        statement
        for statement in overlay_class.body.body
        if isinstance(statement, cst.SimpleStatementLine)
        and isinstance(statement.body[0], cst.AnnAssign)
    ]
    if len(values) > len(fields):
        return overlay_class
    replacements: dict[cst.SimpleStatementLine, cst.SimpleStatementLine] = {}
    for field, value in zip(fields[len(fields) - len(values) :], values):
        ann_assign = field.body[0]
        assert isinstance(ann_assign, cst.AnnAssign)
        if isinstance(ann_assign.value, cst.Ellipsis):
            replacements[field] = field.with_changes(
                body=[ann_assign.with_changes(value=value), *field.body[1:]]
            )
    body = [replacements.get(statement, statement) for statement in overlay_class.body.body]
    return overlay_class.with_changes(body=overlay_class.body.with_changes(body=body))


def is_generic_base(arg: cst.Arg) -> bool:
    value = arg.value
    return isinstance(value, cst.Subscript) and cst.Module([]).code_for_node(value.value) in (
        "Generic",
        "typing.Generic",
    )


def extends_subscript(source: cst.BaseExpression, overlay: cst.BaseExpression) -> bool:
    """Whether the overlay's base is the source's with type arguments added (`Generic[T, J]`
    for `Generic[T]`, `Base[T, J]` for `Base[T]`)."""
    if not isinstance(source, cst.Subscript) or not isinstance(overlay, cst.Subscript):
        return False
    code = cst.Module([]).code_for_node
    source_params = [code(element.slice) for element in source.slice]
    overlay_params = [code(element.slice) for element in overlay.slice]
    return (
        code(source.value) == code(overlay.value)
        and len(overlay_params) > len(source_params)
        and overlay_params[: len(source_params)] == source_params
    )


def refined_bases(source: Sequence[cst.Arg], overlay: Sequence[cst.Arg]) -> list[cst.Arg]:
    """The source's bases, with the type arguments the overlay gives its bare generic ones.

    Only a base the source leaves bare (`dict`, `qmlviews.SharedState`) and the overlay writes
    the same but subscripted (`dict[str, Any]`) is replaced: overlays often spell a base
    differently (`PySide6.QtWidgets.QWidget` for `QtWidgets.QWidget`), and those are left alone.
    A base the overlay writes with type arguments added to the source's (`Base[T, J]` for
    `Base[T]`) replaces it too.  A `Generic[...]` base the overlay gives a class whose source
    has none is added after the source's bases (dropping an explicit `object`, which would
    make the MRO inconsistent), and one that adds type parameters to the source's
    (`Generic[T, J]` for `Generic[T]`) replaces it.
    """
    source_generic = [arg for arg in source if is_generic_base(arg)]
    overlay_generic = [arg for arg in overlay if is_generic_base(arg)]
    added: list[cst.Arg] = []
    if not source_generic:
        added = overlay_generic
        overlay = [arg for arg in overlay if not is_generic_base(arg)]
    elif (
        len(source_generic) == 1
        and len(overlay_generic) == 1
        and extends_subscript(source_generic[0].value, overlay_generic[0].value)
    ):
        extended = source_generic[0].with_changes(value=overlay_generic[0].value)
        source = [extended if arg is source_generic[0] else arg for arg in source]
        overlay = [source_generic[0] if arg is overlay_generic[0] else arg for arg in overlay]
    code = cst.Module([]).code_for_node
    if added:
        # `class C(object, Generic[T])` has no consistent MRO, and `object` is implied anyway.
        source = [arg for arg in source if code(arg.value) != "object"]
        overlay = [arg for arg in overlay if code(arg.value) != "object"]
    if len(source) != len(overlay):
        return [*source, *added]
    return [
        *(
            source_arg.with_changes(value=overlay_arg.value)
            if source_arg.keyword is None
            and overlay_arg.keyword is None
            and (
                not isinstance(source_arg.value, cst.Subscript)
                and isinstance(overlay_arg.value, cst.Subscript)
                and code(overlay_arg.value.value) == code(source_arg.value)
                or extends_subscript(source_arg.value, overlay_arg.value)
            )
            else source_arg
            for source_arg, overlay_arg in zip(source, overlay)
        ),
        *added,
    ]


class OverlayTransformer(cst.CSTTransformer):
    def __init__(self, overlay: Overlay, stub: bool = False) -> None:
        super().__init__()
        self.overlay = overlay
        self.stub = stub
        self.scope: list[str] = []
        self.function_depth = 0
        self.method_name: str | None = None
        self.matched_functions: set[str] = set()
        self.matched_variables: set[str] = set()
        # Members declared, by qualified name, and those the source defines itself.
        self.declared: set[str] = set()
        self.declared_conflicts: set[str] = set()
        # The definitions `@replace` replaced, by qualified name.
        self.replaced: set[str] = set()
        self.uses_overloads = False
        self.replaces_with_overloads = False
        self.source_classes: set[str] = set()
        self.replaced_classes: set[str] = set()
        # The class-level variables annotated in each enclosing class.  A class the source
        # defines more than once (in the branches of an `if`) is annotated each time.
        self.class_matched: list[set[str]] = []

    def qualname(self, name: str) -> str:
        return ".".join([*self.scope, name])

    def visit_ClassDef(self, node: cst.ClassDef) -> bool:
        if not self.scope and not self.function_depth:
            self.source_classes.add(node.name.value)
        self.scope.append(node.name.value)
        self.class_matched.append(set())
        return True

    def leave_ClassDef(
        self, original_node: cst.ClassDef, updated_node: cst.ClassDef
    ) -> cst.ClassDef:
        qualname = ".".join(self.scope)
        self.scope.pop()
        matched_here = self.class_matched.pop()
        if self.function_depth or not isinstance(updated_node.body, cst.IndentedBlock):
            return updated_node
        overlay_bases = self.overlay.class_bases.get(qualname)
        if overlay_bases:
            updated_node = updated_node.with_changes(
                bases=refined_bases(updated_node.bases, overlay_bases)
            )
        prefix = qualname + "."
        declared_here = self.overlay.declared.get(qualname, [])
        if declared_here:
            block = updated_node.body
            assert isinstance(block, cst.IndentedBlock)
            updated_node = updated_node.with_changes(
                body=block.with_changes(body=self._declare(prefix, block.body, declared_here))
            )
        missing = [
            declaration(
                name.removeprefix(prefix), annotation, self.overlay.class_aliases.get(name)
            )
            for name, annotation in self.overlay.variables.items()
            if name.startswith(prefix)
            and "." not in name.removeprefix(prefix)
            and name not in matched_here
        ]
        if not missing:
            return updated_node
        self.matched_variables.update(prefix + m.body[0].target.value for m in missing)  # type: ignore[attr-defined]
        body = insert_after_docstring(updated_node.body.body, missing)
        return updated_node.with_changes(body=updated_node.body.with_changes(body=body))

    def _declare(
        self,
        prefix: str,
        body: Sequence[cst.BaseStatement],
        declarations: Sequence[cst.FunctionDef | cst.ClassDef],
    ) -> list[cst.BaseStatement]:
        """A class's or module's body, with the overlay's declarations for it at the end."""
        defined = {key for statement in body if (key := declared_key(statement))}
        keys = {declared_key(node) for node in declarations}
        if self.stub:
            # A generated stub already has the declarations an earlier merge added: replace them,
            # so that merging is idempotent.
            body = [statement for statement in body if declared_key(statement) not in keys]
            defined -= keys
        added = []
        for node in declarations:
            if declared_key(node) in defined:
                self.declared_conflicts.add(prefix + node.name.value)
            else:
                self.declared.add(prefix + node.name.value)
                added.append(stub_only_declaration(node))
        return [*body, *added]

    def visit_FunctionDef(self, node: cst.FunctionDef) -> bool:
        self.function_depth += 1
        if self.function_depth == 1:
            self.method_name = node.name.value
        return True

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef | cst.FlattenSentinel[cst.BaseStatement] | cst.RemovalSentinel:
        self.function_depth -= 1
        if self.function_depth:
            return updated_node
        qualname = self.qualname(updated_node.name.value)
        replacement = self.overlay.replacements.get(qualname)
        if replacement is not None:
            return self._replace(qualname, updated_node, replacement)
        names = param_names(updated_node.params)
        for candidate in self.overlay.functions.get(qualname, []):
            if param_names(candidate.params) == names:
                self.matched_functions.add(qualname)
                updated_node = updated_node.with_changes(
                    params=annotate_params(updated_node.params, candidate.params),
                    returns=candidate.returns or updated_node.returns,
                )
                break
        overloads = self.overlay.overloads.get(qualname)
        if overloads and "@" + qualname not in self.matched_functions:
            self.matched_functions.add("@" + qualname)
            self.uses_overloads = True
            variants = [*map(as_typing_overload, overloads)]
            # A stub can't have an implementation after its overloads: they replace it.
            return cst.FlattenSentinel(variants if self.stub else [*variants, updated_node])
        if overloads and self.stub:
            # The stub's other definitions of the name (its own overloads) are replaced too.
            return cst.RemoveFromParent()
        return updated_node

    def _replace(
        self, qualname: str, node: cst.FunctionDef, replacement: Sequence[cst.FunctionDef]
    ) -> cst.FunctionDef | cst.FlattenSentinel[cst.BaseStatement] | cst.RemovalSentinel:
        """Give a definition the signature of its `@replace` overlay entry."""
        if qualname in self.replaced:
            # The source's other definitions of the name (its overloads) are replaced too.
            return cst.RemoveFromParent()
        self.replaced.add(qualname)
        if not is_overload(replacement[0]):
            return node.with_changes(params=replacement[0].params, returns=replacement[0].returns)
        self.replaces_with_overloads = True
        overload = cst.Decorator(cst.Attribute(cst.Name("typing"), cst.Name("overload")))
        decorators = [overload, *(d for d in node.decorators if not _is_overload_decorator(d))]
        body = node.body if self.stub else cst.SimpleStatementSuite([cst.Expr(cst.Ellipsis())])
        variants = [
            node.with_changes(
                params=func.params,
                returns=func.returns,
                decorators=decorators,
                body=body,
                leading_lines=node.leading_lines if i == 0 else (),
            )
            for i, func in enumerate(replacement)
        ]
        return cst.FlattenSentinel(variants if self.stub else [*variants, node])

    def leave_SimpleStatementLine(
        self, original_node: cst.SimpleStatementLine, updated_node: cst.SimpleStatementLine
    ) -> cst.BaseStatement:
        """Replace a functional class definition with the overlay's class of that name."""
        if self.scope or self.function_depth or len(updated_node.body) != 1:
            return updated_node
        small = updated_node.body[0]
        if not (
            isinstance(small, cst.Assign)
            and len(small.targets) == 1
            and isinstance(small.targets[0].target, cst.Name)
            and isinstance(small.value, cst.Call)
        ):
            return updated_node
        name = small.targets[0].target.value
        overlay_class = self.overlay.classes.get(name)
        if overlay_class is None or name in self.source_classes or name in self.replaced_classes:
            return updated_node
        self.replaced_classes.add(name)
        prefix = name + "."
        self.matched_functions.update(n for n in self.overlay.functions if n.startswith(prefix))
        self.matched_functions.update(
            "@" + n for n in self.overlay.overloads if n.startswith(prefix)
        )
        self.replaced.update(n for n in self.overlay.replacements if n.startswith(prefix))
        self.matched_variables.update(n for n in self.overlay.variables if n.startswith(prefix))
        return with_source_defaults(overlay_class, small.value)

    def _matched_in_scope(self) -> set[str]:
        return self.class_matched[-1] if self.scope else self.matched_variables

    def _annotation_for(self, target: cst.BaseExpression) -> tuple[str, cst.Annotation] | None:
        if self.function_depth or not isinstance(target, cst.Name):
            return None
        qualname = self.qualname(target.value)
        annotation = self.overlay.variables.get(qualname)
        return (qualname, annotation) if annotation else None

    def leave_Assign(
        self, original_node: cst.Assign, updated_node: cst.Assign
    ) -> cst.Assign | cst.AnnAssign:
        if len(updated_node.targets) != 1:
            return updated_node
        found = self._annotation_for(updated_node.targets[0].target)
        if not found or found[0] in self._matched_in_scope():
            return updated_node
        self.matched_variables.add(found[0])
        if self.scope:
            self.class_matched[-1].add(found[0])
        if found[0] in self.overlay.class_aliases:
            return self.overlay.class_aliases[found[0]]
        return cst.AnnAssign(
            target=updated_node.targets[0].target,
            annotation=found[1],
            value=updated_node.value,
        )

    def leave_AnnAssign(
        self, original_node: cst.AnnAssign, updated_node: cst.AnnAssign
    ) -> cst.AnnAssign:
        target = updated_node.target
        if (
            self.function_depth == 1
            and self.scope
            and isinstance(target, cst.Attribute)
            and isinstance(target.value, cst.Name)
            and target.value.value == "self"
        ):
            # `self.x: T = ...` takes the overlay's type for `x`.  In `__init__`, where stubgen
            # finds it, that is its only declaration; from another method, stubgen might not
            # see it, so leave_ClassDef still declares `x` in the class body.
            qualname = self.qualname(target.attr.value)
            annotation = self.overlay.variables.get(qualname)
            if annotation is None or qualname in self.overlay.class_aliases:
                return updated_node
            if self.method_name == "__init__":
                self.matched_variables.add(qualname)
                self.class_matched[-1].add(qualname)
            return updated_node.with_changes(annotation=annotation)
        found = self._annotation_for(target)
        if not found:
            return updated_node
        self.matched_variables.add(found[0])
        if self.scope:
            self.class_matched[-1].add(found[0])
        if found[0] in self.overlay.class_aliases:
            return self.overlay.class_aliases[found[0]]
        return updated_node.with_changes(annotation=found[1])

    def leave_Module(self, original_node: cst.Module, updated_node: cst.Module) -> cst.Module:
        imports: list[cst.BaseStatement] = list(self.overlay.imports)
        if self.uses_overloads or (
            self.replaces_with_overloads and not any(map(imports_typing, updated_node.body))
        ):
            imports.append(cst.parse_statement("import typing"))
        missing = [
            declaration(name, annotation)
            for name, annotation in self.overlay.variables.items()
            if "." not in name and name not in self.matched_variables
        ]
        self.matched_variables.update(name for name in self.overlay.variables if "." not in name)
        preamble = [
            statement
            for class_name, statement in self.overlay.preamble
            if class_name is None or class_name not in self.source_classes
        ]
        for class_name, _ in self.overlay.preamble:
            if class_name is not None and class_name not in self.source_classes:
                # A helper class: its members are its own, not annotations of the source.
                self.matched_functions.update(
                    name for name in self.overlay.functions if name.startswith(class_name + ".")
                )
                self.matched_functions.update(
                    "@" + name
                    for name in self.overlay.overloads
                    if name.startswith(class_name + ".")
                )
                self.matched_variables.update(
                    name for name in self.overlay.variables if name.startswith(class_name + ".")
                )
                self.replaced.update(
                    name
                    for name in self.overlay.replacements
                    if name.startswith(class_name + ".")
                )
                self.declared.update(
                    f"{class_name}.{func.name.value}"
                    for func in self.overlay.declared.get(class_name, [])
                )
        # The overlay's version of a TypeVar or alias the source also defines replaces it.
        redefined = {defined_name(statement) for statement in preamble} - {None}
        source_body: list[cst.BaseStatement] = [
            s for s in updated_node.body if defined_name(s) not in redefined
        ]
        declared_here = self.overlay.declared.get("", [])
        if declared_here:
            source_body = self._declare("", source_body, declared_here)
        # Declarations go before the source's own statements: stubgen keeps the first type it
        # sees for a name, and a name the source assigns by tuple unpacking (`A, B = 0, 1`) or
        # in a chain (`a = b = f()`) is otherwise Incomplete.
        body = insert_after_docstring(source_body, [*imports, *preamble, *missing])
        return updated_node.with_changes(body=body)


def merge(source: str, overlay_text: str, stub: bool = False) -> MergeResult:
    """Merge an overlay into `source`, a python source file, or a stub if `stub` is true."""
    overlay = Overlay.parse(overlay_text)
    transformer = OverlayTransformer(overlay, stub)
    code = cst.parse_module(source).visit(transformer).code
    unmatched = [
        f"def {name}" for name in overlay.functions if name not in transformer.matched_functions
    ]
    unmatched += [
        f"@overload def {name}"
        for name in overlay.overloads
        if "@" + name not in transformer.matched_functions
    ]
    unmatched += [
        f"@replace def {name}" for name in overlay.replacements if name not in transformer.replaced
    ]
    unmatched += [
        f"variable {name}"
        for name in overlay.variables
        if name not in transformer.matched_variables
    ]
    for scope, nodes in overlay.declared.items():
        for node in nodes:
            qualname = f"{scope}.{node.name.value}" if scope else node.name.value
            if qualname not in transformer.declared:
                conflict = qualname in transformer.declared_conflicts
                suffix = " (the source defines it)" if conflict else ""
                kind = "class" if isinstance(node, cst.ClassDef) else "def"
                unmatched.append(f"@type_check_only {kind} {qualname}{suffix}")
    return MergeResult(code, unmatched)


CACHE_DIR = HERE / ".annotate"


def merged_source(libs: pathlib.Path, rel: str) -> MergeResult:
    """Merge the overlay for `rel` into its source, caching the result."""
    import hashlib
    import json
    import os

    source = (libs / rel).read_text(encoding="utf-8", errors="surrogateescape")
    overlay = overlay_path(rel).read_text()
    key = hashlib.sha256(
        "\0".join([source, overlay, pathlib.Path(__file__).read_text()]).encode(
            "utf-8", "surrogateescape"
        )
    ).hexdigest()
    cache = CACHE_DIR / "merged" / (rel + ".json")
    if cache.exists():
        cached = json.loads(cache.read_text())
        if cached["key"] == key:
            return MergeResult(cached["code"], cached["unmatched"])
    result = merge(source, overlay)
    cache.parent.mkdir(parents=True, exist_ok=True)
    tmp = cache.with_suffix(f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps({"key": key, "code": result.code, "unmatched": result.unmatched}))
    tmp.replace(cache)
    return result


@dataclasses.dataclass
class Staging:
    # The python files staged, relative to the staging directory.
    files: list[str]
    # Overlay entries that matched nothing, by source file.
    unmatched: dict[str, list[str]]
    # Overlays that could not be merged, by source file.
    errors: dict[str, str]


def stage_tree(
    libs: pathlib.Path,
    staging: pathlib.Path,
    skip: set[str],
    apply_overlays: bool = True,
    namespace_inits: bool = False,
) -> Staging:
    """Mirror the python sources in `libs` into `staging`, with overlays merged in.

    Files are symlinked, except those with an overlay, which are written merged.  `skip` names
    top-level modules to leave out.  With `namespace_inits`, top-level directories without an
    __init__.py are given one (see stubgen_houdini_libs.py).
    """
    result = Staging([], {}, {})
    for path in sorted(libs.rglob("*.py*")):
        if path.suffix not in (".py", ".pyi") or "__pycache__" in path.parts:
            continue
        rel = str(path.relative_to(libs))
        top = pathlib.PurePath(rel).parts[0]
        if top.removesuffix(".py") in skip or top.startswith("."):
            continue
        dest = staging / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if apply_overlays and path.suffix == ".py" and overlay_path(rel).exists():
            try:
                merged = merged_source(libs, rel)
            except Exception as exc:  # noqa: BLE001
                result.errors[rel] = f"{type(exc).__name__}: {exc}"
                dest.symlink_to(path)
            else:
                dest.write_text(merged.code, encoding="utf-8", errors="surrogateescape")
                if merged.unmatched:
                    result.unmatched[rel] = merged.unmatched
        else:
            dest.symlink_to(path)
        if path.suffix == ".py":
            result.files.append(rel)
    if namespace_inits:
        for directory in staging.iterdir():
            init = directory / "__init__.py"
            if directory.is_dir() and not init.exists():
                init.touch()
                result.files.append(str(init.relative_to(staging)))
    return result
