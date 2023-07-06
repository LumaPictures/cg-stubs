import nox
import nox.command

import contextlib
import pathlib
import subprocess

APPS = [
    "houdini",
    "katana",
    "mari",
    "nuke",
    "ocio",
    "pyside",
    "substance_painter",
    "usd",
]
PARAMS = [nox.param(x, id=x) for x in APPS]


# TODO: generate pyproject.toml from a jinja template


def make_packages(path: pathlib.Path = pathlib.Path(".")) -> None:
    """Place single file modules into packages.

    As far as I can tell, stub-only modules are not supported by mypy.
    """
    for child in path.iterdir():
        if child.is_file() and child.suffix == ".pyi" and "-stubs" not in child.name:
            pkgdir = child.parent / child.stem
            if not pkgdir.exists():
                pkgdir.mkdir()
            child.rename(pkgdir / "__init__.pyi")
        elif child.is_dir():
            marker = child / "py.typed"
            marker.touch()


def add_stubs_suffix(path: pathlib.Path) -> None:
    import shutil

    # do these at the end to improve time to git refresh
    to_delete = []
    for child in path.iterdir():
        if child.is_dir() and not child.name.endswith('-stubs'):
            name = child.stem + '-stubs'
            newpath = child.with_name(name)
            if newpath.exists():
                backup = newpath.with_suffix(".bak")
                newpath.rename(backup)
                to_delete.append(backup)
            print(f"Renaming to {newpath}")
            child.rename(newpath)
    for dir in to_delete:
        shutil.rmtree(dir)


@contextlib.contextmanager
def stubs_suffix(session, path: pathlib.Path = pathlib.Path("./stubs")):
    """Context manager to add -stubs to all folders in the stubs directory.

    We only do this when it's time to package the stubs because mypy and vscode
    analysis don't work well within this project when the packages have the -stubs suffix.
    """
    paths = []
    path = path.absolute()
    for child in path.iterdir():
        if child.is_dir() and not child.name.endswith('-stubs'):
            name = child.stem + '-stubs'
            newpath = child.with_name(name)
            paths.append((child, newpath))
            child.rename(newpath)

    yield

    for orig, new in paths:
        new.rename(orig)


@nox.session(venv_backend='none')
@nox.parametrize('lib', PARAMS)
def develop(session: nox.Session, lib: str) -> None:
    session.chdir(lib)
    with stubs_suffix(session):
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
    with stubs_suffix(session):
        session.run("poetry", "publish", *session.posargs)


@nox.session(reuse_venv=True)
@nox.parametrize('lib', PARAMS)
def generate(session: nox.Session, lib: str) -> None:
    session.install("-r", "requirements.txt")

    if lib == "pyside":
        session.install("PySide2==5.15.2.1")
    elif lib == "ocio":
        session.install("opencolorio==2.2.1")
    elif lib == "usd":
        session.install("PySide6==6.5.1.1")

    session.chdir(lib)
    session.run(f"./stubgen_{lib}.sh", external=True)
    make_packages(pathlib.Path("stubs"))


@nox.session(reuse_venv=True)
@nox.parametrize('lib', PARAMS)
def mypy(session: nox.Session, lib: str) -> None:
    session.chdir(lib)
    session.install("mypy==1.4.1")
    session.run("mypy", "stubs")
