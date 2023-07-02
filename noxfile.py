import nox
import nox.command

import pathlib

APPS = [
    "houdini",
    "katana",
    "mari",
    "nuke",
    "pyside",
    "substance_painter",
    "usd",
]
PARAMS = [nox.param(x, id=x) for x in APPS]


# TODO: generate pyproject.toml from a jinja template


def add_stubs_suffix(path: pathlib.Path) -> None:
    import shutil

    # do these at the end to improve time to git refresh
    to_delete = []
    for child in path.iterdir():
        if '-stubs' not in child.name:
            name = child.stem + '-stubs'
            if child.is_file():
                name += '.pyi'
            newpath = child.with_name(name)
            if newpath.exists():
                if newpath.is_file():
                    newpath.unlink()
                else:
                    backup = newpath.with_suffix(".bak")
                    newpath.rename(backup)
                    to_delete.append(backup)
            print(f"Renaming to {newpath}")
            child.rename(newpath)
    for dir in to_delete:
        shutil.rmtree(dir)


@nox.session(venv_backend='none')
@nox.parametrize('lib', PARAMS)
def develop(session: nox.Session, lib: str) -> None:
    session.chdir(lib)
    try:
        session.run("poetry", "install", external=True)
    except nox.command.CommandFailed as err:
        msg = str(err)
        if "poetry" in msg:
            print("You must install poetry>=1.3.2 in the destination venv")
        raise


@nox.session(reuse_venv=True)
@nox.parametrize('lib', PARAMS)
def publish(session: nox.Session, lib: str) -> None:
    session.chdir(lib)
    session.install("poetry")
    session.run("poetry", "publish", *session.posargs)


@nox.session(reuse_venv=True)
@nox.parametrize('lib', PARAMS)
def generate(session: nox.Session, lib: str) -> None:
    session.install("-r", "requirements.txt")

    if lib == "pyside":
        session.install("PySide2==5.15.2.1")

    session.chdir(lib)
    session.run(f"./stubgen_{lib}.sh", external=True)
    session.chdir("stubs")
    # add_stubs_suffix(pathlib.Path("."))


@nox.session(reuse_venv=True)
@nox.parametrize('lib', PARAMS)
def mypy(session: nox.Session, lib: str) -> None:
    session.chdir(lib)
    session.install("mypy==1.4.1")
    session.run("mypy", "stubs")
