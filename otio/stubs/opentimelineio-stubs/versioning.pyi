from . import core as core, plugins as plugins

def full_map():
    '''Return the full map of schema version sets, including core and plugins.
    Organized as follows:

    .. code-block:: python

        {
            "FAMILY_NAME": {
                "LABEL": {
                    "SchemaName": schemaversion,
                    "Clip": 2,
                    "Timeline": 3,
                    ...
                }
            }
        }


    The "OTIO_CORE" family is always provided and represents the built in
    schemas defined in the C++ core.
    IE:

    .. code-block:: python

        {
            "OTIO_CORE": {
                "0.15.0": {
                    "Clip": 2,
                    ...
                }
            }
        }

    :returns: full map of schema version sets, including core and plugins
    :rtype: dict[str, dict[str, dict[str, int]]]
    '''
def fetch_map(family, label):
    '''Fetch the version map for the given family and label.  OpenTimelineIO
    includes a built in family called "OTIO_CORE", this is compiled into the
    C++ core and represents the core interchange schemas of OpenTimelineIO.

    Users may define more family/label/schema:version mappings by way of the
    version manifest plugins.

    Returns a dictionary mapping Schema name to schema version, like:

    .. code-block:: python

        {
            "Clip": 2,
            "Timeline": 1,
            ...
        }

    :param str family: family of labels (ie: "OTIO_CORE")
    :param str label: label of schema-version map (ie: "0.15.0")
    :returns: a dictionary mapping Schema name to schema version
    :rtype: dict[str, int]
    '''
