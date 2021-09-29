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
