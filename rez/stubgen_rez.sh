#!/bin/bash

_REZ_NO_KILLPG=1 uv run stubgen --include-private --include-docstrings -v -p rez -p rezplugins -o stubs

# run mypy in an environment that can't import rez source code
unset PYTHONPATH
uvx mypy | uvx mypy-silent
