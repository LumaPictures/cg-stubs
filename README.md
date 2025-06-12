# CG Stubs

## Python stubs for VFX and Animation

These stubs are intended to be used with a type checker like [`mypy`](https://mypy.readthedocs.io/en/stable/) to provide [static type checking](https://realpython.com/python-type-checking/) of python code, as well as analysis and completion in IDEs like PyCharm and VSCode with Pylance.

Supported libraries and applications:

- [USD](https://pypi.org/project/types-usd/)
- [houdini](https://pypi.org/project/types-houdini/)
- [katana](https://pypi.org/project/types-katana/)
- [mari](https://pypi.org/project/types-mari/)
- [maya](https://pypi.org/project/types-maya-strict/)
- [nuke](https://pypi.org/project/types-nuke/)
- [opencolorio](https://pypi.org/project/types-opencolorio/)
- [PySide2](https://pypi.org/project/types-PySide2/)
- [substance_painter](https://pypi.org/project/types-substance_painter/)

Note that [pymel](https://pypi.org/project/pymel/) now has very excellent stubs included (more info [here](https://dev.to/chadrik/pymels-new-type-stubs-2die)). 

## Installing

These are distributed as "stubs-only" python packages, so you can just `pip install` whichever packages you need:

```
pip install types-usd types-houdini types-katana types-mari types-nuke types-opencolorio types-PySide2 types-substance_painter
```

## Generating the stubs

You only need to do this if your goal is to help improve the stubs. Otherwise, just use `pip`, 
as explained above.

Building the stubs requires python 3.9 or greater.

### Step 1: Install `nox`

You can do this using [`pipx`](https://github.com/pypa/pipx):

```bash
pipx install nox
```

Or by creating a virtualenv:

```bash
cd cg-stubs
python3 -m venv .venv
. .venv/bin/activate
pip install nox
nox -h
```

### Step 2: Configure your environment

Look at the `.env` file within the project that you want to build. Either uncomment the necessary 
environment variables and paste in the proper values, or configure your shell environment to set
these variables before the next step, for example using a package manager like `rez`.

### Step 3: Run the generate task

Replace `maya` with the project you want to build: 

```bash
nox -s 'generate(maya)'
```


### Testing while Developing

The easiest way to use the stubs while you're devleoping them is to create an editable install.  
Simply create a `.pth` file in the site-packages directory of the venv where your other deps live:

```
echo "/path/to/cg-stubs/maya/stubs/" > /path/to/venv/lib/python3.7/site-packages/maya.pth
```

The name of the .pth file does not matter.  
Note that if you're using the mypy daemon, be sure to run `dmypy stop` to reread freshly modified stubs.

### Generating the USD stubs

The USD stubs currently require you to build a special fork of USD, until the necessary changes are merged.

```
git clone https://github.com/chadrik/USD
git checkout doc-stubs2
python3.9 -m venv .venv
. .venv/bin/activate
pip install PySide6 PyOpenGL
python3.9 build_scripts/build_usd.py --python-docs --docs .build-23.08-py39
```

Then update the variables in `stubgen_usd.sh` and generate as normal.

### Generating the Substance Painter stubs

These must be generated from within the UI, because I could not figure out how to run a standlone interpreter.

```
import mypy.stubgen;mypy.stubgen.main(['-p', '_substance_painter'])
```

Then generate as normal to cleanup the stubs.

### Generating the Houdini stubs

The Houdini stubs currently use a completely different approach to building which will eventually be ported to `nox`.  So this may be unapproachable for most users for now.


## Publishing to PyPI

To publish to pypi.org, first run the nox installation steps from the Generating section, then run 
the `publish` task (replacing `maya` with the package to publish):

```
nox -s 'publish(maya)'
```
