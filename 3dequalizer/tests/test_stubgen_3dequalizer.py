"""Unit tests for the tde4 stub generator (`stubgen_3dequalizer.py`).

The spec fragments below are **verbatim extracts** from the real WTRL JSON
(only the fields the generator consumes -- `signature.parameters`,
`signature.returns`, `doc_lines` and `doc.Preamble.status` -- are kept).
`test_sample_objects_match_real_spec` re-reads the actual spec (when
`$TDE4_LLM_DOC` points at it) and asserts these samples still match it, so the
fixtures can never silently drift from the file we generate against.
"""

import ast
import json
import os
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest
import stubgen_3dequalizer as stubgen


def _toc(*names: str) -> dict[str, str]:
    """Build a WTRL table-of-contents (name -> JSON pointer), as the real spec does."""
    return {name: f"/__WTRL_OBJECTS__/{name}" for name in names}


def _make_shadowed_vl_sdv_module() -> ModuleType:
    """Build a module with `vl_sdv`-style shadowed bases for tests."""
    module = ModuleType("test_vl_sdv_like")
    module.__file__ = "test_vl_sdv_like.py"
    exec(
        """
class vmcommon:
    pass

class vec(vmcommon):
    def base_method(self):
        return None

class mat(vmcommon):
    pass

class igl:
    def __init__(self, m, v):
        self.m = m
        self.v = v

class vec1d(vec):
    pass

class mat1d(mat):
    vec_type = vec1d

class igl1d(igl):
    vec_type = vec1d
    mat_type = mat1d

def vec(*X):
    return vec1d(*X)

def mat(*X):
    return mat1d(*X)

def igl(m, v):
    return igl1d(m, v)
""",
        module.__dict__,
    )
    return module


# Verbatim `signature` blocks copied from the real spec's `__WTRL_OBJECTS__`,
# keyed by bare function name. These exercise every rendering path: a plain
# accessor, a no-argument query, optional-arg narrowing + tuple->list correction,
# a genuine `| None` return, `*args`, and the return-type override table.
_SIGNATURE_SAMPLES: dict[str, stubgen.SpecObject] = {
    "createCamera": {
        "signature": {
            "parameters": [
                {
                    "name": "mode",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "CameraType_t",
                    "default": None,
                }
            ],
            "returns": "CameraID_t",
        }
    },
    "getCameraFocalLength": {
        "signature": {
            "parameters": [
                {
                    "name": "camera_id",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "CameraID_t",
                    "default": None,
                },
                {
                    "name": "frame",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "int",
                    "default": None,
                },
            ],
            "returns": "float",
        }
    },
    "getSceneRotation3D": {"signature": {"parameters": [], "returns": "Matrix3D_t"}},
    "convertObjectPGroupTransformation3DEToWorld": {
        "signature": {
            "parameters": [
                {
                    "name": "camera_id",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "CameraID_t",
                    "default": None,
                },
                {
                    "name": "frame",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "int",
                    "default": None,
                },
                {
                    "name": "matrix_3d",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "Matrix3D_t",
                    "default": None,
                },
                {
                    "name": "vector_3d",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "Vector3D_t",
                    "default": None,
                },
                {
                    "name": "pgroup_scale",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "float | None",
                    "default": "None",
                },
                {
                    "name": "ignore_scene_node",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "int | None",
                    "default": "None",
                },
            ],
            "returns": "tuple[Matrix3D_t, Vector3D_t]",
        }
    },
    "getPersistentString": {
        "signature": {
            "parameters": [
                {
                    "name": "custom_tag",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "str",
                    "default": None,
                }
            ],
            "returns": "str | None",
        }
    },
    "postQuestionRequester": {
        "signature": {
            "parameters": [
                {
                    "name": "window_title",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "str",
                    "default": None,
                },
                {
                    "name": "message",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "str",
                    "default": None,
                },
                {
                    "name": "label_0",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "str",
                    "default": None,
                },
                {
                    "name": "label_1",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "str",
                    "default": None,
                },
                {
                    "name": "args",
                    "kind": "VAR_POSITIONAL",
                    "annotation": "str",
                    "default": None,
                },
            ],
            "returns": "int",
        }
    },
    "getPGroupRootFrameA": {
        "signature": {
            "parameters": [
                {
                    "name": "pgroup_id",
                    "kind": "POSITIONAL_OR_KEYWORD",
                    "annotation": "PGroupID_t",
                    "default": None,
                }
            ],
            "returns": "list[CameraID_t | int]",
        }
    },
}


# A minimal in-memory spec mirroring the WTRL JSON we consume: dict-shaped TOCs
# (name -> pointer) and per-object detail keyed by qualified name. The objects are
# verbatim extracts (see module docstring); `getCameraZoomingFlag` additionally
# carries the `doc.Preamble.status` we read to flag deprecation.
_SAMPLE_SPEC: stubgen.SpecDocument = {
    "__WTRL_TOC_CALLABLES__": _toc(
        "tde4.createCamera",
        "tde4.getCameraFocalLength",
        "tde4.getCameraZoomingFlag",
        "tde4.getSceneRotation3D",  # -> Matrix3D_t, which pulls in Vector3D_t
        "tde4.WidgetCallbackActionEnum.__init__",  # a method -> must be skipped
    ),
    "__WTRL_TOC_TYPES__": _toc(
        "tde4.CameraID_t",
        "tde4.CameraType_t",
        "tde4.Vector3D_t",
        "tde4.Matrix3D_t",
    ),
    "__WTRL_TOC_CLASSES__": _toc("tde4.WidgetCallbackActionEnum"),
    "__WTRL_TOC_CONSTANTS__": _toc(
        "tde4.WidgetCallbackActionEnum.CLICK",
        "tde4.WidgetCallbackActionEnum.DCLICK",
    ),
    "__WTRL_OBJECTS__": {
        "tde4.CameraID_t": {"doc_lines": ["|type|`str`"]},
        "tde4.CameraType_t": {
            "doc_lines": [
                "Describes the type of a camera object. Required by |func|`tde4.createCamera`.",
                "Possible values are:",
                '* |value|`"SEQUENCE"` - Represents a camera that is defined by a sequence of frames.',
                '* |value|`"REF_FRAME"` - Represents a camera that is defined by a single reference frame.',
                "|",
                "Referenced by:",
                "* |ref|`tde4.createCamera <wtrl://tde4.createCamera>`",
                "* |ref|`tde4.getCameraType <wtrl://tde4.getCameraType>`",
            ]
        },
        "tde4.Vector3D_t": {
            "doc_lines": [
                "|type|`List[float]` with exactly three elements representing the x, y, and z components of a 3D vector."
            ]
        },
        "tde4.Matrix3D_t": {
            "doc_lines": [
                "|type|`List[Vector3D_t]` - 3*3-matrix in |term|`Row_major` layout."
            ]
        },
        "tde4.createCamera": _SIGNATURE_SAMPLES["createCamera"],
        "tde4.getCameraFocalLength": _SIGNATURE_SAMPLES["getCameraFocalLength"],
        "tde4.getCameraZoomingFlag": {
            "signature": {
                "parameters": [
                    {
                        "name": "camera_id",
                        "kind": "POSITIONAL_OR_KEYWORD",
                        "annotation": "CameraID_t",
                        "default": None,
                    }
                ],
                "returns": "int",
            },
            "doc": {"Preamble": {"status": "deprecated"}},
        },
        "tde4.getSceneRotation3D": _SIGNATURE_SAMPLES["getSceneRotation3D"],
    },
}


@pytest.fixture
def spec() -> stubgen.Spec:
    return stubgen.Spec(_SAMPLE_SPEC)


@pytest.fixture
def renderer(spec: stubgen.Spec) -> stubgen.Tde4SpecRenderer:
    return stubgen.Tde4SpecRenderer(spec)


def _real_spec_objects() -> dict[str, Any]:
    """Return `__WTRL_OBJECTS__` from the real doc, or skip if it's unavailable."""
    doc_path = os.getenv("TDE4_LLM_DOC")
    if not doc_path or not (path := Path(doc_path)).is_file():
        pytest.skip("set $TDE4_LLM_DOC to the Python Doc (LLM) JSON to verify samples")

    data = json.loads(path.read_text(encoding="utf-8"))
    return data["__WTRL_OBJECTS__"]


def test_sample_objects_match_real_spec() -> None:
    """Every consumed field of every sample object is verbatim from the real spec.

    Guards against the hand-maintained fixtures drifting away from the actual JSON
    the generator runs against. Only the fields we consume are compared (the real
    objects also carry rich `doc`/`text` we deliberately omit from the samples).
    """
    real = _real_spec_objects()
    samples: dict[str, stubgen.SpecObject] = {
        **_SAMPLE_SPEC["__WTRL_OBJECTS__"],
        **{f"tde4.{name}": obj for name, obj in _SIGNATURE_SAMPLES.items()},
    }

    for qualified_name, sample in samples.items():
        assert qualified_name in real, f"{qualified_name} missing from the real spec"
        actual = real[qualified_name]

        signature = sample.get("signature")
        if signature is not None:
            assert signature.get("parameters") == actual["signature"]["parameters"], (
                f"{qualified_name}.signature.parameters differs from the real spec"
            )
            assert signature.get("returns") == actual["signature"]["returns"], (
                f"{qualified_name}.signature.returns differs from the real spec"
            )

        if "doc_lines" in sample:
            assert sample["doc_lines"] == actual["doc_lines"], (
                f"{qualified_name}.doc_lines differs from the real spec"
            )

        status = sample.get("doc", {}).get("Preamble", {}).get("status")
        if status is not None:
            actual_status = actual.get("doc", {}).get("Preamble", {}).get("status")
            assert status == actual_status, f"{qualified_name} status differs"


def _tuple_members(return_type: str) -> list[str] | None:
    """Return a flat `tuple[...]` return's member types, or `None` if not a tuple.

    Examples:
        `"tuple[Matrix3D_t, Vector3D_t]"` -> `["Matrix3D_t", "Vector3D_t"]`
        `"tuple[float, Vector3D_t] | None"` -> `["float", "Vector3D_t"]`
        `"CameraID_t"` -> `None`
    """
    if not return_type.startswith("tuple["):
        return None

    inner = return_type[len("tuple[") :].split("]", 1)[0]
    return [member.strip() for member in inner.split(",")]


def test_heterogeneous_tuple_returns_have_shape_comment() -> None:
    """Every heterogeneous `tuple[...]` return carries a shape comment, no other.

    3DE returns these fixed-shape tuples as a `list` (corrected in
    `_RETURN_TYPE_OVERRIDES`), which loses the per-position meaning -- so each
    heterogeneous one needs a `_RETURN_SHAPE_COMMENTS` entry to restate it, and
    each homogeneous one must *not* (a comment there would be noise). Re-reads the
    real spec, so a future 3DE version that adds such a return fails here until it
    is documented. Skips without `$TDE4_LLM_DOC`.
    """
    real = _real_spec_objects()

    for qualified_name, obj in real.items():
        bare = stubgen._strip_module_prefix(qualified_name)
        if "." in bare:
            continue  # a method, not a module-level function

        returns = (obj.get("signature") or {}).get("returns")
        members = _tuple_members(returns) if returns else None
        if members is None:
            continue

        heterogeneous = len(set(members)) > 1
        documented = bare in stubgen._RETURN_SHAPE_COMMENTS
        assert heterogeneous == documented, (
            f"{bare} returns {returns}: heterogeneous={heterogeneous} but "
            f"_RETURN_SHAPE_COMMENTS entry={documented} -- add/remove its comment"
        )


@pytest.mark.parametrize(
    "type_name, doc_lines, expected",
    [
        # scalar / container bases come from a `|type|` marker
        ("CameraID_t", ["|type|`str`"], "str"),
        ("Vector3D_t", ["|type|`List[float]` with three elements."], "list[float]"),
        ("Matrix3D_t", ["|type|`List[Vector3D_t]` - 3*3."], "list[Vector3D_t]"),
        # string enums come from `|value|` markers, de-duplicated, order-preserving
        (
            "CameraType_t",
            [
                '* |value|`"SEQUENCE"`',
                '* |value|`"REF_FRAME"`',
                '* |value|`"SEQUENCE"`',
            ],
            'Literal["SEQUENCE", "REF_FRAME"]',
        ),
        # a structured type the markers can't express falls back to an override table
        (
            "LSFResult_t",
            ["prose the resolver can't parse"],
            "list[Vector3D_t | float]",
        ),
        # anything else is left as Incomplete (and logged)
        ("Mystery_t", ["prose, no markers"], "Incomplete"),
    ],
)
def test_resolve_type_alias(
    type_name: str, doc_lines: list[str], expected: str
) -> None:
    assert stubgen._resolve_type_alias(type_name, doc_lines) == expected


def test_spec_defaults_missing_sections_to_empty() -> None:
    empty_spec = stubgen.Spec({})
    assert empty_spec.type_names == set()
    assert empty_spec.callables() == []
    assert empty_spec.enum_classes() == {}
    assert empty_spec.type_doc_lines("Missing_t") == []


def test_spec_callables_skips_methods_and_keeps_toc_order(spec: stubgen.Spec) -> None:
    # Dotted names are methods on a class, not module-level functions, and the rest
    # keep the spec's table-of-contents order.
    assert [name for name, _ in spec.callables()] == [
        "createCamera",
        "getCameraFocalLength",
        "getCameraZoomingFlag",
        "getSceneRotation3D",
    ]


def test_spec_enum_classes_sorts_members_and_classes() -> None:
    spec = stubgen.Spec(
        {
            "__WTRL_TOC_CLASSES__": _toc("tde4.ZEnum", "tde4.AEnum"),
            "__WTRL_TOC_CONSTANTS__": _toc(
                "tde4.ZEnum.ZEBRA",
                "tde4.ZEnum.ALPHA",
                "tde4.AEnum.MIKE",
                "tde4.AEnum.BRAVO",
            ),
        }
    )
    result = spec.enum_classes()

    assert result == {"AEnum": ["BRAVO", "MIKE"], "ZEnum": ["ALPHA", "ZEBRA"]}
    # dict equality ignores key order, so pin the class-name sort separately.
    assert list(result) == ["AEnum", "ZEnum"]


def test_render_enum_classes_renders_memberless_class() -> None:
    # Two real classes (e.g. WidgetShortcutOpcodeEnum) have no documented members
    # and must still produce a valid, non-empty body.
    spec = stubgen.Spec(
        {
            "__WTRL_TOC_CLASSES__": _toc("tde4.EmptyEnum", "tde4.FullEnum"),
            "__WTRL_TOC_CONSTANTS__": _toc("tde4.FullEnum.A", "tde4.FullEnum.B"),
        }
    )
    rendered = "\n".join(stubgen.Tde4SpecRenderer(spec)._render_enum_classes())

    ast.parse(rendered)
    assert "class EmptyEnum:\n    ..." in rendered
    assert "class FullEnum:\n    A: int\n    B: int" in rendered


def test_resolve_all_type_aliases_includes_transitive_closure(
    renderer: stubgen.Tde4SpecRenderer,
) -> None:
    aliases = renderer._resolve_all_type_aliases()

    assert aliases["CameraID_t"] == "str"
    assert aliases["Matrix3D_t"] == "list[Vector3D_t]"
    # Vector3D_t is referenced only by Matrix3D_t's body, not by any signature.
    assert aliases["Vector3D_t"] == "list[float]"


def test_render_type_aliases_emits_shape_comment() -> None:
    # LSFResult_t is a fixed-shape list whose per-element meaning the widened
    # type can't convey, so it is restated as a trailing comment.
    spec = stubgen.Spec(
        {
            "__WTRL_TOC_CALLABLES__": _toc("tde4.calcCameraLSF"),
            "__WTRL_TOC_TYPES__": _toc("tde4.LSFResult_t", "tde4.Vector3D_t"),
            "__WTRL_OBJECTS__": {
                "tde4.LSFResult_t": {"doc_lines": []},
                "tde4.Vector3D_t": {"doc_lines": ["|type|`list[float]`"]},
                "tde4.calcCameraLSF": {
                    "signature": {"parameters": [], "returns": "LSFResult_t"}
                },
            },
        }
    )

    rendered = "\n".join(stubgen.Tde4SpecRenderer(spec)._render_type_aliases())

    assert (
        "LSFResult_t: TypeAlias = list[Vector3D_t | float]  "
        "# [position, rotation (euler), focal length (cm), deviation (px)]"
    ) in rendered


def test_resolve_all_type_aliases_ignores_param_named_like_a_type() -> None:
    # Type discovery scans only the structured annotations/return, so a parameter
    # that happens to be NAMED like a type must not be collected as a reference.
    spec = stubgen.Spec(
        {
            "__WTRL_TOC_CALLABLES__": _toc("tde4.f"),
            "__WTRL_TOC_TYPES__": _toc("tde4.CameraID_t"),
            "__WTRL_OBJECTS__": {
                "tde4.CameraID_t": {"doc_lines": ["|type|`str`"]},
                "tde4.f": {
                    "signature": {
                        "parameters": [
                            {
                                "name": "CameraID_t",
                                "kind": "POSITIONAL_OR_KEYWORD",
                                "annotation": "int",
                                "default": None,
                            }
                        ],
                        "returns": "None",
                    }
                },
            },
        }
    )
    assert stubgen.Tde4SpecRenderer(spec)._resolve_all_type_aliases() == {}


@pytest.mark.parametrize(
    "name, expected",
    [
        (
            "getCameraFocalLength",
            "def getCameraFocalLength(camera_id: CameraID_t, frame: int, /) -> float: ...",
        ),
        ("createCamera", "def createCamera(mode: CameraType_t, /) -> CameraID_t: ..."),
        ("getSceneRotation3D", "def getSceneRotation3D() -> Matrix3D_t: ..."),
        (
            # Two corrections at once: `<type> | None = None` optional args are
            # narrowed to `<type> = ...`, and the `tuple[...]` return (3DE
            # returns a list) becomes `list[<union>]` -- both verified live.
            "convertObjectPGroupTransformation3DEToWorld",
            "def convertObjectPGroupTransformation3DEToWorld("
            "camera_id: CameraID_t, frame: int, matrix_3d: Matrix3D_t,"
            " vector_3d: Vector3D_t, pgroup_scale: float = ...,"
            " ignore_scene_node: int = ..., /) -> list[Matrix3D_t | Vector3D_t]: ..."
            "  # [transform matrix, position]",
        ),
        (
            # A `| None` *return* is genuine and must be preserved.
            "getPersistentString",
            "def getPersistentString(custom_tag: str, /) -> str | None: ...",
        ),
        (
            # `*args` keeps its star prefix and annotation.
            "postQuestionRequester",
            "def postQuestionRequester(window_title: str, message: str, label_0: str,"
            " label_1: str, /, *args: str) -> int: ...",
        ),
        (
            # A return-type override: the spec return omits the None the list can
            # contain (verified live), so _RETURN_TYPE_OVERRIDES corrects it.
            "getPGroupRootFrameA",
            "def getPGroupRootFrameA(pgroup_id: PGroupID_t, /)"
            " -> list[CameraID_t | int | None]: ...",
        ),
    ],
)
def test_build_signature(name: str, expected: str) -> None:
    assert stubgen._build_signature(name, _SIGNATURE_SAMPLES[name]) == expected


def test_build_signature_requires_returns() -> None:
    with pytest.raises(ValueError, match="signature.returns"):
        stubgen._build_signature("f", {"signature": {}})


@pytest.mark.parametrize(
    "name, kind, annotation, default, expected",
    [
        ("frame", "POSITIONAL_OR_KEYWORD", "int", None, "frame: int"),
        # `<type> | None` + a default is narrowed to `<type> = ...`
        ("x", "POSITIONAL_OR_KEYWORD", "int | None", "None", "x: int = ..."),
        # `*args` / `**kwargs` keep their prefixes
        ("args", "VAR_POSITIONAL", "str", None, "*args: str"),
        ("kwargs", "VAR_KEYWORD", None, None, "**kwargs"),
    ],
)
def test_render_parameter(
    name: str, kind: str, annotation: str | None, default: str | None, expected: str
) -> None:
    parameter: stubgen.ParameterSpec = {
        "name": name,
        "kind": kind,
        "annotation": annotation,
        "default": default,
    }
    assert stubgen._render_parameter(parameter) == expected


def test_render_module_produces_valid_python(
    renderer: stubgen.Tde4SpecRenderer,
) -> None:
    module_text = renderer.render()

    ast.parse(module_text)  # must be syntactically valid
    assert module_text.startswith('"""Type stubs for the 3DEqualizer4 `tde4` module.')
    assert "from typing import Literal, TypeAlias" in module_text
    assert "from typing_extensions import deprecated" in module_text
    assert "CameraID_t: TypeAlias = str" in module_text
    assert "Vector3D_t: TypeAlias = list[float]" in module_text
    assert "Matrix3D_t: TypeAlias = list[Vector3D_t]" in module_text
    assert 'CameraType_t: TypeAlias = Literal["SEQUENCE", "REF_FRAME"]' in module_text
    assert "class WidgetCallbackActionEnum:" in module_text
    assert "    CLICK: int" in module_text


def test_render_module_deprecates_only_flagged_functions(
    renderer: stubgen.Tde4SpecRenderer,
) -> None:
    module_text = renderer.render()
    decorator = '@deprecated("deprecated in 3DEqualizer")'
    # the decorator sits immediately above the function the spec flags...
    assert f"{decorator}\ndef getCameraZoomingFlag(" in module_text
    # ...and nowhere else.
    assert module_text.count(decorator) == 1


def test_render_module_imports_incomplete_when_needed() -> None:
    spec = stubgen.Spec(
        {
            "__WTRL_TOC_CALLABLES__": _toc("tde4.getMystery"),
            "__WTRL_TOC_TYPES__": _toc("tde4.Mystery_t"),
            "__WTRL_OBJECTS__": {
                "tde4.Mystery_t": {"doc_lines": ["prose, no markers"]},
                "tde4.getMystery": {
                    "signature": {"parameters": [], "returns": "Mystery_t"}
                },
            },
        }
    )

    module_text = stubgen.Tde4SpecRenderer(spec).render()

    assert "from _typeshed import Incomplete" in module_text
    assert "Mystery_t: TypeAlias = Incomplete" in module_text


def test_render_functions_supplements_absent_math_functions(
    renderer: stubgen.Tde4SpecRenderer,
) -> None:
    rendered = "\n".join(renderer._render_functions())

    assert all(f"def {name}(" in rendered for name in stubgen._SUPPLEMENTAL_FUNCTIONS)
    # atan2 is the only wrapper that isn't `(x: float)`, so pin its exact signature.
    assert "def atan2(y: float, x: float, /) -> float: ..." in rendered


def test_render_functions_skips_supplemental_clashing_with_spec() -> None:
    # If a future spec edition documents a math wrapper, the spec definition wins
    # and the hardcoded supplemental is dropped (rather than emitted twice).
    spec = stubgen.Spec(
        {
            "__WTRL_TOC_CALLABLES__": _toc("tde4.sqrt"),
            "__WTRL_OBJECTS__": {
                "tde4.sqrt": {
                    "signature": {
                        "parameters": [
                            {
                                "name": "value",
                                "kind": "POSITIONAL_OR_KEYWORD",
                                "annotation": "float",
                                "default": None,
                            }
                        ],
                        "returns": "float",
                    }
                }
            },
        }
    )
    rendered = "\n".join(stubgen.Tde4SpecRenderer(spec)._render_functions())

    assert rendered.count("def sqrt(") == 1
    assert "def sqrt(value: float, /) -> float: ..." in rendered  # the spec definition
    assert "def sqrt(x: float" not in rendered  # not the hardcoded wrapper


def test_generate_tde4_writes_package(tmp_path: Path) -> None:
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(_SAMPLE_SPEC), encoding="utf-8")

    out_file = stubgen.Tde4SpecRenderer.from_spec_file(spec_path).write(tmp_path)

    assert out_file == tmp_path / "tde4" / "__init__.pyi"
    ast.parse(out_file.read_text(encoding="utf-8"))


def test_render_vl_sdv_module_handles_shadowed_bases(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = _make_shadowed_vl_sdv_module()
    monkeypatch.setitem(sys.modules, module.__name__, module)

    text = stubgen._render_vl_sdv_module(module)

    ast.parse(stubgen._VL_SDV_HEADER + text)
    # the hidden bases are emitted as private classes and derived classes rebased
    assert "class _vec(vmcommon):" in text
    assert "class _mat(vmcommon):" in text
    assert "class _igl:" in text
    assert "class vec1d(_vec):" in text
    assert "class mat1d(_mat):" in text
    assert "class igl1d(_igl):" in text
    # class-valued attributes stay attributes, not nested classes
    assert "vec_type: ClassVar[type[vec1d]] = ..." in text
    assert "mat_type: ClassVar[type[mat1d]] = ..." in text
    assert "class vec_type(" not in text
    # the shadowing factory functions get the private bases as return types
    assert "def vec(*X) -> _vec: ..." in text
    assert "def mat(*X) -> _mat: ..." in text
    assert "def igl(m, v) -> _igl: ..." in text
    # no type: ignore escape hatch is needed
    assert "type: ignore" not in text


def test_generate_vl_sdv_restores_sys_path(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    tde4_root = tmp_path / "3de"
    vl_sdv_dir = tde4_root / "sys_data" / "py_vl_sdv"
    out_dir = tmp_path / "out"
    vl_sdv_dir.mkdir(parents=True)
    out_dir.mkdir()

    original_sys_path = list(sys.path)
    observed_head: str | None = None
    original_module = ModuleType("vl_sdv")
    module = _make_shadowed_vl_sdv_module()

    def fake_import_module(name: str) -> ModuleType:
        nonlocal observed_head
        observed_head = sys.path[0]
        assert name == "vl_sdv"
        sys.modules[name] = module
        return module

    monkeypatch.setattr(stubgen.importlib, "import_module", fake_import_module)
    monkeypatch.setitem(sys.modules, "vl_sdv", original_module)

    stubgen._generate_vl_sdv(tde4_root, out_dir)

    assert observed_head == str(vl_sdv_dir)
    assert sys.path == original_sys_path
    assert sys.modules["vl_sdv"] is original_module
    text = (out_dir / "vl_sdv.pyi").read_text(encoding="utf-8")
    assert text.startswith(stubgen._VL_SDV_HEADER)
    assert "class vec1d(_vec):" in text
