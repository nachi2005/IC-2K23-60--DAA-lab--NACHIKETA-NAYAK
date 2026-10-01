# DAA Lab 3 - Program 4
# Binary Search (Iterative)


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Sorted sample array
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

# Test 1: Value exists
target1 = 23
result1 = binary_search(arr, target1)

print("Array:", arr)
print("Searching for:", target1)
print("Index:", result1)

# Test 2: Value does not exist
target2 = 30
result2 = binary_search(arr, target2)

print("\nSearching for:", target2)
print("Index:", result2)