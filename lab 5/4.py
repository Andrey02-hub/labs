# 4. Описати рекурсивную функцію Fib1 (N) цілого типу, яка обчислює N-й елемент послідовності чисел Фібоначчі (N - ціле число):
# F1 = F2 = 1, FK = FK-2 + FK-1, K = 3, 4, ....
# За допомогою цієї функції знайти п'ять чисел Фібоначчі з даними номерами,
# і вивести ці числа разом з кількістю рекурсивних викликів функції Fib1, потребовавшихся для їх знаходження.
N = int(input("Введіть ціле число: ")) - 2

def Fib1(N):
    fib1 = fib2 = 1
    i = 0
    while N > 0:
        fib1, fib2 = fib2, fib1 + fib2
        N -= 1
        i += 1
        print("виклик функції - ", i)
    print("N-й елемент послідовності чисел Фібоначчі = ", fib2)
Fib1(N)