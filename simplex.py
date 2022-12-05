import numpy as np
from sympy.solvers import solve
from sympy import Symbol
from fractions import Fraction


# NOTE : Change these values
A = [
    [1, 1, 2, 1, 0, 0],
    [2, 0, 3, 0, 1, 0],
    [2, 1, 4, 0, 0, 1]
]

B = [
    [0],
    [4],
    [5],
    [7]
]

C = [
    [-3, -2, -4, 0, 0, 0]
]


# NOTE : Constants
x = Symbol('x')
ERROR_RUN_TIME = 20
ERROR_VALUE = 1 * 10**(-10)


def find_names(lenght):
    names = []
    for idx in range(lenght):
        names.append(f'x{idx+1}')
    return names


def find_base_solutions(lenght, Mat):
    solutions = []
    for idx in range(rows - 1):
        val = float_to_fraction(Mat[idx+1, cols-1])
        solutions.append(str(val))
    base_solutions = ['0' for i in range(lenght)]
    for idx, elem in enumerate(base):
        base_solutions[int(elem)-1] = str(solutions[idx])
    return base_solutions


def find_base(A):
    A = np.matrix.tolist(A)
    A_T = np.transpose(A)
    base = []
    for idx, row in enumerate(A_T):
        one = False
        found = True
        for val in row:
            # NOTE : Because we work with fractions, then we need a error value to round values up to
            if 0 - ERROR_VALUE < val < 0 + ERROR_VALUE:
                pass
            elif 1 - ERROR_VALUE < val < 1 + ERROR_VALUE and one == False:
                one = True
            else:
                found = False
                break
        if found == True:
            base.append(idx + 1)
    return base


def base_changes(A, B):
    old = find_base(A)
    new = find_base(B)
    base_in = list(set(new) - set(old))
    base_out = list(set(old) - set(new))
    return base_in[0], base_out[0]


def float_to_fraction(val):
    val = Fraction(float(val))
    val = val.limit_denominator(10)
    return val


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


def print_tableau_with_frations_spacing(A):
    lenght = A.shape[1]
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
                val = float_to_fraction(val)
                B[idx].append(str(val))
    # FIXME: Fixeds values
    # Find the length of the values in B
    C = []
    for idx, row in enumerate(B):
        C.append([])
        for idx2, val in enumerate(row):
            if len(val) > 2:
                lengh = len(val)
            else:
                lengh = 2
            if idx2 == len(row) - 1:
                lengh = 3
            C[idx].append(lengh)
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
            row[idx] = ' ' + ' '*(D[idx][0] - len(val)) + val
    # Print matrix B
    # FIXME: Can only do up to x9
    names = []
    for num in range(lenght - 1):
        names.append(f" {' '*(D[num][0] - 2)}x{num+1}")
    names.append(f" {' '*(D[num][0] - 3)}RHS")
    lenght = len(str(' '.join(names)))
    print(' '.join(names))
    for idx, row in enumerate(B):
        if idx == 0 or idx == 1:
            print("-"*lenght)
        print(' '.join(row))


def set_up(A, B, C):
    # Create numpy matrices
    A = np.matrix(A)
    B = np.matrix(B)
    C = np.matrix(C)
    Mat = np.vstack((C, A))
    Mat = np.hstack((Mat, B))
    # NOTE : Print info to user
    base = [str(val) for val in find_base(Mat)]
    print(f"{'='*20} SIMPLEX 0 {'='*20}")
    print()
    print(f"Basen er ({', '.join(base)})")
    print_tableau_with_frations_spacing(Mat)
    return Mat


Mat = set_up(A, B, C)

count = 0
while count < ERROR_RUN_TIME:
    count += 1

    # NOTE : Simplex
    neg_val = np.amin(Mat[0])
    if neg_val >= 0:
        # NOTE : Simplex is solve
        print()
        print()
        names = find_names(Mat.shape[1] - 1)
        base_solutions = find_base_solutions((Mat.shape[1] - 1), Mat)
        print(f"Dermed ses det, at alle reduceret omkostninger er ikke-negative og løsningen ({', '.join(names)}) = ({', '.join(base_solutions)}) er optimal")
        break
    pivot_col = np.argmin(Mat[0])
    rows, cols = Mat.shape
    theta = []
    print_theta = []
    for idx in range(rows - 1):
        if Mat[idx+1, pivot_col] > 0:
            theta.append(Mat[idx+1, cols-1] / Mat[idx+1, pivot_col])
            a = float_to_fraction(Mat[idx+1, cols-1])
            b = float_to_fraction(Mat[idx+1, pivot_col])
            print_theta.append(f"{a}/{b}")
        else:
            theta.append(float('inf'))
    a = float_to_fraction(np.amin(theta))
    b = np.argmin(theta) + 1

    neg_val = float_to_fraction(neg_val)
    old_Mat = Mat
    Mat, solutions = ref(Mat, [b, pivot_col])
    base_in, base_out = base_changes(old_Mat, Mat)
    base = [str(val) for val in find_base(Mat)]

    # NOTE : Print info to user
    print(f"\n")
    print(f"{'='*20} SIMPLEX {count} {'='*20}")
    print()
    print(f"Den største negative værdi i omkostningerne er {neg_val}")
    print(f"Theta = min({', '.join(print_theta)}) = {a}")
    print(f"x{base_in} skal ind i basen, mens x{base_out} skal ud. Dermed er basen ({', '.join(base)})")
    print("Dermed")
    print_tableau_with_frations_spacing(Mat)
