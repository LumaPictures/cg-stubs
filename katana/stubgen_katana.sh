#!/bin/bash

set -e

version=$1
if [[ "$version" == "" ]]; then
  version=5.0v5
  echo "defaulting to $version"
fi

# User provided
export KATANA_HOME=/luma/soft/applications/Foundry/Linux-x86_64/katana/Katana-$version
export PATH=$KATANA_HOME:$PATH
export foundry_LICENSE='4101@katanalicgui.luma.ninja:5053@katanarender.luma.ninja'


PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
export REPO_PATH=$(git rev-parse --show-toplevel)
export PYTHONPATH=$REPO_PATH:$REPO_PATH/katana:$REPO_PATH/../mypy/:$PY_SITE_DIR

sitedir=$KATANA_HOME/bin/python/
tmpdir=${REPO_PATH}/katana/stubs.tmp/$version-$disassembler
outdir=${REPO_PATH}/katana/stubs


if [[ ! -d ${REPO_PATH}/katana/stubs ]]; then
  mkdir ${REPO_PATH}/katana/stubs
fi

echo "Creating stubs"

# stubgen --include-private -o $outdir $tmpdir

args="'-o=$outdir'"

modules=( _FnKatanaCoreUI drawing_cmodule AssetAPI_cmodule ConfigurationAPI_cmodule PyFCurve \
          PyFnAttribute PyFnGeolib PyFnGeolibProducers PyFnGeolibServices \
          PyOpenColorIO PyResolutionTableFn PyXmlIO NodegraphAPI_cmodule Nodes2DAPI_cmodule Nodes3DAPI_cmodule RenderingAPI_cmodule )

for module in "${modules[@]}"
  do
    args="$args, '-p=$module'"
done

for path in $(find $sitedir -mindepth 1 -maxdepth 1 -name '[A-Z]*' -type d)
  do
    module=$(basename $path)
    # FIXME: this no work
    if [[ $module =~ "PyQt5" ]]; then
      continue
    fi
    args="$args, '-p=$module'"
done

echo $args

${REPO_PATH}/katana/katanapy -c "import stubgen_katana;stubgen_katana.main(['-v', '--no-parse', $args])"

rm -rf $outdir/Katana/noxfile.pyi
#rm -rf $outdir/PyQt5
#rm -rf $outdir/NodegraphAPI/Version/v_*
