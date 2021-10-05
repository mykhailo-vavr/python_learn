class Validation:
    @staticmethod
    def isInteger(value):
        if not isinstance(value, int):
            try:
                int(value)
            except:
                return False
        return True

    @staticmethod
    def isInRange(value, a, b = float("inf")):
        if a > b:
            a, b = b, a
        if value < a or value > b:
            return False
        return True
