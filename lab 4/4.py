# 4. Написати рекурсивну процедуру для виведення на екран цифр натурального числа у зворотному порядку.
a = input("Введіть натуральне числло: ")
def zvorot(a):
    d = a[::-1] # переворачиваем список вобратном порядке
    print(d)
zvorot