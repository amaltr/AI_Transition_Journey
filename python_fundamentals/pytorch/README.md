# PyTorch Fundamentals: The Training Loop & Autograd

This folder focuses on the core mechanics of PyTorch, specifically transitioning from static data structures to dynamic computational graphs and backpropagation. The primary focus is understanding the training loop and avoiding the most common pitfalls encountered when writing deep learning code.

## 📁 Directory Structure

* **`pytorch_journey.md`**: The central learning log. Contains the mental models for computational graphs, gradient descent, the standard PyTorch training loop, and the crucial `zero_grad()` mechanism.
* **`pytorch_backward.mmd`**: A Mermaid diagram visualizing the forward and backward pass sequence in a neural network. (Also embedded in `pytorch_journey.md`).
* **`broken_example_gradient_accumulation.py`**: An anti-pattern script demonstrating what happens when `optimizer.zero_grad()` is omitted. Gradients accumulate over epochs, silently corrupting the network's updates.
* **`zerograd_fix.py`**: The corrected standard training loop, utilizing `model.train()`, batches, and the properly placed `optimizer.zero_grad()`.

## 🎯 Learning Objectives
1. **Computational Graphs:** Understanding how PyTorch tracks operations dynamically to calculate gradients (`autograd`).
2. **The Training Loop:** Mastering the sequence of Forward Pass -> Loss -> Backward Pass -> Optimizer Step.
3. **Gradient Accumulation vs Zero Grad:** Internalizing why PyTorch accumulates gradients by default and why we must manually clear them using `zero_grad()` before each training step.

## 🚀 How to Use This Folder
Start with `pytorch_journey.md` to understand the theory and analogies. Review the `.py` files to see the difference between a fatally flawed training loop and an industry-standard one.
