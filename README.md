# CG Stubs

## Python stubs for VFX and Animation

Supported libraries and applications.

- USD
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
pip install types-usd types-houdini types-katana types-mari types-nuke types-substance_painter
```

## Developing

When developing the stubs it is convenient to create an editable install, so that you can edit the files in place.
Below are two ways to create an editable install (these are confirmed to work with `mypy`).

### Manual install

(replace nuke with the package to develop)

```
# activate the venv that you want to install into
. /path/to/.venv/bin/activate
pip install poetry
cd ./nuke
poetry install
```

### Install using `nox`

`nox` is a powerful build tool inspired by `tox`.

(replace nuke with the package to develop)

```
# activate the venv that you want to install into
. /path/to/.venv/bin/activate
pip install nox
nox -s 'develop(nuke)'
```

## Publishing to PyPI

To publish to pypi.org:

(replace nuke with the package to publish)

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
