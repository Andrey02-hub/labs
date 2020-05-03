# 4. З множини списків визначити список з максимальною сумою елементів. Списки заповнити випадковими числами.
import random
n = 30
b = random.randint(0,n)

a = [i for i in range(b)]
b = [0,1,6,8,94,7]

z = sum(list(a))
q = sum(list(b))

if z > q:
    print(z)
elif q > z:
    print(q)
