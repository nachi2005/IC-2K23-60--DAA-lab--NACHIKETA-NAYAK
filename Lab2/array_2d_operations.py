# This program performs basic operations on a 2D array.

def display_matrix(matrix):
    if not matrix:
        print("Matrix is empty.")
        return

    print("Current 2D array:")
    for row in matrix:
        print(row)


def insert_row(matrix, position, new_row):
    if position < 0 or position > len(matrix):
        print("Invalid position.")
        return

    if matrix and len(new_row) != len(matrix[0]):
        print("Invalid row size. It must match the existing rows.")
        return

    matrix.insert(position, new_row)
    display_matrix(matrix)


def delete_row(matrix, position):
    if position < 0 or position >= len(matrix):
        print("Invalid position.")
        return

    matrix.pop(position)
    display_matrix(matrix)


def search_value(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                print("Value found at row", i, "and column", j)
                return

    print("Value not found.")


def rotate_clockwise(matrix):
    if not matrix:
        print("Matrix is empty.")
        return

    rows = len(matrix)
    cols = len(matrix[0])

    rotated = []

    for j in range(cols):
        new_row = []
        for i in range(rows - 1, -1, -1):
            new_row.append(matrix[i][j])
        rotated.append(new_row)

    matrix[:] = rotated
    display_matrix(matrix)


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be greater than zero.")
        return

    matrix = []

    print("Enter matrix elements row by row:")

    for i in range(rows):
        row = list(map(int, input(f"Row {i}: ").split()))

        if len(row) != cols:
            print("Invalid number of elements in the row.")
            return

        matrix.append(row)

    display_matrix(matrix)

    while True:
        print("\n--- 2D Array Operations ---")
        print("1. Insert a row")
        print("2. Delete a row")
        print("3. Search for a value")
        print("4. Rotate 90 degrees clockwise")
        print("5. Display array")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            position = int(input("Enter position: "))
            new_row = list(map(int, input("Enter new row elements: ").split()))
            insert_row(matrix, position, new_row)

        elif choice == "2":
            position = int(input("Enter row position: "))
            delete_row(matrix, position)

        elif choice == "3":
            value = int(input("Enter value to search: "))
            search_value(matrix, value)

        elif choice == "4":
            rotate_clockwise(matrix)

        elif choice == "5":
            display_matrix(matrix)

        elif choice == "6":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
