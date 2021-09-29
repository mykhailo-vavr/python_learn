class Validation:
    @staticmethod
    def isInteger(value):
        if not isinstance(value, int):
            try:
                int(value)
            except:
                raise ValueError("Value should be integer")
        return True

    @staticmethod
    def isInRange(value, a, b = float("inf")):
        if a > b:
            a, b = b, a
        if value < a or value > b:
            raise ValueError("Value should be in range")
        return True

    @staticmethod
    def isAvailableValue(value, arr):
        if not value in arr:
            raise ValueError("Value should be available")
        return True

    @staticmethod
    def isInstance(obj, instance):
        if not isinstance(obj, instance):
            raise TypeError("Invalid instance")
        return True

    @staticmethod
    def isInSpecificFormat(value, countOfLetters, countOfNums):
        letters, nums = value[:countOfLetters], value[countOfLetters:]
        if not letters.isalpha() or not nums.isnumeric():
            raise ValueError("Invalid format")
        return True

    @staticmethod
    def isAlpha(value):
        if not value.isalpha():
            raise ValueError("Is not alpha")
        return True