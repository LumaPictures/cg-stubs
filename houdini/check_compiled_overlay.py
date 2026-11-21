"""Check the annotation overlay for `hou` or a compiled module against its generated stub.

    check_compiled_overlay.py MODULE [--stub PATH]     (e.g. hou, _pdg, hapi, husd.UsdHoudini)

Merges annotations/<module>.pyi into the stub in stubs/ (as the generator does), then reports
overlay entries that match nothing, mypy errors in the merged stub, and what is still untyped or
`Any`.  The stubs in stubs/ are not changed; `--stub` checks another copy of the module's stub
instead (e.g. one a fixup was tried on).  Runs with this directory's venv; no Houdini needed.
"""

from __future__ import annotations

import argparse
import ast
import pathlib
import re
import subprocess
import sys
import tempfile

import annotation_overlays

HERE = pathlib.Path(__file__).parent
LOOSE = re.compile(r"\b(?:Any|Incomplete)\b")


def stub_for(module: str) -> tuple[pathlib.Path, str]:
    """The generated stub for a module, and the source-relative path its overlay is keyed by."""
    top, *rest = module.split(".")
    package = HERE / "stubs" / f"{top}-stubs"
    stub = package.joinpath(*rest, "__init__.pyi")
    if module == "husd.UsdHoudini":
        return stub, "husd/UsdHoudini/__init__.py"
    return stub, module.replace(".", "/") + ".py"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("module")
    parser.add_argument("--stub", type=pathlib.Path, default=None, help="the stub to check instead of the one in stubs/")
    parser.add_argument("--merged", action="store_true", help="the stub already has the overlay merged in")
    args = parser.parse_args()
    module = args.module
    stub, rel = stub_for(module)
    stub = args.stub or stub
    overlay = annotation_overlays.overlay_path(rel)
    print(f"stub: {stub}\noverlay: {overlay}")
    text = stub.read_text()
    if overlay.exists() and not args.merged:
        merged = annotation_overlays.merge(text, overlay.read_text(), stub=True)
        text = merged.code
        print(f"unmatched overlay entries: {merged.unmatched or 'none'}")
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        # Other stub packages, so the merged stub's imports resolve.
        for package in (HERE / "stubs").glob("*-stubs"):
            name = package.name.removesuffix("-stubs")
            if name != module.split(".")[0]:
                (root / name).symlink_to(package)
        target = root / module.split(".")[0]
        target.mkdir()
        # Only the module itself; other submodules of its package are not needed.
        (target / "__init__.pyi").write_text(text if "." not in module else "")
        if "." in module:
            sub = target.joinpath(*module.split(".")[1:], "__init__.pyi")
            sub.parent.mkdir(parents=True, exist_ok=True)
            sub.write_text(text)
            for parent in sub.parents:
                if parent == root:
                    break
                (parent / "__init__.pyi").touch()
        proc = subprocess.run(
            [sys.executable, "-m", "mypy", "--no-incremental", "--python-version", "3.13",
             "--follow-imports", "silent", "-p", module.split(".")[0] if "." not in module else module],
            cwd=root, capture_output=True, text=True,
        )
        own = module.replace(".", "/") + "/"
        errors = [
            l for l in proc.stdout.splitlines()
            if ": error:" in l and "import-not-found" not in l and l.startswith(own)
        ]
        print(f"mypy errors in merged stub: {len(errors)}")
        for line in errors[:200]:
            print("   ", line)

    items = []

    def walk(body: list[ast.stmt], scope: str) -> None:
        for node in body:
            if isinstance(node, ast.ClassDef):
                walk(node.body, f"{scope}{node.name}.")
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                problems = []
                a = node.args
                params = [*a.posonlyargs, *a.args, *a.kwonlyargs]
                if params and params[0].arg in ("self", "cls") and scope:
                    params = params[1:]
                for p in [*params, *(s for s in (a.vararg, a.kwarg) if s)]:
                    if p.annotation is None:
                        problems.append(f"{p.arg}: untyped")
                    elif LOOSE.search(ast.unparse(p.annotation)) or ast.unparse(p.annotation) == "object":
                        problems.append(f"{p.arg}: {ast.unparse(p.annotation)}")
                if node.name != "__init__":
                    if node.returns is None:
                        problems.append("return: untyped")
                    elif LOOSE.search(ast.unparse(node.returns)) or ast.unparse(node.returns) == "object":
                        problems.append(f"return: {ast.unparse(node.returns)}")
                if problems:
                    items.append(f"line {node.lineno} def {scope}{node.name}  ({'; '.join(problems)})")
            elif isinstance(node, ast.AnnAssign) and LOOSE.search(ast.unparse(node.annotation)):
                items.append(f"line {node.lineno} {scope}{ast.unparse(node.target)}: {ast.unparse(node.annotation)}")

    walk(ast.parse(text).body, "")
    print(f"untyped, Any or object: {len(items)}")
    for item in items:
        print("   ", item)


if __name__ == "__main__":
    main()
