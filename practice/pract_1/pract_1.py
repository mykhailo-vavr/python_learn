try:
 n = int(input())
 if n <= 0: raise ValueError()
except:
    print("it should be num > 0")
    exit()

def getCountOfWays(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return getCountOfWays(n - 1) + getCountOfWays(n - 2) + getCountOfWays(n - 3)

print(getCountOfWays(n))

