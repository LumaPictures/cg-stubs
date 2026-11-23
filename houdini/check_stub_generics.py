"""Report the bare generics (`dict`, `list`, `Callable`, ...) in the generated stubs, and the
errors pyright finds in them.

mypy only finds `*-stubs` packages in site-packages, so this builds the wheel, installs it into
a throwaway venv and runs mypy's `--disallow-any-generics` over every stub package there, then
installs the USD and PySide6 stubs the Houdini stubs import and runs pyright (standard mode).
Needs `uv` on the PATH.

pyright's errors are counted by package and rule.  Those in `MUST_BE_CLEAN` are listed in full
and fail the check, as are bare generics; the rest are reported so that their counts can be
compared between Houdini versions: most are SideFX's own overrides that are incompatible with
their base class, which the stubs reflect.  `--all` lists every pyright error.
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import json
import pathlib
import re
import subprocess
import sys
import tempfile
from collections.abc import Sequence
from typing import NotRequired, TypedDict

HERE = pathlib.Path(__file__).parent
TYPE_ARG = re.compile(r"site-packages/((\w+)-stubs/.*)\[type-arg\]$")
# types-PySide6 makes Qt's signals generic, which PySide6's own stubs don't, so the stubs leave
# them bare: mypy runs before it is installed.
PYRIGHT_DEPENDENCIES = ["pyright", "types-usd", "types-PySide6"]
MUST_BE_CLEAN = {"hou", "houtypes"}


class _Position(TypedDict):
    line: int
    character: int


class _Range(TypedDict):
    start: _Position
    end: _Position


class _Diagnostic(TypedDict):
    """One of the `generalDiagnostics` in pyright's `--outputjson`."""

    file: str
    severity: str
    message: str
    range: _Range
    rule: NotRequired[str]


@dataclasses.dataclass
class PyrightError:
    package: str
    path: str
    line: int
    message: str
    rule: str

    def __str__(self) -> str:
        message = self.message.replace("\n", " ")
        return f"{self.path}:{self.line}: {message} ({self.rule})"


def run_mypy(
    python: pathlib.Path, packages: Sequence[str], cwd: pathlib.Path
) -> list[str]:
    """The bare generics mypy finds in the stub packages."""
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    result = subprocess.run(
        [
            str(python),
            "-m",
            "mypy",
            "--python-version",
            python_version,
            "--disallow-any-generics",
            "--no-incremental",
            "--show-error-codes",
            "--no-pretty",
            "--hide-error-context",
            *(arg for package in packages for arg in ("-p", package)),
        ],
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return [
        m.group(1)
        for line in result.stdout.splitlines()
        if (m := TYPE_ARG.search(line)) and m.group(2) in packages
    ]


def run_pyright(
    venv: pathlib.Path, packages: Sequence[str]
) -> tuple[str, list[PyrightError]]:
    """pyright's version, and the errors it finds in the stub packages."""
    site_packages = next(venv.glob("lib/python*/site-packages"))
    config = venv.parent / "pyrightconfig.json"
    config.write_text(
        json.dumps(
            {
                "pythonVersion": f"{sys.version_info.major}.{sys.version_info.minor}",
                "venvPath": str(venv.parent),
                "venv": venv.name,
                "typeCheckingMode": "standard",
                # The stubs of modules whose sources aren't installed (all of them).
                "reportMissingModuleSource": False,
            }
        )
    )
    pyright = str(venv / "bin" / "pyright")
    version = subprocess.run(
        [pyright, "--version"], capture_output=True, text=True, check=True
    ).stdout.strip()
    result = subprocess.run(
        [
            pyright,
            "--outputjson",
            "-p",
            str(config),
            *(str(site_packages / f"{package}-stubs") for package in packages),
        ],
        capture_output=True,
        text=True,
    )
    diagnostics: list[_Diagnostic] = json.loads(result.stdout)["generalDiagnostics"]
    errors = []
    for diagnostic in diagnostics:
        if diagnostic["severity"] != "error":
            continue
        rel = pathlib.Path(diagnostic["file"]).relative_to(site_packages)
        errors.append(
            PyrightError(
                package=rel.parts[0].removesuffix("-stubs"),
                path=str(rel),
                line=diagnostic["range"]["start"]["line"] + 1,
                message=diagnostic["message"],
                rule=diagnostic.get("rule", "no rule"),
            )
        )
    return version, errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--all", action="store_true", help="list every pyright error")
    args = parser.parse_args()

    packages = sorted(
        p.name.removesuffix("-stubs") for p in (HERE / "stubs").glob("*-stubs")
    )
    with tempfile.TemporaryDirectory() as tmp:
        dist = pathlib.Path(tmp) / "dist"
        venv = pathlib.Path(tmp) / "venv"
        subprocess.run(
            ["uv", "build", "-q", "--wheel", "-o", str(dist)], cwd=HERE, check=True
        )
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        subprocess.run(
            ["uv", "venv", "-q", "--python", python_version, str(venv)], check=True
        )
        python = venv / "bin" / "python"
        wheel = next(dist.glob("*.whl"))
        install = ["uv", "pip", "install", "-q", "--python", str(python)]
        subprocess.run([*install, str(wheel), "mypy"], check=True)
        bare_generics = run_mypy(python, packages, pathlib.Path(tmp))
        subprocess.run([*install, *PYRIGHT_DEPENDENCIES], check=True)
        pyright_version, errors = run_pyright(venv, packages)

    for line in bare_generics:
        print(line)
    print(f"{len(bare_generics)} bare generics")

    print(f"\n{pyright_version}: errors by package and rule")
    by_package: dict[str, list[PyrightError]] = collections.defaultdict(list)
    for error in errors:
        by_package[error.package].append(error)
    for package in sorted(MUST_BE_CLEAN | by_package.keys()):
        found = by_package.get(package, [])
        rules = collections.Counter(e.rule for e in found)
        counts = ", ".join(f"{rule} {n}" for rule, n in rules.most_common())
        print(f"{package}: {len(found)}" + (f" ({counts})" if counts else ""))
        if package in MUST_BE_CLEAN or args.all:
            for error in found:
                print(f"    {error}")
    print(f"{len(errors)} pyright errors in {len(by_package)} packages")
    unclean = sum(len(by_package.get(package, [])) for package in MUST_BE_CLEAN)
    return 1 if bare_generics or unclean else 0


if __name__ == "__main__":
    sys.exit(main())
