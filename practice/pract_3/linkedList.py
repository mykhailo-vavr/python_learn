from validation import Validation as V
from random import randint


class LinkedListIterator():
    def __init__(self, list):
        self.__list = list
        self.__start = 0
        self.__end = len(list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start >= self.__end:
            raise StopIteration

        self.__start += 1
        return self.__list[self.__start - 1]


class Node:
    def __init__(self, data, pNext=None):
        self.data = data
        self.pNext = pNext


class LinkedList:
    size = 0
    head = None

    def __iter__(self):
        return LinkedListIterator(self)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        V.isInteger(index)
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
        if V.isInRange(0, self.size) or not V.isInteger(index):
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
        if V.isInRange(0, self.size) or not V.isInteger(index):
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
        if not V.isInteger(count) or not V.isInRange(count, 0):
            return
        for i in range(count):
            data = input()
            self.push(data)

    def generateDataInRange(self, a, b, count):
        if not V.isInteger(a) or not V.isInteger(b) \
                or not V.isInteger(count) or not V.isInRange(count, 0):
            return
        if a > b:
            a, b = b, a
        for i in range(count):
            self.push(randint(a, b))

    def getDataFromKeyboardGenerator(self, count):
        if not V.isInteger(count) or not V.isInRange(count, 0):
            return
        for i in range(count):
            yield input()

    def generateDataInRangeGenerator(self, a, b, count):
        if not V.isInteger(a) or not V.isInteger(b) \
                or not V.isInteger(count) or not V.isInRange(count, 0):
            return
        if a > b:
            a, b = b, a
        for i in range(count):
            yield randint(a, b)

    def show(self):
        for item in self:
            print(item)

    def getCountOfUniqieElems(self):
        arrOfUnique = []
        for i in range(len(self)):
            if not self[i] in arrOfUnique:
                arrOfUnique.append(self[i])

        return len(arrOfUnique)
