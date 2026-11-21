# Unofficial python stubs for SideFX Houdini

These stubs are designed to be used with a type checker like `mypy` to provide static type checking of python code, as well as to provide analysis and completion in IDEs like PyCharm and VSCode (with Pylance).

## Installing

```commandline
pip install types-houdini
```

The version of the package corresponds to the version of Houdini that it is generated from,
plus a version suffix for the revision of the stubs

## Contents

Alongside `hou`, the package has stubs for the other Python modules that Houdini ships in
`$HFS/houdini/pythonX.Ylibs`, one `<module>-stubs` package each: `pdg`, `pdgutils`, `pdgjob`,
`hapi`, `husd`, `toolutils`, `soputils`, `hdefereval`, `viewerstate`, `nodegraph*`, and the rest.

- Compiled extensions (`_pdg`, `_pdgd`, `_pdgutils`, `hapi`, `_houqt`, `husd.UsdHoudini`, ...) are
  stubbed by inspecting them, so their signatures are typed.
- Pure-python modules are stubbed from source, with types from the annotation overlays in
  `annotations/` (see [annotate/README.md](annotate/README.md)), since most of Houdini's python
  code is unannotated.
- `houtypes` has `TypedDict`s for the `kwargs` dictionaries that Houdini passes to Python
  callbacks (viewer states and handles, shelf tools, parameter callbacks and menu scripts, asset
  event handlers, ...), for annotating your own callbacks, e.g.
  `def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool`. It exists only in the
  stubs, so import it under `if TYPE_CHECKING:`.

## Generating

Run inside a Houdini environment, with the venv built on the python version Houdini uses:

```commandline
rez env proto_env python-3.13 -- bash -c 'uv venv --python "$(readlink -f "$(command -v python3.13)")" .venv && uv sync --no-install-project'
rez env houdini-22 -- ./stubgen_houdini.sh
```

`stubgen_houdini.py` generates `hou`; `stubgen_houdini_libs.py` generates everything else. Both
merge in the annotation overlays. For a new Houdini version, see
[annotate/README.md](annotate/README.md#upgrading-to-a-new-houdini-version).
