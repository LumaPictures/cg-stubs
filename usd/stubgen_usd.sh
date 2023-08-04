#!/bin/bash

set -e

REPO_PATH=$(git rev-parse --show-toplevel)

# Custom variables --
MYPY_ROOT=$REPO_PATH/../mypy
export USD_BUILD_ROOT=~/dev/USD/.build-py-sigs
export USD_SOURCE_ROOT=~/dev/USD_private_chadrik
# End custom variables --

export USD_XML_INDEX="${USD_BUILD_ROOT}/docs/doxy_xml/index.xml"
export PYTHONPATH=$REPO_PATH:$REPO_PATH/usd:$MYPY_ROOT:$USD_BUILD_ROOT/lib/python:$USD_SOURCE_ROOT/docs/python

outdir=$REPO_PATH/usd/stubs

# USD is a mixture of pure python (e.g. pxr.Sdf.__init__) and extension modules (pxr.Sdf._sdf), and
# the __init__ modules do runtime injection, so parsing these modules produces bad results..
echo $(which python3)
python3 -c "import stubgen_usd;stubgen_usd.main('$outdir')"

rm -f $outdir/pxr/*/_[a-z]*.pyi
rm -f $outdir/pxr/*/__DOC.pyi
