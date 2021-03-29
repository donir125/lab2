from random import randint


def binarySearch(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if key > arr[mid]:
            left = mid + 1
        elif key < arr[mid]:
            right = mid - 1
        else:
            return mid
    return "No results"


n = 1000
key = int(input("Введите число для поиска: "))
arr = [randint(-500, 500) for i in range(n)]
arr = sorted(arr)
print(binarySearch(arr, key))
print(arr)
