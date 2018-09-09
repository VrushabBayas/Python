
class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, item):
        return self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)


if __name__ == "__main__":
    dq = Deque()
    print(dq.isEmpty())
    dq.addFront("Vrushab Bayas")
    dq.addRear(1)
    print(dq.removeRear())
