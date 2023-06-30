#!/bin/bash

set -e

REPO_PATH=$(git rev-parse --show-toplevel)

setpkg -c nuke-13

outdir=$REPO_PATH/nuke/stubs/

# using $NUKE_APP/python3 crashes in my latest tests
# must import nuke to make nuke modules available, but this consumes sys.argv, so we have to get a bit hacky
export PYTHONPATH=$REPO_PATH/../mypy

$REPO_PATH/nuke/bin/nukepy -c "import _nuke;import sys;sys.argv=['foo', '-o=$outdir', '-m', '_nuke', '-p', 'nuke_internal', '-m', '_curveknob', '-m', '_nuke_color', '-m', '_curvelib', '-m', '_geo', '-m', '_localization', '-m', '_splinewarp']; import mypy.stubgen;mypy.stubgen.main()"

sed -i 's/\bstring\b/str/g' $outdir/_nuke.pyi
sed -i 's/MenuorNone/Optional[Menu]/g' $outdir/_nuke.pyi
sed -i 's/\bBool\b/bool/g' $outdir/_nuke.pyi

rm -rf $outdir/nuke
mv $outdir/nuke_internal $outdir/nuke
#mv .out/* $outdir/
