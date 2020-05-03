# 19. Описати функцію IsSquare (K) логічного типу, яка повертає True,
# якщо цілий параметр K (> 0) є квадратом деякого цілого числа, і False в іншому випадку.
# З її допомогою знайти кількість квадратів в наборі з 10 цілих позитивних чисел.

import random

a = [random.randint(1,100) for i in range(10)]
print(a)

def isSquare(K):
    for i in range(1,K):
        if i**2 == K:
            return True
    return False

for i in a:
    print(isSquare(i))



