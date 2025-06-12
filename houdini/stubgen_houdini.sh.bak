#!/bin/bash

set -e

HOU_LIBS=$REZ_HOUDINI_ROOT/python3.11libs
export UV_PYTHON=/opt/local_packages/houdini/20.5.487/platform-linux/bin/hython
export DYLD_INSERT_LIBRARIES=/Applications/Houdini/Houdini20.5.332/Frameworks/Houdini.framework/Versions/Current/Houdini
export PYTHONPATH=$HOU_LIBS

echo "launching"

uv run ./stubgen_houdini.py || true
