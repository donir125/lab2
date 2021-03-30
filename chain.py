import LinkedList

class ChainHash:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [LinkedList.LinkedList() for x in range(self.size)]


    def hashFunc(self, val):
        sum = 0
        if isinstance(val, int):
            for x in str(val):
               sum += int(x)
        elif isinstance(val, str):
            for x in str(val):
                sum += ord(x)
        return sum % self.size

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


chainhash = ChainHash(5)
chainhash.addEl(123)
chainhash.addEl(33)
chainhash.addEl(42)
chainhash.addEl(124)
chainhash.addEl(34)
chainhash.addEl(43)
chainhash.addEl(9)
chainhash.addEl(45)
chainhash.addEl(333)
chainhash.delEl(9)
print(chainhash)
print(chainhash.search(42))

