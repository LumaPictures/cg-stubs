# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
from . import CatalogGLHelpers as CatalogGLHelpers, CommentWidgets as CommentWidgets, DisplayDetailsWidgets as DisplayDetailsWidgets, Layers as Layers, Manipulators as Manipulators, MenuUtils as MenuUtils, MonitorWidget as MonitorWidget
from UI4.Tabs.Monitor.MonitorPanel import MonitorPanel as MonitorPanel
from typing import Set, Tuple

PluginRegistry: list
