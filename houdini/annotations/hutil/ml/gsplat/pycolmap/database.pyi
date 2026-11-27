import argparse
import os
import sqlite3
from _typeshed import StrOrBytesPath
from collections.abc import Buffer, Callable, Sequence
from typing import Required, TypedDict, TypeVar, Unpack, overload

import numpy as np
import numpy.typing as npt

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

def array_to_blob(arr: npt.NDArray[np.generic]) -> memoryview: ...
@overload
def blob_to_array(blob: Buffer, dtype: type[_ScalarT], shape: Sequence[int] = ...) -> npt.NDArray[_ScalarT]: ...
@overload
def blob_to_array(blob: Buffer, dtype: npt.DTypeLike, shape: Sequence[int] = ...) -> npt.NDArray[np.generic]: ...
def blob_to_array(blob: Buffer, dtype: npt.DTypeLike, shape: Sequence[int] = ...) -> npt.NDArray[np.generic]: ...

MAX_IMAGE_ID: int

def get_pair_id(image_id1: int, image_id2: int) -> int: ...
def get_image_ids_from_pair_id(pair_id: int) -> tuple[float, int]: ...

CREATE_CAMERAS_TABLE: str
CREATE_DESCRIPTORS_TABLE: str
CREATE_IMAGES_TABLE: str
CREATE_INLIER_MATCHES_TABLE: str
CREATE_KEYPOINTS_TABLE: str
CREATE_MATCHES_TABLE: str
CREATE_NAME_INDEX: str
CREATE_ALL: str

def add_camera(
    db: sqlite3.Connection,
    model: int,
    width: int,
    height: int,
    params: npt.ArrayLike,
    prior_focal_length: bool = ...,
    camera_id: int | None = ...,
) -> None: ...
def add_descriptors(db: sqlite3.Connection, image_id: int, descriptors: npt.ArrayLike) -> None: ...
def add_image(
    db: sqlite3.Connection,
    name: str,
    camera_id: int,
    prior_q: npt.NDArray[np.float64] | Sequence[float] = ...,
    prior_t: npt.NDArray[np.float64] | Sequence[float] = ...,
    image_id: int | None = ...,
) -> None: ...
def add_inlier_matches(
    db: sqlite3.Connection,
    image_id1: int,
    image_id2: int,
    matches: npt.NDArray[np.integer],
    config: int = ...,
    F: npt.ArrayLike | None = ...,
    E: npt.ArrayLike | None = ...,
    H: npt.ArrayLike | None = ...,
) -> None: ...
def add_keypoints(db: sqlite3.Connection, image_id: int, keypoints: npt.NDArray[np.number]) -> None: ...
def add_matches(db: sqlite3.Connection, image_id1: int, image_id2: int, matches: npt.NDArray[np.integer]) -> None: ...

# What COLMAPDatabase forwards to sqlite3.Connection, after the database.
class _ConnectionKwargs(TypedDict, total=False):
    timeout: float
    detect_types: int
    isolation_level: str | None
    check_same_thread: bool
    factory: type[sqlite3.Connection] | None
    cached_statements: int
    uri: bool
    autocommit: bool

class _ConnectionDatabaseKwargs(_ConnectionKwargs, total=False):
    database: Required[StrOrBytesPath]

class COLMAPDatabase(sqlite3.Connection):
    @staticmethod
    def connect(database_path: str | os.PathLike[str]) -> "COLMAPDatabase": ...
    initialize_tables: Callable[[], sqlite3.Cursor]
    initialize_cameras: Callable[[], sqlite3.Cursor]
    initialize_descriptors: Callable[[], sqlite3.Cursor]
    initialize_images: Callable[[], sqlite3.Cursor]
    initialize_inlier_matches: Callable[[], sqlite3.Cursor]
    initialize_keypoints: Callable[[], sqlite3.Cursor]
    initialize_matches: Callable[[], sqlite3.Cursor]
    create_name_index: Callable[[], sqlite3.Cursor]
    @overload
    def __init__(self, *args: Unpack[tuple[StrOrBytesPath]], **kwargs: Unpack[_ConnectionKwargs]) -> None: ...
    @overload
    def __init__(self, *args: Unpack[tuple[()]], **kwargs: Unpack[_ConnectionDatabaseKwargs]) -> None: ...

def main(args: argparse.Namespace) -> None: ...
