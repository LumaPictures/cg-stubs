#!/bin/bash
set -e

PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/pyside/stubs/

export PYTHONPATH=$REPO_PATH:$REPO_PATH/pyside:$PY_SITE_DIR

python -m stubgen_pyside -p shiboken2 -p PySide2 --include-private -o $outdir

echo -e "\nclass Object: ..." >> $outdir/shiboken2/shiboken2.pyi
echo -e "__version__: str" >> $outdir/PySide2/__init__.pyi
echo -e "__version_info__: tuple[int, int, float, str, str]" >> $outdir/PySide2/__init__.pyi
