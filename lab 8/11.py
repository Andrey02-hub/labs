# 11. Скласти опис класу прямокутників зі сторонами, паралельними осям координат.
# Передбачити можливість переміщення прямокутників на площині, зміна розмірів,побудова найменшого прямокутника,
# що містить два заданих прямокутника, і прямокутника, що є спільною частиною (перетином) двох прямокутників.

class Rectangle:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = 2
        self.x2 = 3
        self.y1 = 3
        self.y2 = 2

    def move_rect(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def change_size(self, dx, dy):
        self.x2 += dx
        self.y2 += dy

    def find_least_fence(self, rect2):
        fence = Rectangle(0, 0, 0, 0)
        if self.x1 < rect2.x1:
            fence.x1 = self.x1
            fence.x2 = rect2.x2
        elif self.x1 == rect2.x1:
            fence.x1 = self.x1
            if self.x2 > rect2.x2:
                fence.x2 = self.x2
            else:
                fence.x2 = rect2.x2
        else:
            fence.x1 = rect2.x1
            fence.x2 = self.x2
        if self.y1 < rect2.y1:
            fence.y1 = rect2.y1
            fence.y2 = self.y2
        elif self.y1 == rect2.y1:
            fence.y1 = self.y1
            if self.y2 > rect2.y2:
                fence.y2 = self.y2
            else:
                fence.y2 = rect2.y2
        else:
            fence.y1 = rect2.y1
            fence.y2 = self.y2
        return fence



