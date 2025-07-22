from .errors import MockgunError as MockgunError
from _typeshed import Incomplete

class SchemaFactory:
    """
    Allows to instantiate a pickled schema.
    """
    _schema_entity_cache: Incomplete
    _schema_entity_cache_path: Incomplete
    _schema_cache: Incomplete
    _schema_cache_path: Incomplete
    @classmethod
    def get_schemas(cls, schema_path: str, schema_entity_path: str) -> tuple:
        """
        Retrieves the schemas from disk.

        :param str schema_path: Path to the schema.
        :param str schema_entity_path: Path to the entities schema.

        :returns: Pair of dictionaries holding the schema and entities schema.
        :rtype: tuple
        """
    @classmethod
    def _read_file(cls, path): ...

_HIGHEST_24_PICKLE_PROTOCOL: int

def generate_schema(shotgun, schema_file_path, schema_entity_file_path) -> None:
    """
    Helper method for mockgun.
    Generates the schema files needed by the mocker by connecting to a real shotgun
    and downloading the schema information for that site. Once the generated schema
    files are being passed to mockgun, it will mimic the site's schema structure.

    :param sg_url: Shotgun site url
    :param sg_script: Script name to connect with
    :param sg_key: Script key to connect with
    :param schema_file_path: Path where to write the main schema file to
    :param schema_entity_file_path: Path where to write the entity schema file to
    """
