import nox

import pathlib

APPS = [
    "houdini",
    "katana",
    "mari",
    "nuke",
    "substance_painter",
]
PARAMS = [
    nox.param(x, id=x) for x in APPS
]


# TODO: generate pyproject.toml from a jinja template

def add_stubs_suffix(path: pathlib.Path):
    for child in path.iterdir():
        if '-stubs' not in child.name:
            name = child.stem + '-stubs'
            if child.is_file():
                name += '.pyi'
            newpath = child.with_name(name)
            print(f"Renaming to {newpath}")
            child.rename(newpath)


@nox.session(venv_backend='none')
@nox.parametrize('lib', PARAMS)
def develop(session: nox.Session, lib: str):
    session.chdir(lib)
    # must use poetry that is installed in the destination venv
    session.run("poetry", "install", external=True)


@nox.session(reuse_venv=True)
@nox.parametrize('lib', PARAMS)
def publish(session: nox.Session, lib: str):
    session.chdir(lib)
    session.install("poetry")
    session.run("poetry", "publish", *session.posargs)
