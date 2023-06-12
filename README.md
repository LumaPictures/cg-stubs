# CG Stubs

Python stubs for VFX and Animation


## Developing

When developing the stubs it's useful to create an editable install.

Below are two ways to do this. 

### Manual install

```
# activate the venv that you want to install into
. /path/to/.venv/bin/activate
pip install poetry
cd nuke
poetry install
```

### Instlal using `nox`

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
