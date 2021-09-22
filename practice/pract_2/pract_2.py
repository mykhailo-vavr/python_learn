import numpy as np


def isInt(n):
    try:
        int(n)
    except:
        return False
    return True


def getNum(message = "", isPositive=False):
    if message:
        print(message)

    num = input()

    if not isInt(num):
        print("Incorrect data")
        return getNum(message, isPositive)
    elif int(num) <= 0 and isPositive:
        print("Incorrect data")
        return getNum(message, isPositive)

    return int(num)


def getArrayFromUser():
    n = getNum("Write the size of array", True)
    arr = []

    for i in range(n):
        arr.append(getNum())

    return arr


def getArrayInRange():
    n = getNum("Write the size of array", True)
    a = getNum("Write first limit")
    b = getNum("Write second limit")

    if a > b:
        a, b = b, a

    return np.random.randint(a, b, n)


def toMerge(arr, begin, end):
    mid = begin + (end - begin) // 2
    i = begin
    j = mid + 1
    tempArr = []

    global countOfComparisons

    while i <= mid and j <= end:
        countOfComparisons += 1
        if arr[i] <= arr[j]:
            tempArr.append(arr[i])
            i += 1
        else:
            tempArr.append(arr[j])
            j += 1

    while i <= mid:
        tempArr.append(arr[i])
        i += 1

    while j <= end:
        tempArr.append(arr[j])
        j += 1

    for i in range(len(tempArr)):
        arr[begin + i] = tempArr[i]


def mergeSort(arr, left, right):
    global countOfComparisons
    countOfComparisons += 1
    if left < right:
        if right - left == 1:
            if arr[right] < arr[left]:
                arr[left], arr[right] = arr[right], arr[left]
        else:
            mergeSort(arr, left, left + (right - left) // 2)
            mergeSort(arr, left + (right - left) // 2 + 1, right)
            toMerge(arr, left, right)


def start():
    print("Choose the option:\n\
          1. Enter an array on your own\n\
          2. Generate an array in range [a, b]\n\
          3. Exit")

    option = input()
    arr = []

    if option == "1":
        arr = getArrayFromUser()
    elif option == "2":
        arr = getArrayInRange()
    elif option == "3":
        exit()
    else:
        print("Choose correct option")
        start()

    print(arr)
    mergeSort(arr, 0, len(arr) - 1)
    print(arr)
    print(countOfComparisons)
    start()


countOfComparisons = 0
start()
