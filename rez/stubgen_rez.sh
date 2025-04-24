#!/bin/bash

PY_SITE_DIR=$(python -c "import site,os;print(os.pathsep.join(site.getsitepackages()))")
REPO_PATH=$(git rev-parse --show-toplevel)
outdir=$REPO_PATH/rez/stubs/

export PYTHONPATH=$REPO_PATH/common/src:$REPO_PATH/rez:$PY_SITE_DIR

_REZ_NO_KILLPG=1 python -m mypy.stubgen --include-private --include-docstrings -v -p rez -p rezplugins -o $outdir

#python -m mypy.stubgen -v -o $outdir -m rez

#python -m mypy.stubgen -v -o $outdir -p rez.bind
#python -m mypy.stubgen -v -o $outdir -p rez.cli
#python -m mypy.stubgen -v -o $outdir -p rez.utils
#python -m mypy.stubgen -v -o $outdir -p rez.vendor
#python -m mypy.stubgen -v -o $outdir -p rez.version

#python -m mypy.stubgen -v -o $outdir -m rez.cli.__init__
#python -m mypy.stubgen -v -o $outdir -m rez.cli._complete_util
#python -m mypy.stubgen -v -o $outdir -m rez.cli._entry_points
#_REZ_NO_KILLPG=1 python -m mypy.stubgen -v -o $outdir -m rez.cli._main
#python -m mypy.stubgen -v -o $outdir -m rez.cli._util
#python -m mypy.stubgen -v -o $outdir -m rez.cli.benchmark
#python -m mypy.stubgen -v -o $outdir -m rez.cli.bind
#python -m mypy.stubgen -v -o $outdir -m rez.cli.build
#python -m mypy.stubgen -v -o $outdir -m rez.cli.bundle
#python -m mypy.stubgen -v -o $outdir -m rez.cli.complete
#python -m mypy.stubgen -v -o $outdir -m rez.cli.config
#python -m mypy.stubgen -v -o $outdir -m rez.cli.context
#python -m mypy.stubgen -v -o $outdir -m rez.cli.cp
#python -m mypy.stubgen -v -o $outdir -m rez.cli.depends
#python -m mypy.stubgen -v -o $outdir -m rez.cli.diff
#python -m mypy.stubgen -v -o $outdir -m rez.cli.env
#python -m mypy.stubgen -v -o $outdir -m rez.cli.forward
#python -m mypy.stubgen -v -o $outdir -m rez.cli.gui
#python -m mypy.stubgen -v -o $outdir -m rez.cli.help
#python -m mypy.stubgen -v -o $outdir -m rez.cli.interpret
#python -m mypy.stubgen -v -o $outdir -m rez.cli.memcache
#python -m mypy.stubgen -v -o $outdir -m rez.cli.mv
#python -m mypy.stubgen -v -o $outdir -m rez.cli.pip
#python -m mypy.stubgen -v -o $outdir -m rez.cli.pkgche.py
#python -m mypy.stubgen -v -o $outdir -m rez.cli.pkgnore.py
#python -m mypy.stubgen -v -o $outdir -m rez.cli.plugins
#python -m mypy.stubgen -v -o $outdir -m rez.cli.python
#python -m mypy.stubgen -v -o $outdir -m rez.cli.release
#python -m mypy.stubgen -v -o $outdir -m rez.cli.rm
#python -m mypy.stubgen -v -o $outdir -m rez.cli.search
#python -m mypy.stubgen -v -o $outdir -m rez.cli.selftest
#python -m mypy.stubgen -v -o $outdir -m rez.cli.status
#python -m mypy.stubgen -v -o $outdir -m rez.cli.suite
#python -m mypy.stubgen -v -o $outdir -m rez.cli.test
#python -m mypy.stubgen -v -o $outdir -m rez.cli.view

#python -m mypy.stubgen -v -o $outdir -m rez.build_process
#python -m mypy.stubgen -v -o $outdir -m rez.build_system
#python -m mypy.stubgen -v -o $outdir -m rez.bundle_context
#python -m mypy.stubgen -v -o $outdir -m rez.command
#python -m mypy.stubgen -v -o $outdir -m rez.config
#python -m mypy.stubgen -v -o $outdir -m rez.deprecations
#python -m mypy.stubgen -v -o $outdir -m rez.developer_package
#python -m mypy.stubgen -v -o $outdir -m rez.exceptions
#python -m mypy.stubgen -v -o $outdir -m rez.package_bind
#python -m mypy.stubgen -v -o $outdir -m rez.package_cache
#python -m mypy.stubgen -v -o $outdir -m rez.package_copy
#python -m mypy.stubgen -v -o $outdir -m rez.package_filter
#python -m mypy.stubgen -v -o $outdir -m rez.package_help
#python -m mypy.stubgen -v -o $outdir -m rez.package_maker
#python -m mypy.stubgen -v -o $outdir -m rez.package_move
#python -m mypy.stubgen -v -o $outdir -m rez.package_order
#python -m mypy.stubgen -v -o $outdir -m rez.package_py_utils
#python -m mypy.stubgen -v -o $outdir -m rez.package_remove
#python -m mypy.stubgen -v -o $outdir -m rez.package_repository
#python -m mypy.stubgen -v -o $outdir -m rez.package_resources
#python -m mypy.stubgen -v -o $outdir -m rez.package_search
#python -m mypy.stubgen -v -o $outdir -m rez.package_serialise
#python -m mypy.stubgen -v -o $outdir -m rez.package_test
#python -m mypy.stubgen -v -o $outdir -m rez.packages
#python -m mypy.stubgen -v -o $outdir -m rez.pip
#python -m mypy.stubgen -v -o $outdir -m rez.plugin_managers
#python -m mypy.stubgen -v -o $outdir -m rez.release_hook
#python -m mypy.stubgen -v -o $outdir -m rez.release_vcs
#python -m mypy.stubgen -v -o $outdir -m rez.resolved_context
#python -m mypy.stubgen -v -o $outdir -m rez.resolver
#python -m mypy.stubgen -v -o $outdir -m rez.rex
#python -m mypy.stubgen -v -o $outdir -m rez.rex_bindings
#python -m mypy.stubgen -v -o $outdir -m rez.rezconfig
#python -m mypy.stubgen -v -o $outdir -m rez.serialise
#python -m mypy.stubgen -v -o $outdir -m rez.shells
#python -m mypy.stubgen -v -o $outdir -m rez.solver
#python -m mypy.stubgen -v -o $outdir -m rez.status
#python -m mypy.stubgen -v -o $outdir -m rez.suite
#python -m mypy.stubgen -v -o $outdir -m rez.system
#python -m mypy.stubgen -v -o $outdir -m rez.util
#python -m mypy.stubgen -v -o $outdir -m rez.wrapper
