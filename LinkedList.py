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
            if current.next != self.last:
                current.next = current.next.next
            else:
                current.next = None

    def searchEl(self, val):
        current = self.first
        if current is not None:
            if current.val == val:
                return "{} is on 0 position ".format(val)
            else:
                k = 1
                while current.next.val != val:
                    current = current.next
                    k += 1
                    if current.next is None:
                        return "value is not found "
                if current.next.val == val:
                    return "{} is on {} position ".format(val, k)
                else:
                    return "value is not found "
        else:
            return "value is not found "

    def printList(self):
        current = self.first
        while current is not None:
            print(current.val)
            current = current.next