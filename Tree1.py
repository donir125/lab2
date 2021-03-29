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

    def printTree(self):
        if self is not None:
            if self.left is not None:
                self.left.printTree()
            print(self.val)
            if self.right is not None:
                self.right.printTree()


root = Tree(15)
root.insert(12)
root.insert(18)
root.insert(21)
root.printTree()
