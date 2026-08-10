
## PySide6 specifics

- `pyside/stubgen_pyside.py` contains the shared PySide6 generator logic
  (`PySideHelper`, `PySideSignatureGenerator`); `pyside6/stubgen_pyside6.py` is a thin driver.
- Signature fixes are declared in `PySideSignatureGenerator.sig_matcher` as
  `signature_overrides` / `arg_type_overrides` etc. (see `stubgenlib.siggen.advanced`).
- `Signal`/`SignalInstance` are generic, parametrized by *signatures*: each type argument is
  a tuple of the argument types of one signature, e.g. `Signal[tuple[int, str]]` or
  `Signal[tuple[int, int], tuple[str, str]]` for multi-signature signals.  Custom signal
  types are inferred from `Signal.__init__` overloads; `connect`/`emit`/`disconnect` check
  against the first (default) signature, which matches runtime behavior: unsubscripted
  `connect`/`emit` use only the default signature (PySide does not dispatch across
  *genuinely distinct* signatures by argument type -- but `connect` does pick the signature
  with as many arguments as the slot, which is what makes C++ default arguments work; see
  the plugin's third feature below); `__getitem__` validates an index against the first
  or last signature.  `connect` also accepts another signal as the slot (`_SlotFunc |
  _SignalEmitter` union), and `SignalInstance.__call__` is deliberately typed like `emit` --
  signals are not callable at runtime, but Qt accepts them anywhere a slot/callable is
  expected, and an untyped `__call__` would make any signal match any callable.  The guiding principle (agreed in LumaPictures/cg-stubs#41) is **no
  false positives**: prefer letting possibly-invalid code pass over flagging valid code.
- `Signal(object)` idiomatically means "emits anything", but this cannot be special-cased in
  the stubs: every `type[X]` is a subtype of `type[object]`, so a `Signal.__init__` overload
  keyed on `type[object]` would swallow all `Signal(X)` calls, and mypy matches
  `SignalInstance[tuple[X]]` covariantly against `SignalInstance[tuple[object]]` (self-type
  annotations containing a TypeVarTuple are additionally erased to `Any` during self-arg
  checks), so a permissive `connect` overload keyed on `object` would match *every* signal.
  Instead `pyside6/types_pyside6_mypy_plugin/` ships an opt-in mypy plugin (enabled in users'
  mypy config via `plugins = ["types_pyside6_mypy_plugin"]`) that (a) rewrites `object` /
  `typing.Any` args of `Signal(...)` calls to `typing.Any` at the declaration site
  (opt-out: `object_as_any = false` in `[tool.types-pyside6-mypy]` /
  `[types-pyside6-mypy]` in mypy's own config file), and (b) validates a literal signal
  subscript (`sig[...]`) against *every* declared signature -- the stubs can only check
  the first or last -- narrowing the result to `SignalInstance[<selected signature>]` so
  chained `connect`/`emit` are checked against the signature the index selects, and
  reporting an index that matches no signature (`IndexError` at runtime, code `[index]`),
  and (c) treats the trailing arguments of a **native** signal whose signatures form a
  prefix chain as optional -- that is how Qt registers a C++ default argument
  (`clicked: Signal[tuple[()], tuple[bool]]` for `void clicked(bool checked = false)`), so
  `emit` may omit them (`dataChanged.emit(tl, br)`) and `connect` accepts a slot with as
  many arguments as the *longest* signature (`clicked.connect(slot_taking_checked)`).
  Nativeness is required and is decided by the `PySide6.` prefix of the declaring `Var`'s
  fullname, resolved from the receiver expression (`obj.sig.emit(...)`) via
  `TypeChecker.lookup_type` + an MRO lookup: a *Python* signal declared
  `Signal((int, str), (int,))` looks identical in the stubs but raises TypeError on
  `emit(1)` at runtime, so it must stay strict.  A signal read into a variable first cannot
  be traced back to its declaration and is likewise checked strictly.
  The plugin deliberately mirrors runtime semantics; it does NOT relax unsubscripted
  `connect`/`emit` to accept genuinely distinct signatures, because runtime only uses the
  default one.
  Its type-level assertions live in the GENERATED
  `pyside6/tests/mypy_plugin_test_generic_signals.py` and
  `mypy_plugin_test_native_signals.py` -- produced from `test_generic_signals.py` and
  `test_native_signals.py` by `pyside6/tests/gen_mypy_plugin_cases.py` (target name =
  `mypy_plugin_` + source name), never hand-edited -- plus the hand-written
  `mypy_plugin_no_object_cases.py`.  All are excluded from the plain
  mypy run (the assertions only hold with the plugin) and instead checked by
  `pyside6/tests/test_mypy_plugin.py`, a pytest test that runs mypy with
  `tests/mypy-plugin.ini` (plugin on, must pass), without the plugin (must fail -- proves
  the plugin is doing the work), and with the opt-out in both ini and pyproject.toml form.
  To change the shared signal test cases, edit the source `test_*.py` (with the plain
  stubs-only ignores), describe how the plugin changes each line with end-of-line markers
  -- `# type: ignore[...]  # REMOVE` (plugin fixes this false positive),
  `# ADD: ignore[code]` (only the plugin reports this error), `# type: ignore[...]
  # REPLACE: ignore[code]` (the plugin reports a different error code) -- then run
  `uv run python tests/gen_mypy_plugin_cases.py` from `pyside6/` to regenerate the twins;
  `test_mypy_plugin.py::test_cases_are_generated` fails while one is stale.

### Gotchas when editing signature overrides

- `signature_overrides` values may be docstring-style strings or `FunctionSig` objects.
  Strings are parsed with mypy's `infer_sig_from_docstring`, which **silently drops
  annotations containing `()`** (e.g. `Signal[tuple[()]]`, `_SlotFunc[()]`) -- use
  `FunctionSig`/`ArgSig` objects for those.  A single override list cannot mix strings and
  `FunctionSig` objects.
- Dotted type names in overrides must be fully qualified (e.g.
  `PySide6.QtCore.Qt.ConnectionType`, not `Qt.ConnectionType`), otherwise stubgen's
  `AnnotationPrinter` treats the prefix as an unknown module and emits a bogus
  `import Qt` at the top of the stub, silently degrading those names to `Any`.
  Fully-qualified names are stripped back to local names in the emitted stub.
- Stub generation instantiates every `QObject` subclass to inspect its properties.  Classes
  that *kill the process* on instantiation (e.g. `QBluetoothLocalDevice` aborts on macOS with
  a TCC privacy violation) are listed in `PySideHelper._uninstantiable_classes` and are
  inspected via `staticMetaObject` instead.

## Testing methodology

`pyside6/pyproject.toml` runs mypy in `strict` mode over `tests/`, so the test files double
as type-checking assertions: a `# type: ignore[code]` comment asserts that mypy reports
exactly that error on that line (strict mode enables `warn_unused_ignores`, so a stale
ignore also fails).  `tests/test_generic_signals.py` and `tests/test_native_signals.py` are
the canonical examples -- they are both type-checked (plain, stubs only) and executed by
pytest: every connect/emit/subscript example runs at runtime, with `pytest.raises` around
the ones that raise.  Their `tests/mypy_plugin_test_*.py` twins are generated from them (see
the mypy plugin section above) with the `# type: ignore` comments the *plugin-enabled* mypy
run expects; the `# REMOVE`/`# ADD`/`# REPLACE` markers in the sources are the specification
of what the plugin changes (see the module docstring of either file).  Signal semantics that
differ between native (C++) and Python-declared signals belong in `test_native_signals.py`,
which pins both sides.

When validating changes, compare mypy/pytest results against the previous commit rather than
expecting zero errors: there are known pre-existing failures (e.g. PySide 6.10 removed the
cross-enum attribute access that `test_qflag.py` exercises).
