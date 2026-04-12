# 🟢 Level 1: Novice (Foundation)
**Goal:** Master the syntax, the lifecycle of `yield`, and the transition from "Materialized" (Lists) to "Lazy" (Generators).

---

## 1. The Counter Generator
**Challenge:** Implement a function `counter(n)` that yields integers from 0 to `n`.
* **Requirements:** * Must use `yield` inside a loop.
    * Must not create a list of `n` items in memory (e.g., `[i for i in range(n)]` is forbidden).
* **Evaluation:** Can you run `counter(10**9)` without an `OutOfMemoryError`?

## 2. The File Reader
**Challenge:** Implement `read_file_lazily(file_path)` to read a text file.
* **Requirements:** * Must yield one line at a time.
    * Do not use `file.readlines()`, as this loads the entire file into RAM.
* **Evaluation:** Verify that the peak memory usage remains constant regardless of the file size (e.g., a 5GB log file).

## 3. The Simple Filter
**Challenge:** Implement `even_filter(iterable)` using a generator expression.
* **Requirements:** * Use a single-line generator expression: `(x for x in ... if ...)`.
    * It must accept any iterable (list, tuple, or another generator).
* **Evaluation:** Does it return a generator object, or does it try to execute immediately?

## 4. The "Single-Use" Demo
**Challenge:** Create a script that demonstrates **Generator Exhaustion**.
* **Requirements:** * Define a generator `gen = (x for x in range(3))`.
    * Print the output of the generator once using a loop.
    * Attempt to print it a second time.
* **Evaluation:** Can you explain *why* the second loop produces no output using the term "Generator Exhaustion"?

## 5. The List Converter (The "Anti-Pattern" Test)
**Challenge:** Write a function `materialize(iterable)` that consumes a generator and returns a list.
* **Requirements:** * Take any generator as input.
    * Return a list containing all elements.
* **Evaluation:** Explain the trade-off. Why would you want to do this, and why is this almost always the *wrong* thing to do in a large-scale data pipeline?