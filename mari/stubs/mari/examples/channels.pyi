PRINT_IMAGE_SET_INFO: bool

def showGeoPatchImageInfo(obj) -> None: ...
def showAllGeoPatchImageInfo() -> None: ...
def showLayerStackInfo(stack, indent_num_spaces: int = ...) -> None: ...
def getColorspacePrettyName(colorspace_config, stage): ...
def showChannelInfo(channel) -> None: ...
def showAllChannels() -> None: ...
def reimportImageSetPatches(imgset, patches) -> None: ...
def reimportCurrentPaintableLayer() -> None: ...
def linkCurrentChannels() -> None: ...
