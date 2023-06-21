import Boost.Python
import pxr.Usd
from typing import Any, ClassVar, overload

class DenoisePass(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg1: object) -> None: ...
    @overload
    def __init__(self, arg1: object, prim: Prim) -> None: ...
    @overload
    def __init__(self, arg1: object, schemaObj: SchemaBase) -> None: ...
    def Define(self, stage: Stage, path: Path) -> DenoisePass: ...
    def Get(self, stage: Stage, path: Path) -> DenoisePass: ...
    def GetSchemaAttributeNames(self, includeInherited: bool = ...) -> list: ...
    def _GetStaticTfType(self) -> Type: ...
    def __bool__(self, arg1: DenoisePass) -> object: ...
    def __reduce__(self) -> Any: ...

class Pass(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg1: object) -> None: ...
    @overload
    def __init__(self, arg1: object, prim: Prim) -> None: ...
    @overload
    def __init__(self, arg1: object, schemaObj: SchemaBase) -> None: ...
    def CreateCommandAttr(self, arg1: Pass, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateDenoiseEnableAttr(self, arg1: Pass, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateDenoisePassRel(self, arg1: Pass) -> Relationship: ...
    def CreateFileNameAttr(self, arg1: Pass, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateInputPassesRel(self, arg1: Pass) -> Relationship: ...
    def CreatePassTypeAttr(self, arg1: Pass, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateRenderSourceRel(self, arg1: Pass) -> Relationship: ...
    def Define(self, stage: Stage, path: Path) -> Pass: ...
    def Get(self, stage: Stage, path: Path) -> Pass: ...
    def GetCommandAttr(self, arg1: Pass) -> Attribute: ...
    def GetDenoiseEnableAttr(self, arg1: Pass) -> Attribute: ...
    def GetDenoisePassRel(self, arg1: Pass) -> Relationship: ...
    def GetFileNameAttr(self, arg1: Pass) -> Attribute: ...
    def GetInputPassesRel(self, arg1: Pass) -> Relationship: ...
    def GetPassTypeAttr(self, arg1: Pass) -> Attribute: ...
    def GetRenderSourceRel(self, arg1: Pass) -> Relationship: ...
    def GetRenderVisibilityCollectionAPI(self, arg1: Pass) -> CollectionAPI: ...
    def GetSchemaAttributeNames(self, includeInherited: bool = ...) -> list: ...
    def _GetStaticTfType(self) -> Type: ...
    def __bool__(self, arg1: Pass) -> object: ...
    def __reduce__(self) -> Any: ...

class Product(SettingsBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg1: object) -> None: ...
    @overload
    def __init__(self, arg1: object, prim: Prim) -> None: ...
    @overload
    def __init__(self, arg1: object, schemaObj: SchemaBase) -> None: ...
    def CreateOrderedVarsRel(self, arg1: Product) -> Relationship: ...
    def CreateProductNameAttr(self, arg1: Product, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateProductTypeAttr(self, arg1: Product, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def Define(self, stage: Stage, path: Path) -> Product: ...
    def Get(self, stage: Stage, path: Path) -> Product: ...
    def GetOrderedVarsRel(self, arg1: Product) -> Relationship: ...
    def GetProductNameAttr(self, arg1: Product) -> Attribute: ...
    def GetProductTypeAttr(self, arg1: Product) -> Attribute: ...
    def GetSchemaAttributeNames(self, includeInherited: bool = ...) -> list: ...
    def _GetStaticTfType(self) -> Type: ...
    def __bool__(self, arg1: Product) -> object: ...
    def __reduce__(self) -> Any: ...

class Settings(SettingsBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg1: object) -> None: ...
    @overload
    def __init__(self, arg1: object, prim: Prim) -> None: ...
    @overload
    def __init__(self, arg1: object, schemaObj: SchemaBase) -> None: ...
    def CreateIncludedPurposesAttr(self, arg1: Settings, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateMaterialBindingPurposesAttr(self, arg1: Settings, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateProductsRel(self, arg1: Settings) -> Relationship: ...
    def CreateRenderingColorSpaceAttr(self, arg1: Settings, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def Define(self, stage: Stage, path: Path) -> Settings: ...
    def Get(self, stage: Stage, path: Path) -> Settings: ...
    def GetIncludedPurposesAttr(self, arg1: Settings) -> Attribute: ...
    def GetMaterialBindingPurposesAttr(self, arg1: Settings) -> Attribute: ...
    def GetProductsRel(self, arg1: Settings) -> Relationship: ...
    def GetRenderingColorSpaceAttr(self, arg1: Settings) -> Attribute: ...
    def GetSchemaAttributeNames(self, includeInherited: bool = ...) -> list: ...
    def GetStageRenderSettings(self, arg1: Stage) -> Settings: ...
    def _GetStaticTfType(self) -> Type: ...
    def __bool__(self, arg1: Settings) -> object: ...
    def __reduce__(self) -> Any: ...

class SettingsBase(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg1: object) -> None: ...
    @overload
    def __init__(self, arg1: object, prim: Prim) -> None: ...
    @overload
    def __init__(self, arg1: object, schemaObj: SchemaBase) -> None: ...
    def CreateAspectRatioConformPolicyAttr(self, arg1: SettingsBase, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateCameraRel(self, arg1: SettingsBase) -> Relationship: ...
    def CreateDataWindowNDCAttr(self, arg1: SettingsBase, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateDisableMotionBlurAttr(self, arg1: SettingsBase, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateInstantaneousShutterAttr(self, arg1: SettingsBase, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreatePixelAspectRatioAttr(self, arg1: SettingsBase, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateResolutionAttr(self, arg1: SettingsBase, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def Get(self, stage: Stage, path: Path) -> SettingsBase: ...
    def GetAspectRatioConformPolicyAttr(self, arg1: SettingsBase) -> Attribute: ...
    def GetCameraRel(self, arg1: SettingsBase) -> Relationship: ...
    def GetDataWindowNDCAttr(self, arg1: SettingsBase) -> Attribute: ...
    def GetDisableMotionBlurAttr(self, arg1: SettingsBase) -> Attribute: ...
    def GetInstantaneousShutterAttr(self, arg1: SettingsBase) -> Attribute: ...
    def GetPixelAspectRatioAttr(self, arg1: SettingsBase) -> Attribute: ...
    def GetResolutionAttr(self, arg1: SettingsBase) -> Attribute: ...
    def GetSchemaAttributeNames(self, includeInherited: bool = ...) -> list: ...
    def _GetStaticTfType(self) -> Type: ...
    def __bool__(self, arg1: SettingsBase) -> object: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def RenderDenoisePass(self) -> Any: ...
    @property
    def RenderPass(self) -> Any: ...
    @property
    def RenderProduct(self) -> Any: ...
    @property
    def RenderSettings(self) -> Any: ...
    @property
    def RenderSettingsBase(self) -> Any: ...
    @property
    def RenderVar(self) -> Any: ...
    @property
    def adjustApertureHeight(self) -> Any: ...
    @property
    def adjustApertureWidth(self) -> Any: ...
    @property
    def adjustPixelAspectRatio(self) -> Any: ...
    @property
    def aspectRatioConformPolicy(self) -> Any: ...
    @property
    def camera(self) -> Any: ...
    @property
    def collectionRenderVisibilityIncludeRoot(self) -> Any: ...
    @property
    def color3f(self) -> Any: ...
    @property
    def command(self) -> Any: ...
    @property
    def cropAperture(self) -> Any: ...
    @property
    def dataType(self) -> Any: ...
    @property
    def dataWindowNDC(self) -> Any: ...
    @property
    def denoiseEnable(self) -> Any: ...
    @property
    def denoisePass(self) -> Any: ...
    @property
    def disableMotionBlur(self) -> Any: ...
    @property
    def expandAperture(self) -> Any: ...
    @property
    def fileName(self) -> Any: ...
    @property
    def full(self) -> Any: ...
    @property
    def includedPurposes(self) -> Any: ...
    @property
    def inputPasses(self) -> Any: ...
    @property
    def instantaneousShutter(self) -> Any: ...
    @property
    def intrinsic(self) -> Any: ...
    @property
    def lpe(self) -> Any: ...
    @property
    def materialBindingPurposes(self) -> Any: ...
    @property
    def orderedVars(self) -> Any: ...
    @property
    def passType(self) -> Any: ...
    @property
    def pixelAspectRatio(self) -> Any: ...
    @property
    def preview(self) -> Any: ...
    @property
    def primvar(self) -> Any: ...
    @property
    def productName(self) -> Any: ...
    @property
    def productType(self) -> Any: ...
    @property
    def products(self) -> Any: ...
    @property
    def raster(self) -> Any: ...
    @property
    def raw(self) -> Any: ...
    @property
    def renderSettingsPrimPath(self) -> Any: ...
    @property
    def renderSource(self) -> Any: ...
    @property
    def renderVisibility(self) -> Any: ...
    @property
    def renderingColorSpace(self) -> Any: ...
    @property
    def resolution(self) -> Any: ...
    @property
    def sourceName(self) -> Any: ...
    @property
    def sourceType(self) -> Any: ...

class Var(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg1: object) -> None: ...
    @overload
    def __init__(self, arg1: object, prim: Prim) -> None: ...
    @overload
    def __init__(self, arg1: object, schemaObj: SchemaBase) -> None: ...
    def CreateDataTypeAttr(self, arg1: Var, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateSourceNameAttr(self, arg1: Var, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def CreateSourceTypeAttr(self, arg1: Var, defaultValue: object = ..., writeSparsely: bool = ...) -> Attribute: ...
    def Define(self, stage: Stage, path: Path) -> Var: ...
    def Get(self, stage: Stage, path: Path) -> Var: ...
    def GetDataTypeAttr(self, arg1: Var) -> Attribute: ...
    def GetSchemaAttributeNames(self, includeInherited: bool = ...) -> list: ...
    def GetSourceNameAttr(self, arg1: Var) -> Attribute: ...
    def GetSourceTypeAttr(self, arg1: Var) -> Attribute: ...
    def _GetStaticTfType(self) -> Type: ...
    def __bool__(self, arg1: Var) -> object: ...
    def __reduce__(self) -> Any: ...