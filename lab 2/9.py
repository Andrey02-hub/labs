# 9. Мастям гральних карт присвоєно порядкові номери: 1 - піки, 2 - трефи, 3 - бубни, 4 - черви.
# Вартості карт, які старші за десятку, привласнені номери: 11 - валет, 12 - дама, 13 - король, 14 - туз.
# Дано два цілих числа: N - вартість (6 ≤ N ≤ 14) і M - масть карти (1 ≤ M ≤ 4).
# Вивести назву відповідної карти виду «шістка бубон», «дама черв», «туз треф» і т. п.


print('І число від 11 до 14')

n = int(input())

if n < 11 | n > 14:
    if n == 11:
        b = 'валет '
        print(b)
    elif n == 12:
        b = 'дама '
        print(b)
    elif n == 13:
        b = 'король '
        print(b)
    elif n == 14:
        b = 'туз '
        print(b)

print('Введи будь-яке число від 1 до 4')
m = int(input())
if m < 1 | m > 4:
    if m == 1:
       a = 'піки '
       print(a)
    elif m == 2:
        a = 'трефи '
        print(a)
    elif m == 3:
        a = 'бубни '
        print(a)
    elif m == 4:
        a = 'черви '
        print(a)
z = n + m
print(z)




