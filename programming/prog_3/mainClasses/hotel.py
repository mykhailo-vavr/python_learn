import sys

sys.path.append('c:\\python_learn_lnu\\programming\\prog_3\\')

from supportClasses.validation import Validation as V
import json


class Hotel:
    cities = ["Rome", "Berlin", "Nice"]
    ID = 0

    def __init__(self,
                 checkin_datetime=None,
                 checkout_datetime=None,
                 city=None,
                 booking_number=None,
                 guest_name=None,
                 price=None):

        self.__ID = Hotel.ID
        Hotel.ID += 1
        self.__checkin_datetime = checkin_datetime
        self.__checkout_datetime = checkout_datetime
        self.__city = city
        self.__booking_number = booking_number
        self.__guest_name = guest_name
        self.__price = price

    def set_empty_values(self):
        for key, value in vars(self).items():
            if value == None:
                getattr(self, f"set_{key[8:]}")(None)

    def set_valid_data(self, set_func):
        value = self.get_data_from_keyboard(
            f"{set_func.__name__} (id:{self.get_ID()})")
        getattr(self, f"{set_func.__name__}")(value)

    def get_data_from_keyboard(self, message):
        print(f"Incorrect {message}")
        return input()

    @V.isValidDate
    def set_checkin_datetime(self, value):
        self.__checkin_datetime = value

    @V.isValidDate
    def set_checkout_datetime(self, value):
        self.__checkout_datetime = value

    @V.isAvailableValue
    def set_city(self, value):
        self.__city = value

    @V.isInSpecificFormat(r'^[a-zA-Z]{2}\d{6}$')
    def set_booking_number(self, value):
        self.__booking_number = value

    @V.isInSpecificFormat(r'^[a-zA-Z]{2,}$')
    def set_guest_name(self, value):
        self.__guest_name = value

    @V.isIntegerInRange(0)
    def set_price(self, value):
        self.__price = value

    def get_ID(self):
        return self.__ID

    def get_checkin_datetime(self):
        return self.__checkin_datetime

    def get_checkout_datetime(self):
        return self.__checkout_datetime

    def get_city(self):
        return self.__city

    def get_booking_number(self):
        return self.__booking_number

    def get_guest_name(self):
        return self.__guest_name

    def get_price(self):
        return self.__price

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
