# This program performs sparse matrix representation and operations.


def matrix_to_sparse(matrix):
    sparse = []

    rows = len(matrix)
    cols = len(matrix[0])
    non_zero = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                non_zero += 1

    # Header: rows, columns, number of non-zero elements
    sparse.append([rows, cols, non_zero])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])

    return sparse


def sparse_to_matrix(sparse):
    rows = sparse[0][0]
    cols = sparse[0][1]

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for item in sparse[1:]:
        row = item[0]
        col = item[1]
        value = item[2]
        matrix[row][col] = value

    return matrix


def add_sparse_matrices(sparse1, sparse2):
    if sparse1[0][0] != sparse2[0][0] or sparse1[0][1] != sparse2[0][1]:
        print("Matrices have incompatible dimensions.")
        return None

    result = []

    rows = sparse1[0][0]
    cols = sparse1[0][1]

    i = 1
    j = 1

    while i < len(sparse1) and j < len(sparse2):
        r1, c1, v1 = sparse1[i]
        r2, c2, v2 = sparse2[j]

        if (r1, c1) == (r2, c2):
            value = v1 + v2

            if value != 0:
                result.append([r1, c1, value])

            i += 1
            j += 1

        elif (r1, c1) < (r2, c2):
            result.append([r1, c1, v1])
            i += 1

        else:
            result.append([r2, c2, v2])
            j += 1

    while i < len(sparse1):
        result.append(sparse1[i])
        i += 1

    while j < len(sparse2):
        result.append(sparse2[j])
        j += 1

    return [[rows, cols, len(result)]] + result


def display_sparse(sparse):
    print("\nSparse Triple Representation:")
    print("Row  Column  Value")

    for item in sparse:
        print(item[0], "    ", item[1], "    ", item[2])


def display_matrix(matrix):
    print("\nFull Matrix:")

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


def main():
    print("=== Sparse Matrix Operations ===")

    print("\nEnter First Matrix")
    matrix1 = read_matrix()

    if matrix1 is None:
        return

    print("\nEnter Second Matrix")
    matrix2 = read_matrix()

    if matrix2 is None:
        return

    sparse1 = matrix_to_sparse(matrix1)
    sparse2 = matrix_to_sparse(matrix2)

    print("\n--- First Matrix ---")
    display_sparse(sparse1)
    display_matrix(sparse_to_matrix(sparse1))

    print("\n--- Second Matrix ---")
    display_sparse(sparse2)
    display_matrix(sparse_to_matrix(sparse2))

    result = add_sparse_matrices(sparse1, sparse2)

    if result is not None:
        print("\n--- Addition Result ---")
        display_sparse(result)
        display_matrix(sparse_to_matrix(result))


if __name__ == "__main__":
    main()