Set-StrictMode -Version Latest

$ErrorActionPreference = "Stop"

# we have to force update stubgenlib because uv will only reinstall if the version
# changes.  I looked into creating dynamic versions using hatch-vcs but I could
# not get it to work.
uv sync --reinstall-package=stubgenlib
$env:PYTHONPATH =$(.venv/Scripts/python -c 'import sysconfig; print(sysconfig.get_paths()[\"purelib\"])')
& uvx --from=python-dotenv[cli] dotenv run -- mayapy -m stubgen_maya ./stubs
#echo "done"
# uvx mypy ./stubs | uvx mypy-silent
