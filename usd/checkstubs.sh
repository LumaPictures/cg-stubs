#!/bin/bash

export USD_SOURCE_ROOT=~/dev/USD_private_chadrik

dmypy run -- stubs $USD_SOURCE_ROOT/pxr/base/gf/testenv $USD_SOURCE_ROOT/pxr/base/vt/testenv
