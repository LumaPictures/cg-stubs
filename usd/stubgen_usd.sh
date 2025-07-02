#!/bin/bash

set -e

REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/usd/stubs

echo $PYTHONPATH

# USD is a mixture of pure python (e.g. pxr.Sdf.__init__) and extension modules (pxr.Sdf._sdf), and
# the __init__ modules do runtime injection, so parsing these modules produces bad results..
#export UV_PYTHON=$(which python3)
uv run ./stubgen_usd.py $outdir

rm -f $outdir/pxr/*/_[a-z]*.pyi
rm -f $outdir/pxr/*/__DOC.pyi
