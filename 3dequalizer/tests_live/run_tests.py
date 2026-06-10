"""Run the 3DEqualizer-only test suites with pytest, inside a real headless 3DEqualizer.

Launched by the 3DEqualizer executable:

    <3de-executable> -no_gui -run_script tests_live/run_tests.py

3DEqualizer has no standalone interpreter, so pytest runs *inside* the live
application against the genuine `tde4` and `vl_sdv` modules -- no mocks. It runs
every test in this folder; the generator unit tests live in `tests/` and run
standalone (they need `mypy`, absent from 3DE's python).

3DE's bundled python lacks our dev deps (pytest/typeguard/stubgenlib), so put
this project's virtualenv on PYTHONPATH before launching (see README).
"""

import os
import pathlib
import sys

import pytest


def main() -> int:
    project_dir = pathlib.Path.cwd()
    os.chdir(project_dir)

    return pytest.main(["tests_live", "--rootdir=."])


if __name__ == "__main__":
    sys.exit(main())
