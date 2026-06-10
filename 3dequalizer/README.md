# Unofficial python stubs for Science.D.Visions 3DEqualizer4

Type stubs for the following 3DEqualizer's scriptable modules:

* **`tde4`**: the main scripting API.
* **`vl_sdv`**: the bundled vector / matrix / transform math library.

## Installing

```commandline
pip install types-3dequalizer
```

The package version tracks the 3DEqualizer version it was generated from, plus a
suffix for the stub revision.

## Generating

`tde4` is a built-in C module baked into the 3DE interpreter (no file on disk),
so it only exists inside a running 3DE process and can't be imported or
introspected standalone. Instead we parse the vendor's **Python Doc (LLM)**, a
JSON API doc that carries full annotations, a semantic type system, defaults and
deprecation status, so no GUI is needed.

| Module   | Source                                                  | How it's generated |
|----------|---------------------------------------------------------|--------------------|
| `tde4`   | the Python Doc (LLM) JSON (`$TDE4_LLM_DOC`)             | **parsed** by `stubgen_3dequalizer.py` |
| `vl_sdv` | `$TDE4_ROOT/sys_data/py_vl_sdv/vl_sdv.py` (pure python) | **custom mypy inspection** of the real module |

Download the **"Python Doc (LLM)"** (the `(LLM)` JSON, **not** the
`(Human)` HTML) from
[3dequalizer.com &rarr; Tech Docs](https://www.3dequalizer.com/?site=tech_docs)
&rarr; Python Scripting Interface, for the 3DE version you're generating.

Set the paths in `.env`, then generate from the repo root:

```
TDE4_LLM_DOC=/path/to/tde4_with_examples.wtrl.core.rfc-2119.json
TDE4_ROOT=/path/to/3DE4_win64_r<version>
```

```commandline
nox -s 'generate(3dequalizer)'
```

This calls the generator, renames the output to the PEP&nbsp;561 `*-stubs`
layout, and runs mypy + mypy-silent over it.

### How the stubs are built

The doc provides real Python annotations per parameter and return, emitted
mostly verbatim. On top of that the generator:

* emits each referenced `*_t` type as a resolved `TypeAlias` (e.g.
  `Vector3D_t: TypeAlias = list[float]`, and string enums as
  `CameraType_t: TypeAlias = Literal["SEQUENCE", "REF_FRAME"]`),
* emits the `WidgetCallback*Enum` constant classes and their `int` members,
* adds `@deprecated` where the doc marks `status: deprecated`,
* marks every function positional-only with a trailing `/`, since `tde4` is all
  C builtins that reject keyword arguments (`createCamera(mode="...")` raises
  `TypeError: takes no keyword arguments`),
* narrows optional args the doc gets wrong: `x: T | None = None` &rarr;
  `x: T = ...`, since 3DE rejects an explicit `None`.

A few small by-name override tables handle the rest:
* `_RETURN_TYPE_OVERRIDES` corrects returns the doc gets wrong at runtime:
  `tuple[...]` &rarr; `list[...]` (3DE returns lists, not tuples), and lists
  whose elements can be `None`,
* `_RETURN_SHAPE_COMMENTS` / `_TYPE_ALIAS_COMMENTS` add a trailing comment
  restating the per-position meaning a widened `list[...]` can't express,
* `_TYPE_ALIAS_OVERRIDES` for types whose base can't be auto-derived (e.g.
  `LSFResult_t`),
* `_SUPPLEMENTAL_FUNCTIONS` for the `acos`/`sin`/... math wrappers that are live
  but absent from the doc.

### From doc entry to stub line

Take `convertObjectPGroupTransformation3DEToWorld`; it hits both runtime
corrections at once. It flows top to bottom, one box per step:

```text
┌─ 1 · INPUT - one entry in the LLM doc (__WTRL_OBJECTS__) ────────────────┐
│ "signature": {                                                           │
│   "parameters": [                                                        │
│     {"name": "camera_id",    "annotation": "CameraID_t"},                │
│     {"name": "pgroup_scale", "annotation": "float | None",               │
│      "default": "None"},                    # ← optional                 │
│     ... ],                                                               │
│   "returns": "tuple[Matrix3D_t, Vector3D_t]"   # ← a tuple               │
│ }                                                                        │
└──────────────────────────────────────────────────────────────────────────┘
    │
    ▼   _Spec.callables() → _build_signature(name, obj)
┌─ 2 · _render_parameter() - one per parameter ────────────────────────────┐
│ camera_id     "CameraID_t"              →  camera_id: CameraID_t         │
│ pgroup_scale  "float | None" + default  →  pgroup_scale: float = ...     │
│                                            (drop " | None", add " = ...")│
└──────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─ 3 · _RETURN_TYPE_OVERRIDES[name] - the return type ─────────────────────┐
│ tuple[Matrix3D_t, Vector3D_t]  →  list[Matrix3D_t | Vector3D_t]          │
└──────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─ 4 · OUTPUT - a line in tde4-stubs/__init__.pyi ─────────────────────────┐
│ def convertObjectPGroupTransformation3DEToWorld(                         │
│     camera_id: CameraID_t, ..., pgroup_scale: float = ..., /,            │
│ ) -> list[Matrix3D_t | Vector3D_t]: ...  # [transform matrix, position]  │
└──────────────────────────────────────────────────────────────────────────┘
```

Why the two corrections (steps 2 and 3):

* **Optional arg `T | None = None` → `T = ...`**: 3DE rejects an explicit
  `None`; the arg must be omitted, not passed as `None`.
* **`tuple[...]` → `list[...]`**: 3DE returns a `list` at runtime, not a tuple.

The `*_t` names (`CameraID_t`, `Matrix3D_t`, `Vector3D_t`) aren't resolved here:
`_resolve_all_type_aliases` walks each type's `doc_lines` (transitively, so
`Matrix3D_t` pulls in `Vector3D_t`) and emits the aliases near the top. Finally
`_render_module` assembles everything and `_render_header` adds only the imports
the body actually uses.

## Testing

Tests are split by where they run:

* **`tests/`**: generator unit tests; pure python, run standalone.
* **`tests_live/`**: API-usage tests for `tde4`/`vl_sdv`, verified *twice*: mypy
  against the stubs (static) and `assert_type` (from `stubgenlib.test_helpers`)
  against the real module (runtime), so stubs and shipped modules must agree.
  `tde4` only exists inside 3DE, so these run there.

From the repo root:

```commandline
nox -s 'mypy(3dequalizer)'    # static: type-check every suite against the stubs
nox -s 'test(3dequalizer)'    # the generator unit tests (tests/)
```

The live suite runs inside 3DE, whose python lacks our dev deps, so from the
project dir put its virtualenv on PYTHONPATH first:

```commandline
export PYTHONPATH="$(echo .venv/*/site-packages)"   # Windows: set PYTHONPATH=.venv\Lib\site-packages
<3de-executable> -no_gui -run_script tests_live/run_tests.py
```

`<3de-executable>` is the 3DEqualizer binary (use its full path, or your studio's
launch wrapper); `-no_gui -run_script` are 3DEqualizer's own flags.
