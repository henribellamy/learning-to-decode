# DeepTurbo

*A fully neural iterative system, parallelized on GPU: the project's culmination*

***

## Context

The endpoint of the project: an entirely neural iterative system. Two of the conditioned inference blocks from the previous stage (DeepMAP) are placed in a loop, exchanging information back and forth and progressively refining a shared estimate, with the classical algorithm's expensive iterative machinery fully replaced by learned models.

This is the payoff of the incremental design: a complete, hand-crafted iterative pipeline swapped out for cooperating neural networks.

***

## Approach

**Neural iterative loop.** Each iteration, one network processes the sequence and hands its refined belief to the second, which processes an alternate view and passes information back. After a few rounds, the estimate converges.

**Batch parallelization, the key win.** The classical algorithm is strictly sequential, one sequence at a time. DeepTurbo instead runs inference on thousands of sequences at once in a single vectorized forward pass. The entire loop (routing, feature extraction, iteration) is vectorized to exploit the GPU, turning a sequential bottleneck into a throughput-friendly neural workload.

***

## Contents

| File | Description |
|---|---|
| `deepturbo.py` | Core of the system: couples the two neural blocks in a loop, fully batch-vectorized |
| `deepturbo.ipynb` | Building, running and evaluating the full neural iterative decoder (accuracy + speed) |
| `deepmap.keras` | Trained neural block instantiated twice inside the loop |
| `BER.png` | Accuracy vs. the classical baseline |
| `vitesse.png` | Throughput / decoding-time comparison against the classical baseline |
| `rapport.pdf` | Final end-of-studies report |
| `convolutif.py` / `maxlogmap2.py` / `maxlogmap2turbo.py` / `maxstar.py` / `turbocode.py` / `turbodecode.py` | Classical algorithm implementation, used as the baseline to benchmark the deep learning model against |

***

## Result

DeepTurbo matches the accuracy of the optimal classical system while decoding thousands of sequences per forward pass, a large throughput gain from replacing a sequential algorithm with a batch-parallel neural one. The project shows end-to-end that a complete iterative algorithm can be learned, composed, and accelerated with deep learning, with no meaningful loss in quality.
