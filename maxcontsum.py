# find the maximum continue sum of the psitive element


def findMaxContSum(arr):
    if(len(arr) == 0):
        return 0
    result = 0
    max_sum = curr_sum = arr[0]

    for num in arr:
        result = result+num

    print("Result is", result)
    for num in arr[1:]:
        curr_sum = max(curr_sum+num, num)
        max_sum = max(curr_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    print(findMaxContSum([1, 2, -1, 3, 4, 10, 10, -10, -1]))
