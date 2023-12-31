from _typeshed import Incomplete

def watchGeo(obj) -> None: ...
def watchLayer(obj) -> None: ...
def printChannelLayerInfo(header, layer) -> None: ...
def printGroupLayerInfo(header, layer) -> None: ...
def printAdjustmentStackLayerInfo(header, layer) -> None: ...
def printMaskStackLayerInfo(header, layer) -> None: ...
def printImageInfo(header, image) -> None: ...
def printImageSetInfo(header, image_set) -> None: ...
def printPaintableLayerInfo(header, layer) -> None: ...
def printMaskLayerInfo(header, layer) -> None: ...
def printProceduralLayerInfo(header, layer) -> None: ...
def printShaderLayerInfo(header, layer) -> None: ...
def printAdjustmentLayerInfo(header, layer) -> None: ...
def printLayerInfo(header, layer) -> None: ...
def printAllLayersInfo() -> None: ...
def printMaskStackLayerHashes(header, layer, uv_index) -> None: ...
def printAdjustmentStackLayerHashes(header, layer, uv_index) -> None: ...
def printGroupLayerHashes(header, layer, uv_index) -> None: ...
def printLayerHashes(header, layer, uv_index) -> None: ...
def printAllLayersHashes() -> None: ...

geo_values_max: int
geo_values_paint_colors: Incomplete
geo_values_procedural_types: Incomplete
geo_values_procedural_blend_amounts: Incomplete
geo_values_procedural_blend_modes: Incomplete

def createLayers_ImageSetClear(image_set, color) -> None: ...
def createLayers_Channel(geo_index, geo_name, channel) -> None: ...
def createLayers() -> None: ...
