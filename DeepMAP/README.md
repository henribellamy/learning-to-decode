# DeepMAP

*Conditioning a network on external feedback: a reusable inference block*

***

## Context

This model introduces a powerful idea: conditioning a network on external information that evolves over time. Instead of predicting from the input alone, the network also ingests *prior belief* (feedback about what the answer is likely to be) and refines its output accordingly.

This turns the network into a reusable inference block that can be plugged into a larger iterative system, where several such blocks pass information to one another and progressively sharpen a shared estimate.

***

## Approach

The network takes multiple input channels: the observed sequence plus per-step prior information. It outputs a refined confidence score per step.

**Realistic data generation.** The subtle part is training data. A custom pipeline simulates the full iterative system and captures, at a chosen iteration, the exact prior state and the target output it should produce. The network therefore learns to behave correctly *inside the loop*, not just in isolation, a deliberate design choice that makes the block composable.

**Architecture.** Bidirectional GRU (100 units) to handle long sequences and fuse the prior channel, followed by 1D convolutions. Trained as regression (MSE, Adam), evaluated via MAE, MSE, R² and inference time.

***

## Contents
 
| File | Description |
|---|---|
| `deepmap.ipynb` | Model construction, training and evaluation |
| `deepmap.keras` | Trained model (architecture + weights) |
| `prior.py` | Generates the training dataset carrying the prior information fed to the network |
| `datasets/` | Training datasets |
| `BER.png` | Performance curve |
| `Vitesse.png` | Speed comparison against the classical baseline |
| `convolutif.py` / `maxlogmap2turbo.py` / `maxstar.py` / `turbocode.py` / `turbodecode.py` | Classical algorithm implementation, used as the baseline to benchmark the deep learning model against |

***

## Result

DeepMAP delivers a conditioned, composable neural inference block: the cornerstone that makes the fully neural iterative system possible (see DeepTurbo).
