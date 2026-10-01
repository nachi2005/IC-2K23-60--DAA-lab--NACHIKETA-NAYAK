# Section A: Concept Check

1. Bubble sort works by repeatedly swapping **adjacent** elements if they are in the wrong order.

2. Selection sort repeatedly finds the **minimum** element from the unsorted part and places it at the beginning.

3. Insertion sort builds the sorted portion one element at a time by **inserting** each new element into its correct position.

4. Merge sort follows a **divide and conquer** approach: split the array, sort each half, then combine.

5. Quick sort picks a **pivot** and partitions the array around it before recursing.

6. Heap sort relies on a data structure called a **heap**, which is typically implemented using an array.

7. Radix sort processes numbers digit by digit, starting from the **least** significant digit.

8. Binary search requires the input array to be **sorted** before it can be used.

9. In hashing, when two different keys map to the same index, this is called a **collision**.

10. Separate chaining resolves collisions by storing multiple values at the same index using a **linked list**, while linear probing resolves them by **probing the next available slot**.

# Section B: Trace the Logic

## 1. Bubble Sort

Array: [5, 2, 8, 1, 9]

After each swap:

- Swap 5 and 2 → [2, 5, 8, 1, 9]
- Swap 8 and 1 → [2, 5, 1, 8, 9]

Final array after one full pass:

[2, 5, 1, 8, 9]


## 2. Selection Sort

Array: [5, 2, 8, 1, 9]

- Step 1: Minimum = 1 → [1, 2, 8, 5, 9]
- Step 2: Minimum = 2 → [1, 2, 8, 5, 9]
- Step 3: Minimum = 5 → [1, 2, 5, 8, 9]
- Step 4: Minimum = 8 → [1, 2, 5, 8, 9]


## 3. Insertion Sort

Array: [5, 2, 8, 1, 9]

- Insert 2 → [2, 5, 8, 1, 9]
- Insert 8 → [2, 5, 8, 1, 9]
- Insert 1 → [1, 2, 5, 8, 9]
- Insert 9 → [1, 2, 5, 8, 9]


## 4. Merge Sort Splitting

Array: [8, 3, 5, 4, 7, 6, 1, 2]

First split:

[8, 3, 5, 4]    [7, 6, 1, 2]

Second split:

[8, 3]    [5, 4]    [7, 6]    [1, 2]

Final split:

[8] [3] [5] [4] [7] [6] [1] [2]


## 5. Quick Sort First Partition

Array: [8, 3, 5, 4, 7, 6, 1, 2]

Pivot = 2

After partition:

[1, 2, 5, 4, 7, 6, 8, 3]

Pivot final index = 1


## 6. Radix Sort

Array:

[170, 45, 75, 90, 802, 24, 2, 66]

After sorting by ones digit:

[170, 90, 802, 2, 24, 45, 75, 66]

After sorting by tens digit:

[802, 2, 24, 45, 66, 170, 75, 90]


## 7. Binary Search

Sorted array:

[2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

Target = 23

| Step | Low | High | Mid | Value |
|------|-----|------|-----|-------|
| 1 | 0 | 10 | 5 | 23 |

23 is found at index 5.


## 8. Hashing with Separate Chaining

Table size = 7

Hash function:

key % 7

Keys: 10, 3, 17, 24, 9

- 10 % 7 = 3 → Index 3
- 3 % 7 = 3 → Index 3 (Collision)
- 17 % 7 = 3 → Index 3 (Collision)
- 24 % 7 = 3 → Index 3 (Collision)
- 9 % 7 = 2 → Index 2

Final hash table:

- Index 0 → Empty
- Index 1 → Empty
- Index 2 → [9]
- Index 3 → [10, 3, 17, 24]
- Index 4 → Empty
- Index 5 → Empty
- Index 6 → Empty


## 9. Hashing with Linear Probing

Table size = 7

Hash function:

key % 7

- 10 → index 3
- 3 → index 3 occupied → index 4
- 17 → index 3 occupied → index 4 occupied → index 5
- 24 → index 3 occupied → 4 occupied → 5 occupied → index 6
- 9 → index 2

Final positions:

| Key | Final Index |
|-----|-------------|
| 10 | 3 |
| 3 | 4 |
| 17 | 5 |
| 24 | 6 |
| 9 | 2 |

# Section C: Programming Tasks

## Program 1: Basic Sorting Algorithms

### Aim
To implement Bubble Sort, Selection Sort, and Insertion Sort as separate functions.

### Logic
- Bubble Sort repeatedly swaps adjacent elements.
- Selection Sort finds the minimum element and places it at the correct position.
- Insertion Sort inserts each element into its correct position in the sorted part.

### Sample Input
[5, 2, 8, 1, 9]

### Sample Output
Sorted array: [1, 2, 5, 8, 9]

## Program 2: Advanced Sorting Algorithms

### Aim
To implement Merge Sort, Quick Sort, and Heap Sort as separate functions.

### Logic
- Merge Sort divides the array into smaller parts and merges them in sorted order.
- Quick Sort selects a pivot and partitions the array around the pivot.
- Heap Sort uses a heap data structure to sort the elements.

### Sample Input
[5, 2, 8, 1, 9, 3, 7]

### Sample Output
Sorted array: [1, 2, 3, 5, 7, 8, 9]

## Program 3: Radix Sort

### Aim
To implement Radix Sort for sorting non-negative integers.

### Logic
Radix Sort sorts numbers digit by digit, starting from the least significant digit. Counting Sort is used as a helper for each digit position.

### Sample Input
[170, 45, 75, 90, 802, 24, 2, 66]

### Sample Output
Sorted array: [2, 24, 45, 66, 75, 90, 170, 802]

## Program 4: Binary Search

### Aim
To implement Binary Search for finding an element in a sorted array.

### Logic
Binary Search repeatedly divides the sorted array into two halves. It compares the target element with the middle element and continues searching in the appropriate half.

### Sample Input
Array: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
Target: 23

### Sample Output
Element found at index: 5

# Section D: Timing Analysis and Graphs

## Program 5: Timing Analysis of Sorting Algorithms

### Aim
To compare the execution time of six sorting algorithms on different types of input.

### Logic
The program measures the execution time of Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort using random, sorted, and reverse-sorted inputs for different input sizes.

### Input Sizes
100, 500, 1000, 2000

### Input Types
- Random
- Sorted
- Reverse Sorted

### Algorithms Compared
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

## Program 6: Graphs and CSV

### Aim
To store the timing results in a CSV file and generate graphs for comparing sorting algorithms.

### Logic
The timing results are stored in `timing_results.csv`. The graph program reads the CSV file and generates separate graphs for different input types.

### Output Files
- `timing_results.csv`
- `random_input_timing.png`
- `sorted_input_timing.png`

### Graphs
The generated graphs show the execution time of the six sorting algorithms for different input sizes.

# Section E: Applications

## Program 7: Student Record Manager

### Aim
To create a Student Record Manager that sorts student records by Roll No, Name, or Marks and searches records using Binary Search.

### Logic
The program stores student records containing Roll No, Name, and Marks.

The user can:
- Sort records by Roll No.
- Sort records by Name.
- Sort records by Marks.
- Select any of the six sorting algorithms.
- Search for a student using Binary Search.
- Compare the execution time of all six sorting algorithms.

### Sample Input
Sort by: Roll No  
Algorithm: Bubble Sort

### Sample Output
Student records are displayed in sorted order.

Binary Search:
Search Roll No: 108  
Result: Student found — Priya

## Program 8: Search Engine Simulator

### Aim
To implement a simple search engine using Binary Search, Hashing with Separate Chaining, and Hashing with Linear Probing.

### Logic
The program stores a dictionary of words with associated document IDs.

Three search techniques are implemented:
- Binary Search
- Hashing with Separate Chaining
- Hashing with Linear Probing

The number of comparisons or probes is displayed for each search method.

### Sample Input
Search word: algorithm

### Sample Output
Binary Search: Word found
Hashing with Chaining: Word found
Hashing with Linear Probing: Word found

The number of comparisons/probes is displayed for each method.

# Section F: Analysis

## 1. Based on the Section D timing results, which algorithms performed noticeably worse on already-sorted input compared to random input?

Quick Sort performed noticeably worse on already-sorted input compared to random input, especially as the input size increased. For example, at n = 2000, Quick Sort took about 0.135212 seconds on sorted input compared to 0.005741 seconds on random input.

Merge Sort and Heap Sort remained relatively consistent across different input types. Bubble Sort became very fast on sorted input because the data was already in order.

---

## 2. Compare Bubble Sort, Selection Sort, and Insertion Sort on reverse-sorted input specifically.

For n = 2000 reverse-sorted input:

- Selection Sort = 0.474999 seconds
- Insertion Sort = 0.660892 seconds
- Bubble Sort = 0.679107 seconds

Therefore, Selection Sort was the fastest among these three for n = 2000, while Bubble Sort was the slowest. This is consistent with their expected time complexity because Selection Sort performs a similar number of comparisons regardless of input order, while Bubble Sort and Insertion Sort perform more work on reverse-sorted data.

---

## 3. Why does Quick Sort show a difference on already-sorted input?

The Quick Sort implementation used in this project selects the last element as the pivot.

For already-sorted or reverse-sorted data, choosing the last element can produce highly unbalanced partitions. This causes Quick Sort to approach its worst-case time complexity of O(n²).

This can be seen in the results: at n = 2000, Quick Sort took 0.005741 seconds on random input, but 0.135212 seconds on sorted input and 0.195801 seconds on reverse-sorted input.

---

## 4. How did Radix Sort perform relative to the other algorithms?

Radix Sort was not included in the empirical timing program in Section D. The timing program compared Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort.

Therefore, no direct timing comparison between Radix Sort and the other algorithms can be made from the collected Section D data.

Radix Sort is designed for non-negative integers and does not compare elements directly. Its usefulness depends on the number of digits and the range of the input values.

---

## 5. Compare Binary Search with the two hash table methods.

For the word "algorithm", the Search Engine Simulator produced:

- Binary Search: 5 comparisons
- Hashing with Separate Chaining: 1 comparison
- Hashing with Linear Probing: 1 probe

Therefore, for this particular search, both hashing methods required fewer steps than Binary Search.

Binary Search has O(log n) average search time on sorted data, while hashing provides O(1) average search time when the hash function and table load are suitable.

---

## 6. Compare Separate Chaining and Linear Probing for the dataset.

For the searched word "algorithm":

- Separate Chaining: 1 comparison
- Linear Probing: 1 probe

Both methods required the same number of search steps for this particular dataset and hash function.

If the hash table becomes much more full, such as around 90 percent occupied, Linear Probing can experience more clustering and therefore require more probes. Separate Chaining can continue storing multiple elements in the same bucket, although longer chains can increase the number of comparisons

# Section G: Final Documentation
## Program 1: Basic Sorting Algorithms

### Aim
To implement Bubble Sort, Selection Sort, and Insertion Sort as separate sorting functions.

### Logic
Bubble Sort repeatedly swaps adjacent elements when they are in the wrong order. Selection Sort finds the minimum element and places it in the correct position. Insertion Sort inserts each element into its correct position in the sorted portion.

### Sample Input
[5, 2, 8, 1, 9]

### Sample Output
[1, 2, 5, 8, 9]


## Program 2: Advanced Sorting Algorithms

### Aim
To implement Merge Sort, Quick Sort, and Heap Sort as separate sorting functions.

### Logic
Merge Sort divides the array and merges sorted parts. Quick Sort partitions the array using a pivot. The implementation uses the last element as the pivot. Heap Sort uses a heap structure to repeatedly select elements in sorted order.

### Sample Input
[5, 2, 8, 1, 9, 3, 7]

### Sample Output
[1, 2, 3, 5, 7, 8, 9]


## Program 3: Radix Sort

### Aim
To implement Radix Sort using the LSD approach for non-negative integers.

### Logic
The program processes numbers digit by digit starting from the least significant digit. Counting Sort is used as a helper function for sorting elements according to each digit.

### Sample Input
[170, 45, 75, 90, 802, 24, 2, 66]

### Sample Output
[2, 24, 45, 66, 75, 90, 170, 802]


## Program 4: Binary Search

### Aim
To implement iterative Binary Search on a sorted array.

### Logic
Binary Search compares the target with the middle element and repeatedly reduces the search range to half until the target is found or the range becomes empty.

### Sample Input
Array: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
Target: 23

### Sample Output
Element found at index: 5
## Program 5: Sorting Algorithm Timing Analysis

### Aim
To compare the execution time of six sorting algorithms on random, sorted, and reverse-sorted inputs.

### Logic
The program generates three types of input arrays for four different input sizes and measures the execution time of Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort.

### Actual Timing Results

#### Random Input

| Algorithm | n=100 | n=500 | n=1000 | n=2000 |
|---|---:|---:|---:|---:|
| Bubble Sort | 0.002016 | 0.038397 | 0.129672 | 0.672130 |
| Selection Sort | 0.001765 | 0.026073 | 0.096638 | 0.668279 |
| Insertion Sort | 0.001338 | 0.026339 | 0.102739 | 0.483259 |
| Merge Sort | 0.000329 | 0.001024 | 0.002130 | 0.005173 |
| Quick Sort | 0.000189 | 0.000584 | 0.001362 | 0.005741 |
| Heap Sort | 0.000257 | 0.001277 | 0.003720 | 0.013630 |

#### Sorted Input

| Algorithm | n=100 | n=500 | n=1000 | n=2000 |
|---|---:|---:|---:|---:|
| Bubble Sort | 0.000059 | 0.000088 | 0.000155 | 0.000498 |
| Selection Sort | 0.001459 | 0.026273 | 0.103422 | 0.395157 |
| Insertion Sort | 0.001226 | 0.021273 | 0.083354 | 0.278443 |
| Merge Sort | 0.000195 | 0.000867 | 0.002233 | 0.002933 |
| Quick Sort | 0.000463 | 0.009776 | 0.040581 | 0.135212 |
| Heap Sort | 0.000304 | 0.001731 | 0.006215 | 0.007490 |

#### Reverse Sorted Input

| Algorithm | n=100 | n=500 | n=1000 | n=2000 |
|---|---:|---:|---:|---:|
| Bubble Sort | 0.001189 | 0.043691 | 0.152203 | 0.679107 |
| Selection Sort | 0.000886 | 0.028712 | 0.106893 | 0.474999 |
| Insertion Sort | 0.001351 | 0.033848 | 0.170413 | 0.660892 |
| Merge Sort | 0.000325 | 0.003343 | 0.001797 | 0.003206 |
| Quick Sort | 0.000416 | 0.009047 | 0.039678 | 0.195801 |
| Heap Sort | 0.000422 | 0.001599 | 0.003177 | 0.005998 |

## Program 6: Graphs and CSV

### Aim
To visualize the timing results and store the raw timing data in CSV format.

### Logic
The program reads the timing data from the CSV file and creates graphs showing the execution time of the six sorting algorithms for different input sizes.

### Output Files

- `timing_results.csv`
- `random_input_timing.png`
- `sorted_input_timing.png`

### Random Input Graph

![Random Input Timing](random_input_timing.png)

### Sorted Input Graph

![Sorted Input Timing](sorted_input_timing.png)

## Program 7: Student Record Manager

### Aim
To manage student records by sorting them using different sorting algorithms and searching for a student by roll number.

### Logic
The program stores roll number, name, and marks. The user selects the field and sorting algorithm. Binary Search is used to search for a student after sorting by roll number.

### Sample Input

Sort by Roll Number  
Algorithm: Bubble Sort

### Sample Output

Student records are displayed in sorted order.

Binary Search:
Roll Number: 108  
Student Found: Priya

### Comparative Performance Report

| Algorithm | Time (seconds) |
|---|---:|
| Bubble Sort | 0.095341 |
| Selection Sort | 0.079783 |
| Insertion Sort | 0.066600 |
| Merge Sort | 0.009589 |
| Quick Sort | 0.012350 |
| Heap Sort | 0.015824 |

The measured time difference between the slowest and fastest algorithm was approximately 0.085752 seconds for this dataset.


## Program 8: Search Engine Simulator

### Aim
To implement a search engine using Binary Search, Separate Chaining, and Linear Probing.

### Logic
The program stores more than 30 words with document IDs. It searches for a word using a sorted list with Binary Search and two hash-table implementations using a custom hash function.

### Sample Input

Search word: algorithm

### Actual Search Results

| Search Method | Result | Comparisons / Probes |
|---|---|---:|
| Binary Search | Word found at index 0 | 5 comparisons |
| Hashing with Chaining | Word found | 1 comparison |
| Hashing with Linear Probing | Word found | 1 probe |

### Performance Observation

For the searched word "algorithm", both hashing methods required 1 step, while Binary Search required 5 comparisons.

## Final Summary

This lab implemented and analyzed fundamental sorting, searching, and hashing algorithms. The programs included basic and advanced sorting algorithms, Radix Sort, Binary Search, timing analysis, graph generation, a Student Record Manager, and a Search Engine Simulator.

The empirical results showed that the execution time depends on both the algorithm and the type of input data. The Search Engine Simulator also demonstrated the difference between Binary Search and hash-table based searching.