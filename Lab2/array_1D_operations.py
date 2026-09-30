# This program performs basic operations on a 1D array.

def insert_value(arr, index, value):
    if index < 0 or index > len(arr):
        print("Invalid index.")
        return

    arr.insert(index, value)
    print("Array after insertion:", arr)


def delete_value(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid index.")
        return

    arr.pop(index)
    print("Array after deletion:", arr)


def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            print("Value found at index:", i)
            return i

    print("Value not found.")
    return -1


def rotate_left(arr, k):
    if len(arr) == 0:
        print("Array is empty.")
        return

    k = k % len(arr)
    arr[:] = arr[k:] + arr[:k]
    print("Array after left rotation:", arr)


def rotate_right(arr, k):
    if len(arr) == 0:
        print("Array is empty.")
        return

    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k] if k != 0 else arr[:]
    print("Array after right rotation:", arr)


def main():
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

    while True:
        print("\n--- 1D Array Operations ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Linear Search")
        print("4. Rotate Left")
        print("5. Rotate Right")
        print("6. Display Array")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            index = int(input("Enter index: "))
            value = int(input("Enter value: "))
            insert_value(arr, index, value)

        elif choice == "2":
            index = int(input("Enter index: "))
            delete_value(arr, index)

        elif choice == "3":
            value = int(input("Enter value to search: "))
            linear_search(arr, value)

        elif choice == "4":
            k = int(input("Enter number of positions: "))
            rotate_left(arr, k)

        elif choice == "5":
            k = int(input("Enter number of positions: "))
            rotate_right(arr, k)

        elif choice == "6":
            print("Current array:", arr)

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()