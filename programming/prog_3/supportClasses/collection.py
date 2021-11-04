from os import write
import sys

sys.path.append('c:\\python_learn_lnu\\programming\\prog_3\\')

from supportClasses.validation import Validation as V
from patterns.memento.memento import Memento
import copy
import json
import os.path


class Collection:
    def __init__(self, instance, inPath=None, outPath=None):
        self.instance = instance
        self.collection = []
        self.outPath = outPath
        if inPath:
            self.set_items_from_file(inPath)

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

    def sort(self, value):
        try:
            if self.collection[0]:
                a = getattr(self.collection[0], f"get_{value}")()
            else:
                return print("Collection is empty")
        except:
            return print("Invalid parameter for sort")
        # case insensitive sort
        self.collection.sort(key=lambda x: str(getattr(x, f"get_{value}")
                                               ()).lower(),
                             reverse=False)

    @V.isIntegerInRange(-1)
    def delete(self, id, path=""):
        item = self.find_item_by_ID(id)
        if item:
            self.collection.remove(item)
        else:
            print(f"There is no item with id: {id}")

        if path:
            # self.write_item_to_file(path, copy.copy(item))
            self.write_collection_to_file(path)
            self.outPath = path

    def add(self, inputPath, outputPath=""):
        tempItem = self.instance()
        if tempItem.get_data_from_file(inputPath) == -1:
            print("Invalid path")
            return -1

        tempItem.set_data_from_file(inputPath)

        # if outputPath:
        #     self.write_item_to_file(
        #         outputPath,
        #         copy.copy(tempItem),
        #     )
        self.collection.append(tempItem)
        if outputPath:
            self.write_collection_to_file(outputPath)
            self.outPath = outputPath

    @V.isIntegerInRange(-1)
    def change(self, id, inputPath, outputPath=""):
        item = self.find_item_by_ID(id)
        if item.get_data_from_file(inputPath) == -1:
            print("Invalid path")
            return -1

        if item:
            item.set_data_from_file(inputPath)
        else:
            print(f"There is no item with id: {id}")
            return -1

        if outputPath:
            # self.write_item_to_file(outputPath, copy.copy(item))
            self.write_collection_to_file(outputPath)
            self.outPath = outputPath

    def find_item_by_ID(self, id):
        for item in self.collection:
            if item.get_ID() == id:
                self.item = item
                return item
        return None

    def write_item_to_file(self, path, item):
        if not os.path.exists(path):
            print(f"File with path {path} does not exist")
            return
        try:
            with open(path, "w") as file:
                file.write(str(item))
        except:
            return -1

    def write_collection_to_file(self, path):
        if not os.path.exists(path):
            print(f"File with path {path} does not exist")
            return
        try:
            with open(path, "w") as file:
                file.write(str(self))
        except:
            return -1

    # maybe unnecessary method
    def write_to_file(self, path, json):
        if not os.path.exists(path):
            print(f"File with path {path} does not exist")
            return
        try:
            with open(path, "w") as file:
                file.write(json)
        except:
            return -1

    def get_data_from_file(self, path):
        try:
            with open(path) as file:
                data = json.load(file)
        except:
            return -1
        return data

    def get_json_from_file(self, path):
        data = self.get_data_from_file(path)
        if data == -1:
            return -1
        return json.dumps(data["items"], indent=2)

    def set_items_from_file(self, path):
        data = self.get_data_from_file(path)

        if data == -1:
            return -1

        for obj in data["items"]:
            tempItem = self.instance()
            for key, value in obj.items():
                getattr(tempItem, f"set_{key}")(value)
            tempItem.set_empty_values()
            self.collection.append(tempItem)

    def show(self):
        print(self)

    def save(self):
        # return Memento({
        #     "collection": copy.deepcopy(self.collection),
        #     "dataFromFile": self.get_json_from_file(self.outPath)
        # })
        return Memento(copy.deepcopy(self.collection))

    def load(self, state):
        # self.collection = state.get("collection")
        # self.write_collection_to_file(self.outPath, state.get("dataFromFile"))
        self.collection = state
        self.write_collection_to_file(self.outPath)

    def __str__(self):
        return json.dumps([obj.__dict__ for obj in self.collection], indent=2)

    def __len__(self):
        return len(self.collection)

    @V.isIntegerInRange(-1)
    def __getitem__(self, index):
        if index >= len(self.collection):
            return -1
        return self.collection[index]
