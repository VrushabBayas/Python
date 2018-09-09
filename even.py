print("enter the number:")


def getEven(no):
    if (no % 2 == 0):
        return True
    else:
        return False


no = int(input())

if getEven(no):
    print("{0} is Even".format(no))
else:
    print("{0} Is odd".format(no))
