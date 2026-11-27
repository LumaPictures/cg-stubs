import hou

DEFAULT_DURATION: float

class Prompter:
    """ Handle prompts, possibly with a timer as well. """
    msg: str | None
    end_time: float | None
    scene_viewer: hou.SceneViewer
    enabled: bool
    msg_type: hou.EnumValue[hou.promptMessageType]
    def __init__(self, scene_viewer: hou.SceneViewer) -> None: ...
    def enable(self, val: bool) -> bool:
        """ Enable/disable the prompter. If disabled, no actions will be done on the scene viewer. """
    def show(self, msg: str, duration_sec: float | None = None, msg_type: hou.EnumValue[hou.promptMessageType] | None = None) -> None:
        """ Show the message as a prompt, start a new timer. """
    def reshow(self) -> None:
        """ Re-show the last message as the prompt. No new timer. """
    def remainingTime(self) -> float | None:
        """ The remaining time if a timer was set or None if no timer. """
    def alive(self) -> bool:
        """ Whether the last prompt is still alive. """
    def clear(self) -> None:
        """ Clear the last prompt. """
