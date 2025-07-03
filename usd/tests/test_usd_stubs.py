from stubgenlib.test_helpers import assert_type

from typing import Protocol, TypeVar
import pytest

from pxr import Ar, Gf, Sdf, Usd, Vt


def test_path() -> None:
    # no args:
    path = Sdf.Path()

    with pytest.raises(Exception):
        # actually raises Boost.Python.ArgumentError, but not sure how to access this
        path = Sdf.Path(None)


def test_arrays() -> None:
    ba1 = Vt.BoolArray()
    ba2 = Vt.BoolArray()


T = TypeVar("T", covariant=True)


class SizedItems(Protocol[T]):
    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, item: int) -> T:
        raise NotImplementedError


def is_float_seq(arg: SizedItems[float]) -> None:
    pass


def is_seq_of_float_seq(arg: SizedItems[SizedItems[float]]) -> None:
    pass


def test_matrix() -> None:
    mat4 = Gf.Matrix4d()
    # is_float_seq(mat4)
    is_seq_of_float_seq(mat4)


# def test_ancestors_range():
#     assert Sdf.Path("/SomePath") in Sdf.Path("/SomeOtherPath").GetAncestorsRange()
#
#     assert 1 in "foo"


def test_named_arguments():
    path = Sdf.Path("foo")
    path.GetPrefixes()
    path.GetPrefixes(3)
    # this arg is named within boost-python wrappers, and has a default
    path.GetPrefixes(numPrefixes=3)

    path.ReplacePrefix("this", "that")
    # these args are named within boost-python wrappers, and do not have a default
    path.ReplacePrefix(oldPrefix="this", newPrefix="that")

    path.ReplaceName("blah")

    with pytest.raises(Exception):
        # actually raises Boost.Python.ArgumentError, but not sure how to access this
        path.ReplaceName(arg2="blah")  # type: ignore[call-arg]


def test_implicit_conversion():
    path = Sdf.Path("this/foo")
    new_path = path.ReplacePrefix(Ar.ResolvedPath("this"), Sdf.Path("that"))
    assert str(new_path) == "that/foo"


def test_allowed_tokens():
    stage = Usd.Stage.CreateInMemory()
    root_layer = stage.GetRootLayer()
    primpath = Sdf.Path("/prim_here_please")
    prim_spec = Sdf.CreatePrimInLayer(root_layer, primpath)
    attr_spec = Sdf.AttributeSpec(prim_spec, "tokenList", Sdf.ValueTypeNames.Token)

    assert_type(attr_spec.allowedTokens, list[str])


def test_vector_getitem():
    v = Gf.Vec3f(1.0, 2.0, 3.0)
    dimensions: list[float] = [v[0], v[1], v[2]]
