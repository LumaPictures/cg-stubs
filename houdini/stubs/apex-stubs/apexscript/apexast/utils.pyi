from _typeshed import Incomplete

def property_getter(property_name, property_default): ...
def property_setter(property_name, property_default): ...
def dump(node, annotate_fields: bool = True, include_attributes: bool = False, *, indent: Incomplete | None = None):
    """
    Return a formatted dump of the tree in node.  This is mainly useful for
    debugging purposes.  If annotate_fields is true (by default),
    the returned string will show the names and the values for fields.
    If annotate_fields is false, the result string will be more compact by
    omitting unambiguous field names.  Attributes such as line
    numbers and column offsets are not dumped by default.  If this is wanted,
    include_attributes can be set to true.  If indent is a non-negative
    integer or string, then the tree will be pretty-printed with that indent
    level. None (the default) selects the single line representation.
    """
