# Houdini stubs generated from Houdini 22.0.466

class ConnectivityConstant:
    """
    Specifies the connectivity of a neural network that has no inputs.

    This network consists of only output units.
    """
    output_width: int
    def __init__(self, /, *, output_width: int) -> None: ...
    def description(self) -> str: ...
