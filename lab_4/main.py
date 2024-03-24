import numpy as np


def print_mat(matrix):
    for row in matrix:
        for elem in row:
            print("%.2f" % elem, end='\t\t')
        print("")
    print("")


def to_float(x):
    return float(x.strip())


def load_data(file):
    file.readline()

    b = np.array(list(map(to_float, file.readline().strip().split("\t"))), dtype=np.float64)

    file.readline()

    a = np.array(list(map(lambda x: list(map(to_float, x.strip().split("\t"))), file.readlines())), dtype=np.float64)

    return np.c_[a, b]


def sort_mat(matrix, mat_size):
    found = False
    for i in range(mat_size):
        if matrix[i][i] == 0:
            found = True
            break

    if not found:
        return matrix

    weights = []
    for i in range(mat_size):
        weight = 0
        for j in reversed(range(mat_size)):
            if matrix[i][j] == 0:
                if j == mat_size - 1:
                    weight = mat_size + 1
                break

            weight += 1

        weights.append({"row": matrix[i], "weight": weight})

    weights.sort(key=lambda x: x["weight"], reverse=True)

    matrix = np.array(list(map(lambda x: x["row"], weights)), dtype=np.float64)

    print("Sorted:")
    print_mat(matrix)

    return matrix


def gauss(mat):
    matSize = len(mat)

    print("Loaded:")
    print_mat(mat)

    mat = sort_mat(mat, matSize)

    for i in range(len(mat)):
        for j in range(1 + i, len(mat)):
            mul = mat[j][i] / mat[i][i]

            if np.all(mat[j][:matSize] - mul * mat[i][:matSize] == 0):
                raise ArithmeticError("Cannot multiply (linearly dependent lines)")

            mat[j] -= mul * mat[i]

            print("Multiplied:")
            print_mat(mat)

    results = []

    for i in reversed(range(matSize)):
        res = mat[i][matSize]
        k = len(results) - 1

        for j in range(i + 1, matSize):
            res -= mat[i][j] * results[k]
            k -= 1

        res /= mat[i][i]
        mat = sort_mat(mat, matSize)

        results.append(res)

    print(results)


with open("gauss_elimination_gr1_C.txt", 'r') as f:
    gauss(load_data(f))
