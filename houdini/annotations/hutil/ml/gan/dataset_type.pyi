import enum

class DatasetType(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...
