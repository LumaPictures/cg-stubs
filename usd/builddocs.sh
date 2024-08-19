#!/bin/bash

set -e

if [ ! -e .venv-buildusd-39 ]; then
  python3.9 -m venv .venv-buildusd-39
fi
. .venv-buildusd-39/bin/activate

USD_SOURCE_ROOT=/Users/chad/dev/USD
BASE_USD_BUILD=~/dev/USD/.build-24.05-py39-stock
#export CMAKE_INSTALL_PREFIX=/Users/chad/dev/USD/.build-24.05-py39
export CMAKE_INSTALL_PREFIX=/Users/chad/dev/USD/.build-24.05-py39-manual-sigs
#export CMAKE_INSTALL_PREFIX=/Users/chad/dev/USD/.build-24.05-py39-stock

export BUILT_XML_DOCS="${CMAKE_INSTALL_PREFIX}/docs/doxy_xml"
export INSTALL_PYTHON_PXR_ROOT="${CMAKE_INSTALL_PREFIX}/lib/python"

existing=$(find $INSTALL_PYTHON_PXR_ROOT/pxr -type f -name '__DOC.py')
rm -rf $existing

modules=$(find $INSTALL_PYTHON_PXR_ROOT/pxr -type d -d 1 -name '[A-Z]*' -exec basename {} \;  | tr '\n' ',')
#modules="Sdf"

# -m cProfile -o convertDoxygen.prof
cd $USD_SOURCE_ROOT
python3.9 ./docs/python/convertDoxygen.py \
        --package pxr --module $modules \
        --inputIndex ${BUILT_XML_DOCS}/index.xml \
        --pythonPath ${CMAKE_INSTALL_PREFIX}/lib/python \
        --output $INSTALL_PYTHON_PXR_ROOT/pxr


#diff --color -u $BASE_USD_BUILD/lib/python/pxr/Sdf/__DOC.py $INSTALL_PYTHON_PXR_ROOT/pxr/Sdf/__DOC.py
#diff --color -u $BASE_USD_BUILD/lib/python/pxr/Usd/__DOC.py $INSTALL_PYTHON_PXR_ROOT/pxr/Usd/__DOC.py
