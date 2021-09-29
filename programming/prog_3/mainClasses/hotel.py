from programming.prog_3.supportClasses.validation import Validation
import json


class Hotel:
    cities = ["Rome", "Berlin", "Nice"]
    ID = 0

    def __init__(self, checkin_datetime=0, checkout_datetime=0,
                 city="Rome", booking_number="xx000000",
                 guest_name="Unknown", price=0):

        self.__ID = Hotel.ID
        Hotel.ID += 1
        self.set_checkin_datetime(checkin_datetime)
        self.set_checkout_datetime(checkout_datetime)
        self.set_city(city)
        self.set_booking_number(booking_number)
        self.set_guest_name(guest_name)
        self.set_price(price)

    def set_checkin_datetime(self, value):
        Validation.isInteger(value)
        Validation.isInRange(value, 0, 31)
        self.__checkin_datetime = value

    def set_checkout_datetime(self, value):
        Validation.isInteger(value)
        Validation.isInRange(value, self.get_checkin_datetime(), 31)
        self.__checkout_datetime = value

    def set_city(self, value):
        Validation.isAvailableValue(value, self.cities)
        self.__city = value

    def set_booking_number(self, value):
        Validation.isInSpecificFormat(value, 2, 6)
        self.__booking_number = value

    def set_guest_name(self, value):
        Validation.isAlpha((value))
        self.__guest_name = value

    def set_price(self, value):
        Validation.isInteger(value)
        Validation.isInRange(value, 0)
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
        print(path)
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
                raise ValueError("Invalid key or value")
