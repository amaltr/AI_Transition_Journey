# Python Fundamentals: Arrays & Tensors

This folder documents the foundational journey of transitioning from basic Python data structures (like lists) to high-performance NumPy arrays and tensors, an essential step in mastering Machine Learning and AI engineering.

## 📁 Directory Structure

* **`arrays_journey.md`**: The core learning document ("The Cognitive Architect’s Handbook"). Contains mental models, analogies, and detailed explanations of vectorization, broadcasting, and reshaping.
* **`broken_example.py`**: An example illustrating the anti-pattern of using `for` loops to modify 1D array data, highlighting the performance and logical pitfalls of non-vectorized operations.
* **`vectorization_fix.py`**: The corrected version of the 1D array example, demonstrating how to use NumPy's SIMD-optimized vectorization for efficient element-wise operations.
* **`broken_example_tensor.py`**: An example demonstrating the severe performance penalty of using nested `for` loops to iterate over 3D tensors (like a batch of images).
* **`broadcasting_fix.py`**: The vectorized solution to the tensor example, showcasing the power of NumPy **Broadcasting** to apply operations across multi-dimensional arrays simultaneously.
* **`flattening.py`**: Demonstrates how to reshape and flatten high-dimensional tensors (e.g., feeding a 3D image array into a 1D column vector for neural network processing).

## 🎯 Learning Objectives
1. **Memory Paradigms:** Understanding contiguous memory (NumPy) vs. scattered pointers (Python Lists).
2. **Vectorization:** Leveraging CPU/GPU SIMD architecture to eliminate slow Python-level loops.
3. **Broadcasting:** Mastering how NumPy implicitly stretches dimensions to perform math without manual dimension matching.
4. **Reshaping:** Safely altering tensor dimensions while maintaining data volume, setting the foundation for Matrix Multiplication ($W \cdot x$).

## 🚀 How to use this folder
Read `arrays_journey.md` first to grasp the mental models. Then, run the `.py` scripts to see the practical implementation and fixes in action.
