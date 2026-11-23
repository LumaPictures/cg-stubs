from pathlib import Path
import re
import sys
import datetime


if not Path(__file__).parent.parent.as_posix() in sys.path:
    sys.path.append(Path(__file__).parent.parent.as_posix())

from gen import _connection

_connection.RemotePainter().execScript("import substance_painter", "python")
version = _connection.RemotePainter().execScript("substance_painter.application.version()", "python")

# Include year?
# currentDateTime = datetime.datetime.now()
# date = currentDateTime.date()
# year = date.strftime("%Y")

if version:
    version = version.decode('''utf-8''').strip().strip('"')
    with open(Path(__file__).parent.parent / "pyproject.toml", "r") as f:
        text = f.read()
    with open(Path(__file__).parent.parent / "pyproject.toml", "w") as f:
        text = re.sub(
            r'version = "(.*)"',
            #rf'version = "{year}.{version}"',
            rf'version = "{version}"',
            text,
        )
        f.write(text)
else:
    print("Could not find any version")