#!/bin/bash

set -e

version=$1
if [[ "$version" == "" ]]; then
  version="5.0v4"
  echo "defaulting to $version"
fi

# User provided
export MARI_APP=/luma/soft/applications/Foundry/Linux-x86_64/mari/Mari$version
export foundry_LICENSE='5053@foundrylic.luma.ninja'

export PATH=$MARI_APP:$PATH
PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)

outdir=$REPO_PATH/mari/stubs/

export PYTHONPATH=$REPO_PATH:$REPO_PATH/mari:$REPO_PATH/../mypy/:$PY_SITE_DIR


echo "converting Mari"
# py modules
${REPO_PATH}/mari/maripy -c "import mypy.stubgen;mypy.stubgen.main('$outdir')"
