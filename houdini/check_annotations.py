"""Check annotation overlays against the Houdini sources they annotate.

    check_annotations.py [--libs DIR] FILE...

FILEs are source paths relative to the libs directory (e.g. `toolutils.py`, `pdg/node.py`).
For each, this reports:

- errors: what basedpyright finds in the source with its overlay merged in, that it does not
  find in the unannotated source.  These are annotations that the code contradicts.
- unmatched: overlay entries that match nothing in the source.
- untyped: what is still untyped, or typed as `Any`/`Incomplete`, in the stub generated from
  the annotated source.

Runs with any python that has this directory's dev dependencies; Houdini is not needed.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

import annotation_overlays

HERE = pathlib.Path(__file__).parent
STUBS_DIR = HERE / "stubs"
DEFAULT_LIBS = pathlib.Path(
    "/opt/packages/houdini/22.0.466/platform-linux/arch-x86_64/hfs/houdini/python3.13libs"
)


def default_libs() -> pathlib.Path:
    """The libs of the Houdini in $HFS, if set; otherwise DEFAULT_LIBS."""
    hfs = os.environ.get("HFS")
    if hfs:
        found = sorted(pathlib.Path(hfs, "houdini").glob("python3.*libs"))
        if found:
            return found[-1]
    return DEFAULT_LIBS


def overlaid_files(libs: pathlib.Path) -> list[str]:
    """The source files, relative to `libs`, that have an annotation overlay."""
    files = []
    for overlay in sorted(annotation_overlays.OVERLAYS_DIR.rglob("*.pyi")):
        rel = overlay.relative_to(annotation_overlays.OVERLAYS_DIR).with_suffix(".py")
        # These overlays go into generated stubs, which check_compiled_overlay.py checks.
        if rel.parts[0].removesuffix(".py") in SKIPPED or str(rel) in COMPILED_MODULE_OVERLAYS:
            continue
        if (libs / rel).is_file():
            files.append(str(rel))
    return files
SKIPPED = {"hou"}
# A compiled module behind a python package, whose overlay applies to its generated stub.
COMPILED_MODULE_OVERLAYS = {"husd/UsdHoudini/__init__.py"}
LOOSE = re.compile(r"\b(?:Any|Incomplete)\b")


def site_packages(libs: pathlib.Path) -> list[str]:
    python_lib = libs.parent.parent / "python" / "lib" / libs.name.removesuffix("libs")
    return [str(python_lib / "site-packages-forced"), str(python_lib / "site-packages")]


def make_typings(root: pathlib.Path, libs: pathlib.Path) -> str:
    """Stubs of `hou` and the compiled modules, which have no source to analyze."""
    typings = root / "typings"
    typings.mkdir()
    digest = hashlib.sha256()
    for package in sorted(STUBS_DIR.glob("*-stubs")):
        name = package.name.removesuffix("-stubs")
        has_source = (libs / f"{name}.py").exists() or (libs / name).is_dir()
        if name in SKIPPED or not has_source:
            (typings / name).symlink_to(package)
            for stub in sorted(package.rglob("*.pyi")):
                digest.update(stub.read_bytes())
    return digest.hexdigest()


def run_pyright(root: pathlib.Path, tree: pathlib.Path, libs: pathlib.Path, files: list[str]):
    config = {
        "include": [str(tree / f) for f in files],
        "extraPaths": [str(tree), *site_packages(libs)],
        "stubPath": str(root / "typings"),
        "pythonVersion": "3.13",
        "pythonPath": sys.executable,
        "typeCheckingMode": "standard",
        "reportMissingModuleSource": False,
        "reportMissingImports": False,
        "reportAttributeAccessIssue": True,
    }
    config_path = root / f"pyrightconfig.{tree.name}.json"
    config_path.write_text(json.dumps(config))
    proc = subprocess.run(
        [str(pathlib.Path(sys.executable).parent / "basedpyright"), "--outputjson", "-p", str(config_path)],
        capture_output=True,
        text=True,
    )
    try:
        output = json.loads(proc.stdout)
    except json.JSONDecodeError:
        raise SystemExit(f"basedpyright failed:\n{proc.stdout}\n{proc.stderr}") from None
    by_file: dict[str, list[dict]] = collections.defaultdict(list)
    for diag in output["generalDiagnostics"]:
        if diag["severity"] != "error":
            continue
        rel = os.path.relpath(diag["file"], tree)
        by_file[rel].append(diag)
    return by_file


def error_key(diag: dict, lines: list[str]) -> tuple[str, str, str]:
    line = diag["range"]["start"]["line"]
    text = lines[line].strip() if line < len(lines) else ""
    return (diag.get("rule", ""), diag["message"], text)


def baseline_errors(
    root: pathlib.Path, libs: pathlib.Path, files: list[str], typings_hash: str
) -> dict[str, list[tuple[str, str, str]]]:
    """Errors in the unannotated sources, cached by source and typings."""
    cache_dir = annotation_overlays.CACHE_DIR / "baseline"
    result: dict[str, list[tuple[str, str, str]]] = {}
    todo = []
    keys = {}
    for rel in files:
        source = (libs / rel).read_bytes()
        keys[rel] = hashlib.sha256(source + typings_hash.encode()).hexdigest()
        cache = cache_dir / (rel + ".json")
        if cache.exists():
            cached = json.loads(cache.read_text())
            if cached["key"] == keys[rel]:
                result[rel] = [tuple(k) for k in cached["errors"]]
                continue
        todo.append(rel)
    if todo:
        tree = root / "baseline"
        annotation_overlays.stage_tree(libs, tree, SKIPPED, apply_overlays=False)
        found = run_pyright(root, tree, libs, todo)
        for rel in todo:
            lines = (libs / rel).read_text(errors="replace").splitlines()
            errors = [error_key(d, lines) for d in found.get(rel, [])]
            result[rel] = errors
            cache = cache_dir / (rel + ".json")
            cache.parent.mkdir(parents=True, exist_ok=True)
            tmp = cache.with_suffix(f".{os.getpid()}.tmp")
            tmp.write_text(json.dumps({"key": keys[rel], "errors": errors}))
            tmp.replace(cache)
    return result


def loose_items(stub_text: str) -> list[str]:
    """What is untyped, or typed as Any/Incomplete, in a stub."""
    import ast

    items: list[str] = []

    def walk(body: list[ast.stmt], scope: str) -> None:
        for node in body:
            if isinstance(node, ast.ClassDef):
                walk(node.body, f"{scope}{node.name}.")
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                problems = []
                args = node.args
                params = [*args.posonlyargs, *args.args, *args.kwonlyargs]
                if params and params[0].arg in ("self", "cls") and scope:
                    params = params[1:]
                for star, p in (("*", args.vararg), ("**", args.kwarg)):
                    if p is not None:
                        params.append(ast.arg(arg=star + p.arg, annotation=p.annotation))
                for p in params:
                    if p.annotation is None:
                        problems.append(f"{p.arg}: untyped")
                    elif LOOSE.search(ast.unparse(p.annotation)):
                        problems.append(f"{p.arg}: {ast.unparse(p.annotation)}")
                if node.name != "__init__":
                    if node.returns is None:
                        problems.append("return: untyped")
                    elif LOOSE.search(ast.unparse(node.returns)):
                        problems.append(f"return: {ast.unparse(node.returns)}")
                if problems:
                    items.append(f"def {scope}{node.name}  ({'; '.join(problems)})")
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                if LOOSE.search(ast.unparse(node.annotation)):
                    items.append(f"{scope}{node.target.id}: {ast.unparse(node.annotation)}")
            elif isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant):
                # `name = ...`; an alias (`name = other`) is typed by what it names.
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        items.append(f"{scope}{target.id}: untyped")

    walk(ast.parse(stub_text).body, "")
    return items


def untyped_report(tree: pathlib.Path, files: list[str], root: pathlib.Path) -> dict[str, list[str]]:
    """What is still loosely typed in the stubs generated from the annotated sources."""
    out = root / "stubgen"
    cwd = os.getcwd()
    os.chdir(tree)
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "mypy.stubgen", "--no-import", "-o", str(out), *files],
            capture_output=True,
            text=True,
        )
    finally:
        os.chdir(cwd)
    report: dict[str, list[str]] = {}
    for rel in files:
        stub = out / pathlib.Path(rel).with_suffix(".pyi")
        if not stub.exists():
            report[rel] = [f"stubgen failed: {proc.stderr.strip()[-500:]}"]
            continue
        report[rel] = loose_items(stub.read_text())
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*")
    parser.add_argument("--libs", type=pathlib.Path, default=None, help="default: from $HFS")
    parser.add_argument("--all", action="store_true", help="check every file that has an overlay")
    parser.add_argument("--no-untyped", action="store_true", help="skip the untyped report")
    args = parser.parse_args()
    libs: pathlib.Path = args.libs or default_libs()
    files = [str(pathlib.PurePath(f)) for f in args.files]
    if args.all:
        files = overlaid_files(libs)
    if not files:
        parser.error("give FILEs or --all")
    for rel in files:
        if not (libs / rel).is_file():
            raise SystemExit(f"No such source file: {libs / rel}")

    with tempfile.TemporaryDirectory(prefix="check_annotations_") as tmp:
        root = pathlib.Path(tmp)
        typings_hash = make_typings(root, libs)
        tree = root / "annotated"
        staged = annotation_overlays.stage_tree(libs, tree, SKIPPED)
        found = run_pyright(root, tree, libs, files)
        baseline = baseline_errors(root, libs, files, typings_hash)
        untyped = {} if args.no_untyped else untyped_report(tree, files, root)

        total_new = total_untyped = 0
        for rel in files:
            print(f"== {rel}")
            if rel in staged.errors:
                print(f"  OVERLAY ERROR: {staged.errors[rel]}")
            lines = (tree / rel).read_text(errors="replace").splitlines()
            remaining = collections.Counter(baseline[rel])
            new = []
            for diag in found.get(rel, []):
                key = error_key(diag, lines)
                if remaining[key]:
                    remaining[key] -= 1
                else:
                    new.append((diag, key))
            total_new += len(new)
            print(f"  new errors: {len(new)}")
            for diag, key in new:
                line = diag["range"]["start"]["line"] + 1
                message = diag["message"].replace("\n", " ")
                print(f"    line {line} [{key[0]}] {message}")
                print(f"        {key[2]}")
            unmatched = staged.unmatched.get(rel, [])
            if unmatched:
                print(f"  unmatched overlay entries: {', '.join(unmatched)}")
            if not args.no_untyped:
                items = untyped.get(rel, [])
                total_untyped += len(items)
                print(f"  untyped or Any: {len(items)}")
                for item in items:
                    print(f"    {item}")
        print(f"TOTAL: {total_new} new errors, {total_untyped} untyped/Any items")


if __name__ == "__main__":
    main()
