from random import randint


def interSearch(arr, key):
    left = 0
    right = n - 1
    while arr[left] <= key <= arr[right]:
        mid = int(left + (((key - arr[left]) * (right - left)) / (arr[right] - arr[left])))
        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1


n = 1000

arr = [randint(-500, 500) for i in range(n)]
arr = sorted(arr)

key = int(input("Введите элемент для поиска: "))

print(interSearch(arr, key))

print(arr)
