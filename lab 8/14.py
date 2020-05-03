# 14. Скласти опис класу для вектора, заданого координатами його кінців в тривимірному просторі.
# Забезпечити операції додавання і віднімання векторів з отриманням нового вектора (суми або різниці),
# обчислення скалярного добутку двох векторів, довжини вектора, косинуса кута між векторами.
import math
class Vector:
    def __init__(self, x1 = 3, y1 = 2, z1 = 1, x2 = 5, y2 = 4, z2 = 6, alfa = 60):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.alfa = alfa

    def info(self):
        print("вектор1 = (", self.x1, self.y1, self.z1, ")")
        print("вектор2 = (", self.x2, self.y2, self.z2, ")")

    def summ(self):
        summ =( (self.x1 + self.x2), (self.y1 + self.y2),(self.z1 + self.z2))
        return print("ветор1 + вектор2 =", summ)

    def riz(self):
        riz =( (self.x1 - self.x2), (self.y1 - self.y2),(self.z1 - self.z2))
        return print("ветор1 - вектор2 =", riz)

    def scal(self):
        scal = ((self.x1 * self.x2) + (self.y1 * self.y2) + (self.z1 * self.z2) * math.cos(self.alfa))
        return print("скалярний добуток векторів =", scal)

    def len(self):
        len = math.ceil(math.sqrt(((self.x1 + self.x2)**2) + ((self.y1 + self.y2)**2) + ((self.z1 + self.z2)**2)))
        return print("довжина воктора =", len)
    def angle(self):
        angle = (math.ceil((self.x1 * self.x2) + (self.y1 * self.y2) + (self.z1 * self.z2) * math.cos(self.alfa))) / (math.ceil(math.sqrt(((self.x1 + self.x2)**2) + ((self.y1 + self.y2)**2) + ((self.z1 + self.z2)**2))))
        return print("кут між векторами =", angle)




Vec = Vector()
Vec.info()
Vec.summ()
Vec.riz()
Vec.scal()
Vec.len()
Vec.angle()
