#!/bin/bash
# Generate all of the Houdini stubs.  Run inside a Houdini environment, so that $HFS is set and
# hython is on the PATH, e.g.:
#   rez env houdini-22 -- ./stubgen_houdini.sh

set -e
cd "$(dirname "$0")"

PYTHON_VERSION=$(hython -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' </dev/null)
export PYTHONPATH=$PWD:$PWD/.venv/lib/python$PYTHON_VERSION/site-packages:$HFS/houdini/python${PYTHON_VERSION}libs

hython stubgen_houdini.py </dev/null
mv stubs/hou.pyi stubs/hou-stubs/__init__.pyi

# hython always exits 0, so the script reports its status in a file.
export STUBGEN_STATUS_FILE=$(mktemp)
trap 'rm -f "$STUBGEN_STATUS_FILE"' EXIT
hython stubgen_houdini_libs.py </dev/null
if [ "$(cat "$STUBGEN_STATUS_FILE")" != "0" ]; then
    echo "stubgen_houdini_libs.py failed" >&2
    exit 1
fi
