from envtest import my_mat_solve

from sympy import Matrix


A = Matrix([[1, 2], [3, 4]])
b = Matrix([5, 6])

x = my_mat_solve(A, b)

print(x)