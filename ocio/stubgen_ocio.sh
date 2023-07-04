#!/bin/bash

echo $(which python)
PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/ocio/stubs/

export PYTHONPATH=$REPO_PATH:$REPO_PATH/ocio:$REPO_PATH/../mypy/:$PY_SITE_DIR

#python -m mypy.stubgen -m PyOpenColorIO -o $outdir
python -m stubgen_ocio -m PyOpenColorIO -o $outdir
