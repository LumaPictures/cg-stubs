#!/bin/bash

set -e

REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/usd/stubs

# Custom variables --
export USD_BUILD_ROOT=~/dev/USD/.build-24.05-py39-manual-sigs
export USD_SOURCE_ROOT=~/dev/USD
# End custom variables --

# $USD_SOURCE_ROOT/docs/python is required to find doxygenlib
export USD_XML_INDEX="${USD_BUILD_ROOT}/docs/doxy_xml/index.xml"
export PYTHONPATH=$USD_BUILD_ROOT/lib/python:$USD_SOURCE_ROOT/docs/python
export PXR_USD_PYTHON_DISABLE_DOCS=1

# USD is a mixture of pure python (e.g. pxr.Sdf.__init__) and extension modules (pxr.Sdf._sdf), and
# the __init__ modules do runtime injection, so parsing these modules produces bad results..
#export UV_PYTHON=$(which python3)
uv run ./stubgen_usd.py $outdir

rm -f $outdir/pxr/*/_[a-z]*.pyi
rm -f $outdir/pxr/*/__DOC.pyi
