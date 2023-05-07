import random

import numpy as np
from random import *


def transpose_matrix(m):
    return list(map(list, zip(*m)))

def get_matrix_minor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

def get_matrix_determinant(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * get_matrix_determinant(get_matrix_minor(m, 0, c))
    return determinant

def get_matrix_inverse(m):
    determinant = get_matrix_determinant(m)

    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]
    adjutants = []
    for r in range(len(m)):
        adjutants_row = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            adjutants_row.append(((-1) ** (r + c)) * get_matrix_determinant(minor))
        adjutants.append(adjutants_row)
    adjutants = transpose_matrix(adjutants)
    for r in range(len(adjutants)):
        for c in range(len(adjutants)):
            adjutants[r][c] = adjutants[r][c] / determinant
    return adjutants


matrix_1 = []
n = 11
for i in range(n):
    row = []
    for i in range(n):
        row.append(randint(1, 100))
    matrix_1.append(row)

a = np.linalg.inv(np.array(matrix_1))
# print(a)
# print()
inverse_matrix_1 = get_matrix_inverse(matrix_1)
# print(*inverse_matrix_1, sep="\n")
# for row_1 in inverse_matrix_1:
#     print(row_1)


c = np.array(inverse_matrix_1).dot(np.array(matrix_1))
for row in c:
    print(*row)
