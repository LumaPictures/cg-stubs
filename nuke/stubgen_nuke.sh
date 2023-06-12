#!/bin/bash

set -e

version=$1

# . .venv-py37-linux/bin/activate

#setpkg python-3
#setpkg -c nuke-$version


#which stubgen

#pip install -U mypy

outdir=$REPO_PATH/nuke/stubs/
$NUKE_APP/python3 $(which stubgen) -m _nuke -o $outdir
#$NUKE_APP/python3 -c "import _nuke;import sys;sys.argv=['foo', '-m', '_nuke']; import mypy.stubgen;mypy.stubgen.main()"

sed -i 's/\bstring\b/str/g' $outdir/_nuke.pyi
sed -i 's/MenuorNone/Optional[Menu]/g' $outdir/_nuke.pyi
sed -i 's/\bBool\b/bool/g' $outdir/_nuke.pyi

# must import nuke to make nuke modules available, but this consumes sys.argv, so we have to get a bit hacky
$NUKE_APP/python3 -c "import _nuke;import sys;sys.argv=['foo', '-p', 'nuke_internal', '-m', '_curveknob', '-m', '_nuke_color', '-m', '_curvelib', '-m', '_geo', '-m', '_localization', '-m', '_splinewarp']; import mypy.stubgen;mypy.stubgen.main()"

mv .out/nuke_internal $outdir/nuke
mv .out/* $outdir/
