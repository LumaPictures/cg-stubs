#!/bin/bash

python3 -m pip install twine
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*
