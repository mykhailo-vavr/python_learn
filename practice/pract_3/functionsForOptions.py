from validation import Validation

class FuncForOptions:
    @staticmethod
    def getInt(message, isPositive=True):
        print(message)
        value = input()
        Validation.isInteger(value)
        value = int(value)
        if isPositive:
            Validation.isInRange(value, 0)
        return value

    def f1(self, list):
        count = self.getInt("Count of new items:")
        list.getDataFromKeyboard(count)

    def f2(self, list):
        count = self.getInt("Count of new items:")
        a = self.getInt("First limit:", False)
        b = self.getInt("Second limit:", False)
        list.generateDataInRange(a, b, count)

    def f3(self, list):
        index = self.getInt("Index of elem to insert")
        print("Data to insert")
        data = input()
        list.insert(data, index)

    def f4(self, list):
        index = self.getInt("Index of elem to remove")
        list.remove(index)

    @staticmethod
    def f5(list):
        print(list.getCountOfUniqieElems())

    @staticmethod
    def f6(list):
        list.show()

    @staticmethod
    def f7(*args):
        exit()