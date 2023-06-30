#!/bin/bash

#
set -e

version=$1

# . .venv-py37-linux/bin/activate

#setpkg -c substancepainter-$version

outdir=$REPO_PATH/substancepainter/stubs/

# this must be run inside the GUI
# import mypy.stubgen;mypy.stubgen.main(['-p', '_substance_painter'])

# stubgen --no-import $SUBSTANCE_PAINTER_ROOT/resources/python/modules/substance_painter/ --search-path $outdir

# mv out/substance_painter $outdir/

sed -i 's/\b_Number\b/Union[int, float]/g' $outdir/substance_painter/event.pyi
sed -i 's/from _typeshed import Incomplete/from typing import Union/g' $outdir/substance_painter/event.pyi

# I hate bash.  this doesn't work.  rewrite in python
#replace=$(cat <<- EOM
#typing.Union[
#    bool,
#    int,
#    typing.Tuple[int, int],
#    typing.Tuple[int, int, int],
#    typing.Tuple[int, int, int, int],
#    float,
#    typing.Tuple[float, float],
#    typing.Tuple[float, float, float],
#    typing.Tuple[float, float, float,float],
#    str
#]
#EOM
#
#)
#
#echo "$replace"
#sed -i -E "s/PropertyValue[:] Incomplete/${replace//$'\n'/\\n}/g" $outdir/substance_painter/properties.pyi


files="$outdir/substance_painter/*.pyi"
for file in $files
do
  echo $file
  name=$(basename "$file" .pyi)
  echo $name
  sed -i -E "s/\b([A-Z]+[a-z][a-zA-Z0-9_]+)[:] Incomplete/from _substance_painter.$name import \1 as \1/g" $file
done

# FIXME also need to replace PySide2.QtWidgets.QWidget with PySide2.QtCore.QObject in delete_ui_element
