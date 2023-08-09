#!/bin/bash

set -e

REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/substance_painter/stubs/

# this must be run inside the GUI
# import mypy.stubgen;mypy.stubgen.main(['-p', '_substance_painter'])

# stubgen --no-import $SUBSTANCE_PAINTER_ROOT/resources/python/modules/substance_painter/ --search-path $outdir

# mv out/substance_painter $outdir/

sed -i 's/\b_Number\b/Union[int, float]/g' $outdir/substance_painter/event.pyi
sed -i 's/from _typeshed import Incomplete/from typing import Union/g' $outdir/substance_painter/event.pyi

files="$outdir/substance_painter/*.pyi"
for file in $files
do
  echo $file
  name=$(basename "$file" .pyi)
  echo $name
  sed -i -E "s/\b([A-Z]+[a-z][a-zA-Z0-9_]+)[:] Incomplete/from _substance_painter.$name import \1 as \1/g" $file
done

# FIXME also need to replace PySide2.QtWidgets.QWidget with PySide2.QtCore.QObject in delete_ui_element
