# Chapter 1 - Cracking The Coding Interview

# 1.1


def hasAllUniqueCharacters(myString):
    myMap = {}
    for character in myString:
        if (character in myMap):
            return False
        myMap[character] = 0

    return True


# print(hasAllUniqueCharacters("hello"))                          # False
# print(hasAllUniqueCharacters("abcdefghijlmnopqrstuvwxyz"))      # True
# print(hasAllUniqueCharacters("maybe next time"))                # False

# 1.2 is C/C++ specific - skipping

# 1.3


def arePermutationsOfEachOther(s1, s2):
    if (len(s1) != len(s2)):
        return False

    myMap = {}
    for character in s1:
        if (character in myMap):
            myMap[character] += 1
        else:
            myMap[character] = 1
    for character in s2:
        if (character not in myMap):
            return False
        else:

            if (myMap[character] == 0):
                return False
            myMap[character] -= 1

    return sum(myMap.values()) == 0


# print(arePermutationsOfEachOther("hello", "olleh"))     # True
# print(arePermutationsOfEachOther("turtle", "cattle"))   # False
# print(arePermutationsOfEachOther("billy", "libby"))     # False
# print(arePermutationsOfEachOther("dylan", "ynald"))     # True

# 1.5
def stringCompression(originalString):
    charArray = []
    i = 0
    while i < len(originalString):
        myChar = originalString[i]
        count = 1
        j = i + 1
        while j < len(originalString) and originalString[j] == myChar:
            count += 1
            j += 1

        i = j
        charArray.append("%s%d" % (myChar, count))

    return "".join(charArray)


# print(stringCompression("aabcccccaa"))
