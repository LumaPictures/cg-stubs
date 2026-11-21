"""Report the bare generics (`dict`, `list`, `Callable`, ...) in the generated stubs.

mypy only finds `*-stubs` packages in site-packages, so this builds the wheel, installs it into
a throwaway venv and runs mypy's `--disallow-any-generics` over every stub package there.
Needs `uv` on the PATH (e.g. `rez env proto_env -- .venv/bin/python check_stub_generics.py`).
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).parent
TYPE_ARG = re.compile(r"site-packages/(.*)\[type-arg\]$")


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        dist = pathlib.Path(tmp) / "dist"
        venv = pathlib.Path(tmp) / "venv"
        subprocess.run(["uv", "build", "--wheel", "-o", str(dist)], cwd=HERE, check=True)
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        subprocess.run(["uv", "venv", "-q", "--python", python_version, str(venv)], check=True)
        python = venv / "bin" / "python"
        wheel = next(dist.glob("*.whl"))
        subprocess.run(
            ["uv", "pip", "install", "-q", "--python", str(python), str(wheel), "mypy"], check=True
        )
        packages = sorted(p.name.removesuffix("-stubs") for p in (HERE / "stubs").glob("*-stubs"))
        result = subprocess.run(
            [
                str(python), "-m", "mypy", "--python-version", python_version,
                "--disallow-any-generics", "--no-incremental", "--show-error-codes",
                "--no-pretty", "--hide-error-context",
                *(arg for package in packages for arg in ("-p", package)),
            ],
            cwd=tmp,
            capture_output=True,
            text=True,
        )
    errors = [m.group(1) for line in result.stdout.splitlines() if (m := TYPE_ARG.search(line))]
    print("\n".join(errors))
    print(f"{len(errors)} bare generics")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
