from _typeshed import Incomplete

DOCUMENT_HEADER: str
FIELDS_ONLY_HEADER: str
CLASS_HEADER_WITH_DOCS: str
CLASS_HEADER_ONLY_FIELDS: str
MODULE_HEADER: str
PROP_HEADER: str
PROP_HEADER_NO_HELP: str
PROP_FETCHERS: Incomplete

def _parsed_args():
    """ parse commandline arguments with argparse """

SKIP_CLASSES: Incomplete
SKIP_KEYS: Incomplete
SKIP_MODULES: Incomplete

def _generate_model_for_module(mod, classes, modules): ...
def _generate_model(): ...
def _search_mod_recursively(cl, mod_to_search, already_searched): ...
def _remap_to_python_modules(cl):
    """Find the module containing the python wrapped class, rather than the base
    C++ _otio modules.
    """
def _write_documentation(model): ...
def main() -> None:
    """  main entry point  """
def generate_and_write_documentation(): ...
