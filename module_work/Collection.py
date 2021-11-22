import json
from Validation import Validation as V


class Collection:
    def __init__(self, instance, path=None):
        self.instance = instance
        self.collection = []
        self.uniqueNames = []
        if path:
            self.set_items_from_file(path)

    def set_valid_data(self, set_func, *args):
        value = self.get_data_from_keyboard(
            f"value in {set_func.__name__} method")
        getattr(self, f"{set_func.__name__}")(value, *args)

    def get_data_from_keyboard(self, message):
        print(f"Incorrect {message}")
        return input()

    def find(self, value):
        foundItems = []
        for item in self.collection:
            if str(item).find(str(value)) != -1:
                foundItems.append(item)

        if len(foundItems) > 0:
            return foundItems

        return -1

    def find_item_by_ID(self, id):
        for item in self.collection:
            if item.get_ID() == id:
                self.item = item
                return item
        return None

    def count_item_by_point_and_hour(self, point, time):
        count = 0
        for item in self.collection:
            if item.get_point() == point and item.get_time():
                count += 1

    def show_hour_with_largest_order(self):
        arr = []
        arr1 = [None] * 99
        for item in self.collection:
            if item.get_time() not in arr:
                arr.append(item)

    def check_item(self, item):
        name = item.get_name()
        if name in self.uniqueNames:
            print(f"There is someone with name {name}")
            return False
        self.uniqueNames.append(name)

        time = item.get_time()
        point = item.get_point()
        if self.count_item_by_point(point, time) > 20:
            print(f"Too many people in point {point} in date {time}")

    def write_to_file(self, path, item):
        try:
            with open(path, "w") as file:
                file.write(str(item))
        except:
            return -1

    def set_items_from_file(self, path):
        data = self.instance.get_data_from_file(self.instance, path)

        if data == -1:
            return -1

        for obj in data["items"]:
            tempItem = self.instance()
            for key, value in obj.items():
                getattr(tempItem, f"set_{key}")(value)
            tempItem.set_empty_values()
            # if self.checkItem(tempItem):
            self.collection.append(tempItem)

    def show(self):
        print(self)

    def __str__(self):
        return json.dumps([obj.__dict__ for obj in self.collection], indent=2)

    def __len__(self):
        return len(self.collection)

    @V.isIntegerInRange(-1)
    def __getitem__(self, index):
        if index >= len(self.collection):
            return -1
        return self.collection[index]