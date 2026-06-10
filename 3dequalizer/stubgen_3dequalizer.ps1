# Generate the tde4 + vl_sdv stubs.
# Invoked by `nox -s 'generate(3dequalizer)'` (the custom-script branch), which
# loads .env first, so $env:TDE4_LLM_DOC and $env:TDE4_ROOT are available here.
$ErrorActionPreference = "Stop"

if (-not $env:TDE4_LLM_DOC) {
    Write-Error "TDE4_LLM_DOC is not set (the tde4 Python Doc LLM JSON). Edit 3dequalizer/.env."
    exit 1
}
if (-not $env:TDE4_ROOT) {
    Write-Error "TDE4_ROOT is not set (the 3DE install, for vl_sdv). Edit 3dequalizer/.env."
    exit 1
}

uv run --only-dev python stubgen_3dequalizer.py stubs
exit $LASTEXITCODE
