# 9. Побудувати три класи (базовий і 3 нащадка), що описують деяких хижих тварин (один з нащадків), всеїдних (другий нащадок) і травоїдних (третій нащадок).
# Описати в базовому класі абстрактний метод для розрахунку кількості та типу їжі, необхідної для прожитку тварини в зоопарку.
#    a) Упорядкувати всю послідовність тварин по спадаючій кількості їжі. При збігу значень - впорядковувати дані за алфавітом по імені.
#    Вивести ідентифікатор тварини, ім'я, тип і кількість споживаної їжі для всіх елементів списку.
#    b) Вивести перші 5 імен тварин з отриманого в пункті а) списку.
#    c) Вивести останні 3 ідентифікатора тварин з отриманого в пункті а) списку.
#    d) Організувати запис і читання колекції в та з файлу.
#    e) Організувати обробку некоректного формату вхідного файлу.

class Animals:
    def __init__(self, Predator_food = 1, Omnivorous_food = 1, Herbivorous_food = 1):
        self.Predator_food = Predator_food
        self.Omnivorous_food = Omnivorous_food
        self.Herbivorous_food = Herbivorous_food

    def food(self):
        Predator_food = self.Predator_food * 20
        return print('хижаку потрібно',  Predator_food,  "кілограмів мяса")
    def food2(self):
        Omnivorous_food = self.Omnivorous_food * 15
        return print('всеїдному потрібно', Omnivorous_food, "кілограмів їжї")

    def food3(self):
        Herbivorous_food = self.Herbivorous_food * 40
        return print('травоїдному потрібно', Herbivorous_food, "кілограмів трави")




        

class Predator(Animals):
    def __init__(self):
        Animals.__init__(self)


class Omnivorous(Animals):
    def __init__(self):
        Animals.__init__(self)

class Herbivorous(Animals):
    def __init__(self):
        Animals.__init__(self)

if __name__ == '__main__':
    Anim = Animals()
    Anim.food()
    Anim.food2()
    Anim.food3()