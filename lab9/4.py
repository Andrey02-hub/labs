# 4.Даний файл дійсних чисел. Замінити в ньому всі елементи на їх квадрати.
import random
lines = [random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500)]
with open('4.txt', 'w+') as file:
    file.writelines("%s\n" % line for line in lines)
    file.writelines("%s\n" % line**2 for line in lines)
    file.close()
