# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class GenerativeProcedural(pxr.UsdGeom.Boundable):
    '''
    Represents an abstract generative procedural prim which delivers its
    input parameters via properties (including relationships) within
    the"primvars:"namespace.


    It does not itself have any awareness or participation in the
    execution of the procedural but rather serves as a means of delivering
    a procedural\'s definition and input parameters.

    The value of its"proceduralSystem"property (either authored or
    provided by API schema fallback) indicates to which system the
    procedural definition is meaningful.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdProcTokens. So to set an attribute to the value"rightHanded",
    use UsdProcTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdProcGenerativeProcedural on UsdPrim C{prim}.


        Equivalent to UsdProcGenerativeProcedural::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdProcGenerativeProcedural on the prim held by
        C{schemaObj}.


        Should be preferred over UsdProcGenerativeProcedural
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    def CreateProceduralSystemAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetProceduralSystemAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> GenerativeProcedural:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> GenerativeProcedural:
        """
        Return a UsdProcGenerativeProcedural holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdProcGenerativeProcedural(stage->GetPrimAtPath(path));

        """
    def GetProceduralSystemAttr(self) -> pxr.Usd.Attribute:
        """
        The name or convention of the system responsible for evaluating the
        procedural.


        NOTE: A fallback value for this is typically set via an API schema.

        Declaration

        C{token proceduralSystem}

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
    GenerativeProcedural: ClassVar[str] = ...  # read-only
    proceduralSystem: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
