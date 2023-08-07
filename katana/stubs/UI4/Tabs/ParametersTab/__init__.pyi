# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from . import ProjectSettings as ProjectSettings
from UI4.Tabs.ParametersTab.ParameterPanel import ParameterPanel as ParameterPanel, TearoffParameterTab as TearoffParameterTab
from UI4.Tabs.ParametersTab.ProjectSettings import ProjectSettingsTab as ProjectSettingsTab
from typing import Set, Tuple

PluginRegistry: list
