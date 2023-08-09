#!/bin/bash

PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/ocio/stubs/

# Custom variables --
MYPY_ROOT=$REPO_PATH/../mypy
# End custom variables --

export PYTHONPATH=$REPO_PATH:$REPO_PATH/ocio:$MYPY_ROOT:$PY_SITE_DIR

#python -m mypy.stubgen -m PyOpenColorIO -o $outdir
python -m stubgen_ocio -m PyOpenColorIO -o $outdir
