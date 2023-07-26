#!/bin/bash
set -e

POINT_RELEASE=5

#pip install -U git+https://github.com/chadrik/mypy@stubgenc-all-fixes#mypy
# pip install -U -e ../mypy

echo $(which python)
PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/pyside/stubs/

# Custom variables --
MYPY_ROOT=$REPO_PATH/../mypy
# End custom variables --

export PYTHONPATH=$REPO_PATH:$REPO_PATH/pyside:$MYPY_ROOT:$PY_SITE_DIR

python -m stubgen_pyside -p shiboken2 -p PySide2 --include-private -o $outdir

echo -e "\nclass Object:\n    pass" >> $outdir/shiboken2/shiboken2.pyi
echo -e "__version__: str" >> $outdir/PySide2/__init__.pyi
echo -e "__version_info__: tuple[int, int, float, str, str]" >> $outdir/PySide2/__init__.pyi

#rm -rf ./PySide2-stubs
#mv ./.build/PySide2 ./PySide2-stubs
#rm -rf ./shiboken2-stubs
#mv ./.build/shiboken2 ./shiboken2-stubs

VERSION=$(python -c "import PySide2;print(PySide2.__version__)")
echo "$VERSION.$POINT_RELEASE" > ./VERSION
