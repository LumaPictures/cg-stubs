import mari
from _typeshed import Incomplete

filter_factory: Incomplete
PERMUTATIONS: Incomplete
GRADIENTS_3D: Incomplete
CHANNEL_TYPES: Incomplete
CHANNEL_BODIES: Incomplete
CHANNEL_DEFINITIONS: Incomplete
NOISE_PIXELS: Incomplete

def generate_pixels() -> None: ...

class NoiseFilterFactory(mari.GLSLFilterFactory):
    def __init__(self) -> None: ...
    def setupFilter(self, filter) -> None: ...

def registerAddNoiseFilter() -> None: ...
