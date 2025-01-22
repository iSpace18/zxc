import numpy as np

# Коэффициенты системы уравнений
A = np.array([
    [6, -5, 7, 8],
    [3, 18, 2, 4],
    [3, 2, 3, 4],
    [1, 1, 1, 0]
])

# Вектор констант
b = np.array([3, 6, 1, 0])

# Решение системы уравнений
solution = np.linalg.solve(A, b)

# Вывод решения
x1, x2, x3, x4 = solution
print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
