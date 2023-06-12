#!/bin/bash

set -e

version=$1
# unfortunately, none of these completely work.  the first two fail to decompile
# a handful of files correctly, so it appears those will need to be fixed by hand.
# the third tries and fails to build pycdc with cmake.
disassembler='decompyle3'
# disassembler='uncompyle6'
disassembler='pydumpck'

if [[ "$version" == "" ]]; then
  echo "defaulting to 5.0v5 version"
  version=5.0v5
fi

sitedir=/luma/soft/applications/Foundry/Linux-x86_64/katana/Katana-$version/bin/python/
tmpdir=${REPO_PATH}/katana/stubs.tmp/$version-$disassembler
outdir=${REPO_PATH}/katana/stubs
procs=16

setpkg python-3
. .venv-py37-linux/bin/activate

if [[ ! -d ${REPO_PATH}/katana/stubs ]]; then
  mkdir ${REPO_PATH}/katana/stubs
fi

#if [[ -d $tmpdir ]]; then
#  echo "Skipping decompile stage"
#else
#  pip install $disassembler
#
#  for path in $(find $sitedir -mindepth 1 -maxdepth 1 -name '[A-Z]*' -type d)
#    do
#      module=$(basename $path)
#      # TODO: skip PyQt5
#      mkdir -p $tmpdir/$module
#      echo "Uncompiling pyc files in $path using $disassembler"
#      if [[ $disassembler == 'decompyle3' ]] ; then
#        decompyle3 -o $tmpdir/$module -r $path
#      elif [[ $disassembler == 'decompyle3' ]] ; then
#        uncompyle6 -o $tmpdir/$module --encoding utf-8 -r $path
#      else
#        for file in $(find $path -name '*.pyc' -type f)
#          do
#            pydumpck -o $tmpdir/$module $file
#          done
#      fi
#    done
#fi
#
## causes problems with mypy: Duplicate module named 'v0'
#rm -rf $tmpdir/UI4/software_python
## causes problems with stubgen: does not have an __init__
#rm -rf $tmpdir/Main
## causes many spurious mypy errors: not part of katana
#rm -rf $tmpdir/OpenGL $tmpdir/PyQt5
#
#echo "Fixing relative imports"
#futurize -j $procs -f libfuturize.fixes.fix_absolute_import -w -n --no-diffs $tmpdir
## this generates some syntax errors that need to be fixed
## convert  `from . import Foo.Bar` back to `import Foo.Bar`
#find $tmpdir -type f -exec sed -i -E 's/from \. import ([a-zA-Z][a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+) /import \1/g' {} \;
#
## FIXME: there's a bug with stubgen where it does not include private members
##  this would be easy to fix in the mypy.stubgen source, but for now...
#find $tmpdir -type f -exec sed -i -E 's/__all__ =/__all__disabled =/g' {} \;

# TODO: hook up typewriter here
# FIXME: running this with dmypy suggest is very very slow, but does improve the stubs
#   We can get even more improvement by adding epydoc support to typewriter
# cd katana/stubs.tmp
# dmypy run . -- --py2
# typewriter -w --command 'dmypy suggest --json --no-any --max-guesses=32 {filename}:{lineno}'  --annotation-style=py2 --verbose .

echo "Creating stubs"

# stubgen --include-private -o $outdir $tmpdir

setpkg -c katana-5

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

export PYTHONPATH=$REPO_PATH/../mypy/:$REPO_PATH/katana/bin
${REPO_PATH}/katana/bin/katanapy -c "import stubgen_katana;stubgen_katana.main(['-v', '--no-parse', $args])"

rm -rf $outdir/Katana/noxfile.pyi
#rm -rf $outdir/PyQt5
#rm -rf $outdir/NodegraphAPI/Version/v_*
