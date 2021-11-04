class FuncForOptions:
    def __init__(self, collection):
        self.collection = collection

    @staticmethod
    def getId(methodName):
        print(f"Id for {methodName}:")
        id = input()
        return id

    def f1(self):
        self.collection.show()

    def f2(self):
        self.collection.show_hour_with_largest_order()

    def f3(self):
        print("Write point")
        point = input()
        print("Write path")
        path = input()
        self.collection.write_point_with_largest_order(point, path)

    def f0(self):
        exit()