#!/bin/bash

set -e

#version=$1
#if [[ "$version" == "" ]]; then
#  version="5.0v4"
#  echo "defaulting to $version"
#fi

# User provided
#export MARI_APP=/luma/soft/applications/Foundry/Linux-x86_64/mari/Mari$version
#export HHP=/Applications/Houdini/Houdini20.5.332/Frameworks/Houdini.framework/Versions/20.5/Resources/houdini/python3.11libs
#export PATH=$MARI_APP:$PATH
PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")

HOU_LIBS=/Applications/Houdini/Houdini20.5.332/Frameworks/Houdini.framework/Versions/20.5/Resources/houdini/python3.11libs
PYTHON=/Applications/Houdini/Houdini20.5.332/Frameworks/Python.framework/Versions/3.11/bin/python3.11

REPO_PATH=$(git rev-parse --show-toplevel)

outdir=$REPO_PATH/houdini/stubs/

#export PYTHONPATH=$REPO_PATH:$REPO_PATH/houdini:$HOU_LIBS
export PYTHONPATH=$REPO_PATH:$REPO_PATH/houdini:$PY_SITE_DIR:$HOU_LIBS

echo "launching"
export DYLD_INSERT_LIBRARIES=/Applications/Houdini/Houdini20.5.332/Frameworks/Houdini.framework/Versions/Current/Houdini
$PYTHON -c "import stubgen_houdini;stubgen_houdini.main('$outdir')" || true
#$PYTHON -c "import hou" || true
