#!/bin/bash

set -e

PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/openexr/stubs/

export PYTHONPATH=$REPO_PATH:$REPO_PATH/openexr:$PY_SITE_DIR

which python
python -m stubgen_openexr -m OpenEXR -o $outdir
