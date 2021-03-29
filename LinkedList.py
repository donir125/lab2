class cell:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, val):
        if self.first is None:
            self.first = self.last = cell(val)
            self.size += 1
        else:
            self.last.next = self.last = cell(val)

    def deleteEl(self, val):
        if self.first.val == val:
            self.first = self.first.next
        else:
            current = self.first
            while current.next.val != val:
                current = current.next
            current.next = current.next.next

    def printList(self):
        current = self.first
        while current is not None:
            print(current.val)
            current = current.next