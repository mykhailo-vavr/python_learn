def isNum(n):
    try:
        int(n)
    except:
        return False
    n = int(n)
    return isinstance(n, int)


def isPositive(n):
    return n >= 0


def getMatrix():
    print("Enter the dimension of the matrix")

    n = input()
    while not isNum(n):
        print("Incorrect value")
        n = input()
    n = int(n)

    if not isPositive(n):
        print("Value should be >= 0")
        getMatrix()

    A = []
    for i in range(n):
        row = []
        for j in range(n):
            num = input()
            while not isNum(num):
                print("Incorrect value")
                num = input()
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


def options(option):
    return {
        "1": getMinNumFromMaxCol,
        "2": showMatrix,
        "3": exit
    }.get(option)


def start(matrix):
    print("""Choose the option:
        1. Get min num from max col
        2. Show matrix
        3. Exit""")

    option = input()
    method = options(option)

    if method:
        method(matrix)
    else:
        print("Choose correct option")
        start(matrix)
    start(matrix)


matrix = getMatrix()
start(matrix)
