# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Sdf
import pxr.Tf
import pxr.Usd
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class GenerativeProceduralAPI(pxr.Usd.APISchemaBase):
    '''
    This API extends and configures the core UsdProcGenerativeProcedural
    schema defined within usdProc for use with hydra generative
    procedurals as defined within hdGp.


    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdHydraTokens. So to set an attribute to the value"rightHanded",
    use UsdHydraTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdHydraGenerativeProceduralAPI on UsdPrim C{prim}.


        Equivalent to UsdHydraGenerativeProceduralAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdHydraGenerativeProceduralAPI on the prim held by
        C{schemaObj}.


        Should be preferred over UsdHydraGenerativeProceduralAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> GenerativeProceduralAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"HydraGenerativeProceduralAPI"to
        the token-valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdHydraGenerativeProceduralAPI object is returned upon
        success. An invalid (or empty) UsdHydraGenerativeProceduralAPI object
        is returned upon failure. See UsdPrim::ApplyAPI() for conditions
        resulting in failure.

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
    def CreateProceduralSystemAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetProceduralSystemAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateProceduralTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetProceduralTypeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> GenerativeProceduralAPI:
        """
        Return a UsdHydraGenerativeProceduralAPI holding the prim adhering to
        this schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdHydraGenerativeProceduralAPI(stage->GetPrimAtPath(path));

        """
    def GetProceduralSystemAttr(self) -> pxr.Usd.Attribute:
        '''
        This value should correspond to a configured instance of
        HdGpGenerativeProceduralResolvingSceneIndex which will evaluate the
        procedural.


        The default value of"hydraGenerativeProcedural"matches the equivalent
        default of HdGpGenerativeProceduralResolvingSceneIndex. Multiple
        instances of the scene index can be used to determine where within a
        scene index chain a given procedural will be evaluated.

        Declaration

        C{token proceduralSystem ="hydraGenerativeProcedural"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        '''
    def GetProceduralTypeAttr(self) -> pxr.Usd.Attribute:
        """
        The registered name of a HdGpGenerativeProceduralPlugin to be
        executed.



        Declaration

        C{token primvars:hdGp:proceduralType}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
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
    HwPrimvar_1: ClassVar[str] = ...  # read-only
    HwPtexTexture_1: ClassVar[str] = ...  # read-only
    HwUvTexture_1: ClassVar[str] = ...  # read-only
    HydraGenerativeProceduralAPI: ClassVar[str] = ...  # read-only
    black: ClassVar[str] = ...  # read-only
    clamp: ClassVar[str] = ...  # read-only
    displayLookBxdf: ClassVar[str] = ...  # read-only
    faceIndex: ClassVar[str] = ...  # read-only
    faceOffset: ClassVar[str] = ...  # read-only
    frame: ClassVar[str] = ...  # read-only
    hydraGenerativeProcedural: ClassVar[str] = ...  # read-only
    infoFilename: ClassVar[str] = ...  # read-only
    infoVarname: ClassVar[str] = ...  # read-only
    linear: ClassVar[str] = ...  # read-only
    linearMipmapLinear: ClassVar[str] = ...  # read-only
    linearMipmapNearest: ClassVar[str] = ...  # read-only
    magFilter: ClassVar[str] = ...  # read-only
    minFilter: ClassVar[str] = ...  # read-only
    mirror: ClassVar[str] = ...  # read-only
    nearest: ClassVar[str] = ...  # read-only
    nearestMipmapLinear: ClassVar[str] = ...  # read-only
    nearestMipmapNearest: ClassVar[str] = ...  # read-only
    primvarsHdGpProceduralType: ClassVar[str] = ...  # read-only
    proceduralSystem: ClassVar[str] = ...  # read-only
    repeat: ClassVar[str] = ...  # read-only
    textureMemory: ClassVar[str] = ...  # read-only
    useMetadata: ClassVar[str] = ...  # read-only
    uv: ClassVar[str] = ...  # read-only
    wrapS: ClassVar[str] = ...  # read-only
    wrapT: ClassVar[str] = ...  # read-only
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
