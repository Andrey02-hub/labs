# 6. Дано ціле число в діапазоні 1-7. Вивести рядок - назва дня тижня, що відповідає даному числу (1 - «понеділок», 2 - «вівторок» і т. д.).
import random

n=7
b=random.randint(0,n)

if b == 1:
    print('Понеділок')
if b == 2:
    print('Вівторок')
if b == 3:
    print('Середа')
if b == 4:
    print('Четверг')
if b == 5:
    print("П'ятниця")
if b == 6:
    print('Субота')
if b == 7:
    print('Неділя')
