# mypy: disable-error-code="misc, override, no-redef"

_toStringFnCache: dict

def GetScalarTypeFromAttr(attr):
    """
    returns the (scalar, isArray) where isArray is True if it was an array type
    """
def ToClipboard(v, typeName): ...
def ToString(v, valueType):
    '''Returns a string representing a "detailed view" of the value v.
        This string is used in the watch window'''
