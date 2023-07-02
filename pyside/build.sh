#!/bin/bash

python3 -m pip install build
rm -rf dist/*
python3 -m build --wheel
