# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"


__actionClasses: list

def GetRegisteredActionClasses() -> list: ...
def RegisterActionClass(actionClass: type): ...