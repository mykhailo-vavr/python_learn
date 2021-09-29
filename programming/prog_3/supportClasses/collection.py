from programming.prog_3.supportClasses.validation import Validation
import json


class Collection:
    list = []

    def __init__(self, instance):
        self.instance = instance

    def find(self, value):
        str(value)
        isFind = False
        print("Objects with coincidence:")
        for item in self.list:
            if str(item).find(value) != -1:
                print(item)
                isFind = True
        if not isFind:
            print("Oops, there is no coincidence")

    def sort(self, value):
        str(value)
        self.list.sort(key=lambda x: getattr(x, f"get_{value}")(), reverse=False)

    def delete(self, id, path=""):
        Validation.isInteger(id)
        Validation.isInRange(id, 0)
        item = self.find_item_by_ID(id)
        if path:
            self.write_to_file(item, path)
        if item:
            self.list.remove(item)


    def add(self, pathToInput, pathToOutput=""):
        tempItem = self.instance()
        tempItem.set_data_from_file(pathToInput)
        if pathToOutput:
            self.write_to_file(tempItem, pathToOutput)
        self.list.append(tempItem)

    def change(self, id, inputPath, outputPath=""):
        Validation.isInteger(id)
        Validation.isInRange(id, 0)
        item = self.find_item_by_ID(id)
        if item:
            item.set_data_from_file(inputPath)
        if outputPath:
            self.write_to_file(item, outputPath)

    def find_item_by_ID(self, id):
        for item in self.list:
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
            self.list.append(tempItem)

    def show(self):
        print(self)

    def __str__(self):
        return json.dumps([obj.__dict__ for obj in self.list], indent=2)

    def __getitem__(self, value):
        Validation.isInteger(value)
        return list[value]
