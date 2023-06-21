import Boost.Python
from typing import Any

class CapsuleMeshGenerator(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def ComputeNumPoints(cls, arg1: int, arg2: int, arg3: bool) -> int: ...
    @classmethod
    def GeneratePoints(cls, arg1: int, arg2: int, arg3: float, arg4: float) -> Vec3fArray: ...
    @classmethod
    def GenerateTopology(cls, arg1: int, arg2: int, arg3: bool) -> MeshTopology: ...
    def __reduce__(self) -> Any: ...
    @property
    def minNumCapAxial(self) -> Any: ...
    @property
    def minNumRadial(self) -> Any: ...

class ConeMeshGenerator(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def ComputeNumPoints(cls, arg1: int, arg2: bool) -> int: ...
    @classmethod
    def GeneratePoints(cls, arg1: int, arg2: float, arg3: float) -> Vec3fArray: ...
    @classmethod
    def GenerateTopology(cls, arg1: int, arg2: bool) -> MeshTopology: ...
    def __reduce__(self) -> Any: ...
    @property
    def minNumRadial(self) -> Any: ...

class CuboidMeshGenerator(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def ComputeNumPoints(cls) -> int: ...
    @classmethod
    def GeneratePoints(cls, arg1: float, arg2: float, arg3: float) -> Vec3fArray: ...
    @classmethod
    def GenerateTopology(cls) -> MeshTopology: ...
    def __reduce__(self) -> Any: ...

class CylinderMeshGenerator(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def ComputeNumPoints(cls, arg1: int, arg2: bool) -> int: ...
    @classmethod
    def GeneratePoints(cls, arg1: int, arg2: float, arg3: float) -> Vec3fArray: ...
    @classmethod
    def GenerateTopology(cls, arg1: int, arg2: bool) -> MeshTopology: ...
    def __reduce__(self) -> Any: ...
    @property
    def minNumRadial(self) -> Any: ...

class SphereMeshGenerator(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def ComputeNumPoints(cls, arg1: int, arg2: int, arg3: bool) -> int: ...
    @classmethod
    def GeneratePoints(cls, arg1: int, arg2: int, arg3: float) -> Vec3fArray: ...
    @classmethod
    def GenerateTopology(cls, arg1: int, arg2: int, arg3: bool) -> MeshTopology: ...
    def __reduce__(self) -> Any: ...
    @property
    def minNumAxial(self) -> Any: ...
    @property
    def minNumRadial(self) -> Any: ...