# 6. Створити клас, що містить динамічний масив і кількість елементів в ньому.
# Додати конструктор, який виділяє пам'ять під задану кількість елементів, і деструкція.
# Додати методи, що дозволяють заповнювати масив випадковими числами,
# переставляти в даному масиві елементи у випадковому порядку, знаходити кількість різних елементів в масиві,
# виводити масив на екран.

import random
import time

class dinam_array:
    def __init__(self, array):
        self.array = []

    def set_array(self, array):
        self.array = array

    def get_array(self):
        return self.array



ar = dinam_array
ar.array = [i for i in range(random.randint(0, 30))]
time.sleep(3)
print(len(ar.array))
time.sleep(3)
print(ar.array)
time.sleep(2)
print(ar.array[::-1])
time.sleep(3)
sorted(ar.array)
time.sleep(1)
print(ar.array)

