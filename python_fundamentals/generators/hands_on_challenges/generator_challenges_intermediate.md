# 🟡 Level 2: Intermediate (Engineering Logic)
**Goal:** Master the Factory Pattern, error handling, composition, and state management.

---

## 6. The Generator Factory
**Challenge:** Create a function `get_numbers(n)` that acts as a Factory.
* **Requirements:** * Return a generator that yields numbers from 0 to `n`.
    * Ensure the generator can be invoked multiple times (e.g., `gen1 = get_numbers(5)`, `gen2 = get_numbers(5)`).
* **Evaluation:** Can you iterate through the generator three separate times without manual reset logic?

## 7. The Resilient Streamer
**Challenge:** Implement `safe_json_reader(file_path)`.
* **Requirements:** * Read line-by-line, attempting `json.loads(line)`.
    * If a `ValueError` occurs, log the error and skip.
    * Do not stop the iteration.
* **Evaluation:** Does the generator successfully yield the 1st and 3rd lines if the 2nd line is invalid JSON?

## 8. The Sequence Chainer
**Challenge:** Implement `chain_generators(gen1, gen2)`.
* **Requirements:** * Use `itertools.chain()` or a manual loop to join two streams.
    * Do not store all elements in a list.
* **Evaluation:** If `gen1` is infinite and `gen2` is finite, will it ever reach `gen2`? (Discuss the theoretical limit).

## 9. The Stateful Accumulator
**Challenge:** Implement `running_total(iterable)`.
* **Requirements:** * Maintain internal state (`total`).
    * Yield the current sum at each step.
* **Evaluation:** Can you track the state across multiple `next()` calls?

## 10. The Batcher
**Challenge:** Implement `batch_data(iterable, batch_size)`.
* **Requirements:** * Take an iterable and group items into lists of size `batch_size`.
    * Ensure the final batch yields even if it's smaller than `batch_size`.
* **Evaluation:** If you pass `range(5)` and `batch_size=2`, do you get `[0, 1]`, `[2, 3]`, `[4]`?