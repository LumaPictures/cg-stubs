from ._localization import *

class FileEvent:
    LOCALIZED: int
    REMOVED: int
    CACHE_FULL: int
    DISK_FULL: int
    OUT_OF_DATE: int

class ReadStatus:
    LOCALIZATION_DISABLED: int
    NOT_LOCALIZED: int
    LOCALIZING: int
    PARTIALLY_LOCALIZED: int
    LOCALIZED: int
    OUT_OF_DATE: int
