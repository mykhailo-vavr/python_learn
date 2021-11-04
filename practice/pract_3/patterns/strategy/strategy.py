from validation import Validation as V
from abc import ABC, abstractmethod
import json
from random import randint


class DataGetter(ABC):
    @abstractmethod
    def getData(self):
        pass

    def getInt(self, message, isPositive=True):
        print(message)

        if isPositive:
            value = self.getPositiveInt(input())
        else:
            value = self._getInt(input())

        if isinstance(value, int):
            return value

        return self.getInt(message, isPositive)

    @V.isIntegerInRange(0)
    def getPositiveInt(self, value):
        return value

    @V.isIntegerInRange()
    def _getInt(self, value):
        return value

    def getPath(self):
        print("Print path to file")
        return input()


class DataGetterFromFile(DataGetter):
    def getData(self):
        path = self.getPath()

        try:
            with open(path) as file:
                data = json.load(file)
        except:
            return print("Error on file reading")
        return data["items"]


class DataGetterFromIterator(DataGetter):
    def getData(self):
        count = self.getInt("Count of new items:")
        a = self.getInt("First limit:", False)
        b = self.getInt("Second limit:", False)
        generator = self.generateDataInRange(count, a, b)
        data = []
        for i in range(count):
            data.append(next(generator))
        return data

    @V.isIntegerInRange(0)
    def generateDataInRange(self, count, a, b):
        if a > b:
            a, b = b, a
        for i in range(count):
            yield randint(a, b)
