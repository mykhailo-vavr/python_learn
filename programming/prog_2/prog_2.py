def isNum(n):
    try:
        int(n)
    except:
        print("Value should be integer")
        exit()


def isPositive(n):
    return n >= 0


def getMatrix():
    print("Enter the dimension of the matrix")
    n = input()

    isNum(n)
    n = int(n)

    try:
        if not isPositive(n):
            raise ValueError()
    except:
        print("Value should be >= 0")
        exit()

    A = []
    for i in range(n):
        row = []
        for j in range(n):
            num = input()
            isNum(num)
            num = int(num)
            row.append(num)
        A.append(row)

    return A


def getMinNumFromMaxCol(A):
    sum = 0
    minNum = A[0][0]

    for i in range(len(A)):
        tempSum = 0
        tempMinNum = A[0][i]
        for j in range(len(A)):
            tempMinNum = min(A[j][i], tempMinNum)
            tempSum += abs(A[j][i])
        if tempSum > sum:
            sum = tempSum
            minNum = tempMinNum

    return minNum


def showMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


A = getMatrix()
showMatrix(A)
print("\n")

minNum = getMinNumFromMaxCol(A)
print(minNum)
