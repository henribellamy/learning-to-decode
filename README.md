# Learning to Decode: Replacing Classical Algorithms with Deep Learning

*End-of-studies deep learning project · Safran Data Systems (2023–2026)*

***

## Overview

This repository showcases a three-year deep learning research project: teaching neural networks to replace hand-crafted algorithms, learning complex sequential decision processes end-to-end, from data alone.

The testbed is a hard sequence-modeling problem: recovering information corrupted by noise. Classical solutions rely on intricate, iterative, provably-optimal algorithms. The question driving the project: can a neural network learn these algorithms from scratch, match their accuracy, and outperform them on speed through massive parallelization?

The answer, built up over four increasingly ambitious models, is yes: a fully neural system that matches an optimal iterative algorithm while decoding thousands of sequences in a single GPU pass.

***

## Why it matters

Beyond the specific application, this project is a case study in a broadly useful idea: replacing expensive, sequential, expert-designed pipelines with learned neural models that are faster, parallelizable, and trained purely from data. The same recipe (model a hard sequential process, generate realistic training data, benchmark against a strong baseline, then scale) transfers directly to time-series modeling, sequential decision-making, and any setting where a costly algorithm could be amortized into a neural network.

***

## Progression

Each model builds on the previous one, raising the difficulty of what the network must learn:

| Model | What the network learns | Deep learning takeaway |
|---|---|---|
| **DeepViterbi** | Recover a clean sequence from noisy observations | Sequence-to-sequence recovery with bidirectional RNNs |
| **DeepBCJR** | Predict per-step confidence scores (continuous) | Regression on soft outputs, matching an optimal estimator |
| **DeepMAP** | Same, now conditioned on external prior information | Conditioning a network on feedback, a reusable inference block |
| **DeepTurbo** | Two networks exchanging information in a loop | Fully neural iterative system, batch-parallelized on GPU |

***

## Key result

The final model (DeepTurbo) matches the accuracy of the optimal classical algorithm while decoding thousands of sequences in a single vectorized forward pass, where the classical approach processes them one at a time. End-to-end learning replaces a hand-designed iterative pipeline, with no loss in quality and a substantial speed-up.

***

## Repository structure

Each directory contains source code, training and evaluation notebooks, trained models, and results, with a README detailing the methodology.

| Directory | Focus |
|---|---|
| [DeepViterbi](DeepViterbi/) | Sequence recovery with bidirectional RNNs |
| [DeepBCJR](DeepBCJR/) | Soft-output regression against an optimal estimator |
| [DeepMAP](DeepMAP/) | Conditioning on external information, a reusable inference block |
| [DeepTurbo](DeepTurbo/) | Fully neural iterative system, GPU-parallelized |

***

## Technical stack

Python · TensorFlow / Keras · NumPy · Matplotlib · Jupyter

Bidirectional recurrent architectures (GRU, RNN) and 1D convolutions · supervised regression and classification · custom training loops and callbacks (simulated annealing, early stopping, LR scheduling) · realistic synthetic data generation · vectorized batch inference · rigorous benchmarking against theoretical baselines.

***

## Contact

**Henri Bellamy**
[LinkedIn](https://www.linkedin.com/in/henri-bellamy-232b5b28a/) · [henribellamy@icloud.com](mailto:henribellamy@icloud.com)
