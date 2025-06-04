from __future__ import absolute_import, print_function

import mypy.moduleinspect


class ModuleInspect:
    """
    Patch ModuleInspect so that it imports modules directly into the current process rather than
    using a multiprocessing.
    """

    def get_package_properties(
        self, package_id: str
    ) -> mypy.moduleinspect.ModuleProperties:
        return mypy.moduleinspect.get_package_properties(package_id)

    def __enter__(self):
        print("Bypassing multiprocessing for module inspection")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return


def patch():
    import mypy.stubgen
    import mypy.stubutil

    mypy.moduleinspect.ModuleInspect = ModuleInspect
    mypy.stubutil.ModuleInspect = ModuleInspect
    mypy.stubgen.ModuleInspect = ModuleInspect
