# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from . import CatalogWidget as CatalogWidget, CatalogWidgetItem as CatalogWidgetItem, ImageImportDialog as ImageImportDialog
from UI4.Tabs.Catalog.CatalogPanel import CatalogPanel as CatalogPanel
from typing import Set, Tuple

PluginRegistry: list
