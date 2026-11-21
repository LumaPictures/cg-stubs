from collections.abc import Iterable
from houtypes import ShelfToolKwargs

def installPackage(shelf_name: str, shelf_pkg_path: str, install_path: str) -> str:
    """ Installs the shelf package, 'shelf_pkg_path', into
        the given installation directory. This removes previously installed
        packages with the same shelf name.  Returns the final installation
        path for the shelf package.  Returns the empty string on failure. """
def downloadAndInstallPackage(shelf_name: str, shelf_url: str, install_path: str, tmp_path: str | None = None) -> str:
    """ Downloads the shelf package from 'shelf_url' and installs it
        into the given installation directory.  Returns the final install
        path of the shelf package.  Returns the empty string on failure. """
def normalizePath(path: str) -> str:
    """ Normalizes the given file path by replacing backward slashes
        with forward slashes.  This function is useful when comparing
        file paths. """
def findFilesByExtension(dir: str, file_ext: str) -> list[str]:
    """ Recursively searches in 'dir' and returns a list of all the files
        found in the directory tree that match the given file extension.
        Does not search in hidden directories or 'backup' directories. """
def findShelfFiles(shelf_install_dir: str, shelf_extensions: Iterable[str] | None = None) -> list[str]:
    """ Recursively searches in 'shelf_install_dir' and returns a list
        of shelf files found in the directory tree.  Does not search
        in hidden directories or 'backup' directories. """
def findShelfOTLFiles(shelf_install_dir: str) -> list[str]:
    """ Recursively searches in 'shelf_install_dir' and returns a list
        of shelf files found in the directory tree.  Does not search
        in hidden directories or 'backup' directories. """
def chooseAndOpenAudioFile() -> None:
    """ Chooses and loads a soundtrack file, and sets up the Audio Panel 
        parameters to play the audio durng animation playback or playbar 
        scrubbing. """
def populateShelfFromJSON() -> None:
    """ Load the list of shelf tools corresponding to Orbolt assets
        and populate them in the shelf.
        """
def installOrboltAsset(kwargs: ShelfToolKwargs, node_name: str, url: str) -> None:
    """ Script that Houdini calls when clicking on a shelf tool that
        corresponds to an Orbolt asset. We can either direct the user
        to the asset store if it the asset has not been installed yet
        or install it in the viewport.
        """
