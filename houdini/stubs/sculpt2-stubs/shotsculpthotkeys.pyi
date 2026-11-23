import hou
from frameworkstate.hotkeymanager import HotkeyManager

HK_RADIAL_MENU: str

class ShotSculptHotkeys(HotkeyManager):
    hud_parms: str
    hud_sliders: str
    shotsculpt_key_lockseltrack: str
    shotsculpt_key_muteseltrack: str
    shotsculpt_key_soloseltrack: str
    shotsculpt_key_jumpnextpose: str
    shotsculpt_key_jumpprevpose: str
    shotsculpt_key_jumpnexttrack: str
    shotsculpt_key_jumpprevtrack: str
    shotsculpt_key_trackcolor: str
    shotsculpt_key_clipcolor: str
    shotsculpt_key_posecolor: str
    shotsculpt_key_togglecolor_curtrack: str
    shotsculpt_key_togglecolor_othertracks: str
    shotsculpt_key_coloractivegeotype: str
    shotsculpt_key_colorallgeotype: str
    shotsculpt_key_viewallgeointeraction: str
    sculpt_key_claybrush: str
    sculpt_key_smoothbrush: str
    sculpt_key_movebrush: str
    sculpt_key_erasebrush: str
    sculpt_key_claystripsbrush: str
    sculpt_key_inflatebrush: str
    sculpt_key_flattenbrush: str
    sculpt_key_creasebrush: str
    sculpt_key_pinchbrush: str
    sculpt_key_relaxbrush: str
    sculpt_key_volumeshape: str
    sculpt_key_surfaceshape: str
    sculpt_key_togglemaskenable: str
    sculpt_key_clearmask: str
    sculpt_key_invertmask: str
    sculpt_key_paintmaskbrush: str
    groom_key_collidewithskin: str
    groom_key_surfacebrush: str
    groom_key_mirrorbrush: str
    groom_key_usemask: str
    def __init__(self, state_typename: str, state_cat: hou.NodeTypeCategory, bindRadialMenu: bool = True) -> None: ...
