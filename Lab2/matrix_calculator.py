# This program is a menu-driven matrix calculator.


def display_matrix(matrix):
    print("\nMatrix:")
    for row in matrix:
        print(row)


def read_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Invalid dimensions.")
        return None

    matrix = []

    print("Enter matrix elements row by row:")

    for i in range(rows):
        row = list(map(int, input(f"Row {i}: ").split()))

        if len(row) != cols:
            print("Invalid number of elements.")
            return None

        matrix.append(row)

    return matrix


def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Addition not possible: dimensions are different.")
        return None

    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    return result


def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        print("Multiplication not possible.")
        print("Columns of first matrix must equal rows of second matrix.")
        return None

    result = []

    for i in range(len(a)):
        row = []

        for j in range(len(b[0])):
            total = 0

            for k in range(len(b)):
                total += a[i][k] * b[k][j]

            row.append(total)

        result.append(row)

    return result


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        row = []

        for i in range(rows):
            row.append(matrix[i][j])

        result.append(row)

    return result


def determinant(matrix):
    n = len(matrix)

    if n != len(matrix[0]):
        print("Determinant is possible only for a square matrix.")
        return None

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - \
               (matrix[0][1] * matrix[1][0])

    if n == 3:
        return (
            matrix[0][0] * (
                matrix[1][1] * matrix[2][2] -
                matrix[1][2] * matrix[2][1]
            )
            - matrix[0][1] * (
                matrix[1][0] * matrix[2][2] -
                matrix[1][2] * matrix[2][0]
            )
            + matrix[0][2] * (
                matrix[1][0] * matrix[2][1] -
                matrix[1][1] * matrix[2][0]
            )
        )

    print("Determinant is implemented only for 1x1, 2x2 and 3x3 matrices.")
    return None


def main():
    while True:
        print("\n===== MATRIX CALCULATOR =====")
        print("1. Add two matrices")
        print("2. Multiply two matrices")
        print("3. Transpose a matrix")
        print("4. Find determinant")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEnter First Matrix")
            a = read_matrix()

            if a is None:
                continue

            print("\nEnter Second Matrix")
            b = read_matrix()

            if b is None:
                continue

            result = add_matrices(a, b)

            if result is not None:
                print("\nAddition Result:")
                display_matrix(result)

        elif choice == "2":
            print("\nEnter First Matrix")
            a = read_matrix()

            if a is None:
                continue

            print("\nEnter Second Matrix")
            b = read_matrix()

            if b is None:
                continue

            result = multiply_matrices(a, b)

            if result is not None:
                print("\nMultiplication Result:")
                display_matrix(result)

        elif choice == "3":
            print("\nEnter Matrix")
            matrix = read_matrix()

            if matrix is None:
                continue

            result = transpose_matrix(matrix)

            print("\nTranspose:")
            display_matrix(result)

        elif choice == "4":
            print("\nEnter Matrix")
            matrix = read_matrix()

            if matrix is None:
                continue

            result = determinant(matrix)

            if result is not None:
                print("\nDeterminant =", result)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()