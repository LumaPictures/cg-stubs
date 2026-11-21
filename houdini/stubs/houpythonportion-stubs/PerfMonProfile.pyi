# Houdini stubs generated from Houdini 22.0.466

import hou
from houtypes import JSONValue

def stats(self: hou.PerfMonProfile) -> dict[str, JSONValue]:
    """
stats(self)

    Return the profile statistics in JSON format.

    Raises hou.OperationFailed if the profile is still active and has
    not generated any statistics.

"""
def save(self: hou.PerfMonProfile, file_path: str) -> None:
    """
save(self, file_path)

    This method is deprecated in favor of hou.perfMon.saveProfile.

"""
