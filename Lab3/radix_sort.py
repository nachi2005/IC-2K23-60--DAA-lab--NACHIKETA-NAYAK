# DAA Lab 3 - Program 3
# Radix Sort using LSD approach


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Convert count into cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy output back
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    arr = arr.copy()

    if not arr:
        return arr

    max_value = max(arr)

    exp = 1

    # Process ones, tens, hundreds, etc.
    while max_value // exp > 0:
        counting_sort(arr, exp)
        print(f"After sorting by place {exp}: {arr}")
        exp *= 10

    return arr


# Sample input
sample = [170, 45, 75, 90, 802, 24, 2, 66]

print("Original Array:", sample)

result = radix_sort(sample)

print("Final Radix Sort:", result)