

def nRC(str):
    charCount = {}

    for ch in str:
        charCount[ch] = charCount.setdefault(ch, 0)
        charCount[ch] += 1

    for ch in charCount:
        if charCount.get(ch) == 1:
            return True
        else:
            return None


if __name__ == "__main__":
    print(nRC("abc"))
