from fractions import Fraction
import numpy as np
from sympy.solvers import solve
from sympy import Symbol

# INFO : Constants
x = Symbol("x")


# INFO: Inputs
A = [[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]]

pivot = [1, 2]


# INFO : ref will solve a matrix, so the column with the pivot will have zero all the way expect where the pivot is. There it will be one
def ref(A, pivot):
    solutions = []
    for idx, row in enumerate(A):
        if idx == pivot[0]:
            val = 1
        else:
            val = 0
        solution = solve(A[idx, pivot[1]] + A[pivot[0], pivot[1]] * x - val, x)[0]
        solutions.append(solution)
    # Create identity matrix with the solutions
    I = np.identity(A.shape[0])
    B = []
    for solution, row in zip(solutions, I):
        B.append(solution * row)
    B = np.matrix(B)
    # Create matrix with only the row that needs to subtract from the rest
    row = A[pivot[0]]
    C = np.matrix(row)
    for i in range(A.shape[0] - 1):
        C = np.vstack((C, row))
    # The new matrix
    A_new = A + B * C
    return A_new, solutions


# print_matrix_with_frations_spacing will change matrix to fractions and print it with even spacing
def print_matrix_with_frations_spacing(A):
    A = np.matrix.tolist(A)
    # Create matrix B with the values from A as frations as strings
    B = []
    for idx, row in enumerate(A):
        B.append([])
        for val in row:
            if val % 1 == 0:
                val = round(val)
                B[idx].append(str(val))
            else:
                val = Fraction(float(val))
                val = val.limit_denominator(10)
                B[idx].append(str(val))
    # Find the length of the values in B
    C = []
    for idx, row in enumerate(B):
        C.append([])
        for val in row:
            C[idx].append(len(val))
    C = np.matrix(C)
    # Find the max lengt of values in C
    C_T = np.transpose(C)
    D = []
    for idx, row in enumerate(C_T):
        D.append([])
        val = np.amax(row)
        D[idx].append(val)
    # Rewrite the values in B with the right spacing between values
    for row in B:
        for idx, val in enumerate(row):
            row[idx] = " " + " " * (D[idx][0] - len(val)) + val
    # Print matrix B
    for row in B:
        print(" ".join(row))


if __name__ == "__main__":
    A = np.matrix(A)
    B, solutions = ref(A, pivot)
    print(f"{'='*15} Input {'='*15}")
    print()
    print_matrix_with_frations_spacing(A)
    print()
    print(f"{'='*15} Output {'='*15}")
    print()
    print_matrix_with_frations_spacing(B)
    print()
    print(f"Løsninger: {solutions}^T")
