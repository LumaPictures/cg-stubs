# Unofficial python stubs for Adobe Substance 3D Painter

These stubs are designed to be used with a type checker like `mypy` to provide static type checking of python code, as well as to provide analysis and completion in IDEs like PyCharm and VSCode (with Pylance).

## Installing

```commandline
pip install types-substance_painter
```

The version of the package corresponds to the version of Substance Painter that it is generated from,
plus a version suffix for the revision of the stubs.

## Generating

`stubgen_substance_painter.sh` requires preliminary steps before it can be run. Do these two tasks:

### Extract stubs from running Substance Painter

The `_substance_painter` modules are accessible within Substance Painter. You'll need to run stubgen from inside the console. Mypy by default launches a subprocess when doing stubgen, which isn't what we want. So we patch that behavior with `common\src\stubgenlib\moduleinspect.py`. For that to work, you'll need to ensure that your Mypy install is pure-python.

```
# Ensure our mypy is the same version as substance, so we'll be able to import it.
cd cg-stubs/substance_painter && uv sync --python 3.11
# launch painter in the root directory
painter
```

Within painter:

```
import sys; sys.path.append("substance_painter/.venv/Lib/site-packages")
import stubgenlib.moduleinspect; stubgenlib.moduleinspect.patch()
import mypy.stubgen; mypy.stubgen.main(['-p', '_substance_painter', '-o', 'substance_painter/stubs'])
```

* `sys.path.insert(0, ".venv/Lib/site-packages")` to put our mypy install on path.
* `moduleinspect.patch()` patches mypy to run in-process rather than in-subprocess.
* `mypy.stubgen.main(['-p', '_substance_painter', '-o', 'substance_painter/stubs'])` tells mypy to import the `_substance_painter` package and output it to `substance_painter/stubs`.

### Extract stubs from the Substance Painter folder

In the root of the repository, run:
```
uv run --directory substance_painter stubgen --no-import $SUBSTANCE_PAINTER_ROOT/resources/python/modules/substance_painter/ --search-path ./stubs -o ./stubs
```

* set `$SUBSTANCE_PAINTER_ROOT` to the substance painter install directory.
* `--search-path` to find the `_substance_painter/` files
* `-o` to output to the stubs folder

### Run nox target

```
nox -s 'generate(substance_painter)'
```