# /// script
# dependencies = [
#   "nox>=2024.04.15",
#   "python-dotenv",
# ]
# ///

from __future__ import annotations

import contextlib
import os.path
import pathlib
import re
import shutil
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Callable, Iterable, Iterator, Match, Pattern

import nox
import nox.command

APPS = [
    "houdini",
    "katana",
    "mari",
    "maya",
    "nuke",
    "ocio",
    "otio",
    # "openexr",
    "pyside",
    "rez",
    "shotgun",
    "substance_painter",
    "usd",
]
STUB_PROJECTS = [nox.param(x, id=x) for x in APPS]

ALL_PROJECTS = STUB_PROJECTS + [nox.param("common", id="common")]

# TODO: generate pyproject.toml from a jinja template

cache = lru_cache(None)

# FIXME: auto-detect number of cores
PROCESSES = 8
GLOB_TO_REGEX = [
    # I'm pretty sure that "**/*.py" should match a python file at the root, e.g. "setup.py"
    # this first replacement ensures that this works in pre-commit
    ("**/", ".*"),
    ("**", ".*"),
    ("*", "[^/]*"),
    (".", "[.]"),
    ("?", "."),
    ("{", "("),
    ("}", ")"),
    (",", "|"),
]
GLOB_TO_REGEX_MAP = dict(GLOB_TO_REGEX)
GLOB_TO_REGEX_REG = re.compile(
    r"({})".format("|".join(re.escape(f) for f, r in GLOB_TO_REGEX))
)


# Config --

PYTHON_VERSIONS = {"2.7", "3.7", "3.9", "3.11"}

DEFAULT_LINT_TAGS = ["precommit", "prepush", "ci"]
TAG_TO_PRECOMMIT_STAGE = {
    "ci": "manual",
    "precommit": "commit",
    "prepush": "push",
}

# Files to include, and from which to generate pre-commit regex
LINT_FILES = ("**/*.py",)

# Standard set of "special" python files that are not linted
LINT_EXCLUDE = ()


def glob_to_regex(pattern: str) -> str:
    """
    Convert a glob to a regular expression.

    Unlike fnmatch.translate, this handles ** syntax, which match across multiple
    directories, and ensures that * globs only match within one level.

    It currently does not work with paths that contain complex characters that
    need to be escaped.
    """

    def replace(match: Match) -> str:
        pat = match.groups()[0]
        return GLOB_TO_REGEX_MAP[pat]

    return GLOB_TO_REGEX_REG.sub(replace, pattern)


def regexes_to_regex(patterns: Iterable[str]) -> Pattern | None:
    """
    Convert a tuple of regex strings to a single regex Pattern
    """
    patterns = ["^" + p for p in patterns]
    if len(patterns) > 1:
        reg = "|\n".join("    " + p for p in patterns)
        pattern = "(?x)(\n{}\n)$".format(reg)
    elif len(patterns) == 1:
        pattern = patterns[0] + "$"
    else:
        return None

    try:
        return re.compile(pattern)
    except re.error:
        print(pattern)
        raise


@cache
def globs_to_regex(patterns: tuple[str, ...]) -> Pattern | None:
    return regexes_to_regex(glob_to_regex(p) for p in patterns)


def filter_paths_regex(
    paths: Iterable[str],
    include: Pattern | None = None,
    exclude: Pattern | None = None,
) -> Iterator[str]:
    for path in paths:
        if (not include or include.search(path)) and (
            not exclude or not exclude.search(path)
        ):
            yield path


def filter_paths(
    paths: Iterable[str],
    include: tuple[str, ...] | None = None,
    exclude: tuple[str, ...] | None = None,
) -> list[str]:
    return list(
        filter_paths_regex(
            paths,
            globs_to_regex(include) if include else None,
            globs_to_regex(exclude) if exclude else None,
        )
    )


class GitRepo:
    """
    Query and filter files from git and cache results
    """

    def __init__(self, root: str):
        self.root: str = root

    @cache
    def files(self) -> list[str]:
        import subprocess

        output = subprocess.check_output(["git", "ls-files"], cwd=self.root)
        return [x for x in output.decode().split("\n") if x]

    @cache
    def file_matches(
        self, include: tuple[str, ...] | None, exclude: tuple[str, ...] | None = None
    ) -> list[str]:
        return list(filter_paths(self.files(), include, exclude))

    @cache
    def folders(self) -> list[str]:
        results = set()
        for path in self.files():
            while True:
                path = os.path.dirname(path)
                if not path:
                    break
                results.add(path)
        return sorted(results)

    @cache
    def folder_matches(
        self, include: tuple[str, ...] | None, exclude: tuple[str, ...] | None = None
    ) -> list[str]:
        return list(filter_paths(self.folders(), include, exclude))


repo = GitRepo(".")


@dataclass(frozen=True)
class Options:
    # list of globs
    paths: tuple[str, ...] | None
    # list of globs
    exclude: tuple[str, ...] | None = None
    pass_filenames: bool = True
    # we set require_serial to True for tools that do their own multiprocessing,
    # or those where it doesn't make sense to batch into groups of files (like mypy).
    # this only applies to pre-commit.
    # FIXME: look into porting some opt-in xargs-like behavior from pre-commit
    #  to this noxfile for tools that don't do their own multiprocessing.
    #  For now it appears we have to hard-wire this to True because there's a
    #  race condidtion on creating the venv when called from multiple processes
    #  by pre-commit
    require_serial: bool = True

    def paths_regex(self) -> Pattern | None:
        return globs_to_regex(self.paths) if self.paths is not None else None

    def exclude_regex(self) -> Pattern | None:
        return globs_to_regex(self.exclude) if self.exclude is not None else None

    def files(
        self,
        session: nox.Session,
        include: tuple[str, ...] | None = None,
        exclude: tuple[str, ...] | None = None,
    ) -> list[str]:
        if self.pass_filenames and session.posargs:
            return filter_paths(session.posargs, include=include, exclude=exclude)
        return repo.file_matches(
            include=include or self.paths, exclude=exclude or self.exclude
        )


def with_versions(versions: Iterable[str]) -> Callable[[Any], Any]:
    """
    Parametrization decorator that uses the parameters as the name
    """
    return nox.parametrize("ver", [nox.param(v, id=v) for v in sorted(versions)])


def check(
    paths=None,
    exclude: tuple[str, ...] | None = None,
    pass_filenames=True,
    require_serial=True,
    **session_kwargs,
):
    """
    Decorator for lint-like tasks intended to run as pre-commit
    """
    import functools

    session_kwargs.setdefault("reuse_venv", True)
    session_kwargs.setdefault("tags", DEFAULT_LINT_TAGS)

    def deco(func):
        options = Options(
            paths=tuple(paths) if paths else None,
            exclude=tuple(exclude) if exclude else None,
            pass_filenames=pass_filenames,
            require_serial=require_serial,
        )

        @nox.session(**session_kwargs)
        @functools.wraps(func)
        def wrapper(session, *args, **kwargs):
            return func(session, options, *args, **kwargs)

        # the result of @nox.session is a nox._decorators.Func. we bind the
        # options here so we can find them in precommit_gen.
        wrapper.options = options  # type: ignore[attr-defined]

        return wrapper

    return deco


def load_dotenv() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)

    try:
        import dotenv
    except ImportError:
        print(".env files not supported. Upgrade nox")
        return env

    if os.path.exists(".env"):
        env_path = os.path.realpath(".env")
        print(f"Loading environment variables from {env_path}")
        config = dotenv.dotenv_values(env_path)
        print(config)
        env.update(config)
    return env


# @check(
#     paths=LINT_FILES,
#     exclude=LINT_EXCLUDE,
# )
@nox.session(venv_backend="none")
def ruff(session: nox.Session):
    """Run ruff code formatter"""
    session.run("uvx", "--from=ruff==0.11.4", "ruff", "format", log=False)
    session.run("uvx", "--from=ruff==0.11.4", "ruff", "check", "--fix", log=False)


# @check(paths=('**.{yaml|yml}',), venv_backend='none')
# def check_yaml(session: nox.Session, options: Options):
#     import ruamel.yaml
#
#     yaml = ruamel.yaml.YAML()
#
#     load_fn = yaml.load
#
#     retval = 0
#     for filename in options.files(session):
#         try:
#             with open(filename, encoding='UTF-8') as f:
#                 load_fn(f)
#         except ruamel.yaml.YAMLError as exc:
#             print(exc)
#             retval = 1
#     return retval
#
#
# @check(paths=('**.toml',), venv_backend='none')
# def check_toml(session: nox.Session, options: Options):
#     import tomli
#
#     retval = 0
#     for filename in options.files(session):
#         with open(filename, 'rb') as f:
#             try:
#                 tomli.load(f)
#             except tomli.TOMLDecodeError as exc:
#                 print(f'{filename}: {exc}')
#                 retval = 1
#     return retval


@check(
    paths=["noxfile.py"],
    venv_backend="none",  # Imports toml from luma's .venv
    pass_filenames=False,
    tags=["precommit", "prepush"],
)
def precommit_gen(session: nox.Session, options: Options):
    """
    Generate a pre-commit-hooks.yaml from the lint tasks in this module.
    """
    # hooks = []
    # for hook_name, obj in nox.registry._REGISTRY.items():
    #     if hasattr(obj, 'options') and isinstance(obj.options, Options):
    #         assert isinstance(obj, nox._decorators.Func)
    #         hook = {
    #             'id': hook_name,
    #             'name': hook_name,
    #             'entry': 'nox',
    #             'args': flatlist('-s', hook_name, '--no-install', '--'),
    #             'language': 'system',
    #             'pass_filenames': obj.options.pass_filenames,
    #             # see not on Options.require_serial for why we don't use
    #             # obj.options.require_serial,
    #             'require_serial': obj.venv_backend != 'none',
    #             'stages': [TAG_TO_PRECOMMIT_STAGE.get(x, x) for x in obj.tags],
    #         }
    #         paths_regex = obj.options.paths_regex()
    #         if paths_regex:
    #             hook['files'] = multiline(paths_regex.pattern)
    #         exclude_regex = obj.options.exclude_regex()
    #         if exclude_regex:
    #             hook['exclude'] = multiline(exclude_regex.pattern)
    #         hooks.append(hook)
    #
    # with open('.pre-commit-config.yaml', 'w') as f:
    #     yaml.dump(
    #         {
    #             'repos': [
    #                 {
    #                     'repo': 'local',
    #                     'hooks': hooks,
    #                 }
    #             ]
    #         },
    #         f,
    #     )

    text = """
repos:
- repo: local
  hooks:
"""
    for hook_name, obj in nox.registry._REGISTRY.items():
        if hasattr(obj, "options") and isinstance(obj.options, Options):
            assert isinstance(obj, nox._decorators.Func)
            stages = [TAG_TO_PRECOMMIT_STAGE.get(x, x) for x in obj.tags]
            text += f"""
  - id: {hook_name}
    name: {hook_name}
    entry: nox
    args: [-s, {hook_name}, --no-install, --]
    language: system
    pass_filenames: {"true" if obj.options.pass_filenames else "false"}
    require_serial: {"true" if obj.venv_backend != "none" else "false"}
    stages: [{", ".join(stages)}]\n"""

            paths_regex = obj.options.paths_regex()
            if paths_regex:
                text += f"    files: {paths_regex.pattern}\n"
            exclude_regex = obj.options.exclude_regex()
            if exclude_regex:
                text += f"    exclude: {exclude_regex.pattern}\n"

    with open(".pre-commit-config.yaml", "w") as f:
        f.write(text)


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
        elif child.is_dir() and list(child.iterdir()):
            marker = child / "py.typed"
            marker.touch()


def add_stubs_suffix(path: pathlib.Path) -> None:
    """Add a -stubs suffix to packages prior to building.

    This ensures that they are PEP 561 compatible when we distribute them, but
    will be found by mypy as a normal package.
    """
    import shutil

    print("Add -stubs suffixes")
    # do these at the end to improve time to git refresh
    to_delete = []
    for child in path.iterdir():
        if child.is_dir() and not child.name.endswith("-stubs"):
            name = child.stem + "-stubs"
            newpath = child.with_name(name)
            if newpath.exists():
                backup = newpath.with_suffix(".bak")
                newpath.rename(backup)
                to_delete.append(backup)
            print(f"Renaming to {newpath}")
            child.rename(newpath)
            marker = newpath / "py.typed"
            marker.touch()

    for dir in to_delete:
        shutil.rmtree(dir)


@contextlib.contextmanager
def stubs_suffix(path: pathlib.Path = pathlib.Path("./stubs")):
    """Context manager to add -stubs to all folders in the stubs directory.

    We only do this when it's time to package the stubs because mypy and vscode
    analysis don't work well within this project when the packages have the -stubs suffix.
    """
    paths = []
    path = path.absolute()
    for child in path.iterdir():
        if child.is_dir() and not child.name.endswith("-stubs"):
            name = child.stem + "-stubs"
            newpath = child.with_name(name)
            paths.append((child, newpath))
            child.rename(newpath)

    yield

    for orig, new in paths:
        new.rename(orig)


@nox.session(venv_backend="none")
@nox.parametrize("lib", STUB_PROJECTS)
def develop(session: nox.Session, lib: str) -> None:
    """Install the stubs into the current venv"""
    session.chdir(lib)
    try:
        session.run("uv", "sync", external=True)
    except nox.command.CommandFailed as err:
        msg = str(err)
        if "poetry" in msg:
            print("You must install poetry>=1.3.2 in the destination venv")
        raise


@nox.session(venv_backend="none")
@nox.parametrize("lib", ALL_PROJECTS)
def publish(session: nox.Session, lib: str) -> None:
    """Publish the stub package to PyPI"""

    env = load_dotenv()

    session.chdir(lib)

    if os.path.exists("dist"):
        shutil.rmtree("dist")
    session.run("uv", "build", "--wheel", external=True)
    session.run("uv", "publish", env=env, external=True)
    output = session.run(
        "uvx",
        "--from=toml-cli",
        "toml",
        "get",
        "--toml-path=pyproject.toml",
        "project.version",
        silent=True,
    )
    print(output)
    assert output is not None
    version = output.splitlines()[-1]
    session.run("git", "tag", f"{lib}/v{version}", external=True)


@nox.session(venv_backend="none")
@nox.parametrize("lib", STUB_PROJECTS)
def generate(session: nox.Session, lib: str) -> None:
    """Create the stubs"""
    session.chdir(lib)
    env = load_dotenv()

    if sys.platform == "win32":
        script = f"./stubgen_{lib}.ps1"
    else:
        script = f"./stubgen_{lib}.sh"

    if os.path.exists(script):
        # Fully custom workflow
        if sys.platform == "win32":
            session.run(
                "powershell.exe",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                script,
                external=True,
                env=env,
            )
        else:
            session.run(script, env=env, external=True)
    elif os.path.exists(".interpreter"):
        # This is our standard playbook for stubs that are built via a DCC interpreter
        interp = pathlib.Path(".interpreter").read_text().strip()
        assert interp
        # we have to force update stubgenlib because uv will only reinstall if the version
        # changes.  I looked into creating dynamic versions using hatch-vcs but I could
        # not get it to work.
        session.run("uv", "sync", "--reinstall-package=stubgenlib", external=True)
        # Get the site-packages directory and add it to PYTHONPATH
        venv_python = (
            ".venv/Scripts/python.exe"
            if sys.platform == "win32"
            else ".venv/bin/python3"
        )
        sitepath = session.run(
            venv_python,
            "-c",
            'import sysconfig; print(sysconfig.get_paths()["purelib"])',
            silent=True,
        )
        env["PYTHONPATH"] = sitepath.strip()
        # FIXME: load from .env
        # session.run("uvx", "--from=python-dotenv[cli]", "dotenv", "run", "--", interp, "-m", "stubgen_maya", "./stubs", external=True)
        subprocess.check_call(
            [interp, "-m", f"stubgen_{lib}", "./stubs"] + session.posargs, env=env
        )
    else:
        # FIXME: implement a workflow around a standard interpreter for rez, pyside, etc
        raise RuntimeError(f"Could not find {script} or .interpreter")

    add_stubs_suffix(pathlib.Path("stubs"))
    # this has to happen after the stubs are renamed, because before that, the previous state of the
    # stubs still exists in the stubs directory (<foo> and <foo>-stubs coexisting until add_stubs_suffix
    # runs)
    # FIXME: lock down the version of mypy
    print("Adding type: ignore statements")
    subprocess.check_call("uvx mypy ./stubs | uvx mypy-silent", shell=True)


@nox.session(venv_backend="none")
@nox.parametrize("lib", ALL_PROJECTS)
def mypy(session: nox.Session, lib: str) -> None:
    """Run mypy type checker"""
    session.chdir(lib)
    session.run("uv", "run", "mypy")


@nox.session(venv_backend="none")
@nox.parametrize("lib", ALL_PROJECTS)
def test(session: nox.Session, lib: str) -> None:
    """Run mypy type checker"""
    session.chdir(lib)
    env = load_dotenv()
    session.run(
        "uv", "run", "pytest", "tests", *session.posargs, env=env, external=True
    )


# @check(paths=LINT_FILES, pass_filenames=False, tags=["ci", "prepush"])
@nox.session(venv_backend="none")
def self_mypy(session: nox.Session, options: Options) -> None:
    session.run("uvx", "mypy", external=True)
