# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Sdf
import pxr.Tf
import pxr.Usd
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class Backdrop(pxr.Usd.Typed):
    '''
    Provides a\'group-box\'for the purpose of node graph organization.


    Unlike containers, backdrops do not store the Shader nodes inside of
    them. Backdrops are an organizational tool that allows Shader nodes to
    be visually grouped together in a node-graph UI, but there is no
    direct relationship between a Shader node and a Backdrop.

    The guideline for a node-graph UI is that a Shader node is considered
    part of a Backdrop when the Backdrop is the smallest Backdrop a Shader
    node\'s bounding-box fits inside.

    Backdrop objects are contained inside a NodeGraph, similar to how
    Shader objects are contained inside a NodeGraph.

    Backdrops have no shading inputs or outputs that influence the
    rendered results of a NodeGraph. Therefore they can be safely ignored
    during import.

    Like Shaders and NodeGraphs, Backdrops subscribe to the
    NodeGraphNodeAPI to specify position and size.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdUITokens. So to set an attribute to the value"rightHanded", use
    UsdUITokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdUIBackdrop on UsdPrim C{prim}.


        Equivalent to UsdUIBackdrop::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdUIBackdrop on the prim held by C{schemaObj}.


        Should be preferred over UsdUIBackdrop (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateDescriptionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDescriptionAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Backdrop:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Backdrop:
        """
        Return a UsdUIBackdrop holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdUIBackdrop(stage->GetPrimAtPath(path));

        """
    def GetDescriptionAttr(self) -> pxr.Usd.Attribute:
        """
        The text label that is displayed on the backdrop in the node graph.


        This help-description explains what the nodes in a backdrop do.

        Declaration

        C{uniform token ui:description}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class NodeGraphNodeAPI(pxr.Usd.APISchemaBase):
    '''
    This api helps storing information about nodes in node graphs.


    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdUITokens. So to set an attribute to the value"rightHanded", use
    UsdUITokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdUINodeGraphNodeAPI on UsdPrim C{prim}.


        Equivalent to UsdUINodeGraphNodeAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdUINodeGraphNodeAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdUINodeGraphNodeAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> NodeGraphNodeAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"NodeGraphNodeAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdUINodeGraphNodeAPI object is returned upon success. An
        invalid (or empty) UsdUINodeGraphNodeAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult:
        """
        Returns true if this B{single-apply} API schema can be applied to the
        given C{prim}.


        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates C{whyNot} with the reason it can not be
        applied.

        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        """
    def CreateDisplayColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisplayColorAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExpansionStateAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExpansionStateAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateIconAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetIconAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePosAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPosAttr() , and also Create vs Get Property Methods for when to
        use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSizeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateStackingOrderAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetStackingOrderAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeGraphNodeAPI:
        """
        Return a UsdUINodeGraphNodeAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdUINodeGraphNodeAPI(stage->GetPrimAtPath(path));

        """
    def GetDisplayColorAttr(self) -> pxr.Usd.Attribute:
        """
        This hint defines what tint the node should have in the node graph.



        Declaration

        C{uniform color3f ui:nodegraph:node:displayColor}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Color3f

        Variability

        SdfVariabilityUniform
        """
    def GetExpansionStateAttr(self) -> pxr.Usd.Attribute:
        """
        The current expansionState of the node in the ui.


        'open'= fully expanded'closed'= fully collapsed'minimized'= should
        take the least space possible

        Declaration

        C{uniform token ui:nodegraph:node:expansionState}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        open, closed, minimized
        """
    def GetIconAttr(self) -> pxr.Usd.Attribute:
        """
        This points to an image that should be displayed on the node.


        It is intended to be useful for summary visual classification of
        nodes, rather than a thumbnail preview of the computed result of the
        node in some computational system.

        Declaration

        C{uniform asset ui:nodegraph:node:icon}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset

        Variability

        SdfVariabilityUniform
        """
    def GetPosAttr(self) -> pxr.Usd.Attribute:
        """
        Declared relative position to the parent in a node graph.


        X is the horizontal position. Y is the vertical position. Higher
        numbers correspond to lower positions (coordinates are Qt style, not
        cartesian).

        These positions are not explicitly meant in pixel space, but rather
        assume that the size of a node is approximately 1.0x1.0. Where size-x
        is the node width and size-y height of the node. Depending on graph UI
        implementation, the size of a node may vary in each direction.

        Example: If a node's width is 300 and it is position is at 1000, we
        store for x-position: 1000 * (1.0/300)

        Declaration

        C{uniform float2 ui:nodegraph:node:pos}

        C++ Type

        GfVec2f

        Usd Type

        SdfValueTypeNames->Float2

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSizeAttr(self) -> pxr.Usd.Attribute:
        """
        Optional size hint for a node in a node graph.


        X is the width. Y is the height.

        This value is optional, because node size is often determined based on
        the number of in- and outputs of a node.

        Declaration

        C{uniform float2 ui:nodegraph:node:size}

        C++ Type

        GfVec2f

        Usd Type

        SdfValueTypeNames->Float2

        Variability

        SdfVariabilityUniform
        """
    def GetStackingOrderAttr(self) -> pxr.Usd.Attribute:
        """
        This optional value is a useful hint when an application cares about
        the visibility of a node and whether each node overlaps another.


        Nodes with lower stacking order values are meant to be drawn below
        higher ones. Negative values are meant as background. Positive values
        are meant as foreground. Undefined values should be treated as 0.

        There are no set limits in these values.

        Declaration

        C{uniform int ui:nodegraph:node:stackingOrder}

        C++ Type

        int

        Usd Type

        SdfValueTypeNames->Int

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class SceneGraphPrimAPI(pxr.Usd.APISchemaBase):
    '''
    Utility schema for display properties of a prim.


    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdUITokens. So to set an attribute to the value"rightHanded", use
    UsdUITokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdUISceneGraphPrimAPI on UsdPrim C{prim}.


        Equivalent to UsdUISceneGraphPrimAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdUISceneGraphPrimAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdUISceneGraphPrimAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> SceneGraphPrimAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"SceneGraphPrimAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdUISceneGraphPrimAPI object is returned upon success. An
        invalid (or empty) UsdUISceneGraphPrimAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult:
        """
        Returns true if this B{single-apply} API schema can be applied to the
        given C{prim}.


        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates C{whyNot} with the reason it can not be
        applied.

        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        """
    def CreateDisplayGroupAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisplayGroupAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDisplayNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisplayNameAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SceneGraphPrimAPI:
        """
        Return a UsdUISceneGraphPrimAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdUISceneGraphPrimAPI(stage->GetPrimAtPath(path));

        """
    def GetDisplayGroupAttr(self) -> pxr.Usd.Attribute:
        """
        When publishing a nodegraph or a material, it can be useful to provide
        an optional display group, for organizational purposes and
        readability.


        This is because often the usd shading hierarchy is rather flat while
        we want to display it in organized groups.

        Declaration

        C{uniform token ui:displayGroup}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        """
    def GetDisplayNameAttr(self) -> pxr.Usd.Attribute:
        """
        When publishing a nodegraph or a material, it can be useful to provide
        an optional display name, for readability.



        Declaration

        C{uniform token ui:displayName}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    Backdrop: ClassVar[str] = ...  # read-only
    NodeGraphNodeAPI: ClassVar[str] = ...  # read-only
    SceneGraphPrimAPI: ClassVar[str] = ...  # read-only
    closed: ClassVar[str] = ...  # read-only
    minimized: ClassVar[str] = ...  # read-only
    open: ClassVar[str] = ...  # read-only
    uiDescription: ClassVar[str] = ...  # read-only
    uiDisplayGroup: ClassVar[str] = ...  # read-only
    uiDisplayName: ClassVar[str] = ...  # read-only
    uiNodegraphNodeDisplayColor: ClassVar[str] = ...  # read-only
    uiNodegraphNodeExpansionState: ClassVar[str] = ...  # read-only
    uiNodegraphNodeIcon: ClassVar[str] = ...  # read-only
    uiNodegraphNodePos: ClassVar[str] = ...  # read-only
    uiNodegraphNodeSize: ClassVar[str] = ...  # read-only
    uiNodegraphNodeStackingOrder: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...
