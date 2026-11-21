# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Callable as Callable, MutableMapping
from typing import Any

def setStateEventCallback(self: hou.hda, hda_globals: MutableMapping[str, Any], state_name: str, event_name: str, callback: Callable[..., object]) -> None:
    '''
setStateEventCallback(hda_globals, state_name, event_name, callback)

    Register a Python callback that the given state will call whenever a
    particular event (or action) occurs on the node of a particular
    type. This static method will add a special dictionary to
    hda_globals. NOTE: This must be called from inside a Python Module
    section with hda_globals = globals().

  > def callback():
  >     print "in callback"
  > hou.hda.setStateEventCallback(globals(), \'objmirror\', \'mirror\', callback)

    This code will cause the Mirror shelf tool to invoke callback when
    the object which has the associated Python Module.


    State Callbacks

        objmirror

            isWorldSpace()
                Returns a bool indicating whether the mirror occurs in
                world space.

            mirror(kwargs)
                Performs mirroring on kwargs[\'node\'] using the scale
                vector kwargs[\'scale\'].

'''
def reloadHDAModule(self: hou.hda, hda_module: hou.HDAModule) -> None:
    '''
reloadHDAModule(self, hda_module)

    Reload the code in the PythonModule section corresponding to
    hda_module. hda_module must be an hou.HDAModule object.

    For example this code reloads and re-executes the code in the
    PythonModule section of the HDA definition for the \'foobar\' node:

  > hou.hda.reloadHDAModule(hou.node("/obj/foobar").hdaModule())
'''
def reloadHDAViewerStateModule(self: hou.hda, hda_module: hou.HDAViewerStateModule) -> None:
    '''
reloadHDAViewerStateModule(self, hda_module)

    Reload the code in the ViewerStateModule section corresponding to
    hda_module. hda_module must be an hou.HDAViewerStateModule object.

    For example this code reloads the viewer state code in the
    ViewerStateModule section of the HDA definition for the \'foobar\'
    node:

  > hou.hda.reloadHDAViewerStateModule(hou.node("/obj/foobar").hdaViewerStateModule())
'''
def reloadHDAViewerHandleModule(self: hou.hda, hda_module: hou.HDAViewerHandleModule) -> None:
    '''
reloadHDAViewerHandleModule(self, hda_module)

    Reload the code in the ViewerHandleModule section of hda_module.
    hda_module must be an hou.HDAViewerHandleModule object.

    This example shows how to reload the code in the ViewerHandleModule
    section of the HDA definition for the \'xyz\' node:

  > hou.hda.reloadHDAViewerHandleModule(hou.node("/obj/xyz").hdaViewerHandleModule())
'''
