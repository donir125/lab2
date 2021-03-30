def func():
    i = 0
    j = 0
    arr = [[0] * 8 for i in range(8)]
    arr[0][0] = 1
    while i + 1 < 8 and j + 2 < 8:
        i += 1
        j += 2
        arr[i][j] = 1
    j = -1

    while i + 1 < 8 and j + 2 < 8:
        i += 1
        j += 2
        arr[i][j] = 1


    return arr


arr = func()
for i in range(8):
    print(arr[i])