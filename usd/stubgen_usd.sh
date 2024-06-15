#!/bin/bash

set -e

PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/usd/stubs

# Custom variables --
export USD_BUILD_ROOT=~/dev/USD/.build-24.05-py39
export USD_SOURCE_ROOT=~/dev/USD
# End custom variables --

# $USD_SOURCE_ROOT/docs/python is required to find doxygenlib
export USD_XML_INDEX="${USD_BUILD_ROOT}/docs/doxy_xml/index.xml"
export PYTHONPATH=$REPO_PATH:$REPO_PATH/usd:$USD_BUILD_ROOT/lib/python:$USD_SOURCE_ROOT/docs/python:$PY_SITE_DIR
export PXR_USD_PYTHON_DISABLE_DOCS=1

# clean first, in case modules have been removed (or stubgen is silently failing)
find $outdir/pxr -name '*.pyi' -type f -delete

# USD is a mixture of pure python (e.g. pxr.Sdf.__init__) and extension modules (pxr.Sdf._sdf), and
# the __init__ modules do runtime injection, so parsing these modules produces bad results..
echo $(which python3)
python3 -c "import stubgen_usd;stubgen_usd.main('$outdir')"

rm -f $outdir/pxr/*/_[a-z]*.pyi
rm -f $outdir/pxr/*/__DOC.pyi
