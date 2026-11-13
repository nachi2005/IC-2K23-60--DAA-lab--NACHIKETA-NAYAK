# DAA Lab Task 1 - Part 1
# Find the largest number and sort the list

numbers = [8, 3, 15, 6, 2]

# Find the largest number
maximum = numbers[0]
comparisons = 0

for i in range(1, len(numbers)):
    comparisons += 1

    if numbers[i] > maximum:
        maximum = numbers[i]

print("Original List:", numbers)
print("Largest Number:", maximum)
print("Comparisons Made:", comparisons)

# Sort the list using Bubble Sort
arr = numbers.copy()
n = len(arr)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted List:", arr)
