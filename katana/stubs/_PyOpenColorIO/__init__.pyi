# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Any, Set, Tuple

hexversion: int
version: str

class AllocationTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def getAllocation(self) -> Any: ...
    def getNumVars(self, *args, **kwargs): ...
    def getVars(self) -> Any: ...
    def setAllocation(self, hwalloc) -> Any: ...
    def setVars(self, pyvars) -> Any: ...

class Baker:
    def __init__(self, *args, **kwargs) -> None: ...
    def bake(self, *args, **kwargs): ...
    def createEditableCopy(self, *args, **kwargs): ...
    def getConfig(self, *args, **kwargs): ...
    def getCubeSize(self, *args, **kwargs): ...
    def getFormat(self, *args, **kwargs): ...
    def getFormatExtensionByIndex(self, *args, **kwargs): ...
    def getFormatNameByIndex(self, *args, **kwargs): ...
    def getInputSpace(self, *args, **kwargs): ...
    def getLooks(self, *args, **kwargs): ...
    def getMetadata(self, *args, **kwargs): ...
    def getNumFormats(self, *args, **kwargs): ...
    def getShaperSize(self, *args, **kwargs): ...
    def getShaperSpace(self, *args, **kwargs): ...
    def getTargetSpace(self, *args, **kwargs): ...
    def getType(self, *args, **kwargs): ...
    def isEditable(self, *args, **kwargs): ...
    def setConfig(self, *args, **kwargs): ...
    def setCubeSize(self, *args, **kwargs): ...
    def setFormat(self, *args, **kwargs): ...
    def setInputSpace(self, *args, **kwargs): ...
    def setLooks(self, *args, **kwargs): ...
    def setMetadata(self, *args, **kwargs): ...
    def setShaperSize(self, *args, **kwargs): ...
    def setShaperSpace(self, *args, **kwargs): ...
    def setTargetSpace(self, *args, **kwargs): ...
    def setType(self, *args, **kwargs): ...

class CDLTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def CreateFromFile(self, *args, **kwargs): ...
    def equals(self, *args, **kwargs): ...
    def getDescription(self) -> Any: ...
    def getID(self) -> Any: ...
    def getOffset(self, *args, **kwargs): ...
    def getPower(self, *args, **kwargs): ...
    def getSOP(self, *args, **kwargs): ...
    def getSat(self, *args, **kwargs): ...
    def getSatLumaCoefs(self, pyData) -> Any: ...
    def getSlope(self, *args, **kwargs): ...
    def getXML(self, *args, **kwargs): ...
    def setDescription(self, str) -> Any: ...
    def setID(self, str) -> Any: ...
    def setOffset(self, pyData) -> Any: ...
    def setPower(self, pyData) -> Any: ...
    def setSOP(self, pyData) -> Any: ...
    def setSat(self, *args, **kwargs): ...
    def setSlope(self, pyData) -> Any: ...
    def setXML(self, *args, **kwargs): ...

class ColorSpace:
    def __init__(self, *args, **kwargs) -> None: ...
    def createEditableCopy(self, *args, **kwargs): ...
    def getAllocation(self, *args, **kwargs): ...
    def getAllocationVars(self, *args, **kwargs): ...
    def getBitDepth(self, *args, **kwargs): ...
    def getDescription(self, *args, **kwargs): ...
    def getEqualityGroup(self, *args, **kwargs): ...
    def getFamily(self, *args, **kwargs): ...
    def getName(self, *args, **kwargs): ...
    def getTransform(self, *args, **kwargs): ...
    def isData(self, *args, **kwargs): ...
    def isEditable(self, *args, **kwargs): ...
    def setAllocation(self, *args, **kwargs): ...
    def setAllocationVars(self, *args, **kwargs): ...
    def setBitDepth(self, *args, **kwargs): ...
    def setDescription(self, *args, **kwargs): ...
    def setEqualityGroup(self, *args, **kwargs): ...
    def setFamily(self, *args, **kwargs): ...
    def setIsData(self, *args, **kwargs): ...
    def setName(self, *args, **kwargs): ...
    def setTransform(self, *args, **kwargs): ...

class ColorSpaceTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def getDst(self) -> Any: ...
    def getSrc(self) -> Any: ...
    def setDst(self, dstname) -> Any: ...
    def setSrc(self, srcname) -> Any: ...

class Config:
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def CreateFromEnv(cls) -> Any: ...
    @classmethod
    def CreateFromFile(cls, filename) -> Any: ...
    @classmethod
    def CreateFromStream(cls, *args, **kwargs): ...
    def addColorSpace(self, pyColorSpace) -> Any: ...
    def addDisplay(self, *args, **kwargs): ...
    def addEnvironmentVar(self, *args, **kwargs): ...
    def addLook(self, pylook) -> Any: ...
    def clearColorSpaces(self) -> Any: ...
    def clearDisplays(self) -> Any: ...
    def clearEnvironmentVars(self, *args, **kwargs): ...
    def clearLook(self, *args, **kwargs): ...
    def clearLooks(self) -> Any: ...
    def createEditableCopy(self) -> Any: ...
    def getActiveDisplays(self) -> Any: ...
    def getActiveViews(self) -> Any: ...
    def getCacheID(self, *args, **kwargs): ...
    def getColorSpace(self, name) -> Any: ...
    def getColorSpaceNameByIndex(self, *args, **kwargs): ...
    def getColorSpaces(self) -> Any: ...
    def getCurrentContext(self) -> Any: ...
    def getDefaultDisplay(self) -> Any: ...
    def getDefaultLumaCoefs(self) -> Any: ...
    def getDefaultView(self, display) -> Any: ...
    def getDescription(self) -> Any: ...
    def getDisplay(self, *args, **kwargs): ...
    def getDisplayColorSpaceName(self, display, view) -> Any: ...
    def getDisplayLooks(self, display, view) -> Any: ...
    def getDisplays(self) -> Any: ...
    def getEnvironmentVarDefault(self, *args, **kwargs): ...
    def getEnvironmentVarDefaults(self, *args, **kwargs): ...
    def getEnvironmentVarNameByIndex(self, *args, **kwargs): ...
    def getIndexForColorSpace(self, *args, **kwargs): ...
    def getLook(self, str) -> Any: ...
    def getLookNameByIndex(self, *args, **kwargs): ...
    def getLooks(self) -> Any: ...
    def getNumColorSpaces(self, *args, **kwargs): ...
    def getNumDisplays(self, *args, **kwargs): ...
    def getNumEnvironmentVars(self, *args, **kwargs): ...
    def getNumLooks(self, *args, **kwargs): ...
    def getNumRoles(self, *args, **kwargs): ...
    def getNumViews(self, *args, **kwargs): ...
    def getProcessor(self, *args, **kwargs): ...
    def getRoleName(self, *args, **kwargs): ...
    def getSearchPath(self) -> Any: ...
    def getView(self, *args, **kwargs): ...
    def getViews(self, display) -> Any: ...
    def getWorkingDir(self) -> Any: ...
    def hasRole(self, *args, **kwargs): ...
    def isEditable(self) -> Any: ...
    def isStrictParsingEnabled(self, *args, **kwargs): ...
    def parseColorSpaceFromString(self, str) -> Any: ...
    def sanityCheck(self) -> Any: ...
    def serialize(self) -> Any: ...
    def setActiveDisplays(self, displays) -> Any: ...
    def setActiveViews(self, views) -> Any: ...
    def setDefaultLumaCoefs(self, pyCoef) -> Any: ...
    def setDescription(self, desc) -> Any: ...
    def setRole(self, role, csname) -> Any: ...
    def setSearchPath(self, path) -> Any: ...
    def setStrictParsingEnabled(self, *args, **kwargs): ...
    def setWorkingDir(self, path) -> Any: ...

class Context:
    def __init__(self, *args, **kwargs) -> None: ...
    def clearStringVars(self, *args, **kwargs): ...
    def createEditableCopy(self, *args, **kwargs): ...
    def getCacheID(self, *args, **kwargs): ...
    def getEnvironmentMode(self, *args, **kwargs): ...
    def getNumStringVars(self, *args, **kwargs): ...
    def getSearchPath(self, *args, **kwargs): ...
    def getStringVar(self, *args, **kwargs): ...
    def getStringVarNameByIndex(self, *args, **kwargs): ...
    def getWorkingDir(self, *args, **kwargs): ...
    def isEditable(self, *args, **kwargs): ...
    def loadEnvironment(self, *args, **kwargs): ...
    def resolveFileLocation(self, *args, **kwargs): ...
    def resolveStringVar(self, *args, **kwargs): ...
    def setEnvironmentMode(self, *args, **kwargs): ...
    def setSearchPath(self, *args, **kwargs): ...
    def setStringVar(self, *args, **kwargs): ...
    def setWorkingDir(self, *args, **kwargs): ...

class DisplayTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def getChannelView(self) -> Any: ...
    def getColorTimingCC(self) -> Any: ...
    def getDisplay(self) -> Any: ...
    def getDisplayCC(self) -> Any: ...
    def getInputColorSpaceName(self) -> Any: ...
    def getLinearCC(self) -> Any: ...
    def getLooksOverride(self) -> Any: ...
    def getLooksOverrideEnabled(self) -> Any: ...
    def getView(self) -> Any: ...
    def setChannelView(self, pyCC) -> Any: ...
    def setColorTimingCC(self, pyCC) -> Any: ...
    def setDisplay(self, str) -> Any: ...
    def setDisplayCC(self, pyCC) -> Any: ...
    def setInputColorSpaceName(self, name) -> Any: ...
    def setLinearCC(self, pyCC) -> Any: ...
    def setLooksOverride(self, str) -> Any: ...
    def setLooksOverrideEnabled(self, enabled) -> Any: ...
    def setView(self, str) -> Any: ...

class Exception(Exception): ...

class ExceptionMissingFile(Exception): ...

class ExponentTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def getValue(self) -> Any: ...
    def setValue(self) -> Any: ...

class FileTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def getCCCId(self, *args, **kwargs): ...
    def getFormatExtensionByIndex(self, *args, **kwargs): ...
    def getFormatNameByIndex(self, *args, **kwargs): ...
    def getInterpolation(self, *args, **kwargs): ...
    def getNumFormats(self, *args, **kwargs): ...
    def getSrc(self, *args, **kwargs): ...
    def setCCCId(self, *args, **kwargs): ...
    def setInterpolation(self, *args, **kwargs): ...
    def setSrc(self, *args, **kwargs): ...

class GpuShaderDesc:
    def __init__(self, *args, **kwargs) -> None: ...
    def getCacheID(self, *args, **kwargs): ...
    def getFunctionName(self, *args, **kwargs): ...
    def getLanguage(self, *args, **kwargs): ...
    def getLut3DEdgeLen(self, *args, **kwargs): ...
    def setFunctionName(self, *args, **kwargs): ...
    def setLanguage(self, *args, **kwargs): ...
    def setLut3DEdgeLen(self, *args, **kwargs): ...

class GroupTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def clear(self, *args, **kwargs): ...
    def empty(self, *args, **kwargs): ...
    def getTransform(self, *args, **kwargs): ...
    def getTransforms(self, *args, **kwargs): ...
    def push_back(self, *args, **kwargs): ...
    def setTransforms(self, *args, **kwargs): ...
    def size(self, *args, **kwargs): ...

class LogTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def getBase(self) -> Any: ...
    def setBase(self, base) -> Any: ...

class Look:
    def __init__(self, *args, **kwargs) -> None: ...
    def createEditableCopy(self, *args, **kwargs): ...
    def getDescription(self, *args, **kwargs): ...
    def getInverseTransform(self, *args, **kwargs): ...
    def getName(self, *args, **kwargs): ...
    def getProcessSpace(self, *args, **kwargs): ...
    def getTransform(self, *args, **kwargs): ...
    def isEditable(self, *args, **kwargs): ...
    def setDescription(self, *args, **kwargs): ...
    def setInverseTransform(self, *args, **kwargs): ...
    def setName(self, *args, **kwargs): ...
    def setProcessSpace(self, *args, **kwargs): ...
    def setTransform(self, *args, **kwargs): ...

class LookTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    def getDst(self, *args, **kwargs): ...
    def getLooks(self, *args, **kwargs): ...
    def getSrc(self, *args, **kwargs): ...
    def setDst(self, *args, **kwargs): ...
    def setLooks(self, *args, **kwargs): ...
    def setSrc(self, *args, **kwargs): ...

class MatrixTransform(Transform):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def Fit(cls, *args, **kwargs): ...
    @classmethod
    def Identity(cls, *args, **kwargs): ...
    @classmethod
    def Sat(cls, *args, **kwargs): ...
    @classmethod
    def Scale(cls, *args, **kwargs): ...
    @classmethod
    def View(cls, *args, **kwargs): ...
    def equals(self, *args, **kwargs): ...
    def getMatrix(self, *args, **kwargs): ...
    def getOffset(self, *args, **kwargs): ...
    def getValue(self, *args, **kwargs): ...
    def setMatrix(self, *args, **kwargs): ...
    def setOffset(self, *args, **kwargs): ...
    def setValue(self, *args, **kwargs): ...

class Processor:
    def __init__(self, *args, **kwargs) -> None: ...
    def applyRGB(self, pixeldata) -> Any: ...
    def applyRGBA(self, pixeldata) -> Any: ...
    def getCpuCacheID(self) -> Any: ...
    def getGpuLut3D(self, shaderDesc) -> Any: ...
    def getGpuLut3DCacheID(self, shaderDesc) -> Any: ...
    def getGpuShaderText(self, shaderDesc) -> Any: ...
    def getGpuShaderTextCacheID(self, shaderDesc) -> Any: ...
    def getMetadata(self) -> Any: ...
    def hasChannelCrosstalk(self) -> Any: ...
    def isNoOp(self) -> Any: ...

class ProcessorMetadata:
    def __init__(self, *args, **kwargs) -> None: ...
    def getFiles(self) -> Any: ...
    def getLooks(self) -> Any: ...

class Transform:
    def __init__(self, *args, **kwargs) -> None: ...
    def createEditableCopy(self, *args, **kwargs): ...
    def getDirection(self, *args, **kwargs): ...
    def isEditable(self, *args, **kwargs): ...
    def setDirection(self, *args, **kwargs): ...

def ClearAllCaches(*args, **kwargs): ...
def GetCurrentConfig(*args, **kwargs): ...
def GetLoggingLevel(*args, **kwargs): ...
def SetCurrentConfig(*args, **kwargs): ...
def SetLoggingLevel(*args, **kwargs): ...
