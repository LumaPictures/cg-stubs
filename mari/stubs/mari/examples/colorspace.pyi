def getColorspacePrettyName(colorspace_config, stage): ...
def showColorspaceConfigInfo(colorspace_config, indent_num_spaces) -> None: ...
def showProjectInfo() -> None: ...
def showChannelInfo() -> None: ...
def showImageInfo() -> None: ...
def showProjectorInfo() -> None: ...
def showAllColorspaces() -> None: ...
def disableRawOnChannels() -> None: ...
def disableRawOnImages() -> None: ...
def disableRawOnProjectors() -> None: ...
def disableRawOnProject() -> None: ...
def enablePreColorspaceProject() -> None: ...
def switchColorspaceOnProject(ocio_config, from_colorspace, to_colorspace) -> None: ...
def switchColorspaceOnConfig(colorspace_config, ocio_config, from_colorspace, to_colorspace): ...
def switchColorspaceOnChannels(ocio_config, from_colorspace, to_colorspace) -> None: ...
def switchColorspaceOnImages(ocio_config, from_colorspace, to_colorspace) -> None: ...
def switchColorspaceOnProjectors(ocio_config, from_colorspace, to_colorspace) -> None: ...
def switchColorspaceOnAll(ocio_config, from_colorspace, to_colorspace) -> None: ...
def convertSelectedImages(ocio_config, output_colorspace) -> None: ...
def registerOptimizedTransforms() -> None: ...
