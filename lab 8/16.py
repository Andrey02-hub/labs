# 16. Створити абстрактний клас Figure з методами обчислення площі та периметра,
# а також методом, що виводить інформацію про фігуру на екран.
# Створити похідні класи: Rectangle (прямокутник), Circle (коло), Triangle (трикутник) зі своїми методами обчислення площі і періметра.
# Создать масив n фігур і вивести повну інформацію про фігури на екран
import math
import random
class Figure():
    def __init__(self, perimeter=None, square=None):
        self.perimeter = perimeter
        self.square = square
        self.infoFig = []

    def calcPerimeter(self):
        pass

    def calcSquare(self):
        pass

    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSquare()
        print('периметр = %p площадь = %s' % (p, s))


class Rectangle(Figure):
    def __init__(self, x, y, w, h):
        Figure.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def calcPerimeter(self):
        perimeter = self.w * 2 + self.h * 2
        return perimeter

    def calcSquare(self):
        square = self.x * self.y
        return square

    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSquare()
        print('У прямоугольника периметр = %s площадь = %s' % (p, s))

class Circle(Figure):
    def __init__(self, x, y, r, d):
        Figure.__init__(self)
        self.x = x
        self.y = y
        self.r = r
        self.d = 2*r

    def calcPerimeter(self):
        perimeter = math.pi * self.d
        return perimeter

    def calcSquare(self):
        square =  math.pi * (self.r ** 2)
        return square

    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSquare()
        print('У круга периметр = %s площадь = %s' % (p, s))

class Triangle(Figure):
    def __init__(self, a, b, c):
        Figure.__init__(self)

        self.a = a
        self.b = b
        self.c = c

    def calcPerimeter(self):
        perimeter = (self.a + self.b + self.c) / 2
        return perimeter

    def calcSquare(self):
        p = (self.a + self.b + self.c) / 2
        square = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return square

    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSquare()
        print('У трикутника периметр = %s площадь = %s' % (p, s))


if __name__ == '__main__':
        # прямокутник
    fig1 = Rectangle(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
    fig2 = Rectangle(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
    array = [fig1, fig2]
    for f in array:
        f.figInfo()
        # круг
    fig3 = Circle(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
    fig4 = Circle(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
    array = [fig3, fig4]
    for C in array:
        C.figInfo()
        # трикутник
        # площадь треугольника вычисляется по формуле с квадратным крнем, когда число меньше 0, программа выдает ошибку
    fig5 = Triangle(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
    fig6 = Triangle(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
    array = [fig5, fig6]
    for z in array:
        z.figInfo()

