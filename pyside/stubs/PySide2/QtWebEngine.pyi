import shiboken2

class QtWebEngine(shiboken2.Object):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def initialize(cls) -> None: ...
