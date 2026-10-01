# DAA Lab 3 - Program 2
# Merge Sort, Quick Sort and Heap Sort


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Pivot strategy: last element
    pivot = arr[-1]

    smaller = []
    greater = []

    for value in arr[:-1]:
        if value <= pivot:
            smaller.append(value)
        else:
            greater.append(value)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


def heap_sort(arr):
    arr = arr.copy()
    n = len(arr)

    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr


# Same sample array for all three algorithms
sample = [5, 2, 8, 1, 9, 3, 7]

print("Original Array:", sample)

print("\nMerge Sort:")
print("Sorted Array:", merge_sort(sample))

print("\nQuick Sort:")
print("Sorted Array:", quick_sort(sample))

print("\nHeap Sort:")
print("Sorted Array:", heap_sort(sample))