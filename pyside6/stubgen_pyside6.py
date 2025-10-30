import shutil
import sys
from pathlib import Path

import mypy.stubgen

pyside6_root = Path(sys.modules[__name__].__file__).parent
pyside2_root = pyside6_root.parent.joinpath("pyside")
sys.path.append(str(pyside2_root))

from stubgen_pyside import helper

if __name__ == "__main__":
    diff_with_pyside2 = False

    helper.set_pyside_version(6)

    # in order to create and inspect object properties we must create an app
    app = helper.QtWidgets.QApplication()

    # from stubgenlib.moduleinspect import patch
    #
    # # I don't think this works because mypy is compiled
    # patch()

    mypy.stubgen.main(
        [
            f"-p={helper.shiboken_package}",
            f"-p={helper.pyside_package}",
            "--include-private",
            "-o=stubs",
        ]
    )

    helper.add_version_info()

    def swap(src: Path, dest: Path) -> None:
        if dest.exists():
            shutil.rmtree(dest)
        src.rename(dest)

    if diff_with_pyside2:
        pyside2_dir = pyside2_root.joinpath("stubs", "PySide2-stubs")
        pyside6_dir = pyside6_root.joinpath("stubs", "PySide6")
        swap(pyside6_dir, pyside2_dir)

        shiboken2_dir = pyside2_root.joinpath("stubs", "shiboken2-stubs")
        shiboken6_dir = pyside6_root.joinpath("stubs", "shiboken6")
        swap(shiboken6_dir, shiboken2_dir)
