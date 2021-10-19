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
        memento = self.originator.save()
        self.states.append(memento)
        self.statesPosition = len(self.states) - 1

    def undo(self):
        if len(self.states) == 0:
            return print("There are no saves")

        if self.statesPosition == 0:
            return print("You are already up to date with first save")

        self.statesPosition -= 1
        memento = copy.deepcopy(self.states[self.statesPosition].getState())
        self.originator.load(memento)

    def redo(self):
        if len(self.states) == 0:
            return print("There are no saves")

        if len(self.states) - 1 == self.statesPosition:
            return print("You are already up to date with last changes")

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
