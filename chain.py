import LinkedList
from random import randint


class ChainHash:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [LinkedList.LinkedList() for x in range(self.size)]


    def hashFunc(self, val):
        return val % self.size

    def addEl(self, val):
        hashval = self.hashFunc(val)
        self.slots[hashval] = hashval
        self.data[hashval].add(val)

    def delEl(self, val):
        hashvalue = self.hashFunc(val)
        self.data[hashvalue].deleteEl(val)

    def search(self, val):
        hashval = self.hashFunc(val)
        ans = self.data[hashval].searchEl(val)
        return ans + "with hash - {}".format(hashval)


    def __str__(self):
        s = ""
        k = 0
        for x in self.slots:
            if x is not None:
                current = self.data[x].first
                s += "hash - " + str(x) + ": "
                while current is not None:
                    s += str(current.val) + " "
                    current = current.next
                s += '\n'
            else:
                s += "hash - " + str(k) + ": None"
                s += '\n'
            k += 1
        return s


chainhash = ChainHash(1000)
arr = [randint(-100000, 100000) for i in range(100000)]
for x in arr:
    chainhash.addEl(x)
print(chainhash.search(11119))

