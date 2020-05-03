# 9. Дано два файли одного і того ж типу.
# Додати до першого файлу вміст другого файлу, а до другого файлу - вміст першого.
import shutil
import random
lines = [random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500)]
with open('a.txt', 'r+') as file:
    file.writelines("%s\n" % line for line in lines)
    file.close()


with open('b.txt', 'r+') as file:
    file.writelines("%s\n" % line**2 for line in lines)
    file.close()

a = open('a.txt', 'r+')
a1 = a.read()
b = open('b.txt', 'r+')
b1 = b.read()
a.write(b1)
b.write(a1)