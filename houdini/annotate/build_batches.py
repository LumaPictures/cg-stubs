"""Build the worklist of source files that still need annotation work, in batches.

    build_batches.py [--libs DIR] [--output FILE] [--target N] [--report]

A file needs work if, with its overlay merged in, its generated stub still has untyped or
Any/Incomplete items, or if its overlay has entries that match nothing in the source (stale after
a Houdini upgrade). Files are packed in path order into batches of about --target items, so a
batch stays within one package where it can, and written to the output file; --report lists the
per-file counts.

Runs with this directory's venv; Houdini is not needed.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import tempfile

HOUDINI_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HOUDINI_DIR))

import annotation_overlays  # noqa: E402
import check_annotations  # noqa: E402

# Not stubbed from source: hou comes from SWIG, husd.UsdHoudini from inspection.
SKIPPED_FILES = {"hou.py", "husd/UsdHoudini/__init__.py"}


def file_work(libs: pathlib.Path) -> dict[str, dict[str, int]]:
    """Loose and unmatched item counts, and line counts, of every source file."""
    with tempfile.TemporaryDirectory(prefix="build_batches_") as tmp:
        root = pathlib.Path(tmp)
        tree = root / "annotated"
        # As in the generator: namespace packages need an __init__.py, or stubgen mistakes
        # their modules for top-level ones with the same names.
        staged = annotation_overlays.stage_tree(
            libs, tree, check_annotations.SKIPPED, namespace_inits=True
        )
        files = [
            f
            for f in staged.files
            if f not in SKIPPED_FILES and not _added_init(f, libs)
        ]
        loose = check_annotations.untyped_report(tree, files, root)
    failed = [
        rel for rel in files if any(i.startswith("stubgen failed") for i in loose[rel])
    ]
    if failed:
        raise SystemExit(
            f"stubgen failed for {len(failed)} files, e.g. {loose[failed[0]][0]}"
        )
    work = {}
    for rel in files:
        items = loose.get(rel, [])
        work[rel] = {
            "loose": len(items),
            "unmatched": len(staged.unmatched.get(rel, [])),
            "lines": len(
                annotation_overlays.source_path(libs, rel)
                .read_text(errors="replace")
                .splitlines()
            ),
        }
    return work


def _added_init(rel: str, libs: pathlib.Path) -> bool:
    """Whether `rel` is an __init__.py that stage_tree added to a namespace package."""
    return (
        rel.endswith("__init__.py")
        and not annotation_overlays.source_path(libs, rel).exists()
    )


def pack(
    work: dict[str, dict[str, int]], target: int, max_files: int, max_lines: int
) -> list[dict[str, object]]:
    batches: list[list[str]] = []
    current: list[str] = []
    items = lines = 0
    previous_top = None
    for rel in sorted(work):
        count = work[rel]["loose"] + work[rel]["unmatched"]
        if not count:
            continue
        top = rel.split("/")[0].removesuffix(".py")
        full = (
            items + count > target
            or len(current) >= max_files
            or lines + work[rel]["lines"] > max_lines
            # Start a new batch at a package boundary once this one is reasonably full.
            or (top != previous_top and items > target * 0.6)
        )
        if current and full:
            batches.append(current)
            current, items, lines = [], 0, 0
        current.append(rel)
        items += count
        lines += work[rel]["lines"]
        previous_top = top
    if current:
        batches.append(current)
    return [
        {
            "id": i,
            "files": files,
            "items": sum(work[f]["loose"] + work[f]["unmatched"] for f in files),
        }
        for i, files in enumerate(batches)
    ]


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--libs", type=pathlib.Path, default=None, help="default: from $HFS"
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=HOUDINI_DIR / ".annotate" / "batches.json",
    )
    parser.add_argument("--target", type=int, default=450, help="loose items per batch")
    parser.add_argument("--max-files", type=int, default=30)
    parser.add_argument("--max-lines", type=int, default=10000)
    parser.add_argument("--report", action="store_true", help="print per-file counts")
    args = parser.parse_args()

    libs = args.libs or check_annotations.default_libs()
    work = file_work(libs)
    batches = pack(work, args.target, args.max_files, args.max_lines)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(batches, indent=1))

    if args.report:
        for rel, counts in sorted(work.items()):
            if counts["loose"] or counts["unmatched"]:
                print(
                    f"{counts['loose']:5} loose {counts['unmatched']:4} unmatched  {rel}"
                )
    loose = sum(c["loose"] for c in work.values())
    unmatched = sum(c["unmatched"] for c in work.values())
    print(
        f"{len(work)} files: {loose} loose items, {unmatched} unmatched overlay entries. "
        f"Wrote {len(batches)} batches to {args.output}"
    )


if __name__ == "__main__":
    main()
