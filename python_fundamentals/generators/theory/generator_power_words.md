# 📕 Power Word Glossary: Python Data Engineering
**Topic:** Generators, Iterators, and Memory Management
**Purpose:** Use these terms to signal architectural depth in technical interviews.

---

### 1. Architectural Terms (The "Why")
* **Lazy Evaluation:** The strategy of delaying the evaluation of an expression until its value is actually needed. 
    * *Contrast:* **Eager Evaluation** (Lists).
* **O(1) Memory Footprint:** Constant space complexity. Regardless of whether the data source has 10 items or 10 billion, a generator uses the same amount of RAM.
* **Data Ingestion Layer:** The part of a system responsible for bringing data from a source (disk, API, database) into the application. Generators are the standard for high-performance ingestion.
* **Pipeline Composition:** The practice of chaining multiple generators together (Filter -> Map -> Batch).

### 2. Mechanical Terms (The "How")
* **State Machine:** A generator is technically a state machine. It remembers where it left off (the instruction pointer) and the value of all local variables.
* **Stack Frame Preservation:** Unlike a standard function where the stack frame is destroyed on `return`, a generator’s stack frame is **suspended** and kept alive during a `yield`.
* **Instruction Pointer:** The internal "bookmark" that tells Python which line of code to execute next when the generator is resumed.
* **StopIteration:** The specific exception raised by Python to signal that a generator has been exhausted and has no more values to provide.

### 3. Professional Implementation Terms (The "Hands-on")
* **Generator Exhaustion:** The technical term for when a generator has been fully iterated and cannot be used again.
* **Generator Factory:** A function or class pattern used to "re-instantiate" a generator, solving the exhaustion problem for multi-epoch training.
* **Producer-Consumer Pattern:** A design pattern where the generator (Producer) creates data and a loop/model (Consumer) processes it. 
* **Backpressure:** (Advanced) A situation where the consumer is slower than the producer. Generators handle this naturally because they only "produce" when the consumer asks for the next item.

### 4. Advanced Syntax Terms
* **Delegated Iteration (`yield from`):** The process of one generator handing over control to another sub-generator.
* **Iterable vs. Iterator:** * **Iterable:** Anything you can loop over (List, String, or a Factory function). 
    * **Iterator:** The actual object that produces values one by one (The Generator object).