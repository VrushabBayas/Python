
def findCommon(arr1, arr2):
    newarr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            newarr.append(arr1[i])
            i += 1
            j += 1
        elif(arr1[i] > arr2[j]):
            j += 1
        else:
            i += 1
    return newarr


if __name__ == "__main__":
    print(findCommon([1, 2, 3, 5, 4], [1, 4, 5, 8, 9]))
