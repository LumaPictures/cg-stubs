from .._otio import Composable as Composable, Composition as Composition, Item as Item, MediaReference as MediaReference, SerializableObject as SerializableObject, SerializableObjectWithMetadata as SerializableObjectWithMetadata, Track as Track, deserialize_json_from_file as deserialize_json_from_file, deserialize_json_from_string as deserialize_json_from_string, flatten_stack as flatten_stack, install_external_keepalive_monitor as install_external_keepalive_monitor, instance_from_schema as instance_from_schema, release_to_schema_version_map as release_to_schema_version_map, set_type_record as set_type_record, type_version_map as type_version_map
from ._core_utils import add_method as add_method

__all__ = ['Composable', 'Composition', 'Item', 'MediaReference', 'SerializableObject', 'SerializableObjectWithMetadata', 'Track', 'deserialize_json_from_file', 'deserialize_json_from_string', 'flatten_stack', 'install_external_keepalive_monitor', 'instance_from_schema', 'set_type_record', 'add_method', 'upgrade_function_for', 'downgrade_function_from', 'serializable_field', 'deprecated_field', 'serialize_json_to_string', 'serialize_json_to_file', 'register_type', 'type_version_map', 'release_to_schema_version_map']

def serialize_json_to_string(root, schema_version_targets=None, indent: int = 4):
    """Serialize root to a json string.  Optionally downgrade resulting schemas
    to schema_version_targets.

    :param SerializableObject root: root object to serialize
    :param dict[str, int] schema_version_targets: optional dictionary mapping
                                                  schema name to desired schema
                                                  version, for downgrading the
                                                  result to be compatible with
                                                  older versions of
                                                  OpenTimelineIO.
    :param int indent: number of spaces for each json indentation level. Use -1
                       for no indentation or newlines.

    :returns: resulting json string
    :rtype: str
    """
def serialize_json_to_file(root, filename, schema_version_targets=None, indent: int = 4):
    """Serialize root to a json file.  Optionally downgrade resulting schemas
    to schema_version_targets.

    :param SerializableObject root: root object to serialize
    :param dict[str, int] schema_version_targets: optional dictionary mapping
                                                  schema name to desired schema
                                                  version, for downgrading the
                                                  result to be compatible with
                                                  older versions of
                                                  OpenTimelineIO.
    :param int indent: number of spaces for each json indentation level. Use -1
                       for no indentation or newlines.

    :returns: true for success, false for failure
    :rtype: bool
    """
def register_type(classobj, schemaname=None):
    '''Decorator for registering a SerializableObject type

    Example:

    .. code-block:: python

        @otio.core.register_type
        class SimpleClass(otio.core.SerializableObject):
          serializable_label = "SimpleClass.2"
          ...

    :param typing.Type[SerializableObject] cls: class to register
    :param str schemaname: Schema name (default: parse from serializable_label)
    '''
def upgrade_function_for(cls, version_to_upgrade_to):
    """
    Decorator for identifying schema class upgrade functions.

    Example:

    .. code-block:: python

        @upgrade_function_for(MyClass, 5)
        def upgrade_to_version_five(data):
            pass

    This will get called to upgrade a schema of MyClass to version 5. MyClass
    must be a class deriving from :class:`~SerializableObject`.

    The upgrade function should take a single argument - the dictionary to
    upgrade, and return a dictionary with the fields upgraded.

    Remember that you don't need to provide an upgrade function for upgrades
    that add or remove fields, only for schema versions that change the field
    names.

    :param typing.Type[SerializableObject] cls: class to upgrade
    :param int version_to_upgrade_to: the version to upgrade to
    """
def downgrade_function_from(cls, version_to_downgrade_from):
    '''
    Decorator for identifying schema class downgrade functions.

    Example:

    .. code-block:: python

        @downgrade_function_from(MyClass, 5)
        def downgrade_from_five_to_four(data):
            return {"old_attr": data["new_attr"]}

    This will get called to downgrade a schema of MyClass from version 5 to
    version 4. MyClass must be a class deriving from
    :class:`~SerializableObject`.

    The downgrade function should take a single argument - the dictionary to
    downgrade, and return a dictionary with the fields downgraded.

    :param typing.Type[SerializableObject] cls: class to downgrade
    :param int version_to_downgrade_from: the function downgrading from this
                                          version to (version - 1)
    '''
def serializable_field(name, required_type=None, doc=None, default_value=None):
    '''
    Convenience function for adding attributes to child classes of
    :class:`~SerializableObject` in such a way that they will be serialized/deserialized
    automatically.

    Use it like this:

    .. code-block:: python

        @core.register_type
        class Foo(SerializableObject):
            bar = serializable_field("bar", required_type=int, doc="example")

    This would indicate that class "foo" has a serializable field "bar".  So:

    .. code-block:: python

        f = foo()
        f.bar = "stuff"

        # serialize & deserialize
        otio_json = otio.adapters.from_name("otio")
        f2 = otio_json.read_from_string(otio_json.write_to_string(f))

        # fields should be equal
        f.bar == f2.bar

    Additionally, the "doc" field will become the documentation for the
    property.

    :param str name: name of the field to add
    :param type required_type: type required for the field
    :param str doc: field documentation
    :param Any default_value: default value to return if no field value is set yet

    :return: property object
    :rtype: :py:class:`property`
    '''
def deprecated_field():
    """For marking attributes on a SerializableObject deprecated."""
