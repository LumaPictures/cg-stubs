# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Gf
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdShade
import typing
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class BoundableLightBase(pxr.UsdGeom.Boundable):
    """
    Base class for intrinsic lights that are boundable.


    The primary purpose of this class is to provide a direct API to the
    functions provided by LightAPI for concrete derived light types.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxBoundableLightBase on UsdPrim C{prim}.


        Equivalent to UsdLuxBoundableLightBase::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxBoundableLightBase on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxBoundableLightBase
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    def CreateColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateColorAttr() .
        """
    def CreateColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateColorTemperatureAttr() .
        """
    def CreateDiffuseAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateDiffuseAttr() .
        """
    def CreateEnableColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateEnableColorTemperatureAttr() .
        """
    def CreateExposureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateExposureAttr() .
        """
    def CreateFiltersRel(self) -> pxr.Usd.Relationship:
        """
        See UsdLuxLightAPI::CreateFiltersRel() .
        """
    def CreateIntensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateIntensityAttr() .
        """
    def CreateNormalizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateNormalizeAttr() .
        """
    def CreateSpecularAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateSpecularAttr() .
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BoundableLightBase:
        """
        Return a UsdLuxBoundableLightBase holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxBoundableLightBase(stage->GetPrimAtPath(path));

        """
    def GetColorAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetColorAttr() .
        """
    def GetColorTemperatureAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetColorTemperatureAttr() .
        """
    def GetDiffuseAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetDiffuseAttr() .
        """
    def GetEnableColorTemperatureAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetEnableColorTemperatureAttr() .
        """
    def GetExposureAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetExposureAttr() .
        """
    def GetFiltersRel(self) -> pxr.Usd.Relationship:
        """
        See UsdLuxLightAPI::GetFiltersRel() .
        """
    def GetIntensityAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetIntensityAttr() .
        """
    def GetNormalizeAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetNormalizeAttr() .
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSpecularAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetSpecularAttr() .
        """
    def LightAPI(self) -> LightAPI:
        """
        Contructs and returns a UsdLuxLightAPI object for this light.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class CylinderLight(BoundableLightBase):
    """
    Light emitted outward from a cylinder.


    The cylinder is centered at the origin and has its major axis on the X
    axis. The cylinder does not emit light from the flat end-caps.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxCylinderLight on UsdPrim C{prim}.


        Equivalent to UsdLuxCylinderLight::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxCylinderLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxCylinderLight (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateLengthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLengthAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTreatAsLineAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTreatAsLineAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CylinderLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CylinderLight:
        """
        Return a UsdLuxCylinderLight holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxCylinderLight(stage->GetPrimAtPath(path));

        """
    def GetLengthAttr(self) -> pxr.Usd.Attribute:
        """
        Length of the cylinder, in the local X axis.



        Declaration

        C{float inputs:length = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        Radius of the cylinder.



        Declaration

        C{float inputs:radius = 0.5}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTreatAsLineAttr(self) -> pxr.Usd.Attribute:
        """
        A hint that this light can be treated as a'line'light (effectively, a
        zero-radius cylinder) by renderers that benefit from non-area
        lighting.


        Renderers that only support area lights can disregard this.

        Declaration

        C{bool treatAsLine = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class DiskLight(BoundableLightBase):
    """
    Light emitted from one side of a circular disk.


    The disk is centered in the XY plane and emits light along the -Z
    axis.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxDiskLight on UsdPrim C{prim}.


        Equivalent to UsdLuxDiskLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxDiskLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxDiskLight (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DiskLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DiskLight:
        """
        Return a UsdLuxDiskLight holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxDiskLight(stage->GetPrimAtPath(path));

        """
    def GetRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        Radius of the disk.



        Declaration

        C{float inputs:radius = 0.5}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
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

class DistantLight(NonboundableLightBase):
    """
    Light emitted from a distant source along the -Z axis.


    Also known as a directional light.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxDistantLight on UsdPrim C{prim}.


        Equivalent to UsdLuxDistantLight::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxDistantLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxDistantLight (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateAngleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAngleAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DistantLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DistantLight:
        """
        Return a UsdLuxDistantLight holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxDistantLight(stage->GetPrimAtPath(path));

        """
    def GetAngleAttr(self) -> pxr.Usd.Attribute:
        """
        Angular size of the light in degrees.


        As an example, the Sun is approximately 0.53 degrees as seen from
        Earth. Higher values broaden the light and therefore soften shadow
        edges.

        Declaration

        C{float inputs:angle = 0.53}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
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

class DomeLight(NonboundableLightBase):
    '''
    Light emitted inward from a distant external environment, such as a
    sky or IBL light probe.


    In this version of the dome light, the dome\'s default orientation is
    such that its top pole is aligned with the world\'s +Y axis. This
    adheres to the OpenEXR specification for latlong environment maps.
    From the OpenEXR documentation:

    Latitude-Longitude Map:

    The environment is projected onto the image using polar coordinates
    (latitude and longitude). A pixel\'s x coordinate corresponds to its
    longitude, and the y coordinate corresponds to its latitude. Pixel
    (dataWindow.min.x, dataWindow.min.y) has latitude +pi/2 and longitude
    +pi; pixel (dataWindow.max.x, dataWindow.max.y) has latitude -pi/2 and
    longitude -pi.

    In 3D space, latitudes -pi/2 and +pi/2 correspond to the negative and
    positive y direction. Latitude 0, longitude 0 points into positive z
    direction; and latitude 0, longitude pi/2 points into positive x
    direction.

    The size of the data window should be 2*N by N pixels (width by
    height),

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxDomeLight on UsdPrim C{prim}.


        Equivalent to UsdLuxDomeLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxDomeLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxDomeLight (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateGuideRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetGuideRadiusAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePortalsRel(self) -> pxr.Usd.Relationship:
        """
        See GetPortalsRel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        """
    def CreateTextureFileAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTextureFileAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTextureFormatAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTextureFormatAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DomeLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DomeLight:
        """
        Return a UsdLuxDomeLight holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxDomeLight(stage->GetPrimAtPath(path));

        """
    def GetGuideRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of guide geometry to use to visualize the dome light.


        The default is 1 km for scenes whose metersPerUnit is the USD default
        of 0.01 (i.e., 1 world unit is 1 cm).

        Declaration

        C{float guideRadius = 100000}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetPortalsRel(self) -> pxr.Usd.Relationship:
        """
        Optional portals to guide light sampling.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTextureFileAttr(self) -> pxr.Usd.Attribute:
        """
        A color texture to use on the dome, such as an HDR (high dynamic
        range) texture intended for IBL (image based lighting).



        Declaration

        C{asset inputs:texture:file}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetTextureFormatAttr(self) -> pxr.Usd.Attribute:
        '''
        Specifies the parameterization of the color map file.


        Valid values are:
           - automatic: Tries to determine the layout from the file itself.
             For example, Renderman texture files embed an explicit
             parameterization.

           - latlong: Latitude as X, longitude as Y.

           - mirroredBall: An image of the environment reflected in a sphere,
             using an implicitly orthogonal projection.

           - angular: Similar to mirroredBall but the radial dimension is
             mapped linearly to the angle, providing better sampling at the edges.

           - cubeMapVerticalCross: A cube map with faces laid out as a
             vertical cross.

        Declaration

        C{token inputs:texture:format ="automatic"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        automatic, latlong, mirroredBall, angular, cubeMapVerticalCross
        '''
    def OrientToStageUpAxis(self) -> None:
        """
        Adds a transformation op, if neeeded, to orient the dome to align with
        the stage's up axis.


        Uses UsdLuxTokens->orientToStageUpAxis as the op suffix. If an op with
        this suffix already exists, this method assumes it is already applying
        the proper correction and does nothing further. If no op is required
        to match the stage's up axis, no op will be created.

        UsdGeomXformOp

        UsdGeomGetStageUpAxis
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class DomeLight_1(NonboundableLightBase):
    '''
    Light emitted inward from a distant external environment, such as a
    sky or IBL light probe.


    In this version of the dome light, the dome\'s default orientation is
    determined by its *poleAxis* property. The fallback value,"scene",
    means that the dome starts with its top pole aligned with the stage\'s
    up axis.

    Note that the rotation necessary to align the dome light with its
    *poleAxis* is intended to be applied by a renderer to only the dome
    itself, and *not* to inherit down to any USD namespace children of the
    dome light prim.

    If *poleAxis* is set to"Y"or"scene"and the stage\'s up axis is"Y", the
    dome\'s default orientation will adhere to the OpenEXR specification
    for latlong environment maps. From the OpenEXR documentation:

    Latitude-Longitude Map:

    The environment is projected onto the image using polar coordinates
    (latitude and longitude). A pixel\'s x coordinate corresponds to its
    longitude, and the y coordinate corresponds to its latitude. Pixel
    (dataWindow.min.x, dataWindow.min.y) has latitude +pi/2 and longitude
    +pi; pixel (dataWindow.max.x, dataWindow.max.y) has latitude -pi/2 and
    longitude -pi.

    In 3D space, latitudes -pi/2 and +pi/2 correspond to the negative and
    positive y direction. Latitude 0, longitude 0 points into positive z
    direction; and latitude 0, longitude pi/2 points into positive x
    direction.

    The size of the data window should be 2*N by N pixels (width by
    height),

    If *poleAxis* is set to"Z"or"scene"and the stage\'s up axis is"Z",
    latitudes -pi/2 and +pi/2 will instead correspond to the negative and
    positive Z direction, and latitude 0, longitude 0 will instead point
    into the negative Y direction in 3D space.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxDomeLight_1 on UsdPrim C{prim}.


        Equivalent to UsdLuxDomeLight_1::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxDomeLight_1 on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxDomeLight_1 (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateGuideRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetGuideRadiusAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePoleAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPoleAxisAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePortalsRel(self) -> pxr.Usd.Relationship:
        """
        See GetPortalsRel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        """
    def CreateTextureFileAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTextureFileAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTextureFormatAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTextureFormatAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DomeLight_1:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DomeLight_1:
        """
        Return a UsdLuxDomeLight_1 holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxDomeLight_1(stage->GetPrimAtPath(path));

        """
    def GetGuideRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of guide geometry to use to visualize the dome light.


        The default is 1 km for scenes whose metersPerUnit is the USD default
        of 0.01 (i.e., 1 world unit is 1 cm).

        Declaration

        C{float guideRadius = 100000}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetPoleAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        A token which indicates the starting alignment of the dome light\'s top
        pole.


        This alignment is for the dome itself and is *not* inherited by the
        namespace children of the dome. Valid values are:
           - scene: The dome light\'s top pole is aligned with the stage\'s up
             axis.

           - Y: The dome light\'s top pole is aligned with the +Y axis.

           - Z: The dome light\'s top pole is aligned with the +Z axis.

        Declaration

        C{uniform token poleAxis ="scene"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        scene, Y, Z
        '''
    def GetPortalsRel(self) -> pxr.Usd.Relationship:
        """
        Optional portals to guide light sampling.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTextureFileAttr(self) -> pxr.Usd.Attribute:
        """
        A color texture to use on the dome, such as an HDR (high dynamic
        range) texture intended for IBL (image based lighting).



        Declaration

        C{asset inputs:texture:file}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetTextureFormatAttr(self) -> pxr.Usd.Attribute:
        '''
        Specifies the parameterization of the color map file.


        Valid values are:
           - automatic: Tries to determine the layout from the file itself.
             For example, Renderman texture files embed an explicit
             parameterization.

           - latlong: Latitude as X, longitude as Y.

           - mirroredBall: An image of the environment reflected in a sphere,
             using an implicitly orthogonal projection.

           - angular: Similar to mirroredBall but the radial dimension is
             mapped linearly to the angle, providing better sampling at the edges.

           - cubeMapVerticalCross: A cube map with faces laid out as a
             vertical cross.

        Declaration

        C{token inputs:texture:format ="automatic"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        automatic, latlong, mirroredBall, angular, cubeMapVerticalCross
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class GeometryLight(NonboundableLightBase):
    """
    Deprecated

    Light emitted outward from a geometric prim (UsdGeomGprim), which is
    typically a mesh.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxGeometryLight on UsdPrim C{prim}.


        Equivalent to UsdLuxGeometryLight::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxGeometryLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxGeometryLight (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateGeometryRel(self) -> pxr.Usd.Relationship:
        """
        See GetGeometryRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> GeometryLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> GeometryLight:
        """
        Return a UsdLuxGeometryLight holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxGeometryLight(stage->GetPrimAtPath(path));

        """
    def GetGeometryRel(self) -> pxr.Usd.Relationship:
        """
        Relationship to the geometry to use as the light source.
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

class LightAPI(pxr.Usd.APISchemaBase):
    '''
    API schema that imparts the quality of being a light onto a prim.


    A light is any prim that has this schema applied to it. This is true
    regardless of whether LightAPI is included as a built-in API of the
    prim type (e.g. RectLight or DistantLight) or is applied directly to a
    Gprim that should be treated as a light.

    B{Linking}

    Lights can be linked to geometry. Linking controls which geometry a
    light illuminates, and which geometry casts shadows from the light.

    Linking is specified as collections (UsdCollectionAPI) which can be
    accessed via GetLightLinkCollection() and GetShadowLinkCollection().
    Note that these collections have their includeRoot set to true, so
    that lights will illuminate and cast shadows from all objects by
    default. To illuminate only a specific set of objects, there are two
    options. One option is to modify the collection paths to explicitly
    exclude everything else, assuming it is known; the other option is to
    set includeRoot to false and explicitly include the desired objects.
    These are complementary approaches that may each be preferable
    depending on the scenario and how to best express the intent of the
    light setup.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, connectable: pxr.UsdShade.ConnectableAPI) -> None:
        """
        Constructor that takes a ConnectableAPI object.


        Allow implicit conversion of a UsdShadeConnectableAPI to
        UsdLuxLightAPI
        """
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxLightAPI on UsdPrim C{prim}.


        Equivalent to UsdLuxLightAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxLightAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxLightAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> LightAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"LightAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdLuxLightAPI object is returned upon success. An invalid (or
        empty) UsdLuxLightAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def ConnectableAPI(self) -> pxr.UsdShade.ConnectableAPI:
        """
        Contructs and returns a UsdShadeConnectableAPI object with this light.


        Note that most tasks can be accomplished without explicitly
        constructing a UsdShadeConnectable API, since connection-related API
        such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
        and UsdLuxLightAPI will auto-convert to a UsdShadeConnectableAPI when
        passed to functions that want to act generically on a connectable
        UsdShadeConnectableAPI object.
        """
    def CreateColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetColorAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetColorTemperatureAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDiffuseAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDiffuseAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateEnableColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetEnableColorTemperatureAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExposureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExposureAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFiltersRel(self) -> pxr.Usd.Relationship:
        """
        See GetFiltersRel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        """
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Input:
        '''
        Create an input which can either have a value or can be connected.


        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on lights are connectable.
        '''
    def CreateIntensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetIntensityAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateMaterialSyncModeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMaterialSyncModeAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateNormalizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetNormalizeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Output:
        '''
        Create an output which can either have a value or can be connected.


        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a light cannot be connected, as
        their value is assumed to be computed externally.
        '''
    def CreateShaderIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShaderIdAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShaderIdAttrForRenderContext(self, renderContext: str | pxr.Ar.ResolvedPath, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        Creates the shader ID attribute for the given C{renderContext}.


        See GetShaderIdAttrForRenderContext() , and also Create vs Get
        Property Methods for when to use Get vs Create. If specified, author
        C{defaultValue} as the attribute's default, sparsely (when it makes
        sense to do so) if C{writeSparsely} is C{true} - the default for
        C{writeSparsely} is C{false}.
        """
    def CreateSpecularAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSpecularAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LightAPI:
        """
        Return a UsdLuxLightAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxLightAPI(stage->GetPrimAtPath(path));

        """
    def GetColorAttr(self) -> pxr.Usd.Attribute:
        """
        The color of emitted light, in energy-linear terms.



        Declaration

        C{color3f inputs:color = (1, 1, 1)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Color3f
        """
    def GetColorTemperatureAttr(self) -> pxr.Usd.Attribute:
        """
        Color temperature, in degrees Kelvin, representing the white point.


        The default is a common white point, D65. Lower values are warmer and
        higher values are cooler. The valid range is from 1000 to 10000. Only
        takes effect when enableColorTemperature is set to true. When active,
        the computed result multiplies against the color attribute. See
        UsdLuxBlackbodyTemperatureAsRgb() .

        Declaration

        C{float inputs:colorTemperature = 6500}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetDiffuseAttr(self) -> pxr.Usd.Attribute:
        """
        A multiplier for the effect of this light on the diffuse response of
        materials.


        This is a non-physical control.

        Declaration

        C{float inputs:diffuse = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetEnableColorTemperatureAttr(self) -> pxr.Usd.Attribute:
        """
        Enables using colorTemperature.



        Declaration

        C{bool inputs:enableColorTemperature = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    def GetExposureAttr(self) -> pxr.Usd.Attribute:
        """
        Scales the power of the light exponentially as a power of 2 (similar
        to an F-stop control over exposure).


        The result is multiplied against the intensity.

        Declaration

        C{float inputs:exposure = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetFiltersRel(self) -> pxr.Usd.Relationship:
        """
        Relationship to the light filters that apply to this light.
        """
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Input:
        """
        Return the requested input if it exists.
        """
    def GetInputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Input]:
        '''
        Inputs are represented by attributes in the"inputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    def GetIntensityAttr(self) -> pxr.Usd.Attribute:
        """
        Scales the power of the light linearly.



        Declaration

        C{float inputs:intensity = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetLightLinkCollectionAPI(self) -> pxr.Usd.CollectionAPI:
        """
        Return the UsdCollectionAPI interface used for examining and modifying
        the light-linking of this light.


        Light-linking controls which geometry this light illuminates.
        """
    def GetMaterialSyncModeAttr(self) -> pxr.Usd.Attribute:
        '''
        For a LightAPI applied to geometry that has a bound Material, which is
        entirely or partly emissive, this specifies the relationship of the
        Material response to the lighting response.


        Valid values are:
           - materialGlowTintsLight: All primary and secondary rays see the
             emissive/glow response as dictated by the bound Material while the
             base color seen by light rays (which is then modulated by all of the
             other LightAPI controls) is the multiplication of the color feeding
             the emission/glow input of the Material (i.e. its surface or volume
             shader) with the scalar or pattern input to *inputs:color*. This
             allows the light\'s color to tint the geometry\'s glow color while
             preserving access to intensity and other light controls as ways to
             further modulate the illumination.

           - independent: All primary and secondary rays see the emissive/glow
             response as dictated by the bound Material, while the base color seen
             by light rays is determined solely by *inputs:color*. Note that for
             partially emissive geometry (in which some parts are reflective rather
             than emissive), a suitable pattern must be connected to the light\'s
             color input, or else the light will radiate uniformly from the
             geometry.

           - noMaterialResponse: The geometry behaves as if there is no
             Material bound at all, i.e. there is no diffuse, specular, or
             transmissive response. The base color of light rays is entirely
             controlled by the *inputs:color*. This is the standard mode
             for"canonical"lights in UsdLux and indicates to renderers that a
             Material will either never be bound or can always be ignored.

        Declaration

        C{uniform token light:materialSyncMode ="noMaterialResponse"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        materialGlowTintsLight, independent, noMaterialResponse
        '''
    def GetNormalizeAttr(self) -> pxr.Usd.Attribute:
        """
        Normalizes power by the surface area of the light.


        This makes it easier to independently adjust the power and shape of
        the light, by causing the power to not vary with the area or angular
        size of the light.

        Declaration

        C{bool inputs:normalize = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Output:
        """
        Return the requested output if it exists.
        """
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Output]:
        '''
        Outputs are represented by attributes in the"outputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetShaderId(self, renderContexts: list[str] | list[pxr.Ar.ResolvedPath]) -> str:
        """
        Return the light's shader ID for the given list of available
        C{renderContexts}.


        The shader ID returned by this function is the identifier to use when
        looking up the shader definition for this light in the shader
        registry.

        The render contexts are expected to be listed in priority order, so
        for each render context provided, this will try to find the shader ID
        attribute specific to that render context (see
        GetShaderIdAttrForRenderContext() ) and will return the value of the
        first one found that has a non-empty value. If no shader ID value can
        be found for any of the given render contexts or C{renderContexts} is
        empty, then this will return the value of the default shader ID
        attribute (see GetShaderIdAttr() ).
        """
    def GetShaderIdAttr(self) -> pxr.Usd.Attribute:
        '''
        Default ID for the light\'s shader.


        This defines the shader ID for this light when a render context
        specific shader ID is not available.

        The default shaderId for the intrinsic UsdLux lights (RectLight,
        DistantLight, etc.) are set to default to the light\'s type name. For
        each intrinsic UsdLux light, we will always register an SdrShaderNode
        in the SdrRegistry, with the identifier matching the type name and the
        source type"USD", that corresponds to the light\'s inputs.

        GetShaderId

        GetShaderIdAttrForRenderContext

        SdrRegistry::GetShaderNodeByIdentifier

        SdrRegistry::GetShaderNodeByIdentifierAndType

        Declaration

        C{uniform token light:shaderId =""}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        '''
    def GetShaderIdAttrForRenderContext(self, renderContext: str | pxr.Ar.ResolvedPath) -> pxr.Usd.Attribute:
        '''
        Returns the shader ID attribute for the given C{renderContext}.


        If C{renderContext} is non-empty, this will try to return an attribute
        named *light:shaderId* with the namespace prefix C{renderContext}. For
        example, if the passed in render context is"ri"then the attribute
        returned by this function would have the following signature:

        Declaration

        C{token ri:light:shaderId}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        If the render context is empty, this will return the default shader ID
        attribute as returned by GetShaderIdAttr() .
        '''
    def GetShadowLinkCollectionAPI(self) -> pxr.Usd.CollectionAPI:
        """
        Return the UsdCollectionAPI interface used for examining and modifying
        the shadow-linking of this light.


        Shadow-linking controls which geometry casts shadows from this light.
        """
    def GetSpecularAttr(self) -> pxr.Usd.Attribute:
        """
        A multiplier for the effect of this light on the specular response of
        materials.


        This is a non-physical control.

        Declaration

        C{float inputs:specular = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class LightFilter(pxr.UsdGeom.Xformable):
    '''
    A light filter modifies the effect of a light.


    Lights refer to filters via relationships so that filters may be
    shared.

    B{Linking}

    Filters can be linked to geometry. Linking controls which geometry a
    light-filter affects, when considering the light filters attached to a
    light illuminating the geometry.

    Linking is specified as a collection (UsdCollectionAPI) which can be
    accessed via GetFilterLinkCollection().

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, connectable: pxr.UsdShade.ConnectableAPI) -> None:
        """
        Constructor that takes a ConnectableAPI object.


        Allow implicit conversion of UsdShadeConnectableAPI to
        UsdLuxLightFilter.
        """
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxLightFilter on UsdPrim C{prim}.


        Equivalent to UsdLuxLightFilter::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxLightFilter on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxLightFilter (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def ConnectableAPI(self) -> pxr.UsdShade.ConnectableAPI:
        """
        Contructs and returns a UsdShadeConnectableAPI object with this light
        filter.


        Note that most tasks can be accomplished without explicitly
        constructing a UsdShadeConnectable API, since connection-related API
        such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
        and UsdLuxLightFilter will auto-convert to a UsdShadeConnectableAPI
        when passed to functions that want to act generically on a connectable
        UsdShadeConnectableAPI object.
        """
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Input:
        '''
        Create an input which can either have a value or can be connected.


        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on light filters are connectable.
        '''
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Output:
        '''
        Create an output which can either have a value or can be connected.


        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a light filter cannot be connected,
        as their value is assumed to be computed externally.
        '''
    def CreateShaderIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShaderIdAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShaderIdAttrForRenderContext(self, renderContext: str | pxr.Ar.ResolvedPath, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        Creates the shader ID attribute for the given C{renderContext}.


        See GetShaderIdAttrForRenderContext() , and also Create vs Get
        Property Methods for when to use Get vs Create. If specified, author
        C{defaultValue} as the attribute's default, sparsely (when it makes
        sense to do so) if C{writeSparsely} is C{true} - the default for
        C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LightFilter:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LightFilter:
        """
        Return a UsdLuxLightFilter holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxLightFilter(stage->GetPrimAtPath(path));

        """
    def GetFilterLinkCollectionAPI(self) -> pxr.Usd.CollectionAPI:
        """
        Return the UsdCollectionAPI interface used for examining and modifying
        the filter-linking of this light filter.


        Linking controls which geometry this light filter affects.
        """
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Input:
        """
        Return the requested input if it exists.
        """
    def GetInputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Input]:
        '''
        Inputs are represented by attributes in the"inputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Output:
        """
        Return the requested output if it exists.
        """
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Output]:
        '''
        Outputs are represented by attributes in the"outputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetShaderId(self, renderContexts: list[str] | list[pxr.Ar.ResolvedPath]) -> str:
        """
        Return the light filter's shader ID for the given list of available
        C{renderContexts}.


        The shader ID returned by this function is the identifier to use when
        looking up the shader definition for this light filter in the shader
        registry.

        The render contexts are expected to be listed in priority order, so
        for each render context provided, this will try to find the shader ID
        attribute specific to that render context (see
        GetShaderIdAttrForRenderContext() ) and will return the value of the
        first one found that has a non-empty value. If no shader ID value can
        be found for any of the given render contexts or C{renderContexts} is
        empty, then this will return the value of the default shader ID
        attribute (see GetShaderIdAttr() ).
        """
    def GetShaderIdAttr(self) -> pxr.Usd.Attribute:
        '''
        Default ID for the light filter\'s shader.


        This defines the shader ID for this light filter when a render context
        specific shader ID is not available.

        GetShaderId

        GetShaderIdAttrForRenderContext

        SdrRegistry::GetShaderNodeByIdentifier

        SdrRegistry::GetShaderNodeByIdentifierAndType

        Declaration

        C{uniform token lightFilter:shaderId =""}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        '''
    def GetShaderIdAttrForRenderContext(self, renderContext: str | pxr.Ar.ResolvedPath) -> pxr.Usd.Attribute:
        '''
        Returns the shader ID attribute for the given C{renderContext}.


        If C{renderContext} is non-empty, this will try to return an attribute
        named *lightFilter:shaderId* with the namespace prefix
        C{renderContext}. For example, if the passed in render context
        is"ri"then the attribute returned by this function would have the
        following signature:

        Declaration

        C{token ri:lightFilter:shaderId}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        If the render context is empty, this will return the default shader ID
        attribute as returned by GetShaderIdAttr() .
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class LightListAPI(pxr.Usd.APISchemaBase):
    '''
    API schema to support discovery and publishing of lights in a scene.


    Discovering Lights via Traversal
    ================================

    To motivate this API, consider what is required to discover all lights
    in a scene. We must load all payloads and traverse all prims: ::

      01  // Load everything on the stage so we can find all lights,
      02  // including those inside payloads
      03  stage->Load();
      04  
      05  // Traverse all prims, checking if they have an applied UsdLuxLightAPI
      06  // (Note: ignoring instancing and a few other things for simplicity)
      07  SdfPathVector lights;
      08  for (UsdPrim prim: stage->Traverse()) {
      09      if (prim.HasAPI<UsdLuxLightAPI>()) {
      10          lights.push_back(i->GetPath());
      11      }
      12  }

    This traversal  suitably elaborated to handle certain details  is the
    first and simplest thing UsdLuxLightListAPI provides.
    UsdLuxLightListAPI::ComputeLightList() performs this traversal and
    returns all lights in the scene: ::

      01  UsdLuxLightListAPI listAPI(stage->GetPseudoRoot());
      02  SdfPathVector lights = listAPI.ComputeLightList();

    Publishing a Cached Light List
    ==============================

    Consider a USD client that needs to quickly discover lights but wants
    to defer loading payloads and traversing the entire scene where
    possible, and is willing to do up-front computation and caching to
    achieve that.

    UsdLuxLightListAPI provides a way to cache the computed light list, by
    publishing the list of lights onto prims in the model hierarchy.
    Consider a big set that contains lights: ::

      01  def Xform "BigSetWithLights" (
      02      kind = "assembly"
      03      payload = @BigSetWithLights.usd@   // Heavy payload
      04  ) {
      05      // Pre-computed, cached list of lights inside payload
      06      rel lightList = [
      07          <./Lights/light_1>,
      08          <./Lights/light_2>,
      09          ...
      10      ]
      11      token lightList:cacheBehavior = "consumeAndContinue";
      12  }

    The lightList relationship encodes a set of lights, and the
    lightList:cacheBehavior property provides fine-grained control over
    how to use that cache. (See details below.)

    The cache can be created by first invoking
    ComputeLightList(ComputeModeIgnoreCache) to pre-compute the list and
    then storing the result with UsdLuxLightListAPI::StoreLightList() .

    To enable efficient retrieval of the cache, it should be stored on a
    model hierarchy prim. Furthermore, note that while you can use a
    UsdLuxLightListAPI bound to the pseudo-root prim to query the lights
    (as in the example above) because it will perform a traversal over
    descendants, you cannot store the cache back to the pseduo-root prim.

    To consult the cached list, we invoke
    ComputeLightList(ComputeModeConsultModelHierarchyCache): ::

      01  // Find and load all lights, using lightList cache where available
      02  UsdLuxLightListAPI list(stage->GetPseudoRoot());
      03  SdfPathSet lights = list.ComputeLightList(
      04      UsdLuxLightListAPI::ComputeModeConsultModelHierarchyCache);
      05  stage.LoadAndUnload(lights, SdfPathSet());

    In this mode, ComputeLightList() will traverse the model hierarchy,
    accumulating cached light lists.

    Controlling Cache Behavior
    ==========================

    The lightList:cacheBehavior property gives additional fine-grained
    control over cache behavior:

       - The fallback value,"ignore", indicates that the lightList should
         be disregarded. This provides a way to invalidate cache entries. Note
         that unless"ignore"is specified, a lightList with an empty list of
         targets is considered a cache indicating that no lights are present.

       - The value"consumeAndContinue"indicates that the cache should be
         consulted to contribute lights to the scene, and that recursion should
         continue down the model hierarchy in case additional lights are added
         as descedants. This is the default value established when
         StoreLightList() is invoked. This behavior allows the lights within a
         large model, such as the BigSetWithLights example above, to be
         published outside the payload, while also allowing referencing and
         layering to add additional lights over that set.

       - The value"consumeAndHalt"provides a way to terminate recursive
         traversal of the scene for light discovery. The cache will be
         consulted but no descendant prims will be examined.

    Instancing
    ==========

    Where instances are present, UsdLuxLightListAPI::ComputeLightList()
    will return the instance-unique paths to any lights discovered within
    those instances. Lights within a UsdGeomPointInstancer will not be
    returned, however, since they cannot be referred to solely via paths.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    '''

    class ComputeMode(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    ComputeModeConsultModelHierarchyCache: ClassVar[LightListAPI.ComputeMode] = ...
    ComputeModeIgnoreCache: ClassVar[LightListAPI.ComputeMode] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxLightListAPI on UsdPrim C{prim}.


        Equivalent to UsdLuxLightListAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxLightListAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxLightListAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> LightListAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"LightListAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdLuxLightListAPI object is returned upon success. An invalid
        (or empty) UsdLuxLightListAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def ComputeLightList(self, _mode: LightListAPI.ComputeMode, /) -> list[pxr.Sdf.Path]:
        """
        Computes and returns the list of lights and light filters in the
        stage, optionally consulting a cached result.


        In ComputeModeIgnoreCache mode, caching is ignored, and this does a
        prim traversal looking for prims that have a UsdLuxLightAPI or are of
        type UsdLuxLightFilter.

        In ComputeModeConsultModelHierarchyCache, this does a traversal only
        of the model hierarchy. In this traversal, any lights that live as
        model hierarchy prims are accumulated, as well as any paths stored in
        lightList caches. The lightList:cacheBehavior attribute gives further
        control over the cache behavior; see the class overview for details.

        When instances are present, ComputeLightList(ComputeModeIgnoreCache)
        will return the instance-uniqiue paths to any lights discovered within
        those instances. Lights within a UsdGeomPointInstancer will not be
        returned, however, since they cannot be referred to solely via paths.
        """
    def CreateLightListCacheBehaviorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLightListCacheBehaviorAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLightListRel(self) -> pxr.Usd.Relationship:
        """
        See GetLightListRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LightListAPI:
        """
        Return a UsdLuxLightListAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxLightListAPI(stage->GetPrimAtPath(path));

        """
    def GetLightListCacheBehaviorAttr(self) -> pxr.Usd.Attribute:
        """
        Controls how the lightList should be interpreted.


        Valid values are:
           - consumeAndHalt: The lightList should be consulted, and if it
             exists, treated as a final authoritative statement of any lights that
             exist at or below this prim, halting recursive discovery of lights.

           - consumeAndContinue: The lightList should be consulted, but
             recursive traversal over nameChildren should continue in case
             additional lights are added by descendants.

           - ignore: The lightList should be entirely ignored. This provides a
             simple way to temporarily invalidate an existing cache. This is the
             fallback behavior.

        Declaration

        C{token lightList:cacheBehavior}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        consumeAndHalt, consumeAndContinue, ignore
        """
    def GetLightListRel(self) -> pxr.Usd.Relationship:
        """
        Relationship to lights in the scene.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def InvalidateLightList(self) -> None:
        """
        Mark any stored lightlist as invalid, by setting the
        lightList:cacheBehavior attribute to ignore.
        """
    def StoreLightList(self, _unknownArg1: typing.Iterable[pxr.Sdf.Path | str], /) -> None:
        '''
        Store the given paths as the lightlist for this prim.


        Paths that do not have this prim\'s path as a prefix will be silently
        ignored. This will set the listList:cacheBehavior
        to"consumeAndContinue".
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ListAPI(pxr.Usd.APISchemaBase):
    '''
    Deprecated

    Use LightListAPI instead

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdLuxTokens. So to set an attribute to the value"rightHanded", use
    UsdLuxTokens->rightHanded as the value.
    '''

    class ComputeMode(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    ComputeModeConsultModelHierarchyCache: ClassVar[LightListAPI.ComputeMode] = ...
    ComputeModeIgnoreCache: ClassVar[LightListAPI.ComputeMode] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxListAPI on UsdPrim C{prim}.


        Equivalent to UsdLuxListAPI::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxListAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxListAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ListAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"ListAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdLuxListAPI object is returned upon success. An invalid (or
        empty) UsdLuxListAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def ComputeLightList(self, _mode: LightListAPI.ComputeMode, /) -> list[pxr.Sdf.Path]:
        """
        Computes and returns the list of lights and light filters in the
        stage, optionally consulting a cached result.


        In ComputeModeIgnoreCache mode, caching is ignored, and this does a
        prim traversal looking for prims that have a UsdLuxLightAPI or are of
        type UsdLuxLightFilter.

        In ComputeModeConsultModelHierarchyCache, this does a traversal only
        of the model hierarchy. In this traversal, any lights that live as
        model hierarchy prims are accumulated, as well as any paths stored in
        lightList caches. The lightList:cacheBehavior attribute gives further
        control over the cache behavior; see the class overview for details.

        When instances are present, ComputeLightList(ComputeModeIgnoreCache)
        will return the instance-uniqiue paths to any lights discovered within
        those instances. Lights within a UsdGeomPointInstancer will not be
        returned, however, since they cannot be referred to solely via paths.
        """
    def CreateLightListCacheBehaviorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLightListCacheBehaviorAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLightListRel(self) -> pxr.Usd.Relationship:
        """
        See GetLightListRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ListAPI:
        """
        Return a UsdLuxListAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxListAPI(stage->GetPrimAtPath(path));

        """
    def GetLightListCacheBehaviorAttr(self) -> pxr.Usd.Attribute:
        """
        Controls how the lightList should be interpreted.


        Valid values are:
           - consumeAndHalt: The lightList should be consulted, and if it
             exists, treated as a final authoritative statement of any lights that
             exist at or below this prim, halting recursive discovery of lights.

           - consumeAndContinue: The lightList should be consulted, but
             recursive traversal over nameChildren should continue in case
             additional lights are added by descendants.

           - ignore: The lightList should be entirely ignored. This provides a
             simple way to temporarily invalidate an existing cache. This is the
             fallback behavior.

        Declaration

        C{token lightList:cacheBehavior}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        consumeAndHalt, consumeAndContinue, ignore
        """
    def GetLightListRel(self) -> pxr.Usd.Relationship:
        """
        Relationship to lights in the scene.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def InvalidateLightList(self) -> None:
        """
        Mark any stored lightlist as invalid, by setting the
        lightList:cacheBehavior attribute to ignore.
        """
    def StoreLightList(self, _unknownArg1: typing.Iterable[pxr.Sdf.Path | str], /) -> None:
        '''
        Store the given paths as the lightlist for this prim.


        Paths that do not have this prim\'s path as a prefix will be silently
        ignored. This will set the listList:cacheBehavior
        to"consumeAndContinue".
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MeshLightAPI(pxr.Usd.APISchemaBase):
    '''
    This is the preferred API schema to apply to Mesh type prims when
    adding light behaviors to a mesh.


    At its base, this API schema has the built-in behavior of applying
    LightAPI to the mesh and overriding the default materialSyncMode to
    allow the emission/glow of the bound material to affect the color of
    the light. But, it additionally serves as a hook for plugins to attach
    additional properties to"mesh lights"through the creation of API
    schemas which are authored to auto-apply to MeshLightAPI.

    Auto applied API schemas
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxMeshLightAPI on UsdPrim C{prim}.


        Equivalent to UsdLuxMeshLightAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxMeshLightAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxMeshLightAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MeshLightAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"MeshLightAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdLuxMeshLightAPI object is returned upon success. An invalid
        (or empty) UsdLuxMeshLightAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MeshLightAPI:
        """
        Return a UsdLuxMeshLightAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxMeshLightAPI(stage->GetPrimAtPath(path));

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

class NonboundableLightBase(pxr.UsdGeom.Xformable):
    """
    Base class for intrinsic lights that are not boundable.


    The primary purpose of this class is to provide a direct API to the
    functions provided by LightAPI for concrete derived light types.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxNonboundableLightBase on UsdPrim C{prim}.


        Equivalent to UsdLuxNonboundableLightBase::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxNonboundableLightBase on the prim held by
        C{schemaObj}.


        Should be preferred over UsdLuxNonboundableLightBase
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    def CreateColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateColorAttr() .
        """
    def CreateColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateColorTemperatureAttr() .
        """
    def CreateDiffuseAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateDiffuseAttr() .
        """
    def CreateEnableColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateEnableColorTemperatureAttr() .
        """
    def CreateExposureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateExposureAttr() .
        """
    def CreateFiltersRel(self) -> pxr.Usd.Relationship:
        """
        See UsdLuxLightAPI::CreateFiltersRel() .
        """
    def CreateIntensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateIntensityAttr() .
        """
    def CreateNormalizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateNormalizeAttr() .
        """
    def CreateSpecularAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::CreateSpecularAttr() .
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NonboundableLightBase:
        """
        Return a UsdLuxNonboundableLightBase holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxNonboundableLightBase(stage->GetPrimAtPath(path));

        """
    def GetColorAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetColorAttr() .
        """
    def GetColorTemperatureAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetColorTemperatureAttr() .
        """
    def GetDiffuseAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetDiffuseAttr() .
        """
    def GetEnableColorTemperatureAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetEnableColorTemperatureAttr() .
        """
    def GetExposureAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetExposureAttr() .
        """
    def GetFiltersRel(self) -> pxr.Usd.Relationship:
        """
        See UsdLuxLightAPI::GetFiltersRel() .
        """
    def GetIntensityAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetIntensityAttr() .
        """
    def GetNormalizeAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetNormalizeAttr() .
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSpecularAttr(self) -> pxr.Usd.Attribute:
        """
        See UsdLuxLightAPI::GetSpecularAttr() .
        """
    def LightAPI(self) -> LightAPI:
        """
        Contructs and returns a UsdLuxLightAPI object for this light.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class PluginLight(pxr.UsdGeom.Xformable):
    """
    Light that provides properties that allow it to identify an external
    SdrShadingNode definition, through UsdShadeNodeDefAPI, that can be
    provided to render delegates without the need to provide a schema
    definition for the light's type.



    Plugin Lights and Light Filters
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxPluginLight on UsdPrim C{prim}.


        Equivalent to UsdLuxPluginLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxPluginLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxPluginLight (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PluginLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PluginLight:
        """
        Return a UsdLuxPluginLight holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxPluginLight(stage->GetPrimAtPath(path));

        """
    def GetNodeDefAPI(self) -> pxr.UsdShade.NodeDefAPI:
        """
        Convenience method for accessing the UsdShadeNodeDefAPI functionality
        for this prim.


        One can also construct a UsdShadeNodeDefAPI directly from a UsdPrim.
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

class PluginLightFilter(LightFilter):
    """
    Light filter that provides properties that allow it to identify an
    external SdrShadingNode definition, through UsdShadeNodeDefAPI, that
    can be provided to render delegates without the need to provide a
    schema definition for the light filter's type.



    Plugin Lights and Light Filters
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxPluginLightFilter on UsdPrim C{prim}.


        Equivalent to UsdLuxPluginLightFilter::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxPluginLightFilter on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxPluginLightFilter
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PluginLightFilter:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PluginLightFilter:
        """
        Return a UsdLuxPluginLightFilter holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxPluginLightFilter(stage->GetPrimAtPath(path));

        """
    def GetNodeDefAPI(self) -> pxr.UsdShade.NodeDefAPI:
        """
        Convenience method for accessing the UsdShadeNodeDefAPI functionality
        for this prim.


        One can also construct a UsdShadeNodeDefAPI directly from a UsdPrim.
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

class PortalLight(BoundableLightBase):
    """
    A rectangular portal in the local XY plane that guides sampling of a
    dome light.


    Transmits light in the -Z direction. The rectangle is 1 unit in
    length.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxPortalLight on UsdPrim C{prim}.


        Equivalent to UsdLuxPortalLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxPortalLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxPortalLight (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHeightAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateWidthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetWidthAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PortalLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PortalLight:
        """
        Return a UsdLuxPortalLight holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxPortalLight(stage->GetPrimAtPath(path));

        """
    def GetHeightAttr(self) -> pxr.Usd.Attribute:
        """
        Height of the portal rectangle in the local Y axis.



        Declaration

        C{float inputs:height = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetWidthAttr(self) -> pxr.Usd.Attribute:
        """
        Width of the portal rectangle in the local X axis.



        Declaration

        C{float inputs:width = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class RectLight(BoundableLightBase):
    """
    Light emitted from one side of a rectangle.


    The rectangle is centered in the XY plane and emits light along the -Z
    axis. The rectangle is 1 unit in length in the X and Y axis. In the
    default position, a texture file's min coordinates should be at (+X,
    +Y) and max coordinates at (-X, -Y).
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxRectLight on UsdPrim C{prim}.


        Equivalent to UsdLuxRectLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxRectLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxRectLight (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHeightAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTextureFileAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTextureFileAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateWidthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetWidthAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RectLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RectLight:
        """
        Return a UsdLuxRectLight holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxRectLight(stage->GetPrimAtPath(path));

        """
    def GetHeightAttr(self) -> pxr.Usd.Attribute:
        """
        Height of the rectangle, in the local Y axis.



        Declaration

        C{float inputs:height = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTextureFileAttr(self) -> pxr.Usd.Attribute:
        """
        A color texture to use on the rectangle.



        Declaration

        C{asset inputs:texture:file}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetWidthAttr(self) -> pxr.Usd.Attribute:
        """
        Width of the rectangle, in the local X axis.



        Declaration

        C{float inputs:width = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ShadowAPI(pxr.Usd.APISchemaBase):
    """
    Controls to refine a light's shadow behavior.


    These are non-physical controls that are valuable for visual lighting
    work.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, connectable: pxr.UsdShade.ConnectableAPI) -> None:
        """
        Constructor that takes a ConnectableAPI object.


        Allow implicit conversion of UsdShadeConnectableAPI to
        UsdLuxShadowAPI.
        """
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxShadowAPI on UsdPrim C{prim}.


        Equivalent to UsdLuxShadowAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxShadowAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxShadowAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ShadowAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"ShadowAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdLuxShadowAPI object is returned upon success. An invalid
        (or empty) UsdLuxShadowAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def ConnectableAPI(self) -> pxr.UsdShade.ConnectableAPI:
        """
        Contructs and returns a UsdShadeConnectableAPI object with this shadow
        API prim.


        Note that a valid UsdLuxShadowAPI will only return a valid
        UsdShadeConnectableAPI if the its prim's Typed schema type is actually
        connectable.
        """
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Input:
        '''
        Create an input which can either have a value or can be connected.


        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on shadow API are connectable.
        '''
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Output:
        '''
        Create an output which can either have a value or can be connected.


        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a shadow API cannot be connected,
        as their value is assumed to be computed externally.
        '''
    def CreateShadowColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShadowColorAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShadowDistanceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShadowDistanceAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShadowEnableAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShadowEnableAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShadowFalloffAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShadowFalloffAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShadowFalloffGammaAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShadowFalloffGammaAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ShadowAPI:
        """
        Return a UsdLuxShadowAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxShadowAPI(stage->GetPrimAtPath(path));

        """
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Input:
        """
        Return the requested input if it exists.
        """
    def GetInputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Input]:
        '''
        Inputs are represented by attributes in the"inputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Output:
        """
        Return the requested output if it exists.
        """
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Output]:
        '''
        Outputs are represented by attributes in the"outputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetShadowColorAttr(self) -> pxr.Usd.Attribute:
        """
        The color of shadows cast by the light.


        This is a non-physical control. The default is to cast black shadows.

        Declaration

        C{color3f inputs:shadow:color = (0, 0, 0)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Color3f
        """
    def GetShadowDistanceAttr(self) -> pxr.Usd.Attribute:
        """
        The maximum distance shadows are cast.


        The distance is measured as the distance between the point on the
        surface and the occluder. The default value (-1) indicates no limit.

        Declaration

        C{float inputs:shadow:distance = -1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetShadowEnableAttr(self) -> pxr.Usd.Attribute:
        """
        Enables shadows to be cast by this light.



        Declaration

        C{bool inputs:shadow:enable = 1}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    def GetShadowFalloffAttr(self) -> pxr.Usd.Attribute:
        """
        The size of the shadow falloff zone within the shadow max distance,
        which can be used to hide the hard cut-off for shadows seen stretching
        past the max distance.


        The falloff zone is the area that fades from full shadowing at the
        beginning of the falloff zone to no shadowing at the max distance from
        the occluder. The falloff zone distance cannot exceed the shadow max
        distance. A falloff value equal to or less than zero (with -1 as the
        default) indicates no falloff.

        Declaration

        C{float inputs:shadow:falloff = -1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetShadowFalloffGammaAttr(self) -> pxr.Usd.Attribute:
        """
        A gamma (i.e., exponential) control over shadow strength with linear
        distance within the falloff zone.


        This controls the rate of the falloff. This requires the use of
        shadowDistance and shadowFalloff.

        Declaration

        C{float inputs:shadow:falloffGamma = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ShapingAPI(pxr.Usd.APISchemaBase):
    """
    Controls for shaping a light's emission.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, connectable: pxr.UsdShade.ConnectableAPI) -> None:
        """
        Constructor that takes a ConnectableAPI object.


        Allow implicit conversion of UsdShadeConnectableAPI to
        UsdLuxShapingAPI.
        """
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxShapingAPI on UsdPrim C{prim}.


        Equivalent to UsdLuxShapingAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxShapingAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxShapingAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ShapingAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"ShapingAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdLuxShapingAPI object is returned upon success. An invalid
        (or empty) UsdLuxShapingAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def ConnectableAPI(self) -> pxr.UsdShade.ConnectableAPI:
        """
        Contructs and returns a UsdShadeConnectableAPI object with this
        shaping API prim.


        Note that a valid UsdLuxShapingAPI will only return a valid
        UsdShadeConnectableAPI if the its prim's Typed schema type is actually
        connectable.
        """
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Input:
        '''
        Create an input which can either have a value or can be connected.


        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on shaping API are connectable.
        '''
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Output:
        '''
        Create an output which can either have a value or can be connected.


        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a shaping API cannot be connected,
        as their value is assumed to be computed externally.
        '''
    def CreateShapingConeAngleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShapingConeAngleAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShapingConeSoftnessAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShapingConeSoftnessAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShapingFocusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShapingFocusAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShapingFocusTintAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShapingFocusTintAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShapingIesAngleScaleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShapingIesAngleScaleAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShapingIesFileAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShapingIesFileAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShapingIesNormalizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShapingIesNormalizeAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ShapingAPI:
        """
        Return a UsdLuxShapingAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxShapingAPI(stage->GetPrimAtPath(path));

        """
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Input:
        """
        Return the requested input if it exists.
        """
    def GetInputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Input]:
        '''
        Inputs are represented by attributes in the"inputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Output:
        """
        Return the requested output if it exists.
        """
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Output]:
        '''
        Outputs are represented by attributes in the"outputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetShapingConeAngleAttr(self) -> pxr.Usd.Attribute:
        """
        Angular limit off the primary axis to restrict the light spread.



        Declaration

        C{float inputs:shaping:cone:angle = 90}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetShapingConeSoftnessAttr(self) -> pxr.Usd.Attribute:
        """
        Controls the cutoff softness for cone angle.


        TODO: clarify semantics

        Declaration

        C{float inputs:shaping:cone:softness = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetShapingFocusAttr(self) -> pxr.Usd.Attribute:
        """
        A control to shape the spread of light.


        Higher focus values pull light towards the center and narrow the
        spread. Implemented as an off-axis cosine power exponent. TODO:
        clarify semantics

        Declaration

        C{float inputs:shaping:focus = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetShapingFocusTintAttr(self) -> pxr.Usd.Attribute:
        """
        Off-axis color tint.


        This tints the emission in the falloff region. The default tint is
        black. TODO: clarify semantics

        Declaration

        C{color3f inputs:shaping:focusTint = (0, 0, 0)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Color3f
        """
    def GetShapingIesAngleScaleAttr(self) -> pxr.Usd.Attribute:
        """
        Rescales the angular distribution of the IES profile.


        TODO: clarify semantics

        Declaration

        C{float inputs:shaping:ies:angleScale = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetShapingIesFileAttr(self) -> pxr.Usd.Attribute:
        """
        An IES (Illumination Engineering Society) light profile describing the
        angular distribution of light.



        Declaration

        C{asset inputs:shaping:ies:file}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetShapingIesNormalizeAttr(self) -> pxr.Usd.Attribute:
        """
        Normalizes the IES profile so that it affects the shaping of the light
        while preserving the overall energy output.



        Declaration

        C{bool inputs:shaping:ies:normalize = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class SphereLight(BoundableLightBase):
    """
    Light emitted outward from a sphere.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxSphereLight on UsdPrim C{prim}.


        Equivalent to UsdLuxSphereLight::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxSphereLight on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxSphereLight (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTreatAsPointAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTreatAsPointAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SphereLight:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SphereLight:
        """
        Return a UsdLuxSphereLight holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxSphereLight(stage->GetPrimAtPath(path));

        """
    def GetRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        Radius of the sphere.



        Declaration

        C{float inputs:radius = 0.5}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTreatAsPointAttr(self) -> pxr.Usd.Attribute:
        """
        A hint that this light can be treated as a'point'light (effectively, a
        zero-radius sphere) by renderers that benefit from non-area lighting.


        Renderers that only support area lights can disregard this.

        Declaration

        C{bool treatAsPoint = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    BoundableLightBase: ClassVar[str] = ...  # read-only
    CylinderLight: ClassVar[str] = ...  # read-only
    DiskLight: ClassVar[str] = ...  # read-only
    DistantLight: ClassVar[str] = ...  # read-only
    DomeLight: ClassVar[str] = ...  # read-only
    DomeLight_1: ClassVar[str] = ...  # read-only
    GeometryLight: ClassVar[str] = ...  # read-only
    LightAPI: ClassVar[str] = ...  # read-only
    LightFilter: ClassVar[str] = ...  # read-only
    LightListAPI: ClassVar[str] = ...  # read-only
    ListAPI: ClassVar[str] = ...  # read-only
    MeshLight: ClassVar[str] = ...  # read-only
    MeshLightAPI: ClassVar[str] = ...  # read-only
    NonboundableLightBase: ClassVar[str] = ...  # read-only
    PluginLight: ClassVar[str] = ...  # read-only
    PluginLightFilter: ClassVar[str] = ...  # read-only
    PortalLight: ClassVar[str] = ...  # read-only
    RectLight: ClassVar[str] = ...  # read-only
    ShadowAPI: ClassVar[str] = ...  # read-only
    ShapingAPI: ClassVar[str] = ...  # read-only
    SphereLight: ClassVar[str] = ...  # read-only
    VolumeLight: ClassVar[str] = ...  # read-only
    VolumeLightAPI: ClassVar[str] = ...  # read-only
    Y: ClassVar[str] = ...  # read-only
    Z: ClassVar[str] = ...  # read-only
    angular: ClassVar[str] = ...  # read-only
    automatic: ClassVar[str] = ...  # read-only
    collectionFilterLinkIncludeRoot: ClassVar[str] = ...  # read-only
    collectionLightLinkIncludeRoot: ClassVar[str] = ...  # read-only
    collectionShadowLinkIncludeRoot: ClassVar[str] = ...  # read-only
    consumeAndContinue: ClassVar[str] = ...  # read-only
    consumeAndHalt: ClassVar[str] = ...  # read-only
    cubeMapVerticalCross: ClassVar[str] = ...  # read-only
    filterLink: ClassVar[str] = ...  # read-only
    geometry: ClassVar[str] = ...  # read-only
    guideRadius: ClassVar[str] = ...  # read-only
    ignore: ClassVar[str] = ...  # read-only
    independent: ClassVar[str] = ...  # read-only
    inputsAngle: ClassVar[str] = ...  # read-only
    inputsColor: ClassVar[str] = ...  # read-only
    inputsColorTemperature: ClassVar[str] = ...  # read-only
    inputsDiffuse: ClassVar[str] = ...  # read-only
    inputsEnableColorTemperature: ClassVar[str] = ...  # read-only
    inputsExposure: ClassVar[str] = ...  # read-only
    inputsHeight: ClassVar[str] = ...  # read-only
    inputsIntensity: ClassVar[str] = ...  # read-only
    inputsLength: ClassVar[str] = ...  # read-only
    inputsNormalize: ClassVar[str] = ...  # read-only
    inputsRadius: ClassVar[str] = ...  # read-only
    inputsShadowColor: ClassVar[str] = ...  # read-only
    inputsShadowDistance: ClassVar[str] = ...  # read-only
    inputsShadowEnable: ClassVar[str] = ...  # read-only
    inputsShadowFalloff: ClassVar[str] = ...  # read-only
    inputsShadowFalloffGamma: ClassVar[str] = ...  # read-only
    inputsShapingConeAngle: ClassVar[str] = ...  # read-only
    inputsShapingConeSoftness: ClassVar[str] = ...  # read-only
    inputsShapingFocus: ClassVar[str] = ...  # read-only
    inputsShapingFocusTint: ClassVar[str] = ...  # read-only
    inputsShapingIesAngleScale: ClassVar[str] = ...  # read-only
    inputsShapingIesFile: ClassVar[str] = ...  # read-only
    inputsShapingIesNormalize: ClassVar[str] = ...  # read-only
    inputsSpecular: ClassVar[str] = ...  # read-only
    inputsTextureFile: ClassVar[str] = ...  # read-only
    inputsTextureFormat: ClassVar[str] = ...  # read-only
    inputsWidth: ClassVar[str] = ...  # read-only
    latlong: ClassVar[str] = ...  # read-only
    lightFilterShaderId: ClassVar[str] = ...  # read-only
    lightFilters: ClassVar[str] = ...  # read-only
    lightLink: ClassVar[str] = ...  # read-only
    lightList: ClassVar[str] = ...  # read-only
    lightListCacheBehavior: ClassVar[str] = ...  # read-only
    lightMaterialSyncMode: ClassVar[str] = ...  # read-only
    lightShaderId: ClassVar[str] = ...  # read-only
    materialGlowTintsLight: ClassVar[str] = ...  # read-only
    mirroredBall: ClassVar[str] = ...  # read-only
    noMaterialResponse: ClassVar[str] = ...  # read-only
    orientToStageUpAxis: ClassVar[str] = ...  # read-only
    poleAxis: ClassVar[str] = ...  # read-only
    portals: ClassVar[str] = ...  # read-only
    scene: ClassVar[str] = ...  # read-only
    shadowLink: ClassVar[str] = ...  # read-only
    treatAsLine: ClassVar[str] = ...  # read-only
    treatAsPoint: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class VolumeLightAPI(pxr.Usd.APISchemaBase):
    '''
    This is the preferred API schema to apply to Volume type prims when
    adding light behaviors to a volume.


    At its base, this API schema has the built-in behavior of applying
    LightAPI to the volume and overriding the default materialSyncMode to
    allow the emission/glow of the bound material to affect the color of
    the light. But, it additionally serves as a hook for plugins to attach
    additional properties to"volume lights"through the creation of API
    schemas which are authored to auto-apply to VolumeLightAPI.

    Auto applied API schemas
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdLuxVolumeLightAPI on UsdPrim C{prim}.


        Equivalent to UsdLuxVolumeLightAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdLuxVolumeLightAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdLuxVolumeLightAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> VolumeLightAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"VolumeLightAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdLuxVolumeLightAPI object is returned upon success. An
        invalid (or empty) UsdLuxVolumeLightAPI object is returned upon
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
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> VolumeLightAPI:
        """
        Return a UsdLuxVolumeLightAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdLuxVolumeLightAPI(stage->GetPrimAtPath(path));

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

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

def BlackbodyTemperatureAsRgb(_colorTemp: float, /) -> pxr.Gf.Vec3f:
    """
    Compute the RGB equivalent of the spectrum emitted by a blackbody with
    the given temperature in degrees Kelvin, with normalized luminance.
    """
