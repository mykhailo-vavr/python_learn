from datetime import datetime
import re


class Validation:
    dateFormat = "%d.%m.%Y"

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
    def isAvailableValue(func):
        def wrapper(self, value, *args):
            if value in self.cities:
                return func(self, value, *args)
            return self.set_valid_data(func, *args)

        return wrapper

    @staticmethod
    def isInstance(obj, instance):
        return isinstance(obj, instance)

    @staticmethod
    def isInSpecificFormat(regexp):
        def _isInSpecificFormat(func):
            def wrapper(self, value, *args):
                if re.search(regexp, value):
                    return func(self, value, *args)
                return self.set_valid_data(func, *args)

            return wrapper

        return _isInSpecificFormat

    @staticmethod
    def isValidDate(func):
        def wrapper(self, date, *args):
            try:
                datetime.strptime(date, Validation.dateFormat)
            except:
                return self.set_valid_data(func, *args)

            startDate = self.get_checkin_datetime()
            endDate = self.get_checkout_datetime()

            if startDate == None and endDate == None:
                return func(self, date)

            if startDate == None:
                startDate = date
            else:
                endDate = date

            startDate = datetime.strptime(startDate, Validation.dateFormat)
            endDate = datetime.strptime(endDate, Validation.dateFormat)

            if startDate < endDate:
                return func(self, date)
            return self.set_valid_data(func, *args)

        return wrapper
