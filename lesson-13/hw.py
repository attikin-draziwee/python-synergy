import random


def printMatrix(matrix):
    for i in matrix:
        print(*i, sep=", ")


# Задание 1
columns = int(input("Введите количество столбцов (A) в матрице (A x B): "))
rows = int(input("Введите количество строк (B) в матрице (A x B): "))

matrix_a = [[random.randint(-100, 100)
             for b in range(columns)] for a in range(rows)]

print("Первая матрица")
printMatrix(matrix_a)

matrix_b = [[random.randint(-100, 100)
             for b in range(columns)] for a in range(rows)]
print("Вторая матрица")
printMatrix(matrix_b)

matrix_c = []

for row in range(rows):
    result = list(matrix_a[row][column] + matrix_b[row][column]
                  for column in range(0, len(matrix_a[row])))
    matrix_c.append(result)

print("Результат сложения")
printMatrix(matrix_c)
