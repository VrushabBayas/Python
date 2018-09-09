# ip=[1,5,2,9],[8,9,5,1] op=1

import collections

# first solution


def findMissing(arr1, arr2):

    if len(arr1) != len(arr2):
        return False

    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

# Second solution


def findMissing2(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

# extra ordinary solution useing xor


def xorSolution(arr1, arr2):
    result = 0
    print(arr1+arr2)
    for num in arr1+arr2:
        result ^= num
        # print(result)
    return result


if __name__ == "__main__":
    print(xorSolution([2, 5, 5, 7, 9], [7, 9, 8, 2, 5]))
