from _typeshed import Incomplete

__author__: str
__copyright__: str
__contributors__: Incomplete
__version__: str
__license__: str
escape_range: Incomplete

def encode(c): ...
def iri2uri(uri):
    """Convert an IRI to a URI. Note that IRIs must be
    passed in a unicode strings. That is, do not utf-8 encode
    the IRI before passing it into the function."""
