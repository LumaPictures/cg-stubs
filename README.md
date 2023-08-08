# CG Stubs

## Python stubs for VFX and Animation

These stubs are intended to be used with a type checker like [`mypy`](https://mypy.readthedocs.io/en/stable/) to provide [static type checking](https://realpython.com/python-type-checking/) of python code, as well as analysis and completion in IDEs like PyCharm and VSCode with Pylance.

Supported libraries and applications:

- [USD](https://pypi.org/project/types-usd/)
- [houdini](https://pypi.org/project/types-houdini/)
- [katana](https://pypi.org/project/types-katana/)
- [mari](https://pypi.org/project/types-mari/)
- [nuke](https://pypi.org/project/types-nuke/)
- [opencolorio](https://pypi.org/project/types-opencolorio/)
- [PySide2](https://pypi.org/project/types-PySide2/)
- [substance_painter](https://pypi.org/project/types-substance_painter/)

Note that [pymel](https://pypi.org/project/pymel/) now has very excellent stubs included (more info [here](https://dev.to/chadrik/pymels-new-type-stubs-2die)). 

## Installing

```
pip install types-usd types-houdini types-katana types-mari types-nuke types-opencolorio types-PySide2 types-substance_painter
```

## Generating the stubs

(replace ocio with your desired package to generate)

First, look at `ocio/stubgen_ocio.sh` to see if there are any env vars to set in the `# Custom variables` section.

Next, you'll need to check out a custom build of mypy (until my [PR](https://github.com/python/mypy/pull/15770) gets merged):

```
git clone https://github.com/LumaPictures/cg-stubs
git clone https://github.com/chadrik/mypy
cd mypy
git checkout stubgen/shared-sig-gen-14
```

Next, build the stubs using [`nox`](https://nox.thea.codes/en/stable/index.html).  Requires python 3.7+:

```
cd cg-stubs
python3 -m venv .venv
. .venv/bin/activate
pip install -r nox-requirements.txt
nox -s 'generate(ocio)'
```

If this fails, here's a more foolproof approach:

```
# setup your env, e.g. setpkg python-3.7
unset PYTHONPATH
python3 -m venv .venv37
. .venv37/bin/activate
python3 -m pip install -r nox-requirements.txt
rm -rf .nox
python3 -m nox -s 'generate(ocio)'
```


## Developing

The easiest way to test stubs while you're devleoping them is to create an editable install.  Simply create a `.pth` file in your site-packages directory:

```
echo "/path/to/cg-stubs/ocio/stubs/" > /path/to/venv/lib/python3.7/site-packages/ocio.pth
```

The name of the .pth file does not matter.  Note that if you're using the mypy daemon, be sure to run `dmypy stop` to reread freshly modified stubs.

## Publishing to PyPI

To publish to pypi.org, first run the nox installation steps from the Generating section, then:

(replace ocio with the package to publish)

```
nox -s 'publish(ocio)'
```

To publish to a custom registry:

```
poetry config repositories.pypi-nexus https://nexus.myorg/repository/pypi/
nox -s 'publish(ocio)' --  --repository pypi-nexus -u pypi -p 'whatever'
```
