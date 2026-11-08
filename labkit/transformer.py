"""transformer.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def embedding_lookup(ids: list[int], table: list[list[float]]):
    """one row of the embedding table per id

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('embedding_lookup')


def cosine_similarity(a: list[float], b: list[float]):
    """`dot(a, b) / (norm(a) * norm(b))`; `ValueError` on a zero vector

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('cosine_similarity')


def mean_pool(vectors: list[list[float]]):
    """the component-wise mean

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('mean_pool')


def attention_scores(q: list[float], k: list[list[float]], scale: float):
    """one scaled dot product per key

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('attention_scores')


def attention(q: list[float], k: list[list[float]], v: list[list[float]]):
    """softmax-weighted sum of the values

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('attention')


def causal_mask(n: int):
    """`n x n`, 0.0 below the diagonal and a large negative number above it

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('causal_mask')


def split_heads(x: list[list[float]], num_heads: int):
    """split the last axis into `num_heads` heads

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('split_heads')


def merge_heads(heads: list[list[list[float]]]):
    """the inverse

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('merge_heads')


def multi_head_attention(x: list[list[float]], Wq, Wk, Wv, Wo, num_heads: int):
    """one attention layer with `num_heads` heads

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('multi_head_attention')


def layer_norm(x: list[float], gamma: list[float], beta: list[float]):
    """zero mean, unit variance, then scale and shift

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('layer_norm')


def feed_forward(x: list[float], W1, b1, W2, b2):
    """two linear maps with a ReLU between

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('feed_forward')


def transformer_block(x: list[list[float]], params: dict):
    """attention, residual, layer norm, feed-forward, residual, layer norm

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('transformer_block')


def next_token_pairs(ids: list[int]):
    """every (input id, next id) pair from one sequence

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('next_token_pairs')


def sequence_loss(logits: list[list[float]], targets: list[int]):
    """mean cross entropy over the positions

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('sequence_loss')


def train_lm(model: dict, data: list[list[int]], steps: int, learning_rate: float):
    """next-token training; returns the loss per step

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('train_lm')


def sample_token(logits: list[float], temperature: float = 1.0, top_p: float = 1.0, rng=None):
    """temperature, then top-p truncation, then a sample; `ValueError` if temperature <= 0

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('sample_token')


def generate(model: dict, prompt_ids: list[int], steps: int, temperature: float = 1.0, top_p: float = 1.0, rng=None):
    """feed the prompt, sample, append, repeat

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('generate')

