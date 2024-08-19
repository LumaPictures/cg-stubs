# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Ndr
import pxr.Sdf
import typing
from typing import Any, ClassVar

__MFB_FULL_PACKAGE_NAME: str

class NodeContext(Boost.Python.instance):
    Displacement: ClassVar[str] = ...  # read-only
    DisplayFilter: ClassVar[str] = ...  # read-only
    Light: ClassVar[str] = ...  # read-only
    LightFilter: ClassVar[str] = ...  # read-only
    Pattern: ClassVar[str] = ...  # read-only
    PixelFilter: ClassVar[str] = ...  # read-only
    SampleFilter: ClassVar[str] = ...  # read-only
    Surface: ClassVar[str] = ...  # read-only
    Volume: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class NodeMetadata(Boost.Python.instance):
    Category: ClassVar[str] = ...  # read-only
    Departments: ClassVar[str] = ...  # read-only
    Help: ClassVar[str] = ...  # read-only
    ImplementationName: ClassVar[str] = ...  # read-only
    Label: ClassVar[str] = ...  # read-only
    Pages: ClassVar[str] = ...  # read-only
    Primvars: ClassVar[str] = ...  # read-only
    Role: ClassVar[str] = ...  # read-only
    SdrDefinitionNameFallbackPrefix: ClassVar[str] = ...  # read-only
    SdrUsdEncodingVersion: ClassVar[str] = ...  # read-only
    Target: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class NodeRole(Boost.Python.instance):
    Field: ClassVar[str] = ...  # read-only
    Math: ClassVar[str] = ...  # read-only
    Primvar: ClassVar[str] = ...  # read-only
    Texture: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class PropertyMetadata(Boost.Python.instance):
    Colorspace: ClassVar[str] = ...  # read-only
    Connectable: ClassVar[str] = ...  # read-only
    DefaultInput: ClassVar[str] = ...  # read-only
    Help: ClassVar[str] = ...  # read-only
    Hints: ClassVar[str] = ...  # read-only
    ImplementationName: ClassVar[str] = ...  # read-only
    IsAssetIdentifier: ClassVar[str] = ...  # read-only
    IsDynamicArray: ClassVar[str] = ...  # read-only
    Label: ClassVar[str] = ...  # read-only
    Options: ClassVar[str] = ...  # read-only
    Page: ClassVar[str] = ...  # read-only
    RenderType: ClassVar[str] = ...  # read-only
    Role: ClassVar[str] = ...  # read-only
    SdrUsdDefinitionType: ClassVar[str] = ...  # read-only
    Tag: ClassVar[str] = ...  # read-only
    Target: ClassVar[str] = ...  # read-only
    ValidConnectionTypes: ClassVar[str] = ...  # read-only
    VstructConditionalExpr: ClassVar[str] = ...  # read-only
    VstructMemberName: ClassVar[str] = ...  # read-only
    VstructMemberOf: ClassVar[str] = ...  # read-only
    Widget: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class PropertyRole(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class PropertyTypes(Boost.Python.instance):
    Color: ClassVar[str] = ...  # read-only
    Color4: ClassVar[str] = ...  # read-only
    Float: ClassVar[str] = ...  # read-only
    Int: ClassVar[str] = ...  # read-only
    Matrix: ClassVar[str] = ...  # read-only
    Normal: ClassVar[str] = ...  # read-only
    Point: ClassVar[str] = ...  # read-only
    String: ClassVar[str] = ...  # read-only
    Struct: ClassVar[str] = ...  # read-only
    Terminal: ClassVar[str] = ...  # read-only
    Unknown: ClassVar[str] = ...  # read-only
    Vector: ClassVar[str] = ...  # read-only
    Vstruct: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Registry(pxr.Ndr.Registry):
    """
    The shading-specialized version of C{NdrRegistry}.
    """
    def __init__(self) -> None: ...
    def GetShaderNodeByIdentifier(self, identifier: str | pxr.Ar.ResolvedPath, typePriority: typing.Iterable[str | pxr.Ar.ResolvedPath] = ...) -> ShaderNode:
        """
        Exactly like C{NdrRegistry::GetNodeByIdentifier()} , but returns a
        C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.
        """
    def GetShaderNodeByIdentifierAndType(self, identifier: str | pxr.Ar.ResolvedPath, nodeType: str | pxr.Ar.ResolvedPath) -> ShaderNode:
        """
        Exactly like C{NdrRegistry::GetNodeByIdentifierAndType()} , but
        returns a C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.
        """
    def GetShaderNodeByName(self, name: str | pxr.Ar.ResolvedPath, typePriority: typing.Iterable[str | pxr.Ar.ResolvedPath] = ..., filter: pxr.Ndr.VersionFilter = ...) -> ShaderNode:
        """
        Exactly like C{NdrRegistry::GetNodeByName()} , but returns a
        C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.
        """
    def GetShaderNodeByNameAndType(self, name: str | pxr.Ar.ResolvedPath, nodeType: str | pxr.Ar.ResolvedPath, filter: pxr.Ndr.VersionFilter = ...) -> ShaderNode:
        """
        Exactly like C{NdrRegistry::GetNodeByNameAndType()} , but returns a
        C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.
        """
    def GetShaderNodeFromAsset(self, shaderAsset: pxr.Sdf.AssetPath | str, metadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath] = ..., subIdentifier: str | pxr.Ar.ResolvedPath = ..., sourceType: str | pxr.Ar.ResolvedPath = ...) -> ShaderNode:
        """
        Wrapper method for NdrRegistry::GetNodeFromAsset() .


        Returns a valid SdrShaderNode pointer upon success.
        """
    def GetShaderNodeFromSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath, metadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath] = ...) -> ShaderNode:
        """
        Wrapper method for NdrRegistry::GetNodeFromSourceCode() .


        Returns a valid SdrShaderNode pointer upon success.
        """
    def GetShaderNodesByFamily(self, family: str | pxr.Ar.ResolvedPath = ..., filter: pxr.Ndr.VersionFilter = ...) -> ShaderNodeList:
        """
        Exactly like C{NdrRegistry::GetNodesByFamily()} , but returns a vector
        of C{SdrShaderNode} pointers instead of a vector of C{NdrNode}
        pointers.
        """
    def GetShaderNodesByIdentifier(self, identifier: str | pxr.Ar.ResolvedPath) -> ShaderNodeList:
        """
        Exactly like C{NdrRegistry::GetNodesByIdentifier()} , but returns a
        vector of C{SdrShaderNode} pointers instead of a vector of C{NdrNode}
        pointers.
        """
    def GetShaderNodesByName(self, name: str | pxr.Ar.ResolvedPath, filter: pxr.Ndr.VersionFilter = ...) -> ShaderNodeList:
        """
        Exactly like C{NdrRegistry::GetNodesByName()} , but returns a vector
        of C{SdrShaderNode} pointers instead of a vector of C{NdrNode}
        pointers.
        """
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

class ShaderNode(pxr.Ndr.Node):
    """
    A specialized version of C{NdrNode} which holds shading information.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetAdditionalPrimvarProperties(self) -> list[str]:
        """
        The list of string input properties whose values provide the names of
        additional primvars consumed by this node.


        For example, this may return a token named C{varname}. This indicates
        that the client should query the value of a (presumed to be string-
        valued) input attribute named varname from its scene description to
        determine the name of a primvar the node will consume. See
        C{GetPrimvars()} for additional information.
        """
    def GetAllVstructNames(self) -> list[str]:
        """
        Gets all vstructs that are present in the shader.
        """
    def GetAssetIdentifierInputNames(self) -> list[str]:
        """
        Returns the list of all inputs that are tagged as asset identifier
        inputs.
        """
    def GetCategory(self) -> str:
        """
        The category assigned to this node, if any.


        Distinct from the family returned from C{GetFamily()} .
        """
    def GetDefaultInput(self) -> ShaderProperty:
        """
        Returns the first shader input that is tagged as the default input.


        A default input and its value can be used to acquire a fallback value
        for a node when the node is considered'disabled'or otherwise incapable
        of producing an output value.
        """
    def GetDepartments(self) -> list[str]:
        """
        The departments this node is associated with, if any.
        """
    def GetHelp(self) -> str:
        """
        The help message assigned to this node, if any.
        """
    def GetImplementationName(self) -> str:
        """
        Returns the implementation name of this node.


        The name of the node is how to refer to the node in shader networks.
        The label is how to present this node to users. The implementation
        name is the name of the function (or something) this node represents
        in the implementation. Any client using the implementation B{must}
        call this method to get the correct name; using C{getName()} is not
        correct.
        """
    def GetLabel(self) -> str:
        """
        The label assigned to this node, if any.


        Distinct from the name returned from C{GetName()} . In the context of
        a UI, the label value might be used as the display name for the node
        instead of the name.
        """
    def GetPages(self) -> list[str]:
        """
        Gets the pages on which the node's properties reside (an aggregate of
        the unique C{SdrShaderProperty::GetPage()} values for all of the
        node's properties).


        Nodes themselves do not reside on pages. In an example scenario,
        properties might be divided into two pages,'Simple'and'Advanced'.
        """
    def GetPrimvars(self) -> list[str]:
        """
        The list of primvars this node knows it requires / uses.


        For example, a shader node may require the'normals'primvar to function
        correctly. Additional, user specified primvars may have been authored
        on the node. These can be queried via
        C{GetAdditionalPrimvarProperties()} . Together, C{GetPrimvars()} and
        C{GetAdditionalPrimvarProperties()} , provide the complete list of
        primvar requirements for the node.
        """
    def GetPropertyNamesForPage(self, _pageName: str | pxr.Ar.ResolvedPath, /) -> list[str]:
        """
        Gets the names of the properties on a certain page (one that was
        returned by C{GetPages()} ).


        To get properties that are not assigned to a page, an empty string can
        be used for C{pageName}.
        """
    def GetRole(self) -> str:
        """
        Returns the role of this node.


        This is used to annotate the role that the shader node plays inside a
        shader network. We can tag certain shaders to indicate their role
        within a shading network. We currently tag primvar reading nodes,
        texture reading nodes and nodes that access volume fields (like
        extinction or scattering). This is done to identify resources used by
        a shading network.
        """
    def GetShaderInput(self, _inputName: str | pxr.Ar.ResolvedPath, /) -> ShaderProperty:
        """
        Get a shader input property by name.


        C{nullptr} is returned if an input with the given name does not exist.
        """
    def GetShaderOutput(self, _outputName: str | pxr.Ar.ResolvedPath, /) -> ShaderProperty:
        """
        Get a shader output property by name.


        C{nullptr} is returned if an output with the given name does not
        exist.
        """

class ShaderNodeList(Boost.Python.instance):
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

class ShaderProperty(pxr.Ndr.Property):
    """
    A specialized version of C{NdrProperty} which holds shading
    information.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetDefaultValueAsSdfType(self) -> Any:
        """
        Accessor for default value corresponding to the SdfValueTypeName
        returned by GetTypeAsSdfType.


        Note that this is different than GetDefaultValue which returns the
        default value associated with the SdrPropertyType and may differ from
        the SdfValueTypeName, example when sdrUsdDefinitionType metadata is
        specified for a sdr property.

        GetTypeAsSdfType
        """
    def GetHelp(self) -> str:
        """
        The help message assigned to this property, if any.
        """
    def GetHints(self) -> dict:
        '''
        Any UI"hints"that are associated with this property.


        "Hints"are simple key/value pairs.
        '''
    def GetImplementationName(self) -> str:
        """
        Returns the implementation name of this property.


        The name of the property is how to refer to the property in shader
        networks. The label is how to present this property to users. The
        implementation name is the name of the parameter this property
        represents in the implementation. Any client using the implementation
        B{must} call this method to get the correct name; using C{getName()}
        is not correct.
        """
    def GetLabel(self) -> str:
        """
        The label assigned to this property, if any.


        Distinct from the name returned from C{GetName()} . In the context of
        a UI, the label value might be used as the display name for the
        property instead of the name.
        """
    def GetOptions(self) -> list[tuple[str, str]]:
        """
        If the property has a set of valid values that are pre-determined,
        this will return the valid option names and corresponding string
        values (if the option was specified with a value).
        """
    def GetPage(self) -> str:
        '''
        The page (group), eg"Advanced", this property appears on, if any.


        Note that the page for a shader property can be nested, delimited
        by":", representing the hierarchy of sub-pages a property is defined
        in.
        '''
    def GetVStructConditionalExpr(self) -> str:
        """
        If this field is part of a vstruct, this is the conditional
        expression.
        """
    def GetVStructMemberName(self) -> str:
        """
        If this field is part of a vstruct, this is its name in the struct.
        """
    def GetVStructMemberOf(self) -> str:
        """
        If this field is part of a vstruct, this is the name of the struct.
        """
    def GetValidConnectionTypes(self) -> list[str]:
        """
        Gets the list of valid connection types for this property.


        This value comes from shader metadata, and may not be specified. The
        value from C{NdrProperty::GetType()} can be used as a fallback, or you
        can use the connectability test in C{CanConnectTo()} .
        """
    def GetWidget(self) -> str:
        '''
        The widget"hint"that indicates the widget that can best display the
        type of data contained in this property, if any.


        Examples of this value could include"number","slider", etc.
        '''
    def IsAssetIdentifier(self) -> bool:
        """
        Determines if the value held by this property is an asset identifier
        (eg, a file path); the logic for this is left up to the parser.


        Note: The type returned from C{GetTypeAsSdfType()} will be C{Asset} if
        this method returns C{true} (even though its true underlying data type
        is string).
        """
    def IsDefaultInput(self) -> bool:
        """
        Determines if the value held by this property is the default input for
        this node.
        """
    def IsVStruct(self) -> bool:
        """
        Returns true if the field is the head of a vstruct.
        """
    def IsVStructMember(self) -> bool:
        """
        Returns true if this field is part of a vstruct.
        """
