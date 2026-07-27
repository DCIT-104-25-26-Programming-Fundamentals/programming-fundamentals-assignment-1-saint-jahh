# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            value = int(input(f"Enter value for matrix[{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def add_matrices(first, second):
    result = []
    for i in range(len(first)):
        row = []
        for j in range(len(first[0])):
            row.append(first[i][j] + second[i][j])
        result.append(row)
    return result


def subtract_matrices(first, second):
    result = []
    for i in range(len(first)):
        row = []
        for j in range(len(first[0])):
            row.append(first[i][j] - second[i][j])
        result.append(row)
    return result


def multiply_matrices(first, second):
    if len(first[0]) != len(second):
        return None

    result = []
    for i in range(len(first)):
        row = []
        for j in range(len(second[0])):
            total = 0
            for k in range(len(second)):
                total += first[i][k] * second[k][j]
            row.append(total)
        result.append(row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    print("Enter first matrix:")
    first_matrix = read_matrix(rows, columns)

    print("Enter second matrix:")
    second_matrix = read_matrix(rows, columns)

    print("\nSum:")
    print_matrix(add_matrices(first_matrix, second_matrix))

    print("\nDifference:")
    print_matrix(subtract_matrices(first_matrix, second_matrix))

    product = multiply_matrices(first_matrix, second_matrix)
    if product is None:
        print("\nMatrix multiplication is not possible with these dimensions.")
    else:
        print("\nProduct:")
        print_matrix(product)


if __name__ == "__main__":
    main()

