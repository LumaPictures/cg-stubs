from .. import core as core, exceptions as exceptions, versioning as versioning

_DEFAULT_VERSION_ENVVAR: str

def read_from_file(filepath):
    """
    De-serializes an OpenTimelineIO object from a file

    Args:
        filepath (str): The path to an otio file to read from

    Returns:
        OpenTimeline: An OpenTimeline object
    """
def read_from_string(input_str):
    """
    De-serializes an OpenTimelineIO object from a json string

    Args:
        input_str (str): A string containing json serialized otio contents

    Returns:
        OpenTimeline: An OpenTimeline object
    """
def _fetch_downgrade_map_from_env(): ...
def write_to_string(input_otio, target_schema_versions=None, indent: int = 4):
    '''
    Serializes an OpenTimelineIO object into a string

    Args:
        input_otio (OpenTimeline): An OpenTimeline object
        indent (int): number of spaces for each json indentation level. Use            -1 for no indentation or newlines.

    If target_schema_versions is None and the environment variable
    "OTIO_DEFAULT_TARGET_VERSION_FAMILY_LABEL" is set, will read a map out of
    that for downgrade target.  The variable should be of the form
    FAMILY:LABEL, for example "MYSTUDIO:JUNE2022".

    Returns:
        str: A json serialized string representation

    Raises:
        otio.exceptions.InvalidEnvironmentVariableError: if there is a problem
        with the default environment variable
        "OTIO_DEFAULT_TARGET_VERSION_FAMILY_LABEL".
    '''
def write_to_file(input_otio, filepath, target_schema_versions=None, indent: int = 4):
    '''
    Serializes an OpenTimelineIO object into a file

    Args:

        input_otio (OpenTimeline): An OpenTimeline object
        filepath (str): The name of an otio file to write to
        indent (int): number of spaces for each json indentation level.            Use -1 for no indentation or newlines.

    If target_schema_versions is None and the environment variable
    "OTIO_DEFAULT_TARGET_VERSION_FAMILY_LABEL" is set, will read a map out of
    that for downgrade target.  The variable should be of the form
    FAMILY:LABEL, for example "MYSTUDIO:JUNE2022".

    Returns:
        bool: Write success

    Raises:
        ValueError: on write error
        otio.exceptions.InvalidEnvironmentVariableError: if there is a problem
        with the default environment variable
        "OTIO_DEFAULT_TARGET_VERSION_FAMILY_LABEL".
    '''
