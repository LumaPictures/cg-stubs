#!/bin/bash

set -e

version=19.5

setpkg -c python-3 houdini-$version

# can't activate
#. .venv-py37-linux/bin/activate


outdir=$REPO_PATH/houdini/stubs/

export PYTHONPATH=$REPO_PATH/../mypy:$REPO_PATH/core/python:$REPO_PATH/.venv-py37-linux/lib/python3.7/site-packages:$REPO_PATH/houdini/bin/
export PATH=${REPO_PATH}/houdini/bin:${PATH}
hython -c "import stubgen_houdini;stubgen_houdini.main(['-m', 'hou', '--parse-only', '--verbose', '-o=.out'])"

mv .out/* $outdir/
