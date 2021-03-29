from random import randint


def FibonacciSearch(arr, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(arr):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while fibM > 1:
        i = min(index + fibM_minus_2, (len(arr)-1))
        if arr[i] < val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif arr[i] > val:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(arr)-1) and arr[index+1] == val):
        return index+1;
    return -1



key = int(input("Введите элемент для поиска: "))
n = 1000
arr = [randint(-500, 500) for i in range(n)]
arr = sorted(arr)
print(arr)
print(FibonacciSearch(arr, key))
