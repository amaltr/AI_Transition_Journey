# Interview Prep: Python Generators (Model Answers)

## Q1: Stack Frame & Mechanics
**Question:** In terms of memory management, what happens to a function's **stack frame** when it encounters a `yield` vs. a `return`?
* **Answer:** When a function hits `return`, the stack frame is destroyed—local variables are cleared, and the lifecycle ends. With `yield`, Python performs **stack frame preservation**. The function's state, including local variables and the **instruction pointer**, is suspended in memory. It remains a **state machine** until the next `next()` call triggers a resumption, allowing it to pick up exactly where it left off.

**Follow-up A:** How does it resume?
* **Answer:** The generator object stores the **instruction pointer**. This is a reference to the specific bytecode offset where the function was paused, allowing the Python interpreter to jump directly back into the suspended execution context.

**Follow-up B:** What is the memory cost?
* **Answer:** The memory cost is $O(1)$. We only store the generator object, its local variable references, and the instruction pointer. This is significantly more efficient than a List, which requires $O(N)$ allocation for the entire dataset.

---

## Q2: The "Single-Use" Trap
**Question:** A developer runs `sum(data)` and `max(data)` on a generator and it fails. Why, and how do you fix it?
* **Answer:** The `sum()` call consumes the generator entirely, leading to **generator exhaustion**. Once the internal instruction pointer reaches the end of the stream, it is empty. To fix this, we use a **Generator Factory** function that returns a fresh generator instance, creating a new **blueprint** for the iterator each time we start a new pass.

**Follow-up A:** Why not use a "shadow copy" (assignment)?
* **Answer:** Assigning `data2 = data` just creates two references to the same exhausted generator object. You aren't cloning the *process*; you're just pointing two variables at the same dead projector.

**Follow-up B:** How does a list differ?
* **Answer:** A list is an **iterable container**. It stores all values in memory, allowing it to be traversed multiple times without exhaustion. Generators are **iterators**, which are single-use streams.

---

## Q3: Lazy vs. Eager Trade-offs
**Question:** Explain **Lazy vs. Eager Evaluation**. When would a generator be *slower* than a list?
* **Answer:** **Lazy Evaluation** computes values on-demand; **Eager Evaluation** computes everything upfront. Generators are slower when you need **random access**. Lists provide `O(1)` index-based lookup, whereas generators require `O(N)` sequential iteration to reach a specific item because they do not index their contents.

**Follow-up A:** How does cache locality factor in?
* **Answer:** Sequential generators offer excellent **cache locality** for the CPU because data is accessed predictably in order. However, if the logic requires jumping back and forth, you lose this benefit.

**Follow-up B:** When should you use a list instead of a generator?
* **Answer:** Use a list when you need random access, multi-pass iteration without re-instantiation, or when the dataset is small enough that the memory overhead is negligible.

---

## Q4: AI/ML Application
**Question:** You are training for 100 **epochs** with a massive dataset. How do you ensure your **Data Ingestion Layer** doesn't crash?
* **Answer:** I use a **Generator Factory** to ensure each epoch starts with a clean stream. I implement a **Producer-Consumer Pattern** where the generator streams one batch at a time to the model. This keeps the memory footprint at $O(1)$ relative to the total dataset size.

**Follow-up A:** How do you implement a simple "Batcher"?
* **Answer:** A batcher is a generator that wraps an inner loop: it `yields` a chunk of $N$ items. It is effectively a nested pipeline where the inner loop consumes items and the outer loop yields the batch.

**Follow-up B:** Why is `StopIteration` important?
* **Answer:** `StopIteration` is the internal signal in Python that an iterator is exhausted. In a training loop, this signal informs the orchestrator that the epoch is complete, triggering the epoch-reset logic.

---

## Q5: Advanced Flow Control
**Question:** What is **Delegated Iteration** (`yield from`) and how does it simplify nested pipelines?
* **Answer:** **Delegated Iteration** allows a generator to act as a **transparent bridge** to a sub-generator. It flattens the pipeline, allowing values to flow from the sub-generator directly to the caller without the parent generator needing to manually iterate.

**Follow-up A:** Can you use a loop instead of `yield from`?
* **Answer:** While `for x in sub: yield x` works, `yield from` is more performant. It creates a direct channel, reducing the bytecode overhead and properly handling exception propagation between the caller and the sub-generator.

**Follow-up B:** How does it affect modularity?
* **Answer:** It makes the system **modular**. You can replace a sub-generator (e.g., swapping a CPU-based augmentation for a GPU-based one) without changing a single line of code in the parent pipeline.