# program to find even number
# print("enter the number:")


# def getEven(no):
#     if (no % 2 == 0):
#         return True
#     else:
#         return False


# no = int(input())

# if getEven(no):
#     print("{0} is Even".format(no))
# else:
#     print("{0} Is odd".format(no))

# -------------------------------------
# program to find percentage

# print("Enter the marks")
# marks = int(input())


# def getPercentage(marks):
#     return (marks/1200)*100


# print("Yo got {0}".format(getPercentage(marks)))
# -----------------------------------------------------

# 3) Accept simgle digit number and print it into the word

# Function to convert number into string
# Switcher is dictionary data type here

# def getWord(no):
#     Switcher = {
#         0: "Zero",
#         1: "one",
#         2: "Two",
#         3: "Three",
#         4: "Four",
#         5: "five",
#         6: "six",
#         7: "seven",
#         8: "eight",
#         9: "Nine",
#         10: "Ten"
#     }
#     return Switcher.get(no, "Only single digit allowed")


# # Driver Program
# if __name__ == "__main__":
#     print("enter single digit:")
#     no = int(input())
#     print (getWord(no))
# =====================================================================================

# write a program to print digit from 1-n

# def printNumberBetweenrange(no):
#     # for i in range(1, no+1):
#     #     print(i)
#     # or eASY WAY
#     print(*range(1, no+1), sep=' ')


# driver program
# if __name__ == "__main__":
#     print("enter the number")
#     no = int(input())
#     printNumberBetweenrange(no)

# ======================================================================================

# accept number from user and print ots table

# def printTable(no):
#     for i in range(1, 11):
#         # print(no, "X", i, "=", i*no, sep=" ")
#         print("{:6d} X {:d}   =  {:6d}".format(no, i, i*no), sep=" ")


# driver program
# if __name__ == "__main__":
#     print("enter the number")
#     no = int(input())
#     printTable(no)
# =====================================================================================

# program to print factore of the number

# def Factor(no):
#     for i in range(2, no+1):
#         if no % i == 0:
#             print("{0}".format(i), sep=" ")


# if __name__ == "__main__":
#     print("enter the number")
#     no = int(input())
#     Factor(no)
# ================================================================================

# Check wether number is Prime or not

# def checkPerfect(no):
#     for i in range(2, no+1):
#         if no % i == 0:
#             break

#     if(no == i):
#         print("{0} is Prime".format(no))
#     else:
#         print("{0} is  not Prime".format(no))


# if __name__ == "__main__":
#     print("enter the number")
#     no = int(input())
#     checkPerfect(no)

# ==============================================================================

# Program to find the Power of the number

# def getPower(n1, n2):
#     power = 1
#     for i in range(1, n2+1):
#         power = n1*power
#     return power


# if __name__ == "__main__":
#     print("enter the number 1:")
#     no = int(input())
#     print("enter the number 2:")
#     no2 = int(input())
#     print(getPower(no, no2))
# ========================================================

# Write a program to find perfect number

# def getPerfectNumber(no):
#     sum = 0
#     for i in range(1, no):
#         if no % i == 0:
#             sum = sum+i
#     if sum == no:
#         return True
#     else:
#         return False


# if __name__ == "__main__":
#     print("enter the number 1:")
#     no = int(input())
#     if getPerfectNumber(no):
#         print("{0} is Perfect number".format(no))
#     else:
#         print("{0} is Not Perfect number".format(no))

# ==========================================================

# display all prime numbers fro the range

# funtion to Check wether number is Prime or not

# def checkPrimeInRange(no1, no2):
#     for num in range(no1, no2+1):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 print(num, sep=" ")


# if __name__ == "__main__":
#     print("enter the number")
#     no1 = int(input())
#     print("enter the number")
#     no2 = int(input())
#     checkPrimeInRange(no1, no2)
# ==========================================================

# Print number in the revers order

# no = int(input())

# for i in range(no, 0, -1):
#     print(i, sep=" ")
#======================================================