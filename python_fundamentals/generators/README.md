# Python Generators & Memory Streaming

This module covers the shift from "Data at Rest" (Lists/Memory-bound) to "Data in Motion" (Generators/Compute-bound). Understanding generators is the prerequisite for building MLOps pipelines and training data loaders that don't crash servers.

## 📂 Module Structure

This module has been organized using Domain-Driven Design to separate theory from execution and testing. 

### 1. `\theory`
The mental models, architectural explanations, and vocabulary required for this topic.
* **`generators_journey.md`:** The "Cognitive Architect's Journey" — a deep dive into state machines, lazy evaluation, and the Projector vs. Box analogy.
* **`generator_power_words.md`:** A glossary of terms (e.g., *Generator Exhaustion*, *Backpressure*) to use in system design interviews.

### 2. `\code`
Runnable `.py` scripts designed to prove Python's memory mechanics locally.
* **`memory_usage.py`:** Proves the O(1) memory footprint.
* **`broken_data_pipeline...` files:** Demonstrates the "Single-Use Trap" and how to bypass it using the Factory Pattern.
* **`excercise1_broken_data_pipeline.py`:** Simulates an AI Training loop using generators.

### 3. `\hands_on_challenges`
Progressive coding challenges to test your ability to implement generators without relying on framework magic.
* **`..._novice.md`:** Basic syntax and file reading limits.
* **`..._intermediate.md`:** Orchestration, batching, and error handling.
* **`..._architect.md`:** High-level system design, shuffling algorithms, and `yield from`.

### 4. `\interview`
Strict QA sets covering edge cases and interview curveballs.
* **`interview_prep_qa_set1.md` - `set4.md`:** Covers everything from basic memory constraints to advanced DL framework (`DataLoader`) integration and deadlocks.
