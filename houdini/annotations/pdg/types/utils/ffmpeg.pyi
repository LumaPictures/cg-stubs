from typing import TypedDict

import _pdg
from pdg.processor import PyProcessor

# The dictionaries that the nodes' _buildCommandAttr evaluate from their parameters.
class _FFmpegConfig(TypedDict):
    ffmpegbinary: int
    customffmpegbinary: str

class _ExtractInputConfig(TypedDict):
    inputsource: int
    inputfiletag: str
    inputfilepath: str

class _ExtractOptionsConfig(TypedDict):
    enablesize: int
    width: int
    height: int

class _EncodeInputConfig(TypedDict):
    inputsource: int
    inputfiletag: str
    inputfilepath: str
    framelistfile: str

# Each option has an `enable<option>` toggle; fps is the float parameter as a string.
class _EncodeOptionsConfig(TypedDict):
    enablefps: int
    fps: str
    enableformat: int
    format: str
    enablesize: int
    size: str
    enablevideocodec: int
    videocodec: str
    enablemovflags: int
    movflags: str
    enablepixelformat: int
    pixelformat: str
    enablecolorrange: int
    colorrange: str
    enablecolorspace: int
    colorspace: str
    enablecolorprimaries: int
    colorprimaries: str
    enablecolortrc: int
    colortrc: str
    enableexrcolortrc: int
    exrcolortrc: str
    additionalargs: str

class FFmpegExtractImages(PyProcessor):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    # `item` is needed with expand_inputs.
    @staticmethod
    def buildCommand(
        fps: float,
        output_file_pattern: str,
        input_config: _ExtractInputConfig,
        options_config: _ExtractOptionsConfig,
        ffmpeg_config: _FFmpegConfig,
        expand_inputs: bool = ...,
        item: _pdg.WorkItem | None = ...,
        escape_env_vars: bool = ...,
    ) -> list[str]: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> None: ...
    def onPrepareTask(self, work_item: _pdg.WorkItem) -> None: ...

class FFmpegEncodeVideo(PyProcessor):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    @staticmethod
    def checkCodec(command: str) -> None: ...
    @staticmethod
    def isUsingHFFmpeg(work_item: _pdg.WorkItem | None, command: str) -> bool: ...
    # `item` is needed with expand_inputs.
    @staticmethod
    def buildCommand(
        outputfilepath: str,
        options_config: _EncodeOptionsConfig,
        input_config: _EncodeInputConfig,
        ffmpeg_config: _FFmpegConfig,
        expand_inputs: bool = ...,
        item: _pdg.WorkItem | None = ...,
        escape_env_vars: bool = ...,
    ) -> list[str]: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> None: ...
    def onPrepareTask(self, work_item: _pdg.WorkItem) -> None: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
