# CG Stubs

## Python stubs for VFX and Animation

Supported libraries and applications.

- [USD](https://pypi.org/project/types-usd/)
- [houdini](https://pypi.org/project/types-houdini/)
- [katana](https://pypi.org/project/types-katana/)
- [mari](https://pypi.org/project/types-mari/)
- [nuke](https://pypi.org/project/types-nuke/)
- [opencolorio](https://pypi.org/project/types-opencolorio/)
- [PySide2](https://pypi.org/project/types-PySide2/)
- [substance_painter](https://pypi.org/project/types-substance_painter/)

For code completion and type analysis in Maya, [pymel](https://pypi.org/project/pymel/) has very excellent stubs included. 

## Installing

```
pip install types-usd types-houdini types-katana types-mari types-nuke types-opencolorio types-PySide2 types-substance_painter
```

## Generating the stubs

(replace ocio with your desired package to generate)

First, look at `ocio/stubgen_ocio.sh` to see if there are any env vars to set in the `# Custom variables` section.

Next, build it.  Requires python 3.7+:

```
python3 -m venv .venv
. .venv/bin/activate
pip install nox
nox -s 'generate(ocio)'
```

If this fails, here's a paranoid/foolproof approach:

```
# setup your env, e.g. setpkg python-3.7
unset PYTHONPATH
python3 -m venv .venv37
. .venv37/bin/activate
python3 -m pip install nox
rm -rf .nox
python3 -m nox -s 'generate(ocio)'
```


## Developing

This project uses [`nox`](https://nox.thea.codes/en/stable/index.html) as a build tool.

The folowing recipe will create an editable install of the stubs for the specified project, so that you can edit the files in place, and test the results in another project using mypy 
(if you're using the daemon, be sure to run `dmypy stop` to reread freshly modified stubs).

```
# activate the venv that you want to install into
. /path/to/.venv/bin/activate
pip install nox
nox -s 'develop(ocio)'
```

## Publishing to PyPI

To publish to pypi.org:

(replace ocio with the package to publish)

```
python3 -m venv .venv
. .venv/bin/activate
pip install nox
nox -s 'publish(ocio)'
```

To publish to a custom registry:

```
python3 -m venv .venv
. .venv/bin/activate
pip install nox poetry
poetry config repositories.pypi-nexus https://nexus.myorg/repository/pypi/
nox -s 'publish(ocio)' --  --repository pypi-nexus -u pypi -p 'whatever'
```
