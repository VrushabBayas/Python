class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.push(True)
    s.push("Vrushab Bayas")
    s.push(1)
    print(s.pop())
    print(s.peek())
