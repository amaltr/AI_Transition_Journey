# 🔴 Level 3: Architect (System Design)
**Goal:** Master high-level orchestration, resource safety, and framework-level integration.

---

## 11. The "Resilient" Streamer (Advanced)
**Challenge:** Implement `guaranteed_file_reader(file_path)`.
* **Requirements:** * Must use a `try...finally` block.
    * Even if the user executes `break` or an exception occurs mid-iteration, the file must be closed.
* **Evaluation:** Run a test where you `break` the loop after 2 lines. Verify `file.closed` is `True` immediately afterward.

## 12. The "Circular" Shuffle-Buffer
**Challenge:** Implement `shuffle_stream(iterable, buffer_size)`.
* **Requirements:** * Maintain a buffer of size `buffer_size`.
    * Yield a random element from the buffer and immediately replace it with the next element from the `iterable`.
* **Evaluation:** Can you shuffle an infinite stream (`itertools.count()`) without memory bloat?

## 13. The "Two-Way" Coroutine Pipeline
**Challenge:** Implement `normalizer_coroutine()`.
* **Requirements:** * Initial call `next()` primes it. 
    * Subsequent `.send(value)` yields a normalized result.
    * If `.send(None)` is received, reset internal stats to 0.
* **Evaluation:** Verify that `.send(None)` acknowledges the reset without error.

## 14. The "Delegated" Multi-Source Pipeline
**Challenge:** Implement `master_pipeline(sources)` using `yield from`.
* **Requirements:** * Aggregate a list, a range, and a network-mock generator.
    * Wrap the network source to catch `ConnectionError` and failover to a static list.
* **Evaluation:** Ensure the caller sees a seamless stream despite the forced network failure.

## 15. The "Epoch-Aware" Batcher
**Challenge:** Create a `BatchGenerator` class.
* **Requirements:** * Implement `__iter__`. 
    * When the stream finishes, increment `epoch`, shuffle the dataset, and reset the internal iterator.
* **Evaluation:** Pass this class to a `for` loop that runs for 1000 steps; ensure the data reshuffles automatically at the end of every epoch.