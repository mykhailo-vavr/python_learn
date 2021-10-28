from unittest import TestCase, main
import sys

sys.path.append('c:\\python_learn_lnu\\programming\\prog_3')
from supportClasses.collection import Collection
from mainClasses.hotel import Hotel
from patterns.memento.memento import Memento, Caretaker


class TestMemento(TestCase):
    path = "C:/python_learn_lnu/programming/prog_3/data/data.json"

    def test_init(self):
        collection = Collection(Hotel, self.path)
        caretaker = Caretaker(collection)

        self.assertEqual(caretaker.originator, collection)
        self.assertEqual(len(caretaker.states), 0)
        self.assertEqual(caretaker.statesPosition, -1)

    def test_addMemento(self):
        collection = Collection(Hotel, self.path)
        caretaker = Caretaker(collection)

        caretaker.addMemento()
        self.assertEqual(caretaker.statesPosition, 0)

        collection.save = None
        self.assertEqual(caretaker.addMemento(), -1)

    def test_undo(self):
        collection = Collection(Hotel, self.path)
        caretaker = Caretaker(collection)

        self.assertEqual(caretaker.undo(), -1)
        caretaker.addMemento()
        caretaker.addMemento()
        caretaker.undo()
        self.assertEqual(caretaker.states[caretaker.statesPosition],
                         caretaker.states[0])

        collection.load = None
        self.assertEqual(caretaker.undo(), -1)

    def test_redo(self):
        collection = Collection(Hotel, self.path)
        caretaker = Caretaker(collection)

        self.assertEqual(caretaker.redo(), -1)
        caretaker.addMemento()
        caretaker.addMemento()
        caretaker.undo()
        caretaker.redo()
        self.assertEqual(caretaker.states[caretaker.statesPosition],
                         caretaker.states[1])

        collection.redo = None
        self.assertEqual(caretaker.redo(), -1)

    def test_get_state(self):
        caretaker = Caretaker(Collection(Hotel, self.path))
        caretaker.addMemento()
        self.assertTrue(caretaker.states[0].getState())


if __name__ == "__main__":
    main()
