#!/bin/bash

# we have to force update stubgenlib because uv will only reinstall if the version
# changes.  I looked into creating dynamic versions using hatch-vcs but I could
# not get it to work.
uv sync --reinstall-package=stubgenlib
export PYTHONPATH=$(.venv/bin/python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')
/Applications/Autodesk/maya2026/Maya.app/Contents/bin/mayapy -m stubgen_maya ./stubs

#UV_PYTHON=/Applications/Autodesk/maya2026/Maya.app/Contents/bin/mayapy
#uv run ./stubgen_maya.py ./stubs
