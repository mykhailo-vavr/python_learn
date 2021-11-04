class FuncForOptions:
    def __init__(self, collection, caretaker):
        self.collection = collection
        self.caretaker = caretaker

    @staticmethod
    def getId(methodName):
        print(f"Id for {methodName}:")
        id = input()
        return id

    @staticmethod
    def getPath(message):
        print(f"{message}")
        return input()

    def askForPath(self, message):
        print(f"{message}\nIf you want, print 'y'")
        if input() == "y":
            return True
        return False

    def f1(self):
        print("String for find:")
        str = input()
        for item in self.collection.find(str):
            print(item)

    def f2(self):
        print("Attribute for sort:")
        attr = input()
        self.collection.sort(attr)

    def f3(self):
        id = self.getId("delete")
        path = ""
        if self.askForPath("Do you want to output data?"):
            path = self.getPath("Write path to output data:")
        self.collection.delete(id, path)

    def f4(self):
        inPath = self.getPath("Write path to input data:")
        outPath = ""
        # if self.askForPath("Do you want to output data?"):
        outPath = self.getPath("Write path to output data:")
        self.collection.add(inPath, outPath)

    def f5(self):
        id = self.getId("change")
        inPath = self.getPath("Write path to input data:")
        outPath = ""
        # if self.askForPath("Do you want to output data?"):
        outPath = self.getPath("Write path to output data:")
        self.collection.change(id, inPath, outPath)

    def f6(self):
        self.collection.show()

    def f7(self):
        self.caretaker.addMemento()

    def f8(self):
        self.caretaker.undo()

    def f9(self):
        self.caretaker.redo()

    def f10(self):
        self.caretaker.show()

    def f0(self):
        exit()