from programming.prog_3.supportClasses.validation import Validation as V
import json
import datetime


class Hotel:
    cities = ["Rome", "Berlin", "Nice"]
    ID = 0

    def __init__(self, checkin_datetime=None, checkout_datetime=None,
                 city=None, booking_number=None,
                 guest_name=None, price=None):

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
                getattr(self, f"set_{key[8:]}")("-1")

    def check_date_interval(self, startDate, endDate):
        if startDate == None \
                or endDate == None:
            return True

        return V.isValidDateInterval(startDate, endDate)

    def get_data_from_keyboard(self, message):
        print(f"Write correct {message}")
        return input()

    def set_checkin_datetime(self, value):
        if not V.isValidDate(value) or not self.check_date_interval(value, self.__checkout_datetime):
            value = self.get_data_from_keyboard(f"checkin_datetime (id:{self.get_ID()})")
            self.set_checkin_datetime(value)
        self.__checkin_datetime = value

    def set_checkout_datetime(self, value):
        if not V.isValidDate(value) or not self.check_date_interval(self.__checkin_datetime, value):
            value = self.get_data_from_keyboard(f"checkout_datetime (id:{self.get_ID()})")
            self.set_checkout_datetime(value)
        self.__checkout_datetime = value

    def set_city(self, value):
        if not V.isAvailableValue(value, self.cities):
            value = self.get_data_from_keyboard(f"city (id:{self.get_ID()})")
            self.set_city(value)
        self.__city = value

    def set_booking_number(self, value):
        if not V.isInSpecificFormat(value, 2, 6):
            value = self.get_data_from_keyboard(f"booking_number (id:{self.get_ID()})")
            self.set_booking_number(value)
        self.__booking_number = value

    def set_guest_name(self, value):
        if not V.isAlpha((value)):
            value = self.get_data_from_keyboard(f"guest_name (id:{self.get_ID()})")
            self.set_guest_name(value)

        self.__guest_name = value

    def set_price(self, value):
        if not V.isInteger(value):
            value = self.get_data_from_keyboard(f"price (id:{self.get_ID()})")
            self.set_price(value)

        value = int(value)

        if not V.isInRange(value, 0):
            value = self.get_data_from_keyboard(f"price (id:{self.get_ID()})")
            self.set_price(value)

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
            raise FileExistsError("Error on file reading")
        return data

    def set_data_from_file(self, path):
        data = self.get_data_from_file(path)
        for key, value in data.items():
            try:
                getattr(self, f"set_{key}")(value)
            except:
                print("Error: Invalid key or value")
                return
        self.set_empty_values()
