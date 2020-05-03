# 3. Написати функцію, яка розраховує суму елементів головної або побічної діагоналі матриці.
# Матрицю заповнити випадковими числами.
import random
M,N = 3,3
matrix = [[random.randrange(0,10) for y in range(M)] for x in range(N)]
for im in range(M):
    print (matrix[im])

