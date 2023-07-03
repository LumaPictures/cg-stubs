# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"


_openWidgets: dict

def QueryOpenState(key): ...
def RegisterOpenState(key, isOpen): ...