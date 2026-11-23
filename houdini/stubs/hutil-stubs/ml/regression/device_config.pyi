from hutil.ml.utils.menu import indexed_menu as indexed_menu

class DeviceConfig:
    """
    Configure device used for training
    """
    use_cpu_exclusively: bool
    def __init__(self, /, *, use_cpu_exclusively: bool = False) -> None: ...
    def description(self) -> str: ...
