# Annotating Houdini's python library

Most of the python modules Houdini ships are unannotated, so stubs generated from them alone are
mostly untyped. Their types are kept as **annotation overlays** in `../annotations/`: one partial
stub per source file, at the same relative path (`annotations/pdg/node.pyi` annotates
`$HFS/houdini/python3.13libs/pdg/node.py`). `hou` and the compiled modules (`_pdg`, `hapi`, ...)
have overlays too (`annotations/hou.pyi`, `annotations/_pdg.pyi`), merged into their generated
stubs. For `hou`, whose stub is generated from SideFX's docs, the overlay is where every fix to
one member goes (see [The `hou` overlay](#the-hou-overlay)).

The stub generator merges every overlay into its source before running stubgen, so regenerating
the stubs needs no annotation work: it is a script, as before. Annotation work is only needed for
code that is new or changed in a Houdini release.

| File | Purpose |
|---|---|
| `../annotation_overlays.py` | Merges an overlay into a source file (or a generated stub). |
| `../check_annotations.py` | Type-checks Houdini's sources with their overlays merged in (basedpyright), reporting errors the overlays introduce, stale overlay entries, and what is still untyped. |
| `../check_compiled_overlay.py` | The same for `hou` and the compiled modules, against their generated stubs. |
| `../check_runtime_types.py` | Checks the `hou` stub's return types against what hython really returns, by walking a scene built for the purpose (needs Houdini). |
| `../check_hou_signatures.py` | Checks the `hou` stub's parameter names, order, required and positional-only parameters against hython's, `_hou.so`'s and the HDK headers' (needs Houdini). |
| `../check_stub_generics.py` | Reports the bare generics (`dict`, `list`, `Callable`, ...) left in the generated stubs, by installing the wheel and running mypy's `--disallow-any-generics`, and pyright's errors in them, by package and rule (needs `uv`). |
| `build_batches.py` | Lists the source files that still need work: untyped items and overlay entries that match nothing. |

All of these run with this project's venv (`.venv`). Commands that need Houdini are shown run
inside its environment with rez (`rez env houdini-23 -- ...`); use whatever sets up `$HFS` and puts
`hython` on the `PATH` at your site.

## Regenerating the stubs

```bash
cd cg-stubs/houdini
rez env houdini-22 -- ./stubgen_houdini.sh
```

The generator prints any overlay entries that no longer match their source.

## Upgrading to a new Houdini version

Between 21.0 and 22.0, 93% of the public functions in Houdini's python library kept their
names and parameters (85% between 20.5 and 21.0), so most overlay entries carry over. The work
for a new version is the code that is new or changed.

1. **Set up** a branch, and a venv on the rez python with the same version as the new
   Houdini's (`rez env houdini-23 -- hython --version`). The generator runs hython with the
   venv's packages on its path, so the two must match:

   ```bash
   git checkout -b houdini/23.0.123
   uv venv --python 3.13 .venv && uv sync --no-install-project
   ```

   Update `version` in `pyproject.toml`, and check the python version in `stubgen_houdini.sh`
   (it follows `$HFS`).

2. **Regenerate the stubs** with the existing overlays:

   ```bash
   rez env houdini-23 -- ./stubgen_houdini.sh
   ```

   Fix anything the generator reports, as for the `hou` stub's new C++ types (see the
   `TYPE_MAP` in `stubgen_houdini.py`, and the generic rules in `hou_cleanup_config.py`), and
   the `hou` overlay entries that match nothing (see
   [Upgrading the `hou` overlay](#upgrading-the-hou-overlay)).

   Every `hou` enum value is typed by its enum: `hou.EnumValue` is generic, its members are
   `Float: EnumValue[parmTemplateType]`, and a parameter or return that takes or gives a
   `hou.parmTemplateType` is an `EnumValue[parmTemplateType]` (`EnumValue[a] | EnumValue[b]`
   for either). A bare `EnumValue` is a value of any enum. The generator finds the enum of each
   bare `EnumValue` parameter and return in the docs: the method's docstring, its runtime
   docstring and every overload in `hom.zip`'s help, then a getter's setter (and the other way
   round) and the getter of a constructor's parameter. It lists those it can't find, which
   need an entry in `annotations/hou.pyi` (as do those the docs get wrong), e.g.
   `def pickStyle(self) -> EnumValue[pickStyle]: ...` in `class SceneViewer`. An overlay entry
   that types a getter doesn't type its setter: give each its own. A bare `EnumValue` written
   in the overlay is a value of any enum, on purpose, and isn't listed. In a class that has a
   member named like an enum (`Ramp.colorType()`), write `EnumValue[hou.colorType]`.

3. **Check the `hou` stub against the runtime.** Most of its types come from SideFX's docs and
   C++ signatures, which miss `None` returns, tuples that are lists, subclasses and the like.
   `check_runtime_types.py` builds a scene with nodes in every context, parameters of every
   template type, geometry with attributes of every type, an HDA, ..., calls every method the
   stub allows without arguments (and one-argument lookups with real and missing names, indices
   and frames), and checks each value with typeguard against the stub's return type:

   ```bash
   rez env houdini-23 -- hython check_runtime_types.py </dev/null > .annotate/runtime_types.txt
   ```

   It skips methods with side effects (`set*`, `destroy*`, `save*`, ...; see `DENIED_PREFIXES`)
   and restarts hython without any call that crashes it (listed at the end of the report).
   Fix each mismatch in `annotations/hou.pyi` (or, if it is wrong for every member, in the
   rules of `hou_cleanup_config.py`). If a mismatch comes from the harness instead (e.g. a
   scene it can't build), fix the harness. `--class REGEX` limits the report to some classes, `--exceptions`
   lists what the calls raised.

   The UI classes (`SceneViewer`, `NetworkEditor`, `GeometryViewport`, panes, ...) only exist
   in an interactive Houdini. To check them too, start one with a new, empty scene and run, in
   its Python Shell:

   ```python
   import runpy, sys; sys.argv = ["check_runtime_types.py", "--ui"]; runpy.run_path("/path/to/cg-stubs/houdini/check_runtime_types.py", run_name="__main__")
   ```

   It writes `.annotate/runtime_types_ui.txt`. If a call crashes Houdini, restart it and run
   the same lines again: that call is skipped from then on.

   A returned enum value is checked against the stub's enum by its repr (`parmData.Float` is
   not a `parmTemplateType`). The report counts the enum returns it never reached (listed
   with `--coverage`): most are the UI classes', which only the `--ui` run checks.

   Then check the parameters: names a keyword call would fail on, parameters the stub is
   missing or has extra, C++ overloads, which SWIG wraps to take no keywords, and the order of
   positional parameters. Most SWIG wrappers have python signatures to compare with; for those
   that take `(*args, **kwargs)`, the keywords come from probing the wrapper (its argument
   parsing fails on an unknown keyword before anything reaches C++) and from the names its
   machine code in `_hou.so` loads, and the order from the declarations in the HDK's
   `$HFS/toolkit/include/HOM/*.h`, which are also the best reference for a parameter's type:

   ```bash
   rez env houdini-23 -- hython check_hou_signatures.py </dev/null
   ```

   Fix these in `annotations/hou.pyi`, with a `@replace` entry, or `@replace` `@overload`
   entries for the overloads (see [The `hou` overlay](#the-hou-overlay)). The help sources in
   `$HFS/houdini/help/hom.zip` (`hou/<Class>.txt`) list every overload of a method, where the
   runtime docstrings only keep one. An enum parameter whose
   C++ default belongs to another enum (`HOM_nodeTypeFilter::NoFilter`) is reported with the
   types.

4. **Re-verify every overlay** against the new sources. An overlay entry can still match by
   name after SideFX has changed what the function does:

   ```bash
   rez env houdini-23 -- .venv/bin/python check_annotations.py --all > .annotate/check_all.txt
   for m in hou _pdg _pdgd _pdgutils hapi _houqt husd.UsdHoudini; do
       .venv/bin/python check_compiled_overlay.py $m
   done
   ```

   Compare the new errors with a run on the previous version to find what changed.

   Then check that no bare generics crept in. The generator gives the containers pybind11 and
   Boost.Python leave bare their element types (enum `__entries` and `allValues`, bound
   vectors, `_pdg`'s dict arguments), and compiled IntEnums their `__format__` signature;
   SideFX's own bare annotations need overlay entries. (It also marks the TypedDicts that use
   PEP 728's `closed=`/`extra_items=` with `# type: ignore[call-arg]`, as mypy doesn't support
   them yet; overlays can use them freely.)

   ```bash
   .venv/bin/python check_stub_generics.py
   ```

   The same script runs pyright (standard mode) over every stub package, with the USD and
   PySide6 stubs installed, and counts its errors by package and rule. `hou` and `houtypes` must
   have none (it lists theirs, and fails if there are any). The other packages' errors are
   mostly SideFX's own overrides that are incompatible with their base class, which the stubs
   reflect, and imports of third-party modules Houdini doesn't ship (`torch`, `numpy`, ...):
   compare their counts with a run on the previous version, and look into a package whose count
   grew (`--all` lists every error).

5. **Build the worklist** of files with untyped items or stale overlay entries:

   ```bash
   rez env houdini-23 -- .venv/bin/python annotate/build_batches.py
   # 1512 files: 9876 loose items, 42 unmatched overlay entries. Wrote 23 batches to .annotate/batches.json
   ```

   `--report` lists the per-file counts.

6. **Annotate** what the worklist lists, in the overlays (see
   [Writing overlays by hand](#writing-overlays-by-hand)), checking each file with
   `check_annotations.py <file>`.

7. **Regenerate the stubs** again (step 2), check them, and commit the overlays with the stubs.

## Writing overlays by hand

An overlay mirrors its module: functions, classes and methods with exactly the source's parameter
names (including `self`, `*args` and `**kwargs`), defaults written as `= ...`, attributes as
`name: type` in the class or module body. It only needs the definitions it annotates. TypeVars,
type aliases and private helper classes (TypedDicts, Protocols) defined in an overlay are copied
into the stub. A name the source binds by tuple unpacking (`A, B = 0, 1`) or in a chain
(`a = b = f()`) is typed by declaring it, as any other. A public class in an overlay replaces a
functional definition of that name in the source, so a namedtuple is typed as:

```python
# source: SuccessEvent = namedtuple('SuccessEvent', 'workitem_id index cook_duration jobid')
class SuccessEvent(NamedTuple):
    workitem_id: str
    index: int
    cook_duration: float
    jobid: str
```

Its fields must keep the source's names and order; defaults come from the source.

A class in an overlay gives the type arguments of the source's bare generic bases: the overlay's
`class Config(dict[str, Any])` makes the source's `class Config(dict)` a `dict[str, Any]`, and
`class FuncChange(Change[SS])` makes a `FuncChange(Change)` generic. It can also add type
arguments to a base the source subscripts (`DraggableModel[MenuItem, _MenuItemJson]` for
`DraggableModel[MenuItem]`), and make a class generic that the source does not: a
`Generic[...]` base in the overlay's class (`class MenuMapping(Generic[_V])`,
`class AttributeArray(AttributeBase, Generic[_E])`) is added to a source class that has none
(dropping an explicit `object` base), and extends one that has fewer type parameters
(`Generic[T, _J]` for `Generic[T]`). Declare its TypeVars in the overlay. Only these changes
are made; any other difference between the two classes' bases is ignored. An instance attribute that the source
annotates itself (`self.prefixes: dict[K, PrefixParselet] = {}`) takes the overlay's type
(`prefixes: dict[K, PrefixParselet[T]]` in the class) there too.

A method that a class inherits, but whose type depends on the subclass, can be declared in the
subclass's overlay even though its source does not define it, by marking it
`@type_check_only` (from `typing`). `PythonCallback.__getitem__` returns what the wrapped C++
object's `__getitem__` returns, so `PyScheduler`'s overlay declares
`@type_check_only def __getitem__(self, key: str) -> _pdg.Port: ...`, and the stub has that
override. The marker is dropped from the stub. Without it, a method the source class lacks is
reported as unmatched; with it, a method the source class defines is.

The stub has every public name the module defines, including those its `__all__` leaves out
(`__all__` only limits `import *`), and of its private names only those the overlay declares:
declare one (`_quick_mat_funcs: dict[str, _QuickMaterialFunc]`, `def _updateHUD(self) -> None`)
when code outside the module uses it. To export a name the module imports, for code that uses
it through the module, import it as itself in the overlay
(`from toolutils import OrientInfo as OrientInfo`).

Check an overlay with:

```bash
.venv/bin/python check_annotations.py toolutils.py
```

### The `hou` overlay

`hou.py` is SWIG's wrappers, which all take `(*args)`, so `stubgen_houdini.py` generates the
`hou` stub from SideFX's docs: the wrappers' docstrings and the C++ signatures in them, turned
into python types by the generic rules in `hou_cleanup_config.py` (type aliases, enum values,
which pointer returns are never `None`, the comparison operators of every class). Then it
merges `annotations/hou.pyi` in. Whatever is wrong for one member, or missing from the docs,
goes in the overlay, in one of three kinds of entry:

```python
class Face:
    # Takes the stub's parameters as they are, and gives them and the return these types.
    def vertex(self, index: int) -> Vertex: ...

class AgentLayer:
    # Replaces the signature, whatever the docs' parameters: names, order, defaults and `/`
    # are the overlay's.  The stub's docstring and decorators are kept.
    @replace
    def bindings(self, transform: int|None = ..., /) -> Tuple[AgentShapeBinding,...]: ...
    # Replaces it with these overloads, each with the stub's docstring.
    @replace
    @overload
    def __init__(self, filename: str, rig: AgentRig, shapelib: AgentShapeLibrary, keep_external_ref: bool = ..., /) -> None: ...
    @replace
    @overload
    def __init__(self, name: str, rig: AgentRig, shapelib: AgentShapeLibrary, shape_bindings: Sequence[AgentShapeBinding], source_layer: AgentLayer|None = ..., /) -> None: ...

class Node:
    # A member the docs lack (houpythonportion adds it to hou at runtime): declared at the end
    # of the class, decorators and all.
    @type_check_only
    def createOutputNode(self, node_type_name: str, node_name: str | None = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> Self: ...
```

A plain entry is the default: it keeps up with the docs' defaults, and needs the docs'
parameter names, so use `@replace` when the names, their order, their kinds or their defaults
are wrong. A method is always a `def`: one a subclass narrows (`ObjNode.parent()`, which
returns an `OpNode`) is a `@type_check_only` declaration in the subclass, and one that
houpythonportion adds to a hou submodule (`hou.qt.createIcon`) a `@type_check_only`
`@staticmethod`. Typed as a `Callable` or a Protocol, it would be an instance variable, which
pyright reports as clashing with the base class's method. A function hou.py makes at runtime
(`expandString = __createTopLevelFunc("expandString")`) is a `@replace` `def` too: it replaces
the variable the stub has for it. Write `= ...` for a plain entry's defaults (the stub's are
kept), and the real defaults in a `@replace` one. A module-level function is written the same
way; a hou submodule
(`hou.ui`, `hou.hipFile`) is a class whose functions have no `self` (the stub makes them static
methods). `@type_check_only` also declares a class the docs lack (`hou.data`, the widget
classes of `hou.qt`), body and all; a private class at module level (`_TraversalDemands`) is a
helper class instead, copied ahead of the stub's own code. A variable the docs lack is just
written, and is declared. Comments above a plain or `@replace` entry stay in the overlay; those
above a `@type_check_only` one go into the stub with it.

#### Upgrading the `hou` overlay

The generator prints the overlay entries that match nothing in the new docs-derived stub:

```
Overlay entries for hou that match nothing: def Parm.set, @replace def Desktop.createFloatingPane, ...
```

`def X` is a plain entry whose member is gone or whose parameters were renamed, and
`@replace def X` (or `@overload def X`) a replacement whose member is gone. Compare each with
the new docs: if the member was renamed or moved, move the entry; if the docs now have it
right, delete the entry. `check_compiled_overlay.py hou` reports the same, against the stub in
`stubs/`. `@type_check_only` declarations are added whatever the docs say, so they are never
reported: when upgrading, check them against `houpythonportion` (which adds them) and the
docs (which may have caught up, in which case the declaration replaces the docs' signature).

The `kwargs` dictionaries that Houdini passes to callbacks (viewer state and handle callbacks,
shelf tool scripts, parameter callbacks and menu scripts, action buttons, asset event handlers,
...) have `TypedDict`s in the hand-written stub-only module `houtypes`
(`stubs/houtypes-stubs/__init__.pyi`). Type such a parameter with one rather than
`dict[str, Any]`, and so the library functions that are handed the callback's dictionary,
including those that add keys to it. Import it at the top of the overlay like any other module
(`from houtypes import ViewerStateEventKwargs`), not under `if TYPE_CHECKING:`: the merger only
copies an overlay's top-level imports. A key a callback only sometimes gets is not required, so
the source's `kwargs["node"]` in a state's `onMouseEvent` is an error to basedpyright; that is
right, as nodeless states have no node.
