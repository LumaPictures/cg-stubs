#!/usr/bin/env bash
# Generate the tde4 + vl_sdv stubs.
# Invoked by `nox -s 'generate(3dequalizer)'` (the custom-script branch), which
# loads .env first, so $TDE4_LLM_DOC and $TDE4_ROOT are available here.
set -euo pipefail

if [ -z "${TDE4_LLM_DOC:-}" ]; then
    echo "TDE4_LLM_DOC is not set (the tde4 Python Doc LLM JSON). Edit 3dequalizer/.env." >&2
    exit 1
fi
if [ -z "${TDE4_ROOT:-}" ]; then
    echo "TDE4_ROOT is not set (the 3DE install, for vl_sdv). Edit 3dequalizer/.env." >&2
    exit 1
fi

uv run --only-dev python stubgen_3dequalizer.py stubs
