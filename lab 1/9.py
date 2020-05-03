# Дано двозначне число. Знайти суму і добуток його цифр.
a = int(input('Введіть двозначне число'))

sum = 0
mult = 1

while a > 0:
    digit = a % 10
    sum += digit
    mult *= digit
    a = a // 10
print(sum)
print(mult)