from typing import Any
from typing import Never
import numpy
from numpy.typing import NDArray
import hapi
import enum
from _typeshed import Incomplete
from typing import Callable, ClassVar

ATTRIB_COLOR: str
ATTRIB_INPUT_CURVE_COORDS: str
ATTRIB_INSTANCE: str
ATTRIB_NAME: str
ATTRIB_NORMAL: str
ATTRIB_POSITION: str
ATTRIB_ROT: str
ATTRIB_SCALE: str
ATTRIB_TANGENT: str
ATTRIB_TANGENT2: str
ATTRIB_UV: str
ATTRIB_UV2: str
BMP_FORMAT_NAME: str
CACHE_COP2_COOK: str
CACHE_COP2_FLIPBOOK: str
CACHE_GL_TEXTURE: str
CACHE_GL_VERTEX: str
CACHE_IMAGE: str
CACHE_OBJ: str
CACHE_SOP: str
CACHE_VEX: str
COLOR_VECTOR_SIZE: int
CV_VECTOR_SIZE: int
DEFAULT_IMAGE_FORMAT_NAME: str
ENV_CLIENT_NAME: str
ENV_HIP: str
ENV_JOB: str
EULER_VECTOR_SIZE: int
GLOBAL_NODES_NODE_NAME: str
INVALID_PARM_ID: int
JPEG_FORMAT_NAME: str
MAX_NUM_CONNECTIONS: int
NORMAL_VECTOR_SIZE: int
PNG_FORMAT_NAME: str
POSITION_VECTOR_SIZE: int
PRIM_MAX_VERTEX_COUNT: int
PRIM_MIN_VERTEX_COUNT: int
QUATERNION_VECTOR_SIZE: int
RAW_FORMAT_NAME: str
SCALE_VECTOR_SIZE: int
SHEAR_VECTOR_SIZE: int
TGA_FORMAT_NAME: str
TIFF_FORMAT_NAME: str
UNGROUPED_GROUP_NAME: str
UV_VECTOR_SIZE: int
VERSION_HOUDINI_BUILD: int
VERSION_HOUDINI_ENGINE_API: int
VERSION_HOUDINI_ENGINE_MAJOR: int
VERSION_HOUDINI_ENGINE_MINOR: int
VERSION_HOUDINI_MAJOR: int
VERSION_HOUDINI_MINOR: int
VERSION_HOUDINI_PATCH: int

class AlreadyInitializedError(HapiError): ...

class AssetDefAlreadyLoadedError(HapiError): ...

class AssetInfo:
    filePathSH: int
    fullOpNameSH: int
    geoInputCount: int
    geoOutputCount: int
    handleCount: int
    hasEverCooked: bool
    haveMaterialsChanged: bool
    haveObjectsChanged: bool
    helpTextSH: int
    helpURLSH: int
    labelSH: int
    nameSH: int
    nodeId: int
    objectCount: int
    objectNodeId: int
    transformInputCount: int
    versionSH: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class AssetInvalidError(HapiError): ...

class AttributeInfo:
    count: int
    exists: bool
    originalOwner: attributeOwner
    owner: attributeOwner
    storage: storageType
    totalArrayElements: int
    tupleSize: int
    typeInfo: attributeTypeInfo
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class BoxInfo:
    center: tuple[float, float, float]
    rotation: tuple[float, float, float]
    size: tuple[float, float, float]
    def __init__(self, *, no_constructor: Never) -> None: ...

class CameraInfo:
    aperture: float
    clipFar: float
    clipNear: float
    cropX: tuple[float, float]
    cropY: tuple[float, float]
    fStop: float
    focal: float
    focusDistance: float
    guideScale: float
    imagingDistance: float
    orthoZoom: float
    pixelAspect: float
    projection: cameraProjectionType
    resX: int
    resY: int
    shutterClose: float
    shutterOpen: float
    winX: tuple[float, float]
    winY: tuple[float, float]
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class CantGeneratePresetError(HapiError): ...

class CantLoadGeoError(HapiError): ...

class CantLoadPresetError(HapiError): ...

class CantLoadfileError(HapiError): ...

class CompositorOptions:
    maximumResolutionX: int
    maximumResolutionY: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class CookOptions:
    cacheMeshTopology: bool
    checkPartChanges: bool
    clearErrorsAndWarnings: bool
    cookTemplatedGeos: bool
    curveRefineLOD: float
    extraFlags: int
    handleBoxPartTypes: bool
    handleSpherePartTypes: bool
    maxVerticesPerPrimitive: int
    packedPrimInstancingMode: hapi.packedPrimInstancingMode
    preferOutputNodes: bool
    refineCurveToLinear: bool
    splitAttrSH: int
    splitGeosByAttribute: bool
    splitGeosByGroup: bool
    splitGroupSH: int
    splitPointsByVertexAttributes: bool
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class CurveInfo:
    curveCount: int
    curveType: hapi.curveType
    hasKnots: bool
    isClosed: bool
    isPeriodic: bool
    isRational: bool
    knotCount: int
    order: int
    vertexCount: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class DisallowedHengineindieW3partyPluginError(HapiError): ...

class DisallowedLcAssetWithCLicenseError(HapiError): ...

class DisallowedNcAssetWithCLicenseError(HapiError): ...

class DisallowedNcAssetWithLcLicenseError(HapiError): ...

class DisallowedNcLicenseFoundError(HapiError): ...

class FailureError(HapiError): ...

class GeoInfo:
    edgeGroupCount: int
    hasGeoChanged: bool
    hasMaterialChanged: bool
    isDisplayGeo: bool
    isEditable: bool
    isTemplated: bool
    nameSH: int
    nodeId: int
    partCount: int
    pointGroupCount: int
    primitiveGroupCount: int
    type: geoType
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class HandleBindingInfo:
    assetParmId: int
    assetParmIndex: int
    assetParmNameSH: int
    handleParmNameSH: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class HandleInfo:
    bindingsCount: int
    nameSH: int
    typeNameSH: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class HapiError(Exception): ...

class ImageFileFormat:
    defaultExtensionSH: int
    descriptionSH: int
    nameSH: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class ImageInfo:
    dataFormat: imageDataFormat
    gamma: float
    imageFileFormatNameSH: int
    interleaved: bool
    packing: imagePacking
    xRes: int
    yRes: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class InputCurveInfo:
    breakpointParameterization: inputCurveParameterization
    closed: bool
    curveType: hapi.curveType
    inputMethod: inputCurveMethod
    order: int
    reverse: bool
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class InvalidArgumentError(HapiError): ...

class InvalidSessionError(HapiError): ...

class InvalidSharedMemoryBufferError(HapiError): ...

class Keyframe:
    inTangent: float
    outTangent: float
    time: float
    value: float
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class MaterialInfo:
    exists: bool
    hasChanged: bool
    nodeId: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class NoLicenseFoundError(HapiError): ...

class NodeInfo:
    childNodeCount: int
    createdPostAssetLoad: bool
    id: int
    inputCount: int
    internalNodePathSH: int
    isTimeDependent: bool
    isValid: bool
    nameSH: int
    outputCount: int
    parentId: int
    parmChoiceCount: int
    parmCount: int
    parmFloatValueCount: int
    parmIntValueCount: int
    parmStringValueCount: int
    totalCookCount: int
    type: nodeType
    uniqueHoudiniNodeId: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class NodeInvalidError(HapiError): ...

class NotInitializedError(HapiError): ...

class ObjectInfo:
    geoCount: int
    hasTransformChanged: bool
    haveGeosChanged: bool
    isInstanced: bool
    isInstancer: bool
    isVisible: bool
    nameSH: int
    nodeId: int
    objectInstancePathSH: int
    objectToInstanceId: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class PDG_EventInfo:
    currentState: int
    dependencyId: int
    eventType: int
    lastState: int
    msgSH: int
    nodeId: int
    workItemId: int
    def __init__(self, *, no_constructor: Never) -> None: ...

class PDG_WorkItemInfo:
    index: int
    nameSH: int
    outputFileCount: int
    def __init__(self, *, no_constructor: Never) -> None: ...

class PDG_WorkItemOutputFile:
    filePathSH: int
    hash: int
    tagSH: int
    def __init__(self, *, no_constructor: Never) -> None: ...

class PDG_WorkitemInfo:
    index: int
    nameSH: int
    outputFileCount: int
    def __init__(self, *, no_constructor: Never) -> None: ...

class PDG_WorkitemResultInfo:
    filePathSH: int
    hash: int
    tagSH: int
    def __init__(self, *, no_constructor: Never) -> None: ...

class ParmChoiceInfo:
    labelSH: int
    parentParmId: int
    valueSH: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class ParmInfo:
    UIMax: float
    UIMin: float
    childIndex: int
    choiceCount: int
    choiceIndex: int
    choiceListType: hapi.choiceListType
    disabled: bool
    disabledConditionSH: int
    floatValuesIndex: int
    hasMax: bool
    hasMin: bool
    hasUIMax: bool
    hasUIMin: bool
    helpSH: int
    id: int
    inputNodeFlag: nodeFlags
    inputNodeType: nodeType
    instanceCount: int
    instanceLength: int
    instanceNum: int
    instanceStartOffset: int
    intValuesIndex: int
    invisible: bool
    isChildOfMultiParm: bool
    joinNext: bool
    labelNone: bool
    labelSH: int
    max: float
    min: float
    nameSH: int
    parentId: int
    permissions: hapi.permissions
    rampType: hapi.rampType
    scriptType: prmScriptType
    size: int
    spare: bool
    stringValuesIndex: int
    tagCount: int
    templateNameSH: int
    type: parmType
    typeInfoSH: int
    useMenuItemTokenAsValue: bool
    visibilityConditionSH: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class ParmSetFailedError(HapiError): ...

class PartInfo:
    attributeCounts: tuple[int, int, int, int]
    faceCount: int
    hasChanged: bool
    id: int
    instanceCount: int
    instancedPartCount: int
    isInstanced: bool
    nameSH: int
    pointCount: int
    type: partType
    vertexCount: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class Session:
    id: int
    type: sessionType
    def __init__(self, *, no_constructor: Never) -> None: ...

class SessionInfo:
    connectionCount: int
    enableSharedMemoryDataTransfer: bool
    maxPort: int
    minPort: int
    portType: tcpPortType
    ports: tuple[int, ...]
    sharedMemoryBufferSize: int
    sharedMemoryBufferType: thriftSharedMemoryBufferType
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class SessionSyncInfo:
    cookUsingHoudiniTime: bool
    syncViewport: bool
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class SharedMemoryBufferOverflowError(HapiError): ...

class SphereInfo:
    center: tuple[float, float, float]
    radius: float
    def __init__(self, *, no_constructor: Never) -> None: ...

class SuccessError(HapiError): ...

class ThriftServerOptions:
    autoClose: bool
    sharedMemoryBufferSize: int
    sharedMemoryBufferType: thriftSharedMemoryBufferType
    timeoutMs: float
    verbosity: statusVerbosity
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class TimelineOptions:
    endTime: float
    fps: float
    startTime: float
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class Transform:
    position: tuple[float, float, float]
    rotationQuaternion: tuple[float, float, float, float]
    rstOrder: hapi.rstOrder
    scale: tuple[float, float, float]
    shear: tuple[float, float, float]
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class TransformEuler:
    position: tuple[float, float, float]
    rotationEuler: tuple[float, float, float]
    rotationOrder: xyzOrder
    rstOrder: hapi.rstOrder
    scale: tuple[float, float, float]
    shear: tuple[float, float, float]
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class UserInterruptedError(HapiError): ...

class Viewport:
    offset: float
    position: tuple[float, float, float]
    rotationQuaternion: tuple[float, float, float, float]
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class VolumeInfo:
    hasTaper: bool
    minX: int
    minY: int
    minZ: int
    nameSH: int
    storage: storageType
    tileSize: int
    transform: Transform
    tupleSize: int
    type: volumeType
    xLength: int
    xTaper: float
    yLength: int
    yTaper: float
    zLength: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class VolumeTileInfo:
    isValid: bool
    minX: int
    minY: int
    minZ: int
    def __init__(self) -> None:
        """__init__(self, **kwargs) -> None"""

class VolumeVisualInfo:
    density: float
    iso: float
    type: volumeVisualType
    def __init__(self, *, no_constructor: Never) -> None: ...

class attributeOwner(enum.IntEnum):
    Detail = 3
    Invalid = -1
    Max = 4
    Point = 1
    Prim = 2
    Vertex = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class attributeTypeInfo(enum.IntEnum):
    Box = 12
    Box2 = 11
    Color = 5
    Hidden = 10
    Hpoint = 2
    Invalid = -1
    Matrix = 8
    Matrix3 = 7
    Max = 14
    Normal = 4
    Point = 1
    Quaternion = 6
    St = 9
    Texture = 13
    Vector = 3
    _None = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class cacheProperty(enum.IntEnum):
    CullLevel = 5
    Current = 0
    HasMax = 3
    HasMin = 1
    Max = 4
    Min = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class cameraProjectionType(enum.IntEnum):
    Invalid = -1
    Max = 2
    Ortho = 1
    Perspective = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class choiceListType(enum.IntEnum):
    Mini = 2
    Normal = 1
    Replace = 3
    Toggle = 4
    _None = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class curveOrders(enum.IntEnum):
    Cubic = 4
    Invalid = 1
    Linear = 2
    Quadratic = 3
    Varying = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class curveType(enum.IntEnum):
    Bezier = 2
    Invalid = -1
    Linear = 0
    Max = 3
    Nurbs = 1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class envIntType(enum.IntEnum):
    Invalid = -1
    Max = 221
    VersionHoudiniBuild = 120
    VersionHoudiniEngineApi = 220
    VersionHoudiniEngineMajor = 200
    VersionHoudiniEngineMinor = 210
    VersionHoudiniMajor = 100
    VersionHoudiniMinor = 110
    VersionHoudiniPatch = 130
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class errorCode(enum.IntEnum):
    AssetDefNotFound = 1
    PythonNodeError = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class geoType(enum.IntEnum):
    Curve = 3
    Default = 0
    Input = 2
    Intermediate = 1
    Invalid = -1
    Max = 4
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class groupType(enum.IntEnum):
    Edge = 2
    Invalid = -1
    Max = 3
    Point = 0
    Prim = 1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class heightFieldSampling(enum.IntEnum):
    Center = 0
    Corner = 1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class imageDataFormat(enum.IntEnum):
    Default = 0
    Float16 = 3
    Float32 = 4
    Int16 = 1
    Int32 = 2
    Int8 = 0
    Max = 5
    Unknown = -1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class imagePacking(enum.IntEnum):
    Abgr = 5
    Bgr = 3
    Default3 = 2
    Default4 = 4
    Dual = 1
    Max = 6
    Rgb = 2
    Rgba = 4
    Single = 0
    Unknown = -1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class inputCurveMethod(enum.IntEnum):
    Breakpoints = 1
    Cvs = 0
    Invalid = -1
    Max = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class inputCurveParameterization(enum.IntEnum):
    Centripetal = 2
    Chord = 1
    Invalid = -1
    Max = 3
    Uniform = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class inputType(enum.IntEnum):
    Geometry = 1
    Invalid = -1
    Max = 2
    Transform = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class jobStatus(enum.IntEnum):
    Idle = 1
    Max = 2
    Running = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class license(enum.IntEnum):
    Houdini = 2
    HoudiniEducation = 7
    HoudiniEngine = 1
    HoudiniEngineEducation = 8
    HoudiniEngineIndie = 4
    HoudiniEngineUnityUnreal = 6
    HoudiniFx = 3
    HoudiniIndie = 5
    Max = 9
    _None = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class nodeFlags(enum.IntEnum):
    Any = -1
    Bypass = 32
    Display = 1
    Editable = 16
    Locked = 8
    Network = 64
    NonBypass = 16384
    ObjCamera = 256
    ObjGeometry = 128
    ObjLight = 512
    ObjSubnet = 1024
    Render = 2
    SopCurve = 2048
    SopGuide = 4096
    Templated = 4
    TopNonscheduler = 8192
    _None = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class nodeType(enum.IntEnum):
    Any = -1
    Chop = 4
    Cop = 512
    Cop2 = 32
    Dop = 128
    Lop = 1024
    Obj = 1
    Rop = 8
    Shop = 16
    Sop = 2
    Top = 256
    Vop = 64
    _None = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class packedPrimInstancingMode(enum.IntEnum):
    Disabled = 0
    Flat = 2
    Hierarchy = 1
    Invalid = -1
    Max = 3
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class parmType(enum.IntEnum):
    Button = 3
    Color = 5
    ContainerEnd = 12
    ContainerStart = 11
    Float = 4
    FloatEnd = 5
    FloatStart = 4
    Folder = 13
    Folderlist = 11
    FolderlistRadio = 12
    Int = 0
    IntEnd = 3
    IntStart = 0
    Label = 14
    Max = 17
    Multiparmlist = 1
    Node = 10
    NodeEnd = 10
    NodeStart = 10
    NonvalueEnd = 15
    NonvalueStart = 13
    PathEnd = 9
    PathFile = 7
    PathFileDir = 16
    PathFileGeo = 8
    PathFileImage = 9
    PathStart = 7
    Separator = 15
    String = 6
    StringEnd = 10
    StringStart = 6
    Toggle = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class partType(enum.IntEnum):
    Box = 4
    Camera = 6
    Curve = 1
    Instancer = 3
    Invalid = -1
    Max = 7
    Mesh = 0
    Sphere = 5
    Volume = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class pdgEventType(enum.IntEnum):
    ContextEvents = 46
    EventAll = 37
    EventBatchItemInitialized = 36
    EventCookComplete = 11
    EventCookError = 9
    EventCookStart = 32
    EventCookWarning = 10
    EventDirtyAll = 14
    EventDirtyStart = 12
    EventDirtyStop = 13
    EventLog = 38
    EventNodeClear = 8
    EventNodeConnect = 19
    EventNodeCooked = 43
    EventNodeCreate = 16
    EventNodeDisconnect = 20
    EventNodeFirstCook = 21
    EventNodeGenerated = 44
    EventNodeProgressUpdate = 35
    EventNodeRemove = 17
    EventNodeRename = 18
    EventNull = 0
    EventSchedulerAdded = 39
    EventSchedulerRemoved = 40
    EventServiceManagerAll = 42
    EventSetScheduler = 41
    EventUiSelect = 15
    EventWorkitemAdd = 1
    EventWorkitemAddDep = 4
    EventWorkitemAddParent = 6
    EventWorkitemAddStaticAncestor = 33
    EventWorkitemFrame = 45
    EventWorkitemMerge = 29
    EventWorkitemPriority = 31
    EventWorkitemRemove = 2
    EventWorkitemRemoveDep = 5
    EventWorkitemRemoveParent = 7
    EventWorkitemRemoveStaticAncestor = 34
    EventWorkitemResult = 30
    EventWorkitemSetDict = 26
    EventWorkitemSetFile = 25
    EventWorkitemSetFloat = 23
    EventWorkitemSetGeometry = 28
    EventWorkitemSetInt = 22
    EventWorkitemSetPyobject = 27
    EventWorkitemSetString = 24
    EventWorkitemStateChange = 3
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class pdgState(enum.IntEnum):
    StateCooking = 1
    StateMax = 2
    StateMaxReadyState = 0
    StateReady = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class pdgWorkItemState(enum.IntEnum):
    WorkitemCookedCache = 6
    WorkitemCookedCancel = 8
    WorkitemCookedFail = 7
    WorkitemCookedSuccess = 5
    WorkitemCooking = 4
    WorkitemDirty = 9
    WorkitemScheduled = 3
    WorkitemUncooked = 1
    WorkitemUndefined = 0
    WorkitemWaiting = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class pdgWorkitemState(enum.IntEnum):
    WorkitemCookedCache = 6
    WorkitemCookedCancel = 8
    WorkitemCookedFail = 7
    WorkitemCookedSuccess = 5
    WorkitemCooking = 4
    WorkitemDirty = 9
    WorkitemScheduled = 3
    WorkitemUncooked = 1
    WorkitemUndefined = 0
    WorkitemWaiting = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class permissions(enum.IntEnum):
    Max = 4
    NonApplicable = 0
    ReadOnly = 2
    ReadWrite = 1
    WriteOnly = 3
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class presetType(enum.IntEnum):
    Binary = 0
    Idx = 1
    Invalid = -1
    Max = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class prmScriptType(enum.IntEnum):
    Angle = 2
    Button = 9
    Buttonstrip = 41
    Color = 19
    Color4 = 20
    Data = 37
    Dir = 18
    Directory = 5
    File = 4
    Float = 1
    FloatLog = 35
    FloatMinmax = 38
    Geometry = 7
    GeometryData = 28
    Group = 1003
    Groupcollapsible = 1001
    Groupradio = 1000
    Groupsimple = 1002
    Huecircle = 21
    Iconstrip = 42
    Image = 6
    Int = 0
    IntLog = 36
    IntMinmax = 39
    IntStartend = 40
    Intvector2 = 13
    Intvector3 = 14
    Intvector4 = 15
    KeyValueDict = 29
    Label = 30
    Object = 24
    Objectlist = 25
    Oplist = 23
    Oppath = 22
    Ordinal = 32
    RampFlt = 33
    RampRgb = 34
    Render = 26
    Rgbamask = 31
    Separator = 27
    String = 3
    Toggle = 8
    Uv = 16
    Uvw = 17
    Vector2 = 10
    Vector3 = 11
    Vector4 = 12
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class rampType(enum.IntEnum):
    Color = 1
    Float = 0
    Invalid = -1
    Max = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class result(enum.IntEnum):
    AlreadyInitialized = 2
    AssetDefAlreadyLoaded = 10
    AssetInvalid = 200
    CantGeneratePreset = 8
    CantLoadGeo = 7
    CantLoadPreset = 9
    CantLoadfile = 4
    DisallowedHengineindieW3partyPlugin = 160
    DisallowedLcAssetWithCLicense = 150
    DisallowedNcAssetWithCLicense = 130
    DisallowedNcAssetWithLcLicense = 140
    DisallowedNcLicenseFound = 120
    Failure = 1
    InvalidArgument = 6
    InvalidSession = 400
    InvalidSharedMemoryBuffer = 180
    NoLicenseFound = 110
    NodeInvalid = 210
    NotInitialized = 3
    ParmSetFailed = 5
    SharedMemoryBufferOverflow = 170
    Success = 0
    UserInterrupted = 300
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class rstOrder(enum.IntEnum):
    Default = 5
    Rts = 2
    Srt = 5
    Str = 4
    Trs = 0
    Tsr = 1
    rst = 3
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class sessionEnvIntType(enum.IntEnum):
    Invalid = -1
    License = 100
    Max = 101
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class sessionType(enum.IntEnum):
    Custom1 = 2
    Custom2 = 3
    Custom3 = 4
    Inprocess = 0
    Max = 5
    Thrift = 1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class state(enum.IntEnum):
    Cooking = 4
    Loading = 6
    Max = 7
    MaxReadyState = 2
    Ready = 0
    ReadyWithCookErrors = 2
    ReadyWithFatalErrors = 1
    StartingCook = 3
    StartingLoad = 5
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class statusType(enum.IntEnum):
    CallResult = 0
    CookResult = 1
    CookState = 2
    Max = 3
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class statusVerbosity(enum.IntEnum):
    All = 2
    Errors = 0
    Messages = 2
    Warnings = 1
    _0 = 0
    _1 = 1
    _2 = 2
    _None = -1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class storageType(enum.IntEnum):
    Dictionary = 8
    DictionaryArray = 17
    Float = 2
    Float64 = 3
    Float64Array = 12
    FloatArray = 11
    Int = 0
    Int16 = 7
    Int16Array = 16
    Int64 = 1
    Int64Array = 10
    Int8 = 6
    Int8Array = 15
    IntArray = 9
    Invalid = -1
    Max = 18
    String = 4
    StringArray = 13
    Uint8 = 5
    Uint8Array = 14
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class tcpPortType(enum.IntEnum):
    PortAny = 0
    PortList = 2
    PortRange = 1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class thriftSharedMemoryBufferType(enum.IntEnum):
    Buffer = 1
    LengthBuffer = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class transformComponent(enum.IntEnum):
    Qw = 9
    Qx = 6
    Qy = 7
    Qz = 8
    Rx = 3
    Ry = 4
    Rz = 5
    Sx = 10
    Sy = 11
    Sz = 12
    Tx = 0
    Ty = 1
    Tz = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class volumeType(enum.IntEnum):
    Houdini = 0
    Invalid = -1
    Max = 2
    Vdb = 1
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class volumeVisualType(enum.IntEnum):
    Heightfield = 4
    Invalid = -1
    Invisible = 3
    Iso = 2
    Max = 5
    Rainbow = 1
    Smoke = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class xyzOrder(enum.IntEnum):
    Default = 0
    Xzy = 1
    Yxz = 2
    Yzx = 3
    Zxy = 4
    Zyx = 5
    xyz = 0
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

def addAttribute(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo) -> bool:
    """addAttribute(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo) -> bool

    Add an attribute.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo stores attribute properties.
    
    """
def addGroup(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_name: str) -> bool:
    """addGroup(session: hapi.Session | None = None, node_id: int, part_id: int, group_type: hapi.groupType, group_name: str) -> bool

    Add a group to the input geo with the given type and name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    group_type:
        The group type.
    

    group_name:
        Name of new group to be added.
    
    """
def bindCustomImplementation(session_type: sessionType, dll_path: str) -> bool:
    """bindCustomImplementation(session_type: hapi.sessionType, dll_path: str) -> bool

    Binds a new implementation DLL to one of the custom session
    slots.



    session_type:
        Which custom implementation slot to bind the
        DLL to. Must be one of hapi.sessionType.Custom1
        hapi.sessionType.Custom2 or hapi.sessionType.Custom3.
    

    dll_path:
        The path to the custom implementation DLL.
    
    """
def cancelPDGCook(session: Session | None, graph_context_id: int) -> bool:
    """cancelPDGCook(session: hapi.Session | None = None, graph_context_id: int) -> bool

    Cancel the PDG cooking operation.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    graph_context_id:
        The id of the graph context
    
    """
def checkForSpecificErrors(session: Session | None, node_id: int, errors_to_look_for: int) -> int:
    """checkForSpecificErrors(session: hapi.Session | None = None, node_id: int, errors_to_look_for: int) -> int

    Recursively check for specific errors by error code on a node.

    Note that checking for errors can be expensive because it checks
    ALL child nodes within a node and then tries to do a string match
    for the errors being looked for. This is why such error checking
    is part of a standalone function and not done during the cooking
    step.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    errors_to_look_for:
        The hapi.errorCode error codes (as a bitfield) to look for.
    
    """
def cleanup(session: Session | None = ...) -> bool:
    """cleanup(session: hapi.Session | None = None) -> bool

    Clean up memory. This will unload all assets and you will
    need to call hapi.initialize again to be able to use any
    HAPI methods again.

    This does not release any licenses. The license will be returned when
    the process terminates.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def clearConnectionError() -> bool:
    """clearConnectionError() -> bool

    Clears the connection error. Should be used before starting
    or creating Thrift server.

    Only available when using Thrift connections.


    """
def closeSession(session: Session) -> bool:
    """closeSession(session: hapi.Session) -> bool

    Closes a session. If the session has been established using
    RPC, then the RPC connection is closed.



    session:
        The hapi.Session to close. After this call, this
        session is invalid and passing it to HAPI calls other
        than hapi.isSessionValid may result in undefined
        behavior.
    
    """
def commitGeo(session: Session | None, node_id: int) -> bool:
    """commitGeo(session: hapi.Session | None = None, node_id: int) -> bool

    Commit the current input geometry to the cook engine. Nodes
    that use this geometry node will re-cook using the input
    geometry given through the geometry setter API calls.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    
    """
def commitWorkItems(session: Session | None, node_id: int) -> bool:
    """commitWorkItems(session: hapi.Session | None = None, node_id: int) -> bool

    Commits any pending work items.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id for which the pending work items have been
        created but not yet injected.
    
    """
def composeChildNodeList(session: Session | None, parent_node_id: int, node_type_filter: int, node_flags_filter: int, recursive: bool) -> int:
    """composeChildNodeList(session: hapi.Session | None = None, parent_node_id: int, node_type_filter: int, node_flags_filter: int, recursive: bool) -> int

    Compose a list of child nodes based on given filters.

    This function will only compose the list of child nodes. It will
    not return this list. After your call to this function, call
    hapi.getComposedChildNodeList to get the list of child node ids.

    Note: When looking for all Display SOP nodes using this function,
    and using recursive mode, the recursion will stop as soon as a
    display SOP is found within each OBJ geometry network. It is
    almost never useful to get a list of ALL display SOP nodes
    recursively as they would all contain the same geometry. Even so,
    this special case only comes up if the display SOP itself is a
    subnet.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The node id of the parent node.
    

    node_type_filter:
        The node type by which to filter the children.
    

    node_flags_filter:
        The node flags by which to filter the children.
    

    recursive:
        Whether or not to compose the list recursively.
    
    """
def composeNodeCookResult(session: Session | None, node_id: int, verbosity: statusVerbosity) -> int:
    """composeNodeCookResult(session: hapi.Session | None = None, node_id: int, verbosity: hapi.statusVerbosity) -> int

    Compose the cook result string (errors and warnings) of a
    specific node.

    This will actually parse the node network inside the given
    node and return ALL errors/warnings/messages of all child nodes,
    combined into a single string. If you'd like a more narrowed
    search, call this function on one of the child nodes.

    You MUST call hapi.composeNodeCookResult before calling
    hapi.getComposedNodeCookResult because
    hapi.getComposedNodeCookResult will
    not return the real result string and instead return a
    cached version of the string that was created inside
    hapi.composeNodeCookResult. The reason for this is that
    the length of the real status string may change between
    the call to hapi.composeNodeCookResult and the call to
    hapi.getComposedNodeCookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    verbosity:
        Preferred verbosity level.
    
    """
def composeObjectList(session: Session | None, parent_node_id: int, categories: str = ...) -> int:
    """composeObjectList(session: hapi.Session | None = None, parent_node_id: int, categories: str = '') -> int

    Compose a list of child object nodes given a parent node id.

    Use the object_count returned by this function to get the
    hapi.ObjectInfo structs for each child object using
    hapi.getComposedObjectList.

    Note, if not using the categories arg, this is equivalent to:

    hapi.composeChildNodeList
    session, parent_node_id,
    hapi.nodeType.Obj
    hapi.nodeFlags.ObjGeometry
    true, &object_count );




    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The parent node id.
    

    categories:
        (Optional) Lets you filter object nodes by their render
        categories. This is a standard OBJ parameter, usually
        under the Render > Shading tab. If an OBJ node does not
        have this parameter, one can always add it as a spare.
    
        The value of this string argument should be None if not
        used or a space-separated list of category names.
        Multiple category names will be treated as an AND op.
    
    """
def connectNodeInput(session: Session | None, node_id: int, input_index: int, node_id_to_connect: int, output_index: int) -> bool:
    """connectNodeInput(session: hapi.Session | None = None, node_id: int, input_index: int, node_id_to_connect: int, output_index: int) -> bool

    Connect two nodes together.


    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    

    node_id:
        The node whom's input to connect to.
    

    input_index:
        The input index. Should be between 0 and the
        to_node's hapi.NodeInfo.inputCount - 1.
    

    node_id_to_connect:
        The node to connect to node_id's input.
    

    output_index:
        The output index. Should be between 0 and the
        to_node's hapi.NodeInfo.outputCount - 1.
    
    """
def convertMatrixToEuler(session: Session | None, matrix: list[float], rst_order: rstOrder, rot_order: xyzOrder) -> TransformEuler:
    """convertMatrixToEuler(session: hapi.Session | None = None, matrix: list, rst_order: hapi.rstOrder, rot_order: hapi.xyzOrder) -> hapi.TransformEuler

    Converts a 4x4 matrix into its TRS form.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    matrix:
        A 4x4 matrix expressed in a 16 element float array.
    

    rst_order:
        The desired transform order of the output.
    

    rot_order:
        The desired rotation order of the output.
    
    """
def convertMatrixToEuler_np(session: Session | None, matrix: NDArray[numpy.float32], rst_order: rstOrder, rot_order: xyzOrder) -> TransformEuler:
    """convertMatrixToEuler_np(session: hapi.Session | None = None, matrix: numpy.ndarray[dtype=float32], rst_order: hapi.rstOrder, rot_order: hapi.xyzOrder) -> hapi.TransformEuler

    Converts a 4x4 matrix into its TRS form.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    matrix:
        A 4x4 matrix expressed in a 16 element float array.
    

    rst_order:
        The desired transform order of the output.
    

    rot_order:
        The desired rotation order of the output.
    
    """
def convertMatrixToQuat(session: Session | None, matrix: list[float], rst_order: rstOrder) -> Transform:
    """convertMatrixToQuat(session: hapi.Session | None = None, matrix: list, rst_order: hapi.rstOrder) -> hapi.Transform

    Converts a 4x4 matrix into its TRS form.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    matrix:
        A 4x4 matrix expressed in a 16 element float array.
    

    rst_order:
        The desired transform order of the output.
    
    """
def convertMatrixToQuat_np(session: Session | None, matrix: NDArray[numpy.float32], rst_order: rstOrder) -> Transform:
    """convertMatrixToQuat_np(session: hapi.Session | None = None, matrix: numpy.ndarray[dtype=float32], rst_order: hapi.rstOrder) -> hapi.Transform

    Converts a 4x4 matrix into its TRS form.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    matrix:
        A 4x4 matrix expressed in a 16 element float array.
    

    rst_order:
        The desired transform order of the output.
    
    """
def convertTransform(session: Session | None, transform_in: TransformEuler, rst_order: rstOrder, rot_order: xyzOrder) -> TransformEuler:
    """convertTransform(session: hapi.Session | None = None, transform_in: hapi.TransformEuler, rst_order: hapi.rstOrder, rot_order: hapi.xyzOrder) -> hapi.TransformEuler

    Converts the transform described by a hapi.TransformEuler
    struct into a different transform and rotation order.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    transform_in:
        The transform to be converted.
    

    rst_order:
        The desired transform order of the output.
    

    rot_order:
        The desired rotation order of the output.
    
    """
def convertTransformEulerToMatrix(session: Session | None, transform: TransformEuler) -> list[float]:
    """convertTransformEulerToMatrix(session: hapi.Session | None = None, transform: hapi.TransformEuler) -> list

    Converts hapi.TransformEuler into a 4x4 transform matrix.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    transform:
        The hapi.TransformEuler you wish to convert.
    
    """
def convertTransformEulerToMatrix_np(session: Session | None, transform: TransformEuler) -> NDArray[numpy.float32]:
    """convertTransformEulerToMatrix_np(session: hapi.Session | None = None, transform: hapi.TransformEuler) -> numpy.ndarray[dtype=float32]

    Converts hapi.TransformEuler into a 4x4 transform matrix.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    transform:
        The hapi.TransformEuler you wish to convert.
    
    """
def convertTransformQuatToMatrix(session: Session | None, transform: Transform) -> list[float]:
    """convertTransformQuatToMatrix(session: hapi.Session | None = None, transform: hapi.Transform) -> list

    Converts hapi.Transform into a 4x4 transform matrix.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    transform:
        The hapi.Transform you wish to convert.
    
    """
def convertTransformQuatToMatrix_np(session: Session | None, transform: Transform) -> NDArray[numpy.float32]:
    """convertTransformQuatToMatrix_np(session: hapi.Session | None = None, transform: hapi.Transform) -> numpy.ndarray[dtype=float32]

    Converts hapi.Transform into a 4x4 transform matrix.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    transform:
        The hapi.Transform you wish to convert.
    
    """
def cookNode(session: Session | None, node_id: int, cook_options: CookOptions | None = ...) -> bool:
    """cookNode(session: hapi.Session | None = None, node_id: int, cook_options: hapi.CookOptions | None = None) -> bool

    Initiate a cook on this node. Note that this may trigger
    cooks on other nodes if they are connected.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    cook_options:
        The cook options. Pass in None to use the global
        cook options that you specified when calling
        hapi.initialize.
    
    """
def cookPDG(session: Session, cook_node_id: int, generate_only: int, blocking: int) -> bool:
    """cookPDG(session: hapi.Session, cook_node_id: int, generate_only: int, blocking: int) -> bool

    Starts a PDG cooking operation. This can be asynchronous.
    Progress can be checked with hapi.getPDGState and
    hapi.getPDGState. Events generated during this cook can be
    collected with hapi.getPDGEvents. Any uncollected events will be
    discarded at the start of the cook.

    If there are any $HIPFILE file dependencies on nodes involved in the cook
    a hip file will be automatically saved to $HOUDINI_TEMP_DIR directory so
    that it can be copied to the working directory by the scheduler. This means
    $HIP will be equal to $HOUDINI_TEMP_DIR.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    cook_node_id:
        The node id of a TOP node for the cook operation.
    

    generate_only:
        1 means only static graph generation will done. 0 means
        a full graph cook. Generation is always blocking.
    

    blocking:
        0 means return immediately and cooking will be done
        asynchronously. 1 means return when cooking completes.
    
    """
def cookPDGAllOutputs(session: Session, cook_node_id: int, generate_only: int, blocking: int) -> bool:
    """cookPDGAllOutputs(session: hapi.Session, cook_node_id: int, generate_only: int, blocking: int) -> bool

    Starts a PDG cooking operation. This can be asynchronous.
    Progress can be checked with hapi.getPDGState and
    hapi.getPDGState. Events generated during this cook can be
    collected with hapi.getPDGEvents. Any uncollected events will be
    discarded at the start of the cook.

    If there are any $HIPFILE file dependencies on nodes involved in the
    cook a hip file will be automatically saved to $HOUDINI_TEMP_DIR
    directory so that it can be copied to the working directory by the
    scheduler. This means $HIP will be equal to $HOUDINI_TEMP_DIR.

    If cook_node_id is a network / subnet, then if it has output nodes
    it cooks all of its output nodes and not just output 0. If it does
    not have output nodes it cooks the node with the output flag.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    cook_node_id:
        The node id of a TOP node for the cook operation.
    

    generate_only:
        1 means only static graph generation will done. 0 means
        a full graph cook. Generation is always blocking.
    

    blocking:
        0 means return immediately and cooking will be done
        asynchronously. 1 means return when cooking completes.
    
    """
def createCOPImage(session: Session | None, parent_node_id: int, width: int, height: int, packing: imagePacking, flip_x: bool, flip_y: bool, data_array: list[float], start: int, length: int) -> int:
    """createCOPImage(session: hapi.Session | None = None, parent_node_id: int, width: int, height: int, packing: hapi.imagePacking, flip_x: bool, flip_y: bool, data_array: list, start: int = 0, length: int) -> int

    Loads some raw image data into a COP node.

    This method expects the image data to be in linear color space.
    It will not do any color space conversions for you; the data
    must be converted beforehand.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The node that the copnet containing the texture will be
        created in, or -1 if the parent is the image manager.
    

    width:
        The width of the image in pixels. `width` * `height` *
        channel count (implied by `packing)` should equal the size
        of `data_array`.
    

    height:
        The height of the image in pixels. `width` * `height` *
        channel count (implied by `packing)` should equal the size
        of `data_array`.
    

    packing:
        How the image data is packed (single-channel, RBGA, etc).
    

    flip_x:
        Whether to flip the image horizontally.
    

    flip_y:
        Whether to flip the image vertically.
    

    data_array:
        A float array representing the image's pixel data. Values
        should be between 0.0 and 1.0. The data should be packed
        according to `packing`.
    

    start:
        The index of the first value of `data_array` to use.
        Must be at least 0 and at most (size of `data_array` - 1).
    

    length:
        How much of `data_array` to use. Must be at least 0
        and at most (size of `data_array` - start).
    
    """
def createCOPImage_np(session: Session | None, parent_node_id: int, width: int, height: int, packing: imagePacking, flip_x: bool, flip_y: bool, data_array: NDArray[numpy.float32], start: int, length: int) -> int:
    """createCOPImage_np(session: hapi.Session | None = None, parent_node_id: int, width: int, height: int, packing: hapi.imagePacking, flip_x: bool, flip_y: bool, data_array: numpy.ndarray[dtype=float32], start: int = 0, length: int) -> int

    Loads some raw image data into a COP node.

    This method expects the image data to be in linear color space.
    It will not do any color space conversions for you; the data
    must be converted beforehand.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The node that the copnet containing the texture will be
        created in, or -1 if the parent is the image manager.
    

    width:
        The width of the image in pixels. `width` * `height` *
        channel count (implied by `packing)` should equal the size
        of `data_array`.
    

    height:
        The height of the image in pixels. `width` * `height` *
        channel count (implied by `packing)` should equal the size
        of `data_array`.
    

    packing:
        How the image data is packed (single-channel, RBGA, etc).
    

    flip_x:
        Whether to flip the image horizontally.
    

    flip_y:
        Whether to flip the image vertically.
    

    data_array:
        A float array representing the image's pixel data. Values
        should be between 0.0 and 1.0. The data should be packed
        according to `packing`.
    

    start:
        The index of the first value of `data_array` to use.
        Must be at least 0 and at most (size of `data_array` - 1).
    

    length:
        How much of `data_array` to use. Must be at least 0
        and at most (size of `data_array` - start).
    
    """
def createHeightFieldInput(session: Session | None, parent_node_id: int, name: str, xsize: int, ysize: int, voxelsize: float, sampling: heightFieldSampling) -> tuple[int, int, int, int]:
    '''createHeightFieldInput(session: hapi.Session | None = None, parent_node_id: int = -1, name: str = \'\', xsize: int, ysize: int, voxelsize: float, sampling: hapi.heightFieldSampling) -> tuple

    Creates the required node hierarchy needed for heightfield inputs.

    Note that when saving the Houdini scene using
    hapi.saveHIPFile the nodes created with this
    method will be green and will start with the name "input".



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The parent node network\'s node id or -1 if the parent
        network is the manager (top-level) node. In that case,
        the manager must be identified by the table name in the
        operator_name.
    

    name:
        Give this input node a name for easy debugging.
        The node\'s parent OBJ node and the Null SOP node will both
        get this given name with "input_" prepended.
        You can also pass None in which case the name will
        be "input#" where # is some number.
    

    xsize:
        size of the heightfield in X
    

    ysize:
        size of the heightfield in y
    

    voxelsize:
        Size of the voxel
    

    sampling:
        Type of sampling which should be either center or corner.
    
    '''
def createHeightfieldInputVolumeNode(session: Session | None, parent_node_id: int, name: str, xsize: int, ysize: int, voxelsize: float) -> int:
    '''createHeightfieldInputVolumeNode(session: hapi.Session | None = None, parent_node_id: int = -1, name: str = \'\', xsize: int, ysize: int, voxelsize: float) -> int

    Creates a volume input node that can be used with Heightfields

    Note that when saving the Houdini scene using
    hapi.saveHIPFile the nodes created with this
    method will be green and will start with the name "input".



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The parent node network\'s node id or -1 if the parent
        network is the manager (top-level) node. In that case,
        the manager must be identified by the table name in the
        operator_name.
    

    name:
        The name of the volume to create.
        You can also pass None in which case the name will
        be "input#" where # is some number.
    

    xsize:
        size of the heightfield in X
    

    ysize:
        size of the heightfield in y
    

    voxelsize:
        Size of the voxel
    
    '''
def createInProcessSession(session_info: SessionInfo) -> Session:
    """createInProcessSession(session_info: hapi.SessionInfo) -> hapi.Session

    Creates a new in-process session. There can only be
    one such session per host process.



    session_info:
        A hapi.SessionInfo struct to specify session configurations.
    
    """
def createInputCameraNode(session: Session | None = ..., parent_node_id: int = ..., camera_name: str = ..., node_label: str = ...) -> int:
    '''createInputCameraNode(session: hapi.Session | None = None, parent_node_id: int = -1, camera_name: str = \'\', node_label: str = \'\') -> int

    Creates a SOP Camera node which can then be configured with
    hapi.setInputCameraInfo and
    hapi.setInputCameraTransform.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The node id of the parent OBJ node or SOP subnetwork node in
        which the input camera node should be created, or -1 to
        create a new dummy parent OBJ node for this input node.
    

    camera_name:
        The name of the camera. The name of the camera will be added
        to the SOP camera primitive as a "name" attribute. You can
        also pass None if you want the default name to be used.
    

    node_label:
        Give this input node a name for easy debugging.
        The node\'s parent OBJ node and the Null SOP node will both
        get this given name with "input_" prepended.
        You can also pass None in which case the name will
        be "input#" where # is some number.
    
    '''
def createInputCurveNode(session: Session | None = ..., parent_node_id: int = ..., name: str = ...) -> int:
    '''createInputCurveNode(session: hapi.Session | None = None, parent_node_id: int = -1, name: str = \'\') -> int

    Helper for specifically creating a curve input geometry SOP.
    Inside the specified parent node, this will create a Null SOP that
    contains the hapi.ATTRIB_INPUT_CURVE_COORDS attribute.
    It will set up the node as a curve part with no points.
    In addition to creating the input node, it will also commit and cook
    the geometry.

    Note that when saving the Houdini scene using
    hapi.saveHIPFile the nodes created with this
    method will be green and will start with the name "input".



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The node id of the parent OBJ node or SOP subnetwork node in
        which the input node should be created, or -1 to create a
        new dummy parent OBJ node for this input node.
    

    name:
        Give this input node a name for easy debugging.
        The node\'s parent OBJ node and the Null SOP node will both
        get this given name with "input_" prepended.
        You can also pass None in which case the name will
        be "input#" where # is some number.
    
    '''
def createInputNode(session: Session | None = ..., parent_node_id: int = ..., name: str = ...) -> int:
    '''createInputNode(session: hapi.Session | None = None, parent_node_id: int = -1, name: str = \'\') -> int

    Creates a simple geometry SOP node that can accept geometry input.
    Inside the specified parent node, this will create a Null SOP
    you can set the geometry of using the geometry SET APIs.
    You can then connect this node to any other node as a geometry
    input.

    Note that when saving the Houdini scene using
    hapi.saveHIPFile the nodes created with this
    method will be green and will start with the name "input".



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The node id of the parent OBJ node or SOP subnetwork node in
        which the input node should be created, or -1 to create a
        new dummy parent OBJ node for this input node.
    

    name:
        Give this input node a name for easy debugging.
        The node\'s parent OBJ node and the Null SOP node will both
        get this given name with "input_" prepended.
        You can also pass None in which case the name will
        be "input#" where # is some number.
    
    '''
def createNode(session: Session | None, parent_node_id: int, operator_name: str, node_label: str = ..., cook_on_creation: bool = ...) -> int:
    '''createNode(session: hapi.Session | None = None, parent_node_id: int = -1, operator_name: str, node_label: str = \'\', cook_on_creation: bool = False) -> int

    Create a node inside a node network. Nodes created this way
    will have their hapi.NodeInfo.createdPostAssetLoad set
    to True.

    In threaded mode, this is an _async call_!

    This is also when we actually check for valid licenses.

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately with a call
    result of hapi.result.Success even if fed garbage. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the creation (and, optionally, the first cook)
    of the node has finished.

    Also note that the cook result won\'t be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The parent node network\'s node id or -1 if the parent
        network is the manager (top-level) node. In that case,
        the manager must be identified by the table name in the
        operator_name.
    

    operator_name:
        The name of the node operator type.
    
        If you are creating an Object or SOP node, you can pass
        parent_node_id == -1 as long as you include the table name
        (ie. Object/ or Sop/) as a prefix to the operator_name.
        This convenience is only available for Object or SOP nodes.
        This is the common case for when creating asset nodes
        from a loaded asset library. In that case, just pass
        whatever hapi.getAvailableAssets returns.
    
        If you have a parent_node_id then you should
        include only the namespace, name, and version.
    
        For example, lets say you have an Object type asset, in
        the "hapi" namespace, of version 2.0, named "foo". If
        you pass parent_node_id == -1, then set the operator_name
        as "Object/hapi::foo::2.0". Otherwise, if you have a valid
        parent_node_id, then just pass operator_name as
        "hapi::foo::2.0".
    

    node_label:
        (Optional) The label of the newly created node.
    

    cook_on_creation:
        Set whether the node should cook once created or not.
    
    '''
def createThriftNamedPipeSession(pipe_name: str, session_info: SessionInfo) -> Session:
    """createThriftNamedPipeSession(pipe_name: str, session_info: hapi.SessionInfo) -> hapi.Session

    Creates a Thrift RPC session using a Windows named pipe
    or a Unix domain socket as transport.



    pipe_name:
        The name of the pipe or socket.
    

    session_info:
        A hapi.SessionInfo struct to specify session configurations.
    
    """
def createThriftSharedMemorySession(shared_mem_name: str, session_info: SessionInfo) -> Session:
    """createThriftSharedMemorySession(shared_mem_name: str, session_info: hapi.SessionInfo) -> hapi.Session

    Creates a Thrift RPC session using a shared memory buffer as the
    transport mechanism.



    shared_mem_name:
        The name of the memory buffer. This must match the name of
        the shared memory buffer of the server that you are wishing
        to connect to.
    

    session_info:
        A hapi.SessionInfo struct to specify session configurations.
    
    """
def createThriftSocketSession(host_name: str, port: int, session_info: SessionInfo) -> Session:
    """createThriftSocketSession(host_name: str, port: int, session_info: hapi.SessionInfo) -> hapi.Session

    Creates a Thrift RPC session using a TCP socket as transport.


    host_name:
        The name of the server host.
    

    port:
        The server port to connect to.
    

    session_info:
        A hapi.SessionInfo struct to specify session configurations.
    
    """
def createWorkItem(session: Session | None, node_id: int, name: str, index: int) -> int:
    """createWorkItem(session: hapi.Session | None = None, node_id: int, name: str, index: int) -> int

    Creates a new pending work item for the given node. The work item
    will not be submitted to the graph until it is committed with
    hapi.commitWorkItems. The node is expected to be a generator type.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    name:
        The null-terminated name of the work item. The name will
        be automatically suffixed to make it unique.
    

    index:
        The index of the work item. The semantics of the index
        are user defined.
    
    """
def deleteAttribute(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo) -> bool:
    """deleteAttribute(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo) -> bool

    Delete an attribute from an input geo



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo stores attribute properties.
    
    """
def deleteGroup(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_name: str) -> bool:
    """deleteGroup(session: hapi.Session | None = None, node_id: int, part_id: int, group_type: hapi.groupType, group_name: str) -> bool

    Remove a group from the input geo with the given type and name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    group_type:
        The group type.
    

    group_name:
        Name of the group to be removed
    
    """
def deleteNode(session: Session | None, node_id: int) -> bool:
    """deleteNode(session: hapi.Session | None = None, node_id: int) -> bool

    Delete a node from a node network. Only nodes with their
    hapi.NodeInfo.createdPostAssetLoad set to True can be
    deleted this way.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node to delete.
    
    """
def dirtyPDGNode(session: Session | None, node_id: int, clean_results: bool = ...) -> bool:
    """dirtyPDGNode(session: hapi.Session | None = None, node_id: int, clean_results: bool = 0) -> bool

    Dirties the given node. Cancels the cook if necessary and then
    deletes all workitems on the node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    clean_results:
        Remove the results generated by the node.
    
    """
def disconnectNodeInput(session: Session | None, node_id: int, input_index: int) -> bool:
    """disconnectNodeInput(session: hapi.Session | None = None, node_id: int, input_index: int) -> bool

    Disconnect a node input.


    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    

    node_id:
        The node whom's input to disconnect.
    

    input_index:
        The input index. Should be between 0 and the
        to_node's hapi.NodeInfo.inputCount - 1.
    
    """
def disconnectNodeOutputsAt(session: Session | None, node_id: int, output_index: int) -> bool:
    """disconnectNodeOutputsAt(session: hapi.Session | None = None, node_id: int, output_index: int) -> bool

    Disconnect all of the node's output connections at the output index.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node whom's outputs to disconnect.
    

    output_index:
        The output index. Should be between 0 and the
        to_node's hapi.NodeInfo.outputCount.
    
    """
def extractImageToFile(session: Session | None, material_node_id: int, image_file_format_name: str, image_planes: str, destination_folder_path: str, destination_file_name: str) -> int:
    '''extractImageToFile(session: hapi.Session | None = None, material_node_id: int, image_file_format_name: str, image_planes: str, destination_folder_path: str, destination_file_name: str) -> int

    Extract a rendered image to a file.

    Note that you must call one of hapi.renderTextureToImage
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    first for this method call to make sense.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    

    image_file_format_name:
        The image file format name you wish the image to be
        extracted as. You can leave this parameter None to
        get the image in the original format if it comes from
        another texture file or in the default HAPI format,
        which is hapi.DEFAULT_IMAGE_FORMAT_NAME if the image
        is generated.
    
        You can get some of the very common standard image
        file format names from HAPI_Common.h under the
        "Defines" section.
    
        You can also get a list of all supported file formats
        (and the exact names this parameter expects)
        by using hapi.getSupportedImageFileFormats. This
        list will include custom file formats you created via
        custom DSOs (see HDK docs about IMG_Format). You will
        get back a list of hapi.ImageFileFormat. This
        parameter expects the hapi.ImageFileFormat.nameSH
        of a given image file format.
    

    image_planes:
        The image planes you wish to extract into the file.
        Multiple image planes should be separated by spaces.
    

    destination_folder_path:
        The folder where the image file should be created.
    

    destination_file_name:
        Optional parameter to overwrite the name of the
        extracted texture file. This should NOT include
        the extension as the file type will be decided
        by the hapi.ImageInfo you can set using
        hapi.setImageInfo. You still have to use
        destination_file_path to get the final file path.
    
        Pass in None to have the file name be automatically
        generated from the name of the material SHOP node,
        the name of the texture map parameter if the
        image was rendered from a texture, and the image
        plane names specified.
    
    '''
def extractImageToMemory(session: Session | None, material_node_id: int, image_file_format_name: str, image_planes: str) -> int:
    '''extractImageToMemory(session: hapi.Session | None = None, material_node_id: int, image_file_format_name: str, image_planes: str) -> int

    Extract a rendered image to memory.

    Note that you must call one of hapi.renderTextureToImage
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    first for this method call to make sense.

    Also note that this function will do all the work of
    extracting and compositing the image into a memory buffer
    but will not return to you that buffer, only its size. Use
    the returned size to allocated a sufficiently large buffer
    and call hapi.getImageMemoryBuffer to fill your buffer
    with the just extracted image.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    

    image_file_format_name:
        The image file format name you wish the image to be
        extracted as. You can leave this parameter None to
        get the image in the original format if it comes from
        another texture file or in the default HAPI format,
        which is hapi.DEFAULT_IMAGE_FORMAT_NAME if the image
        is generated.
    
        You can get some of the very common standard image
        file format names from HAPI_Common.h under the
        "Defines" section.
    
        You can also get a list of all supported file formats
        (and the exact names this parameter expects)
        by using hapi.getSupportedImageFileFormats. This
        list will include custom file formats you created via
        custom DSOs (see HDK docs about IMG_Format). You will
        get back a list of hapi.ImageFileFormat. This
        parameter expects the hapi.ImageFileFormat.nameSH
        of a given image file format.
    

    image_planes:
        The image planes you wish to extract into the file.
        Multiple image planes should be separated by spaces.
    
    '''
def getActiveCacheCount(session: Session | None = ...) -> int:
    """getActiveCacheCount(session: hapi.Session | None = None) -> int

    Get the number of currently active caches.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getActiveCacheNames(session: Session | None, active_cache_count: int) -> list[int]:
    """getActiveCacheNames(session: hapi.Session | None = None, active_cache_count: int) -> list

    Get the names of the currently active caches.

    Requires a valid active cache count which you get from:
    hapi.getActiveCacheCount.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    active_cache_count:
        The count returned by hapi.getActiveCacheCount.
    
    """
def getAssetDefinitionParmCounts(session: Session | None, library_id: int, asset_name: str) -> tuple[int, int, int, int, int]:
    """getAssetDefinitionParmCounts(session: hapi.Session | None = None, library_id: int, asset_name: str) -> tuple

    Get the number of asset parameters contained in an asset
    library, as well as the number of parameter int, float,
    string, and choice values.

    This does not create the asset in the session.
    Use this for faster querying of asset parameters compared to
    creating the asset node and querying the node's parameters.

    This does require hapi.loadAssetLibraryFromFile to be
    called prior, in order to load the asset library and
    acquire library_id. Then hapi.getAvailableAssetCount and
    hapi.getAvailableAssets should be called to get the
    asset_name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_id:
        Returned by hapi.loadAssetLibraryFromFile.
    

    asset_name:
        Name of the asset to get the parm counts for.
    
    """
def getAssetDefinitionParmInfos(session: Session | None, library_id: int, asset_name: str, start: int, length: int) -> list[ParmInfo]:
    """getAssetDefinitionParmInfos(session: hapi.Session | None = None, library_id: int, asset_name: str, start: int = 0, length: int) -> list

    Fill an array of hapi.ParmInfo structs with parameter
    information for the specified asset in the specified asset
    library.

    This does not create the asset in the session.
    Use this for faster querying of asset parameters compared to
    creating the asset node and querying the node's parameters.

    This does require hapi.loadAssetLibraryFromFile to be
    called prior, in order to load the asset library and
    acquire library_id. hapi.getAssetDefinitionParmCounts should
    be called prior to acquire the count for the size of
    parm_infos_array.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_id:
        Returned by hapi.loadAssetLibraryFromFile.
    

    asset_name:
        Name of the asset to get the parm counts for.
    

    start:
        First index of range. Must be at least 0 and at
        most parm_count - 1 acquired from
        hapi.getAssetInfo.
    

    length:
        Must be at least 1 and at most parm_count - start acquired
        from hapi.getAssetInfo
    
    """
def getAssetDefinitionParmTagName(session: Session | None, library_id: int, asset_name: str, parm_id: int, tag_index: int) -> int:
    """getAssetDefinitionParmTagName(session: hapi.Session | None = None, library_id: int, asset_name: str, parm_id: int, tag_index: int) -> int




    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_id:
        Returned by hapi.loadAssetLibraryFromFile.
    

    asset_name:
        Name of the asset that the parm tag is being retrieved from.
    

    parm_id:
        Id of the parm that the tag belongs to.
    

    tag_index:
        The index of the parm tag to retrieve the name of.
    
    """
def getAssetDefinitionParmTagValue(session: Session | None, library_id: int, asset_name: str, parm_id: int, tag_name: str) -> int:
    """getAssetDefinitionParmTagValue(session: hapi.Session | None = None, library_id: int, asset_name: str, parm_id: int, tag_name: str) -> int




    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_id:
        Returned by hapi.loadAssetLibraryFromFile.
    

    asset_name:
        Name of the asset that the parm tag is being retrieved from.
    

    parm_id:
        Id of the parm that the tag belongs to.
    

    tag_name:
        The name of the parm tag to retrieve the value of.
    
    """
def getAssetDefinitionParmValues(session: Session | None, library_id: int, asset_name: str, int_start: int, int_length: int, float_start: int, float_length: int, string_evaluate: bool, string_start: int, string_length: int, choice_start: int, choice_length: int) -> tuple[list[int], list[float], list[int], list[ParmChoiceInfo]]:
    '''getAssetDefinitionParmValues(session: hapi.Session | None = None, library_id: int, asset_name: str, int_start: int = 0, int_length: int, float_start: int = 0, float_length: int, string_evaluate: bool = True, string_start: int = 0, string_length: int, choice_start: int = 0, choice_length: int) -> tuple

    Fill arrays of parameter int values, float values, string values,
    and choice values for parameters in the specified asset in the
    specified asset library.

    This does not create the asset in the session.
    Use this for faster querying of asset parameters compared to
    creating the asset node and querying the node\'s parameters.
    Note that only default values are retrieved.

    This does require hapi.loadAssetLibraryFromFile to be
    called prior, in order to load the asset library and
    acquire library_id. hapi.getAssetDefinitionParmCounts should
    be called prior to acquire the counts for the sizes of
    the values arrays.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_id:
        Returned by hapi.loadAssetLibraryFromFile.
    

    asset_name:
        Name of the asset to get the parm counts for.
    

    int_start:
        First index of range for int_values_array. Must be at
        least 0 and at most int_value_count - 1 acquired from
        hapi.getAssetDefinitionParmCounts.
    

    int_length:
        Must be at least 0 and at most int_value_count - int_start
        acquired from hapi.getAssetDefinitionParmCounts.
    

    float_start:
        First index of range for float_values_array. Must be at
        least 0 and at most float_value_count - 1 acquired from
        hapi.getAssetDefinitionParmCounts.
    

    float_length:
        Must be at least 0 and at most float_value_count -
        float_start acquired from
        hapi.getAssetDefinitionParmCounts.
    

    string_evaluate:
        Whether or not to evaluate the string expressions.
        For example, the string "$F" would evaluate to the
        current frame number. So, passing in evaluate = False
        would give you back the string "$F" and passing
        in evaluate = True would give you back "1" (assuming
        the current frame is 1).
    

    string_start:
        First index of range for string_values_array. Must be at
        least 0 and at most string_value_count - 1 acquired from
        hapi.getAssetDefinitionParmCounts.
    

    string_length:
        Must be at least 0 and at most string_value_count -
        string_start acquired from
        hapi.getAssetDefinitionParmCounts.
    

    choice_start:
        First index of range for choice_values_array. Must be at
        least 0 and at most choice_value_count - 1 acquired from
        hapi.getAssetDefinitionParmCounts.
    

    choice_length:
        Must be at least 0 and at most choice_value_count -
        choice_start acquired from
        hapi.getAssetDefinitionParmCounts.
    
    '''
def getAssetDefinitionParmValues_np(session: Session | None, library_id: int, asset_name: str, int_start: int, int_length: int, float_start: int, float_length: int, string_evaluate: bool, string_start: int, string_length: int, choice_start: int, choice_length: int) -> tuple[NDArray[numpy.int32], NDArray[numpy.float32], list[int], list[ParmChoiceInfo]]:
    '''getAssetDefinitionParmValues_np(session: hapi.Session | None = None, library_id: int, asset_name: str, int_start: int = 0, int_length: int, float_start: int = 0, float_length: int, string_evaluate: bool = True, string_start: int = 0, string_length: int, choice_start: int = 0, choice_length: int) -> tuple

    Fill arrays of parameter int values, float values, string values,
    and choice values for parameters in the specified asset in the
    specified asset library.

    This does not create the asset in the session.
    Use this for faster querying of asset parameters compared to
    creating the asset node and querying the node\'s parameters.
    Note that only default values are retrieved.

    This does require hapi.loadAssetLibraryFromFile to be
    called prior, in order to load the asset library and
    acquire library_id. hapi.getAssetDefinitionParmCounts should
    be called prior to acquire the counts for the sizes of
    the values arrays.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_id:
        Returned by hapi.loadAssetLibraryFromFile.
    

    asset_name:
        Name of the asset to get the parm counts for.
    

    int_start:
        First index of range for int_values_array. Must be at
        least 0 and at most int_value_count - 1 acquired from
        hapi.getAssetDefinitionParmCounts.
    

    int_length:
        Must be at least 0 and at most int_value_count - int_start
        acquired from hapi.getAssetDefinitionParmCounts.
    

    float_start:
        First index of range for float_values_array. Must be at
        least 0 and at most float_value_count - 1 acquired from
        hapi.getAssetDefinitionParmCounts.
    

    float_length:
        Must be at least 0 and at most float_value_count -
        float_start acquired from
        hapi.getAssetDefinitionParmCounts.
    

    string_evaluate:
        Whether or not to evaluate the string expressions.
        For example, the string "$F" would evaluate to the
        current frame number. So, passing in evaluate = False
        would give you back the string "$F" and passing
        in evaluate = True would give you back "1" (assuming
        the current frame is 1).
    

    string_start:
        First index of range for string_values_array. Must be at
        least 0 and at most string_value_count - 1 acquired from
        hapi.getAssetDefinitionParmCounts.
    

    string_length:
        Must be at least 0 and at most string_value_count -
        string_start acquired from
        hapi.getAssetDefinitionParmCounts.
    

    choice_start:
        First index of range for choice_values_array. Must be at
        least 0 and at most choice_value_count - 1 acquired from
        hapi.getAssetDefinitionParmCounts.
    

    choice_length:
        Must be at least 0 and at most choice_value_count -
        choice_start acquired from
        hapi.getAssetDefinitionParmCounts.
    
    '''
def getAssetInfo(session: Session | None, node_id: int) -> AssetInfo:
    """getAssetInfo(session: hapi.Session | None = None, node_id: int) -> hapi.AssetInfo

    Fill an asset_info struct from a node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    
    """
def getAssetLibraryFilePath(session: Session, asset_library_id: int) -> int:
    """getAssetLibraryFilePath(session: hapi.Session, asset_library_id: int) -> int

    Gets the hapi.HAPI_StringHandle for the file path of a loaded asset
    library.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    asset_library_id:
        The hapi.HAPI_AssetLibraryId of the asset library.
    
    """
def getAssetLibraryIds(session: Session | None, start: int, length: int) -> list[int]:
    """getAssetLibraryIds(session: hapi.Session | None = None, start: int, length: int) -> list

    Gets the hapi.HAPI_AssetLibraryId for HDAs that are loaded in Houdini.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    start:
        First index from the list of hapi.HAPI_AssetLibraryId to
        return. Must be at least 0 and at most count - 1 where count
        is the value returned by hapi.getLoadedAssetLibraryCount.
    

    length:
        The number of hapi.HAPI_AssetLibraryId to return. Must be at
        least 0 and at most count - start where count is the value
        returned by hapi.getLoadedAssetLibraryCount.
    
    """
def getAttributeDictionaryArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int]]:
    """getAttributeDictionaryArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute dictionary data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.

    Dictionary data is serialized as JSON-encoded strings.
    Note that the string handles returned are only valid until
    the next time this function is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for the.
        totalArrayElements. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
        Warning: The string handles should be used to retrieve the strings
        immediately and are invalidated when another call to get
        this attribute's data is made.
    
    """
def getAttributeDictionaryArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int], int]:
    """getAttributeDictionaryArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute dictionary data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeDictionaryArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32], int]:
    """getAttributeDictionaryArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute dictionary data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeDictionaryArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32]]:
    """getAttributeDictionaryArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute dictionary data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.

    Dictionary data is serialized as JSON-encoded strings.
    Note that the string handles returned are only valid until
    the next time this function is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for the.
        totalArrayElements. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
        Warning: The string handles should be used to retrieve the strings
        immediately and are invalidated when another call to get
        this attribute's data is made.
    
    """
def getAttributeDictionaryData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, start: int, length: int) -> list[int]:
    """getAttributeDictionaryData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, start: int = 0, length: int) -> list

    Get attribute dictionary data.

    Dictionary data is serialized as JSON-encoded strings.
    Note that the string handles returned are only valid until the next
    time this function is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
        Warning: The string handles should be used to retrieve the strings
        immediately and are invalidated when another call to get
        this attribute's data is made.
    
    """
def getAttributeDictionaryDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, start: int, length: int) -> tuple[list[int], int]:
    """getAttributeDictionaryDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, start: int = 0, length: int) -> tuple

    Get attribute dictionary data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloat64ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[float], list[int]]:
    """getAttributeFloat64ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 64-bit float data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for the.
        totalArrayElements. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloat64ArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[float], list[int], int]:
    """getAttributeFloat64ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 64-bit float data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloat64ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[NDArray[numpy.float64], NDArray[numpy.int32], int]:
    """getAttributeFloat64ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 64-bit float data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloat64ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[NDArray[numpy.float64], NDArray[numpy.int32]]:
    """getAttributeFloat64ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 64-bit float data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for the.
        totalArrayElements. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloat64Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> list[float]:
    """getAttributeFloat64Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> list

    Get 64-bit attribute float data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloat64DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[list[float], int]:
    """getAttributeFloat64DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute 64-bit float data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloat64DataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[NDArray[numpy.float64], int]:
    """getAttributeFloat64DataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute 64-bit float data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloat64Data_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> NDArray[numpy.float64]:
    """getAttributeFloat64Data_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> numpy.ndarray[dtype=float64]

    Get 64-bit attribute float data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloatArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[float], list[int]]:
    """getAttributeFloatArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute float data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloatArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[float], list[int], int]:
    """getAttributeFloatArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute float data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloatArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[NDArray[numpy.float32], NDArray[numpy.int32], int]:
    """getAttributeFloatArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute float data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloatArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[NDArray[numpy.float32], NDArray[numpy.int32]]:
    """getAttributeFloatArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute float data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloatData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> list[float]:
    """getAttributeFloatData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> list

    Get attribute float data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloatDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[list[float], int]:
    """getAttributeFloatDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute float data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloatDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[NDArray[numpy.float32], int]:
    """getAttributeFloatDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute float data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeFloatData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> NDArray[numpy.float32]:
    """getAttributeFloatData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> numpy.ndarray[dtype=float32]

    Get attribute float data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInfo(session: Session | None, node_id: int, part_id: int, name: str, owner: attributeOwner) -> AttributeInfo:
    """getAttributeInfo(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, owner: hapi.attributeOwner) -> hapi.AttributeInfo

    Get the attribute info struct for the attribute specified by name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    owner:
        Attribute owner.
    
    """
def getAttributeInt16ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int]]:
    """getAttributeInt16ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 16-bit integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt16ArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int], int]:
    """getAttributeInt16ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 16-bit integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt16ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32], int]:
    """getAttributeInt16ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 16-bit integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt16ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32]]:
    """getAttributeInt16ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 16-bit integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt16Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> list[int]:
    """getAttributeInt16Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> list

    Get attribute 16-bit integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt16DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[list[int], int]:
    """getAttributeInt16DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute 16-bit integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt64ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int]]:
    """getAttributeInt64ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 64-bit integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt64ArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int], int]:
    """getAttributeInt64ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 64-bit integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt64ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[NDArray[numpy.int64], NDArray[numpy.int32], int]:
    """getAttributeInt64ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 64-bit integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt64ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[NDArray[numpy.int64], NDArray[numpy.int32]]:
    """getAttributeInt64ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 64-bit integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt64Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> list[int]:
    """getAttributeInt64Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> list

    Get attribute 64-bit integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt64DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[list[int], int]:
    """getAttributeInt64DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute 64-bit integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt64DataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[NDArray[numpy.int64], int]:
    """getAttributeInt64DataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute 64-bit integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt64Data_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> NDArray[numpy.int64]:
    """getAttributeInt64Data_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> numpy.ndarray[dtype=int64]

    Get attribute 64-bit integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt8ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int]]:
    """getAttributeInt8ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 8-bit integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt8ArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int], int]:
    """getAttributeInt8ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 8-bit integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt8ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32], int]:
    """getAttributeInt8ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 8-bit integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt8ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32]]:
    """getAttributeInt8ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute 8-bit integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt8Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> list[int]:
    """getAttributeInt8Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> list

    Get attribute 8-bit integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeInt8DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[list[int], int]:
    """getAttributeInt8DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute 8-bit integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeIntArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int]]:
    """getAttributeIntArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeIntArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int], int]:
    """getAttributeIntArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeIntArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[NDArray[numpy.int32], NDArray[numpy.int32], int]:
    """getAttributeIntArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeIntArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[NDArray[numpy.int32], NDArray[numpy.int32]]:
    """getAttributeIntArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeIntData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> list[int]:
    """getAttributeIntData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> list

    Get attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeIntDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[list[int], int]:
    """getAttributeIntDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeIntDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[NDArray[numpy.int32], int]:
    """getAttributeIntDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeIntData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> NDArray[numpy.int32]:
    """getAttributeIntData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> numpy.ndarray[dtype=int32]

    Get attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeNames(session: Session | None, node_id: int, part_id: int, owner: attributeOwner, count: int) -> list[int]:
    """getAttributeNames(session: hapi.Session | None = None, node_id: int, part_id: int, owner: hapi.attributeOwner, count: int) -> list

    Get list of attribute names by attribute owner. Note that the
    name string handles are only valid until the next time this
    function is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    owner:
        The hapi.attributeOwner enum value specifying the
        owner of the attribute.
    

    count:
        Sanity check count. Must be equal to the appropriate
        attribute owner type count in hapi.PartInfo.
    
    """
def getAttributeStringArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int]]:
    """getAttributeStringArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute string data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.
    Note that the string handles returned are only valid until
    the next time this function is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for the.
        totalArrayElements. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
        Warning: The string handles should be used to retrieve the strings
        immediately and are invalidated when another call to get
        this attribute's data is made.
    
    """
def getAttributeStringArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int], int]:
    """getAttributeStringArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute string data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeStringArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32], int]:
    """getAttributeStringArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute string data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeStringArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32]]:
    """getAttributeStringArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute string data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.
    Note that the string handles returned are only valid until
    the next time this function is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for the.
        totalArrayElements. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
        Warning: The string handles should be used to retrieve the strings
        immediately and are invalidated when another call to get
        this attribute's data is made.
    
    """
def getAttributeStringData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, start: int, length: int) -> list[int]:
    """getAttributeStringData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, start: int = 0, length: int) -> list

    Get attribute string data. Note that the string handles
    returned are only valid until the next time this function
    is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
        Warning: The string handles should be used to retrieve the strings
        immediately and are invalidated when another call to get
        this attribute's data is made.
    
    """
def getAttributeStringDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, start: int, length: int) -> tuple[list[int], int]:
    """getAttributeStringDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, start: int = 0, length: int) -> tuple

    Get attribute string data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeUInt8ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int]]:
    """getAttributeUInt8ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute unsigned 8-bit integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeUInt8ArrayDataAsync(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], list[int], int]:
    """getAttributeUInt8ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute unsigned 8-bit integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeUInt8ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, attr_name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32], int]:
    """getAttributeUInt8ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, attr_name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute unsigned 8-bit integer data asynchronously.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    attr_name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeUInt8ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_length: int, start: int, sizes_fixed_length: int) -> tuple[list[int], NDArray[numpy.int32]]:
    """getAttributeUInt8ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_length: int, start: int = 0, sizes_fixed_length: int) -> tuple

    Get array attribute unsigned 8-bit integer data.
    Each entry in an array attribute can have varying array lengths.
    Therefore the array values are returned as a flat array, with
    another sizes array containing the lengths of each array entry.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_fixed_length:
        Must be hapi.AttributeInfo.totalArrayElements.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeUInt8Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> list[int]:
    """getAttributeUInt8Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> list

    Get attribute unsigned 8-bit integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAttributeUInt8DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, stride: int, start: int, length: int) -> tuple[list[int], int]:
    """getAttributeUInt8DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, stride: int, start: int = 0, length: int) -> tuple

    Get attribute unsigned 8-bit integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    stride:
        Specifies how many items to skip over for each element.
        With a stride of -1, the stride will be set to
        attr_info->tuple_size. Otherwise, the stride will be
        set to the maximum of attr_info->tuple_size and
        stride.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
        Note, if 0 is passed for length, the function will just
        do nothing and return hapi.result.Success.
    
    """
def getAvailableAssetCount(session: Session | None, library_id: int) -> int:
    """getAvailableAssetCount(session: hapi.Session | None = None, library_id: int) -> int

    Get the number of assets contained in an asset library.
    You should call hapi.loadAssetLibraryFromFile prior to
    get a library_id.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_id:
        Returned by hapi.loadAssetLibraryFromFile.
    
    """
def getAvailableAssets(session: Session | None, library_id: int, asset_count: int) -> list[int]:
    '''getAvailableAssets(session: hapi.Session | None = None, library_id: int, asset_count: int) -> list

    Get the names of the assets contained in an asset library.

    The asset names will contain additional information about
    the type of asset, namespace, and version, along with the
    actual asset name. For example, if you have an Object type
    asset, in the "hapi" namespace, of version 2.0, named
    "foo", the asset name returned here will be:
    hapi::Object/foo::2.0

    You should call hapi.loadAssetLibraryFromFile prior to
    get a library_id. Then, you should call
    hapi.getAvailableAssetCount to get the number of assets to
    know how large of a string handles array you need to allocate.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_id:
        Returned by hapi.loadAssetLibraryFromFile.
    

    asset_count:
        Should be the same or less than the value returned by
        hapi.getAvailableAssetCount.
    
    '''
def getBoxInfo(session: Session | None, geo_node_id: int, part_id: int) -> BoxInfo:
    """getBoxInfo(session: hapi.Session | None = None, geo_node_id: int, part_id: int) -> hapi.BoxInfo

    Get the box info on a geo part (if the part is a box).



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    geo_node_id:
        The geo node id.
    

    part_id:
        The part id of the
    
    """
def getCacheProperty(session: Session | None, cache_name: str, cache_property: cacheProperty) -> int:
    """getCacheProperty(session: hapi.Session | None = None, cache_name: str, cache_property: hapi.cacheProperty) -> int

    Lets you inspect specific properties of the different memory
    caches in the current Houdini context.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    cache_name:
        Cache name from hapi.getActiveCacheNames.
    

    cache_property:
        The specific property of the cache to get the value for.
    
    """
def getCameraInfo(session: Session | None, node_id: int, part_id: int) -> CameraInfo:
    """getCameraInfo(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.CameraInfo

    Retrieves the camera parms for a SOP camera primitive



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id. The hapi.PartInfo.type must be
        hapi.partType.Camera.
    
    """
def getCameraTransform(session: Session | None, node_id: int, part_id: int) -> Transform:
    """getCameraTransform(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.Transform

    Retrieves the transform of the SOP camera primitive. Scale is always
    locked to [1, 1, 1].



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id. The hapi.PartInfo.type must be
        hapi.partType.Camera.
    
    """
def getComposedChildNodeList(session: Session | None, parent_node_id: int, count: int) -> list[int]:
    """getComposedChildNodeList(session: hapi.Session | None = None, parent_node_id: int, count: int) -> list

    Get the composed list of child node ids from the previous call
    to hapi.composeChildNodeList.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The node id of the parent node.
    

    count:
        The number of children in the composed list. MUST match
        the count returned by hapi.composeChildNodeList.
    
    """
def getComposedNodeCookResult(session: Session | None, length: int) -> str:
    """getComposedNodeCookResult(session: hapi.Session | None = None, length: int) -> str

    Return cook result string message on a single node.

    You MUST call hapi.composeNodeCookResult before calling
    hapi.getComposedNodeCookResult because
    hapi.getComposedNodeCookResult will
    not return the real result string and instead return a
    cached version of the string that was created inside
    hapi.composeNodeCookResult. The reason for this is that
    the length of the real status string may change between
    the call to hapi.composeNodeCookResult and the call to
    hapi.getComposedNodeCookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    length:
        Length of the string buffer (must match size of
        `string_value` - so including None terminator).
    
    """
def getComposedObjectList(session: Session | None, parent_node_id: int, start: int, length: int) -> list[ObjectInfo]:
    """getComposedObjectList(session: hapi.Session | None = None, parent_node_id: int, start: int = 0, length: int) -> list

    Fill an array of hapi.ObjectInfo structs.

    This is best used with hapi.composeObjectList with.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The parent node id.
    

    start:
        At least 0 and at most object_count returned by
        hapi.composeObjectList.
    

    length:
        Given object_count returned by
        hapi.composeObjectList length should be at least
        0 and at most object_count - start.
    
    """
def getComposedObjectTransforms(session: Session | None, parent_node_id: int, rst_order: rstOrder, start: int, length: int) -> list[Transform]:
    """getComposedObjectTransforms(session: hapi.Session | None = None, parent_node_id: int, rst_order: hapi.rstOrder, start: int = 0, length: int) -> list

    Fill an array of hapi.Transform structs.

    This is best used with hapi.composeObjectList with.

    Note that these transforms will be relative to the
    parent_node_id originally given to hapi.composeObjectList
    and expected to be the same with this call. If parent_node_id
    is not an OBJ node, the transforms will be given as they are on
    the object node itself.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        The parent node id. The object transforms will be
        relative to this node unless this node is not an OBJ.
    

    rst_order:
        The order of application of translation, rotation and
        scale.
    

    start:
        At least 0 and at most object_count returned by
        hapi.composeObjectList.
    

    length:
        Given object_count returned by
        hapi.composeObjectList length should be at least
        0 and at most object_count - start.
    
    """
def getCompositorOptions(session: Session | None = ...) -> CompositorOptions:
    """getCompositorOptions(session: hapi.Session | None = None) -> hapi.CompositorOptions

    Gets the global compositor options.


    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getConnectionError(length: int, clear: bool) -> str:
    """getConnectionError(length: int, clear: bool) -> str

    Return the connection error message.

    You MUST call hapi.getConnectionErrorLength before calling
    this to get the correct string length.

    Only available when using Thrift connections.



    length:
        Length of the string buffer (must match size of
        string_value - so including None terminator).
        Use hapi.getConnectionErrorLength to get this length.
    

    clear:
        If true, will clear the error when hapi.result.Success
        is returned.
    
    """
def getConnectionErrorLength() -> int:
    """getConnectionErrorLength() -> int

    Return the length of string buffer storing connection error
    message.


    Only available when using Thrift connections.

    """
def getCookingCurrentCount(session: Session | None = ...) -> int:
    """getCookingCurrentCount(session: hapi.Session | None = None) -> int

    Get current number of nodes that have already cooked in the
    current session. Note that this is a very crude approximation
    of the cooking progress - it may never make it to 100% or it
    might spend another hour at 100%. Use hapi.getStatusString
    to get a better idea of progress if this number gets stuck.


    NOTE: This function is deprecated.

    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getCookingTotalCount(session: Session | None = ...) -> int:
    """getCookingTotalCount(session: hapi.Session | None = None) -> int

    Get total number of nodes that need to cook in the current
    session.


    NOTE: This function is deprecated.

    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getCurveCounts(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> list[int]:
    """getCurveCounts(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> list

    Retrieve the number of vertices for each curve in the part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' counts to retrieve.
    
    """
def getCurveCounts_np(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> NDArray[numpy.int32]:
    """getCurveCounts_np(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> numpy.ndarray[dtype=int32]

    Retrieve the number of vertices for each curve in the part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' counts to retrieve.
    
    """
def getCurveInfo(session: Session | None, node_id: int, part_id: int) -> CurveInfo:
    """getCurveInfo(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.CurveInfo

    Retrieve any meta-data about the curves, including the
    curve's type, order, and periodicity.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    
    """
def getCurveKnots(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> list[float]:
    """getCurveKnots(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> list

    Retrieve the knots of the curves in this part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' knots to retrieve. The
        length of all the knots on a single curve is
        the order of that curve plus the number of
        vertices (see hapi.getCurveOrders
        and hapi.getCurveCounts.
    
    """
def getCurveKnots_np(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> NDArray[numpy.float32]:
    """getCurveKnots_np(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> numpy.ndarray[dtype=float32]

    Retrieve the knots of the curves in this part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' knots to retrieve. The
        length of all the knots on a single curve is
        the order of that curve plus the number of
        vertices (see hapi.getCurveOrders
        and hapi.getCurveCounts.
    
    """
def getCurveOrders(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> list[int]:
    """getCurveOrders(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> list

    Retrieve the orders for each curve in the part if the
    curve has varying order.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' orders to retrieve.
    
    """
def getCurveOrders_np(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> NDArray[numpy.int32]:
    """getCurveOrders_np(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> numpy.ndarray[dtype=int32]

    Retrieve the orders for each curve in the part if the
    curve has varying order.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' orders to retrieve.
    
    """
def getDisplayGeoInfo(session: Session | None, object_node_id: int) -> GeoInfo:
    """getDisplayGeoInfo(session: hapi.Session | None = None, object_node_id: int) -> hapi.GeoInfo

    Get the display geo (SOP) node inside an Object node. If there
    there are multiple display SOP nodes, only the first one is
    returned. If the node is a display SOP itself, even if a network,
    it will return its own geo info. If the node is a SOP but not
    a network and not the display SOP, this function will fail.

    The above implies that you can safely call this function on both
    OBJ and SOP asset nodes and get the same (equivalent) geometry
    display node back. SOP asset nodes will simply return themselves.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    object_node_id:
        The object node id.
    
    """
def getEdgeCountOfEdgeGroup(session: Session | None, node_id: int, part_id: int, group_name: str) -> int:
    """getEdgeCountOfEdgeGroup(session: hapi.Session | None = None, node_id: int, part_id: int, group_name: str) -> int

    Gets the number of edges that belong to an edge group on a geometry
    part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        The part id.
    

    group_name:
        The name of the edge group.
    
    """
def getEnvInt(int_type: envIntType) -> int:
    """getEnvInt(int_type: hapi.envIntType) -> int

    Gives back a certain environment integers like version number.
    Note that you do not need a session for this. These constants
    are hard-coded in all HAPI implementations, including HARC and
    HAPIL. This should be the first API you call to determine if
    any future API calls will mismatch implementation.



    int_type:
        One of hapi.envIntType.
    
    """
def getFaceCounts(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> list[int]:
    """getFaceCounts(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> list

    Get the array of faces where the nth integer in the array is
    the number of vertices the nth face has.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.faceCount - 1.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.faceCount - `start`.
    
    """
def getFaceCounts_np(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> NDArray[numpy.int32]:
    """getFaceCounts_np(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> numpy.ndarray[dtype=int32]

    Get the array of faces where the nth integer in the array is
    the number of vertices the nth face has.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.faceCount - 1.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.faceCount - `start`.
    
    """
def getFirstVolumeTile(session: Session | None, node_id: int, part_id: int) -> VolumeTileInfo:
    """getFirstVolumeTile(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.VolumeTileInfo

    Iterate through a volume based on 8x8x8 sections of the volume
    Start iterating through the value of the volume at part_id.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    
    """
def getGeoInfo(session: Session | None, node_id: int) -> GeoInfo:
    """getGeoInfo(session: hapi.Session | None = None, node_id: int) -> hapi.GeoInfo

    Get the geometry info struct (::HAPI_GeoInfo) on a SOP node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    
    """
def getGeoSize(session: Session | None, node_id: int, format: str) -> int:
    '''getGeoSize(session: hapi.Session | None = None, node_id: int, format: str) -> int

    Cache the current state of the geo to memory, given the
    format, and return the size. Use this size with your call
    to hapi.saveGeoToMemory to copy the cached geo to your
    buffer. It is guaranteed that the size will not change between
    your call to hapi.getGeoSize and hapi.saveGeoToMemory.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    format:
        The file format, ie. ".obj", ".bgeo.sc" etc.
    
    '''
def getGroupCountOnPackedInstancePart(session: Session | None, node_id: int, part_id: int) -> tuple[int, int]:
    """getGroupCountOnPackedInstancePart(session: hapi.Session | None = None, node_id: int, part_id: int) -> tuple

    Get group counts for a specific packed instanced part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id. (should be a packed primitive)
    
    """
def getGroupMembership(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_name: str, start: int, length: int) -> tuple[bool, list[int]]:
    """getGroupMembership(session: hapi.Session | None = None, node_id: int, part_id: int, group_type: hapi.groupType, group_name: str, start: int = 0, length: int) -> tuple

    Get group membership.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    group_type:
        The group type.
    

    group_name:
        The group name.
    

    start:
        Start offset into the membership array. Must be
        less than HAPI_PartInfo_GetElementCountByGroupType when
        it is a point or primitive group. When getting the
        membership information for an edge group, this argument must
        be less than the size returned by
        hapi.getEdgeCountOfEdgeGroup * 2 - 1.
    

    length:
        Should be less than or equal to the size
        of `membership_array`.
    
    """
def getGroupMembershipOnPackedInstancePart(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_name: str, start: int, length: int) -> tuple[bool, list[int]]:
    """getGroupMembershipOnPackedInstancePart(session: hapi.Session | None = None, node_id: int, part_id: int, group_type: hapi.groupType, group_name: str, start: int = 0, length: int) -> tuple

    Get group membership for a packed instance part
    This functions allows you to get the group membership for a specific
    packed primitive part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id. (should be a packed primitive)
    

    group_type:
        The group type.
    

    group_name:
        The group name.
    

    start:
        Start offset into the membership array. Must be
        less than HAPI_PartInfo_GetElementCountByGroupType.
    

    length:
        Should be less than or equal to the size
        of `membership_array`.
    
    """
def getGroupMembershipOnPackedInstancePart_np(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_name: str, start: int, length: int) -> tuple[bool, NDArray[numpy.int32]]:
    """getGroupMembershipOnPackedInstancePart_np(session: hapi.Session | None = None, node_id: int, part_id: int, group_type: hapi.groupType, group_name: str, start: int = 0, length: int) -> tuple

    Get group membership for a packed instance part
    This functions allows you to get the group membership for a specific
    packed primitive part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id. (should be a packed primitive)
    

    group_type:
        The group type.
    

    group_name:
        The group name.
    

    start:
        Start offset into the membership array. Must be
        less than HAPI_PartInfo_GetElementCountByGroupType.
    

    length:
        Should be less than or equal to the size
        of `membership_array`.
    
    """
def getGroupMembership_np(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_name: str, start: int, length: int) -> tuple[bool, NDArray[numpy.int32]]:
    """getGroupMembership_np(session: hapi.Session | None = None, node_id: int, part_id: int, group_type: hapi.groupType, group_name: str, start: int = 0, length: int) -> tuple

    Get group membership.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    group_type:
        The group type.
    

    group_name:
        The group name.
    

    start:
        Start offset into the membership array. Must be
        less than HAPI_PartInfo_GetElementCountByGroupType when
        it is a point or primitive group. When getting the
        membership information for an edge group, this argument must
        be less than the size returned by
        hapi.getEdgeCountOfEdgeGroup * 2 - 1.
    

    length:
        Should be less than or equal to the size
        of `membership_array`.
    
    """
def getGroupNames(session: Session | None, node_id: int, group_type: groupType, group_count: int) -> list[int]:
    """getGroupNames(session: hapi.Session | None = None, node_id: int, group_type: hapi.groupType, group_count: int) -> list

    Get group names for an entire geo. Please note that this
    function is NOT per-part, but it is per-geo. The companion
    function hapi.getGroupMembership IS per-part. Also keep
    in mind that the name string handles are only
    valid until the next time this function is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    group_type:
        The group type.
    

    group_count:
        Sanity check. Should be less than or equal to the size
        of `group_names`.
    
    """
def getGroupNamesOnPackedInstancePart(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_count: int) -> list[int]:
    """getGroupNamesOnPackedInstancePart(session: hapi.Session | None = None, node_id: int, part_id: int, group_type: hapi.groupType, group_count: int) -> list

    Get the group names for a packed instance part
    This functions allows you to get the group name for a specific
    packed primitive part.
    Keep in mind that the name string handles are only
    valid until the next time this function is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id. (should be a packed primitive)
    

    group_type:
        The group type.
    

    group_count:
        Sanity check. Should be less than or equal to the size
        of `group_names`.
    
    """
def getHIPFileNodeCount(session: Session, id: int) -> int:
    """getHIPFileNodeCount(session: hapi.Session, id: int) -> int

    Gets the number of nodes that were created as a result of loading a
    .hip file



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    id:
        The HIP file id.
    
    """
def getHIPFileNodeIds(session: Session, id: int, length: int) -> int:
    """getHIPFileNodeIds(session: hapi.Session, id: int, length: int) -> int

    Fills an array of hapi.HAPI_NodeId of nodes that were created as a
    result of loading the HIP file specified by the hapi.HAPI_HIPFileId



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    id:
        The HIP file id.
    

    length:
        The number of hapi.HAPI_NodeId to be stored. This should be at
        least 0 and at most the count provided by
        hapi.getHIPFileNodeCount
    """
def getHandleBindingInfo(session: Session | None, node_id: int, handle_index: int, start: int, length: int) -> list[HandleBindingInfo]:
    """getHandleBindingInfo(session: hapi.Session | None = None, node_id: int, handle_index: int, start: int = 0, length: int) -> list

    Fill an array of hapi.HandleBindingInfo structs with information
    about the binding of a particular handle on the given node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    handle_index:
        The index of the handle, from 0 to handleCount - 1
        from the call to hapi.getAssetInfo.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.HandleInfo.bindingsCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.HandleInfo.bindingsCount - start.
    
    """
def getHandleInfo(session: Session | None, node_id: int, start: int, length: int) -> list[HandleInfo]:
    """getHandleInfo(session: hapi.Session | None = None, node_id: int, start: int = 0, length: int) -> list

    Fill an array of hapi.HandleInfo structs with information
    about every exposed user manipulation handle on the node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AssetInfo.handleCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.AssetInfo.handleCount - start.
    
    """
def getHeightFieldData(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> list[float]:
    """getHeightFieldData(session: hapi.Session | None = None, node_id: int, part_id: int, start: int, length: int) -> list

    Get the height field data for a terrain volume as a flattened
    2D array of float heights. Should call hapi.getVolumeInfo
    first to make sure the volume info is initialized.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        The start at least 0 and at most
        ( hapi.VolumeInfo.xLength * hapi.VolumeInfo.yLength )
        - `length`.
    

    length:
        The length should be at least 1 or at most
        ( hapi.VolumeInfo.xLength * hapi.VolumeInfo.yLength )
        - `start`.
    
    """
def getHeightFieldData_np(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> NDArray[numpy.float32]:
    """getHeightFieldData_np(session: hapi.Session | None = None, node_id: int, part_id: int, start: int, length: int) -> numpy.ndarray[dtype=float32]

    Get the height field data for a terrain volume as a flattened
    2D array of float heights. Should call hapi.getVolumeInfo
    first to make sure the volume info is initialized.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        The start at least 0 and at most
        ( hapi.VolumeInfo.xLength * hapi.VolumeInfo.yLength )
        - `length`.
    

    length:
        The length should be at least 1 or at most
        ( hapi.VolumeInfo.xLength * hapi.VolumeInfo.yLength )
        - `start`.
    
    """
def getImageFilePath(session: Session | None, material_node_id: int, image_file_format_name: str, image_planes: str, destination_folder_path: str, destination_file_name: str, texture_parm_id: int) -> int:
    """getImageFilePath(session: hapi.Session | None = None, material_node_id: int, image_file_format_name: str, image_planes: str, destination_folder_path: str, destination_file_name: str, texture_parm_id: int) -> int

    Get the file name that this image would be saved to

    Check to see what file path hapi.extractImageToFile would have
    saved to given the same parms. Perhaps you might wish to see
    if it already exists before extracting.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    

    image_file_format_name:
        The image file format name you wish the image to be
        extracted as. See hapi.extractImageToFile for more information.
    

    image_planes:
        The image planes you wish to extract into the file.
        Multiple image planes should be separated by spaces.
    

    destination_folder_path:
        The folder where the image file should be created.
    

    destination_file_name:
        Optional parameter to overwrite the name of the
        extracted texture file. See hapi.extractImageToFile for more information.
    

    texture_parm_id:
        The index in the parameter list of the material node.
        of the parameter containing the texture map file path
    
    """
def getImageInfo(session: Session | None, material_node_id: int) -> ImageInfo:
    """getImageInfo(session: hapi.Session | None = None, material_node_id: int) -> hapi.ImageInfo

    Get information about the image that was just rendered, like
    resolution and default file format. This information will be
    used when extracting planes to an image.

    Note that you must call one of hapi.renderTextureToImage
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    first for this method call to make sense.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    
    """
def getImageMemoryBuffer(session: Session | None, material_node_id: int, length: int) -> list[str]:
    """getImageMemoryBuffer(session: hapi.Session | None = None, material_node_id: int, length: int) -> list

    Fill your allocated buffer with the just extracted
    image buffer.

    Note that you must call one of hapi.renderTextureToImage
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    first for this method call to make sense.

    Also note that you must call hapi.extractImageToMemory
    first in order to perform the extraction and get the
    extracted image buffer size that you need to know how much
    memory to allocated to fit your extracted image.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    

    length:
        Sanity check. This size should be the same as the
        size allocated for the buffer passed in and should
        be at least as large as the buffer_size returned by
        the call to hapi.extractImageToMemory.
    
    """
def getImageMemoryBuffer_np(session: Session | None, material_node_id: int, length: int) -> NDArray[numpy.int8]:
    """getImageMemoryBuffer_np(session: hapi.Session | None = None, material_node_id: int, length: int) -> numpy.ndarray[dtype=int8]

    Fill your allocated buffer with the just extracted
    image buffer.

    Note that you must call one of hapi.renderTextureToImage
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    first for this method call to make sense.

    Also note that you must call hapi.extractImageToMemory
    first in order to perform the extraction and get the
    extracted image buffer size that you need to know how much
    memory to allocated to fit your extracted image.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    

    length:
        Sanity check. This size should be the same as the
        size allocated for the buffer passed in and should
        be at least as large as the buffer_size returned by
        the call to hapi.extractImageToMemory.
    
    """
def getImagePlaneCount(session: Session | None, material_node_id: int) -> int:
    """getImagePlaneCount(session: hapi.Session | None = None, material_node_id: int) -> int

    Get the number of image planes for the just rendered image.

    Note that you must call one of hapi.renderTextureToImage
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    first for this method call to make sense.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    
    """
def getImagePlanes(session: Session | None, material_node_id: int, image_plane_count: int) -> list[int]:
    """getImagePlanes(session: hapi.Session | None = None, material_node_id: int, image_plane_count: int) -> list

    Get the names of the image planes of the just rendered image.

    Note that you must call one of hapi.renderTextureToImage
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    first for this method call to make sense.

    You should also call hapi.getImagePlaneCount first to get
    the total number of image planes so you know how large the
    image_planes string handle array should be.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    

    image_plane_count:
        The number of image planes to get names for. This
        must be less than or equal to the count returned
        by hapi.getImagePlaneCount.
    
    """
def getInputCurveInfo(session: Session | None, node_id: int, part_id: int) -> InputCurveInfo:
    """getInputCurveInfo(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.InputCurveInfo

    Retrieve meta-data about the input curves, including the
    curve's type, order, and whether or not the curve is closed and reversed.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    
    """
def getInstanceTransformsOnPart(session: Session | None, node_id: int, part_id: int, rst_order: rstOrder, start: int, length: int) -> list[Transform]:
    """getInstanceTransformsOnPart(session: hapi.Session | None = None, node_id: int, part_id: int, rst_order: hapi.rstOrder, start: int = 0, length: int) -> list

    Fill an array of hapi.Transform structs with the transforms
    of each instance of this instancer object for a given part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The object node id.
    

    part_id:
        The part id.
    

    rst_order:
        The order of application of translation, rotation and
        scale.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.pointCount - 1. This is the 0th
        part of the display geo of the instancer object node.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.pointCount - `start`. This is the 0th
        part of the display geo of the instancer object node.
    
    """
def getInstancedObjectIds(session: Session | None, object_node_id: int, start: int, length: int) -> list[int]:
    """getInstancedObjectIds(session: hapi.Session | None = None, object_node_id: int, start: int = 0, length: int) -> list

    Get the node ids for the objects being instanced by an
    Instance OBJ node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    object_node_id:
        The object node id.
    

    start:
        At least 0 and at most object_count returned by
        hapi.composeObjectList.
    

    length:
        Given object_count returned by
        hapi.composeObjectList length should be at least
        0 and at most object_count - start.
    
    """
def getInstancedPartIds(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> list[int]:
    """getInstancedPartIds(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> list

    Get the part ids that this instancer part is instancing.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The instancer part id.
    

    start:
        Should be less than `part_id's`
        hapi.PartInfo.instancedPartCount but more than or
        equal to 0.
    

    length:
        Should be less than `part_id's`
        hapi.PartInfo.instancedPartCount - `start`.
    
    """
def getInstancerPartTransforms(session: Session | None, node_id: int, part_id: int, rst_order: rstOrder, start: int, length: int) -> list[Transform]:
    """getInstancerPartTransforms(session: hapi.Session | None = None, node_id: int, part_id: int, rst_order: hapi.rstOrder, start: int = 0, length: int) -> list

    Get the instancer part's list of transforms on which to
    instance the instanced parts you got from
    hapi.getInstancedPartIds.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The instancer part id.
    

    rst_order:
        The order of application of translation, rotation and
        scale.
    

    start:
        Should be less than `part_id's`
        hapi.PartInfo.instanceCount but more than or
        equal to 0.
    

    length:
        Should be less than `part_id's`
        hapi.PartInfo.instanceCount - `start`.
    
    """
def getJobStatus(session: Session | None, job_id: int) -> jobStatus:
    """getJobStatus(session: hapi.Session | None = None, job_id: int) -> hapi.jobStatus

    Get status of a job.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    job_id:
        The id assigned to the job. It must equal to the index
        assigned through a previous call to an asynchronous HAPI
        method.
    
    """
def getLoadedAssetLibraryCount(session: Session | None = ...) -> int:
    """getLoadedAssetLibraryCount(session: hapi.Session | None = None) -> int

    Gets the number of HDAs that have been loaded by Houdini.

    This only includes HDAs that have been loaded from disk.
    Embedded HDAs will be excluded.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getManagerNodeId(session: Session | None, node_type: nodeType) -> int:
    """getManagerNodeId(session: hapi.Session | None = None, node_type: hapi.nodeType) -> int

    Get the root node of a particular network type (ie. OBJ).



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_type:
        The node network type.
    
    """
def getMaterialInfo(session: Session | None, material_node_id: int) -> MaterialInfo:
    """getMaterialInfo(session: hapi.Session | None = None, material_node_id: int) -> hapi.MaterialInfo

    Get the material info.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    
    """
def getMaterialNodeIdsOnFaces(session: Session | None, geometry_node_id: int, part_id: int, start: int, length: int) -> tuple[bool, list[int]]:
    """getMaterialNodeIdsOnFaces(session: hapi.Session | None = None, geometry_node_id: int, part_id: int, start: int = 0, length: int) -> tuple

    Get material ids by face/primitive. The material ids returned
    will be valid as long as the asset is alive. You should query
    this list after every cook to see if the material assignments
    have changed. You should also query each material individually
    using hapi.getMaterialInfo to see if it is dirty and needs
    to be re-imported.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    geometry_node_id:
        The geometry node id.
    

    part_id:
        The part id.
    

    start:
        The starting index into the list of faces from which
        you wish to get the material ids from. Note that
        this should be less than hapi.PartInfo.faceCount.
    

    length:
        The number of material ids you wish to get. Note that
        this should be at most:
        hapi.PartInfo.faceCount - `start`.
    
    """
def getMessageNodeCount(session: Session | None, node_id: int) -> int:
    '''getMessageNodeCount(session: hapi.Session | None = None, node_id: int) -> int

    Get the number of message nodes set in "Type Properties".



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    
    '''
def getMessageNodeIds(session: Session | None, node_id: int, count: int) -> list[int]:
    '''getMessageNodeIds(session: hapi.Session | None = None, node_id: int, count: int) -> list

    Get the ids of message nodes set in the "Type Properties".



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    count:
        The number of message nodes.
    
    '''
def getNextVolumeTile(session: Session | None, node_id: int, part_id: int) -> VolumeTileInfo:
    """getNextVolumeTile(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.VolumeTileInfo

    Iterate through a volume based on 8x8x8 sections of the volume
    Continue iterating through the value of the volume at part_id.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    
    """
def getNodeCookResult(session: Session | None, length: int) -> str:
    """getNodeCookResult(session: hapi.Session | None = None, length: int) -> str

    Return the cook result string that was composed during a call to
    hapi.getNodeCookResultLength.

    You MUST call hapi.getNodeCookResultLength before calling
    hapi.getNodeCookResult because hapi.getNodeCookResult will
    not return the real result and instead returns a cached version of
    the string that was created during the call to
    hapi.getNodeCookResultLength. The reason for this is that the
    length of the real status string may change between the call to
    hapi.getNodeCookResultLength and hapi.getNodeCookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    length:
        Length of the char buffer (must match size of
        `string_value` - so include None terminator).
    
    """
def getNodeCookResultLength(session: Session | None, node_id: int, verbosity: statusVerbosity) -> int:
    """getNodeCookResultLength(session: hapi.Session | None = None, node_id: int, verbosity: hapi.statusVerbosity) -> int

    Gets the length of the cook result string (errors and warnings) of
    a specific node.

    Unlike hapi.composeNodeCookResult this node does not parse
    inside the node network. Only errors, warnings, and messages that
    appear on the specified node will be a part of the cook result
    string.

    You MUST call hapi.getNodeCookResultLength before calling
    hapi.getNodeCookResult because hapi.getNodeCookResult will
    not return the real result and instead returns a cached version of
    the string that was created during the call to
    hapi.getNodeCookResultLength. The reason for this is that the
    length of the real status string may change between the call to
    hapi.getNodeCookResultLength and hapi.getNodeCookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    verbosity:
        Preferred verbosity level.
    
    """
def getNodeFromPath(session: Session | None, parent_node_id: int, path: str) -> int:
    '''getNodeFromPath(session: hapi.Session | None = None, parent_node_id: int, path: str) -> int

    Get the id of the node with the specified path.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    parent_node_id:
        If path does not start with "/", search for the path
        relative to this node. Provide -1 if path is an absolute
        path.
    

    path:
        The path of the node. If the path does not start with "/",
        it is treated as a relative path from the node specified in
        parent_node_id.
    
    '''
def getNodeInfo(session: Session | None, node_id: int) -> NodeInfo:
    """getNodeInfo(session: hapi.Session | None = None, node_id: int) -> hapi.NodeInfo

    Fill an hapi.NodeInfo struct.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    
    """
def getNodeInputName(session: Session | None, node_id: int, input_idx: int) -> int:
    """getNodeInputName(session: hapi.Session | None = None, node_id: int, input_idx: int) -> int

    Get the name of an node's input. This function will return
    a string handle for the name which will be valid (persist)
    until the next call to this function.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    input_idx:
        The input index. Should be between 0 and the
        node_to_query's hapi.NodeInfo.inputCount - 1.
    
    """
def getNodeOutputName(session: Session | None, node_id: int, output_idx: int) -> int:
    """getNodeOutputName(session: hapi.Session | None = None, node_id: int, output_idx: int) -> int

    Get the name of an node's output. This function will return
    a string handle for the name which will be valid (persist)
    until the next call to this function.
    Only COPs and VOPs can have output names - other node types
    will return their node label when this is called



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    output_idx:
        The output index. Should be between 0 and the
        to_node's hapi.NodeInfo.outputCount - 1.
    
    """
def getNodePath(session: Session | None, node_id: int, relative_to_node_id: int) -> int:
    """getNodePath(session: hapi.Session | None = None, node_id: int, relative_to_node_id: int) -> int

    Get the node absolute path in the Houdini node network or a
    relative path any other node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    relative_to_node_id:
        Set this to -1 to get the absolute path of the node_id.
        Otherwise, the path will be relative to this node id.
    
    """
def getNumWorkItems(session: Session | None, node_id: int) -> int:
    """getNumWorkItems(session: hapi.Session | None = None, node_id: int) -> int

    Gets the number of work items that are available on the given node.
    Should be used with hapi.getWorkItems.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    
    """
def getObjectInfo(session: Session | None, node_id: int) -> ObjectInfo:
    """getObjectInfo(session: hapi.Session | None = None, node_id: int) -> hapi.ObjectInfo

    Get the object info on an OBJ node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    
    """
def getObjectTransform(session: Session | None, node_id: int, relative_to_node_id: int, rst_order: rstOrder) -> Transform:
    """getObjectTransform(session: hapi.Session | None = None, node_id: int, relative_to_node_id: int, rst_order: hapi.rstOrder) -> hapi.Transform

    Get the transform of an OBJ node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The object node id.
    

    relative_to_node_id:
        The object node id for the object to which the returned
        transform will be relative to. Pass -1 or the node_id
        to just get the object's local transform.
    

    rst_order:
        The order of application of translation, rotation and
        scale.
    
    """
def getOutputGeoCount(session: Session | None, node_id: int) -> int:
    """getOutputGeoCount(session: hapi.Session | None = None, node_id: int) -> int

    A helper method that gets the number of main geometry outputs inside
    an Object node or SOP node. If the node is an Object node, this
    method will return the cumulative number of geometry outputs for all
    geometry nodes that it contains. When searching for output geometry,
    this method will only consider subnetworks that have their display
    flag enabled.

    This method must be called before hapi.getOutputGeoInfos is
    called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id of the Object or SOP node to get the geometry
        output count of.
    
    """
def getOutputGeoInfos(session: Session | None, node_id: int, count: int) -> list[GeoInfo]:
    """getOutputGeoInfos(session: hapi.Session | None = None, node_id: int, count: int) -> list

    Gets the geometry info structs (::HAPI_GeoInfo) for a node's
    main geometry outputs. This method can only be called after
    hapi.getOutputGeoCount has been called with the same node id.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id of the Object or SOP node to get the output
        geometry info structs (::HAPI_GeoInfo) for.
    

    count:
        Sanity check count. The count must be equal to the count
        returned by the hapi.getOutputGeoCount method.
    """
def getOutputNodeId(session: Session | None, node_id: int, output: int) -> int:
    """getOutputNodeId(session: hapi.Session | None = None, node_id: int, output: int) -> int

    Gets the node id of an output node in a SOP network.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id of a SOP node with at least one output node. The
        total number of node outputs can be found from the node's
        hapi.NodeInfo.outputCount
    

    output:
        The output index. Should be between 0 and the node's
        hapi.NodeInfo.outputCount - 1.
    
    """
def getPDGEvents(session: Session | None, graph_context_id: int, length: int) -> tuple[list[PDG_EventInfo], int, int]:
    """getPDGEvents(session: hapi.Session | None = None, graph_context_id: int, length: int) -> tuple

    Returns PDG events that have been collected. Calling this function
    will remove those events from the queue. Events collection is restarted
    by calls to hapi.cookPDG.




    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    graph_context_id:
        The id of the graph context
    

    length:
        The size of the buffer passed in.
    
    """
def getPDGGraphContextId(session: Session | None, top_node_id: int) -> int:
    """getPDGGraphContextId(session: hapi.Session | None = None, top_node_id: int) -> int

    Get the PDG graph context for the specified TOP node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    top_node_id:
        The id of the TOP node to query its graph context.
    
    """
def getPDGGraphContexts(session: Session | None = ..., start: int = ..., length: int = ...) -> tuple[list[int], list[int]]:
    """getPDGGraphContexts(session: hapi.Session | None = None, start: int = 0, length: int = 0) -> tuple

    Return an array of PDG graph context names and ids, the first
    count names will be returned. These ids can be used
    with hapi.getPDGEvents and hapi.getPDGState. The values
    of the names can be retrieved with hapi.getString.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    start:
        First index of range. Must be at least 0 and at most
        context_count - 1 where context_count is the count
        returned by hapi.getPDGGraphContextsCount
    

    length:
        Given num_contexts returned by hapi.getPDGGraphContextsCount
        length should be at least 0 and at most num_contexts - start.
    """
def getPDGGraphContextsCount(session: Session | None = ...) -> int:
    """getPDGGraphContextsCount(session: hapi.Session | None = None) -> int

    Return the total number of PDG graph contexts found.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getPDGState(session: Session | None, graph_context_id: int) -> int:
    """getPDGState(session: hapi.Session | None = None, graph_context_id: int) -> int

    Gets the state of a PDG graph




    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    graph_context_id:
        The graph context id
    
    """
def getParameters(session: Session | None, node_id: int, start: int, length: int) -> list[ParmInfo]:
    """getParameters(session: hapi.Session | None = None, node_id: int, start: int = 0, length: int) -> list

    Fill an array of hapi.ParmInfo structs with parameter
    information from the asset instance node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmCount - start.
    
    """
def getParmChoiceLists(session: Session | None, node_id: int, start: int, length: int) -> list[ParmChoiceInfo]:
    """getParmChoiceLists(session: hapi.Session | None = None, node_id: int, start: int = 0, length: int) -> list

    Fill an array of hapi.ParmChoiceInfo structs with parameter
    choice list information from the asset instance node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmChoiceCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmChoiceCount - start.
    
    """
def getParmExpression(session: Session | None, node_id: int, parm_name: str, index: int) -> int:
    """getParmExpression(session: hapi.Session | None = None, node_id: int, parm_name: str, index: int) -> int

    Get single integer or float parm expression by name
    or Null string if no expression is present



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    

    index:
        Index within the parameter's values tuple.
    
    """
def getParmFile(session: Session | None, node_id: int, parm_name: str, destination_directory: str, destination_file_name: str) -> bool:
    """getParmFile(session: hapi.Session | None = None, node_id: int, parm_name: str, destination_directory: str, destination_file_name: str) -> bool

    Extract a file specified by path on a parameter. This will copy
    the file to the destination directory from wherever it might be,
    including inside the asset definition or online.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The name of the parameter.
    

    destination_directory:
        The destination directory to copy the file to.
    

    destination_file_name:
        The destination file name.
    
    """
def getParmFloatValue(session: Session | None, node_id: int, parm_name: str, index: int) -> float:
    """getParmFloatValue(session: hapi.Session | None = None, node_id: int, parm_name: str, index: int) -> float

    Get single parm float value by name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    

    index:
        Index within the parameter's values tuple.
    
    """
def getParmFloatValues(session: Session | None, node_id: int, start: int, length: int) -> list[float]:
    """getParmFloatValues(session: hapi.Session | None = None, node_id: int, start: int = 0, length: int) -> list

    Fill an array of parameter float values. This is more efficient
    than calling hapi.getParmFloatValue individually for each
    parameter value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmFloatValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmFloatValueCount - start.
    
    """
def getParmFloatValues_np(session: Session | None, node_id: int, start: int, length: int) -> NDArray[numpy.float32]:
    """getParmFloatValues_np(session: hapi.Session | None = None, node_id: int, start: int = 0, length: int) -> numpy.ndarray[dtype=float32]

    Fill an array of parameter float values. This is more efficient
    than calling hapi.getParmFloatValue individually for each
    parameter value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmFloatValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmFloatValueCount - start.
    
    """
def getParmIdFromName(session: Session | None, node_id: int, parm_name: str) -> int:
    """getParmIdFromName(session: hapi.Session | None = None, node_id: int, parm_name: str) -> int

    All parameter APIs require a hapi.HAPI_ParmId but if you know the
    parameter you wish to operate on by name than you can use
    this function to get its hapi.HAPI_ParmId. If the parameter with
    the given name is not found the parameter id returned
    will be -1.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    
    """
def getParmInfo(session: Session | None, node_id: int, parm_id: int) -> ParmInfo:
    """getParmInfo(session: hapi.Session | None = None, node_id: int, parm_id: int) -> hapi.ParmInfo

    Get the parm info of a parameter by parm id.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_id:
        The parm id.
    
    """
def getParmInfoFromName(session: Session | None, node_id: int, parm_name: str) -> ParmInfo:
    """getParmInfoFromName(session: hapi.Session | None = None, node_id: int, parm_name: str) -> hapi.ParmInfo

    Get the parm info of a parameter by name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    
    """
def getParmIntValue(session: Session | None, node_id: int, parm_name: str, index: int) -> int:
    """getParmIntValue(session: hapi.Session | None = None, node_id: int, parm_name: str, index: int) -> int

    Get single parm int value by name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    

    index:
        Index within the parameter's values tuple.
    
    """
def getParmIntValues(session: Session | None, node_id: int, start: int, length: int) -> list[int]:
    """getParmIntValues(session: hapi.Session | None = None, node_id: int, start: int = 0, length: int) -> list

    Fill an array of parameter int values. This is more efficient
    than calling hapi.getParmIntValue individually for each
    parameter value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmIntValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmIntValueCount - start.
    
    """
def getParmIntValues_np(session: Session | None, node_id: int, start: int, length: int) -> NDArray[numpy.int32]:
    """getParmIntValues_np(session: hapi.Session | None = None, node_id: int, start: int = 0, length: int) -> numpy.ndarray[dtype=int32]

    Fill an array of parameter int values. This is more efficient
    than calling hapi.getParmIntValue individually for each
    parameter value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmIntValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmIntValueCount - start.
    
    """
def getParmNodeValue(session: Session | None, node_id: int, parm_name: str) -> int:
    """getParmNodeValue(session: hapi.Session | None = None, node_id: int, parm_name: str) -> int

    Get a single node id parm value of an Op Path parameter. This is
    how you see which node is connected as an input for the current
    node (via parameter).



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The name of the parameter.
    
    """
def getParmStringValue(session: Session | None, node_id: int, parm_name: str, index: int, evaluate: bool = ...) -> int:
    '''getParmStringValue(session: hapi.Session | None = None, node_id: int, parm_name: str, index: int, evaluate: bool = True) -> int

    Get single parm string value by name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The name of the parameter.
    

    index:
        Index within the parameter\'s values tuple.
    

    evaluate:
        Whether or not to evaluate the string expression.
        For example, the string "$F" would evaluate to the
        current frame number. So, passing in evaluate = False
        would give you back the string "$F" and passing
        in evaluate = True would give you back "1" (assuming
        the current frame is 1).
    
    '''
def getParmStringValues(session: Session | None, node_id: int, evaluate: bool, start: int, length: int) -> list[int]:
    '''getParmStringValues(session: hapi.Session | None = None, node_id: int, evaluate: bool, start: int = 0, length: int) -> list

    Fill an array of parameter string handles. These handles must
    be used in conjunction with hapi.getString to get the
    actual string values. This is more efficient than calling
    hapi.getParmStringValue individually for each
    parameter value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    evaluate:
        Whether or not to evaluate the string expression.
        For example, the string "$F" would evaluate to the
        current frame number. So, passing in evaluate = False
        would give you back the string "$F" and passing
        in evaluate = True would give you back "1" (assuming
        the current frame is 1).
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmStringValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmStringValueCount - start.
    
    '''
def getParmTagName(session: Session | None, node_id: int, parm_id: int, tag_index: int) -> int:
    """getParmTagName(session: hapi.Session | None = None, node_id: int, parm_id: int, tag_index: int) -> int

    Get the tag name on a parameter given an index.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_id:
        The parm id.
    

    tag_index:
        The tag index, which should be between 0 and
        hapi.ParmInfo.tagCount - 1.
        These indices are invalidated whenever tags are added
        to parameters. Do not store these or expect them to be the
        same if the scene is modified.
    
    """
def getParmTagValue(session: Session | None, node_id: int, parm_id: int, tag_name: str) -> int:
    """getParmTagValue(session: hapi.Session | None = None, node_id: int, parm_id: int, tag_name: str) -> int

    Get the tag value on a parameter given the tag name.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_id:
        The parm id.
    

    tag_name:
        The tag name, either known or returned by
        hapi.getParmTagName.
    
    """
def getParmWithTag(session: Session | None, node_id: int, tag_name: str) -> int:
    """getParmWithTag(session: hapi.Session | None = None, node_id: int, tag_name: str) -> int

    Get the first parm with a specific, ideally unique, tag on it.
    This is particularly useful for getting the ogl parameters on a
    material node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    tag_name:
        The tag name to look for.
    
    """
def getPartInfo(session: Session | None, node_id: int, part_id: int) -> PartInfo:
    """getPartInfo(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.PartInfo

    Get a particular part info struct.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        The part id.
    
    """
def getPreset(session: Session | None, node_id: int, buffer_length: int) -> list[str]:
    """getPreset(session: hapi.Session | None = None, node_id: int, buffer_length: int) -> list

    Generates a preset for the given asset.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The exposed node id.
    

    buffer_length:
        Size of the buffer. Should be the same as the length
        returned by hapi.getPresetBufLength.
    
    """
def getPresetBufLength(session: Session | None, node_id: int, preset_type: presetType, preset_name: str) -> int:
    """getPresetBufLength(session: hapi.Session | None = None, node_id: int, preset_type: hapi.presetType, preset_name: str) -> int

    Generate a preset blob of the current state of all the
    parameter values, cache it, and return its size in bytes.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The exposed node id.
    

    preset_type:
        The preset type.
    

    preset_name:
        Optional. This is only used if the `preset_type` is
        hapi.presetType.Idx. If None is given, the preset
        name will be the same as the name of the node with
        the given `node_id`.
    
    """
def getPresetCount(session: Session | None, buffer: str, buffer_length: int) -> int:
    """getPresetCount(session: hapi.Session | None = None, buffer: str, buffer_length: int) -> int

    Gets the number of presets in an IDX file. When this method is
    called, the names of the presets are stored in a single internal
    buffer from which they can be retrieved by calling
    hapi.getPresetNames.

    Note that calling hapi.getPresetCount will overwrite the preset
    names that were previously stored in the internal buffer. Therefore,
    ensure that you have called hapi.getPresetNames before calling
    hapi.getPresetCount again.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    buffer:
        A buffer containing the raw binary data of the .idx file.
    

    buffer_length:
        Size of the buffer.
    
    """
def getPresetNames(session: Session | None, buffer: str, buffer_length: int, preset_names_count: int) -> list[int]:
    """getPresetNames(session: hapi.Session | None = None, buffer: str, buffer_length: int, preset_names_count: int) -> list

    Gets the names of presets in an IDX file. hapi.getPresetCount must
    be called before calling this method. See the hapi.getPresetCount
    documentation for more information.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    buffer:
        A buffer containing the raw binary data of the .idx file.
        This should be the same buffer that was passed into
        hapi.getPresetCount.
    

    buffer_length:
        Size of the buffer.
    

    preset_names_count:
        Number of presets in the file. Should be the same as
        the count returned by hapi.getPresetCount
    
    """
def getPreset_np(session: Session | None, node_id: int, buffer_length: int) -> NDArray[numpy.int8]:
    """getPreset_np(session: hapi.Session | None = None, node_id: int, buffer_length: int) -> numpy.ndarray[dtype=int8]

    Generates a preset for the given asset.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The exposed node id.
    

    buffer_length:
        Size of the buffer. Should be the same as the length
        returned by hapi.getPresetBufLength.
    
    """
def getServerEnvInt(session: Session | None, variable_name: str) -> int:
    """getServerEnvInt(session: hapi.Session | None = None, variable_name: str) -> int

    Get environment variable from the server process as an integer.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    variable_name:
        Name of the environment variable.
    
    """
def getServerEnvString(session: Session | None, variable_name: str) -> int:
    """getServerEnvString(session: hapi.Session | None = None, variable_name: str) -> int

    Get environment variable from the server process as a string.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    variable_name:
        Name of the environment variable.
    
    """
def getServerEnvVarCount(session: Session | None = ...) -> int:
    """getServerEnvVarCount(session: hapi.Session | None = None) -> int

    Provides the number of environment variables that are in
    the server environment's process

    Note that hapi.getServerEnvVarList should be called directly after
    this method, otherwise there is the possibility that the environment
    variable count of the server will have changed by the time that
    hapi.getServerEnvVarList is called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getServerEnvVarList(session: Session | None = ..., start: int = ..., length: int = ...) -> list[int]:
    """getServerEnvVarList(session: hapi.Session | None = None, start: int = 0, length: int = 0) -> list

    Provides a list of all of the environment variables
    in the server's process



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    start:
        First index of range. Must be at least 0 and at most
        env_count - 1 where env_count is the count returned by
        hapi.getServerEnvVarCount
    

    length:
        Given env_count returned by hapi.getServerEnvVarCount
        length should be at least 0 and at most env_count - start.
    """
def getSessionEnvInt(session: Session | None, int_type: sessionEnvIntType) -> int:
    """getSessionEnvInt(session: hapi.Session | None = None, int_type: hapi.sessionEnvIntType) -> int

    Gives back a certain session-specific environment integers
    like current license type being used.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    int_type:
        One of hapi.sessionEnvIntType.
    
    """
def getSessionSyncInfo(session: Session) -> SessionSyncInfo:
    """getSessionSyncInfo(session: hapi.Session) -> hapi.SessionSyncInfo

    Get the hapi.SessionSyncInfo for synchronizing SessionSync
    state between Houdini and Houdini Engine integrations.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getSphereInfo(session: Session | None, geo_node_id: int, part_id: int) -> SphereInfo:
    """getSphereInfo(session: hapi.Session | None = None, geo_node_id: int, part_id: int) -> hapi.SphereInfo

    Get the sphere info on a geo part (if the part is a sphere).



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    geo_node_id:
        The geo node id.
    

    part_id:
        The part id of the
    
    """
def getStatus(session: Session | None, status_type: statusType) -> int:
    """getStatus(session: hapi.Session | None = None, status_type: hapi.statusType) -> int

    Gives back the status code for a specific status type.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    status_type:
        One of hapi.statusType.
    
    """
def getStatusString(session: Session | None, status_type: statusType, length: int) -> str:
    """getStatusString(session: hapi.Session | None = None, status_type: hapi.statusType, length: int) -> str

    Return status string message.

    You MUST call hapi.getStatusStringBufLength before calling
    hapi.getStatusString because hapi.getStatusString will
    not return the real status string and instead return a
    cached version of the string that was created inside
    hapi.getStatusStringBufLength. The reason for this is that
    the length of the real status string may change between
    the call to hapi.getStatusStringBufLength and the call to
    hapi.getStatusString.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    status_type:
        One of hapi.statusType.
    

    length:
        Length of the string buffer (must match size of
        `string_value` - so including None terminator).
    
    """
def getStatusStringBufLength(session: Session | None, status_type: statusType, verbosity: statusVerbosity) -> int:
    '''getStatusStringBufLength(session: hapi.Session | None = None, status_type: hapi.statusType, verbosity: hapi.statusVerbosity) -> int

    Return length of string buffer storing status string message.

    If called with hapi.statusType.CookResult this will actually
    parse the node networks for the previously cooked asset(s)
    and aggregate all node errors, warnings, and messages
    (depending on the verbosity level set). Usually this is done
    just for the last cooked single asset but if you load a whole
    Houdini scene using hapi.loadHIPFile then you\'ll have
    multiple "previously cooked assets".

    You MUST call hapi.getStatusStringBufLength before calling
    hapi.getStatusString because hapi.getStatusString will
    not return the real status string and instead return a
    cached version of the string that was created inside
    hapi.getStatusStringBufLength. The reason for this is that
    the length of the real status string may change between
    the call to hapi.getStatusStringBufLength and the call to
    hapi.getStatusString.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    status_type:
        One of hapi.statusType.
    

    verbosity:
        Preferred verbosity level.
    
    '''
def getString(session: Session | None, string_handle: int, length: int) -> str:
    """getString(session: hapi.Session | None = None, string_handle: int, length: int) -> str

    Gives back the string value of the string with the
    given handle.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    string_handle:
        Handle of the string to query.
    

    length:
        Length of the string buffer (must match size of
        `string_value` - so including None terminator).
    
    """
def getStringBatch(session: Session | None, char_array_length: int) -> list[str]:
    """getStringBatch(session: hapi.Session | None = None, char_array_length: int) -> list

    Gives back the values of the given string handles.
    The given char array is filled with null-separated
    values, and the final value is null-terminated.
    Used with hapi.getStringBatchSize. Using this function
    instead of repeated calls to hapi.getString can be more
    more efficient for a large number of strings.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    char_array_length:
        Length of `char_array`. Must be large enough to hold
        all the string values including None separators.
    
    """
def getStringBatchSize(session: Session | None, string_handle_array: list[int], string_handle_count: int) -> int:
    """getStringBatchSize(session: hapi.Session | None = None, string_handle_array: list, string_handle_count: int) -> int

    Gives back the length of the buffer needed to hold
    all the values null-separated for the given string
    handles. Used with hapi.getStringBatch.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    string_handle_array:
        Array of string handles to be read.
    

    string_handle_count:
        Length of `string_handle_array`
    
    """
def getStringBatchSize_np(session: Session | None, string_handle_array: NDArray[numpy.int32], string_handle_count: int) -> int:
    """getStringBatchSize_np(session: hapi.Session | None = None, string_handle_array: numpy.ndarray[dtype=int32], string_handle_count: int) -> int

    Gives back the length of the buffer needed to hold
    all the values null-separated for the given string
    handles. Used with hapi.getStringBatch.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    string_handle_array:
        Array of string handles to be read.
    

    string_handle_count:
        Length of `string_handle_array`
    
    """
def getStringBatch_np(session: Session | None, char_array_length: int) -> NDArray[numpy.int8]:
    """getStringBatch_np(session: hapi.Session | None = None, char_array_length: int) -> numpy.ndarray[dtype=int8]

    Gives back the values of the given string handles.
    The given char array is filled with null-separated
    values, and the final value is null-terminated.
    Used with hapi.getStringBatchSize. Using this function
    instead of repeated calls to hapi.getString can be more
    more efficient for a large number of strings.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    char_array_length:
        Length of `char_array`. Must be large enough to hold
        all the string values including None separators.
    
    """
def getStringBufLength(session: Session | None, string_handle: int) -> int:
    """getStringBufLength(session: hapi.Session | None = None, string_handle: int) -> int

    Gives back the string length of the string with the
    given handle.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    string_handle:
        Handle of the string to query.
    
    """
def getSupportedImageFileFormatCount(session: Session | None = ...) -> int:
    """getSupportedImageFileFormatCount(session: hapi.Session | None = None) -> int

    Get the number of supported texture file formats.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getSupportedImageFileFormats(session: Session | None, file_format_count: int) -> list[ImageFileFormat]:
    """getSupportedImageFileFormats(session: hapi.Session | None = None, file_format_count: int) -> list

    Get a list of support image file formats - their names,
    descriptions and a list of recognized extensions.

    Note that you MUST call
    hapi.getSupportedImageFileFormatCount
    before calling this function for the first time.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    file_format_count:
        The number of supported texture file formats. This
        should be at least as large as the count returned
        by hapi.getSupportedImageFileFormatCount.
    
    """
def getTime(session: Session | None = ...) -> float:
    """getTime(session: hapi.Session | None = None) -> float

    Gets the global time of the scene. All API calls deal with
    this time to cook.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getTimelineOptions(session: Session | None = ...) -> TimelineOptions:
    """getTimelineOptions(session: hapi.Session | None = None) -> hapi.TimelineOptions

    Gets the current global timeline options.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getTotalCookCount(session: Session | None, node_id: int, node_type_filter: int, node_flags_filter: int, recursive: bool) -> int:
    """getTotalCookCount(session: hapi.Session | None = None, node_id: int, node_type_filter: int, node_flags_filter: int, recursive: bool) -> int

    Get the specified node's total cook count, including
    its children, if specified.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    node_type_filter:
        The node type by which to filter the children.
    

    node_flags_filter:
        The node flags by which to filter the children.
    

    recursive:
        Whether or not to include the specified node's
        children cook count in the tally.
    
    """
def getUseHoudiniTime(session: Session | None = ...) -> bool:
    """getUseHoudiniTime(session: hapi.Session | None = None) -> bool

    Returns whether the Houdini session will use the current time in
    Houdini when cooking and retrieving data. By default this is
    disabled and the Houdini session uses time 0 (i.e. frame 1).
    In SessionSync, it is enabled by default, but can be overridden.
    Note that this function will ALWAYS return
    hapi.result.Success.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getVertexList(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> list[int]:
    """getVertexList(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> list

    Get array containing the vertex-point associations where the
    ith element in the array is the point index the ith vertex
    associates with.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.vertexCount - 1.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.vertexCount - `start`.
    
    """
def getVertexList_np(session: Session | None, node_id: int, part_id: int, start: int, length: int) -> NDArray[numpy.int32]:
    """getVertexList_np(session: hapi.Session | None = None, node_id: int, part_id: int, start: int = 0, length: int) -> numpy.ndarray[dtype=int32]

    Get array containing the vertex-point associations where the
    ith element in the array is the point index the ith vertex
    associates with.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.vertexCount - 1.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.vertexCount - `start`.
    
    """
def getViewport(session: Session) -> Viewport:
    """getViewport(session: hapi.Session) -> hapi.Viewport

    Get the hapi.Viewport info for synchronizing viewport in
    SessionSync. When SessionSync is running this will
    return Houdini's current viewport information.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def getVolumeBounds(session: Session | None, node_id: int, part_id: int) -> tuple[float, float, float, float, float, float, float, float, float]:
    """getVolumeBounds(session: hapi.Session | None = None, node_id: int, part_id: int) -> tuple

    Get the bounding values of a volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    
    """
def getVolumeInfo(session: Session | None, node_id: int, part_id: int) -> VolumeInfo:
    """getVolumeInfo(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.VolumeInfo

    Retrieve any meta-data about the volume primitive, including
    its transform, location, scale, taper, resolution.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    
    """
def getVolumeTileFloatData(session: Session | None, node_id: int, part_id: int, fill_value: float, tile: VolumeTileInfo, length: int) -> list[float]:
    """getVolumeTileFloatData(session: hapi.Session | None = None, node_id: int, part_id: int, fill_value: float, tile: hapi.VolumeTileInfo, length: int) -> list

    Retrieve floating point values of the voxels pointed to
    by a tile. Note that a tile may extend beyond the limits
    of the volume so not all values in the given buffer will
    be written to. Voxels outside the volume will be initialized
    to the given fill value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    fill_value:
        Value that will be used to fill the `values_array`.
        This is useful so that you can see what values
        have actually been written to.
    

    tile:
        The tile to retrieve.
    

    length:
        The length should be ( 8 ^ 3 ) * tupleSize.
    
    """
def getVolumeTileFloatData_np(session: Session | None, node_id: int, part_id: int, fill_value: float, tile: VolumeTileInfo, length: int) -> NDArray[numpy.float32]:
    """getVolumeTileFloatData_np(session: hapi.Session | None = None, node_id: int, part_id: int, fill_value: float, tile: hapi.VolumeTileInfo, length: int) -> numpy.ndarray[dtype=float32]

    Retrieve floating point values of the voxels pointed to
    by a tile. Note that a tile may extend beyond the limits
    of the volume so not all values in the given buffer will
    be written to. Voxels outside the volume will be initialized
    to the given fill value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    fill_value:
        Value that will be used to fill the `values_array`.
        This is useful so that you can see what values
        have actually been written to.
    

    tile:
        The tile to retrieve.
    

    length:
        The length should be ( 8 ^ 3 ) * tupleSize.
    
    """
def getVolumeTileIntData(session: Session | None, node_id: int, part_id: int, fill_value: int, tile: VolumeTileInfo, length: int) -> list[int]:
    """getVolumeTileIntData(session: hapi.Session | None = None, node_id: int, part_id: int, fill_value: int, tile: hapi.VolumeTileInfo, length: int) -> list

    Retrieve integer point values of the voxels pointed to
    by a tile. Note that a tile may extend beyond the limits
    of the volume so not all values in the given buffer will
    be written to. Voxels outside the volume will be initialized
    to the given fill value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    fill_value:
        Value that will be used to fill the `values_array`.
        This is useful so that you can see what values
        have actually been written to.
    

    tile:
        The tile to retrieve.
    

    length:
        The length should be ( 8 ^ 3 ) * tupleSize.
    
    """
def getVolumeTileIntData_np(session: Session | None, node_id: int, part_id: int, fill_value: int, tile: VolumeTileInfo, length: int) -> NDArray[numpy.int32]:
    """getVolumeTileIntData_np(session: hapi.Session | None = None, node_id: int, part_id: int, fill_value: int, tile: hapi.VolumeTileInfo, length: int) -> numpy.ndarray[dtype=int32]

    Retrieve integer point values of the voxels pointed to
    by a tile. Note that a tile may extend beyond the limits
    of the volume so not all values in the given buffer will
    be written to. Voxels outside the volume will be initialized
    to the given fill value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    fill_value:
        Value that will be used to fill the `values_array`.
        This is useful so that you can see what values
        have actually been written to.
    

    tile:
        The tile to retrieve.
    

    length:
        The length should be ( 8 ^ 3 ) * tupleSize.
    
    """
def getVolumeVisualInfo(session: Session | None, node_id: int, part_id: int) -> VolumeVisualInfo:
    """getVolumeVisualInfo(session: hapi.Session | None = None, node_id: int, part_id: int) -> hapi.VolumeVisualInfo

    Retrieve the visualization meta-data of the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    
    """
def getVolumeVoxelFloatData(session: Session | None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, value_count: int) -> list[float]:
    """getVolumeVoxelFloatData(session: hapi.Session | None = None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, value_count: int) -> list

    Retrieve floating point values of the voxel at a specific
    index. Note that you must call hapi.getVolumeInfo prior
    to this call.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    x_index:
        The x index/coordinate of the voxel.
    

    y_index:
        The y index/coordinate of the voxel.
    

    z_index:
        The z index/coordinate of the voxel.
    

    value_count:
        Should be equal to the volume's
        hapi.VolumeInfo.tupleSize.
    
    """
def getVolumeVoxelFloatData_np(session: Session | None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, value_count: int) -> NDArray[numpy.float32]:
    """getVolumeVoxelFloatData_np(session: hapi.Session | None = None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, value_count: int) -> numpy.ndarray[dtype=float32]

    Retrieve floating point values of the voxel at a specific
    index. Note that you must call hapi.getVolumeInfo prior
    to this call.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    x_index:
        The x index/coordinate of the voxel.
    

    y_index:
        The y index/coordinate of the voxel.
    

    z_index:
        The z index/coordinate of the voxel.
    

    value_count:
        Should be equal to the volume's
        hapi.VolumeInfo.tupleSize.
    
    """
def getVolumeVoxelIntData(session: Session | None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, value_count: int) -> list[int]:
    """getVolumeVoxelIntData(session: hapi.Session | None = None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, value_count: int) -> list

    Retrieve integer point values of the voxel at a specific
    index. Note that you must call hapi.getVolumeInfo prior
    to this call.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    x_index:
        The x index/coordinate of the voxel.
    

    y_index:
        The y index/coordinate of the voxel.
    

    z_index:
        The z index/coordinate of the voxel.
    

    value_count:
        Should be equal to the volume's
        hapi.VolumeInfo.tupleSize.
    
    """
def getVolumeVoxelIntData_np(session: Session | None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, value_count: int) -> NDArray[numpy.int32]:
    """getVolumeVoxelIntData_np(session: hapi.Session | None = None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, value_count: int) -> numpy.ndarray[dtype=int32]

    Retrieve integer point values of the voxel at a specific
    index. Note that you must call hapi.getVolumeInfo prior
    to this call.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    x_index:
        The x index/coordinate of the voxel.
    

    y_index:
        The y index/coordinate of the voxel.
    

    z_index:
        The z index/coordinate of the voxel.
    

    value_count:
        Should be equal to the volume's
        hapi.VolumeInfo.tupleSize.
    
    """
def getWorkItemAttributeSize(session: Session | None, node_id: int, work_item_id: int, attribute_name: str) -> int:
    """getWorkItemAttributeSize(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str) -> int

    Gets the size of the work item attribute.
    It is the length of the array of data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the work item
    

    attribute_name:
        null-terminated name of the work item attribute
    
    """
def getWorkItemFloatAttribute(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> list[float]:
    """getWorkItemFloatAttribute(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> list

    Gets float data from a work item attribute.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the work_item
    

    attribute_name:
        null-terminated name of the work item attribute
    

    length:
        The length of the `data_array`
    
    """
def getWorkItemFloatAttribute_np(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> NDArray[numpy.float32]:
    """getWorkItemFloatAttribute_np(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> numpy.ndarray[dtype=float32]

    Gets float data from a work item attribute.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the work_item
    

    attribute_name:
        null-terminated name of the work item attribute
    

    length:
        The length of the `data_array`
    
    """
def getWorkItemInfo(session: Session | None, graph_context_id: int, work_item_id: int) -> PDG_WorkItemInfo:
    """getWorkItemInfo(session: hapi.Session | None = None, graph_context_id: int, work_item_id: int) -> hapi.PDG_WorkItemInfo

    Retrieves the info of a given work item by id.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    graph_context_id:
        The graph context that the work item is in.
    

    work_item_id:
        The id of the work item.
    
    """
def getWorkItemIntAttribute(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> list[int]:
    """getWorkItemIntAttribute(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> list

    Gets int data from a work item attribute.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the work_item
    

    attribute_name:
        null-terminated name of the work item attribute
    

    length:
        The length of `data_array`
    
    """
def getWorkItemIntAttribute_np(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> NDArray[numpy.int32]:
    """getWorkItemIntAttribute_np(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> numpy.ndarray[dtype=int32]

    Gets int data from a work item attribute.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the work_item
    

    attribute_name:
        null-terminated name of the work item attribute
    

    length:
        The length of `data_array`
    
    """
def getWorkItemOutputFiles(session: Session | None, node_id: int, work_item_id: int, resultinfo_count: int) -> list[PDG_WorkItemOutputFile]:
    """getWorkItemOutputFiles(session: hapi.Session | None = None, node_id: int, work_item_id: int, resultinfo_count: int) -> list

    Gets the info for work item output files.
    The number of work item results is found on the hapi.PDG_WorkItemInfo
    returned by hapi.getWorkItemInfo



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the work item
    

    resultinfo_count:
        The length of `resultinfo_array`
    
    """
def getWorkItemStringAttribute(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> list[int]:
    """getWorkItemStringAttribute(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, length: int) -> list

    Gets string ids from a work item attribute.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the work item
    

    attribute_name:
        null-terminated name of the work item attribute
    

    length:
        The length of `data_array`
    
    """
def getWorkItems(session: Session | None, node_id: int, length: int) -> list[int]:
    """getWorkItems(session: hapi.Session | None = None, node_id: int, length: int) -> list

    Gets the list of work item ids for the given node



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    length:
        The length of the `work_item_ids` buffer
    
    """
def getWorkItems_np(session: Session | None, node_id: int, length: int) -> NDArray[numpy.int32]:
    """getWorkItems_np(session: hapi.Session | None = None, node_id: int, length: int) -> numpy.ndarray[dtype=int32]

    Gets the list of work item ids for the given node



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    length:
        The length of the `work_item_ids` buffer
    
    """
def initialize(session: Session | None, cook_options: CookOptions, use_cooking_thread: bool = ..., cooking_thread_stack_size: int = ..., houdini_environment_files: str = ..., otl_search_path: str = ..., dso_search_path: str = ..., image_dso_search_path: str = ..., audio_dso_search_path: str = ...) -> bool:
    '''initialize(session: hapi.Session | None = None, cook_options: hapi.CookOptions, use_cooking_thread: bool = True, cooking_thread_stack_size: int = -1, houdini_environment_files: str = \'\', otl_search_path: str = \'\', dso_search_path: str = \'\', image_dso_search_path: str = \'\', audio_dso_search_path: str = \'\') -> bool

    Create the asset manager, set up environment variables, and
    initialize the main Houdini scene. No license check is done
    during this step. Only when you try to load an asset library
    (OTL) do we actually check for licenses.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    cook_options:
        Global cook options used by subsequent default cooks.
        This can be overwritten by individual cooks but if
        you choose to instantiate assets with cook_on_load
        set to True then these cook options will be used.
    

    use_cooking_thread:
        Use a separate thread for cooking of assets. This
        allows for asynchronous cooking and larger stack size.
    

    cooking_thread_stack_size:
        Set the stack size of the cooking thread. Use -1 to
        set the stack size to the Houdini default. This
        value is in bytes.
    

    houdini_environment_files:
        A list of paths, separated by a ";" on Windows and a ":"
        on Linux and Mac, to .env files that follow the same
        syntax as the houdini.env file in Houdini\'s user prefs
        folder. These will be applied after the default
        houdini.env file and will overwrite the process\'
        environment variable values. You an use this to enforce
        a stricter environment when running engine.
        For more info, see:
        http://www.sidefx.com/docs/houdini/basics/config_env
    

    otl_search_path:
        The directory where OTLs are searched for. You can
        pass None here which will only use the default
        Houdini OTL search paths. You can also pass in
        multiple paths separated by a ";" on Windows and a ":"
        on Linux and Mac. If something other than None is
        passed the default Houdini search paths will be
        appended to the end of the path string.
    

    dso_search_path:
        The directory where generic DSOs (custom plugins) are
        searched for. You can pass None here which will
        only use the default Houdini DSO search paths. You
        can also pass in multiple paths separated by a ";"
        on Windows and a ":" on Linux and Mac. If something
        other than None is passed the default Houdini search
        paths will be appended to the end of the path string.
    

    image_dso_search_path:
        The directory where image DSOs (custom plugins) are
        searched for. You can pass None here which will
        only use the default Houdini DSO search paths. You
        can also pass in multiple paths separated by a ";"
        on Windows and a ":" on Linux and Mac. If something
        other than None is passed the default Houdini search
        paths will be appended to the end of the path string.
    

    audio_dso_search_path:
        The directory where audio DSOs (custom plugins) are
        searched for. You can pass None here which will
        only use the default Houdini DSO search paths. You
        can also pass in multiple paths separated by a ";"
        on Windows and a ":" on Linux and Mac. If something
        other than None is passed the default Houdini search
        paths will be appended to the end of the path string.
    
    '''
def insertMultiparmInstance(session: Session | None, node_id: int, parm_id: int, instance_position: int) -> bool:
    """insertMultiparmInstance(session: hapi.Session | None = None, node_id: int, parm_id: int, instance_position: int) -> bool

    Insert an instance of a multiparm before instance_position.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_id:
        A parm id given by a hapi.ParmInfo struct that
        has type hapi.parmType.Multiparmlist.
    

    instance_position:
        The new instance will be inserted at this position
        index. Do note the multiparms can start at position
        1 or 0. Use hapi.ParmInfo.instanceStartOffset to
        distinguish.
    
    """
def interrupt(session: Session | None = ...) -> bool:
    """interrupt(session: hapi.Session | None = None) -> bool

    Interrupt a cook or load operation.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def isInitialized(session: Session | None = ...) -> bool:
    """isInitialized(session: hapi.Session | None = None) -> bool

    Check whether the runtime has been initialized yet using
    hapi.initialize. Function will return hapi.result.Success
    if the runtime has been initialized and hapi.result.NotInitialized
    otherwise.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def isNodeValid(session: Session | None, node_id: int, unique_node_id: int) -> bool:
    """isNodeValid(session: hapi.Session | None = None, node_id: int, unique_node_id: int) -> bool

    Determine if your instance of the node actually still exists
    inside the Houdini scene. This is what can be used to
    determine when the Houdini scene needs to be re-populated
    using the host application's instances of the nodes.
    Note that this function will ALWAYS return
    hapi.result.Success.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    unique_node_id:
        The unique node id from
        hapi.NodeInfo.uniqueHoudiniNodeId.
    
    """
def isSessionValid(session: Session) -> bool:
    """isSessionValid(session: hapi.Session) -> bool

    Checks whether the session identified by hapi.Session.id is
    a valid session opened in the implementation identified by
    hapi.Session.type.


    Returns hapi.result.Success if the session is valid.
    Otherwise, the session is invalid and passing it to
    other HAPI calls may result in undefined behavior.


    session:
        The hapi.Session to check.
    
    """
def loadAssetLibraryFromFile(session: Session | None, file_path: str, allow_overwrite: bool) -> int:
    """loadAssetLibraryFromFile(session: hapi.Session | None = None, file_path: str, allow_overwrite: bool) -> int

    Loads a Houdini asset library (OTL) from a .otl file.
    It does NOT create anything inside the Houdini scene.

    This is when we actually check for valid licenses.

    The next step is to call hapi.getAvailableAssetCount
    to get the number of assets contained in the library using the
    returned library_id. Then call hapi.getAvailableAssets
    to get the list of available assets by name. Use the asset
    names with hapi.createNode to actually create
    one of these nodes in the Houdini scene and get back
    an asset_id.

    The HIP file saved using hapi.saveHIPFile will only
    have an absolute path reference to the loaded OTL meaning
    that if the OTL is moved or renamed the HIP file won't
    load properly. It also means that if you change the OTL
    using the saved HIP scene the same OTL file will change
    as the one used with Houdini Engine.
    See `hapi.saveHIPFile`.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    file_path:
        Absolute path to the .otl file.
    

    allow_overwrite:
        With this true, if the library file being loaded
        contains asset definitions that have already been
        loaded they will overwrite the existing definitions.
        Otherwise, a library containing asset definitions that
        already exist will fail to load, returning a
        hapi.result of
        hapi.result.AssetDefAlreadyLoaded.
    
    """
def loadAssetLibraryFromMemory(session: Session | None, library_buffer: str, library_buffer_length: int, allow_overwrite: bool) -> int:
    """loadAssetLibraryFromMemory(session: hapi.Session | None = None, library_buffer: str, library_buffer_length: int, allow_overwrite: bool) -> int

    Loads a Houdini asset library (OTL) from memory.
    It does NOT create anything inside the Houdini scene.

    This is when we actually check for valid licenses.

    Please note that the performance benefit of loading a library
    from memory are negligible at best. Due to limitations of
    Houdini's library manager, there is still some disk access
    and file writes because every asset library needs to be
    saved to a real file. Use this function only as a convenience
    if you already have the library file in memory and don't wish
    to have to create your own temporary library file and then
    call hapi.loadAssetLibraryFromFile.

    The next step is to call hapi.getAvailableAssetCount
    to get the number of assets contained in the library using the
    returned library_id. Then call hapi.getAvailableAssets
    to get the list of available assets by name. Use the asset
    names with hapi.createNode to actually create
    one of these nodes in the Houdini scene and get back
    an asset_id.

    The saved HIP file using hapi.saveHIPFile will
    contain the OTL loaded as part of its Embedded OTLs.
    This means that you can safely move or rename the original
    OTL file and the HIP will continue to work but if you make
    changes to the OTL while using the saved HIP the changes
    won't be saved to the original OTL.
    See `hapi.saveHIPFile`.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    library_buffer:
        The memory buffer containing the asset definitions
        in the same format as a standard Houdini .otl file.
    

    library_buffer_length:
        The size of the OTL memory buffer.
    

    allow_overwrite:
        With this true, if the library file being loaded
        contains asset definitions that have already been
        loaded they will overwrite the existing definitions.
        Otherwise, a library containing asset definitions that
        already exist will fail to load, returning a
        hapi.result of
        hapi.result.AssetDefAlreadyLoaded.
    
    """
def loadGeoFromFile(session: Session | None, node_id: int, file_name: str) -> bool:
    """loadGeoFromFile(session: hapi.Session | None = None, node_id: int, file_name: str) -> bool

    Loads a geometry file and put its contents onto a SOP
    node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    file_name:
        The name of the file to be loaded
    
    """
def loadGeoFromMemory(session: Session | None, node_id: int, format: str, buffer: str, length: int) -> bool:
    '''loadGeoFromMemory(session: hapi.Session | None = None, node_id: int, format: str, buffer: str, length: int) -> bool

    Loads a geometry from memory and put its
    contents onto a SOP node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    format:
        The file format, ie. "obj", "bgeo" etc.
    

    buffer:
        The buffer we will read the geometry from.
    

    length:
        The size of the buffer passed in.
    
    '''
def loadHIPFile(session: Session | None, file_name: str, cook_on_load: bool = ...) -> bool:
    """loadHIPFile(session: hapi.Session | None = None, file_name: str, cook_on_load: bool = False) -> bool

    Loads a .hip file into the main Houdini scene.

    In threaded mode, this is an _async call_!

    This method will load the HIP file into the scene. This means
    that any registered `hou.hipFile` event callbacks will be triggered
    with the `hou.hipFileEventType.BeforeMerge` and
    `hou.hipFileEventType.AfterMerge` events.

    This method loads a HIP file, completely overwriting
    everything that already exists in the scene. Therefore, any HAPI ids
    (node ids, part ids, etc.) that were obtained before calling this
    method will be invalidated.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    file_name:
        Absolute path to the .hip file to load.
    

    cook_on_load:
        Set to True if you wish the nodes to cook as soon
        as they are created. Otherwise, you will have to
        call hapi.cookNode explicitly for each after you
        call this function.
    
    """
def loadNodeFromFile(session: Session | None, file_name: str, parent_node_id: int, node_label: str, cook_on_load: bool) -> int:
    """loadNodeFromFile(session: hapi.Session | None = None, file_name: str, parent_node_id: int, node_label: str, cook_on_load: bool) -> int

    Loads and creates a previously saved node and all
    its contents from given file.
    The saved file must have been created by calling
    hapi.saveNodeToFile.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    file_name:
        The name of the file to be loaded
    

    parent_node_id:
        The parent node id of the Geometry object.
    

    node_label:
        The name of the new Geometry object.
    

    cook_on_load:
        Set to True if you wish the nodes to cook as soon
        as they are created. Otherwise, you will have to
        call hapi.cookNode explicitly for each after you
        call this function.
    
    """
def mergeHIPFile(session: Session, file_name: str, cook_on_load: bool) -> int:
    """mergeHIPFile(session: hapi.Session, file_name: str, cook_on_load: bool) -> int

    Loads a .hip file into the main Houdini scene.

    In threaded mode, this is an _async call_!

    This method will merge the HIP file into the scene. This means
    that any registered `hou.hipFile` event callbacks will be triggered
    with the `hou.hipFileEventType.BeforeMerge` and
    `hou.hipFileEventType.AfterMerge` events.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    file_name:
        Absolute path to the .hip file to load.
    

    cook_on_load:
        Set to True if you wish the nodes to cook as soon
        as they are created. Otherwise, you will have to
        call hapi.cookNode explicitly for each after you
        call this function.
    
    """
def parmHasExpression(session: Session | None, node_id: int, parm_name: str, index: int) -> bool:
    """parmHasExpression(session: hapi.Session | None = None, node_id: int, parm_name: str, index: int) -> bool

    See if a parameter has an expression



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    

    index:
        The parm index.
    
    """
def parmHasTag(session: Session | None, node_id: int, parm_id: int, tag_name: str) -> bool:
    """parmHasTag(session: hapi.Session | None = None, node_id: int, parm_id: int, tag_name: str) -> bool

    See if a parameter has a specific tag.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_id:
        The parm id.
    

    tag_name:
        The tag name to look for.
    
    """
def pausePDGCook(session: Session | None, graph_context_id: int) -> bool:
    """pausePDGCook(session: hapi.Session | None = None, graph_context_id: int) -> bool

    Pause the PDG cooking operation.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    graph_context_id:
        The id of the graph context
    
    """
def pythonThreadInterpreterLock(session: Session | None, locked: bool) -> bool:
    '''pythonThreadInterpreterLock(session: hapi.Session | None = None, locked: bool) -> bool

    Acquires or releases the Python interpreter lock. This is
    needed if HAPI is called from Python and HAPI is in threaded
    mode (see hapi.initialize.

    The problem arises when async functions like
    hapi.createNode may start a cooking thread that
    may try to run Python code. That is, we would now have
    Python running on two different threads - something not
    allowed by Python by default.

    We need to tell Python to explicitly "pause" the Python state
    on the client thread while we run Python in our cooking thread.

    You must call this function first with locked == True before
    any async HAPI call. Then, after the async call finished,
    detected via calls to hapi.getStatus call this method
    again to release the lock with locked == False.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    locked:
        True will acquire the interpreter lock to use it for
        the HAPI cooking thread. False will release the lock
        back to the client thread.
    
    '''
def queryNodeInput(session: Session | None, node_to_query: int, input_index: int) -> int:
    """queryNodeInput(session: hapi.Session | None = None, node_to_query: int, input_index: int) -> int

    Query which node is connected to another node's input.


    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    

    node_to_query:
        The node to query.
    

    input_index:
        The input index. Should be between 0 and the
        to_node's hapi.NodeInfo.inputCount - 1.
    
    """
def queryNodeOutputConnectedCount(session: Session | None, node_id: int, output_idx: int, into_subnets: bool = ..., through_dots: bool = ...) -> int:
    """queryNodeOutputConnectedCount(session: hapi.Session | None = None, node_id: int, output_idx: int, into_subnets: bool = True, through_dots: bool = True) -> int

    Get the number of nodes currently connected to the given node at
    the output index.


    Use the count returned by this function to get the
    hapi.HAPI_NodeId of connected nodes using
    hapi.queryNodeOutputConnectedNodes.


    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    output_idx:
        The output index. Should be between 0 and the
        to_node's hapi.NodeInfo.outputCount - 1.
    

    into_subnets:
        Whether to search by diving into subnets.
    

    through_dots:
        Whether to search through dots.
    
    """
def queryNodeOutputConnectedNodes(session: Session | None, node_id: int, output_idx: int, into_subnets: bool, through_dots: bool, start: int, length: int) -> list[int]:
    """queryNodeOutputConnectedNodes(session: hapi.Session | None = None, node_id: int, output_idx: int, into_subnets: bool = True, through_dots: bool = True, start: int = 0, length: int) -> list

    Get the ids of nodes currently connected to the given node
    at the output index.

    Use the connected_count returned by
    hapi.queryNodeOutputConnectedCount.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    output_idx:
        The output index. Should be between 0 and the
        to_node's hapi.NodeInfo.outputCount - 1.
    

    into_subnets:
        Whether to search by diving into subnets.
    

    through_dots:
        Whether to search through dots.
    

    start:
        At least 0 and at most connected_count returned by
        hapi.queryNodeOutputConnectedCount.
    

    length:
        Given connected_count returned by
        hapi.queryNodeOutputConnectedCount length should
        be at least 1 and at most connected_count - start.
    
    """
def removeCustomString(session: Session | None, string_handle: int) -> bool:
    """removeCustomString(session: hapi.Session | None = None, string_handle: int) -> bool

    Removes the specified string from the server
    and invalidates the handle



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    string_handle:
        Handle of the string that was added
    
    """
def removeMultiparmInstance(session: Session | None, node_id: int, parm_id: int, instance_position: int) -> bool:
    """removeMultiparmInstance(session: hapi.Session | None = None, node_id: int, parm_id: int, instance_position: int) -> bool

    Remove the instance of a multiparm given by instance_position.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_id:
        A parm id given by a hapi.ParmInfo struct that
        has type hapi.parmType.Multiparmlist.
    

    instance_position:
        The instance at instance_position will removed.
    
    """
def removeParmExpression(session: Session | None, node_id: int, parm_id: int, index: int) -> bool:
    """removeParmExpression(session: hapi.Session | None = None, node_id: int, parm_id: int, index: int) -> bool

    Remove the expression string, leaving the value of the
    parm at the current value of the expression

    Regardless of the value, when calling this function
    on a parameter, if that parameter has a callback function
    attached to it, that callback function will be called. For
    example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_id:
        Parameter id of the parameter being updated.
    

    index:
        Index within the parameter's values tuple.
    
    """
def renameNode(session: Session | None, node_id: int, new_name: str) -> bool:
    """renameNode(session: hapi.Session | None = None, node_id: int, new_name: str) -> bool

    Rename a node that you created. Only nodes with their
    hapi.NodeInfo.createdPostAssetLoad set to True can be
    renamed this way.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node to rename.
    

    new_name:
        The new node name.
    
    """
def renderCOPOutputToImage(session: Session | None, cop_node_id: int, cop_output_name: str) -> bool:
    """renderCOPOutputToImage(session: hapi.Session | None = None, cop_node_id: int, cop_output_name: str) -> bool

    Render a single texture from a COP to an image for
    later extraction. COPs may have multiple outputs,
    so this method lets you select which output to use.


    Note that you must call this method,
    hapi.renderCOPToImage or hapi.renderTextureToImage
    before any of the other material APIs.


    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    cop_node_id:
        The COP node id.
    

    cop_output_name:
        The name of the output to extract. Passing in
        an empty string will default to the COP's first output.
    
    """
def renderCOPToImage(session: Session | None, cop_node_id: int) -> bool:
    """renderCOPToImage(session: hapi.Session | None = None, cop_node_id: int) -> bool

    Render a single texture from a COP to an image for
    later extraction.


    Note that you must call this method,
    hapi.renderCOPOutputToImage or hapi.renderTextureToImage
    before any of the other material APIs.


    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    cop_node_id:
        The COP node id.
    
    """
def renderTextureToImage(session: Session | None, material_node_id: int, parm_id: int) -> bool:
    """renderTextureToImage(session: hapi.Session | None = None, material_node_id: int, parm_id: int) -> bool

    Render only a single texture to an image for later extraction.
    An example use of this method might be to render the diffuse,
    normal, and bump texture maps of a material to individual
    texture files for use within the client application.

    Note that you must call this method,
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    before any of the other material APIs.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    

    parm_id:
        This is the index in the parameter list of the
        material_id's node of the parameter containing the
        texture map file path.
    
    """
def resetSimulation(session: Session | None, node_id: int) -> bool:
    """resetSimulation(session: hapi.Session | None = None, node_id: int) -> bool

    Resets the simulation cache of the asset. This is very useful
    for assets that use dynamics, to be called after some
    setup has changed for the asset - for example, asset inputs



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The asset node id.
    
    """
def revertGeo(session: Session | None, node_id: int) -> bool:
    """revertGeo(session: hapi.Session | None = None, node_id: int) -> bool

    Remove all changes that have been committed to this
    geometry. If this is an intermediate result node (Edit SOP), all
    deltas will be removed. If it's any other type of node, the node
    will be unlocked if it is locked.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    
    """
def revertParmToDefault(session: Session | None, node_id: int, parm_name: str, index: int) -> bool:
    """revertParmToDefault(session: hapi.Session | None = None, node_id: int, parm_name: str, index: int) -> bool

    Revert single parm by name to default



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    

    index:
        Index within the parameter's values tuple.
    
    """
def revertParmToDefaults(session: Session | None, node_id: int, parm_name: str) -> bool:
    """revertParmToDefaults(session: hapi.Session | None = None, node_id: int, parm_name: str) -> bool

    Revert all instances of the parm by name to defaults



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    
    """
def saveGeoToFile(session: Session | None, node_id: int, file_name: str) -> bool:
    """saveGeoToFile(session: hapi.Session | None = None, node_id: int, file_name: str) -> bool

    Saves a geometry to file. The type of file to save is
    to be determined by the extension ie. .bgeo, .obj



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    file_name:
        The name of the file to be saved. The extension
        of the file determines its type.
    
    """
def saveGeoToMemory(session: Session | None, node_id: int, length: int) -> list[str]:
    """saveGeoToMemory(session: hapi.Session | None = None, node_id: int, length: int) -> list

    Saves the cached geometry to your buffer in memory,
    whose format and required size is identified by the call to
    hapi.getGeoSize. The call to hapi.getGeoSize is
    required as hapi.getGeoSize does the actual saving work.

    Also note that this call to hapi.saveGeoToMemory will delete
    the internal geo buffer that was cached in the previous call
    to hapi.getGeoSize. This means that you will need to call
    hapi.getGeoSize again before you can call this function.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    length:
        The size of the buffer passed in.
    
    """
def saveGeoToMemory_np(session: Session | None, node_id: int, length: int) -> NDArray[numpy.int8]:
    """saveGeoToMemory_np(session: hapi.Session | None = None, node_id: int, length: int) -> numpy.ndarray[dtype=int8]

    Saves the cached geometry to your buffer in memory,
    whose format and required size is identified by the call to
    hapi.getGeoSize. The call to hapi.getGeoSize is
    required as hapi.getGeoSize does the actual saving work.

    Also note that this call to hapi.saveGeoToMemory will delete
    the internal geo buffer that was cached in the previous call
    to hapi.getGeoSize. This means that you will need to call
    hapi.getGeoSize again before you can call this function.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    length:
        The size of the buffer passed in.
    
    """
def saveHIPFile(session: Session | None, file_path: str, lock_nodes: bool = ...) -> bool:
    """saveHIPFile(session: hapi.Session | None = None, file_path: str, lock_nodes: bool = False) -> bool

    Saves a .hip file of the current Houdini scene.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    file_path:
        Absolute path to the .hip file to save to.
    

    lock_nodes:
        Specify whether to lock all SOP nodes before saving
        the scene file. This way, when you load the scene
        file you can see exactly the state of each SOP at
        the time it was saved instead of relying on the
        re-cook to accurately reproduce the state. It does,
        however, take a lot more space and time locking all
        nodes like this.
    
    """
def saveNodeToFile(session: Session | None, node_id: int, file_name: str) -> bool:
    """saveNodeToFile(session: hapi.Session | None = None, node_id: int, file_name: str) -> bool

    Saves the node and all its contents to file.
    The saved file can be loaded by calling hapi.loadNodeFromFile.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    file_name:
        The name of the file to be saved. The extension
        of the file determines its type.
    
    """
def setAnimCurve(session: Session | None, node_id: int, parm_id: int, parm_index: int, curve_keyframes_array: list[Keyframe], keyframe_count: int) -> bool:
    """setAnimCurve(session: hapi.Session | None = None, node_id: int, parm_id: int, parm_index: int, curve_keyframes_array: list, keyframe_count: int) -> bool

    Set an animation curve on a parameter of an exposed node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The exposed node id.
    

    parm_id:
        The id of an exposed parameter within the node.

    parm_index:
        The index of the parameter, if it is for example
        a 3 tuple
    

    curve_keyframes_array:
        An array of hapi.Keyframe structs that describes
        the keys on this curve.
    

    keyframe_count:
        The number of keys on the curve.
    
    """
def setAttributeDictionaryArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[str], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeDictionaryArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set attribute dictionary array data. The dictionary data should
    be provided as JSON-encoded strings.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the dictionary values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeDictionaryArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[str], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeDictionaryArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set attribute dictionary array data asynchronously. The dictionary
    should be provided as JSON-encoded strings.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the dictionary values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeDictionaryArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[str], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeDictionaryArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set attribute dictionary array data asynchronously. The dictionary
    should be provided as JSON-encoded strings.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the dictionary values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeDictionaryArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[str], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeDictionaryArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set attribute dictionary array data. The dictionary data should
    be provided as JSON-encoded strings.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the dictionary values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeDictionaryData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[str], start: int, length: int) -> bool:
    """setAttributeDictionaryData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set attribute dictionary data. The dictionary data should
    be provided as JSON-encoded strings.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An hapi.HAPI_StringHandle array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeDictionaryDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[str], start: int, length: int) -> int:
    """setAttributeDictionaryDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set attribute dictionary data asynchronously. The dictionary data
    should be provided as JSON-encoded strings.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An hapi.HAPI_StringHandle array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloat64ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[float], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeFloat64ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set 64-bit float array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the double values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeFloat64ArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[float], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeFloat64ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set 64-bit float array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the double values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloat64ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: NDArray[numpy.float64], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeFloat64ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: numpy.ndarray[dtype=float64], data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set 64-bit float array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the double values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloat64ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: NDArray[numpy.float64], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeFloat64ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: numpy.ndarray[dtype=float64], data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set 64-bit float array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the double values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeFloat64Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[float], start: int, length: int) -> bool:
    """setAttributeFloat64Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set 64-bit attribute float data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 64-bit float array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloat64DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[float], start: int, length: int) -> int:
    """setAttributeFloat64DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set 64-bit attribute float data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 64-bit float array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloat64DataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.float64], start: int, length: int) -> int:
    """setAttributeFloat64DataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=float64], start: int = 0, length: int) -> int

    Set 64-bit attribute float data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 64-bit float array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloat64Data_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.float64], start: int, length: int) -> bool:
    """setAttributeFloat64Data_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=float64], start: int = 0, length: int) -> bool

    Set 64-bit attribute float data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 64-bit float array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloat64UniqueData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[float], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeFloat64UniqueData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute 64-bit float data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A floating point array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeFloat64UniqueDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[float], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeFloat64UniqueDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute 64-bit float data to the same unique
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A floating point array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeFloat64UniqueDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.float64], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeFloat64UniqueDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=float64], data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute 64-bit float data to the same unique
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A floating point array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeFloat64UniqueData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.float64], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeFloat64UniqueData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=float64], data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute 64-bit float data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A floating point array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeFloatArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[float], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeFloatArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set float array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the float values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeFloatArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[float], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeFloatArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set float array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the float values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloatArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: NDArray[numpy.float32], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeFloatArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: numpy.ndarray[dtype=float32], data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set float array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the float values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloatArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: NDArray[numpy.float32], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeFloatArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: numpy.ndarray[dtype=float32], data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set float array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the float values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeFloatData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[float], start: int, length: int) -> bool:
    """setAttributeFloatData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set attribute float data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An float array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloatDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[float], start: int, length: int) -> int:
    """setAttributeFloatDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set attribute float data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An float array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloatDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.float32], start: int, length: int) -> int:
    """setAttributeFloatDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=float32], start: int = 0, length: int) -> int

    Set attribute float data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An float array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloatData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.float32], start: int, length: int) -> bool:
    """setAttributeFloatData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=float32], start: int = 0, length: int) -> bool

    Set attribute float data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An float array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeFloatUniqueData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[float], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeFloatUniqueData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute float data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A floating point array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeFloatUniqueDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[float], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeFloatUniqueDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute float data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A floating point array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeFloatUniqueDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.float32], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeFloatUniqueDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=float32], data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute float data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A floating point array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeFloatUniqueData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.float32], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeFloatUniqueData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=float32], data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute float data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A floating point array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeIndexedStringData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, string_fixed_array: list[str], string_fixed_length: int, indices_array: list[int], indices_start: int, indices_length: int) -> bool:
    """setAttributeIndexedStringData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, string_fixed_array: list, string_fixed_length: int, indices_array: list, indices_start: int = 0, indices_length: int) -> bool

    Set attribute string data by index.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    string_fixed_array:
        An array of strings at least the size of
        string_fixed_length/tt>.
    

    string_fixed_length:
        Number of strings that are indexed.
    

    indices_array:
        integer array at least the size of
        length * hapi.AttributeInfo.tupleSize. Each
        entry indexes string_array.
    

    indices_start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    indices_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIndexedStringDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, string_array: list[str], string_count: int, indices_array: list[int], indices_start: int, indices_length: int) -> int:
    """setAttributeIndexedStringDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, string_array: list, string_count: int, indices_array: list, indices_start: int = 0, indices_length: int) -> int

    Set attribute string data by index asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    string_array:
        An array of strings at least the size of
        string_count/tt>.
    

    string_count:
        Number of strings that are indexed.
    

    indices_array:
        integer array at least the size of
        length * hapi.AttributeInfo.tupleSize. Each
        entry indexes string_array.
    

    indices_start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    indices_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIndexedStringDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, string_array: list[str], string_count: int, indices_array: NDArray[numpy.int32], indices_start: int, indices_length: int) -> int:
    """setAttributeIndexedStringDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, string_array: list, string_count: int, indices_array: numpy.ndarray[dtype=int32], indices_start: int = 0, indices_length: int) -> int

    Set attribute string data by index asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    string_array:
        An array of strings at least the size of
        string_count/tt>.
    

    string_count:
        Number of strings that are indexed.
    

    indices_array:
        integer array at least the size of
        length * hapi.AttributeInfo.tupleSize. Each
        entry indexes string_array.
    

    indices_start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    indices_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIndexedStringData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, string_fixed_array: list[str], string_fixed_length: int, indices_array: NDArray[numpy.int32], indices_start: int, indices_length: int) -> bool:
    """setAttributeIndexedStringData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, string_fixed_array: list, string_fixed_length: int, indices_array: numpy.ndarray[dtype=int32], indices_start: int = 0, indices_length: int) -> bool

    Set attribute string data by index.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    string_fixed_array:
        An array of strings at least the size of
        string_fixed_length/tt>.
    

    string_fixed_length:
        Number of strings that are indexed.
    

    indices_array:
        integer array at least the size of
        length * hapi.AttributeInfo.tupleSize. Each
        entry indexes string_array.
    

    indices_start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    indices_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt16ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeInt16ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set 16-bit integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int16 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeInt16ArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeInt16ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set 16-bit integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int16 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt16ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeInt16ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set 16-bit integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int16 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt16ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeInt16ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set 16-bit integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int16 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeInt16Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> bool:
    """setAttributeInt16Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set 16-bit attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 16-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt16DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> int:
    """setAttributeInt16DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set 16-bit attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 16-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt16UniqueData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeInt16UniqueData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute 16-bit int data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeInt16UniqueDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeInt16UniqueDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute 16-bit int data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeInt64ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeInt64ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set 64-bit integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int64 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeInt64ArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeInt64ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set 64-bit integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int64 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt64ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: NDArray[numpy.int64], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeInt64ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: numpy.ndarray[dtype=int64], data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set 64-bit integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int64 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt64ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: NDArray[numpy.int64], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeInt64ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: numpy.ndarray[dtype=int64], data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set 64-bit integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int64 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeInt64Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> bool:
    """setAttributeInt64Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set 64-bit attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 64-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt64DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> int:
    """setAttributeInt64DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set 64-bit attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 64-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt64DataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.int64], start: int, length: int) -> int:
    """setAttributeInt64DataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=int64], start: int = 0, length: int) -> int

    Set 64-bit attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 64-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt64Data_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.int64], start: int, length: int) -> bool:
    """setAttributeInt64Data_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=int64], start: int = 0, length: int) -> bool

    Set 64-bit attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 64-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt64UniqueData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeInt64UniqueData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute 64-bit int data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeInt64UniqueDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeInt64UniqueDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute 64-bit int data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeInt64UniqueDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.int64], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeInt64UniqueDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=int64], data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute 64-bit int data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeInt64UniqueData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.int64], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeInt64UniqueData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=int64], data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute 64-bit int data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeInt8ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeInt8ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set 8-bit integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int8 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeInt8ArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeInt8ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set 8-bit integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int8 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt8ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeInt8ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set 8-bit integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int8 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt8ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeInt8ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set 8-bit integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_Int8 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeInt8Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> bool:
    """setAttributeInt8Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set 8-bit attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 8-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt8DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> int:
    """setAttributeInt8DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set 8-bit attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An 8-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeInt8UniqueData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeInt8UniqueData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute 8-bit int data to the same unique value.




    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeInt8UniqueDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeInt8UniqueDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute 8-bit int data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeIntArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeIntArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the int values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeIntArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeIntArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the int values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIntArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: NDArray[numpy.int32], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeIntArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: numpy.ndarray[dtype=int32], data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the int values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIntArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: NDArray[numpy.int32], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeIntArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: numpy.ndarray[dtype=int32], data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the int values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeIntData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> bool:
    """setAttributeIntData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIntDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> int:
    """setAttributeIntDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIntDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.int32], start: int, length: int) -> int:
    """setAttributeIntDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=int32], start: int = 0, length: int) -> int

    Set attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIntData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.int32], start: int, length: int) -> bool:
    """setAttributeIntData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=int32], start: int = 0, length: int) -> bool

    Set attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeIntUniqueData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeIntUniqueData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute int data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeIntUniqueDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeIntUniqueDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute int data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeIntUniqueDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.int32], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeIntUniqueDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=int32], data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute int data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeIntUniqueData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: NDArray[numpy.int32], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeIntUniqueData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: numpy.ndarray[dtype=int32], data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute int data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeStringArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[str], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeStringArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set string array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the string values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeStringArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[str], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeStringArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set string array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the string values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeStringArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[str], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeStringArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set string array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the string values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeStringArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[str], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeStringArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set string array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the string values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeStringData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[str], start: int, length: int) -> bool:
    """setAttributeStringData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set attribute string data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An hapi.HAPI_StringHandle array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeStringDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[str], start: int, length: int) -> int:
    """setAttributeStringDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set attribute string data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An hapi.HAPI_StringHandle array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeStringUniqueData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[str], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeStringUniqueData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int, num_indices: int) -> bool

    Set multiple attribute string data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A string
    

    data_length:
        Must be the length of string data.
    

    start_index:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeStringUniqueDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[str], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeStringUniqueDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int, num_indices: int) -> int

    Set multiple attribute string data to the same unique value
    asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A string
    

    data_length:
        Must be the length of string data.
    

    start_index:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeUInt8ArrayData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeUInt8ArrayData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> bool

    Set unsigned 8-bit integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_UInt8 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeUInt8ArrayDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: list[int], start: int, sizes_fixed_length: int) -> int:
    """setAttributeUInt8ArrayDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: list, start: int = 0, sizes_fixed_length: int) -> int

    Set unsigned 8-bit integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_UInt8 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeUInt8ArrayDataAsync_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> int:
    """setAttributeUInt8ArrayDataAsync_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> int

    Set unsigned 8-bit integer array attribute data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_UInt8 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeUInt8ArrayData_np(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_fixed_array: list[int], data_fixed_length: int, sizes_fixed_array: NDArray[numpy.int32], start: int, sizes_fixed_length: int) -> bool:
    """setAttributeUInt8ArrayData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_fixed_array: list, data_fixed_length: int, sizes_fixed_array: numpy.ndarray[dtype=int32], start: int = 0, sizes_fixed_length: int) -> bool

    Set unsigned 8-bit integer array attribute data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo that contains the description for the
        attribute that is being set.
    

    data_fixed_array:
        An array containing the hapi.HAPI_UInt8 values of the attribute.
    

    data_fixed_length:
        The total size of the data array. The size can be no greater
        than the hapi.AttributeInfo.totalArrayElements
        of the attribute.
    

    sizes_fixed_array:
        An array of integers that contains the sizes of each
        attribute array. This is required because the attribute
        array for each geometry component can be of variable size.
    

    start:
        First index of range. Must be at least 0 and at most
        hapi.AttributeInfo.count - 1.
    

    sizes_fixed_length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    """
def setAttributeUInt8Data(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> bool:
    """setAttributeUInt8Data(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> bool

    Set unsigned 8-bit attribute integer data.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An unsigned 8-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeUInt8DataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], start: int, length: int) -> int:
    """setAttributeUInt8DataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, start: int = 0, length: int) -> int

    Set unsigned 8-bit attribute integer data asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        An unsigned 8-bit integer array at least the size of
        length * hapi.AttributeInfo.tupleSize.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    length:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start`.
    
    """
def setAttributeUInt8UniqueData(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> bool:
    """setAttributeUInt8UniqueData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> bool

    Set multiple attribute unsigned 8-bit int data to the same unique value.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setAttributeUInt8UniqueDataAsync(session: Session | None, node_id: int, part_id: int, name: str, attr_info: AttributeInfo, data_array: list[int], data_length: int, start_index: int, num_indices: int) -> int:
    """setAttributeUInt8UniqueDataAsync(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, attr_info: hapi.AttributeInfo, data_array: list, data_length: int, start_index: int = 0, num_indices: int) -> int

    Set multiple attribute unsigned 8-bit int data to the same unique
    value asynchronously.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    name:
        Attribute name.
    

    attr_info:
        hapi.AttributeInfo used as input for what tuple size.
        you want. Also contains some sanity checks like
        data type. Generally should be the same struct
        returned by hapi.getAttributeInfo.
    

    data_array:
        A integer array at least the size of
        hapi.AttributeInfo.tupleSize.
    

    data_length:
        An integer of at least the size of
        hapi.AttributeInfo.tupleSize.
    

    start_index:
        First index of range. Must be at least 0 and at
        most hapi.AttributeInfo.count - 1.
    

    num_indices:
        Must be at least 0 and at most
        hapi.AttributeInfo.count - `start_index`.
    
    """
def setCacheProperty(session: Session | None, cache_name: str, cache_property: cacheProperty, property_value: int) -> bool:
    """setCacheProperty(session: hapi.Session | None = None, cache_name: str, cache_property: hapi.cacheProperty, property_value: int) -> bool

    Lets you modify specific properties of the different memory
    caches in the current Houdini context. This includes clearing
    caches, reducing their memory use, or changing how memory limits
    are respected by a cache.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    cache_name:
        Cache name from hapi.getActiveCacheNames.
    

    cache_property:
        The specific property of the cache to modify.
    

    property_value:
        The new property value.
    
    """
def setCompositorOptions(session: Session | None, compositor_options: CompositorOptions) -> bool:
    """setCompositorOptions(session: hapi.Session | None = None, compositor_options: hapi.CompositorOptions) -> bool

    Sets the global compositor options.


    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    compositor_options:
        The compositor options.
    
    """
def setCurveCounts(session: Session | None, node_id: int, part_id: int, counts_array: list[int], start: int, length: int) -> bool:
    """setCurveCounts(session: hapi.Session | None = None, node_id: int, part_id: int, counts_array: list, start: int = 0, length: int) -> bool

    Set the number of vertices for each curve in the part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    counts_array:
        The number of cvs each curve contains.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' counts to set.
    
    """
def setCurveCounts_np(session: Session | None, node_id: int, part_id: int, counts_array: NDArray[numpy.int32], start: int, length: int) -> bool:
    """setCurveCounts_np(session: hapi.Session | None = None, node_id: int, part_id: int, counts_array: numpy.ndarray[dtype=int32], start: int = 0, length: int) -> bool

    Set the number of vertices for each curve in the part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    counts_array:
        The number of cvs each curve contains.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' counts to set.
    
    """
def setCurveInfo(session: Session | None, node_id: int, part_id: int, info: CurveInfo) -> bool:
    """setCurveInfo(session: hapi.Session | None = None, node_id: int, part_id: int, info: hapi.CurveInfo) -> bool

    Set meta-data for the curve mesh, including the
    curve type, order, and periodicity.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    info:
        The curve info represents the meta-data about
        the curves, including the type, order,
        and periodicity.
    
    """
def setCurveKnots(session: Session | None, node_id: int, part_id: int, knots_array: list[float], start: int, length: int) -> bool:
    """setCurveKnots(session: hapi.Session | None = None, node_id: int, part_id: int, knots_array: list, start: int = 0, length: int) -> bool

    Set the knots of the curves in this part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    knots_array:
        The knots of each curve.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' knots to set. The
        length of all the knots on a single curve is
        the order of that curve plus the number of
        vertices (see hapi.setCurveOrders
        and hapi.setCurveCounts.
    
    """
def setCurveKnots_np(session: Session | None, node_id: int, part_id: int, knots_array: NDArray[numpy.float32], start: int, length: int) -> bool:
    """setCurveKnots_np(session: hapi.Session | None = None, node_id: int, part_id: int, knots_array: numpy.ndarray[dtype=float32], start: int = 0, length: int) -> bool

    Set the knots of the curves in this part.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    knots_array:
        The knots of each curve.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' knots to set. The
        length of all the knots on a single curve is
        the order of that curve plus the number of
        vertices (see hapi.setCurveOrders
        and hapi.setCurveCounts.
    
    """
def setCurveOrders(session: Session | None, node_id: int, part_id: int, orders_array: list[int], start: int, length: int) -> bool:
    """setCurveOrders(session: hapi.Session | None = None, node_id: int, part_id: int, orders_array: list, start: int = 0, length: int) -> bool

    Set the orders for each curve in the part if the
    curve has varying order.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    orders_array:
        The orders of each curve.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' orders to retrieve.
    
    """
def setCurveOrders_np(session: Session | None, node_id: int, part_id: int, orders_array: NDArray[numpy.int32], start: int, length: int) -> bool:
    """setCurveOrders_np(session: hapi.Session | None = None, node_id: int, part_id: int, orders_array: numpy.ndarray[dtype=int32], start: int = 0, length: int) -> bool

    Set the orders for each curve in the part if the
    curve has varying order.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    orders_array:
        The orders of each curve.
    

    start:
        The index of the first curve.
    

    length:
        The number of curves' orders to retrieve.
    
    """
def setCustomString(session: Session | None, string_value: str) -> int:
    """setCustomString(session: hapi.Session | None = None, string_value: str) -> int

    Adds the given string to the string table and returns
    the handle. It is the responsibility of the caller to
    manage access to the string. The intended use for custom strings
    is to allow structs that reference strings to be passed in to HAPI



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    string_value:
        Actual string value (character array).
    
    """
def setFaceCounts(session: Session | None, node_id: int, part_id: int, face_counts_array: list[int], start: int, length: int) -> bool:
    """setFaceCounts(session: hapi.Session | None = None, node_id: int, part_id: int = 0, face_counts_array: list, start: int = 0, length: int) -> bool

    Set the array of faces where the nth integer in the array is
    the number of vertices the nth face has.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    face_counts_array:
        An integer array at least the size of `length`.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.faceCount - 1.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.faceCount - `start`.
    
    """
def setFaceCounts_np(session: Session | None, node_id: int, part_id: int, face_counts_array: NDArray[numpy.int32], start: int, length: int) -> bool:
    """setFaceCounts_np(session: hapi.Session | None = None, node_id: int, part_id: int = 0, face_counts_array: numpy.ndarray[dtype=int32], start: int = 0, length: int) -> bool

    Set the array of faces where the nth integer in the array is
    the number of vertices the nth face has.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    face_counts_array:
        An integer array at least the size of `length`.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.faceCount - 1.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.faceCount - `start`.
    
    """
def setGroupMembership(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_name: str, membership_array: list[int], start: int, length: int) -> bool:
    """setGroupMembership(session: hapi.Session | None = None, node_id: int, part_id: int = 0, group_type: hapi.groupType, group_name: str, membership_array: list, start: int = 0, length: int) -> bool

    Set group membership.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    group_type:
        The group type.
    

    group_name:
        The group name.
    

    membership_array:
        Array of ints that represent the membership of this
        group. Should be the size given by
        HAPI_PartInfo_GetElementCountByGroupType with
        `group_type` and the hapi.PartInfo of `part_id`.
    

    start:
        Start offset into the membership array. Must be
        less than HAPI_PartInfo_GetElementCountByGroupType.
    

    length:
        Should be less than or equal to the size
        of `membership_array`. When setting edge group membership,
        this parameter should be set to the number of points (which
        are used to implicitly define the edges), not to the number
        edges in the group.
    
    """
def setGroupMembership_np(session: Session | None, node_id: int, part_id: int, group_type: groupType, group_name: str, membership_array: NDArray[numpy.int32], start: int, length: int) -> bool:
    """setGroupMembership_np(session: hapi.Session | None = None, node_id: int, part_id: int = 0, group_type: hapi.groupType, group_name: str, membership_array: numpy.ndarray[dtype=int32], start: int = 0, length: int) -> bool

    Set group membership.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    group_type:
        The group type.
    

    group_name:
        The group name.
    

    membership_array:
        Array of ints that represent the membership of this
        group. Should be the size given by
        HAPI_PartInfo_GetElementCountByGroupType with
        `group_type` and the hapi.PartInfo of `part_id`.
    

    start:
        Start offset into the membership array. Must be
        less than HAPI_PartInfo_GetElementCountByGroupType.
    

    length:
        Should be less than or equal to the size
        of `membership_array`. When setting edge group membership,
        this parameter should be set to the number of points (which
        are used to implicitly define the edges), not to the number
        edges in the group.
    
    """
def setHeightFieldData(session: Session | None, node_id: int, part_id: int, name: str, values_array: list[float], start: int, length: int) -> bool:
    '''setHeightFieldData(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, values_array: list, start: int, length: int) -> bool

    Set the height field data for a terrain volume with the values from
    a flattened 2D array of float.
    hapi.setVolumeInfo should be called first to make sure that the
    volume and its info are initialized.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        The name of the volume used for the heightfield.
        If set to "height" the values will be used for height information,
        if not, the data will used as a mask.
    

    values_array:
        Heightfield flattened array. Should be at least the size of
        `start` + `length`.
    

    start:
        The start at least 0 and at most
        ( hapi.VolumeInfo.xLength * hapi.VolumeInfo.yLength ) - `length`.
    

    length:
        The length should be at least 1 or at most
        ( hapi.VolumeInfo.xLength * hapi.VolumeInfo.yLength ) - `start`.
    
    '''
def setHeightFieldData_np(session: Session | None, node_id: int, part_id: int, name: str, values_array: NDArray[numpy.float32], start: int, length: int) -> bool:
    '''setHeightFieldData_np(session: hapi.Session | None = None, node_id: int, part_id: int, name: str, values_array: numpy.ndarray[dtype=float32], start: int, length: int) -> bool

    Set the height field data for a terrain volume with the values from
    a flattened 2D array of float.
    hapi.setVolumeInfo should be called first to make sure that the
    volume and its info are initialized.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    name:
        The name of the volume used for the heightfield.
        If set to "height" the values will be used for height information,
        if not, the data will used as a mask.
    

    values_array:
        Heightfield flattened array. Should be at least the size of
        `start` + `length`.
    

    start:
        The start at least 0 and at most
        ( hapi.VolumeInfo.xLength * hapi.VolumeInfo.yLength ) - `length`.
    

    length:
        The length should be at least 1 or at most
        ( hapi.VolumeInfo.xLength * hapi.VolumeInfo.yLength ) - `start`.
    
    '''
def setImageInfo(session: Session | None, material_node_id: int, image_info: ImageInfo) -> bool:
    """setImageInfo(session: hapi.Session | None = None, material_node_id: int, image_info: hapi.ImageInfo) -> bool

    Set image information like resolution and file format.
    This information will be used when extracting planes to
    an image.

    Note that you must call one of hapi.renderTextureToImage
    hapi.renderCOPToImage or hapi.renderCOPOutputToImage
    first for this method call to make sense.

    You should also first call hapi.getImageInfo to get the
    current Image Info and change only the properties
    you don't like.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    material_node_id:
        The material node id.
    

    image_info:
        The struct containing the new image information.
    
    """
def setInputCameraInfo(session: Session | None, node_id: int, camera_info: CameraInfo) -> bool:
    """setInputCameraInfo(session: hapi.Session | None = None, node_id: int, camera_info: hapi.CameraInfo) -> bool

    Configures the SOP Camera node's parameters.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id of a node created with
        hapi.createInputCameraNode.
    

    camera_info:
        A hapi.CameraInfo struct with camera configuration that
        will be used to set the parameters on the camera node.
    
    """
def setInputCameraTransform(session: Session | None, node_id: int, rst_order: rstOrder, rot_order: xyzOrder, transform: Transform) -> bool:
    """setInputCameraTransform(session: hapi.Session | None = None, node_id: int, rst_order: hapi.rstOrder, rot_order: hapi.xyzOrder, transform: hapi.Transform) -> bool

    Configures the SOP Camera node's transform parameters.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id of a node created with
        hapi.createInputCameraNode.
    

    rst_order:
        The order in which the camera's transformations occur.
    

    rot_order:
        The order in which the camera's rotations occur.
    

    transform:
        A hapi.Transform struct that will be used to set the
        transform related parameters on the camera node. Only the
        position and rotation quaternion will be used. Other fields
        will be ignored.
    
    """
def setInputCurveInfo(session: Session | None, node_id: int, part_id: int, info: InputCurveInfo) -> bool:
    """setInputCurveInfo(session: hapi.Session | None = None, node_id: int, part_id: int, info: hapi.InputCurveInfo) -> bool

    Set meta-data for the input curves, including the
    curve type, order, reverse and closed properties.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    info:
        The curve info represents the meta-data about
        the curves, including the type, order,
        and closed and reverse properties.
    
    """
def setInputCurvePositions(session: Session | None, node_id: int, part_id: int, positions_array: list[float], start: int, length: int) -> bool:
    """setInputCurvePositions(session: hapi.Session | None = None, node_id: int, part_id: int, positions_array: list, start: int = 0, length: int) -> bool

    Sets the positions for input curves, doing checks for
    curve validity, and adjusting the curve settings accordingly.
    Will also cook the node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    positions_array:
        A float array representing the positions attribute.
        It will read the array assuming a tuple size of 3.
        Note that this function does not do any coordinate axes
        conversion.
    

    start:
        The index of the first position in positions_array.
    

    length:
        The size of the positions array.
    
    """
def setInputCurvePositionsRotationsScales(session: Session | None, node_id: int, part_id: int, positions_array: list[float], positions_start: int, positions_length: int, rotations_array: list[float], rotations_start: int, rotations_length: int, scales_array: list[float], scales_start: int, scales_length: int) -> bool:
    """setInputCurvePositionsRotationsScales(session: hapi.Session | None = None, node_id: int, part_id: int, positions_array: list, positions_start: int = 0, positions_length: int, rotations_array: list, rotations_start: int = 0, rotations_length: int, scales_array: list, scales_start: int = 0, scales_length: int) -> bool

    Sets the positions for input curves, doing checks for
    curve validity, and adjusting the curve settings accordingly.
    Will also cook the node. Additionally, adds rotation and scale
    attributes to the curve.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    positions_array:
        A float array representing the positions attribute.
        It will read the array assuming a tuple size of 3.
        Note that this function does not do any coordinate axes
        conversion.
    

    positions_start:
        The index of the first position in positions_array.
    

    positions_length:
        The size of the positions array.
    

    rotations_array:
        A float array representing the rotation (rot) attribute.
        It will read the array assuming a tuple size of 4
        representing quaternion values
    

    rotations_start:
        The index of the first rotation in rotations_array.
    

    rotations_length:
        The size of the rotations array.
    

    scales_array:
        A float array representing the scale attribute.
        It will read the array assuming a tuple size of 3
    

    scales_start:
        The index of the first scale in scales_array.
    

    scales_length:
        The size of the scales array.
    
    """
def setInputCurvePositionsRotationsScales_np(session: Session | None, node_id: int, part_id: int, positions_array: NDArray[numpy.float32], positions_start: int, positions_length: int, rotations_array: NDArray[numpy.float32], rotations_start: int, rotations_length: int, scales_array: NDArray[numpy.float32], scales_start: int, scales_length: int) -> bool:
    """setInputCurvePositionsRotationsScales_np(session: hapi.Session | None = None, node_id: int, part_id: int, positions_array: numpy.ndarray[dtype=float32], positions_start: int = 0, positions_length: int, rotations_array: numpy.ndarray[dtype=float32], rotations_start: int = 0, rotations_length: int, scales_array: numpy.ndarray[dtype=float32], scales_start: int = 0, scales_length: int) -> bool

    Sets the positions for input curves, doing checks for
    curve validity, and adjusting the curve settings accordingly.
    Will also cook the node. Additionally, adds rotation and scale
    attributes to the curve.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    positions_array:
        A float array representing the positions attribute.
        It will read the array assuming a tuple size of 3.
        Note that this function does not do any coordinate axes
        conversion.
    

    positions_start:
        The index of the first position in positions_array.
    

    positions_length:
        The size of the positions array.
    

    rotations_array:
        A float array representing the rotation (rot) attribute.
        It will read the array assuming a tuple size of 4
        representing quaternion values
    

    rotations_start:
        The index of the first rotation in rotations_array.
    

    rotations_length:
        The size of the rotations array.
    

    scales_array:
        A float array representing the scale attribute.
        It will read the array assuming a tuple size of 3
    

    scales_start:
        The index of the first scale in scales_array.
    

    scales_length:
        The size of the scales array.
    
    """
def setInputCurvePositions_np(session: Session | None, node_id: int, part_id: int, positions_array: NDArray[numpy.float32], start: int, length: int) -> bool:
    """setInputCurvePositions_np(session: hapi.Session | None = None, node_id: int, part_id: int, positions_array: numpy.ndarray[dtype=float32], start: int = 0, length: int) -> bool

    Sets the positions for input curves, doing checks for
    curve validity, and adjusting the curve settings accordingly.
    Will also cook the node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        Currently unused. Input asset geos are assumed
        to have only one part.
    

    positions_array:
        A float array representing the positions attribute.
        It will read the array assuming a tuple size of 3.
        Note that this function does not do any coordinate axes
        conversion.
    

    start:
        The index of the first position in positions_array.
    

    length:
        The size of the positions array.
    
    """
def setNodeDisplay(session: Session | None, node_id: int, onOff: int) -> bool:
    """setNodeDisplay(session: hapi.Session | None = None, node_id: int, onOff: int) -> bool

    Set the specified node's display flag.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    onOff:
        Display flag.
    
    """
def setObjectTransform(session: Session | None, node_id: int, trans: TransformEuler) -> bool:
    """setObjectTransform(session: hapi.Session | None = None, node_id: int, trans: hapi.TransformEuler) -> bool

    Set the transform of an individual object. Note that the object
    nodes have to either be editable or have their transform
    parameters exposed at the asset level. This won't work otherwise.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The object node id.
    

    trans:
        A hapi.TransformEuler that stores the transform.
    
    """
def setParmExpression(session: Session | None, node_id: int, value: str, parm_id: int, index: int) -> bool:
    """setParmExpression(session: hapi.Session | None = None, node_id: int, value: str, parm_id: int, index: int) -> bool

    Set (push) an expression string. We can only set a single value at
    a time because we want to avoid fixed size string buffers.

    Regardless of the value, when calling this function
    on a parameter, if that parameter has a callback function
    attached to it, that callback function will be called. For
    example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    value:
        The expression string.
    

    parm_id:
        Parameter id of the parameter being updated.
    

    index:
        Index within the parameter's values tuple.
    
    """
def setParmFloatValue(session: Session | None, node_id: int, parm_name: str, index: int, value: float) -> bool:
    """setParmFloatValue(session: hapi.Session | None = None, node_id: int, parm_name: str, index: int, value: float) -> bool

    Set single parm float value by name.

    Regardless of the value, when calling this function
    on a parameter, if that parameter has a callback function
    attached to it, that callback function will be called. For
    example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    

    index:
        Index within the parameter's values tuple.
    

    value:
        The float value.
    
    """
def setParmFloatValues(session: Session | None, node_id: int, values_array: list[float], start: int, length: int) -> bool:
    """setParmFloatValues(session: hapi.Session | None = None, node_id: int, values_array: list, start: int, length: int) -> bool

    Set (push) an array of parameter float values.

    Regardless of the values, when calling this function
    on a set of parameters, if any parameter has a callback
    function attached to it, that callback function will be called.
    For example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    values_array:
        Array of floats at least the size of length.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmFloatValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmFloatValueCount - start.
    
    """
def setParmFloatValues_np(session: Session | None, node_id: int, values_array: NDArray[numpy.float32], start: int, length: int) -> bool:
    """setParmFloatValues_np(session: hapi.Session | None = None, node_id: int, values_array: numpy.ndarray[dtype=float32], start: int, length: int) -> bool

    Set (push) an array of parameter float values.

    Regardless of the values, when calling this function
    on a set of parameters, if any parameter has a callback
    function attached to it, that callback function will be called.
    For example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    values_array:
        Array of floats at least the size of length.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmFloatValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmFloatValueCount - start.
    
    """
def setParmIntValue(session: Session | None, node_id: int, parm_name: str, index: int, value: int) -> bool:
    """setParmIntValue(session: hapi.Session | None = None, node_id: int, parm_name: str, index: int, value: int) -> bool

    Set single parm int value by name.

    Regardless of the value, when calling this function
    on a parameter, if that parameter has a callback function
    attached to it, that callback function will be called. For
    example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The parm name.
    

    index:
        Index within the parameter's values tuple.
    

    value:
        The int value.
    
    """
def setParmIntValues(session: Session | None, node_id: int, values_array: list[int], start: int, length: int) -> bool:
    """setParmIntValues(session: hapi.Session | None = None, node_id: int, values_array: list, start: int = 0, length: int) -> bool

    Set (push) an array of parameter int values.

    Regardless of the values, when calling this function
    on a set of parameters, if any parameter has a callback
    function attached to it, that callback function will be called.
    For example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    values_array:
        Array of integers at least the size of length.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmIntValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmIntValueCount - start.
    
    """
def setParmIntValues_np(session: Session | None, node_id: int, values_array: NDArray[numpy.int32], start: int, length: int) -> bool:
    """setParmIntValues_np(session: hapi.Session | None = None, node_id: int, values_array: numpy.ndarray[dtype=int32], start: int = 0, length: int) -> bool

    Set (push) an array of parameter int values.

    Regardless of the values, when calling this function
    on a set of parameters, if any parameter has a callback
    function attached to it, that callback function will be called.
    For example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    values_array:
        Array of integers at least the size of length.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.NodeInfo.parmIntValueCount - 1.
    

    length:
        Must be at least 1 and at most
        hapi.NodeInfo.parmIntValueCount - start.
    
    """
def setParmNodeValue(session: Session | None, node_id: int, parm_name: str, value: int) -> bool:
    """setParmNodeValue(session: hapi.Session | None = None, node_id: int, parm_name: str, value: int) -> bool

    Set a node id parm value of an Op Path parameter. For example,
    This is how you connect the geometry output of an asset to the
    geometry input of another asset - whether the input is a parameter
    or a node input (the top of the node). Node inputs get converted
    top parameters in HAPI.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    parm_name:
        The name of the parameter.
    

    value:
        The node id of the node being connected. Pass -1 to
        disconnect.
    
    """
def setParmStringValue(session: Session | None, node_id: int, value: str, parm_id: int, index: int) -> bool:
    """setParmStringValue(session: hapi.Session | None = None, node_id: int, value: str, parm_id: int, index: int) -> bool

    Set (push) a string value. We can only set a single value at
    a time because we want to avoid fixed size string buffers.

    Regardless of the value, when calling this function
    on a parameter, if that parameter has a callback function
    attached to it, that callback function will be called. For
    example, if the parameter is a button the button will be
    pressed.

    In threaded mode, this is an _async call_!

    This API will invoke the cooking thread if threading is
    enabled. This means it will return immediately. Use
    the status and cooking count APIs under DIAGNOSTICS to get
    a sense of the progress. All other API calls will block
    until the cook operation has finished.

    Also note that the cook result won't be of type
    hapi.statusType.CallResult like all calls (including this one).
    Whenever the threading cook is done it will fill the
    cook result which is queried using
    hapi.statusType.CookResult.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    value:
        The string value.
    

    parm_id:
        Parameter id of the parameter being updated.
    

    index:
        Index within the parameter's values tuple.
    
    """
def setPartInfo(session: Session | None, node_id: int, part_id: int, part_info: PartInfo) -> bool:
    """setPartInfo(session: hapi.Session | None = None, node_id: int, part_id: int = 0, part_info: hapi.PartInfo) -> bool

    Set the main part info struct (::HAPI_PartInfo).



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    part_info:
        hapi.PartInfo value that describes the input
        geometry.
    
    """
def setPreset(session: Session | None, node_id: int, preset_type: presetType, preset_name: str, buffer: str, buffer_length: int) -> bool:
    """setPreset(session: hapi.Session | None = None, node_id: int, preset_type: hapi.presetType, preset_name: str = '', buffer: str, buffer_length: int) -> bool

    Sets a particular asset to a given preset.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The exposed node id.
    

    preset_type:
        The preset type.
    

    preset_name:
        Optional. This is only used if the `preset_type` is
        hapi.presetType.Idx. If None is give, the first
        preset in the IDX file will be chosen.
    

    buffer:
        Buffer to hold the preset data.
    

    buffer_length:
        Size of the buffer.
    
    """
def setServerEnvInt(session: Session | None, variable_name: str, value: int) -> bool:
    """setServerEnvInt(session: hapi.Session | None = None, variable_name: str, value: int) -> bool

    Set environment variable for the server process as an integer.

    Note that this may affect other sessions on the same server
    process. The session parameter is mainly there to identify the
    server process, not the specific session.

    For in-process sessions, this will affect the current process's
    environment.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    variable_name:
        Name of the environment variable.
    

    value:
        The integer value.
    
    """
def setServerEnvString(session: Session | None, variable_name: str, value: str) -> bool:
    """setServerEnvString(session: hapi.Session | None = None, variable_name: str, value: str) -> bool

    Set environment variable for the server process as a string.

    Note that this may affect other sessions on the same server
    process. The session parameter is mainly there to identify the
    server process, not the specific session.

    For in-process sessions, this will affect the current process's
    environment.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    variable_name:
        Name of the environment variable.
    

    value:
        The string value.
    
    """
def setSessionSync(session: Session | None, enable: bool) -> bool:
    """setSessionSync(session: hapi.Session | None = None, enable: bool) -> bool

    Enable or disable SessionSync mode.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    enable:
        Enable or disable SessionSync mode.
    
    """
def setSessionSyncInfo(session: Session, session_sync_info: SessionSyncInfo) -> bool:
    """setSessionSyncInfo(session: hapi.Session, session_sync_info: hapi.SessionSyncInfo) -> bool

    Set the hapi.SessionSyncInfo for synchronizing SessionSync
    state between Houdini and Houdini Engine integrations.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    session_sync_info:
        A hapi.SessionSyncInfo that stores the state.
    
    """
def setTime(session: Session | None, time: float) -> bool:
    """setTime(session: hapi.Session | None = None, time: float) -> bool

    Sets the global time of the scene. All API calls will deal
    with this time to cook.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    time:
        Time as a double in seconds.
    
    """
def setTimelineOptions(session: Session | None, timeline_options: TimelineOptions) -> bool:
    """setTimelineOptions(session: hapi.Session | None = None, timeline_options: hapi.TimelineOptions) -> bool

    Sets the global timeline options.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    timeline_options:
        The global timeline options struct.
    
    """
def setTransformAnimCurve(session: Session | None, node_id: int, trans_comp: transformComponent, curve_keyframes_array: list[Keyframe], keyframe_count: int) -> bool:
    """setTransformAnimCurve(session: hapi.Session | None = None, node_id: int, trans_comp: hapi.transformComponent, curve_keyframes_array: list, keyframe_count: int) -> bool

    A specialized convenience function to set the T,R,S values
    on an exposed node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The exposed node id.
    

    trans_comp:
        A value of hapi.transformComponent that
        identifies the particular component of the
        transform to attach the curve to, for example
        hapi.transformComponent.Tx.
    

    curve_keyframes_array:
        An array of hapi.Keyframe structs that describes
        the keys on this curve.
    

    keyframe_count:
        The number of keys on the curve.
    
    """
def setUseHoudiniTime(session: Session | None, enabled: bool) -> bool:
    """setUseHoudiniTime(session: hapi.Session | None = None, enabled: bool) -> bool

    Sets whether the Houdini session should use the current time in
    Houdini when cooking and retrieving data. By default this is
    disabled and the Houdini session uses time 0 (i.e. frame 1).
    In SessionSync, it is enabled by default, but can be overridden.
    Note that this function will ALWAYS return
    hapi.result.Success.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    enabled:
        Set to True to use Houdini time.
    
    """
def setVertexList(session: Session | None, node_id: int, part_id: int, vertex_list_array: list[int], start: int, length: int) -> bool:
    """setVertexList(session: hapi.Session | None = None, node_id: int, part_id: int, vertex_list_array: list, start: int = 0, length: int) -> bool

    Set array containing the vertex-point associations where the
    ith element in the array is the point index the ith vertex
    associates with.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    vertex_list_array:
        An integer array at least the size of length.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.vertexCount - 1.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.vertexCount - `start`.
    
    """
def setVertexList_np(session: Session | None, node_id: int, part_id: int, vertex_list_array: NDArray[numpy.int32], start: int, length: int) -> bool:
    """setVertexList_np(session: hapi.Session | None = None, node_id: int, part_id: int, vertex_list_array: numpy.ndarray[dtype=int32], start: int = 0, length: int) -> bool

    Set array containing the vertex-point associations where the
    ith element in the array is the point index the ith vertex
    associates with.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The SOP node id.
    

    part_id:
        Currently not used. Just pass 0.
    

    vertex_list_array:
        An integer array at least the size of length.
    

    start:
        First index of range. Must be at least 0 and at
        most hapi.PartInfo.vertexCount - 1.
    

    length:
        Must be at least 0 and at most
        hapi.PartInfo.vertexCount - `start`.
    
    """
def setViewport(session: Session, viewport: Viewport) -> bool:
    """setViewport(session: hapi.Session, viewport: hapi.Viewport) -> bool

    Set the hapi.Viewport info for synchronizing viewport in
    SessionSync. When SessionSync is running, this can be
    used to set the viewport information which Houdini
    will then synchronize with for its viewport.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    viewport:
        A hapi.Viewport that stores the viewport.
    
    """
def setVolumeInfo(session: Session | None, node_id: int, part_id: int, volume_info: VolumeInfo) -> bool:
    """setVolumeInfo(session: hapi.Session | None = None, node_id: int, part_id: int, volume_info: hapi.VolumeInfo) -> bool

    Set the volume info of a geo on a geo input.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    volume_info:
        All volume information that can be specified per
        volume. This includes the position, orientation, scale,
        data format, tuple size, and taper. The tile size is
        always 8x8x8.
    
    """
def setVolumeTileFloatData(session: Session | None, node_id: int, part_id: int, tile: VolumeTileInfo, values_array: list[float], length: int) -> bool:
    """setVolumeTileFloatData(session: hapi.Session | None = None, node_id: int, part_id: int, tile: hapi.VolumeTileInfo, values_array: list, length: int) -> bool

    Set the values of a float tile: this is an 8x8x8 subsection of
    the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    tile:
        The tile that the volume will be input into.
    

    values_array:
        The values of the individual voxel tiles in the
        volume. The length of this array should
        be ( 8 ^ 3 ) * tupleSize.
    

    length:
        The length should be ( 8 ^ 3 ) * tupleSize.
    
    """
def setVolumeTileFloatData_np(session: Session | None, node_id: int, part_id: int, tile: VolumeTileInfo, values_array: NDArray[numpy.float32], length: int) -> bool:
    """setVolumeTileFloatData_np(session: hapi.Session | None = None, node_id: int, part_id: int, tile: hapi.VolumeTileInfo, values_array: numpy.ndarray[dtype=float32], length: int) -> bool

    Set the values of a float tile: this is an 8x8x8 subsection of
    the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    tile:
        The tile that the volume will be input into.
    

    values_array:
        The values of the individual voxel tiles in the
        volume. The length of this array should
        be ( 8 ^ 3 ) * tupleSize.
    

    length:
        The length should be ( 8 ^ 3 ) * tupleSize.
    
    """
def setVolumeTileIntData(session: Session | None, node_id: int, part_id: int, tile: VolumeTileInfo, values_array: list[int], length: int) -> bool:
    """setVolumeTileIntData(session: hapi.Session | None = None, node_id: int, part_id: int, tile: hapi.VolumeTileInfo, values_array: list, length: int) -> bool

    Set the values of an int tile: this is an 8x8x8 subsection of
    the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    tile:
        The tile that the volume will be input into.
    

    values_array:
        The values of the individual voxel tiles in the
        volume. The length of this array should
        be ( 8 ^ 3 ) * tupleSize.
    

    length:
        The length should be ( 8 ^ 3 ) * tupleSize.
    
    """
def setVolumeTileIntData_np(session: Session | None, node_id: int, part_id: int, tile: VolumeTileInfo, values_array: NDArray[numpy.int32], length: int) -> bool:
    """setVolumeTileIntData_np(session: hapi.Session | None = None, node_id: int, part_id: int, tile: hapi.VolumeTileInfo, values_array: numpy.ndarray[dtype=int32], length: int) -> bool

    Set the values of an int tile: this is an 8x8x8 subsection of
    the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    tile:
        The tile that the volume will be input into.
    

    values_array:
        The values of the individual voxel tiles in the
        volume. The length of this array should
        be ( 8 ^ 3 ) * tupleSize.
    

    length:
        The length should be ( 8 ^ 3 ) * tupleSize.
    
    """
def setVolumeVoxelFloatData(session: Session | None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, values_array: list[float], value_count: int) -> bool:
    """setVolumeVoxelFloatData(session: hapi.Session | None = None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, values_array: list, value_count: int) -> bool

    Set the values of a float voxel in the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    x_index:
        The x index/coordinate of the voxel.
    

    y_index:
        The y index/coordinate of the voxel.
    

    z_index:
        The z index/coordinate of the voxel.
    

    values_array:
        The values of the voxel.
    

    value_count:
        Should be equal to the volume's
        hapi.VolumeInfo.tupleSize.
    
    """
def setVolumeVoxelFloatData_np(session: Session | None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, values_array: NDArray[numpy.float32], value_count: int) -> bool:
    """setVolumeVoxelFloatData_np(session: hapi.Session | None = None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, values_array: numpy.ndarray[dtype=float32], value_count: int) -> bool

    Set the values of a float voxel in the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    x_index:
        The x index/coordinate of the voxel.
    

    y_index:
        The y index/coordinate of the voxel.
    

    z_index:
        The z index/coordinate of the voxel.
    

    values_array:
        The values of the voxel.
    

    value_count:
        Should be equal to the volume's
        hapi.VolumeInfo.tupleSize.
    
    """
def setVolumeVoxelIntData(session: Session | None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, values_array: list[int], value_count: int) -> bool:
    """setVolumeVoxelIntData(session: hapi.Session | None = None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, values_array: list, value_count: int) -> bool

    Set the values of a integer voxel in the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    x_index:
        The x index/coordinate of the voxel.
    

    y_index:
        The y index/coordinate of the voxel.
    

    z_index:
        The z index/coordinate of the voxel.
    

    values_array:
        The values of the voxel.
    

    value_count:
        Should be equal to the volume's
        hapi.VolumeInfo.tupleSize.
    
    """
def setVolumeVoxelIntData_np(session: Session | None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, values_array: NDArray[numpy.int32], value_count: int) -> bool:
    """setVolumeVoxelIntData_np(session: hapi.Session | None = None, node_id: int, part_id: int, x_index: int, y_index: int, z_index: int, values_array: numpy.ndarray[dtype=int32], value_count: int) -> bool

    Set the values of a integer voxel in the volume.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    part_id:
        The part id.
    

    x_index:
        The x index/coordinate of the voxel.
    

    y_index:
        The y index/coordinate of the voxel.
    

    z_index:
        The z index/coordinate of the voxel.
    

    values_array:
        The values of the voxel.
    

    value_count:
        Should be equal to the volume's
        hapi.VolumeInfo.tupleSize.
    
    """
def setWorkItemFloatAttribute(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, values_array: list[float], length: int) -> bool:
    """setWorkItemFloatAttribute(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, values_array: list, length: int) -> bool

    Adds float data to a pending PDG work item attribute for the given node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the pending work item returned by hapi.createWorkItem
    

    attribute_name:
        null-terminated name of the work item attribute
    

    values_array:
        array of float values
    

    length:
        number of values to copy from values_array to the parameter
    
    """
def setWorkItemFloatAttribute_np(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, values_array: NDArray[numpy.float32], length: int) -> bool:
    """setWorkItemFloatAttribute_np(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, values_array: numpy.ndarray[dtype=float32], length: int) -> bool

    Adds float data to a pending PDG work item attribute for the given node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the pending work item returned by hapi.createWorkItem
    

    attribute_name:
        null-terminated name of the work item attribute
    

    values_array:
        array of float values
    

    length:
        number of values to copy from values_array to the parameter
    
    """
def setWorkItemIntAttribute(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, values_array: list[int], length: int) -> bool:
    """setWorkItemIntAttribute(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, values_array: list, length: int) -> bool

    Adds integer data to a pending PDG work item attribute for the given node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the pending work item returned by hapi.createWorkItem
    

    attribute_name:
        null-terminated name of the work item attribute
    

    values_array:
        array of integer values
    

    length:
        number of values to copy from values_array to the parameter
    
    """
def setWorkItemIntAttribute_np(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, values_array: NDArray[numpy.int32], length: int) -> bool:
    """setWorkItemIntAttribute_np(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, values_array: numpy.ndarray[dtype=int32], length: int) -> bool

    Adds integer data to a pending PDG work item attribute for the given node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the pending work item returned by hapi.createWorkItem
    

    attribute_name:
        null-terminated name of the work item attribute
    

    values_array:
        array of integer values
    

    length:
        number of values to copy from values_array to the parameter
    
    """
def setWorkItemStringAttribute(session: Session | None, node_id: int, work_item_id: int, attribute_name: str, data_index: int, value: str) -> bool:
    """setWorkItemStringAttribute(session: hapi.Session | None = None, node_id: int, work_item_id: int, attribute_name: str, data_index: int, value: str) -> bool

    Adds integer data to a pending PDG work item attribute for the given node.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    node_id:
        The node id.
    

    work_item_id:
        The id of the created work item returned by hapi.createWorkItem
    

    attribute_name:
        null-terminated name of the work item attribute
    

    data_index:
        index of the string data member
    

    value:
        null-terminated string to copy to the work item data member
    
    """
def shutdown(session: Session | None = ...) -> bool:
    """shutdown(session: hapi.Session | None = None) -> bool

    When using an in-process session, this method **must** be called in
    order for the host process to shutdown cleanly. This method should
    be called before hapi.closeSession.

    This method should only be called before exiting the program,
    because HAPI can no longer be used by the process once this method
    has been called.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    
    """
def startPerformanceMonitorProfile(session: Session | None, title: str) -> int:
    """startPerformanceMonitorProfile(session: hapi.Session | None = None, title: str) -> int

    Start a Houdini Performance Monitor profile.
    A profile records time and memory statistics from events
    that occur in the Houdini session. A profile records node cooks
    for example; how long it takes to cook a node and how many times
    a node is cooked. Return hapi.result.InvalidArgument if None
    is passed in for the `profile_id` parameter.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    title:
        The title of the profile. If None is passed into this
        parameter, then a default title will be chosen for the
        profile.
    
    """
def startThriftNamedPipeServer(options: ThriftServerOptions, pipe_name: str, log_file: str) -> int:
    """startThriftNamedPipeServer(options: hapi.ThriftServerOptions, pipe_name: str, log_file: str) -> int

    Starts a Thrift RPC server process on the local host serving
    clients on a Windows named pipe or a Unix domain socket and
    waits for it to start serving. It is safe to create an RPC
    session using the specified pipe or socket after this call
    succeeds.



    options:
        Options to configure the server being started.
    

    pipe_name:
        The name of the pipe or socket.
    

    log_file:
        When a filepath is provided for this argument, all logs will
        be appended to the specified file. The specfied path must be
        an absolute path. The server will create any intermediate
        directories in the filepath that do not already exist. When
        this argument is NULL/nullptr, logging will be directed to
        the standard streams.
    
    """
def startThriftSharedMemoryServer(options: ThriftServerOptions, shared_mem_name: str, log_file: str) -> int:
    """startThriftSharedMemoryServer(options: hapi.ThriftServerOptions, shared_mem_name: str, log_file: str) -> int

    Starts a Thrift RPC server process on the localhost serving clients
    by utilizing shared memory to transfer data between the client and
    server and waits for it to start serving.



    options:
        Options to configure the server being started.
    

    shared_mem_name:
        The name of the memory buffer. This must be unique to the
        server in order to avoid any conflicts.
    

    log_file:
        When a filepath is provided for this argument, all logs will
        be appended to the specified file. The specified path must
        be an absolute path. The server will create any intermediate
        directories in the filepath that do not already exist. When
        this argument is NULL/nullptr, logging will be directed to
        the standard streams.
    """
def startThriftSocketServer(options: ThriftServerOptions, port: int, log_file: str) -> int:
    """startThriftSocketServer(options: hapi.ThriftServerOptions, port: int, log_file: str) -> int

    Starts a Thrift RPC server process on the local host serving
    clients on a TCP socket and waits for it to start serving.
    It is safe to create an RPC session on local host using the
    specified port after this call succeeds.


    options:
        Options to configure the server being started.
    

    port:
        The TCP socket to create on the server.
    

    log_file:
        When a filepath is provided for this argument, all logs will
        be appended to the specified file. The specified path must be
        an absolute path. The server will create any intermediate
        directories in the filepath that do not already exist. When
        this argument is NULL/nullptr, logging will be directed to
        the standard streams.
    
    """
def stopPerformanceMonitorProfile(session: Session | None, profile_id: int, file_path: str) -> bool:
    """stopPerformanceMonitorProfile(session: hapi.Session | None = None, profile_id: int, file_path: str) -> bool

    Stop the Performance Monitor profile that matches the given
    profile id and save out the profile's statistics to the specified
    file path on disk. The profile is cleared from memory after its
    statistics are saved to disk. Return hapi.result.InvalidArgument
    if no profile exists for the given id. Return hapi.result.Failure
    if the profile statistics could not be saved out to the specified
    file path. In this case, the profile is stopped but is not cleared
    from memory. You can call
    hapi.stopPerformanceMonitorProfile to attempt saving the
    profile to disk again.



    session:
        The session of Houdini you are interacting with.
        See `hapi.Session` for more on sessions.
        Pass None to just use the default in-process session.
    

    profile_id:
        The id of the profile to stop.
    

    file_path:
        The path to the file where the profile statistics should be
        written to. Use the Performance Monitor file extension,
        .hperf, in the file name (i.e. /path/to/myProfile.hperf).
    
    """
