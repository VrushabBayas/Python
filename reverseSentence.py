

def rev_sen(arr):

    word = []
    spaces = [' ']
    length = len(arr)
    i = 0
    while i < length:
        if arr[i] not in spaces:
            word_start = i
            while i < length and arr[i] not in spaces:
                i += 1
            word.append(arr[word_start:i])
        i += 1

    return " ".join(reversed(word))


if __name__ == "__main__":
    print(rev_sen(" Hello Vrushabh How Are you...!"))
