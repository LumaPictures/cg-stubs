from _typeshed import Incomplete

def getCurrentLinkedPatches(): ...
def lookupUdimsFromPatches(patches): ...
def lookupPatchesFromUdims(udims): ...
def copyLinksFromCurrentImageSet() -> None: ...
def getMaximumResolution(images): ...
def resizeImages(images, size) -> None: ...
def pasteLinksToCurrentImageSet() -> None: ...
def onCopyLinks() -> None: ...
def onPasteLinks() -> None: ...

copy_action: Incomplete
paste_action: Incomplete
