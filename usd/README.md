# Unofficial python stubs for Pixar's Universal Scene Description (USD)

These stubs are designed to be used with a type checker like `mypy` to provide static type checking of python code, as well as to provide analysis and completion in IDEs like PyCharm and VSCode (with Pylance).

## Installing

```commandline
pip install types-usd
```

The version of the package corresponds to the version of USD that it is generated from,
plus a version suffix for the revision of the stubs

The stubs have been tested against a large USD codebase using `mypy`, however, there
are still known issues that need to be resolved.

Using these stubs with `mypy` will produce erros within the stubs themselves, mostly about 
missing/unknown types.  I've left these errors unsilenced as a reminder to fix them. 
I recommend adding the following config to your `mypy.ini` to silence these errors:

```ini
[mypy-pxr.*]
ignore_errors = true
```

If you find any other issues, please report them on the [github issues page](https://github.com/LumaPictures/cg-stubs/issues).

## Developing

The stubs are created using information extracted from python signatures generated
by boost-python in each function's docstring, combined with data parsed as from the USD C++ docs.

Currently, creating the stubs requires custom forks of mypy and USD, but I hope to have
my changes merged into upstream soon.
