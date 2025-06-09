#!/bin/bash

_REZ_NO_KILLPG=1 uv run stubgen --include-private --include-docstrings -v -p rez -p rezplugins -o stubs
