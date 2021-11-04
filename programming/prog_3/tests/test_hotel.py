from unittest import TestCase, main
import sys

sys.path.append('c:\\python_learn_lnu\\programming\\prog_3\\mainClasses')
from hotel import Hotel


class TestHotel(TestCase):
    args = {
        "checkin_datetime": "20.11.2002",
        "checkout_datetime": "21.12.2002",
        "city": "Rome",
        "booking_number": "as123123",
        "guest_name": "Leks",
        "price": 100
    }

    hotel = Hotel(*args.values())

    def test_id_generation(self):
        self.assertNotEqual(self.hotel.get_ID, Hotel().get_ID())

    def test_set_empty_values(self):
        hotel = Hotel()
        hotel.set_empty_values()
        for key in self.args.keys():
            self.assertNotEqual(getattr(hotel, f"get_{key}")(), None)

    def test_get_data_from_keyboard(self):
        self.assertNotEqual(self.hotel.get_data_from_keyboard("data for test"),
                            None)

    def test_getters(self):
        for key, value in self.args.items():
            self.assertEqual(getattr(self.hotel, f"get_{key}")(), value)

    def test_setters(self):
        hotel = Hotel(*self.args.values())
        argsForSetters = {
            "city": "Berlin",
            "booking_number": "EM567567",
            "guest_name": "Eva",
            "price": 999
        }

        for key, value in argsForSetters.items():
            getattr(hotel, f"set_{key}")(value)
        for key, value in argsForSetters.items():
            self.assertEqual(getattr(hotel, f"get_{key}")(), value)

        for key in argsForSetters.keys():
            getattr(hotel, f"set_{key}")(None)
        for key in argsForSetters.keys():
            self.assertNotEqual(getattr(hotel, f"get_{key}")(), None)

    def test_str(self):
        jsonHotel = '''{
  "_Hotel__ID": 0,
  "_Hotel__checkin_datetime": "20.11.2002",
  "_Hotel__checkout_datetime": "21.12.2002",
  "_Hotel__city": "Rome",
  "_Hotel__booking_number": "as123123",
  "_Hotel__guest_name": "Leks",
  "_Hotel__price": 100
}'''
        self.assertEqual(jsonHotel, self.hotel.__str__())

    def test_get_data_from_file(self):
        path = "C:/python_learn_lnu/programming/prog_3/data/testData.json"
        testData = {
            'checkin_datetime': '20.11.2001',
            'checkout_datetime': '22.11.2002',
            'city': 'Rome',
            'booking_number': 'EY345345',
            'guest_name': 'Levi',
            'price': 999
        }

        self.assertRaises(FileExistsError, self.hotel.get_data_from_file,
                          "invalid_path")

        data = self.hotel.get_data_from_file(path)
        self.assertEqual(data, testData)

    def test_set_data_from_file(self):
        hotel = Hotel()
        path = "C:/python_learn_lnu/programming/prog_3/data/testData.json"
        hotel.set_data_from_file(path)

        testData = {
            "checkin_datetime": "20.11.2001",
            "checkout_datetime": "22.11.2002",
            "city": "Rome",
            "booking_number": "EY345345",
            "guest_name": "Levi",
            "price": 999
        }

        self.assertEqual(hotel.set_data_from_file("invalid_path"), -1)
        for key, value in testData.items():
            self.assertEqual(getattr(hotel, f"get_{key}")(), value)


if __name__ == "__main__":
    main()
