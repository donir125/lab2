from random import randint


class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = Tree(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def search(self, val):
        if self.val == val:
            print("Success!", val, "найдено!")
            return self
        else:
            if val < self.val:
                if self.left is not None:
                    return self.left.search(val)
                else:
                    print(val, "not found!")
            elif val > self.val:
                if self.right is not None:
                    return self.right.search(val)
                else:
                    print(val, "not found!")

    def delete(self, obj):
        if self.left.val == obj.val:
            self.left = None
            return
        elif self.right.val == obj.val:
            self.right = None
            return
        return self.delete(obj.left)

    def insertLostValues(self, arr):
        for x in arr:
            Tree.insert(self, x)

    def collectValues(self, obj):
        arr = []
        if obj is not None:
            arr = self.collectValues(obj.left)
            obj.left = None
            arr.append(obj.val)
            arr += self.collectValues(obj.right)
            obj.right = None
        return arr

    def printTree(self):
        if self is not None:
            if self.left is not None:
                print("Root: ", self.val)
                print("L:", self.left.val)
                self.left.printTree()
            if self.right is not None:
                print("Root: ", self.val)
                print("R:", self.right.val)
                self.right.printTree()


# n = 1000
# key = int(input("Введите число для поиска: "))
# arr = [randint(-500, 500) for i in range(n)]
# root = Tree(arr[0])
# for x in arr[1::]:
#     root.insert(x)
# root.search(key)


root = Tree(15)
root.insert(12)
root.insert(9)
root.insert(2)
root.insert(14)
root.insert(21)
root.insert(19)
root.insert(20)
root.insert(30)
root.insert(10)
root.insert(35)
x = root.search(12)
arr = root.collectValues(x)
root.delete(x)
root.insertLostValues(arr)
root.printTree()

