from random import randint
import time


start = time.time()
class HashTable:
    def __init__(self, size):
        self.size = size + 1
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunc(self, val):
        return val % self.size

    def addEl(self, val, k = 0):
        global savedVal
        if k == 0:
            savedVal = val
            k += 1
        hashVal = self.hashFunc(val)
        if self.slots[hashVal] is None:
            self.slots[hashVal] = hashVal
            self.data[hashVal] = savedVal
        else:
            self.addEl(hashVal + 1, k)

    def getElbyHash(self, val):
        return self.data[val]

    def getPositionByValue(self, val, k = 0):
        global savedVal1
        if k == 0:
            savedVal1 = val
            k += 1
        hashVal = self.hashFunc(val)
        if self.slots[hashVal] is not None:
            if self.data[hashVal] == savedVal1:
                return hashVal
            else:
                return self.getPositionByValue(hashVal + 1, k)
        else:
            return "No Results"

    def delElByHash(self, val):
        self.slots[val] = None
        self.data[val] = None

    def delElByValue(self, val):
        j = 0
        for i in range(len(self.data)):
            if self.data[i] == val:
                self.data[i] = None
                self.slots[i] = None
                j = 1
            if j == 1:
                for k in range(i, len(self.data) - 1):
                    self.data[k] = self.data[k + 1]
                    self.slots[k] = self.slots[k + 1]
                break


hashtable = HashTable(1000)
arr = [randint(-500, 500) for i in range(1000)]
for x in arr:
    hashtable.addEl(x)
print(hashtable.getPositionByValue(119))
print(time.time() - start)