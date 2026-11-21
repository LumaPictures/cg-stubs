export const meta = {
  name: 'houdini-annotate',
  description: 'Annotate Houdini 22 python library as stub overlays, one agent at a time: compiled modules, all annotations, then reviews, then verified hou stub fixes',
  phases: [
    { title: 'Compiled', detail: '_pdg, hou, and the other compiled extensions' },
    { title: 'Annotate', detail: 'one agent per batch of source files' },
    { title: 'Review', detail: 'independent audit of each batch' },
    { title: 'hou fixes', detail: 'verify and fix hou stub issues reported by batches' },
  ],
}

// See annotate/README.md. Args:
//   batches: batch indices into <root>/.annotate/batches.json (from annotate/build_batches.py)
//   version: the Houdini major version named in the prompts (default 22)
//   root: this directory (cg-stubs/houdini); libs: the Houdini python libs being annotated
//   extraHouIssues: hou stub issues reported outside this run, for the hou fixes stage
// Agents run one at a time, so the run uses a steady fraction of the plan's usage limits.
// Finished agents replay from cache when a run is resumed with the same prompts.
const VERSION = args.version || '22'
const ROOT = args.root || '/data/projects/cg-stubs/houdini'
const LIBS = args.libs || '/opt/packages/houdini/22.0.466/platform-linux/arch-x86_64/hfs/houdini/python3.13libs'

const TYPE_RULES = `Choosing types — the goal is every type as specific AND correct as possible:
- Derive types from the body (how parameters are used, what is returned on every path), docstrings, your knowledge of Houdini's API, and call sites across LIBS (grep -rn "name(" ${LIBS} --include=*.py): callers show what is really passed.
- The hou stub is ${ROOT}/stubs/hou-stubs/__init__.pyi; grep it for exact class names and method signatures. Use the most specific hou class that is correct for all callers (hou.SopNode vs hou.OpNode vs hou.Node; hou.EnumValue for hou enums).
- Qt: annotate with PySide6 types, even where the source imports Qt via hutil.Qt or PySide2.
- Parameters: structural/abstract types where the code only needs that (Sequence, Iterable, Mapping, Callable[[...], R]). Returns: concrete types (list[...], dict[...], tuple[...]). Always parameterize generics (no bare list/dict/tuple/Callable).
- "X | None" exactly when None is possible: parameters defaulting to None or that callers pass None to; returns where any path returns None, including falling off the end.
- Dicts passed to shelf tools and callbacks (kwargs, scriptargs): dict[str, Any].
- Use Any only when a value is genuinely dynamic: arbitrary user data, JSON-like values, values whose type varies at runtime with no expressible relationship. Prefer unions, TypeVars, ParamSpecs or overloads when the type is knowable. Never invent: an annotation must hold on every path through the code and for every caller.`

const REPORTING = `Reporting:
- hou_stub_issues: wherever the hou stub itself is wrong or imprecise (a wrong return type, a missing Optional, an Optional that can never be None, a missing method or overload, an argument type too narrow), record: the hou API, its current stub signature, what it should be, and your evidence (file:line of real usage, docs). Don't work around these with Any in your overlays; type your code correctly and report the stub issue.
- sidefx_bugs: genuine bugs in SideFX's code you notice (briefly).
- cross_module_issues: errors caused by another module's overlay or stub, other than hou.
- Rules: never modify Houdini's install, the tools, other agents' overlays, or stubs/, and never run stubgen_houdini.sh (it rewrites stubs/, which every agent is reading). rm is aliased to prompt interactively: use rm -f. hython always exits 0 and may leave a child holding stdout: run it as  rez env houdini-22 -- hython SCRIPT.py </dev/null  with output redirected to a file, and keep runs short. Put scratch files under ${ROOT}/.annotate/scratch/.`

const SOURCE_SETUP = `Setup (absolute paths):
- Houdini ${VERSION}'s python sources, READ-ONLY: LIBS=${LIBS}
- Stub project: ${ROOT} (run tools from this directory)
- Your files (paths relative to LIBS): python3 -c "import json; print('\\n'.join(json.load(open('${ROOT}/.annotate/batches.json'))[BATCH]['files']))"

Overlays: for each source file LIBS/X.py you own, the overlay is ${ROOT}/annotations/X.pyi (e.g. LIBS/pdg/node.py -> annotations/pdg/node.pyi; LIBS/foo/__init__.py -> annotations/foo/__init__.pyi). An overlay is a partial stub that the stub generator merges into the source before generating stubs:
- Mirror the module's structure: module-level functions, classes (and nested classes), methods. Every def must have EXACTLY the source's parameter names and kinds in order, including self/cls, *args and **kwargs; write defaults as "= ...". A def whose parameter names differ from the source is reported as unmatched and ignored.
- Annotate every parameter (including *args and **kwargs) and every return ("-> None" when nothing is returned).
- Attributes: declare instance attributes (self.x = ... anywhere in the class) and class attributes in the class body as "x: T". Module-level variables and constants as "NAME: T".
- Only public names matter (stubs omit names starting with an underscore, except dunders like __init__, __call__, __enter__). Skip private functions, methods, classes and attributes.
- Put the imports the annotations need at the top of the overlay (import hou; from PySide6 import QtCore, QtGui, QtWidgets; from collections.abc import ...; from typing import ...; other Houdini modules). You may define module-level TypeVars, ParamSpecs and type aliases (X: TypeAlias = ...), and private helper classes (e.g. class _Options(TypedDict), Protocols); they are copied into the stub.
- Properties: "@property def x(self) -> T: ..." and "@x.setter def x(self, value: T) -> None: ...". @overload variants are allowed where the return type depends on argument types or literal values.
- Existing annotations in the source: keep correct ones (you may omit them) and override wrong ones (e.g. hou.parmTuple -> hou.ParmTuple, any -> Any).

${TYPE_RULES}

Verify with the check tool (required): cd ${ROOT} && .venv/bin/python check_annotations.py FILE [FILE...]   (paths relative to LIBS; 10-90s). It merges the overlays into the sources and type-checks the sources with basedpyright, then reports per file:
- "new errors": errors that only appear with the overlays, i.e. the code contradicts an annotation. Fix the annotation — not by loosening it to Any unless the value really is dynamic. Remaining errors are acceptable only when the annotation is right and the error is a genuine SideFX bug, a hou stub issue (report it), or a checker limitation (e.g. narrowing it can't follow); explain these in the file's note.
- "unmatched overlay entries": fix the names or parameters.
- "untyped or Any": what is still loose in the generated stub. Drive this as low as you correctly can.
If a file can't be parsed (e.g. Python 2 syntax), skip it and say so. Only create or edit overlays for YOUR files.

${REPORTING}`

const COMPILED_SETUP = `Setup (absolute paths):
- Stub project: ${ROOT}. Generated stubs: ${ROOT}/stubs/<module>-stubs/__init__.pyi (husd.UsdHoudini: stubs/husd-stubs/UsdHoudini/__init__.pyi).
- Houdini ${VERSION}'s python libs (READ-ONLY): ${LIBS}. Pure-python code there that uses these modules shows how they are really called and what comes back.

These modules have no python source, so their stubs come from runtime inspection. You improve them with an annotation overlay, which the generator merges into the generated stub: ${ROOT}/annotations/<module>.pyi (hou -> annotations/hou.pyi; _pdg -> annotations/_pdg.pyi; husd.UsdHoudini -> annotations/husd/UsdHoudini/__init__.pyi).
- An overlay is a partial stub mirroring the generated stub's structure. Each def must have EXACTLY the parameter names, in order, of the stub def it retypes (including self); it replaces that def's annotations. Write defaults as "= ...".
- Where the stub has @overload variants, retype one by writing a def WITHOUT @overload with that variant's parameter names. To add new overload variants, write them with @overload (they are inserted before the stub's def of that name).
- Variables and attributes: "name: T" in the module or class body.
- Imports at the top of the overlay; module-level TypeVars, type aliases and private helper classes are allowed.

Ground truth comes from running Houdini: introspect objects, call functions on real data, and check value types (write a script, run it with hython as described below). Use docs knowledge and the pure-python callers as supporting evidence. Every annotation must be true at runtime.

${TYPE_RULES}

Verify (required): cd ${ROOT} && .venv/bin/python check_compiled_overlay.py MODULE   — merges your overlay into the stub and reports overlay entries that match nothing, mypy errors in the merged stub, and what is still untyped, Any or object. "object" is correct for parameters that truly accept anything (e.g. __eq__'s other); otherwise make it specific.

${REPORTING}`

const FILE_RESULT = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    status: { type: 'string', enum: ['annotated', 'partial', 'skipped'] },
    new_errors: { type: 'integer' },
    untyped_remaining: { type: 'integer' },
    note: { type: 'string' },
  },
  required: ['file', 'status', 'new_errors', 'untyped_remaining'],
}
const LISTS = {
  hou_stub_issues: { type: 'array', items: { type: 'string' } },
  sidefx_bugs: { type: 'array', items: { type: 'string' } },
  cross_module_issues: { type: 'array', items: { type: 'string' } },
}
const ANNOTATE_SCHEMA = {
  type: 'object',
  properties: { batch: { type: 'integer' }, files: { type: 'array', items: FILE_RESULT }, ...LISTS },
  required: ['batch', 'files', 'hou_stub_issues', 'sidefx_bugs', 'cross_module_issues'],
}
const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    batch: { type: 'integer' },
    corrections: { type: 'integer', description: 'number of annotations changed' },
    correction_examples: { type: 'array', items: { type: 'string' }, description: 'up to 10 examples: old -> new, and why' },
    files: { type: 'array', items: FILE_RESULT },
    ...LISTS,
  },
  required: ['batch', 'corrections', 'correction_examples', 'files', 'hou_stub_issues', 'sidefx_bugs', 'cross_module_issues'],
}
const COMPILED_SCHEMA = {
  type: 'object',
  properties: {
    modules: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          module: { type: 'string' },
          loose_before: { type: 'integer' },
          loose_after: { type: 'integer' },
          note: { type: 'string' },
        },
        required: ['module', 'loose_before', 'loose_after'],
      },
    },
    ...LISTS,
  },
  required: ['modules', 'hou_stub_issues', 'sidefx_bugs', 'cross_module_issues'],
}
const HOU_FIX_SCHEMA = {
  type: 'object',
  properties: {
    fixed: { type: 'array', items: { type: 'string' } },
    rejected: { type: 'array', items: { type: 'string' }, description: 'reported issues that were wrong, with the runtime evidence' },
    loose_after: { type: 'integer' },
  },
  required: ['fixed', 'rejected', 'loose_after'],
}

const annotatePrompt = (b) => `You are annotating part of Houdini ${VERSION}'s python library, to generate type stubs whose types are as specific and correct as possible. Your batch is BATCH=${b}.

${SOURCE_SETUP.replaceAll('BATCH', String(b))}

Write the overlays for all of your files, verify them with the check tool, and return the summary.`

const reviewPrompt = (b) => `You are reviewing batch BATCH=${b} of an effort to annotate Houdini ${VERSION}'s python library for type stubs. Another agent has written annotation overlays for these files. Your job: find and fix annotations that are wrong, or less specific than they could correctly be, and fill anything still missing.

${SOURCE_SETUP.replaceAll('BATCH', String(b))}

Review each file's source and overlay side by side. In particular check:
- every parameter type against the body and ALL call sites across LIBS: too narrow (some caller passes something else) or too broad (Any, object, bare containers, Callable without a signature, a base class where a subclass is always passed);
- "| None" in both directions;
- return types on every path, including implicit None, generators (Iterator/Generator), and context managers;
- that hou methods the code calls on a value actually exist on the annotated hou class (grep the hou stub);
- public attributes, module variables, and anything the check tool still lists as untyped or Any.
Fix problems by editing the overlays, re-run the check tool until clean, and return the summary. Count each annotation you changed as a correction. In the issue lists, include only issues you found or confirmed (the annotator's own reports are collected separately).`

const COMPILED_TASKS = [
  {
    label: 'compiled:_pdg',
    modules: ['_pdg'],
    focus: `_pdg is PDG's pybind11 core (re-exported by the pdg package). Its stub has ~175 "-> Any" returns and ~195 "object" parameters left from pybind's untyped "object", plus a few other loose items. Attribute values (attribValue, attribArray, setAttrib..., Dictionary values) can be typed with the attribute value types PDG supports (int, float, str, pdg.File, dict, PyObject...) as unions or overloads keyed on pdg.attribType where possible. Use the pure-python pdg package, pdgjob, pdgutils and the TOP node code in LIBS as evidence, plus runtime experiments in hython (create a TOP network, cook it, inspect work items).`,
  },
  {
    label: 'compiled:misc',
    modules: ['_pdgd', '_pdgutils', '_cop', '_hwebserver', '_haio', '_houfs', '_houshfs', '_texturepaint', '_parsepeakusagelog', 'hapi'],
    focus: 'These are mostly well typed already; fix every remaining Any, object, untyped and Incomplete item, and check that existing types are right where callers in LIBS suggest otherwise.',
  },
  {
    label: 'compiled:qt-alembic-usd',
    modules: ['_houqt', '_alembic_hom_extensions', 'hjson', 'mantra', '_gltf_hom_extensions', 'husd.UsdHoudini'],
    focus: `_houqt is a shiboken (PySide6) module whose signatures couldn't be inspected: most methods are untyped; type them from runtime introspection and its callers in LIBS (shotsculpt, the motion mixer, etc.). _alembic_hom_extensions, hjson, mantra and _gltf_hom_extensions are small modules with untyped functions; their docstrings describe their results (e.g. "(value, isConstant) = alembicBoundingBox(abcPath, objectPath, sampleTime)"). husd.UsdHoudini is a USD schema module: the conventional schema methods are already typed; type its remaining methods (e.g. on HoudiniXformCommonAPI) and enums the way types-usd would, and check the conventional ones against runtime.`,
  },
  {
    label: 'compiled:hou',
    modules: ['hou'],
    focus: `hou is generated from SWIG with an established cleanup config, and is already ~98% typed. Its remaining loose items: "-> Any", "dict[str, Any]" where the dict has a known shape (consider TypedDicts or precise value types), "object" parameters (correct only for things like __eq__), Incomplete attributes, and untyped methods. Fix those that can be made precise, verifying each against runtime behaviour. Don't touch hou_cleanup_config.py; put everything in annotations/hou.pyi.`,
  },
]

const compiledPrompt = (t) => `You are improving the type stubs for these compiled Houdini ${VERSION} modules: ${t.modules.join(', ')}.

${COMPILED_SETUP}

Focus: ${t.focus}

For each module, record how many loose items (untyped, Any, object, Incomplete) check_compiled_overlay.py reported before you started and after you finished. Return the summary.`

// One agent at a time, so the work uses about half of each 5-hour usage window and leaves the
// rest for interactive work. Finished agents replay from cache (same prompts and options).
const compiledResults = []
phase('Compiled')
for (const t of COMPILED_TASKS) {
  compiledResults.push(await agent(compiledPrompt(t), { label: t.label, phase: 'Compiled', schema: COMPILED_SCHEMA }))
}

// Annotate everything first, so coverage lands before the reviews.
phase('Annotate')
const annotated = {}
for (const b of args.batches) {
  annotated[b] = await agent(annotatePrompt(b), { label: `annotate:${b}`, phase: 'Annotate', schema: ANNOTATE_SCHEMA })
  log(`annotated batch ${b} (${Object.keys(annotated).length}/${args.batches.length})`)
}

phase('Review')
const batchResults = []
for (const b of args.batches) {
  const review = await agent(reviewPrompt(b), { label: `review:${b}`, phase: 'Review', schema: REVIEW_SCHEMA })
  batchResults.push({ batch: b, annotated: annotated[b], review })
  log(`reviewed batch ${b} (${batchResults.length}/${args.batches.length})`)
}

// Every hou stub issue reported anywhere, for agents that verify and fix them one chunk at a time.
const houIssues = []
for (const r of batchResults) {
  for (const part of [r.annotated, r.review]) {
    if (part && part.hou_stub_issues) houIssues.push(...part.hou_stub_issues.map((i) => `[batch ${r.batch}] ${i}`))
  }
}
for (const r of compiledResults.filter(Boolean)) {
  if (r.hou_stub_issues) houIssues.push(...r.hou_stub_issues.map((i) => `[compiled] ${i}`))
}
houIssues.push(...(args.extraHouIssues || []))
log(`${houIssues.length} hou stub issues reported`)

phase('hou fixes')
const CHUNK = 60
const houFixes = []
for (let i = 0; i < houIssues.length; i += CHUNK) {
  const chunk = houIssues.slice(i, i + CHUNK)
  const fix = await agent(`You are fixing reported issues in the type stubs for Houdini ${VERSION}'s hou module. Other agents, while annotating code that uses hou, reported the issues below. Reports can be wrong or duplicated: verify each against runtime behaviour before changing anything.

${COMPILED_SETUP}

The overlay is ${ROOT}/annotations/hou.pyi; it may already contain fixes from earlier agents — keep them, and add to it. Verify with: .venv/bin/python check_compiled_overlay.py hou

Reported issues (chunk ${i / CHUNK + 1} of ${Math.ceil(houIssues.length / CHUNK)}):
${chunk.map((x, n) => `${n + 1}. ${x}`).join('\n')}

For each issue: confirm it with a hython experiment or decisive evidence, then fix it in the overlay; or reject it with your evidence. Return what you fixed and rejected.`, { label: `hou-fix:${i / CHUNK + 1}`, phase: 'hou fixes', schema: HOU_FIX_SCHEMA })
  houFixes.push(fix)
}

return { batchResults, compiledResults, houIssueCount: houIssues.length, houFixes }
