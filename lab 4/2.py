# 2. Дано перший член і знаменник геометричної прогресії.
# Написати рекурсивну функцію знаходження n-го члена прогресії і знаходження суми n перших членів прогресії.
def recur:
    b = int(input("Введіть перший член геометричної прогресії: "))
    q = int(input("Введіть знаменник геометричної прогресії: "))
    n = int(input("Який член потрібно знайти?: "))

    for i in range (n):
        b *= q
    print(b)

recur()
