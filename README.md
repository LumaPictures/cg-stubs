# CG Stubs

Python stubs for VFX and Animation

Supported applications
- houdini
- katana
- mari
- nuke
- substance_painter

See also:
- pymel
- pyside2

## Installing

```
pip install types-houdini types-katana types-mari types-nuke types-substance_painter
```

## Developing

When developing the stubs it is convenient to create an editable install, so that you can edit the files in place.  This is confirmed to work with `mypy`.

Below are two ways to create an editable install.

### Manual install

```
# activate the venv that you want to install into
. /path/to/.venv/bin/activate
pip install poetry
cd nuke
poetry install
```

### Install using `nox`

`nox` is a powerful build tool inspired by `tox`.

```
# activate the venv that you want to install into
. /path/to/.venv/bin/activate
pip install nox
nox -s 'develop(nuke)'
```

## Publishing to PyPI

To publish to pypi.org:

```
python3 -m venv .venv
. .venv/bin/activate
pip install nox
nox -s 'publish(nuke)'
```

To publish to a custom registry:

```
python3 -m venv .venv
. .venv/bin/activate
pip install nox poetry
poetry config repositories.pypi-nexus https://nexus.myorg/repository/pypi/
nox -s 'publish(nuke)' --  --repository pypi-nexus -u pypi -p 'whatever'
```
