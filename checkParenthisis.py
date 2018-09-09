

def chekPran(str):

    opening = set('({[')
    matches = set([('(', ')'), ('{', '}'), ('[', ']')])

    Stack = []

    if len(str) % 2 != 0:
        return False

    for paran in str:
        if paran in opening:
            Stack.append(paran)
        else:
            if len(Stack) == 0:
                return False
            last_open = Stack.pop()

            if (last_open, paran) not in matches:
                return False

    return len(Stack) == 0


if __name__ == "__main__":
    ipStr = "({(())[]}[])"
    print(chekPran(ipStr))
