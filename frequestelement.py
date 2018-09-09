

def mostFreqEle(arr):

    count = {}
    max_count = -1
    for num in arr:
        count[num] = count.setdefault(num, 0)
        count[num] += 1
        if count[num] > max_count:
            max_count = count[num]
            max_count_item = num

    return {max_count_item: max_count}


if __name__ == "__main__":
    print(mostFreqEle([1, 2, 5, 4, 2, 8, 2, 9, 2, 3, 1, 5, 1, 2]))
