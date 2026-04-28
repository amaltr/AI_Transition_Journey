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

## 📂 File Structure & Implementations

### Documentation
* **`transformers_journey.md`**: The primary knowledge base detailing mental model shifts from traditional programming to Transformer logic. Includes core analogies like "The Global Code Reviewer".

### Positional Encoding Scripts
* **`broken_positional_encoding.py`**: Demonstrates an anti-pattern and common broadcasting error when applying positional tags to batched word embeddings.
* **`positional_encoding_fix.py`**: The corrected PyTorch implementation demonstrating the use of `.unsqueeze(0)` for proper dimension alignment and broadcasting.
* **`positional_encoding.mmd`**: A Mermaid diagram visualizing the conceptual architecture of Positional Encodings.

### Self-Attention Scripts
* **`vanishing_gradient_stuck.py`**: Simulates the "Stuck Softmax" error by implementing basic dot-product attention without scaling.
* **`vanishing_gradient_fix.py`**: The corrected `scaled_dot_product_attention` implementation, applying the critical $\sqrt{d_k}$ scaling factor to preserve gradient flow.

---
*Part of the AI Transition Journey portfolio.*
