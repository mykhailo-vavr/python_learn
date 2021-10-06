from datetime import datetime


class Validation:
    dateFormat = "%d.%m.%Y"

    @staticmethod
    def isInteger(value):
        if not isinstance(value, int):
            try:
                int(value)
            except:
                return False
        return True

    @staticmethod
    def isInRange(value, a, b=float("inf")):
        if a > b:
            a, b = b, a
        if value < a or value > b:
            return False
        return True

    @staticmethod
    def isAvailableValue(value, arr):
        if not value in arr:
            return False
        return True

    @staticmethod
    def isInstance(obj, instance):
        if not isinstance(obj, instance):
            return False
        return True

    @staticmethod
    def isInSpecificFormat(value, countOfLetters, countOfNums):
        letters, nums = value[:countOfLetters], value[countOfLetters:]
        if not letters.isalpha() or not nums.isnumeric():
            return False
        return True

    @staticmethod
    def isAlpha(value):
        if not value.isalpha():
            return False
        return True

    @staticmethod
    def isValidDate(date):
        try:
            datetime.strptime(date, Validation.dateFormat)
        except:
            return False
        return True

    @staticmethod
    def isValidDateInterval(startDate, endDate):
        startDate = datetime.strptime(startDate, Validation.dateFormat)
        endDate = datetime.strptime(endDate, Validation.dateFormat)
        return startDate < endDate
