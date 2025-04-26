#!/bin/bash

PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/rez/stubs/

export PYTHONPATH=$REPO_PATH/common/src:$REPO_PATH/rez:$PY_SITE_DIR

_REZ_NO_KILLPG=1 python -m mypy.stubgen --include-private --include-docstrings -v -p rez -p rezplugins -o $outdir

#mypy | mypy-silent
