from typing import Protocol, TypeVar

from pxr import Ar, Gf, Sdf, Usd, Vt


def test_path() -> None:
    # no args:
    path = Sdf.Path()

    # None arg
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


def test_ancestors_range():
    assert Sdf.Path("/SomePath") in Sdf.Path("/SomeOtherPath").GetAncestorsRange()

    assert 1 in "foo"


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
    try:
        path.ReplaceName(arg2="blah")
    except Exception:  # Boost.Python.ArgumentError
        # we except this to fail
        pass


def test_implicit_conversion():
    path = Sdf.Path("foo")

    path.ReplacePrefix(Ar.ResolvedPath("this"), Sdf.Path("that"))


def test_asset_array():
    clips = Usd.ClipsAPI()
    paths = clips.GetClipAssetPaths()
    assert isinstance(paths, list), type(paths)
