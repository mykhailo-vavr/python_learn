from validation import Validation as V


class FuncForOptions:
    def __init__(self, list):
        self.list = list

    @staticmethod
    def getInt(message, isPositive=True):
        print(message)
        value = input()

        if not V.isInteger(value):
            print("Invalid data")
            return FuncForOptions.getInt(message, isPositive)

        value = int(value)
        if isPositive:
            if not V.isInRange(value, 0):
                print("Invalid data")
                return FuncForOptions.getInt(message, isPositive)
        return value

    def f1(self):
        count = self.getInt("Count of new items:")
        self.list.getDataFromKeyboard(count)

    def f2(self):
        count = self.getInt("Count of new items:")
        a = self.getInt("First limit:", False)
        b = self.getInt("Second limit:", False)
        self.list.generateDataInRange(a, b, count)

    def f3(self):
        index = self.getInt("Index of elem to insert")
        print("Data to insert")
        data = input()
        self.list.insert(data, index)

    def f4(self):
        index = self.getInt("Index of elem to remove")
        self.list.remove(index)

    def f5(self):
        print(self.list.getCountOfUniqieElems())

    def f6(self):
        self.list.show()

    def f7(self):
        exit()

    def f8(self):
        count = self.getInt("Count of new items:")
        generator = self.list.getDataFromKeyboardGenerator(count)
        for i in range(count):
            self.list.push(next(generator))

    def f9(self):
        count = self.getInt("Count of new items:")
        a = self.getInt("First limit:", False)
        b = self.getInt("Second limit:", False)
        generator = self.list.generateDataInRangeGenerator(a, b, count)
        for i in range(count):
            self.list.push(next(generator))
