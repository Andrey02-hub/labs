#2. На шахівниці NxN в клітинці (x1, y1) стоїть голодний шаховий кінь.
# Він хоче потрапити в клітинку (x2, y2), де росте смачна шахова трава.
# Яку найменшу кількість ходів він повинен для цього зробити?
# Вхідні дані
# На вхід програми поступає п'ять чисел: N, x1, y1, x2, y2 (5 ≤ N ≤ 20, 1 ≤ x1, y1, x2, y2 ≤ N).
# Ліва верхня клітинка дошки має координати (1, 1), права нижня - (N, N).
# Вихідні дані
# У першому рядку виведіть єдине число K - найменшу необхідну кількість ходів коня.
# У кожному з наступних K + 1 рядків має бути записано 2 числа - координати чергової клітинки в шляху коня.
import random

N = random.randint(5,20)
x1 = random.randint(5,N)
y1 = random.randint(5,N)
x2 = random.randint(5,N)
y2 = (N - random.randint(1,N))


SIDE = random.randint(5,20)
MOVES = [(1, 2), (-1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]

board = [[0 for x in range(SIDE)] for y in range(SIDE)]


def test_move(row, col):
    return (0 <= row < SIDE) and (0 <= col < SIDE) and (board[row][col] == 0)


def find_path(firstMove=(0, 0, 1)):
    movesCollection = [(firstMove, [(firstMove[0] + m[0], firstMove[1] + m[1], firstMove[2] + 1) for m in MOVES if
                                    test_move(firstMove[0] + m[0], firstMove[1] + m[1])])]
    board[firstMove[0]][firstMove[1]] = firstMove[2]

    while len(movesCollection) > 0:
        topMoves = movesCollection[-1][1]
        if len(topMoves) == 0:
            lastMove = movesCollection[-1][0]
            board[lastMove[0]][lastMove[1]] = 0
            movesCollection.pop()
        else:
            lastMove = topMoves.pop()
            board[lastMove[0]][lastMove[1]] = lastMove[2]
            if lastMove[2] == (SIDE * SIDE):
                return True
            nextMoves = [(lastMove[0] + m[0], lastMove[1] + m[1], lastMove[2] + 1) for m in MOVES if
                         test_move(lastMove[0] + m[0], lastMove[1] + m[1])]
            if len(nextMoves) == 0:
                board[lastMove[0]][lastMove[1]] = 0
            else:
                movesCollection.append((lastMove, nextMoves))

    return False


def dump_board():
    for i in range(SIDE):
        for j in range(SIDE):
            print("%02d" % board[i][j], end=' ')
        print()


print("OK" if find_path() else "FAIL")
dump_board()
