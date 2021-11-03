from mainClasses.hotel import Hotel
from patterns.memento.memento import Caretaker
from supportClasses.collection import Collection
from supportClasses.funcForOptions import FuncForOptions

# use for input "C:/python_learn_lnu/programming/prog_3/data/testData.json"
# use for output "C:/python_learn_lnu/programming/prog_3/data/outputData.json"
# use to fill collection "C:/python_learn_lnu/programming/prog_3/inputData/data.json"


def options(option, collection, caretaker):
    functions = FuncForOptions(collection, caretaker)
    return {
        "1": functions.f1,
        "2": functions.f2,
        "3": functions.f3,
        "4": functions.f4,
        "5": functions.f5,
        "6": functions.f6,
        "7": functions.f7,
        "8": functions.f8,
        "9": functions.f9,
        "10": functions.f10,
        "0": functions.f0,
    }.get(option)


def start(collection, caretaker):
    print("""
Choose the option:
    1. Find data in collection
    2. Sort collection
    3. Delete item in collection
    4. Add item in collection
    5. Set new values to item
    6. Show collection

    7. Save changes
    8. Undo changes
    9. Redo changes
    10. Show states
    0. Exit
    """)

    option = input()
    method = options(option, collection, caretaker)
    if method:
        method()
    else:
        print("Choose correct option")
        start(collection, caretaker)
    start(collection, caretaker)


if __name__ == "__main__":
    path = "C:/python_learn_lnu/programming/prog_3/data/inputData.json"
    collection = Collection(Hotel, path)
    caretaker = Caretaker(collection)

    start(collection, caretaker)
