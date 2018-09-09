print("Enter the marks")
marks = int(input())


def getPercentage(marks):
    return (marks/1200)*100


print("Yo got {0}".format(getPercentage(marks)))
