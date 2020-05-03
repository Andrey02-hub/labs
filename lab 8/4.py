# 4. Описати клас,
# який реалізує десятковий лічильник, який може збільшувати або зменшувати своє значення на одиницю в заданому діапазоні.
# Передбачити ініціалізацію лічильника значеннями за замовчуванням і довільними значеннями.
# Лічильник має два методи: збільшення і зменшення, - і властивість, що дозволяє отримати його поточний стан.
# Написати програму, яка демонструвала б всі можливості класу.
import random
class Recipe():
    def __init__(self, a, b):
        self.a = 1
        self.b = random.randint(0,10)

    def Up(self):
        self.a += 1
        self.b += 1

    def Down(self):
        self.a -= 1
        self.b -= 1

    def Stan(self):
        print(self.a)
        print(self.b)

recipe = Recipe(2, 2)
recipe.Stan()
recipe.Down()
recipe.Stan()
recipe.Up()
recipe.Stan()