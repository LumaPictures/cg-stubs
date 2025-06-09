#!/bin/bash

PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/maya/stubs/

export PYTHONPATH=$REPO_PATH/common/src:$REPO_PATH/maya:$PY_SITE_DIR

#python -m mypy.stubgen -m PyOpenColorIO -o $outdir

#/Applications/Autodesk/maya2026/Maya.app/Contents/bin/mayapy -m mypy.stubgen -p maya.app -o $outdir --parse-only
#/Applications/Autodesk/maya2026/Maya.app/Contents/bin/mayapy -m stubgen_maya -m maya.cmds -m maya.app.commands -p maya.api -o $outdir --inspect-mode

/Applications/Autodesk/maya2026/Maya.app/Contents/bin/mayapy -m stubgen_maya $outdir
