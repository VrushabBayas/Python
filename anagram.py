# program to check wether number is anagram or not

# 1) Normalsolution


def solution1(s1, s2):

    s1 = s1.replace(" ", '').lower()
    s2 = s2.replace(" ", '').lower()

    if len(s1) != len(s2):
        return False
    else:
        return sorted(s1) == sorted(s2)


def solution2(s1, s2):

    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for character in s1:
        count[character] = count.setdefault(character, 0)
        count[character] = count[character]+1
    # print(count)
    for character in s2:
        count[character] = count[character]-1
    # print(count)
    for k in count:
        if count[k] != 0:
            return False

    return True


if __name__ == "__main__":
    print(solution2("I am Vrushab", "Vrushab Am I"))
