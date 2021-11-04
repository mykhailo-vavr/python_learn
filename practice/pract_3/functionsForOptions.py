from validation import Validation as V
from patterns.strategy.strategy import DataGetterFromFile, DataGetterFromIterator


class FuncForOptions:
    def __init__(self, list):
        self.list = list

    def getInt(self, message, isPositive=True):
        print(message)

        if isPositive:
            value = self.getPositiveInt(input())
        else:
            value = self._getInt(input())

        if isinstance(value, int):
            return value

        return self.getInt(message, isPositive)

    @V.isIntegerInRange(-1)
    def getPositiveInt(self, value):
        return value

    @V.isIntegerInRange()
    def _getInt(self, value):
        return value

    def f1(self):
        self.list.setDataGetter(DataGetterFromIterator())

    def f2(self):
        self.list.setDataGetter(DataGetterFromFile())

    def f3(self):
        index = self.getInt("Index to insert")
        self.list.setData(index)

    def f4(self):
        index = self.getInt("Index to remove")
        self.list.remove(index)

    def f5(self):
        a = self.getInt("First limit:")
        b = self.getInt("Second limit:")
        self.list.removeInRange(a, b)

    def f6(self):
        print(self.list.getCountOfUniqueElems())

    def f7(self):
        self.list.show()

    def f0(self):
        exit()