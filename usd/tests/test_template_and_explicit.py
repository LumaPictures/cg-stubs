#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Use the Value Clip API's template syntax to author Value Clips."""

from __future__ import annotations

# IMPORT THIRD-PARTY LIBRARIES
from pxr import Sdf, Usd, Vt
from stubgenlib.test_helpers import assert_type

def test():
    """Run the main execution of this module."""
    stage: Usd.Stage = Usd.Stage.CreateInMemory()
    stage.SetStartTimeCode(0)
    stage.SetEndTimeCode(2)

    prim: Usd.Prim = stage.DefinePrim("/Set")
    non_template_set_name = "non_template_clips"
    model = Usd.ClipsAPI(prim)
    model.SetClipActive([(0.0, 0)], non_template_set_name)
    model.SetClipAssetPaths(
        [Sdf.AssetPath("./non_template_clip.usda")], non_template_set_name
    )
    model.SetClipPrimPath("/NonTemplate", non_template_set_name)

    template_set_name = "template_clips"
    model.SetClipTemplateAssetPath("./template_clip.##.usda", template_set_name)
    model.SetClipTemplateEndTime(2, template_set_name)
    model.SetClipTemplateStartTime(0, template_set_name)
    model.SetClipTemplateStride(1, template_set_name)
    model.SetClipPrimPath("/Template", template_set_name)

    paths = assert_type(model.GetClipAssetPaths(non_template_set_name), list[Sdf.AssetPath])
    assert paths == [Sdf.AssetPath("./non_template_clip.usda")]

    assert_type(model.GetClipActive(), Vt.Vec2dArray)

    prim.GetReferences().AddReference(assetPath="./set.usda", primPath="/Set")

    print(stage.GetRootLayer().ExportToString())


if __name__ == "__main__":
    test()
