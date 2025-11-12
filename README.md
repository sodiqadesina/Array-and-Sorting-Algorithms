# 🧮 Array and Sorting Algorithms

This repository contains implementations and runtime analyses of key **sorting algorithms** 
The goal is to compare **different sorting paradigms** (comparison-based vs. distribution-based) using real numeric data — in this case, simulated phone numbers (`647-XXXXXXX`) from a telecommunications dataset.

---

## 📘 Overview

Sorting is a core algorithmic concept that affects the performance of nearly every data-processing pipeline.  
Here, five classical sorting algorithms are implemented from scratch (no built-in `sort()` or STL calls) and benchmarked on a uniform 7-digit numeric dataset.

| Algorithm | Paradigm | Best Case | Average | Worst | Space | Stable |
|------------|-----------|------------|-----------|----------|--------|---------|
| 🪣 **Bucket Sort** | Distribution | O(n + k) | O(n + k) | O(n²) | O(n + k) | ✅ |
| 🔢 **Radix Sort** | Non-comparison | O(nk) | O(nk) | O(nk) | O(n + k) | ✅ |
| ⚡ **Quick Sort** | Divide-and-Conquer | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| ✍️ **Insertion Sort** | Incremental | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| 💨 **Bubble Sort** | Exchange | O(n) | O(n²) | O(n²) | O(1) | ✅ |

---

## ⚙️ Implementations


Each script:
- Loads `Bell.txt` (list of phone numbers: `647-XXXXXXX`)
- Extracts the 7-digit numeric portion  
- Applies a sorting algorithm  
- Tracks runtime (`time.time()`)
- Outputs results to a new file (e.g., `Quick_Sorted_Bell.txt`)

---

## 🧩 Problem Statement

> As a data analyst at telecoms company say  **Bell Inc.** for example, your task is to manage a large list of phone numbers and sort them efficiently using various algorithms.  
> The objective is to evaluate the **execution time and efficiency trade-offs** between each sorting approach under identical conditions.



---

## 💻 Example Workflow

```bash
# Example run for Quick Sort
$ python part2-1-3.py
Quick Sort took 11.500283 seconds and sorted numbers are saved in 'Quick_Sorted_Bell.txt'.

Sample Input

647-9234567
647-1234567
647-8456123
647-2678912


Sample Output

647-1234567
647-2678912
647-8456123
647-9234567

```
⏱️ Benchmark Results
| Algorithm      | Dataset Size    | Time (s)  | Notes                                                     |
| -------------- | --------------- | --------- | --------------------------------------------------------- |
| Bucket Sort    | ~4,000,000      | **3.905** | Fastest; efficient for uniformly distributed numeric data |
| Radix Sort     | ~4,000,000      | 11.145    | Strong performance; digit-wise stable                     |
| Quick Sort     | ~4,000,000      | 11.500    | Competitive; performance depends on pivot selection       |
| Insertion Sort | 40,000 (sample) | 21.627    | Inefficient for large data, quadratic growth              |
| Bubble Sort    | 40,000 (sample) | 51.121    | Slowest; purely educational                               |

