# mypy: disable-error-code="misc, override, no-redef"

class ConstantsGroup:
    @classmethod
    def __init__(cls, *args, **kwargs): ...

class _MetaConstantsGroup(type):
    def __init__(self, metacls, cls, bases, classdict): ...
    def __contains__(self, value): ...
    @classmethod
    def __delattr__(cls, name): ...
    def __iter__(self): ...
    def __len__(self): ...
    @classmethod
    def __setattr__(cls, name, value): ...
