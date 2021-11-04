import re
from datetime import datetime


class Validation:
    @staticmethod
    def isInSpecificFormat(regexp):
        def _isInSpecificFormat(func):
            def wrapper(self, value, *args):
                if isinstance(value, str) and re.search(regexp, value):
                    return func(self, value, *args)
                return self.set_valid_data(func, *args)

            return wrapper

        return _isInSpecificFormat

    @staticmethod
    def isIntegerInRange(a, b=float("inf")):
        def _isIntegerInRange(func):
            def wrapper(self, value, *args):
                if not isinstance(value, int):
                    try:
                        int(value)
                    except:
                        return self.set_valid_data(func, *args)

                value = int(value)

                if a < value and value < b:
                    return func(self, value, *args)
                return self.set_valid_data(func, *args)

            return wrapper

        return _isIntegerInRange

    @staticmethod
    def isValidDate(func):
        def wrapper(self, date, *args):
            dateFormat = "%d.%m.%Y"

            try:
                datetime.strptime(date, dateFormat)
            except:
                return self.set_valid_data(func, *args)

            return func(self, date)

        return wrapper