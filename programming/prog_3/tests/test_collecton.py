from unittest import TestCase, main
import sys

sys.path.append('c:\\python_learn_lnu\\programming\\prog_3')
from supportClasses.collection import Collection
from mainClasses.hotel import Hotel
from patterns.memento.memento import Memento


class TestCollection(TestCase):
    path = "C:/python_learn_lnu/programming/prog_3/data/data.json"
    invalid_path = "invalid_path"
    collection = Collection(Hotel, path)

    def test_find(self):
        self.assertEqual(self.collection.find("Jean")[0], self.collection[0])
        self.assertEqual(self.collection.find("Nero"), -1)

    def test_sort(self):
        self.collection.sort("price")
        self.assertTrue(
            self.collection[0].get_price() <= self.collection[1].get_price())

    def test_delete(self):
        collection = Collection(Hotel, self.path)
        collection.delete(9999)
        self.assertEqual(len(collection), 2)

        id = collection[0].get_ID()
        collection.delete(id)
        self.assertTrue(len(collection) == 1 and collection[0].get_ID != id)

    def test_add(self):
        collection = Collection(Hotel)
        collection.add(
            "C:/python_learn_lnu/programming/prog_3/data/testData.json")
        self.assertEqual(len(collection), 1)

        self.assertEqual(collection.add(self.invalid_path), -1)

    def test_change(self):
        collection = Collection(Hotel, self.path)
        id = collection[0].get_ID()
        collection.change(
            id, "C:/python_learn_lnu/programming/prog_3/data/testData.json")
        self.assertEqual(collection[0].get_guest_name(), "Levi")

        self.assertEqual(collection.change(id, self.invalid_path), -1)

    def test_find_by_ID(self):
        id = self.collection[0].get_ID()
        self.assertEqual(self.collection.find_item_by_ID(id),
                         self.collection[0])

    def test_set_items_from_file(self):
        collection = Collection(Hotel)
        self.assertEqual(collection.set_items_from_file(self.invalid_path), -1)

        collection.set_items_from_file(self.path)
        self.assertEqual(len(collection), 2)
        self.assertEqual(collection[0].get_guest_name(), "Jean")

    def test_save(self):
        memento = self.collection.save()
        self.assertTrue(isinstance(memento, Memento))

    def test_str(self):
        jsonCollection = '''[
  {
    "_Hotel__ID": 1,
    "_Hotel__checkin_datetime": "01.01.2000",
    "_Hotel__checkout_datetime": "01.01.2001",
    "_Hotel__city": "Berlin",
    "_Hotel__booking_number": "AS123123",
    "_Hotel__guest_name": "Avilio",
    "_Hotel__price": 200
  },
  {
    "_Hotel__ID": 0,
    "_Hotel__checkin_datetime": "01.01.2000",
    "_Hotel__checkout_datetime": "01.01.2001",
    "_Hotel__city": "Rome",
    "_Hotel__booking_number": "AS123123",
    "_Hotel__guest_name": "Jean",
    "_Hotel__price": 500
  }
]'''
        self.assertEqual(jsonCollection, self.collection.__str__())

    def test_len(self):
        self.assertEqual(self.collection.__len__(), 2)

    def test_get_item(self):
        print(self.collection[8])
        self.assertTrue(isinstance(self.collection[0], Hotel))


if __name__ == "__main__":
    main()
