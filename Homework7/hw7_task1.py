# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.

import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
            # s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
                s += f'{self.matrix[i][j]:03} '
            s += "\n"
        return s

    # def __add__(self, other):
    #     if len(self.matrix) != len(other.matrix):
    #         return None
    #     res = copy.deepcopy(self.matrix)
    #     for i in range(len(self.matrix)):
    #         for k in range(len(self.matrix[i])):
    #             res[i][k] = self.matrix[i][k] + other.matrix[i][k]
    #     return Matrix(res)

    def __add__(self, other):
        # matrix = []
        # for i in range(len(self.matrix)):
        #     row = []
        #     for j in range(len(self.matrix[i])):
        #         matrx = self.matrix[i][j] + other.matrix[i][j]
        #         row.append(matrx)
        #     matrix.append(row)
        matrix = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))]
            for i in range(len(self.matrix))]
        return Matrix(matrix)




m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[15,71,38],[44,22,76],[77,88,9]]
m = Matrix(m1)
s = Matrix(m2)
print(m)
print(s)
t = m + s
print('sum ')
print(t)
print(type(t))



