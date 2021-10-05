from validation import Validation

class FuncForOptions:
    def __init__(self, list):
        self.list = list

    @staticmethod
    def getInt(message, isPositive=True):
        print(message)
        value = input()
        Validation.isInteger(value)
        value = int(value)
        if isPositive:
            Validation.isInRange(value, 0)
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