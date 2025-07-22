from ... import ShotgunError as ShotgunError
from ...shotgun import _Config as _Config
from .errors import MockgunError as MockgunError
from .schema import SchemaFactory as SchemaFactory
from _typeshed import Incomplete
from typing import Any

__version__: str

class Shotgun:
    """
    Mockgun is a mocked Shotgun API, designed for test purposes.
    It generates an object which looks and feels like a normal Shotgun API instance.
    Instead of connecting to a real server, it keeps all its data in memory in a way
    which makes it easy to introspect and test.

    The methods presented in this class reflect the Shotgun API and are therefore
    sparsely documented.

    Please note that this class is built for test purposes only and only creates an
    object which *roughly* resembles the Shotgun API - however, for most common
    use cases, this is enough to be able to perform relevant and straight forward
    testing of code.
    """
    __schema_path: Incomplete
    __schema_entity_path: Incomplete
    @classmethod
    def set_schema_paths(cls, schema_path, schema_entity_path) -> None:
        """
        Set the path where schema files can be found. This is done at the class
        level so all Shotgun instances will share the same schema.
        The responsability to generate and load these files is left to the user
        changing the default value.

        :param schema_path: Directory path where schema files are.
        """
    @classmethod
    def get_schema_paths(cls):
        """
        Returns a tuple with paths to the files which are part of the schema.
        These paths can then be used in generate_schema if needed.

        :returns: A tuple with schema_file_path and schema_entity_file_path
        """
    config: Incomplete
    _db: Incomplete
    base_url: Incomplete
    finds: int
    def __init__(self, base_url, script_name=None, api_key=None, convert_datetimes_to_utc: bool = True, http_proxy=None, ensure_ascii: bool = True, connect: bool = True, ca_certs=None, login=None, password=None, sudo_as_login=None, session_token=None, auth_token=None) -> None: ...
    def get_session_token(self): ...
    def schema_read(self): ...
    def schema_field_create(self, entity_type, data_type, display_name, properties=None) -> None: ...
    def schema_field_update(self, entity_type, field_name, properties) -> None: ...
    def schema_field_delete(self, entity_type, field_name) -> None: ...
    def schema_entity_read(self): ...
    def schema_field_read(self, entity_type, field_name=None): ...
    def find(self, entity_type, filters, fields=None, order=None, filter_operator=None, limit: int = 0, retired_only: bool = False, page: int = 0): ...
    def find_one(self, entity_type, filters, fields=None, order=None, filter_operator=None, retired_only: bool = False): ...
    def batch(self, requests): ...
    def create(self, entity_type, data, return_fields=None): ...
    def update(self, entity_type, entity_id, data, multi_entity_update_modes=None): ...
    def delete(self, entity_type, entity_id): ...
    def revive(self, entity_type, entity_id): ...
    def upload(self, entity_type, entity_id, path, field_name=None, display_name=None, tag_list=None) -> None: ...
    def upload_thumbnail(self, entity_type, entity_id, path, **kwargs) -> None: ...
    def add_user_agent(self, agent) -> None: ...
    def set_session_uuid(self, session_uuid) -> None: ...
    def _validate_entity_type(self, entity_type) -> None: ...
    def _validate_entity_data(self, entity_type, data) -> None: ...
    def _validate_entity_fields(self, entity_type, fields) -> None: ...
    def _get_default_value(self, entity_type, field): ...
    def _get_new_row(self, entity_type): ...
    def _compare(self, field_type: str, lval: Any, operator: str, rval: Any) -> bool:
        """
        Compares a field using the operator and value provide by the filter.

        :param str field_type: Type of the field we are operating on.
        :param lval: Value inside that field. Can be of any type: datetime, date, int, str, bool, etc.
        :param str operator: Name of the operator to use.
        :param rval: The value following the operator in a filter.

        :returns: The result of the operator that was applied.
        :rtype: bool
        """
    def _get_field_from_row(self, entity_type, row, field): ...
    def _get_field_type(self, entity_type, field): ...
    def _row_matches_filter(self, entity_type, row, sg_filter, retired_only): ...
    def _rearrange_filters(self, filters: list) -> None:
        '''
        Modifies the filter syntax to turn it into a list of three items regardless
        of the actual filter. Most of the filters are list of three elements, so this doesn\'t change much.

        The filter_operator syntax uses a dictionary with two keys, "filters" and
        "filter_operator". Filters using this syntax will be turned into
        [None, filter["filter_operator"], filter["filters"]]

        Filters of the form [field, operator, values....] will be turned into
        [field, operator, [values...]].

        :param list filters: List of filters to rearrange.

        :returns: A list of three items.
        '''
    def _row_matches_filters(self, entity_type, row, filters, filter_operator, retired_only): ...
    def _update_row(self, entity_type, row, data, multi_entity_update_modes=None) -> None: ...
    def _validate_entity_exists(self, entity_type, entity_id) -> None: ...
