from _typeshed import Incomplete
from maya.app.prefs.OptionVar import OPTION_VAR_TYPE_BOOL as OPTION_VAR_TYPE_BOOL, OPTION_VAR_TYPE_FLOAT as OPTION_VAR_TYPE_FLOAT, OPTION_VAR_TYPE_INT as OPTION_VAR_TYPE_INT, OPTION_VAR_TYPE_RGB as OPTION_VAR_TYPE_RGB, OPTION_VAR_TYPE_STRING as OPTION_VAR_TYPE_STRING, OptionVar as OptionVar
from maya.common.utils import Singleton as Singleton

GHOSTING_MODE_PRE_AND_POST_FRAMES: str
GHOSTING_MODE_PRE_FRAMES: str
GHOSTING_MODE_POST_FRAMES: str
GHOSTING_MODE_CUSTOM_FRAMES: str
GHOSTING_MODE_KEYFRAMES: str
GHOSTING_MODE_ALL_KEYFRAMES: str
GHOSTING_MODES: Incomplete
GHOSTING_MODE_ATTRIBUTE_VALUES: Incomplete
GHOSTING_PRESET_1S: str
GHOSTING_PRESET_2S: str
GHOSTING_PRESET_4S: str
GHOSTING_PRESET_5S: str
GHOSTING_PRESET_10S: str
GHOSTING_PRESET_CUSTOM: str
GHOSTING_PRESETS: Incomplete
INDEX_ENUM_ID: int
INDEX_ENUM_NAME: int
INDEX_ENUM_INFO: int
INDEX_ENUM_DATA: int
PREF_CATEGORY: str

class GhostingPreferenceAllInRange(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceCustomFrames(Incomplete):
    ov_id: str
    SIGNAL_DELETE: int
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceEnabled(OptionVar):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceFarOpacity(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceGeometryFilter(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferencePreFrames(OptionVar):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferencePostFrames(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceGhostsStep(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    title_key: Incomplete
    info_key: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceHierarchy(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceJointFilter(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceLocatorFilter(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferenceMode(Incomplete):
    ov_id: str
    DATA: Incomplete
    KEYS: Incomplete
    title: Incomplete
    info: Incomplete
    lookup: Incomplete
    def __init__(self) -> None: ...
    def find_index(self, value): ...

class GhostingPreferenceNearOpacity(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferencePostColour(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferencePreColour(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...

class GhostingPreferencePreset(Incomplete):
    ov_id: str
    DATA: Incomplete
    KEYS: Incomplete
    title: Incomplete
    info: Incomplete
    title_key: Incomplete
    info_key: Incomplete
    lookup: Incomplete
    def __init__(self) -> None: ...
    def find_index(self, value): ...
    def step_preset(self, value): ...

class GhostingPreferenceUseDriver(Incomplete):
    ov_id: str
    title: Incomplete
    info: Incomplete
    def __init__(self) -> None: ...
