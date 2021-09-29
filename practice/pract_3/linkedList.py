from validation import Validation
from random import randint


class Node:
    def __init__(self, data, pNext=None):
        self.data = data
        self.pNext = pNext


class LinkedList:
    size = 0
    head = None

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        Validation.isInteger(index)
        current = self.head
        i = 0
        while current != None:
            if i == index:
                return current.data
            current = current.pNext
            i += 1

    def getSize(self):
        return self.size

    def pop(self):
        self.remove(self.size - 1)

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.pNext != None:
                current = current.pNext
            current.pNext = Node(data)
        self.size += 1

    def shift(self):
        if self.head == None:
            return
        self.head = self.head.pNext
        self.size -= 1

    def unshift(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def remove(self, index):
        if index > self.size:
            return

        if index == 0:
            self.shift()
            return

        current = self.head
        for i in range(index - 1):
            current = current.pNext

        current.pNext = current.pNext.pNext
        self.size -= 1

    def insert(self, data, index):
        if index > self.size:
            return

        if index == 0:
            self.unshift(data)
            return

        current = self.head
        for i in range(index - 1):
            current = current.pNext

        current.pNext = Node(data, current.pNext)
        self.size += 1

    def getDataFromKeyboard(self, count):
        Validation.isInteger(count)
        for i in range(count):
            data = input()
            self.push(data)

    def generateDataInRange(self, a, b, count):
        Validation.isInteger(a)
        Validation.isInteger(b)
        Validation.isInteger(count)
        if a > b:
            a, b = b, a
        for i in range(count):
            self.push(randint(a, b))

    def show(self):
        for i in range(self.size):
            print(self[i])

    def getCountOfUniqieElems(self):
        arrOfUnique = []
        for i in range(len(self)):
            if not self[i] in arrOfUnique:
                arrOfUnique.append(self[i])

        return len(arrOfUnique)