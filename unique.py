

def checkUnique(str):
    print(set(str))
    return len(set(str)) == len(str)


if __name__ == "__main__":
    print(checkUnique("abcdefga"))
