#!/bin/bash

# the current problems:

# 1
# The __init__ from all of the Array types (PathArray, TimeCodeArray, AssetPathArray, etc)
# have ugly docstrings, and bad stub overloads.

# - For the docstrings:  need to check if the __init__ methods are being visited by doxygenlib
# - For the stubs:  may require special handling in stubgen. These classes all have _isVtArray class attribute.

# 2
# when omitting the change to remove manually provided signatures, stubgen is making multiple overloads for functions.
# we probably don't want to include the change to remove manually sigs, so we need to fix this.
# take Sdf.Spec.HasInfo as an example.


BASE_BUILD=~/dev/USD/.build-24.05-py39-stock
COMPARE_BUILD=~/dev/USD/.build-24.05-py39-manual-sigs

#diff --color -u ~/dev/USD/.build-24.05-py39-stock/lib/python/pxr/Sdf/__DOC.py ~/dev/USD/.build-24.05-py39/lib/python/pxr/Sdf/__DOC.py

modules=$(find $BASE_BUILD/lib/python/pxr -type d -d 1 -name '[A-Z]*' -exec basename {} \;  | tr '\n' ',')

PYTHONPATH=$BASE_BUILD/lib/python python3.9 -c "import pxr.Sdf as Sdf;help(Sdf)" > Sdf-base.txt
PYTHONPATH=$COMPARE_BUILD/lib/python python3.9 -c "import pxr.Sdf as Sdf;help(Sdf)" > Sdf-compare.txt

diff --color -u Sdf-base.txt Sdf-compare.txt
