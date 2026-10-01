# DAA Lab 3 - Program 6
# Graphing Timing Results

import csv
import matplotlib.pyplot as plt


results = []

# Read timing data from CSV
with open("timing_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        results.append({
            "algorithm": row["Algorithm"],
            "input_type": row["Input Type"],
            "n": int(row["Input Size"]),
            "time": float(row["Time (seconds)"])
        })


algorithms = [
    "Bubble Sort",
    "Selection Sort",
    "Insertion Sort",
    "Merge Sort",
    "Quick Sort",
    "Heap Sort"
]


# -------------------------------------------------
# Graph 1: Random Input
# -------------------------------------------------

plt.figure()

for algorithm in algorithms:

    data = [
        r for r in results
        if r["algorithm"] == algorithm
        and r["input_type"] == "Random"
    ]

    data.sort(key=lambda x: x["n"])

    x = [r["n"] for r in data]
    y = [r["time"] for r in data]

    plt.plot(x, y, marker="o", label=algorithm)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithms - Random Input")
plt.legend()
plt.grid(True)

plt.savefig("random_input_timing.png")
plt.show()


# -------------------------------------------------
# Graph 2: Already Sorted Input
# -------------------------------------------------

plt.figure()

for algorithm in algorithms:

    data = [
        r for r in results
        if r["algorithm"] == algorithm
        and r["input_type"] == "Sorted"
    ]

    data.sort(key=lambda x: x["n"])

    x = [r["n"] for r in data]
    y = [r["time"] for r in data]

    plt.plot(x, y, marker="o", label=algorithm)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithms - Already Sorted Input")
plt.legend()
plt.grid(True)

plt.savefig("sorted_input_timing.png")
plt.show()


print("Graphs created successfully!")
print("1. random_input_timing.png")
print("2. sorted_input_timing.png")