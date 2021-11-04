from validation import Validation as V
from patterns.observer.observer import Change, Event, Observer


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
    def __init__(self):
        self.size = 0
        self.head = None
        self.dataGetter = None

        self.event = Event()
        self.event.subscribe(Observer())

    def __iter__(self):
        return LinkedListIterator(self)

    def __len__(self):
        return self.size

    def __str__(self):
        data = []
        for item in self:
            data.append(item)
        return str(data)

    @V.isIntegerInRange(-1)
    def __getitem__(self, index):
        current = self.head
        i = 0
        while current != None:
            if i == index:
                return current.data
            current = current.pNext
            i += 1

    def setDataGetter(self, dataGetter):
        self.dataGetter = dataGetter

    @V.isIntegerInRange(-1)
    def setData(self, index):
        if not self.dataGetter:
            return print("No dataGetter selected")

        listBeforeChanges = str(self)

        data = self.dataGetter.getData()
        if not data:
            return print("Invalid data")

        for i in range(len(data)):
            if not self.insert(data[i], index + i):
                return print(f"Impossible to set data with index {index}")

        listAfterChanges = str(self)
        self.event.fire(
            Change(
                "add", {
                    "listBeforeChanges": listBeforeChanges,
                    "positionOfInsert": index,
                    "listAfterChanges": listAfterChanges
                }))

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

    @V.isIntegerInRange(-1)
    def remove(self, index):
        if index > self.size:
            print(f"There is no elem with index {index}")
            return

        listBeforeChanges = str(self)

        if index == 0:
            self.shift()
        else:
            current = self.head
            for i in range(index - 1):
                current = current.pNext
            current.pNext = current.pNext.pNext
            self.size -= 1

        listAfterChanges = str(self)
        self.event.fire(
            Change(
                "add", {
                    "listBeforeChanges": listBeforeChanges,
                    "positionOfDelete": index,
                    "listAfterChanges": listAfterChanges
                }))

    def removeInRange(self, a, b):
        if a > b:
            a, b = b, a

        count = b - a + 1

        listBeforeChanges = str(self)
        for i in range(count):
            self.remove(a)

        listAfterChanges = str(self)
        self.event.fire(
            Change(
                "add", {
                    "listBeforeChanges": listBeforeChanges,
                    "rangeOfDelete": [a, b],
                    "listAfterChanges": listAfterChanges
                }))

    @V.isIntegerInRange(0)
    def insert(self, data, index):
        if index > self.size:
            return print(f"Impossible to insert in index {index}")
        listBeforeChanges = str(self)

        if index == 0:
            self.unshift(data)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.pNext
            current.pNext = Node(data, current.pNext)
            self.size += 1

        listAfterChanges = str(self)

        self.event.fire(
            Change(
                "add", {
                    "listBeforeChanges": listBeforeChanges,
                    "positionOfInsert": index,
                    "listAfterChanges": listAfterChanges
                }))

        return 1

    def show(self):
        print("------ List ------")
        if not self.size:
            return print("List is empty\n------------------")

        print(self)

        print("------------------")

    def getCountOfUniqueElems(self):
        arrOfUnique = []
        for i in range(len(self)):
            if not self[i] in arrOfUnique:
                arrOfUnique.append(self[i])

        return len(arrOfUnique)
