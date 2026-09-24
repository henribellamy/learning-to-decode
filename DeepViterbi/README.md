# DeepViterbi

*Learning sequence recovery with bidirectional RNNs*

***

## Context

The starting point of the project, and a clean deep learning problem: **can a neural network learn to recover a clean sequence from noisy observations**, matching a provably-optimal algorithm it has never been shown?

The classical solution here is a sequential dynamic-programming algorithm that searches for the most likely underlying sequence. The deep learning goal is to bypass it entirely and learn the mapping end-to-end, purely from examples.

***

## Approach

The network takes a noisy sequence as input and predicts the original clean sequence: a supervised sequence-to-sequence task. Ground-truth sequences serve as labels; the optimal classical algorithm defines the performance ceiling to beat.

**Architecture.** Bidirectional RNN (two `SimpleRNN` layers, 64 units) with dropout and batch normalization, followed by dense layers. Bidirectionality lets the model condition each prediction on the full sequence context, past and future.

**Training.** Binary cross-entropy, Adam, plus a custom simulated-annealing callback that injects decaying noise into the weights to escape sharp minima and improve generalization.

***

## Contents

| File | Description |
|---|---|
| `RNN.ipynb` | Model construction, training and evaluation |
| `RNN.keras` | Trained model (architecture + weights) |
| `BER.ipynb` | Error-rate evaluation via Monte-Carlo simulation |
| `BER.png` | Performance curve vs. the classical baseline |
| `rapport.pdf` | Detailed report |
| `convolutif.py` / `CC.py` / `Viterbi.py` | Classical algorithm implementation, used as the baseline to benchmark the deep learning model against |

***

## Result

The network learns the recovery task from data alone and closely tracks the optimal algorithm's performance, establishing that a neural model can absorb a non-trivial sequential algorithm end-to-end.
