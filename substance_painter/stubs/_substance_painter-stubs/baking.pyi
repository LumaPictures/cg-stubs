from typing import Any, ClassVar, List, Tuple, Union

class BakingStatus:
    __members__: ClassVar[dict] = ...  # read-only
    Cancel: ClassVar[BakingStatus] = ...
    Fail: ClassVar[BakingStatus] = ...
    Success: ClassVar[BakingStatus] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...

class CurvatureMethod:
    __members__: ClassVar[dict] = ...  # read-only
    FromMesh: ClassVar[CurvatureMethod] = ...
    FromNormalMap: ClassVar[CurvatureMethod] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...

def bake_async(arg0: int) -> None: ...
def baker_parameters(*args, **kwargs) -> Any: ...
def common_parameters(*args, **kwargs) -> Any: ...
def detail_parameters(*args, **kwargs) -> Any: ...
def get_curvature_method(*args, **kwargs) -> Any: ...
def get_enabled_bakers(*args, **kwargs) -> Any: ...
def get_enabled_uv_tiles(arg0: int) -> List[Tuple[int,int]]: ...
def get_link_group(arg0) -> List[int]: ...
def get_link_group_common_parameters() -> List[int]: ...
def get_linked_texture_sets(arg0: int, arg1) -> List[int]: ...
def get_linked_texture_sets_common_parameters(arg0: int) -> List[int]: ...
def is_baker_enabled(arg0: int, arg1) -> bool: ...
def is_textureset_enabled(arg0: int) -> bool: ...
def is_uv_tile_enabled(arg0: int, arg1: Tuple[int,int]) -> bool: ...
def set_baker_enabled(arg0: int, arg1, arg2: bool) -> None: ...
def set_curvature_method(arg0: int, arg1) -> None: ...
def set_enabled_bakers(arg0: int, arg1) -> None: ...
def set_enabled_uv_tiles(arg0: int, arg1: List[Tuple[int,int]]) -> None: ...
def set_linked_group(arg0: List[int], arg1: int, arg2) -> None: ...
def set_linked_group_common_parameters(arg0: List[int], arg1: int) -> None: ...
def set_textureset_enabled(arg0: int, arg1: bool) -> None: ...
def set_tweaks_values(arg0: List[Tuple[int,Union[bool,int,Tuple[int,int],Tuple[int,int,int],Tuple[int,int,int,int],float,Tuple[float,float],Tuple[float,float,float],Tuple[float,float,float,float],str]]]) -> None: ...
def set_uv_tile_enabled(arg0: int, arg1: Tuple[int,int], arg2: bool) -> None: ...
def unlink_all(arg0) -> None: ...
def unlink_all_common_parameters() -> None: ...
