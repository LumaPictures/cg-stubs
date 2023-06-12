# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_7_34(Updater):
    RENAME_ShadingNetworkMaterialAppend_TO: ClassVar[str] = ...
    RENAME_ShadingNetworkMaterialConditionalHint_TO: ClassVar[str] = ...
    RENAME_ShadingNetworkMaterialEdit_TO: ClassVar[str] = ...
    RENAME_ShadingNetworkMaterialLayer_TO: ClassVar[str] = ...
    RENAME_ShadingNetworkMaterialSourceEdit_TO: ClassVar[str] = ...
    RENAME_ShadingNetworkMaterial_TO: ClassVar[str] = ...
    VERSION: ClassVar[tuple] = ...