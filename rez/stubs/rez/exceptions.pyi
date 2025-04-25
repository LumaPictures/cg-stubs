from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from typing import Any

class RezError(Exception):
    """Base-class Rez error."""
    value: Any
    def __init__(self, value: Incomplete | None = None) -> None: ...
    def __str__(self) -> str: ...

class RezSystemError(RezError):
    """Rez system/internal error."""
class RezBindError(RezError):
    """A bind-related error."""
class RezPluginError(RezError):
    """An error related to plugin or plugin load."""
class ConfigurationError(RezError):
    """A misconfiguration error."""
class ResolveError(RezError):
    """A resolve-related error."""
class PackageFamilyNotFoundError(RezError):
    """A package could not be found on disk."""
class PackageNotFoundError(RezError):
    """A package could not be found on disk."""
class ResourceError(RezError):
    """Resource-related exception base class."""
class ResourceNotFoundError(ResourceError):
    """A resource could not be found."""

class ResourceContentError(ResourceError):
    """A resource contains incorrect data."""
    type_name: str
    def __init__(self, value: Incomplete | None = None, path: Incomplete | None = None, resource_key: Incomplete | None = None) -> None: ...

class PackageMetadataError(ResourceContentError):
    """There is an error in a package's definition file."""
    type_name: str

class PackageCommandError(RezError):
    """There is an error in a command or list of commands"""
class PackageRequestError(RezError):
    """There is an error related to a package request."""
class PackageCopyError(RezError):
    """There was a problem copying a package."""
class PackageMoveError(RezError):
    """There was a problem moving a package."""
class ContextBundleError(RezError):
    """There was a problem bundling a context."""
class PackageCacheError(RezError):
    """There was an error related to a package cache."""
class PackageTestError(RezError):
    """There was a problem running a package test."""
class ResolvedContextError(RezError):
    """An error occurred in a resolved context."""
class RexError(RezError):
    """There is an error in Rex code."""
class RexUndefinedVariableError(RexError):
    """There is a reference to an undefined variable."""
class RexStopError(RexError):
    """Special error raised when a package commands uses the 'stop' command."""
class BuildError(RezError):
    """Base class for any build-related error."""
class BuildSystemError(BuildError):
    """Base class for buildsys-related errors."""

class BuildContextResolveError(BuildError):
    """Raised if unable to resolve the required context when creating the
    environment for a build process."""
    context: Any
    def __init__(self, context) -> None: ...

class BuildProcessError(RezError):
    """Base class for build process-related errors."""
class ReleaseError(RezError):
    """Any release-related error."""
class ReleaseVCSError(ReleaseError):
    """Base class for release VCS-related errors."""
class ReleaseHookError(RezError):
    """Base class for release-hook- related errors."""
class ReleaseHookCancellingError(RezError):
    """A release hook error that asks to cancel the release as a result."""
class SuiteError(RezError):
    """Any suite-related error."""
class PackageRepositoryError(RezError):
    """Base class for package repository- related errors."""
class InvalidPackageError(RezError):
    """A special case exception used in package 'preprocess function'."""
class RezGuiQTImportError(ImportError):
    """A special case - see cli/gui.py
    """
class _NeverError(RezError):
    """Exception that is never raised.

    Used to toggle exception handling in some cases.
    """

@contextmanager
def convert_errors(from_, to, msg: Incomplete | None = None) -> Generator[None]: ...
