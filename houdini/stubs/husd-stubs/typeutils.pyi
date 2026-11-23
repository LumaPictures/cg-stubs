import typing

from typing import TypeAlias
from pxr import Gf
from pxr import Sdf
from pxr import Vt
from typing import TypeAlias
_GfConvertible: TypeAlias = Gf.Vec2d | Gf.Vec2f | Gf.Vec2h | Gf.Vec2i | Gf.Vec3d | Gf.Vec3f | Gf.Vec3h | Gf.Vec3i | Gf.Vec4d | Gf.Vec4f | Gf.Vec4h | Gf.Vec4i | Gf.Size2 | Gf.Size3 | Gf.Matrix2d | Gf.Matrix2f | Gf.Matrix3d | Gf.Matrix3f | Gf.Matrix4d | Gf.Matrix4f | Gf.Quatd | Gf.Quatf | Gf.Quath | Gf.Quaternion | Gf.Range1d | Gf.Range1f | Gf.Range2d | Gf.Range2f | Gf.Range3d | Gf.Range3f | Gf.Transform | Gf.BBox3d
_SdfPyScalar: TypeAlias = bool | int | float | str | Sdf.AssetPath | Sdf.TimeCode | Sdf.PathExpression
_SdfGfScalar: TypeAlias = Gf.Vec2d | Gf.Vec2f | Gf.Vec2h | Gf.Vec2i | Gf.Vec3d | Gf.Vec3f | Gf.Vec3h | Gf.Vec3i | Gf.Vec4d | Gf.Vec4f | Gf.Vec4h | Gf.Vec4i | Gf.Quatd | Gf.Quatf | Gf.Quath | Gf.Matrix2d | Gf.Matrix3d | Gf.Matrix4d
_SdfScalarValue: TypeAlias = _SdfPyScalar | _SdfGfScalar
_SdfArrayValue: TypeAlias = Vt.BoolArray | Vt.UCharArray | Vt.IntArray | Vt.UIntArray | Vt.Int64Array | Vt.UInt64Array | Vt.HalfArray | Vt.FloatArray | Vt.DoubleArray | Vt.StringArray | Vt.TokenArray | Vt.Vec2dArray | Vt.Vec2fArray | Vt.Vec2hArray | Vt.Vec2iArray | Vt.Vec3dArray | Vt.Vec3fArray | Vt.Vec3hArray | Vt.Vec3iArray | Vt.Vec4dArray | Vt.Vec4fArray | Vt.Vec4hArray | Vt.Vec4iArray | Vt.QuatdArray | Vt.QuatfArray | Vt.QuathArray | Vt.Matrix2dArray | Vt.Matrix3dArray | Vt.Matrix4dArray | Sdf.AssetPathArray | Sdf.TimeCodeArray | Sdf.PathExpressionArray
_SdfValue: TypeAlias = _SdfScalarValue | _SdfArrayValue
def isGfType(gfValue: object) -> bool:
    """
    Check if the given value has an valid Gf type.
    """
@typing.overload
def convertFromGf(gfValue: _GfConvertible) -> list[float]: ...
@typing.overload
def convertFromGf(gfValue: object) -> list[float] | None: ...
