# ip: (1,2,3,2),4 op=(1,3) (2,2)


def findPair(arr, k):
    if len(arr) < 2:
        return False

    seen = set()
    output = set()

    for num in arr:

        target = k-num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    print('\n'.join(map(str, list(output))))


if __name__ == "__main__":
    findPair([1, 2, 3, 2], 4)
