# DAA Lab 3 - Program 7
# Student Record Manager

import time
import contextlib
import io


from sorting_basic import bubble_sort, selection_sort, insertion_sort
from sorting_advanced import merge_sort, quick_sort, heap_sort
from binary_search import binary_search


# -------------------------------------------------
# Student Data
# -------------------------------------------------

students = [
    {"roll": 105, "name": "Rahul", "marks": 78},
    {"roll": 101, "name": "Aman", "marks": 92},
    {"roll": 108, "name": "Priya", "marks": 85},
    {"roll": 103, "name": "Neha", "marks": 74},
    {"roll": 110, "name": "Rohan", "marks": 88},
    {"roll": 102, "name": "Anjali", "marks": 95},
    {"roll": 107, "name": "Vikas", "marks": 69},
    {"roll": 104, "name": "Sneha", "marks": 81}
]


algorithms = {
    "1": ("Bubble Sort", bubble_sort),
    "2": ("Selection Sort", selection_sort),
    "3": ("Insertion Sort", insertion_sort),
    "4": ("Merge Sort", merge_sort),
    "5": ("Quick Sort", quick_sort),
    "6": ("Heap Sort", heap_sort)
}


# -------------------------------------------------
# Sorting Records
# -------------------------------------------------

def sort_records(records, field, algorithm):
    # Create (sorting_key, student_record) pairs
    data = []

    for student in records:
        data.append((student[field], student))

    # Sort using the selected DAA algorithm
    with contextlib.redirect_stdout(io.StringIO()):
        sorted_pairs = algorithm(data)

    return [pair[1] for pair in sorted_pairs]



def display_students(records):
    print("\nRoll No.   Name       Marks")
    print("-" * 30)

    for student in records:
        print(
            f"{student['roll']:<10}"
            f"{student['name']:<11}"
            f"{student['marks']}"
        )


# -------------------------------------------------
# Binary Search by Roll Number
# -------------------------------------------------

def search_student_by_roll(records, roll_number):

    # First sort records by roll number
    sorted_records = sort_records(
        records,
        "roll",
        merge_sort
    )

    roll_numbers = [student["roll"] for student in sorted_records]

    index = binary_search(roll_numbers, roll_number)

    if index != -1:
        return sorted_records[index]

    return None


# -------------------------------------------------
# Performance Comparison
# -------------------------------------------------

def performance_report(records, field):

    print("\nPerformance Report")
    print("=" * 55)

    results = []

    for name, algorithm in algorithms.values():

        start = time.perf_counter()

        # Repeat several times to get measurable timing
        for _ in range(1000):
            sort_records(records, field, algorithm)

        end = time.perf_counter()

        elapsed = end - start

        results.append((name, elapsed))

        print(f"{name:<20} {elapsed:.6f} seconds")

    fastest = min(results, key=lambda x: x[1])
    slowest = max(results, key=lambda x: x[1])

    difference = slowest[1] - fastest[1]

    print("\nComparative Performance Report")
    print("-" * 55)
    print(f"Fastest algorithm : {fastest[0]}")
    print(f"Time              : {fastest[1]:.6f} seconds")
    print(f"Slowest algorithm : {slowest[0]}")
    print(f"Time              : {slowest[1]:.6f} seconds")
    print(f"Difference        : {difference:.6f} seconds")


# -------------------------------------------------
# Main Menu
# -------------------------------------------------

while True:

    print("\n===== STUDENT RECORD MANAGER =====")

    print("\nStudent Records:")
    display_students(students)

    print("\nSort By:")
    print("1. Roll Number")
    print("2. Name")
    print("3. Marks")
    print("4. Search Student by Roll Number")
    print("5. Performance Comparison")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # Sorting
    if choice in ["1", "2", "3"]:

        fields = {
            "1": "roll",
            "2": "name",
            "3": "marks"
        }

        field = fields[choice]

        print("\nChoose Sorting Algorithm:")

        for key, value in algorithms.items():
            print(f"{key}. {value[0]}")

        algorithm_choice = input("Enter algorithm number: ")

        if algorithm_choice in algorithms:

            algorithm_name, algorithm = algorithms[algorithm_choice]

            sorted_records = sort_records(
                students,
                field,
                algorithm
            )

            print(
                f"\nSorted by {field} using {algorithm_name}:"
            )

            display_students(sorted_records)

        else:
            print("Invalid algorithm choice.")

    # Binary Search
    elif choice == "4":

        try:
            roll = int(input("Enter roll number to search: "))

            student = search_student_by_roll(
                students,
                roll
            )

            if student:
                print("\nStudent Found:")
                print("Roll Number:", student["roll"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
            else:
                print("\nStudent not found.")

        except ValueError:
            print("Please enter a valid roll number.")

    # Performance Comparison
    elif choice == "5":

        print("\nChoose field for performance comparison:")
        print("1. Roll Number")
        print("2. Name")
        print("3. Marks")

        field_choice = input("Enter choice: ")

        fields = {
            "1": "roll",
            "2": "name",
            "3": "marks"
        }

        if field_choice in fields:
            performance_report(
                students,
                fields[field_choice]
            )
        else:
            print("Invalid choice.")

    # Exit
    elif choice == "6":
        print("\nProgram ended.")
        break

    else:
        print("Invalid choice. Please try again.")