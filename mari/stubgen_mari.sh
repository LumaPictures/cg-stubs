#!/bin/bash

set -e

version=5

setpkg -c python-3 mari-$version

REPO_PATH=$(git rev-parse --show-toplevel)

outdir=$REPO_PATH/mari/stubs/

export PYTHONPATH=$REPO_PATH/../mypy:$REPO_PATH/core/python:$REPO_PATH/.venv-py37-linux/lib/python3.7/site-packages:$REPO_PATH/mari/bin/

${REPO_PATH}/mari/bin/maripy -c "import stubgen_mari;stubgen_mari.main(['-m', 'mari', '--verbose', '-o=.out'])"

mv .out/* $outdir/
