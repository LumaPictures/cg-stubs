# Unofficial python stubs for Pixar's Universal Scene Description (USD)

These stubs are designed to be used with a type checker like `mypy` to provide static type checking of python code, as well as to provide analysis and completion in IDEs like PyCharm and VSCode (with Pylance).

## Features

- Includes docstrings for easy access with an IDE.
- Number of `@overloads` is extracted from Boost, so it is always accurate.
- Handles pointer arguments and properly converts them to python results.
- Converts numerous known types such as `std::vector`, `std::sequence`, `std::set`, `std::unordered_set`, `std::function`, `std::map`, `std::unordered_map`, `std::optional`.
- More esoteric types are converted by scaning headers for `typedef` and `using` statements to substitute these aliases for their actual types
- Stub signatures indicate arguments which can be referenced by name vs those which must be passed by position, via [pep0570](https://peps.python.org/pep-0570/#syntax-and-semantics).  For example, for `Sdf.Layer.ReloadLayers`, arguments after `/` can be passed by name, while those before can only be passed base on position:
    ```python
    def ReloadLayers(_layers: typing.Iterable[Layer], /, force: bool = ...) -> bool: ...
    ```

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
