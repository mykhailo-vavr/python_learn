import copy
import json


class Memento:
    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state

    def __str__(self):
        return json.dumps([obj.__dict__ for obj in self.state], indent=2)


class Caretaker:
    def __init__(self, originator):
        self.originator = originator
        self.states = []
        self.statesPosition = -1

    def addMemento(self):
        if not self.originator.save:
            return -1

        memento = self.originator.save()
        self.states.append(memento)
        self.statesPosition = len(self.states) - 1

    def undo(self):
        if len(self.states) == 0:
            print("There are no saves")
            return -1

        if self.statesPosition == 0:
            print("You are already up to date with first save")
            return -1

        if not self.originator.load:
            return -1

        self.statesPosition -= 1
        memento = copy.deepcopy(self.states[self.statesPosition].getState())
        self.originator.load(memento)

    def redo(self):
        if len(self.states) == 0:
            print("There are no saves")
            return -1

        if len(self.states) - 1 == self.statesPosition:
            print("You are already up to date with last changes")
            return -1

        if not self.originator.load:
            return -1

        self.statesPosition += 1
        memento = copy.deepcopy(self.states[self.statesPosition].getState())
        self.originator.load(memento)

    def show(self):
        if not self.states:
            return print("There is no saves")

        i = 0
        for state in self.states:
            print(f"------- State {i} -------")
            print(state, "\n")
            i += 1
        print(f"------- States position: {self.statesPosition} -------")
