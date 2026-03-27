import textwrap
from pathlib import Path
import sys

if not Path(__file__).parent.parent.as_posix() in sys.path:
    sys.path.append(Path(__file__).parent.parent.as_posix())

from gen import _connection

def generate_stubs(out_dir, site_packages):
    data = f"""
    print("DEBUG   | Adding {site_packages} to sys.path")
    print("DEBUG   | Output to {out_dir}/stubs/")
    import sys; sys.path.append("{site_packages}")
    import stubgenlib.moduleinspect; stubgenlib.moduleinspect.patch()
    import mypy.stubgen; mypy.stubgen.main(['-p', '_substance_painter', '-o', '{out_dir}/stubs/'])
    """
    _connection.RemotePainter().execScript(textwrap.dedent(data), "python")


this = Path(__file__).absolute().parent.parent
generate_stubs(this.as_posix(), (this / ".venv" / "Lib" / "site-packages").as_posix())
