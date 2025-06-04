from _typeshed import Incomplete

kUnknownKeys: Incomplete
kMissingTypeName: Incomplete
kFaultyTypeName: Incomplete
kWrongMergeType: Incomplete
kUnknownTypeNode: Incomplete
kObjectAlreadyExists: Incomplete
kMissingProperty: Incomplete
kUnknownData: Incomplete
kTypeNodeCreationFailed: Incomplete
DECODE_AND_ADD: int
DECODE_AND_MERGE: int
DECODE_AND_RENAME: int
REJECT_COLOR: int
ACCEPT_COLOR: int
NAME_ATTRIBUTE_NAME: str
IMPORTED_ATTRIBUTE_NAME: str
NOTES_ATTRIBUTE_NAME: str
LAYERS_ATTRIBUTE_NAME: str
COLLECTIONS_ATTRIBUTE_NAME: str
GROUPS_ATTRIBUTE_NAME: str
VISIBILITY_ATTRIBUTE_NAME: str
RENDERABLE_ATTRIBUTE_NAME: str
LABEL_COLOR_ATTRIBUTE_NAME: str
CHILDREN_ATTRIBUTE_NAME: str
SCENE_SETTINGS_ATTRIBUTE_NAME: str
SELECTOR_ATTRIBUTE_NAME: str
SCENE_AOVS_ATTRIBUTE_NAME: str
SCENE_LIGHTEDITOR_ATTRIBUTE_NAME: str

def enableCopyPasteLabelColor(value) -> None: ...
def copyPasteLabelColorEnabled(): ...
def enableExportLabelColor(value) -> None: ...
def exportLabelColorEnabled(): ...
def enableImportLabelColor(value) -> None: ...
def importLabelColorEnabled(): ...
def computeValidObjectName(dict, mergeType, prependToName, objectTypeName): ...
