# Algorithms

sampleList = [65, 2, 54, 4, 94, 4, 1, 8, 21, 12]


def insertionSort(iList):
    print("Insertion sort")
    for i in range(1, len(iList)):
        j = i
        while j > 0 and iList[j] <= iList[j - 1]:
            # if iList[j] is less than iList[j-1], we need to swap
            iList[j], iList[j - 1] = iList[j - 1], iList[j]
            j -= 1

    print(iList)


# insertionSort(sampleList.copy())


def selectionSort(iList):
    print("Selection sort")
    for i in range(0, len(iList)):
        currentVal = i
        currentMin = i
        for j in range(i + 1, len(iList)):
            if iList[currentMin] > iList[j]:
                currentMin = j
        if currentMin != currentVal:
            # swap
            iList[currentMin], iList[currentVal] = iList[currentVal], iList[currentMin]

    print(iList)


# selectionSort(sampleList.copy())


def mergeSort(iList):
    if (len(iList)) <= 1:
        return iList
    mid = len(iList) // 2
    left = iList[:mid]
    right = iList[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(iList1, iList2):
    left, right = 0, 0
    mergedList = []
    if iList1 == None:
        return iList2
    if iList2 == None:
        return iList1
    while left < len(iList1) and right < len(iList2):
        if iList1[left] < iList2[right]:
            mergedList.append(iList1[left])
            left += 1
        else:
            mergedList.append(iList2[right])
            right += 1
    if left > right:
        mergedList.extend(iList2[right:])
    else:
        mergedList.extend(iList1[left:])
    return mergedList


# sortedList = mergeSort(sampleList.copy())
# print(sortedList)


def quickSort(iList, low, high):
    if low < high:
        p = partition(iList, low, high)
        quickSort(iList, low, p - 1)
        quickSort(iList, p + 1, high)


def partition(iList, low, high):
    pivot = iList[high]

    i = low
    for j in range(low, high):
        if iList[j] < pivot:
            if i != j:
                iList[i], iList[j] = iList[j], iList[i]
            i += 1
    iList[high], iList[i] = iList[i], iList[high]
    return i


# qsList = sampleList.copy()
# quickSort(qsList, 0, len(qsList) - 1)
# print(qsList)
