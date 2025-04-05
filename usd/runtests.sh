REPO_PATH=$(git rev-parse --show-toplevel)

MYPY_ROOT=$REPO_PATH/../mypy
export USD_BUILD_ROOT=~/dev/USD/.build-py-sigs
export USD_SOURCE_ROOT=~/dev/USD_private_chadrik
export USD_XML_INDEX="${USD_BUILD_ROOT}/docs/doxy_xml/index.xml"
export PYTHONPATH=$REPO_PATH/common/src:$REPO_PATH/usd:$MYPY_ROOT:$USD_BUILD_ROOT/lib/python:$USD_SOURCE_ROOT/docs/python

pytest "$@"
