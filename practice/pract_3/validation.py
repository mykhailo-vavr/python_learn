class Validation:
    def isIntegerInRange(a=float("-inf"), b=float("inf")):
        def _isIntegerInRange(func):
            def wrapper(self, value, *args):
                if not isinstance(value, int):
                    try:
                        int(value)
                    except:
                        return print(f"Incorrect value in {func.__name__}")

                value = int(value)

                if a < value and value < b:
                    return func(self, value, *args)
                return print(f"Incorrect value in {func.__name__}")

            return wrapper

        return _isIntegerInRange