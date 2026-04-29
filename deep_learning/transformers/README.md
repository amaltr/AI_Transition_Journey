# Transformer Architecture Foundations

This directory contains learning materials, core PyTorch implementations, and diagnostic exercises focused on the foundational mechanisms of the Transformer architecture. It serves to bridge theoretical AI concepts with practical engineering realities.

## 📖 Overview

The materials here are mapped to the **80/20 Recursive Learning Method** detailed in the accompanying [`transformers_journey.md`](./transformers_journey.md) knowledge base. The goal is to translate abstract Transformer mechanisms (like Self-Attention and Positional Encoding) into concrete Python/PyTorch mental models.

## 🧠 Core Concepts Explored

### 1. Positional Encoding
Since Transformers process entire sequences simultaneously in parallel (unlike sequential RNNs), they lack an inherent sense of word order. Positional Encodings act as "frequency fingerprints" (Sine/Cosine waves) injected directly into word embeddings to provide explicit sequence coordinates.
* **Key Engineering Challenge**: Broadcasting the 2D positional grid correctly across a 3D batch tensor `(Batch, Seq_Len, Dim)` without causing shape mismatches.

### 2. Self-Attention & The "Stuck" Softmax (Vanishing Gradients)
The Self-Attention mechanism allows tokens to dynamically query and weight their relationships with other tokens in the sequence using Query (Q), Key (K), and Value (V) matrices.
* **Key Engineering Challenge**: Raw dot-product attention scores can grow excessively large as the embedding dimension increases. When these large values are passed through an exponential function like Softmax, the probabilities "saturate" (the highest value becomes `1.0`, the rest `0.0`). This effectively kills the gradient, halting the network's ability to learn.
* **The Fix**: Dividing the scores by a scaling factor—the square root of the key dimension ($\sqrt{d_k}$). This acts as an algorithmic "volume knob", keeping the values within a healthy gradient range for the Softmax distribution.

### 3. Multi-Head Attention (Parallel Subspaces)
Multi-Head Attention splits the embedding dimension into multiple "heads", allowing the model to simultaneously attend to information from different representation subspaces (e.g., one head focuses on grammar, another on sentiment).
* **Key Engineering Challenge**: Managing the complex tensor reshaping required to split and rejoin heads. A common error is flattening dimensions incorrectly, which mixes data from different heads and corrupts the representation.
* **The Fix**: Using `.transpose(1, 2).contiguous()` to explicitly align the dimensions back to `(Batch, Seq, Heads, D_k)` *before* applying the `.view()` operation to merge the heads back into the original embedding dimension.

### 4. Residual Connections & Layer Normalization (Signal Stability)
In very deep architectures, the learning signal can degrade (vanishing gradients). Residual (Skip) Connections solve this by providing a "gradient superhighway" that allows the original signal to bypass the transformation block ($y = f(x) + x$).
* **Key Engineering Challenge**: Determining where to apply Layer Normalization. "Post-LN" applies normalization after the residual addition, which can force the gradient through normalization and cause instability in very deep models.
* **The Fix**: Adopting the modern "Pre-LN" architecture where normalization happens *before* the sublayer ($x + f(\text{LayerNorm}(x))$), keeping the gradient pathway completely unobstructed.


## 📂 File Structure & Implementations

### Documentation
* **`transformers_journey.md`**: The primary knowledge base detailing mental model shifts from traditional programming to Transformer logic. Includes core analogies like "The Global Code Reviewer".
* **`multihead_attention_journey.md`**: A focused guide on the mechanics of Multi-Head Attention, Residual connections, and Layer Normalization, emphasizing dimensional transformations and signal preservation.

### Positional Encoding Scripts
* **`broken_positional_encoding.py`**: Demonstrates an anti-pattern and common broadcasting error when applying positional tags to batched word embeddings.
* **`positional_encoding_fix.py`**: The corrected PyTorch implementation demonstrating the use of `.unsqueeze(0)` for proper dimension alignment and broadcasting.
* **`positional_encoding.mmd`**: A Mermaid diagram visualizing the conceptual architecture of Positional Encodings.

### Self-Attention Scripts
* **`vanishing_gradient_stuck.py`**: Simulates the "Stuck Softmax" error by implementing basic dot-product attention without scaling.
* **`vanishing_gradient_fix.py`**: The corrected `scaled_dot_product_attention` implementation, applying the critical $\sqrt{d_k}$ scaling factor to preserve gradient flow.

### Multi-Head Attention Scripts
* **`broken_mha_split.py`**: Demonstrates the common dimension-flattening error when attempting to rejoin parallel attention heads back into a single tensor.
* **`mha_split_rejoin_fix.py`**: The corrected implementation showing the proper sequence of `.transpose()` and `.contiguous()` operations before the final `.view()` merge.
* **`multihead_attention.mmd`**: A Mermaid diagram illustrating the data flow from input embeddings through parallel attention heads and the final concatenation.

### Residual & LayerNorm Scripts
* **`residual_block_implementation.py`**: Compares the implementations of "Post-LN" and modern "Pre-LN" architectures, emphasizing how Pre-LN provides an unobstructed gradient superhighway.

---
*Part of the AI Transition Journey portfolio.*
