"""Runtime + static checks for the `vl_sdv` stubs.

Each `assert_type` is checked twice: by mypy against the stub and by typeguard
on the runtime value. `vl_sdv` is pure python, so this runs anywhere. The
untyped `vec`/`mat`/`igl` factories and operators (widened to `Any` in the
stub) are covered by runtime value/identity checks instead.
"""

import vl_sdv

from stubgenlib.test_helpers import assert_type


def test_module_version() -> None:
    assert_type(vl_sdv.vl_sdv_version, str)
    assert vl_sdv.vl_sdv_version


def test_apply_order_constants_are_tuples() -> None:
    assert_type(vl_sdv.VL_APPLY_XYZ, tuple)
    assert_type(vl_sdv.VL_APPLY_ZYX, tuple)


def test_construct_vec1d() -> None:
    assert_type(vl_sdv.vec1d(1.0), vl_sdv.vec1d)


def test_construct_vec2d() -> None:
    assert_type(vl_sdv.vec2d(1.0, 2.0), vl_sdv.vec2d)


def test_construct_vec3d() -> None:
    assert_type(vl_sdv.vec3d(1.0, 2.0, 3.0), vl_sdv.vec3d)


def test_construct_vec4d() -> None:
    assert_type(vl_sdv.vec4d(1.0, 2.0, 3.0, 4.0), vl_sdv.vec4d)


def test_construct_mat1d() -> None:
    assert_type(vl_sdv.mat1d(), vl_sdv.mat1d)


def test_construct_mat2d() -> None:
    assert_type(vl_sdv.mat2d(), vl_sdv.mat2d)


def test_construct_mat3d() -> None:
    assert_type(vl_sdv.mat3d(), vl_sdv.mat3d)


def test_construct_mat4d() -> None:
    assert_type(vl_sdv.mat4d(), vl_sdv.mat4d)


def test_construct_igl1d() -> None:
    assert_type(vl_sdv.igl1d(), vl_sdv.igl1d)


def test_construct_igl3d() -> None:
    assert_type(vl_sdv.igl3d(), vl_sdv.igl3d)


def test_construct_quatd() -> None:
    assert_type(vl_sdv.quatd(), vl_sdv.quatd)


def test_construct_rot3d() -> None:
    assert_type(vl_sdv.rot3d(), vl_sdv.rot3d)


def test_construct_vecnd() -> None:
    assert_type(vl_sdv.vecnd(1.0, 2.0, 3.0), vl_sdv.vecnd)


def test_dim_vec1d() -> None:
    assert_type(vl_sdv.vec1d.dim, int)
    assert vl_sdv.vec1d.dim == 1


def test_dim_vec2d() -> None:
    assert_type(vl_sdv.vec2d.dim, int)
    assert vl_sdv.vec2d.dim == 2


def test_dim_vec3d() -> None:
    assert_type(vl_sdv.vec3d.dim, int)
    assert vl_sdv.vec3d.dim == 3


def test_dim_vec4d() -> None:
    assert_type(vl_sdv.vec4d.dim, int)
    assert vl_sdv.vec4d.dim == 4


def test_dim_mat3d() -> None:
    assert_type(vl_sdv.mat3d.dim, int)
    assert vl_sdv.mat3d.dim == 3


def test_dim_igl3d() -> None:
    assert_type(vl_sdv.igl3d.dim, int)
    assert vl_sdv.igl3d.dim == 3


def test_dim_quatd() -> None:
    assert_type(vl_sdv.quatd.dim, int)
    assert vl_sdv.quatd.dim == 4


def test_name_vec3d() -> None:
    assert_type(vl_sdv.vec3d.name, str)
    assert vl_sdv.vec3d.name == "vec3d"


def test_name_mat3d() -> None:
    assert_type(vl_sdv.mat3d.name, str)
    assert vl_sdv.mat3d.name == "mat3d"


def test_name_igl3d() -> None:
    assert_type(vl_sdv.igl3d.name, str)
    assert vl_sdv.igl3d.name == "igl3d"


def test_name_quatd() -> None:
    assert_type(vl_sdv.quatd.name, str)
    assert vl_sdv.quatd.name == "quatd"


def test_name_rot3d() -> None:
    assert_type(vl_sdv.rot3d.name, str)
    assert vl_sdv.rot3d.name == "rot3d"


def test_vec_type_mat1d() -> None:
    assert_type(vl_sdv.mat1d.vec_type, type[vl_sdv.vec1d])
    assert vl_sdv.mat1d.vec_type is vl_sdv.vec1d


def test_vec_type_mat3d() -> None:
    assert_type(vl_sdv.mat3d.vec_type, type[vl_sdv.vec3d])
    assert vl_sdv.mat3d.vec_type is vl_sdv.vec3d


def test_vec_type_quatd() -> None:
    assert_type(vl_sdv.quatd.vec_type, type[vl_sdv.vec3d])
    assert vl_sdv.quatd.vec_type is vl_sdv.vec3d


def test_vec_type_igl3d() -> None:
    assert_type(vl_sdv.igl3d.vec_type, type[vl_sdv.vec3d])
    assert vl_sdv.igl3d.vec_type is vl_sdv.vec3d


def test_mat_type_igl3d() -> None:
    assert_type(vl_sdv.igl3d.mat_type, type[vl_sdv.mat3d])
    assert vl_sdv.igl3d.mat_type is vl_sdv.mat3d


def test_len_vec2d() -> None:
    assert_type(len(vl_sdv.vec2d(1.0, 2.0)), int)
    assert len(vl_sdv.vec2d(1.0, 2.0)) == 2


def test_len_vec3d() -> None:
    assert_type(len(vl_sdv.vec3d(1.0, 2.0, 3.0)), int)
    assert len(vl_sdv.vec3d(1.0, 2.0, 3.0)) == 3


def test_len_vec4d() -> None:
    assert_type(len(vl_sdv.vec4d(1.0, 2.0, 3.0, 4.0)), int)
    assert len(vl_sdv.vec4d(1.0, 2.0, 3.0, 4.0)) == 4


def test_len_mat3d() -> None:
    assert_type(len(vl_sdv.mat3d()), int)
    assert len(vl_sdv.mat3d()) == 3


def needs_vmcommon(value: vl_sdv.vmcommon) -> None:
    """Static-only: a vec/mat must be accepted where a vmcommon base is expected."""


def test_vec3d_is_vmcommon() -> None:
    needs_vmcommon(vl_sdv.vec3d(1.0, 2.0, 3.0))
    assert isinstance(vl_sdv.vec3d(1.0, 2.0, 3.0), vl_sdv.vmcommon)


def test_mat3d_is_vmcommon() -> None:
    needs_vmcommon(vl_sdv.mat3d())
    assert isinstance(vl_sdv.mat3d(), vl_sdv.vmcommon)


def test_quatd_is_vmcommon() -> None:
    assert isinstance(vl_sdv.quatd(), vl_sdv.vmcommon)


def _coords3(vec: object) -> list[float]:
    return [vec[i] for i in range(3)]  # type: ignore[index]


def test_vec_indexing_values() -> None:
    v = vl_sdv.vec3d(1.0, 2.0, 3.0)
    assert v[0] == 1.0
    assert v[2] == 3.0


def test_vec_addition_returns_same_type() -> None:
    result = vl_sdv.vec3d(1.0, 2.0, 3.0) + vl_sdv.vec3d(4.0, 5.0, 6.0)
    assert isinstance(result, vl_sdv.vec3d)
    assert _coords3(result) == [5.0, 7.0, 9.0]


def test_vec_subtraction_values() -> None:
    result = vl_sdv.vec3d(4.0, 5.0, 6.0) - vl_sdv.vec3d(1.0, 2.0, 3.0)
    assert _coords3(result) == [3.0, 3.0, 3.0]


def test_vec_scalar_multiplication() -> None:
    result = vl_sdv.vec3d(1.0, 2.0, 3.0) * 2.0
    assert _coords3(result) == [2.0, 4.0, 6.0]


def test_vec_negation() -> None:
    result = -vl_sdv.vec3d(1.0, -2.0, 3.0)
    assert _coords3(result) == [-1.0, 2.0, -3.0]


def test_module_dot_product() -> None:
    result = vl_sdv.dot(vl_sdv.vec3d(1.0, 0.0, 0.0), vl_sdv.vec3d(1.0, 0.0, 0.0))
    assert result == 1.0


def test_module_norm2_of_unit_vector() -> None:
    assert vl_sdv.norm2(vl_sdv.vec3d(0.0, 3.0, 4.0)) == 5.0


def test_module_unit_is_normalized() -> None:
    unit = vl_sdv.unit(vl_sdv.vec3d(0.0, 0.0, 2.0))
    assert _coords3(unit) == [0.0, 0.0, 1.0]


def test_factory_vec_dispatches_on_arity() -> None:
    # Edge case: the vec() factory returns a concrete subclass by argument count
    # (the stub widens its return to the _vec base).
    assert isinstance(vl_sdv.vec(1.0, 2.0), vl_sdv.vec2d)
    assert isinstance(vl_sdv.vec(1.0, 2.0, 3.0), vl_sdv.vec3d)
