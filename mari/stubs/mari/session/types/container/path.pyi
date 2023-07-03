from . import storage as storage

class Path(storage.Storage):
    copy: bool
    def __init__(self, value) -> None: ...
