class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def checkParamOnStack(str, paramStack):

    if len(str) % 2 != 0:
        return False

    for param in str:
        if param == "(" or param == "[" or param == "{":
            paramStack.push(param)
        # elif param == ")" or param == "]" or param == "}":
        else:
            if paramStack.isEmpty():
                return False
            else:
                paramStack.pop()
    if paramStack.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    paramStack = Stack()

    ipStr = "({(())[]}[])"
    print("Is string balenced:", checkParamOnStack(ipStr, paramStack))
