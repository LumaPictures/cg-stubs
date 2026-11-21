# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Iterable
from houtypes import JSONValue
from typing import TypedDict

class _AssetInfo(TypedDict, total=False):
    name: JSONValue
    description: JSONValue
    author: JSONValue
    version: JSONValue
    thumbnailURL: JSONValue
    fileURL: JSONValue
    lastModified: JSONValue

def getAssetsFromURL(url: str) -> list[_AssetInfo]:
    """ Queries the url and returns a list of details on the
        assets that are available for download. """
def getAssetsFromURLAsStringArray(url: str) -> list[str]:
    ''' Queries the url and returns a list of assets in the form 
        of a string array.  The string array has the following format:
        [ "asset_name1", "asset_description1", "asset_author1",
          "asset_version1", "asset_thumbnail1", "asset_download_url1", 
          "asset_last_modified1", "asset_name2", "asset_description2", ... ] '''
def downloadFile(file_url: str, destination_path: str, file_name: str | None = None) -> str:
    """ Downloads the file from the given url and places it in
        specified destination folder.  If 'file_name' is not specified,
        then the downloaded file is named by the one that is listed in the
        'Contents-Type' header from http response.  Returns the path
        of the downloaded file on success.  Returns the empty string
        on failure.  """
def downloadAssetThumbnail(thumbnail_url: str, temp_dir: str | None = None) -> str:
    """ Downloads the given thumbnail url and saves it into a temporary
        file.  Returns the path of the temporary file on success. 
        Returns the empty string on failure. """
def endsWithAnyOf(file_path: str, extension_list: Iterable[str]) -> bool:
    """ Return whether the file ends with any of the extensions in the
        list. This only looks at last extension, after the last dot"""
def zipExtensions() -> list[str]:
    """ Supported extensions for zip archives """
def gzipExtensions() -> list[str]:
    """ Supported extensions for gzip archives """
def isSupportedArchive(file_path: str) -> bool:
    """ Returns whether the file is an archive type that is
        supported for downloadable assets by Houdini.
        The current supported archive formats are: zip."""
def extractZipArchive(archive_path: str, destination_path: str, required_extension: str | None) -> None:
    """ Precondition: archive_path is a zip archive.
        If required_extension is specified, then only files
        inside the archive that have this extension will be extracted
        from the archive. """
def extractGzipArchive(archive_path: str, destination_path: str, required_extension: str | None) -> None:
    """ Precondition: archive_path is a gzip file. """
def extractArchive(archive_path: str, destination_path: str, required_extension: str | None = None) -> None:
    """ Precondition: isSupportedArchive(archive_path) == True. 
        Extracts the specified archive file and stores the contents in
        'destination_path'. If required_extension is specified, then
        only files inside the archive that have this extension will be
        extracted from the archive. """
