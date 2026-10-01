# DAA Lab 3 - Program 1
# Bubble Sort, Selection Sort and Insertion Sort


def bubble_sort(arr):
    arr = arr.copy()

    print("\nBubble Sort:")
    for i in range(len(arr)):
        swapped = False

        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        print(f"Pass {i + 1}: {arr}")

        if not swapped:
            break

    return arr


def selection_sort(arr):
    arr = arr.copy()

    print("\nSelection Sort:")
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Step {i + 1}: {arr}")

    return arr


def insertion_sort(arr):
    arr = arr.copy()

    print("\nInsertion Sort:")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        print(f"Step {i}: {arr}")

    return arr


# Same sample array for all three algorithms
sample = [5, 2, 8, 1, 9]

print("Original Array:", sample)

result1 = bubble_sort(sample)
print("Final Bubble Sort:", result1)

result2 = selection_sort(sample)
print("Final Selection Sort:", result2)

result3 = insertion_sort(sample)
print("Final Insertion Sort:", result3)