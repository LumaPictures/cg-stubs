# Houdini stubs generated from Houdini 22.0.466

from hutil.ml.oidn.config import *
from hutil.ml.oidn.utils import *
from hutil.ml.oidn.result import *
from hutil.ml.oidn import tza as tza
from hutil.ml.oidn.options import ExportOptions as ExportOptions

def export_weights(cfg: ExportOptions) -> tuple[bool, str]:
    """
    Exports model weights to a TZA file
    Returns a tuple where first entry is True if exporting is successful
    and False otherwise
    """
def export_package(cfg: ExportOptions) -> tuple[bool, str]:
    """
    Exports the results directory to a ZIP file
    Returns a tuple where first entry is True if exporting is successful
    and False otherwise
    """
