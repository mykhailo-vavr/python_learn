import sys
import json

sys.path.append('c:\\python_learn_lnu\\practice\\pract_3')

from logger import Logger


class Change():
    def __init__(self, name, options):
        self.name = name
        self.options = options

    def __str__(self) -> str:
        return json.dumps(vars(self), indent=2)


class Event():
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def fire(self, change):
        for observer in self.observers:
            observer.update(change)


class Observer():
    path = "practice\pract_3\data\outputData.json"
    events = {"add": Logger.printToFile, "remove": Logger.printToFile}

    def update(self, change):
        item = self.events.get(change.name)
        if not item:
            return -1
        item(self.path, change)
