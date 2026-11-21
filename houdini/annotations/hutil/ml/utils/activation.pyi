import torch.nn

class Activation:
    @classmethod
    def menu(cls) -> list[str]: ...
    def activation(
        self,
    ) -> (
        torch.nn.ReLU
        | torch.nn.LeakyReLU
        | torch.nn.RReLU
        | torch.nn.Sigmoid
        | torch.nn.Tanh
        | torch.nn.LogSoftmax
        | None
    ): ...
