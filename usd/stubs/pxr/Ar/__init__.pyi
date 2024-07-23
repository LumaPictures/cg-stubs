# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Tf
import types
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class AssetInfo(Boost.Python.instance):
    """
    Contains information about a resolved asset.
    """
    __instance_size__: ClassVar[int] = ...
    assetName: Incomplete
    resolverInfo: Incomplete
    version: Incomplete
    def __init__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class DefaultResolver(Resolver):
    '''
    Default asset resolution implementation used when no plugin
    implementation is provided.


    In order to resolve assets specified by relative paths, this resolver
    implements a simple"search path"scheme. The resolver will anchor the
    relative path to a series of directories and return the first absolute
    path where the asset exists.

    The first directory will always be the current working directory. The
    resolver will then examine the directories specified via the following
    mechanisms (in order):

       - The currently-bound ArDefaultResolverContext for the calling
         thread

       - ArDefaultResolver::SetDefaultSearchPath

    The environment variable PXR_AR_DEFAULT_SEARCH_PATH may be used to
    specify an inital search path value. This is expected to be a list of
    directories delimited by the platform\'s standard path separator. A
    search path specified in this manner is overwritten by any call to
    ArDefaultResolver::SetDefaultSearchPath.

    ArDefaultResolver supports creating an ArDefaultResolverContext via
    ArResolver::CreateContextFromString by passing a list of directories
    delimited by the platform\'s standard path separator.
    '''
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def SetDefaultSearchPath(searchPath: typing.Iterable[str | ResolvedPath]) -> None:
        """
        Set the default search path that will be used during asset resolution.


        Calling this function will trigger a ResolverChanged notification to
        be sent if the search path differs from the currently set default
        value.

        The inital search path may be specified using via the environment
        variable PXR_AR_DEFAULT_SEARCH_PATH. Calling this function will
        override any path specified in this manner.

        This function is not thread-safe and should not be called concurrently
        with any other ArResolver operations
        """

class DefaultResolverContext(Boost.Python.instance):
    '''
    Resolver context object that specifies a search path to use during
    asset resolution.


    This object is intended for use with the default ArDefaultResolver
    asset resolution implementation; see documentation for that class for
    more details on the search path resolution algorithm.

    Example usage: ::

      ArDefaultResolverContext ctx({"/Local/Models", "/Installed/Models"});
      {
          // Bind the context object:
          ArResolverContextBinder binder(ctx);
  
         // While the context is bound, all calls to ArResolver::Resolve
         // (assuming ArDefaultResolver is the underlying implementation being
         // used) will include the specified paths during resolution.
         std::string resolvedPath = resolver.Resolve("ModelName/File.txt")
      }
  
      // Once the context is no longer bound (due to the ArResolverContextBinder
      // going out of scope), its search path no longer factors into asset
      // resolution.

    '''
    @overload
    def __init__(self) -> None:
        """
        Default construct a context with no search path.
        """
    @overload
    def __init__(self, searchPaths: typing.Iterable[str | ResolvedPath]) -> None:
        """
        Construct a context with the given C{searchPath}.


        Elements in C{searchPath} should be absolute paths. If they are not,
        they will be anchored to the current working directory.
        """
    def GetSearchPath(self) -> list[str]:
        """
        Return this context's search path.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class Notice(Boost.Python.instance):
    class ResolverChanged(Notice.ResolverNotice):
        """
        Notice sent when asset paths may resolve to a different path than
        before due to a change in the resolver.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def AffectsContext(self, context: ResolverContext) -> bool:
            """
            Returns true if the results of asset resolution when C{ctx} is bound
            may be affected by this resolver change.
            """

    class ResolverNotice(pxr.Tf.Notice):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ResolvedPath(Boost.Python.instance):
    """
    Represents a resolved asset path.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    def GetPathString(self) -> str:
        """
        Return the resolved path held by this object as a string.
        """
    def __bool__(self) -> bool:
        """
        Return true if this object is holding a non-empty resolved path, false
        otherwise.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Resolver(Boost.Python.instance):
    """
    Interface for the asset resolution system.


    An asset resolver is responsible for resolving asset information
    (including the asset's physical path) from a logical path.

    See ar_implementing_resolver for information on how to customize asset
    resolution behavior by implementing a subclass of ArResolver. Clients
    may use ArGetResolver to access the configured asset resolver.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def CanWriteAssetToPath(self, resolvedPath: ResolvedPath) -> _PyAnnotatedBoolResult:
        """
        Returns true if an asset may be written to the given C{resolvedPath},
        false otherwise.


        If this function returns false and C{whyNot} is not C{nullptr}, it may
        be filled with an explanation.
        """
    @overload
    def CreateContextFromString(self, contextStr: str | ResolvedPath) -> ResolverContext:
        """
        Return an ArResolverContext created from the primary ArResolver
        implementation using the given C{contextStr}.
        """
    @overload
    def CreateContextFromString(self, uriScheme: str | ResolvedPath, contextStr: str | ResolvedPath) -> ResolverContext:
        """
        Return an ArResolverContext created from the ArResolver registered for
        the given C{uriScheme} using the given C{contextStr}.


        An empty C{uriScheme} indicates the primary resolver and is equivalent
        to CreateContextFromString(string).

        If no resolver is registered for C{uriScheme}, returns an empty
        ArResolverContext.

        'uriScheme'can be used to register IRI resolvers
        """
    def CreateContextFromStrings(self, contextStrs: typing.Iterable[tuple[str | ResolvedPath, str | ResolvedPath]]) -> ResolverContext:
        '''
        Return an ArResolverContext created by combining the ArResolverContext
        objects created from the given C{contextStrs}.


        C{contextStrs} is a list of pairs of strings. The first element in the
        pair is the URI/IRI scheme for the ArResolver that will be used to
        create the ArResolverContext from the second element in the pair. An
        empty resource identifier scheme indicates the primary resolver.

        For example: ::

          ArResolverContext ctx = ArGetResolver().CreateContextFromStrings(
             { {"", "context str 1"}, 
               {"my-scheme", "context str 2"} });

        This will use the primary resolver to create an ArResolverContext
        using the string"context str 1"and use the resolver registered for
        the"my-scheme"URI/IRI scheme to create an ArResolverContext
        using"context str 2". These contexts will be combined into a single
        ArResolverContext and returned.

        If no resolver is registered for a URI/IRI scheme in an entry in
        C{contextStrs}, that entry will be ignored.
        '''
    def CreateDefaultContext(self) -> ResolverContext:
        """
        Return an ArResolverContext that may be bound to this resolver to
        resolve assets when no other context is explicitly specified.


        The returned ArResolverContext will contain the default context
        returned by the primary resolver and all URI/IRI resolvers.
        """
    def CreateDefaultContextForAsset(self, assetPath: str | ResolvedPath) -> ResolverContext:
        """
        Return an ArResolverContext that may be bound to this resolver to
        resolve the asset located at C{assetPath} or referenced by that asset
        when no other context is explicitly specified.


        The returned ArResolverContext will contain the default context for
        C{assetPath} returned by the primary resolver and all URI/IRI
        resolvers.
        """
    def CreateIdentifier(self, assetPath: str | ResolvedPath, anchorAssetPath: ResolvedPath = ...) -> str:
        """
        Returns an identifier for the asset specified by C{assetPath}.


        If C{anchorAssetPath} is not empty, it is the resolved asset path that
        C{assetPath} should be anchored to if it is a relative path.
        """
    def CreateIdentifierForNewAsset(self, assetPath: str | ResolvedPath, anchorAssetPath: ResolvedPath = ...) -> str:
        """
        Returns an identifier for a new asset specified by C{assetPath}.


        If C{anchorAssetPath} is not empty, it is the resolved asset path that
        C{assetPath} should be anchored to if it is a relative path.
        """
    def GetAssetInfo(self, assetPath: str | ResolvedPath, resolvedPath: ResolvedPath) -> AssetInfo:
        """
        Returns an ArAssetInfo populated with additional metadata (if any)
        about the asset at the given C{assetPath}.


        C{resolvedPath} is the resolved path computed for the given
        C{assetPath}.
        """
    def GetCurrentContext(self) -> ResolverContext:
        """
        Returns the asset resolver context currently bound in this thread.



        ArResolver::BindContext, ArResolver::UnbindContext
        """
    def GetExtension(self, assetPath: str | ResolvedPath) -> str:
        '''
        Returns the file extension for the given C{assetPath}.


        The returned extension does not include a"."at the beginning.
        '''
    def GetModificationTimestamp(self, assetPath: str | ResolvedPath, resolvedPath: ResolvedPath) -> Timestamp:
        """
        Returns an ArTimestamp representing the last time the asset at
        C{assetPath} was modified.


        C{resolvedPath} is the resolved path computed for the given
        C{assetPath}. If a timestamp cannot be retrieved, return an invalid
        ArTimestamp.
        """
    def IsContextDependentPath(self, assetPath: str | ResolvedPath) -> bool:
        """
        Returns true if C{assetPath} is a context-dependent path, false
        otherwise.


        A context-dependent path may result in different resolved paths
        depending on what asset resolver context is bound when Resolve is
        called. Assets located at the same context-dependent path may not be
        the same since those assets may have been loaded from different
        resolved paths. In this case, the assets'resolved paths must be
        consulted to determine if they are the same.
        """
    def RefreshContext(self, _context: ResolverContext, /) -> None:
        """
        Refresh any caches associated with the given context.


        If doing so would invalidate asset paths that had previously been
        resolved, an ArNotice::ResolverChanged notice will be sent to inform
        clients of this.

        Avoid calling RefreshContext() on the same context from more than one
        thread concurrently as ArNotice::ResolverChanged notice listeners may
        mutate their state in response to receiving the notice.

        Avoid calling RefreshContext() with a context that is active (bound to
        a resolver). Unbind the context before refreshing it.

        Threading Model and Performance Considerations
        """
    def Resolve(self, assetPath: str | ResolvedPath) -> ResolvedPath:
        """
        Returns the resolved path for the asset identified by the given
        C{assetPath} if it exists.


        If the asset does not exist, returns an empty ArResolvedPath.
        """
    def ResolveForNewAsset(self, assetPath: str | ResolvedPath) -> ResolvedPath:
        """
        Returns the resolved path for the given C{assetPath} that may be used
        to create a new asset.


        If such a path cannot be computed for C{assetPath}, returns an empty
        ArResolvedPath.

        Note that an asset might or might not already exist at the returned
        resolved path.
        """

class ResolverContext(Boost.Python.instance):
    """
    An asset resolver context allows clients to provide additional data to
    the resolver for use during resolution.


    Clients may provide this data via context objects of their own
    (subject to restrictions below). An ArResolverContext is simply a
    wrapper around these objects that allows it to be treated as a single
    type. Note that an ArResolverContext may not hold multiple context
    objects with the same type.

    A client-defined context object must provide the following:
       - Default and copy constructors

       - operator<

       - operator==

       - An overload for size_t hash_value(const T&)

    Note that the user may define a free function:

    std::string ArGetDebugString(const Context & ctx); (Where Context is
    the type of the user's path resolver context.)

    This is optional; a default generic implementation has been
    predefined. This function should return a string representation of the
    context to be utilized for debugging purposes(such as in TF_DEBUG
    statements).

    The ArIsContextObject template must also be specialized for this
    object to declare that it can be used as a context object. This is to
    avoid accidental use of an unexpected object as a context object. The
    AR_DECLARE_RESOLVER_CONTEXT macro can be used to do this as a
    convenience.

    AR_DECLARE_RESOLVER_CONTEXT

    ArResolver::BindContext

    ArResolver::UnbindContext

    ArResolverContextBinder
    """
    @overload
    def __init__(self) -> None:
        """
        Construct an empty asset resolver context.
        """
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    def Get(self) -> list:
        """
        Returns pointer to the context object of the given type held in this
        resolver context.


        Returns None if this resolver context is not holding an object of the
        requested type.
        """
    def GetDebugString(self) -> str:
        """
        Returns a debug string representing the contained context objects.
        """
    def IsEmpty(self) -> bool:
        """
        Returns whether this resolver context is empty.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class ResolverContextBinder(Boost.Python.instance):
    """
    Helper object for managing the binding and unbinding of
    ArResolverContext objects with the asset resolver.


    Context binding and unbinding are thread-specific. If you bind a
    context in a thread, that binding will only be visible to that thread.
    See Resolver Contexts for more details.

    Asset Resolver Context Operations
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self, _context: ResolverContext, /) -> None:
        """
        Bind the given C{context} with the asset resolver.


        Calls ArResolver::BindContext on the configured asset resolver and
        saves the bindingData populated by that function.
        """
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool: ...

class ResolverScopedCache(Boost.Python.instance):
    """
    Helper object for managing asset resolver cache scopes.


    A scoped resolution cache indicates to the resolver that results of
    calls to Resolve should be cached for a certain scope. This is
    important for performance and also for consistency  it ensures that
    repeated calls to Resolve with the same parameters will return the
    same result.

    Scoped Resolution Cache
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None:
        """
        Begin an asset resolver cache scope.


        Calls ArResolver::BeginCacheScope on the configured asset resolver and
        saves the cacheScopeData populated by that function.
        """
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool: ...

class Timestamp(Boost.Python.instance):
    """
    Represents a timestamp for an asset.


    Timestamps are represented by Unix time, the number of seconds elapsed
    since 00:00:00 UTC 1/1/1970.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Create an invalid timestamp.
        """
    @overload
    def __init__(self, _time: Timestamp, /) -> None:
        """
        Create a timestamp at C{time}, which must be a Unix time value.
        """
    @overload
    def __init__(self, arg2: float, /) -> None: ...
    def GetTime(self) -> float:
        """
        Return the time represented by this timestamp as a double.


        If this timestamp is invalid, issue a coding error and return a quiet
        NaN value.
        """
    def IsValid(self) -> bool:
        """
        Return true if this timestamp is valid, false otherwise.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class _PyAnnotatedBoolResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

def GetRegisteredURISchemes() -> list[str]:
    """
    Returns list of all URI schemes for which a resolver has been
    registered.


    Schemes are returned in all lower-case and in alphabetically sorted
    order.
    """
def GetResolver() -> Resolver:
    """
    Returns the configured asset resolver.


    When first called, this function will determine the ArResolver
    subclass to use for asset resolution via the following process:

       - If a preferred resolver has been set via ArSetPreferredResolver,
         it will be selected.

       - Otherwise, a list of available ArResolver subclasses in plugins
         will be generated. If multiple ArResolver subclasses are found, the
         list will be sorted by typename. ArDefaultResolver will be added as
         the last element of this list, and the first resolver in the list will
         be selected.

       - The plugin for the selected subclass will be loaded and an
         instance of the subclass will be constructed.

       - If an error occurs, an ArDefaultResolver will be constructed.

    The constructed ArResolver subclass will be cached and used to service
    function calls made on the returned resolver.

    Note that this function may not return the constructed subclass
    itself, meaning that dynamic casts to the subclass type may fail. See
    ArGetUnderlyingResolver if access to this object is needed.
    """
def GetUnderlyingResolver() -> Resolver:
    """
    Returns the underlying ArResolver instance used by ArGetResolver.


    This function returns the instance of the ArResolver subclass used by
    ArGetResolver and can be dynamic_cast to that type.

    This functions should typically not be used by consumers except in
    very specific cases. Consumers who want to retrieve an ArResolver to
    perform asset resolution should use ArGetResolver.
    """
def IsPackageRelativePath(path: str | ResolvedPath) -> bool:
    """
    Return true if C{path} is a package-relative path, false otherwise.
    """
@overload
def JoinPackageRelativePath(packagePath: str | ResolvedPath, packagedPath: str | ResolvedPath) -> str:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def JoinPackageRelativePath(paths: object) -> str: ...
def SetPreferredResolver(resolverTypeName: str | ResolvedPath) -> None:
    """
    Set the preferred ArResolver subclass used by ArGetResolver.


    Consumers may override ArGetResolver's plugin resolver discovery and
    force the use of a specific resolver subclass by calling this function
    with the typename of the implementation to use.

    If the subclass specified by C{resolverTypeName} cannot be found,
    ArGetResolver will issue a warning and fall back to using
    ArDefaultResolver.

    This must be called before the first call to ArGetResolver.
    """
def SplitPackageRelativePathInner(path: str | ResolvedPath) -> tuple[str, str]:
    '''
    Split package-relative path C{path} into a (package path, packaged
    path) pair.


    If C{packageRelativePath} contains nested package-relative paths the
    package path will be the outermost package-relative path, and the
    packaged path will be the innermost packaged path. ::

      ArSplitPackageRelativePathInner("a.pack[b.pack]")
         => ("a.pack", "b.pack")
  
      ArSplitPackageRelativePathInner("a.pack[b.pack[c.pack]]")
         => ("a.pack[b.pack]", "c.pack")

    '''
def SplitPackageRelativePathOuter(path: str | ResolvedPath) -> tuple[str, str]:
    '''
    Split package-relative path C{path} into a (package path, packaged
    path) pair.


    If C{packageRelativePath} contains nested package-relative paths the
    package path will be the outermost package path, and the packaged path
    will be the inner package-relative path. ::

      ArSplitPackageRelativePathOuter("a.pack[b.pack]")
         => ("a.pack", "b.pack")
  
      ArSplitPackageRelativePathOuter("a.pack[b.pack[c.pack]]")
         => ("a.pack", "b.pack[c.pack]")

    '''
def _TestImplicitConversion(arg1: ResolverContext, /) -> ResolverContext: ...
