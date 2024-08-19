# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Tf
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

VersionFilterAllVersions: VersionFilter
VersionFilterDefaultOnly: VersionFilter
__MFB_FULL_PACKAGE_NAME: str

class DiscoveryPlugin(Boost.Python.instance):
    '''
    Interface for discovery plugins.


    Discovery plugins, like the name implies, find nodes. Where the plugin
    searches is up to the plugin that implements this interface. Examples
    of discovery plugins could include plugins that look for nodes on the
    filesystem, another that finds nodes in a cloud service, and another
    that searches a local database. Multiple discovery plugins that search
    the filesystem in specific locations/ways could also be created. All
    discovery plugins are executed as soon as the registry is
    instantiated.

    These plugins simply report back to the registry what nodes they found
    in a generic way. The registry doesn\'t know much about the innards of
    the nodes yet, just that the nodes exist. Understanding the nodes is
    the responsibility of another set of plugins defined by the
    C{NdrParserPlugin} interface.

    Discovery plugins report back to the registry via
    C{NdrNodeDiscoveryResult} s. These are small, lightweight classes that
    contain the information for a single node that was found during
    discovery. The discovery result only includes node information that
    can be gleaned pre-parse, so the data is fairly limited; to see
    exactly what\'s included, and what is expected to be populated, see the
    documentation for C{NdrNodeDiscoveryResult}.

    How to Create a Discovery Plugin
    ================================

    There are three steps to creating a discovery plugin:
       - Implement the discovery plugin interface, C{NdrDiscoveryPlugin}

       - Register your new plugin with the registry. The registration
         macro must be called in your plugin\'s implementation file: ::

      NDR_REGISTER_DISCOVERY_PLUGIN(YOUR_DISCOVERY_PLUGIN_CLASS_NAME)

     This macro is available in discoveryPlugin.h.

       - In the same folder as your plugin, create a C{plugInfo.json}
         file. This file must be formatted like so, substituting
         C{YOUR_LIBRARY_NAME}, C{YOUR_CLASS_NAME}, and C{YOUR_DISPLAY_NAME} :
         ::

      {
          "Plugins": [{
              "Type": "module",
              "Name": "YOUR_LIBRARY_NAME",
              "Root": "@PLUG_INFO_ROOT@",
              "LibraryPath": "@PLUG_INFO_LIBRARY_PATH@",
              "ResourcePath": "@PLUG_INFO_RESOURCE_PATH@",
              "Info": {
                  "Types": {
                      "YOUR_CLASS_NAME" : {
                          "bases": ["NdrDiscoveryPlugin"],
                          "displayName": "YOUR_DISPLAY_NAME"
                      }
                  }
              }
          }]
      }

    The NDR ships with one discovery plugin, the
    C{_NdrFilesystemDiscoveryPlugin}. Take a look at NDR\'s plugInfo.json
    file for example values for C{YOUR_LIBRARY_NAME}, C{YOUR_CLASS_NAME},
    and C{YOUR_DISPLAY_NAME}. If multiple discovery plugins exist in the
    same folder, you can continue adding additional plugins under the
    C{Types} key in the JSON. More detailed information about the
    plugInfo.json format can be found in the documentation for the C{plug}
    module (in pxr/base).

    '''
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @overload
    def DiscoverNodes(self, _unknownArg1: DiscoveryPluginContext, /) -> None:
        """
        Finds and returns all nodes that the implementing plugin should be
        aware of.
        """
    @overload
    def DiscoverNodes(self, arg2: DiscoveryPluginContext, /) -> Any: ...
    @overload
    def GetSearchURIs(self) -> None:
        """
        Gets the URIs that this plugin is searching for nodes in.
        """
    @overload
    def GetSearchURIs(self) -> Any: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

class DiscoveryPluginContext(Boost.Python.instance):
    """
    A context for discovery.


    Discovery plugins can use this to get a limited set of non-local
    information without direct coupling between plugins.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @overload
    def GetSourceType(self, _discoveryType: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Returns the source type associated with the discovery type.


        This may return an empty token if there is no such association.
        """
    @overload
    def GetSourceType(self, arg2: object, /) -> Any: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

class DiscoveryPluginList(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def append(self, arg2: object, /) -> None: ...
    def extend(self, arg2: object, /) -> None: ...
    def __contains__(self, arg2: object, /) -> bool: ...
    def __delitem__(self, arg2: object, /) -> None: ...
    def __getitem__(self, arg2: object, /) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...

class DiscoveryUri(Boost.Python.instance):
    """
    Struct for holding a URI and its resolved URI for a file discovered by
    NdrFsHelpersDiscoverFiles.
    """
    __instance_size__: ClassVar[int] = ...
    resolvedUri: Incomplete
    uri: Incomplete
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: DiscoveryUri, /) -> None: ...

class Node(Boost.Python.instance):
    """
    Represents an abstract node.


    Describes information like the name of the node, what its inputs and
    outputs are, and any associated metadata.

    In almost all cases, this class will not be used directly. More
    specialized nodes can be created that derive from C{NdrNode}; those
    specialized nodes can add their own domain-specific data and methods.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetContext(self) -> str:
        """
        Gets the context of the node.


        The context is the context that the node declares itself as having
        (or, if a particular node does not declare a context, it will be
        assigned a default context by the parser).

        As a concrete example from the C{Sdr} module, a shader with a
        specific source type may perform different duties vs. another shader
        with the same source type. For example, one shader with a source type
        of C{SdrArgsParser::SourceType} may declare itself as having a context
        of'pattern', while another shader of the same source type may say it
        is used for lighting, and thus has a context of'light'.
        """
    def GetFamily(self) -> str:
        """
        Gets the name of the family that the node belongs to.


        An empty token will be returned if the node does not belong to a
        family.
        """
    def GetIdentifier(self) -> str:
        """
        Return the identifier of the node.
        """
    def GetInfoString(self) -> str:
        """
        Gets a string with basic information about this node.


        Helpful for things like adding this node to a log.
        """
    def GetInput(self, _inputName: str | pxr.Ar.ResolvedPath, /) -> Property:
        """
        Get an input property by name.


        C{nullptr} is returned if an input with the given name does not exist.
        """
    def GetInputNames(self) -> list[str]:
        """
        Get an ordered list of all the input names on this node.
        """
    def GetMetadata(self) -> dict:
        """
        All metadata that came from the parse process.


        Specialized nodes may isolate values in the metadata (with possible
        manipulations and/or additional parsing) and expose those values in
        their API.
        """
    def GetName(self) -> str:
        """
        Gets the name of the node.
        """
    def GetOutput(self, _outputName: str | pxr.Ar.ResolvedPath, /) -> Property:
        """
        Get an output property by name.


        C{nullptr} is returned if an output with the given name does not
        exist.
        """
    def GetOutputNames(self) -> list[str]:
        """
        Get an ordered list of all the output names on this node.
        """
    def GetResolvedDefinitionURI(self) -> str:
        """
        Gets the URI to the resource that provided this node's definition.


        Could be a path to a file, or some other resource identifier. This URI
        should be fully resolved.

        NdrNode::GetResolvedImplementationURI()
        """
    def GetResolvedImplementationURI(self) -> str:
        """
        Gets the URI to the resource that provides this node's implementation.


        Could be a path to a file, or some other resource identifier. This URI
        should be fully resolved.

        NdrNode::GetResolvedDefinitionURI()
        """
    def GetSourceCode(self) -> str:
        """
        Returns the source code for this node.


        This will be empty for most nodes. It will be non-empty only for the
        nodes that are constructed using NdrRegistry::GetNodeFromSourceCode()
        , in which case, the source code has not been parsed (or even
        compiled) yet.

        An unparsed node with non-empty source-code but no properties is
        considered to be invalid. Once the node is parsed and the relevant
        properties and metadata are extracted from the source code, the node
        becomes valid.

        NdrNode::IsValid
        """
    def GetSourceType(self) -> str:
        """
        Gets the type of source that this node originated from.


        Note that this is distinct from C{GetContext()} , which is the type
        that the node declares itself as having.

        As a concrete example from the C{Sdr} module, several shader parsers
        exist and operate on different types of shaders. In this scenario,
        each distinct type of shader (OSL, Args, etc) is considered a
        different *source*, even though they are all shaders. In addition, the
        shaders under each source type may declare themselves as having a
        specific context (shaders can serve different roles). See
        C{GetContext()} for more information on this.
        """
    def GetVersion(self) -> Version:
        """
        Return the version of the node.
        """
    def IsValid(self) -> bool:
        """
        Whether or not this node is valid.


        A node that is valid indicates that the parser plugin was able to
        successfully parse the contents of this node.

        Note that if a node is not valid, some data like its name, URI, source
        code etc. could still be available (data that was obtained during the
        discovery process). However, other data that must be gathered from the
        parsing process will NOT be available (eg, inputs and outputs).
        """
    def __bool__(self) -> bool: ...

class NodeDiscoveryResult(Boost.Python.instance):
    """
    Represents the raw data of a node, and some other bits of metadata,
    that were determined via a C{NdrDiscoveryPlugin}.
    """
    def __init__(self, identifier: str | pxr.Ar.ResolvedPath, version: Version, name: str | pxr.Ar.ResolvedPath, family: str | pxr.Ar.ResolvedPath, discoveryType: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath, uri: str | pxr.Ar.ResolvedPath, resolvedUri: str | pxr.Ar.ResolvedPath, sourceCode: str | pxr.Ar.ResolvedPath = ..., metadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath] = ..., blindData: str | pxr.Ar.ResolvedPath = ..., subIdentifier: str | pxr.Ar.ResolvedPath = ...) -> None:
        """
        Constructor.
        """
    @property
    def blindData(self): ...
    @property
    def discoveryType(self): ...
    @property
    def family(self): ...
    @property
    def identifier(self): ...
    @property
    def metadata(self): ...
    @property
    def name(self): ...
    @property
    def resolvedUri(self): ...
    @property
    def sourceCode(self): ...
    @property
    def sourceType(self): ...
    @property
    def subIdentifier(self): ...
    @property
    def uri(self): ...
    @property
    def version(self): ...

class NodeList(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def append(self, arg2: object, /) -> None: ...
    def extend(self, arg2: object, /) -> None: ...
    def __contains__(self, arg2: object, /) -> bool: ...
    def __delitem__(self, arg2: object, /) -> None: ...
    def __getitem__(self, arg2: object, /) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...

class Property(Boost.Python.instance):
    """
    Represents a property (input or output) that is part of a C{NdrNode}
    instance.


    A property must have a name and type, but may also specify a host of
    additional metadata. Instances can also be queried to determine if
    another C{NdrProperty} instance can be connected to it.

    In almost all cases, this class will not be used directly. More
    specialized properties can be created that derive from C{NdrProperty};
    those specialized properties can add their own domain-specific data
    and methods.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def CanConnectTo(self, _other: Property, /) -> bool:
        """
        Determines if this property can be connected to the specified
        property.
        """
    def GetArraySize(self) -> int:
        """
        Gets this property's array size.


        If this property is a fixed-size array type, the array size is
        returned. In the case of a dynamically-sized array, this method
        returns the array size that the parser reports, and should not be
        relied upon to be accurate. A parser may report -1 for the array size,
        for example, to indicate a dynamically-sized array. For types that are
        not a fixed-size array or dynamic array, this returns 0.
        """
    def GetDefaultValue(self) -> Any:
        """
        Gets this property's default value associated with the type of the
        property.



        GetType()
        """
    def GetInfoString(self) -> str:
        """
        Gets a string with basic information about this property.


        Helpful for things like adding this property to a log.
        """
    def GetMetadata(self) -> dict:
        """
        All of the metadata that came from the parse process.
        """
    def GetName(self) -> str:
        """
        Gets the name of the property.
        """
    def GetType(self) -> str:
        """
        Gets the type of the property.
        """
    def GetTypeAsSdfType(self) -> tuple:
        """
        Converts the property's type from C{GetType()} into a
        C{SdfValueTypeName}.


        Two scenarios can result: an exact mapping from property type to Sdf
        type, and an inexact mapping. In the first scenario, the first element
        in the pair will be the cleanly-mapped Sdf type, and the second
        element, a TfToken, will be empty. In the second scenario, the Sdf
        type will be set to C{Token} to indicate an unclean mapping, and the
        second element will be set to the original type returned by
        C{GetType()} .

        This base property class is generic and cannot know ahead of time how
        to perform this mapping reliably, thus it will always fall into the
        second scenario. It is up to specialized properties to perform the
        mapping.

        GetDefaultValueAsSdfType()
        """
    def IsArray(self) -> bool:
        """
        Whether this property's type is an array type.
        """
    def IsConnectable(self) -> bool:
        """
        Whether this property can be connected to other properties.
        """
    def IsDynamicArray(self) -> bool:
        """
        Whether this property's array type is dynamically-sized.
        """
    def IsOutput(self) -> bool:
        """
        Whether this property is an output.
        """

class Registry(Boost.Python.instance):
    '''
    The registry provides access to node information.


    "Discovery Plugins"are responsible for finding the nodes that should
    be included in the registry.

    Discovery plugins are found through the plugin system. If additional
    discovery plugins need to be specified, a client can pass them to
    C{SetExtraDiscoveryPlugins()} .

    When the registry is first told about the discovery plugins, the
    plugins will be asked to discover nodes. These plugins will generate
    C{NdrNodeDiscoveryResult} instances, which only contain basic
    metadata. Once the client asks for information that would require the
    node\'s contents to be parsed (eg, what its inputs and outputs are),
    the registry will begin the parsing process on an as-needed basis. See
    C{NdrNodeDiscoveryResult} for the information that can be retrieved
    without triggering a parse.

    Some methods in this module may allow for a"family"to be provided. A
    family is simply a generic grouping which is optional.
    '''
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetAllNodeSourceTypes(self) -> list[str]:
        """
        Get a sorted list of all node source types that may be present on the
        nodes in the registry.


        Source types originate from the discovery process, but there is no
        guarantee that the discovered source types will also have a registered
        parser plugin. The actual supported source types here depend on the
        parsers that are available. Also note that some parser plugins may not
        advertise a source type.

        See the documentation for C{NdrParserPlugin} and
        C{NdrNode::GetSourceType()} for more information.
        """
    def GetNodeByIdentifier(self, identifier: str | pxr.Ar.ResolvedPath, typePriority: typing.Iterable[str | pxr.Ar.ResolvedPath] = ...) -> Node:
        """
        Get the node with the specified C{identifier}, and an optional
        C{sourceTypePriority} list specifying the set of node SOURCE types
        (see C{NdrNode::GetSourceType()} ) that should be searched.


        If no sourceTypePriority is specified, the first encountered node with
        the specified identifier will be returned (first is arbitrary) if
        found.

        If a sourceTypePriority list is specified, then this will iterate
        through each source type and try to find a node matching by
        identifier. This is equivalent to calling
        NdrRegistry::GetNodeByIdentifierAndType for each source type until a
        node is found.

        Nodes of the same identifier but different source type can exist in
        the registry. If a node'Foo'with source types'abc'and'xyz'exist in the
        registry, and you want to make sure the'abc'version is fetched before
        the'xyz'version, the priority list would be specified as
        ['abc','xyz']. If the'abc'version did not exist in the registry, then
        the'xyz'version would be returned.

        Returns C{nullptr} if a node matching the arguments can't be found.
        """
    def GetNodeByIdentifierAndType(self, identifier: str | pxr.Ar.ResolvedPath, nodeType: str | pxr.Ar.ResolvedPath) -> Node:
        """
        Get the node with the specified C{identifier} and C{sourceType}.


        If there is no matching node for the sourceType, nullptr is returned.
        """
    def GetNodeByName(self, name: str | pxr.Ar.ResolvedPath, typePriority: typing.Iterable[str | pxr.Ar.ResolvedPath] = ..., filter: VersionFilter = ...) -> Node:
        """
        Get the node with the specified name.


        An optional priority list specifies the set of node SOURCE types (

        NdrNode::GetSourceType() ) that should be searched and in what order.
        Optionally, a filter can be specified to consider just the default
        versions of nodes matching C{name} (the default) or all versions of
        the nodes.

        GetNodeByIdentifier() .
        """
    def GetNodeByNameAndType(self, name: str | pxr.Ar.ResolvedPath, nodeType: str | pxr.Ar.ResolvedPath, filter: VersionFilter = ...) -> Node:
        """
        A convenience wrapper around C{GetNodeByName()} .


        Instead of providing a priority list, an exact type is specified, and
        C{nullptr} is returned if a node with the exact identifier and type
        does not exist.

        Optionally, a filter can be specified to consider just the default
        versions of nodes matching C{name} (the default) or all versions of
        the nodes.
        """
    def GetNodeFromAsset(self, asset: pxr.Sdf.AssetPath | str, metadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath] = ..., subIdentifier: str | pxr.Ar.ResolvedPath = ..., sourceType: str | pxr.Ar.ResolvedPath = ...) -> Node:
        """
        Parses the given C{asset}, constructs a NdrNode from it and adds it to
        the registry.


        Nodes created from an asset using this API can be looked up by the
        unique identifier and sourceType of the returned node, or by URI,
        which will be set to the unresolved asset path value.

        C{metadata} contains additional metadata needed for parsing and
        compiling the source code in the file pointed to by C{asset}
        correctly. This metadata supplements the metadata available in the
        asset and overrides it in cases where there are key collisions.

        C{subidentifier} is optional, and it would be used to indicate a
        particular definition in the asset file if the asset contains multiple
        node definitions.

        C{sourceType} is optional, and it is only needed to indicate a
        particular type if the asset file is capable of representing a node
        definition of multiple source types.

        Returns a valid node if the asset is parsed successfully using one of
        the registered parser plugins.
        """
    def GetNodeFromSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath, metadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath] = ...) -> Node:
        """
        Parses the given C{sourceCode} string, constructs a NdrNode from it
        and adds it to the registry.


        The parser to be used is determined by the specified C{sourceType}.

        Nodes created from source code using this API can be looked up by the
        unique identifier and sourceType of the returned node.

        C{metadata} contains additional metadata needed for parsing and
        compiling the source code correctly. This metadata supplements the
        metadata available in C{sourceCode} and overrides it cases where there
        are key collisions.

        Returns a valid node if the given source code is parsed successfully
        using the parser plugins that is registered for the specified
        C{sourceType}.
        """
    def GetNodeIdentifiers(self, family: str | pxr.Ar.ResolvedPath = ..., filter: VersionFilter = ...) -> list[str]:
        '''
        Get the identifiers of all the nodes that the registry is aware of.


        This will not run the parsing plugins on the nodes that have been
        discovered, so this method is relatively quick. Optionally,
        a"family"name can be specified to only get the identifiers of nodes
        that belong to that family and a filter can be specified to get just
        the default version (the default) or all versions of the node.
        '''
    def GetNodeNames(self, family: str | pxr.Ar.ResolvedPath = ...) -> list[str]:
        '''
        Get the names of all the nodes that the registry is aware of.


        This will not run the parsing plugins on the nodes that have been
        discovered, so this method is relatively quick. Optionally,
        a"family"name can be specified to only get the names of nodes that
        belong to that family.
        '''
    def GetNodesByFamily(self, family: str | pxr.Ar.ResolvedPath = ..., filter: VersionFilter = ...) -> NodeList:
        """
        Get all nodes from the registry, optionally restricted to the nodes
        that fall under a specified family and/or the default version.


        Note that this will parse *all* nodes that the registry is aware of
        (unless a family is specified), so this may take some time to run the
        first time it is called.
        """
    def GetNodesByIdentifier(self, identifier: str | pxr.Ar.ResolvedPath) -> NodeList:
        """
        Get all nodes matching the specified identifier (multiple nodes of the
        same identifier, but different source types, may exist).


        If no nodes match the identifier, an empty vector is returned.
        """
    def GetNodesByName(self, name: str | pxr.Ar.ResolvedPath, filter: VersionFilter = ...) -> NodeList:
        """
        Get all nodes matching the specified name.


        Only nodes matching the specified name will be parsed. Optionally, a
        filter can be specified to get just the default version (the default)
        or all versions of the node. If no nodes match an empty vector is
        returned.
        """
    def GetSearchURIs(self) -> list[str]:
        """
        Get the locations where the registry is searching for nodes.


        Depending on which discovery plugins were used, this may include non-
        filesystem paths.
        """
    def SetExtraDiscoveryPlugins(self, arg2: list, /) -> None: ...
    def SetExtraParserPlugins(self, _pluginTypes: typing.Iterable[pxr.Tf.Type], /) -> None:
        """
        Allows the client to set any additional parser plugins that would
        otherwise NOT be found through the plugin system.


        Note that this method cannot be called after any nodes in the registry
        have been parsed (eg, through GetNode*()), otherwise an error will
        result.
        """

class Version(Boost.Python.instance):
    @overload
    def __init__(self) -> None:
        """
        Create an invalid version.
        """
    @overload
    def __init__(self, _major: int, _minor: int, /) -> None:
        """
        Create a version with the given major and minor numbers.


        Numbers must be non-negative, and at least one must be non-zero.  On
        failure generates an error and yields an invalid version.
        """
    @overload
    def __init__(self, _x: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Create a version from a string.


        On failure generates an error and yields an invalid version.
        """
    @overload
    def __init__(self, arg2: int, /) -> None: ...
    def GetAsDefault(self) -> Version:
        """
        Return an equal version marked as default.


        It's permitted to mark an invalid version as the default.
        """
    def GetMajor(self) -> int:
        """
        Return the major version number or zero for an invalid version.
        """
    def GetMinor(self) -> int:
        """
        Return the minor version number or zero for an invalid version.
        """
    def GetStringSuffix(self) -> str:
        """
        Return the version as a identifier suffix.
        """
    def IsDefault(self) -> bool:
        """
        Return true iff this version is marked as default.
        """
    def __bool__(self) -> bool:
        """
        Return true iff the version is valid.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class VersionFilter(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class _AnnotatedBool(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def message(self): ...

class _FilesystemDiscoveryPlugin(DiscoveryPlugin):
    class Context(DiscoveryPluginContext):
        def __init__(self) -> None: ...
        def __bool__(self) -> bool:
            """True if this object has not expired.  False otherwise."""
        def __eq__(self, other: object) -> bool:
            """Equality operator:  x == y"""
        def __lt__(self, other: object) -> bool:
            """Less than operator: x < y"""
        def __ne__(self, other: object) -> bool:
            """Non-equality operator: x != y"""
        @property
        def expired(self): ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    def DiscoverNodes(self, arg2: DiscoveryPluginContext, /) -> list: ...
    def GetSearchURIs(self) -> Any: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

def FsHelpersDiscoverFiles(searchPaths: typing.Iterable[str | pxr.Ar.ResolvedPath], allowedExtensions: typing.Iterable[str | pxr.Ar.ResolvedPath], followSymlinks: bool = ...) -> list:
    """
    Returns a vector of discovered URIs (as both the unresolved URI and
    the resolved URI) that are found while walking the given search paths.


    Each path in C{searchPaths} is walked recursively, optionally
    following symlinks if C{followSymlinks} is true, looking for files
    that match one of the provided C{allowedExtensions}. These
    files'unresolved and resolved URIs are returned in the result vector.

    This is an alternative to NdrFsHelpersDiscoverNodes for discovery
    plugins that want to search for files that are not meant to be
    returned by discovery themselves, but can be parsed to generate the
    discovery results.
    """
def FsHelpersDiscoverNodes(searchPaths: typing.Iterable[str | pxr.Ar.ResolvedPath], allowedExtensions: typing.Iterable[str | pxr.Ar.ResolvedPath], followSymlinks: bool = ..., context: DiscoveryPluginContext = ...) -> tuple[NodeDiscoveryResultVec, DiscoveryPluginContext]:
    """
    Returns a vector of discovery results that have been found while
    walking the given search paths.


    Each path in C{searchPaths} is walked recursively, optionally
    following symlinks if C{followSymlinks} is true, looking for files
    that match one of the provided C{allowedExtensions}. These files are
    represented in the discovery results that are returned.

    The identifier for each discovery result is the base name of the
    represented file with the extension removed. The C{parseIdentifierFn}
    is used to parse the family, name, and version from the identifier
    that will set in the file's discovery result. By default,
    NdrFsHelpersSplitShaderIdentifier is used to parse the identifier, but
    the family/name/version parsing behavior can be changed by passing a
    custom parseIdentifierFn. Any identifiers that cannot be parsed by
    whatever the parseIdentifierFn will be considered invalid and not
    added as a discovery result. Note that the version for every discovery
    result returned by this function will be naively marked as being
    default even if multiple versions with the same name are found.
    """
def FsHelpersSplitShaderIdentifier(identifier: str | pxr.Ar.ResolvedPath) -> tuple[str, str, Version]:
    """
    Given a shader's C{identifier} token, computes the corresponding
    NdrNode 's family name, implementation name and shader version (as
    NdrVersion).



       - C{family} is the prefix of C{identifier} up to and not including
         the first underscore.

       - C{version} is the suffix of C{identifier} comprised of one or two
         integers representing the major and minor version numbers.

       - C{name} is the string we get by joining *family* with everything
         that's in between *family* and *version* with an underscore.

    Returns true if C{identifier} is valid and was successfully split into
    the different components.

    The python version of this function returns a tuple containing
    (famiyName, implementationName, version).
    """
def _ValidateProperty(arg1: Node, arg2: Property, /) -> _AnnotatedBool: ...
