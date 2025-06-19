from .signal_helpers import connect as connect, disconnect as disconnect
from _typeshed import Incomplete

VERBOSE_ENABLED: bool

class MessageType:
    DEBUG: int
    INFO: int
    WARNING: int
    ERROR: int

def printMessage(type, message) -> None: ...
def configFileFilter(): ...
def lutFileFilter(): ...

LUT_PATH_DEFAULT: str
LUT_FILE_LIST_DEFAULT: Incomplete
CONFIG_PATH_DEFAULT: Incomplete
CONFIG_FILE_LIST_RESET: Incomplete
CONFIG_FILE_LIST_DEFAULT: Incomplete
SQRT_TWO: Incomplete
EXTRAPOLATE_DEFAULT: bool
ENABLED_RESET: bool
ENABLED_DEFAULT = ENABLED_RESET
PROFILE_RESET: str
PROFILE_DEFAULT = PROFILE_RESET
SWIZZLE_TYPES: Incomplete
SWIZZLE_MASK: Incomplete
SWIZZLE_GLSL: Incomplete
SWIZZLE_DEFAULT: Incomplete
FSTOP_STEP_SIZE: float
FSTOP_CENTER_MIN: float
FSTOP_CENTER_MAX: float
FSTOP_CENTER_STEP_SIZE: float
FSTOP_CENTER_RESET: float
FSTOP_CENTER = FSTOP_CENTER_RESET
EXPOSURE_MIN: Incomplete
EXPOSURE_MAX: Incomplete
EXPOSURE_DELTA: Incomplete
EXPOSURE_STEP_SIZE: float
GAIN_DEFAULT: float
GAIN_MIN: Incomplete
GAIN_MAX: Incomplete
GAIN_STEP_SIZE: float
GAIN_PRECISION: int
GAMMA_DEFAULT: float
GAMMA_MIN: float
GAMMA_MAX: float
GAMMA_STEP_SIZE: float
GAMMA_PRECISION: int
CONFIG_DEFAULT: Incomplete
INPUT_COLORSPACE_DEFAULT: str
COLOR_DISPLAY_DEFAULT: str
SCALAR_DISPLAY_DEFAULT: str
OCIO_ENV_VAR_SET: bool

def registerFStopCenterChanged(function) -> None: ...
def convertExposureToGain(exposure): ...
def convertGainToExposure(gain): ...
def convertExposureToFStop(exposure): ...
def convertGainToFStop(gain): ...
def buildEmptyFilter(filter) -> None: ...
def buildProcessorFilter(processor, filter, filter_cache_id, texture_cache_id, lut_size: int = ..., extrapolate: bool = ..., force_shader_build: bool = ..., swizzle: Incomplete | None = ..., lut: Incomplete | None = ..., update_lut: bool = ...): ...
def loadConfig(path, display_message_box: bool = ..., message_box_title: str = ...): ...
def defaultInputColorspace(config): ...
def activeViewDisplays(config): ...
def defaultViewDisplay(config, scalar): ...
def buildSavePath(path): ...
def buildLoadPath(path): ...

config_path: Incomplete
CONFIG_PATH_DEFAULT = config_path
message: Incomplete
