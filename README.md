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

### 🗂 Repository Structure

