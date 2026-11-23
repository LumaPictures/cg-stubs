from typing import Never
__version__: str

class License:
    expires: str
    ip_mask: str
    keyhole: str
    lam: str
    license_id: str
    platform: str
    product: str
    quantity: int
    server_name: str
    start_date: str
    version: str
    def __init__(self, *, no_constructor: Never) -> None: ...
    def simple_product_name(self) -> str:
        """simple_product_name(self: _parsepeakusagelog.License) -> str"""

class LogSection:
    intervals: list[UsageInterval]
    messages: list[str]
    prev_signature: str
    public_key: str
    time_interval_in_s: int
    variables: dict[str, str]
    vbuild: int
    vmaj: int
    vmin: int
    def __init__(self, *, no_constructor: Never) -> None: ...
    def set_version(self, arg0: tuple[int, int, int]) -> None:
        """set_version(self: _parsepeakusagelog.LogSection, arg0: tuple[int, int, int]) -> None"""
    def version_str(self) -> str:
        """version_str(self: _parsepeakusagelog.LogSection) -> str"""
    def version_tuple(self) -> tuple[int, int, int]:
        """version_tuple(self: _parsepeakusagelog.LogSection) -> tuple[int, int, int]"""

class PeakLicenseUsage:
    license: License
    peak: int
    users: set[User]
    def __init__(self, *, no_constructor: Never) -> None: ...

class UsageInterval:
    timestamp: int
    usages: list[PeakLicenseUsage]
    def __init__(self, *, no_constructor: Never) -> None: ...
    def merge(self, interval: UsageInterval, take_max: bool = ...) -> None:
        """merge(self: _parsepeakusagelog.UsageInterval, interval: _parsepeakusagelog.UsageInterval, take_max: bool = False) -> None"""

class UsageLog:
    license_id_to_license: dict[str, License]
    sections: list[LogSection]
    timezone: str
    user_string_to_user: dict[str, User]
    def __init__(self, *, no_constructor: Never) -> None: ...
    def combine_usages_by_product(self, arg0: bool) -> None:
        """combine_usages_by_product(self: _parsepeakusagelog.UsageLog, arg0: bool) -> None"""
    def merge_overlapping_sections(self) -> None:
        """merge_overlapping_sections(self: _parsepeakusagelog.UsageLog) -> None"""
    def merge_to_one_section(self) -> None:
        """merge_to_one_section(self: _parsepeakusagelog.UsageLog) -> None"""
    def remove_section(self, arg0: int) -> None:
        """remove_section(self: _parsepeakusagelog.UsageLog, arg0: int) -> None"""

class User:
    username_and_machine: str
    def __init__(self, *, no_constructor: Never) -> None: ...

def parse(file: str, no_progress_info: bool = ..., export_users: bool = ..., verbosity: int = ...) -> tuple[UsageLog, bool]:
    """parse(file: str, no_progress_info: bool = False, export_users: bool = False, verbosity: int = 0) -> tuple[_parsepeakusagelog.UsageLog, bool]"""
def version_info() -> str:
    """version_info() -> str"""
