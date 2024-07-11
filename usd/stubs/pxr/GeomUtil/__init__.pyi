# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.PxOsd
import pxr.Vt
from typing import ClassVar

__MFB_FULL_PACKAGE_NAME: str

class CapsuleMeshGenerator(Boost.Python.instance):
    """
    This class provides an implementation for generating topology and
    point positions on a capsule.


    The simplest form takes a radius and height and is a cylinder capped
    by two hemispheres that is centered at the origin. The generated
    capsule is made up of circular cross-sections in the XY plane. Each
    cross-section has numRadial segments. Successive cross-sections for
    each of the hemispheres are generated at numCapAxial locations along
    the Z and -Z axes respectively. The height is aligned with the Z axis
    and represents the height of just the cylindrical portion.

    An optional transform may be provided to GeneratePoints to orient the
    capsule as necessary (e.g., whose height is along the Y axis).

    An additional overload of GeneratePoints is provided to specify
    different radii and heights for the bottom and top caps, as well as
    the sweep angle for the capsule about the +Z axis. When the sweep is
    less than 360 degrees, the generated geometry is not closed.

    Usage: ::

      const size_t numRadial = 4, numCapAxial = 4;
      const size_t numPoints =
          GeomUtilCapsuleMeshGenerator::ComputeNumPoints(numRadial, numCapAxial);
      const float radius = 1, height = 2;
  
      MyPointContainer<GfVec3f> points(numPoints);
  
      GeomUtilCapsuleMeshGenerator::GeneratePoints(
          points.begin(), numRadial, numCapAxial, radius, height);

    """
    minNumCapAxial: ClassVar[int] = ...  # read-only
    minNumRadial: ClassVar[int] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def ComputeNumPoints(_numRadial: int, _numCapAxial: int, _closedSweep: bool, /) -> int: ...
    @staticmethod
    def GeneratePoints(arg1: int, arg2: int, arg3: float, arg4: float, /) -> pxr.Vt.Vec3fArray: ...
    @staticmethod
    def GenerateTopology(_numRadial: int, _numCapAxial: int, _closedSweep: bool, /) -> pxr.PxOsd.MeshTopology: ...

class ConeMeshGenerator(Boost.Python.instance):
    """
    This class provides an implementation for generating topology and
    point positions on a cone of a given radius and height.


    The cone is made up of circular cross-sections in the XY plane and is
    centered at the origin. Each cross-section has numRadial segments. The
    height is aligned with the Z axis, with the base of the object at Z =
    -h/2 and apex at Z = h/2.

    An optional transform may be provided to GeneratePoints to orient the
    cone as necessary (e.g., whose height is along the Y axis).

    An additional overload of GeneratePoints is provided to specify the
    sweep angle for the cone about the +Z axis. When the sweep is less
    than 360 degrees, the generated geometry is not closed.

    Usage: ::

      const size_t numRadial = 8;
      const size_t numPoints =
          GeomUtilConeMeshGenerator::ComputeNumPoints(numRadial);
      const float radius = 1, height = 2;
  
      MyPointContainer<GfVec3f> points(numPoints);
  
      GeomUtilConeMeshGenerator::GeneratePoints(
          points.begin(), numRadial, radius, height);

    """
    minNumRadial: ClassVar[int] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def ComputeNumPoints(_numRadial: int, _closedSweep: bool, /) -> int: ...
    @staticmethod
    def GeneratePoints(arg1: int, arg2: float, arg3: float, /) -> pxr.Vt.Vec3fArray: ...
    @staticmethod
    def GenerateTopology(_numRadial: int, _closedSweep: bool, /) -> pxr.PxOsd.MeshTopology: ...

class CuboidMeshGenerator(Boost.Python.instance):
    """
    This class provides an implementation for generating topology and
    point positions on a rectangular cuboid given the dimensions along the
    X, Y and Z axes.


    The generated cuboid is centered at the origin.

    An optional transform may be provided to GeneratePoints to orient the
    cuboid as necessary.

    Usage: ::

      const size_t numPoints =
          GeomUtilCuboidMeshGenerator::ComputeNumPoints();
      const float l = 5, b = 4, h = 3;
  
      MyPointContainer<GfVec3f> points(numPoints);
  
      GeomUtilCuboidMeshGenerator::GeneratePoints(
          points.begin(), l, b, h);

    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def ComputeNumPoints() -> int: ...
    @staticmethod
    def GeneratePoints(arg1: float, arg2: float, arg3: float, /) -> pxr.Vt.Vec3fArray: ...
    @staticmethod
    def GenerateTopology() -> pxr.PxOsd.MeshTopology: ...

class CylinderMeshGenerator(Boost.Python.instance):
    """
    This class provides an implementation for generating topology and
    point positions on a cylinder with a given radius and height.


    The cylinder is made up of circular cross-sections in the XY plane and
    is centered at the origin. Each cross-section has numRadial segments.
    The height is aligned with the Z axis, with the base at Z = -h/2.

    An optional transform may be provided to GeneratePoints to orient the
    cone as necessary (e.g., whose height is along the Y axis).

    An additional overload of GeneratePoints is provided to specify
    different radii for the bottom and top discs of the cylinder and a
    sweep angle for cylinder about the +Z axis. When the sweep is less
    than 360 degrees, the generated geometry is not closed.

    Setting one radius to 0 in order to get a cone is inefficient and
    could result in artifacts. Clients should use
    GeomUtilConeMeshGenerator instead. Usage: ::

      const size_t numRadial = 8;
      const size_t numPoints =
          GeomUtilCylinderMeshGenerator::ComputeNumPoints(numRadial);
      const float radius = 1, height = 2;
  
      MyPointContainer<GfVec3f> points(numPoints);
  
      GeomUtilCylinderMeshGenerator::GeneratePoints(
          points.begin(), numRadial, radius, height);

    """
    minNumRadial: ClassVar[int] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def ComputeNumPoints(_numRadial: int, _closedSweep: bool, /) -> int: ...
    @staticmethod
    def GeneratePoints(arg1: int, arg2: float, arg3: float, /) -> pxr.Vt.Vec3fArray: ...
    @staticmethod
    def GenerateTopology(_numRadial: int, _closedSweep: bool, /) -> pxr.PxOsd.MeshTopology: ...

class SphereMeshGenerator(Boost.Python.instance):
    """
    This class provides an implementation for generating topology and
    point positions on a sphere with a given radius.


    The sphere is made up of circular cross-sections in the XY plane and
    is centered at the origin. Each cross-section has numRadial segments.
    Successive cross-sections are generated at numAxial locations along
    the Z axis, with the bottom of the sphere at Z = -r and top at Z = r.

    An optional transform may be provided to GeneratePoints to orient the
    sphere as necessary (e.g., cross-sections in the YZ plane).

    An additional overload of GeneratePoints is provided to specify a
    sweep angle for the sphere about the +Z axis. When the sweep is less
    than 360 degrees, the generated geometry is not closed.

    Usage: ::

      const size_t numRadial = 4, numAxial = 4;
      const size_t numPoints =
          GeomUtilSphereMeshGenerator::ComputeNumPoints(numRadial, numAxial);
      const float radius = 5;
  
      MyPointContainer<GfVec3f> points(numPoints);
  
      GeomUtilSphereMeshGenerator::GeneratePoints(
          points.begin(), numRadial, numAxial, radius);

    """
    minNumAxial: ClassVar[int] = ...  # read-only
    minNumRadial: ClassVar[int] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def ComputeNumPoints(_numRadial: int, _numAxial: int, _closedSweep: bool, /) -> int: ...
    @staticmethod
    def GeneratePoints(arg1: int, arg2: int, arg3: float, /) -> pxr.Vt.Vec3fArray: ...
    @staticmethod
    def GenerateTopology(_numRadial: int, _numAxial: int, _closedSweep: bool, /) -> pxr.PxOsd.MeshTopology: ...
