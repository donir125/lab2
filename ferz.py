import time

start = time.time()
board = [[0 for j in range(8)] for i in range(8)]
def setQueen(i, j):
    for x in range(8):
        board[x][j] += 1
        board[i][x] += 1
        foo = j - i + x
        if 0 <= foo < 8:
            board[x][foo] += 1
        foo = j + i - x
        if 0 <= foo < 8:
            board[x][foo] += 1
    board[i][j] = -1


def resetQueen(i, j):
    for x in range(8):
        board[x][j] -= 1
        board[i][x] -= 1
        foo = j - i + x
        if 0 <= foo < 8:
            board[x][foo] -= 1
        foo = j + i - x
        if 0 <= foo < 8:
            board[x][foo] -= 1
    board[i][j] = 0


def tryQueen(i):
    result = False
    for j in range(8):
        if board[i][j] == 0:
            setQueen(i, j)
            if i == 7:
                result = True
            else:
                result = tryQueen(i + 1)
                if not result:
                    resetQueen(i, j)
        if result:
            break
    return result


tryQueen(0)
for i in range(8):
    for j in range(8):
        if board[i][j] == -1:
            print("1", end="")
        else:
            print("0", end = "")
    print()

finish = time.time()
print(finish - start)