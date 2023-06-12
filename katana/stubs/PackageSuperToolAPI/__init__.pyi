# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PackageSuperToolAPI.BaseNode as BaseNode
import PackageSuperToolAPI.NodeUtils as NodeUtils
import PackageSuperToolAPI.Packages as Packages

def IsUIMode() -> bool: ...