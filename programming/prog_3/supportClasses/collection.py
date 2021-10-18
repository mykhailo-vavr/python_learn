from supportClasses.validation import Validation as V
import json


class Collection:
    collection = []

    def __init__(self, instance):
        self.instance = instance

    def set_valid_data(self, set_func, *args):
        value = self.get_data_from_keyboard(
            f"value in {set_func.__name__} method")
        getattr(self, f"{set_func.__name__}")(value, *args)

    def get_data_from_keyboard(self, message):
        print(f"Incorrect {message}")
        return input()

    def find(self, value):
        str(value)
        isFind = False
        print("Objects with coincidence:")
        for item in self.collection:
            if str(item).find(value) != -1:
                print(item)
                isFind = True
        if not isFind:
            print("Oops, there is no coincidence")

    def sort(self, value):
        str(value)
        self.collection.sort(key=lambda x: getattr(x, f"get_{value}")(),
                             reverse=False)

    @V.isIntegerInRange(-1)
    def delete(self, id, path=""):
        item = self.find_item_by_ID(id)
        if path:
            self.write_to_file(item, path)
        if item:
            self.collection.remove(item)
        else:
            print(f"There is no item with id: {id}")

    def add(self, pathToInput, pathToOutput=""):
        tempItem = self.instance()
        tempItem.set_data_from_file(pathToInput)
        if pathToOutput:
            self.write_to_file(tempItem, pathToOutput)
        self.collection.append(tempItem)

    @V.isIntegerInRange(-1)
    def change(self, id, inputPath, outputPath=""):
        item = self.find_item_by_ID(id)
        if item:
            item.set_data_from_file(inputPath)
        else:
            print(f"There is no item with id: {id}")

        if outputPath:
            self.write_to_file(item, outputPath)

    def find_item_by_ID(self, id):
        for item in self.collection:
            if item.get_ID() == id:
                self.item = item
                return item

    @classmethod
    def write_to_file(cls, path, item):
        try:
            with open(path, "w") as file:
                file.write(str(item))
        except:
            raise FileExistsError("Error on file reading")

    def set_items_from_file(self, path):
        data = self.instance.get_data_from_file(self.instance, path)

        for obj in data["items"]:
            tempItem = self.instance()
            for key, value in obj.items():
                getattr(tempItem, f"set_{key}")(value)
            tempItem.set_empty_values()
            self.collection.append(tempItem)

    def show(self):
        print(self)

    def __str__(self):
        return json.dumps([obj.__dict__ for obj in self.collection], indent=2)

    @V.isIntegerInRange(-1)
    def __getitem__(self, value):
        return self.collection[value]
