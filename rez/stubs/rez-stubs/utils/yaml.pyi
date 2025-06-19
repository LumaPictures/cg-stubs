from rez.utils.sourcecode import SourceCode as SourceCode
from rez.vendor import yaml as yaml  # type: ignore[import-not-found]
from rez.vendor.yaml.dumper import SafeDumper as SafeDumper  # type: ignore[import-not-found]
from rez.version import Requirement as Requirement, Version as Version

class _Dumper(SafeDumper):
    """Dumper which can serialise custom types such as Version, and keeps
    long strings nicely formatted in >/| block-style format.
    """
    def represent_as_str(self, data): ...
    def represent_function(self, data): ...
    def represent_builtin_function(self, data): ...
    def represent_sourcecode(self, data): ...

def dump_yaml(data, Dumper=..., default_flow_style: bool = False):
    """Returns data as yaml-formatted string."""
def load_yaml(filepath):
    """Convenience function for loading yaml-encoded data from disk."""
def save_yaml(filepath, **fields) -> None:
    """Convenience function for writing yaml-encoded data to disk."""
