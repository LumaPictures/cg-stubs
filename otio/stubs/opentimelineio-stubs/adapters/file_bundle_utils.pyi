from .. import exceptions as exceptions, schema as schema, url_utils as url_utils

BUNDLE_VERSION: str
BUNDLE_VERSION_FILE: str
BUNDLE_PLAYLIST_PATH: str
BUNDLE_DIR_NAME: str

class NotAFileOnDisk(exceptions.OTIOError): ...  # type: ignore[name-defined]

class MediaReferencePolicy:
    ErrorIfNotFile: str
    MissingIfNotFile: str
    AllMissing: str

def reference_cloned_and_missing(orig_mr, reason_missing):
    """Replace orig_mr with a missing reference with the same metadata.

    Also adds original_target_url and missing_reference_because fields.
    """
def _guarantee_unique_basenames(path_list, adapter_name) -> None: ...
def _prepped_otio_for_bundle_and_manifest(input_otio, media_policy, adapter_name):
    """ Create a new OTIO based on input_otio that has had media references
    replaced according to the media_policy.  Return that new OTIO and a
    mapping of all the absolute file paths (not URLs) to be used in the bundle,
    mapped to MediaReferences associated with those files.  Media references in
    the OTIO will be relinked by the adapters to point to their output
    locations.

    The otio[dz] adapters use this function to do further relinking and build
    their bundles.

    This is considered an internal API.
    """
def _total_file_size_of(filepaths): ...
