"""nn.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def relu(x: list[float]):
    """elementwise `max(0, v)`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('relu')


def sigmoid(x: list[float]):
    """elementwise `1 / (1 + exp(-v))`, computed stably

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('sigmoid')


def forward(x: list[float], W: list[list[float]], b: list[float]):
    """one dense layer: `matvec(W, x) + b`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('forward')


class MLP:
    """sizes = `[in, hidden..., out]`; seeded random init so runs are reproducible; `.forward(x)`, `.train(data, steps, learning_rate)`

    TODO: implement this class.
    """

    # TODO: attributes, methods and their behaviour come from the contract.
    raise NotImplementedError('MLP')

def two_layer(x: list[float], W1, b1, W2, b2):
    """hidden layer then output layer, with ReLU between

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('two_layer')


def hidden_activations(x: list[float], W1, b1):
    """the hidden layer's output, so the learner can look at what the network built

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('hidden_activations')



# MLP.forward
        def forward(self, x: list[float]):
            """the network's output for one input
    
            TODO: implement this. The behaviour above is the contract.
            """
            raise NotImplementedError('forward')


# MLP.train
        def train(self, data: list[tuple[list[float], float]], steps: int, learning_rate: float):
            """trains on `(input, target)` pairs, returns the loss per step
    
            TODO: implement this. The behaviour above is the contract.
            """
            raise NotImplementedError('train')
