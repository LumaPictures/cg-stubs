
import pathlib
import re

outdir = pathlib.Path(__file__).parent.parent / "stubs" / "substance_painter-stubs"

# Fix event.pyi: replace _Number with Union[int, float]
event_pyi = outdir / "event.pyi"
text = event_pyi.read_text()
text = re.sub(r"\b_Number\b", "Union[int, float]", text)
text = text.replace("from _typeshed import Incomplete", "from typing import Union")
text = text.replace("DISPATCHER: Incomplete", "DISPATCHER: Dispatcher")
event_pyi.write_text(text)

# For each .pyi file, replace CamelCase: Incomplete with an import from _substance_painter
print("Patching Incomplete Class reference")
for file in sorted(outdir.glob("*.pyi")):
    name = file.stem
    print(f"  {file} ({name})")
    text = file.read_text()
    text = re.sub(
        r"\b([A-Z]+[a-z][a-zA-Z0-9_]+): Incomplete",
        rf"from _substance_painter.{name} import \1 as \1",
        text,
    )
    file.write_text(text)


# Add missing import
print("Patching missing types import")
for path in [outdir / "layerstack.pyi", outdir / "project.pyi"]:
    with open(path, "r") as f:
        data = f.read()

    if "import types" not in data:
        data = "import types\n" + data

        with open(path, "w") as f:
            f.write(data)


# In each stub file replace floatN and intN.
print("Patching floatN and intN")
for file in sorted(outdir.parent.glob("**/*.pyi")):
    name = file.stem
    print(f"  {file} ({name})")
    text = file.read_text()
    text = re.sub(
        r"(float|int)\d+",
        rf"\1",
        text,
    )
    file.write_text(text)


# Path accept None as Default
# print("None as Default")
# for file in sorted(outdir.parent.glob("**/*.pyi")):
#     name = file.stem
#     print(f"  {file} ({name})")
#     text = file.read_text()
#     text = re.sub(
#         r": str = None",
#         rf": str",
#         text,
#     )
#     text = re.sub(
#         r": list[str] = None",
#         rf": list[str]",
#         text,
#     )
#     file.write_text(text)