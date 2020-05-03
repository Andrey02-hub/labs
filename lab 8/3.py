# 3. Створити клас з двома змінними. Додати функцію виведення на екран і функцію зміни цих змінних.
# Додати функцію, яка знаходить суму значень цих змінних, і функцію яка знаходить найбільше значення з цих двох змінних.
import random
class Numb:
    def __init__(self, a, b):
        self.a = 1
        self.b = 1

    def vivod(self):
        print(self.a, self.b)

    def change(self):
        self.a += random.randint(0, 10)
        print(self.a)
        self.b += random.randint(0, 10)
        print(self.b)

    def summ(self):
        c = self.a + self.b
        print()

    def max(self):
        if self.a > self.b:
            maxx = self.a
        elif self.b > self.a:
            maxx = self.b
        print(maxx)
