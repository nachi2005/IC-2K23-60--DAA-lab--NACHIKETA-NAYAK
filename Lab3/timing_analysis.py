# DAA Lab 3 - Program 5
# Sorting Algorithm Comparison

import random
import time
import sys
import contextlib
import io
import csv

sys.setrecursionlimit(10000)

from sorting_basic import bubble_sort, selection_sort, insertion_sort
from sorting_advanced import merge_sort, quick_sort, heap_sort


algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}


# Different input sizes
# Small sizes are used for the O(n^2) algorithms
sizes = [100, 500, 1000, 2000]


def generate_data(n, input_type):
    if input_type == "Random":
        return random.sample(range(n * 10), n)

    elif input_type == "Sorted":
        return list(range(n))

    elif input_type == "Reverse Sorted":
        return list(range(n - 1, -1, -1))


def measure_time(sort_function, data):
    start = time.perf_counter()

    # Hide sorting-process print statements during timing
    with contextlib.redirect_stdout(io.StringIO()):
        sort_function(data)

    end = time.perf_counter()

    return end - start


results = []

print("\nSorting Algorithm Timing Analysis")
print("=" * 75)

for n in sizes:

    for input_type in ["Random", "Sorted", "Reverse Sorted"]:

        data = generate_data(n, input_type)

        for algorithm_name, algorithm in algorithms.items():

            # Use a copy so every algorithm receives the same input
            test_data = data.copy()

            elapsed = measure_time(algorithm, test_data)

            results.append(
                [algorithm_name, input_type, n, elapsed]
            )

            print(
                f"{algorithm_name:<18} "
                f"{input_type:<15} "
                f"n={n:<5} "
                f"time={elapsed:.6f} seconds"
            )

print("\nTiming analysis completed.")

# Save timing results to CSV
with open("timing_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Algorithm",
        "Input Type",
        "Input Size",
        "Time (seconds)"
    ])

    for row in results:
        writer.writerow(row)

print("Timing data saved to timing_results.csv")