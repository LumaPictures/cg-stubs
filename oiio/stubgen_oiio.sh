#!/bin/bash

set -e

PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/oiio/stubs/

OIIO_PYTHON_PATH=/usr/local/Cellar/openimageio/2.5.16.0_2/lib/python3.12/site-packages/

export PYTHONPATH=$REPO_PATH:$REPO_PATH/oiio:$PY_SITE_DIR:$OIIO_PYTHON_PATH

which python
python -m stubgen_oiio -p OpenImageIO -o $outdir
