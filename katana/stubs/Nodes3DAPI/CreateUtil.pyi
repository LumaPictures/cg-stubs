# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute

def BuildChild(root, childPath, childType): ...
def _AddChild(producer, childName): ...