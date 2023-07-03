# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio

localVersion: tuple
nodeUpgraders: dict

def UpgradeRenderMode(node, nodeType): ...
def UpgradeRenderModeStack(node, nodeType): ...
def update(document): ...