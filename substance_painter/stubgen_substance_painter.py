"""Post-process generated substance_painter stubs.

IMPORTANT:
This script does NOT generate the stubs automatically. You must first manually
generate the _substance_painter stubs inside the Substance Painter GUI, then run
the stubgen command for the wrapper module. See README.md for full instructions.

This script + the noxfile post-process the stubs into a publishable state.
"""

import pathlib
import re

outdir = pathlib.Path("stubs/substance_painter")

# Fix event.pyi: replace _Number with Union[int, float]
event_pyi = outdir / "event.pyi"
text = event_pyi.read_text()
text = re.sub(r"\b_Number\b", "Union[int, float]", text)
text = text.replace("from _typeshed import Incomplete", "from typing import Union")
text = text.replace("DISPATCHER: Incomplete", "DISPATCHER: Dispatcher")
event_pyi.write_text(text)

# For each .pyi file, replace CamelCase: Incomplete with an import from _substance_painter
for file in sorted(outdir.glob("*.pyi")):
    name = file.stem
    print(f"{file} ({name})")
    text = file.read_text()
    text = re.sub(
        r"\b([A-Z]+[a-z][a-zA-Z0-9_]+): Incomplete",
        rf"from _substance_painter.{name} import \1 as \1",
        text,
    )
    file.write_text(text)

# FIXME: also need to replace PySide2.QtWidgets.QWidget with PySide2.QtCore.QObject in delete_ui_element
