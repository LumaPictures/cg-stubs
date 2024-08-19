#!/bin/bash

set -e

if [ ! -e .venv-buildusd-39 ]; then
  python3.9 -m venv .venv-buildusd-39
fi
. .venv-buildusd-39/bin/activate
pip install PySide6 PyOpenGL
cd "${USD_SOURCE_ROOT}"
python3.9 build_scripts/build_usd.py --python-docs --docs .build-24.05-py39-manual-sigs
