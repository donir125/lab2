from random import choice

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunc(self, val):
        sum = 0
        if isinstance(val, int):
            for x in str(val):
               sum += int(x)
        elif isinstance(val, str):
            for x in str(val):
                sum += ord(x)
        return (sum + choice(arr)) % self.size

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
        for i in range(len(self.data)):
            if self.data[i] == val:
                self.data[i] = None
                self.slots[i] = None

global arr
arr = [i for i in range(1, 26)]
hashtable = HashTable(25)
hashtable.addEl(123)
hashtable.addEl(33)
hashtable.addEl(222)
hashtable.addEl(111111)
hashtable.addEl(141)
hashtable.addEl(132)
hashtable.addEl(1245)
hashtable.addEl(876)
hashtable.addEl(432627)
hashtable.addEl(3570)
hashtable.addEl(347307)
hashtable.addEl(1256721)
hashtable.addEl("216132")
hashtable.addEl("dsfgy")
print(hashtable.__dict__)

