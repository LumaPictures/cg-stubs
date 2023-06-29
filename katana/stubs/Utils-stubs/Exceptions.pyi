# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"


def GetExceptionMessage(exception: Exception | None) -> str: ...