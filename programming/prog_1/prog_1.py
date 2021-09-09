def isNum(n):
	try:
		int(n)
	except:
		print("Value should be num")
		exit()

def isPositive(n):
	return n >= 0

def getArray():
	n = input()
	isNum(n)
	n = int(n)
	try:
		if not isPositive(n):
			raise ValueError()
	except:
		print("Value should be >= 0")
		exit()

	array = []
	for num in range(n):
		num = input()
		isNum(n)
		num = int(num)
		array.append(num)

	return array

def isSorted(arr):
	return sorted(arr) == arr or \
			sorted(arr, reverse = True) == arr

def removeItems(arr):
	i = 1
	for item in arr:
		if i % 4 == 0:
			arr.remove(item)
			i += 1
		i += 1
	return arr

def show(arr):
	for item in arr:
		print(item)

array = getArray()
show(array)
print("\n")

if (not isSorted(array)):
	array = removeItems(array)
show(array)
