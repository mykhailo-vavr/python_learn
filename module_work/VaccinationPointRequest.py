import json
from Validation import Validation as V
from datetime import time


class VaccinationPointRequest():
    ID = 0

    def __init__(self, point=None, time=None, date=None, name=None):
        self.__ID = VaccinationPointRequest.ID
        VaccinationPointRequest.ID += 1
        self.point = point
        self.time = time
        self.date = date
        self.name = name

    def set_empty_values(self):
        for key, value in vars(self).items():
            print(value == None)
            if value == None:
                getattr(self, f"set_{key}")(None)

    def set_valid_data(self, set_func):
        value = self.get_data_from_keyboard(
            f"{set_func.__name__} (id:{self.get_ID()})")
        getattr(self, f"{set_func.__name__}")(value)

    def get_data_from_keyboard(self, message):
        print(f"Incorrect {message}")
        return input()

    @V.isInSpecificFormat(r'^[a-zA-Z0-9]{2,}$')
    def set_point(self, value):
        self.point = value

    @V.isInSpecificFormat(r'^10|1[2345678].[024]0$')
    def set_time(self, value):
        self.time = value

    @V.isValidDate
    def set_date(self, value):
        self.date = value

    @V.isInSpecificFormat(r'^[a-zA-Z]{2,}$')
    def set_name(self, value):
        self.name = value

    def get_ID(self):
        return self.ID

    def get_point(self):
        return self.point

    def get_time(self):
        return self.time

    def get_date(self):
        return self.date

    def get_name(self):
        return self.ID

    def __str__(self):
        return json.dumps(vars(self), indent=2)

    def get_data_from_file(self, path):
        try:
            with open(path) as file:
                data = json.load(file)
        except:
            return -1
        return data

    def set_data_from_file(self, path):
        data = self.get_data_from_file(path)
        if data == -1:
            print("Invalid path")
            return -1
        for key, value in data.items():
            try:
                getattr(self, f"set_{key}")(value)
            except:
                print("Error: Invalid key or value")
                return -1
        self.set_empty_values()
