#9. Описати рекурсивную функцію MaxElem (A, N) цілого типу,
# яка знаходить максимальний елемент цілочисельного масиву A розміру N (1 ≤ N ≤ 10),
# не використовуючи оператор циклу.
# За допомогою цієї функції знайти максимальні елементи масивів A, B, C розміру NA, NB, NC відповідно.
import random
N = random.randint(0, 10)
def MaxElem(A, N):
    print(max(A))
    print(max(B))
    print(max(C))

A = [i for i in range (N)]
B = [i for i in range (N)]
C = [i for i in range (N)]
print(A, B, C)
MaxElem(A, N)
