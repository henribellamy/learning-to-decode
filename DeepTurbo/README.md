# DeepTurbo

*A fully neural iterative system, parallelized on GPU: the project's culmination*

> **Note:** the DeepTurbo source code, notebooks and trained models were developed in a corporate setting and are confidential. This folder describes the approach and results; the full work is summarized in the two-page executive summary [`summary.pdf`](summary.pdf).

***

## Context

The endpoint of the project: an entirely neural iterative system. Two neural inference blocks are placed in a loop, exchanging information back and forth and progressively refining a shared estimate, with the classical algorithm's expensive iterative machinery fully replaced by learned models.

This is the payoff of the incremental design: a complete, hand-crafted iterative pipeline swapped out for cooperating neural networks.

***

## How we got here

DeepTurbo builds on two intermediate models (not published):

- **DeepBCJR** taught a network to output calibrated per-step confidence scores (continuous values), matching an optimal probabilistic estimator. This moved the problem from classification to regression.
- **DeepMAP** conditioned that network on *prior information*, i.e. feedback about what the answer is likely to be. It was trained on data captured from inside a simulated iterative decoder, so it behaves correctly *inside the loop*, not just in isolation. The result is a reusable inference block (bidirectional GRU followed by 1D convolutions).

DeepTurbo plugs two instances of this block together.

***

## Approach

**Neural iterative loop.** At each iteration, one network processes the sequence and hands its refined belief to the second, which processes an alternate view and passes information back. After a few rounds, the estimate converges.

**Batch parallelization, the key win.** The classical algorithm is strictly sequential, one sequence at a time. DeepTurbo instead runs inference on thousands of sequences at once in a single vectorized forward pass. The entire loop (routing, feature extraction, iteration) is vectorized to exploit the GPU, turning a sequential bottleneck into a throughput-friendly neural workload.

***

## Contents

| File | Description |
|---|---|
| `summary.pdf` | Two-page executive summary of the project: approach, architecture and results |

***

## Result

DeepTurbo matches the accuracy of the optimal classical system while decoding thousands of sequences per forward pass, a large throughput gain from replacing a sequential algorithm with a batch-parallel neural one. The project shows end-to-end that a complete iterative algorithm can be learned, composed and accelerated with deep learning, with no meaningful loss in quality.