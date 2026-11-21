# Houdini stubs generated from Houdini 22.0.466

import hpackage
from pathlib import Path
from typing import Literal

theScannablePaths: list[tuple[Path, str | None, bool]] | None

def makeUserPackageFilePath(file_base_name: str) -> str:
    """ Create a package file path under the user folder.
        Returns the package file path.
    """
def makePackageFilePath(package_name: str, package_path: str | None = None, add_to_packages: bool = False) -> str | Literal[-1]:
    """ Create a package file path under package_path/packages.
        Returns the package file path.
    """
def writeUserPackageFile(file_base_name: str, package_content: str) -> str:
    """ Create a new user package file, add package_content to 
        the file.
    """
def writePackageFile(file_base_name: str, package_content: str, package_path: str | None = None, add_to_packages: bool = False) -> str | Literal[-1]:
    """ Create a new package file, add package_content to the file.
    """
def createPackage(package_name: str, package_path: str | None = None, package_type: str | None = None, add_to_packages: bool = False, **kwargs_content: str) -> Path | None:
    """ Create a package on disk from a package template.
        Return 1 if successful, 0 if no package template was
        provided, -1 if an error occured.
    """
def loadPackageArchive(arc_file_content: bytes, arc_file_name: str | None = None, install_dir: str | None = None, extract_path: str | None = None) -> None:
    """ Loads the package(s) from an package archive file.

        arc_file_content:   The content of an archive in binary format. 
                            Note: only zip is supported for now.

        arc_file_name:      Optional archive file name. Used for 
                            create the file, defaults to a unique file 
                            name.

        install_dir:        Optional installation folder where to 
                            deploy the archive. A unique temporary 
                            folder is created if none is supplied.

        extract_path:       Optional folder path where to extract the 
                            archive. install_dir is used by default.
    """
def unloadPackageArchive() -> None:
    """ Unloads the package(s) previously loaded and uninstalls the 
        archive.
    """
def createPackageArchive(arch_file_path: str, package_file_path: str | None, content_folder_path: str, include_folder_as_root: bool = True, archive_type: str = '.zip') -> bool:
    """ Create a package archive. A package archive contains
        a content folder with subfolders and a package file. 
        An archive is typically used for embedding a plugin, 
        the resulting archive can be extracted and installed 
        with PackageArc.install().

        arch_file_path: The full path name of the new archive.
        package_file_path: The full path package to archive. The
                           package is optional and can be generated
                           when loading the package.

        content_folder_path: The folder to archive. The content 
                            is archived under content folder 
                            name. The folder structure is 
                            preserved in the archive

        include_folder_as_root: 
                            When True, the content folder will 
                            be included as the root folder in the 
                            archive. This means that when you 
                            extract the contents of the archive, 
                            the folder itself will appear at the 
                            top level, containing all the subfolders 
                            and files inside it.

                            When False, only the contents of the 
                            folder (subfolders and files) will 
                            be archived. When you extract the 
                            archive, the files and subfolders will 
                            appear directly at the top level, 
                            without the outer folder.

        archive_type: Archive type. Defaults to zip.

        The structure of the archive is the following:
            arch_file_path.zip
            ./{content folder name}/
            ./{content folder name}{resource folders ...}
            ./{package file name}.json  
    """
def isPackageAutoLoaded(package_file_path: str) -> bool:
    """ Return True if package_file_path is auto-loaded and 
        located in a folder scannable by Houdini i.e. the package 
        path must match one of these:
        $HOUDINI_USER_PREF_DIR/packages
        $HFS/packages
        $HSITE/../packages
        $HOUDINI_PACKAGE_DIR
    """

class PackageArcError(Exception): ...

class PackageArc:
    ''' Class utility to install/uninstall a package from a package 
        archive.

        Here\'s an example to demonstrate how to use it for loading a 
        package embedded in an HDA with a zip file.

        1) Add a zip file containing the package/plugin files in the 
           Extra Files section. For instance, add the zip file in the 
           "zip_example" section.

        2) Python Module: contains the functions used by the HDA to
                          load/unload a package archive.
        
        import hpackage.utils 

        def loadPackageArchive(arc_file_content=None, arc_file_name=None, install_dir=None, extract_path=None):
            return hpackage.utils.loadPackageArchive(arc_file_content, arc_file_name, install_dir, extract_path)

        def unloadPackageArchive():
            return hpackage.utils.unloadPackageArchive()

        3) OnLoaded: Called when the HDA is loaded. It installs the 
                     embedded zip file on disk and loads the package(s) 
                     from the zip file.

        arc_file_content = kwargs["type"].definition().sections()["zip_example"].contents()
        kwargs["type"].hdaModule().loadPackageArchive(arc_file_content)

        4) OnDeleted: Called when the HDA is deleted. It unloads the 
                      package(s) previously loaded in OnLoaded and 
                      uninstalls the archive.

        kwargs["type"].hdaModule().unloadPackageArchive()

    '''
    arc_file_name: str | None
    arc_file_path: str | None
    arc_path: str | None
    package_files: tuple[str, ...] | None
    log: bool
    @staticmethod
    def instance() -> PackageArc:
        """ Static access method. 
        """
    def __init__(self) -> None: ...
    def createArchive(self, arch_file_path: str, package_file_path: str | None, content_folder_path: str, include_folder_as_root: bool, archive_type: str) -> bool: ...
    def install(self, arc_file_content: bytes, arc_file_name: str | None = None, install_dir: str | None = None, archive_type: str = '.zip') -> None:
        """ Save the archive on disk.
        """
    def uninstall(self) -> None: ...
    def load(self, extract_path: str | None = None) -> tuple[str, ...] | None:
        """ Load the package from the archive.
        """
    def unload(self) -> None: ...
