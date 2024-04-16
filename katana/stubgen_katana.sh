#!/bin/bash

set -e

version=$1
if [[ "$version" == "" ]]; then
  version=5.0v5
  echo "defaulting to $version"
fi

export REPO_PATH=$(git rev-parse --show-toplevel)

# Custom variables --
export KATANA_HOME=/luma/soft/applications/Foundry/Linux-x86_64/katana/Katana-$version
export PATH=$KATANA_HOME:$PATH
export foundry_LICENSE='4101@katanalicgui.luma.ninja:5053@katanarender.luma.ninja'
# End custom variables --

export PYTHONPATH=$REPO_PATH:$REPO_PATH/katana:$PY_SITE_DIR

sitedir=$KATANA_HOME/bin/python/
outdir=${REPO_PATH}/katana/stubs


if [[ ! -d ${REPO_PATH}/katana/stubs ]]; then
  mkdir ${REPO_PATH}/katana/stubs
fi

echo "Creating stubs"

# stubgen --include-private -o $outdir $tmpdir

${REPO_PATH}/katana/katanapy -c "import stubgen_katana;stubgen_katana.main('$outdir', '$sitedir')"

rm -rf $outdir/Katana/noxfile.pyi
#rm -rf $outdir/PyQt5
rm -rf $outdir/NodegraphAPI/Version/v_*
