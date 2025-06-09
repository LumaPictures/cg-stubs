from __future__ import absolute_import, print_function

import pathlib


def add_stubs_suffix(path: pathlib.Path) -> None:
    """Add a -stubs suffix to packages prior to building.

    This ensures that they are PEP 561 compatible when we distribute them, but
    will be found by mypy as a normal package.
    """
    import shutil

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
