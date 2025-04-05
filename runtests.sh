
REPO_PATH=$(git rev-parse --show-toplevel)
# FIMXE:
MYPY_ROOT=$REPO_PATH/../mypy
export PYTHONPATH=$REPO_PATH/common/src:$REPO_PATH/usd:$MYPY_ROOT

pytest "$@"
