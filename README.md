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
## ⏱️ Benchmark Results

<img width="1819" height="1182" alt="report" src="https://github.com/user-attachments/assets/f0d2ec32-ce1c-4184-ab04-31fa24001e79" />

I ran the five sorting algorithms (Bucket Sort, Radix Sort, Quick Sort, Insertion Sort, and Bubble Sort) one after the other, and here are the results I got from the console, as shown in the attached image:
Bucket Sort: 3.905046 seconds
Radix Sort: 11.145777 seconds
Quick Sort: 11.500283 seconds
Insertion Sort (Sample of 40,000 numbers): 21.626634 seconds
Bubble Sort (Sample of 40,000 numbers): 51.121498 seconds

| Algorithm      | Dataset Size    | Time (s)  | Notes                                                     |
| -------------- | --------------- | --------- | --------------------------------------------------------- |
| Bucket Sort    | ~4,000,000      | **3.905** | Fastest; efficient for uniformly distributed numeric data |
| Radix Sort     | ~4,000,000      | 11.145    | Strong performance; digit-wise stable                     |
| Quick Sort     | ~4,000,000      | 11.500    | Competitive; performance depends on pivot selection       |
| Insertion Sort | 40,000 (sample) | 21.627    | Inefficient for large data, quadratic growth              |
| Bubble Sort    | 40,000 (sample) | 51.121    | Slowest; purely educational                               |

## Analysis of the Results

Bucket Sort was the fastest, clocking in at around 3.9 seconds. This is expected because Bucket Sort works well when the data is uniformly distributed, which is the case with these 7-digit phone numbers. By placing the numbers into different "buckets" and sorting each bucket individually, it greatly reduces the overall complexity compared to other sorting methods that rely on comparing elements directly.

Radix Sort took around 11.1 seconds. While this is slower than Bucket Sort, it's still relatively fast. Radix Sort processes the numbers digit by digit, which means it makes multiple passes over the data. Each pass sorts by a single digit, which adds to the overall time taken. Even though it performs more operations than Bucket Sort, it’s still faster than comparison-based sorts like Quick Sort for this type of data.

Quick Sort performed similarly to Radix Sort, taking about 11.5 seconds. This algorithm is usually quite efficient for large datasets, with an average time complexity of O(n log n). However, Quick Sort’s speed can vary depending on how balanced the partitions are. In this case, it was slightly slower than Radix Sort, but still competitive for a comparison-based algorithm.

Insertion Sort took much longer at 21.6 seconds, even though I only sorted a sample of 40,000 numbers (instead of the full 4 million). Insertion Sort works by repeatedly inserting each element into its correct position in the sorted section of the array. This leads to O(n²) time complexity, which explains why it slows down significantly with larger datasets. It’s more suited for smaller datasets, and its quadratic nature makes it much less efficient than the other algorithms.

Bubble Sort was the slowest, taking 51.1 seconds for the same 40,000-sample dataset. This algorithm repeatedly compares and swaps adjacent elements if they are in the wrong order, which also gives it an O(n²) time complexity. Like Insertion Sort, Bubble Sort is not efficient for large datasets, and its performance suffers significantly as the number of elements increases.

In conclusion, Bucket Sort and Radix Sort are the most efficient for sorting large sets of phone numbers due to their near-linear time complexity, with Bucket Sort performing best in this case. Quick Sort also performed well, though slightly slower, likely due to its reliance on comparisons. On the other hand, Insertion Sort and Bubble Sort, both O(n²) algorithms, took significantly longer, even with a much smaller dataset sample, proving they are not ideal for handling large datasets.
