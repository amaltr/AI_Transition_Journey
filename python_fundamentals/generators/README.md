# Python Generators & Memory Streaming

This module covers the shift from "Data at Rest" (Lists/Memory-bound) to "Data in Motion" (Generators/Compute-bound). Understanding generators is the prerequisite for building MLOps pipelines and training data loaders that don't crash servers.

## 📂 File Index

The scripts in this folder are designed to be run locally to prove python memory mechanics.

1. **`memory_usage.py`**
   * **Concept:** Proves the O(1) memory footprint of generators.
   * *Run this to see the difference in bytes between a 1-million item list and a 1-million item generator.*

2. **`broken_data_pipeline.py`**
   * **Concept:** The "Single-Use Trap." Demonstrates how iterating over a generator completely exhausts it, leading to silent bugs if you try to reuse it.

3. **`broken_data_pipeline_fix.py`** & **`reuse_recipe.py`**
   * **Concept:** The Factory Pattern limit bypass. Shows how to wrap generator logic in functions or use `itertools.tee` to spawn fresh streams.

4. **`excercise1_broken_data_pipeline.py`**
   * **Concept:** Simulating an AI Training loop (Epochs). Proves how the Factory Pattern is used in real machine learning loops to iterate over datasets infinitely.

## 📖 Deep Dive Notes
For the theoretical breakdown, mental models, and the "Projector vs Box" analogy, read the full thesis here:
👉 **[The Cognitive Architect’s Journey (Generators)](generators_journey.md)**
