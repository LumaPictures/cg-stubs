"""Runtime + static checks for the `tde4` stubs.

Each `assert_type` is checked by mypy against the stub and, at runtime under
pytest, by typeguard. `tde4` only exists inside 3DE, so these run there via
`tests_live/run_tests.py`.
"""

import pathlib
from typing import Literal

import pytest
import tde4

from stubgenlib.test_helpers import assert_type

# Identity matrix / zero vector for the transform calls.
_I3 = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
_V0 = [0.0, 0.0, 0.0]

# A distortion model that ships with every 3DE install, for the LD-model accessors.
_LD_MODEL = "3DE4 Radial - Standard, Degree 4"

_RESOURCES = pathlib.Path(__file__).parent / "resources"
_OBJ = str(_RESOURCES / "cube.obj")
_PLATE = str(_RESOURCES / "plate" / "plate.####.jpg")
_PLATE_START, _PLATE_END = 1, 3


@pytest.fixture
def camera() -> str:
    return tde4.createCamera("SEQUENCE")


@pytest.fixture
def pgroup() -> str:
    return tde4.createPGroup("CAMERA")


@pytest.fixture
def point(pgroup: str) -> str:
    return tde4.createPoint(pgroup)


@pytest.fixture
def lens() -> str:
    return tde4.createLens()


@pytest.fixture
def requester() -> str:
    return tde4.createCustomRequester()


@pytest.fixture
def populated_requester() -> str:
    # A requester with a few widgets so widget-value accessors have something real.
    req = tde4.createCustomRequester()
    tde4.addToggleWidget(req, "tog", "Toggle", 1)
    tde4.addTextFieldWidget(req, "txt", "Text", "hello")

    return req


@pytest.fixture
def list_requester() -> str:
    # A requester with a list widget holding one item, so item accessors resolve.
    req = tde4.createCustomRequester()
    tde4.addListWidget(req, "lst", "List", 0)

    # tde4 builtins are positional-only: pass userdata then item_type.
    tde4.insertListWidgetItem(req, "lst", "item", 0, "LIST_ITEM_ATOM")

    return req


@pytest.fixture
def model(pgroup: str) -> tuple[str, str]:
    # The point group with the resources/ OBJ imported as a 3D model.
    model_id = tde4.create3DModel(pgroup)
    tde4.importOBJ3DModel(pgroup, model_id, _OBJ)

    return pgroup, model_id


@pytest.fixture
def camera_with_plate() -> str:
    # A camera with the resources/ plate loaded, so it has real pixels to work on.
    cam = tde4.createCamera("SEQUENCE")
    tde4.setCameraPath(cam, _PLATE)
    tde4.setCameraSequenceAttr(cam, _PLATE_START, _PLATE_END, 1)

    return cam


def test_install_path_is_str() -> None:
    assert_type(tde4.get3DEInstallPath(), str)


def test_version_is_str() -> None:
    assert_type(tde4.get3DEVersion(), str)


def test_project_notes_is_str() -> None:
    assert_type(tde4.getProjectNotes(), str)


def test_near_clipping_plane_is_float() -> None:
    assert_type(tde4.getNearClippingPlane(), float)


def test_far_clipping_plane_is_float() -> None:
    assert_type(tde4.getFarClippingPlane(), float)


def test_motionblur_samples_is_int() -> None:
    assert_type(tde4.getMotionblurRenderingSamples(), int)


def test_line_rendering_width_is_float() -> None:
    assert_type(tde4.getLineRenderingWidth(), float)


def test_persistent_tags_is_list_of_str() -> None:
    assert_type(tde4.getPersistentTags(), list[str])


def test_camera_name_is_str(camera: str) -> None:
    assert_type(tde4.getCameraName(camera), str)


def test_camera_path_is_str(camera: str) -> None:
    assert_type(tde4.getCameraPath(camera), str)


def test_camera_selection_flag_is_int(camera: str) -> None:
    assert_type(tde4.getCameraSelectionFlag(camera), int)


def test_camera_enabled_flag_is_int(camera: str) -> None:
    assert_type(tde4.getCameraEnabledFlag(camera), int)


def test_camera_no_frames_is_int(camera: str) -> None:
    assert_type(tde4.getCameraNoFrames(camera), int)


def test_camera_image_width_is_int(camera: str) -> None:
    assert_type(tde4.getCameraImageWidth(camera), int)


def test_camera_image_height_is_int(camera: str) -> None:
    assert_type(tde4.getCameraImageHeight(camera), int)


def test_camera_fps_is_float(camera: str) -> None:
    assert_type(tde4.getCameraFPS(camera), float)


def test_camera_timeshift_is_float(camera: str) -> None:
    assert_type(tde4.getCameraTimeshift(camera), float)


def test_camera_zoom_curve_alias_is_str(camera: str) -> None:
    # CurveID_t is a semantic alias for str.
    assert_type(tde4.getCameraZoomCurve(camera), str)


def test_camera_sequence_attr_is_list_of_int(camera: str) -> None:
    assert_type(tde4.getCameraSequenceAttr(camera), list[int])


def test_camera_fov_is_list_of_float(camera: str) -> None:
    assert_type(tde4.getCameraFOV(camera), list[float])


def test_camera_matrix_dimensions_is_list_of_int(camera: str) -> None:
    assert_type(tde4.getCameraMatrixDimensions(camera), list[int])


def test_current_frame_is_int(camera: str) -> None:
    assert_type(tde4.getCurrentFrame(camera), int)


def test_pgroup_name_is_str(pgroup: str) -> None:
    assert_type(tde4.getPGroupName(pgroup), str)


def test_pgroup_selection_flag_is_int(pgroup: str) -> None:
    assert_type(tde4.getPGroupSelectionFlag(pgroup), int)


def test_pgroup_enabled_flag_is_int(pgroup: str) -> None:
    assert_type(tde4.getPGroupEnabledFlag(pgroup), int)


def test_pgroup_scale_is_float(pgroup: str) -> None:
    assert_type(tde4.getPGroupScale3D(pgroup), float)


def test_pgroup_postfilter_value_is_float(pgroup: str) -> None:
    assert_type(tde4.getPGroupPostfilterValue(pgroup), float)


def test_pgroup_persistent_id_is_int(pgroup: str) -> None:
    assert_type(tde4.getPGroupPersistentID(pgroup), int)


def test_point_name_is_str(pgroup: str, point: str) -> None:
    assert_type(tde4.getPointName(pgroup, point), str)


def test_point_selection_flag_is_int(pgroup: str, point: str) -> None:
    assert_type(tde4.getPointSelectionFlag(pgroup, point), int)


def test_point_weight_is_float(pgroup: str, point: str) -> None:
    assert_type(tde4.getPointWeight(pgroup, point), float)


def test_point_color2d_is_int(pgroup: str, point: str) -> None:
    assert_type(tde4.getPointColor2D(pgroup, point), int)


def test_point_color3d_is_int(pgroup: str, point: str) -> None:
    assert_type(tde4.getPointColor3D(pgroup, point), int)


def test_point_survey_position_is_list_of_float(pgroup: str, point: str) -> None:
    # Vector3D_t is a semantic alias for list[float].
    assert_type(tde4.getPointSurveyPosition3D(pgroup, point), list[float])


def test_point_calc_position_is_list_of_float(pgroup: str, point: str) -> None:
    assert_type(tde4.getPointCalcPosition3D(pgroup, point), list[float])


def test_camera_list_is_list() -> None:
    assert_type(tde4.getCameraList(), list)


def test_pgroup_list_is_list() -> None:
    assert_type(tde4.getPGroupList(1), list)


def test_point_list_is_list(pgroup: str) -> None:
    assert_type(tde4.getPointList(pgroup), list)


def test_none_returns() -> None:
    # Setters are typed `-> None`; mypy rejects using their result as a value,
    # so we just call them (a `func-returns-value` error would mean the stub
    # stopped declaring `-> None`).
    tde4.setNearClippingPlane(0.1)
    tde4.setProjectNotes("hello")


def test_optional_int_arg_rejects_explicit_none() -> None:
    assert_type(tde4.getCameraList(), list)
    assert_type(tde4.getCameraList(1), list)

    with pytest.raises(TypeError):
        tde4.getCameraList(None)  # type: ignore[arg-type]


def test_optional_float_arg_rejects_explicit_none(camera: str) -> None:
    tde4.convertObjectPGroupTransformation3DEToWorld(camera, 1, _I3, _V0)

    with pytest.raises(TypeError):
        tde4.convertObjectPGroupTransformation3DEToWorld(
            camera,
            1,
            _I3,
            _V0,
            None,  # type: ignore[arg-type]
        )


def test_optional_str_arg_rejects_explicit_none(requester: str) -> None:
    tde4.addTextFieldWidget(requester, "w_ok", "label")

    with pytest.raises(TypeError):
        tde4.addTextFieldWidget(requester, "w_none", "label", None)  # type: ignore[arg-type]


def test_optional_id_arg_rejects_explicit_none(pgroup: str, point: str) -> None:
    assert_type(tde4.calcPointPosition3D(pgroup, point), list)

    with pytest.raises(TypeError):
        tde4.calcPointPosition3D(pgroup, point, None)  # type: ignore[arg-type]


def test_positional_only_rejects_keyword_argument(camera: str) -> None:
    # tde4 builtins are positional-only; the stubs mark them with `/`. The
    # ignore below confirms mypy flags the keyword call (warn_unused_ignores
    # fails if it doesn't), and the runtime raises to match.
    assert_type(tde4.getCameraName(camera), str)

    with pytest.raises(TypeError):
        tde4.getCameraName(camera_id=camera)  # type: ignore[call-arg]


def test_display_area_dimensions_is_list_of_int() -> None:
    assert_type(tde4.getDisplayAreaDimensions(), list[int])


def test_display_area_transformation_is_list_of_float() -> None:
    assert_type(tde4.getDisplayAreaTransformation(), list[float])


def test_transform_return_is_two_element_list(camera: str) -> None:
    result = tde4.convertObjectPGroupTransformation3DEToWorld(camera, 1, _I3, _V0)

    assert isinstance(result, list)
    assert len(result) == 2


def test_main_window_resolution_is_list_of_int() -> None:
    assert_type(tde4.getMainWindowResolution(), list[int])


def test_available_cpu_cores_is_int() -> None:
    assert_type(tde4.getAvailableCPUCores(), int)


def test_current_session_id_is_int() -> None:
    assert_type(tde4.getCurrentSessionID(), int)


def test_no_cameras_is_int() -> None:
    assert_type(tde4.getNoCameras(), int)


def test_no_pgroups_is_int() -> None:
    assert_type(tde4.getNoPGroups(), int)


def test_no_lenses_is_int() -> None:
    assert_type(tde4.getNoLenses(), int)


def test_project_path_optional_str_returns_none() -> None:
    # str | None: with no saved project the real return is None, confirming the
    # union is accurate (not just a documented-but-never-None alias).
    assert_type(tde4.getProjectPath(), str | None)
    assert tde4.getProjectPath() is None


def test_scene_position_is_list_of_float() -> None:
    assert_type(tde4.getScenePosition3D(), list[float])


def test_scene_rotation_is_matrix() -> None:
    # Matrix3D_t is list[Vector3D_t] == list[list[float]].
    assert_type(tde4.getSceneRotation3D(), list[list[float]])


def test_scene_scale_is_float() -> None:
    assert_type(tde4.getSceneScale3D(), float)


def test_lens_name_is_str(lens: str) -> None:
    assert_type(tde4.getLensName(lens), str)


def test_lens_fback_width_is_float(lens: str) -> None:
    assert_type(tde4.getLensFBackWidth(lens), float)


def test_lens_focal_length_is_float(lens: str) -> None:
    assert_type(tde4.getLensFocalLength(lens), float)


def test_lens_ld_model_is_str(lens: str) -> None:
    assert_type(tde4.getLensLDModel(lens), str)


def test_lens_list_is_list() -> None:
    assert_type(tde4.getLensList(), list)


def test_lens_ld_model_list_is_list_of_str() -> None:
    assert_type(tde4.getLensLDModelList(), list[str])


def test_curve_no_keys_is_int(camera: str) -> None:
    curve = tde4.getCameraZoomCurve(camera)

    assert_type(tde4.getNoCurveKeys(curve), int)


def test_ld_model_no_parameters_is_int() -> None:
    assert_type(tde4.getLDModelNoParameters(_LD_MODEL), int)


def test_ld_model_parameter_name_is_str() -> None:
    assert_type(tde4.getLDModelParameterName(_LD_MODEL, 0), str)


def test_ld_model_parameter_range_is_list_of_float() -> None:
    name = tde4.getLDModelParameterName(_LD_MODEL, 0)

    assert_type(tde4.getLDModelParameterRange(_LD_MODEL, name), list[float])


def test_ld_model_parameter_default_union() -> None:
    # str | float | int | None -- a real multi-member union; the standard model's
    # first parameter default comes back as a float.
    name = tde4.getLDModelParameterName(_LD_MODEL, 0)

    assert_type(
        tde4.getLDModelParameterDefault(_LD_MODEL, name), str | float | int | None
    )


def test_widget_value_union_toggle(populated_requester: str) -> None:
    # str | None | int | float: a toggle's value comes back as int.
    assert_type(
        tde4.getWidgetValue(populated_requester, "tog"), str | int | float | None
    )


def test_widget_value_union_textfield(populated_requester: str) -> None:
    assert_type(
        tde4.getWidgetValue(populated_requester, "txt"), str | int | float | None
    )


def test_widget_callback_optional_returns_none(populated_requester: str) -> None:
    # str | None: an unset callback really returns None.
    assert_type(tde4.getWidgetCallbackFunction(populated_requester, "tog"), str | None)
    assert tde4.getWidgetCallbackFunction(populated_requester, "tog") is None


def test_text_area_widget_string_is_optional_str(requester: str) -> None:
    # EDGE CASE (audit): spec'd `str`, but an empty text area really returns None
    # (like its sibling getTextAreaWidget* accessors), so the stub is corrected to
    # `str | None`. After appending text it reads back as a str.
    tde4.addTextAreaWidget(requester, "ta", "Text")

    assert_type(tde4.getTextAreaWidgetString(requester, "ta"), str | None)
    assert tde4.getTextAreaWidgetString(requester, "ta") is None

    tde4.appendTextAreaWidgetString(requester, "ta", "hello")
    value = tde4.getTextAreaWidgetString(requester, "ta")
    assert value is not None and "hello" in value


def test_create_lens_returns_str() -> None:
    assert_type(tde4.createLens(), str)


def test_create_dconstr_returns_str(pgroup: str) -> None:
    assert_type(tde4.createDConstr(pgroup), str)


def test_create_camera_mask_returns_str(camera: str) -> None:
    assert_type(tde4.createCameraMask(camera), str)


def test_dconstr_list_is_list(pgroup: str) -> None:
    tde4.createDConstr(pgroup)

    assert_type(tde4.getDConstrList(pgroup), list)


def test_pgroup_root_frame_a_list_element_can_be_none(pgroup: str) -> None:
    # EDGE CASE (audit): the spec types this list[CameraID_t | int] but for an
    # unset root frame the camera element is None ([None, 0]), so the stub is
    # corrected to allow None in the element type.
    result = tde4.getPGroupRootFrameA(pgroup)

    assert_type(result, list[str | int | None])
    assert result[0] is None


def test_pgroup_root_frame_b_list_element_can_be_none(pgroup: str) -> None:
    result = tde4.getPGroupRootFrameB(pgroup)

    assert_type(result, list[str | int | None])
    assert result[0] is None


def test_pgroup_extract_overall_motion_points_can_be_none(pgroup: str) -> None:
    # EDGE CASE (audit): spec'd list[str] but the entries come back as None
    # ([None, None, None]); corrected to list[str | None].
    result = tde4.getPGroupExtractOverallMotionPoints(pgroup)

    assert_type(result, list[str | None])
    assert all(item is None for item in result)


def test_calc_distortion_from_pixel_pairs(camera: str, lens: str) -> None:
    # The coverage audit hard-crashed 3DE on this with empty pixel lists (it
    # indexes the vectors); with real matching reference/distorted pixel pairs it
    # returns a float, so we exercise it safely here.
    tde4.setCameraLens(camera, lens)
    reference = [
        [float(x), float(y)] for x in (100, 300, 500, 700) for y in (100, 300, 500)
    ]
    distorted = [[rx + 1.0, ry + 1.0] for rx, ry in reference]

    assert_type(
        tde4.calcDistortionFromPixelPairs(camera, 1, 0, 0, reference, distorted), float
    )


def test_persistent_string_is_optional_str() -> None:
    # Declared return is str | None; after writing a value we read it back.
    tde4.addPersistentString("cg_stubs", "hello")

    assert_type(tde4.getPersistentString("cg_stubs"), str | None)
    assert tde4.getPersistentString("cg_stubs") == "hello"


def test_list_widget_item_type_is_optional(list_requester: str) -> None:
    # The list holds one ATOM item at index 0. Declared return is
    # ListWidgetItemType_t | None (the alias is this Literal).
    assert_type(
        tde4.getListWidgetItemType(list_requester, "lst", 0),
        Literal["LIST_ITEM_NODE", "LIST_ITEM_ATOM"] | None,
    )
    assert tde4.getListWidgetItemType(list_requester, "lst", 0) == "LIST_ITEM_ATOM"


def test_3d_model_face_list_is_list_of_int_lists(model: tuple[str, str]) -> None:
    pgroup, model_id = model

    assert_type(tde4.get3DModelFaceList(pgroup, model_id), list[list[int]])
    assert tde4.get3DModelNoFaces(pgroup, model_id) > 0


def test_run_matrix_tracking_procedure(camera_with_plate: str) -> None:
    # Track from the first frame (3DE numbers loaded frames 1..N internally, not
    # by the plate's file frame number). Needs real pixels; a frameless camera
    # hard-crashes 3DE. Declared return is Vector2D_t.
    result = tde4.runMatrixTrackingProcedure(camera_with_plate, 1, [0.5, 0.5], 0.1, 0.1)

    assert_type(result, list[float])


def test_pgroup_invert_point_cloud_points(pgroup: str) -> None:
    # With no inverted cloud set the entries come back as None ([None, None]),
    # confirming the corrected element type. Declared return is list[str | None].
    assert_type(tde4.getPGroupInvertPointCloudPoints(pgroup), list[str | None])


def test_save_render_cache_frame(
    camera_with_plate: str, tmp_path: pathlib.Path
) -> None:
    out = str(tmp_path / "frame.jpg")
    result = tde4.saveRenderCacheFrame(
        camera_with_plate, 1, out, "IMAGE_JPEG", 1.0, 0, 0
    )

    assert_type(result, int)


def test_save_render_cache_zbuffer(
    camera_with_plate: str, tmp_path: pathlib.Path
) -> None:
    out = str(tmp_path / "z.exr")
    result = tde4.saveRenderCacheZBuffer(
        camera_with_plate, 1, out, "IMAGE_OPENEXR", 1.0, 0
    )

    assert_type(result, int)
