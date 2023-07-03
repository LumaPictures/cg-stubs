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
${REPO_PATH}/mari/maripy -c "import mypy.stubgen;mypy.stubgen.main(['-p=Mari', '--verbose', '--parse-only', '-o=$outdir'])" || true
rm -rf $outdir/mari-stubs
mv $outdir/Mari $outdir/mari-stubs

echo "converting mari.so"
# c module
${REPO_PATH}/mari/maripy -c "import stubgen_mari;stubgen_mari.main(['-m=mari', '--verbose', '-o=$outdir'])"
mv $outdir/mari.pyi $outdir/mari-stubs/__init__.pyi
