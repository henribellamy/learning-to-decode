# DeepBCJR

*Soft-output regression: learning to match an optimal estimator*

***

## Context

The previous model made hard decisions. This one goes further: it learns to output calibrated per-step confidence scores (continuous values encoding both a decision and its certainty), reproducing the output of an optimal probabilistic estimator.

The deep learning shift is from classification to regression: the network must predict a continuous value per timestep and match, as closely as possible, the output of a mathematically optimal algorithm.

***

## Approach

The network maps a noisy input sequence to one continuous confidence score per step.

**Hybrid architecture.** A bidirectional GRU captures long-range temporal dependencies, followed by 1D convolutional layers that extract local structure and project to a per-step output. This RNN + CNN combination is a reusable pattern for sequence regression.

**Training.** Supervised regression: targets are the optimal estimator's outputs, loss is MSE. Quality is measured by R² against the optimal estimator (not just final accuracy) and by per-sequence inference time (a network that both matches the estimator *and* runs faster is the goal).

This model conditions only on the input sequence. The next stage adds external conditioning (see DeepMAP).

***

## Contents

| File | Description |
|---|---|
| `deepbcjr.ipynb` | Architecture, training and evaluation |
| `deepbcjr.keras` | Trained model (architecture + weights) |
| `BER.ipynb` | Error-rate evaluation via Monte-Carlo simulation |
| `BER.png` | Performance curve vs. the classical baseline |
| `vitesse.png` | Speed comparison against the classical baseline |
| `facteur.png` | Speed-up factor over the classical baseline |
| `Datasets/` | Training datasets |
| `convolutif.py` / `maxlogmap2.py` / `maxstar.py` | Classical algorithm implementation, used as the baseline to benchmark the deep learning model against |

***

## Result

The network reproduces the optimal estimator's continuous outputs with high fidelity (strong R²) and matches its decision performance, proving a neural model can learn calibrated soft outputs, the key ingredient for the iterative system that follows.
