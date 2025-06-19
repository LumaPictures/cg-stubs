from _typeshed import Incomplete
from rez.config import Validatable as Validatable
from rez.vendor.schema.schema import And as And, Optional as Optional, Schema as Schema, Use as Use  # type: ignore[import-not-found]

Required = Schema

def schema_keys(schema):
    '''Get the string values of keys in a dict-based schema.

    Non-string keys are ignored.

    Returns:
        set[str]: Set of string keys of a schema which is in the form (eg):

        .. code-block:: python

           schema = Schema({Required("foo"): int,
                            Optional("bah"): str})
    '''
def dict_to_schema(schema_dict, required, allow_custom_keys: bool = True, modifier: Incomplete | None = None):
    """Convert a dict of Schemas into a Schema.

    Args:
        required (bool): Whether to make schema keys optional or required.
        allow_custom_keys (typing.Optional[bool]): If True, creates a schema that
            allows custom items in dicts.
        modifier (typing.Optional[typing.Callable]): Functor to apply to dict values - it is applied
            via `Schema.Use`.

    Returns:
        A `Schema` object.
    """
def extensible_schema_dict(schema_dict):
    """Create schema dict that allows arbitrary extra keys.

    This helps to keep newer configs or package definitions compatible with
    older rez versions, that may not support newer schema fields.
    """
