#!/bin/bash

set -e

# User provided
export MARI_APP=/luma/soft/applications/Foundry/Linux-x86_64/mari/Mari$version
# we have to force update stubgenlib because uv will only reinstall if the version
# changes.  I looked into creating dynamic versions using hatch-vcs but I could
# not get it to work.
uv sync --reinstall-package=stubgenlib
export PYTHONPATH=$(.venv/bin/python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')

./maripy -c "import stubgen_mari;stubgen_mari.main('./stubs')" || true
